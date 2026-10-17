"""Packaging integrity: the wheel must ship the runtime the CLI checks."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python < 3.11
    import tomli as tomllib

ROOT = Path(__file__).parents[1]


class PackagingTests(unittest.TestCase):
    def test_data_files_cover_doctor_assets(self):
        pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text())
        patterns = [
            pattern
            for group in pyproject["tool"]["setuptools"]["data-files"].values()
            for pattern in group
        ]
        shipped = set()
        for pattern in patterns:
            shipped.update(str(path.relative_to(ROOT)) for path in ROOT.glob(pattern))
        for asset in [
            "plugins/progravity-antigravity/plugin.json",
            "plugins/progravity-antigravity/hooks.json",
            "plugins/progravity-antigravity/scripts/pre_tool.py",
            "plugins/progravity-antigravity/scripts/stop_gate.py",
            "plugins/progravity-antigravity/scripts/evidence_chain.py",
            "plugins/progravity-antigravity/scripts/validator_runner.py",
            "plugins/progravity-antigravity/scripts/progravity_action.py",
            "plugins/progravity-antigravity/scripts/progravity_policy.py",
            "skills/progravity/SKILL.md",
            "skills/progravity/SESSION_FAILURES.md",
            "skills/progravity-highstakes/SKILL.md",
            "plugins/progravity-antigravity/rules/progravity-invariants.md",
            "adapters/opencode/contract-template.json",
            "adapters/opencode/plugin/progravity.js",
            "adapters/opencode/permissions/balanced.json",
        ]:
            self.assertIn(asset, shipped, f"wheel data-files omit {asset}")

    def test_doctor_passes_in_checkout(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "progravity_cli.py"), "doctor"],
            text=True,
            capture_output=True,
            cwd=ROOT,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        checks = json.loads(result.stdout)
        self.assertTrue(checks["mode"].startswith("checkout"))
        for key in ("skill", "plugin_manifest", "hooks", "evidence_chain"):
            self.assertTrue(checks[key], key)


if __name__ == "__main__":
    unittest.main()
