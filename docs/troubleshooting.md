# Troubleshooting

For the tested commands, see [install.md](install.md).

| Symptom | Check | Resolution |
|---|---|---|
| `npx` is not found | `node --version` and `npm --version` | Install a current Node.js/npm release, then rerun the Core install command. |
| Core is not visible | `python3 .agents/skills/progravity/scripts/doctor.py` | Confirm the command was run from the project where you use Antigravity. Start a new conversation and ask which skills are available. |
| `agy` is not found | `agy --version` | Follow [Google’s CLI installation guide](https://antigravity.google/docs/cli/install/) and ensure the installed binary directory is on `PATH`. |
| Native is not listed | `agy plugin validate "$PWD/dist/progravity-antigravity"` | Rebuild with `bash scripts/build-native-bundle.sh`, validate the bundle, then install the absolute bundle path. |
| Hooks are not shown | `/hooks` in a new `agy` TUI session | Confirm `agy plugin list` includes `progravity-native`; restart the CLI session after installation. |

Do not manually delete broad Antigravity configuration directories. Remove Native
with `agy plugin uninstall progravity-native`; Core removal is documented in
[install.md](install.md).

## Runtime failure modes

| Symptom | Check | Resolution |
|---|---|---|
| `progravity doctor` fails after `pip install` | run it outside the repo checkout | Reinstall; `mode` must be `installed`. If `unresolved`, the wheel lacks `share/progravity` assets. |
| Stop gate loops `continue` after edits | `progravity explain --session-dir <dir>` | Evidence predating the final mutation is stale by design; re-run validators after the last edit. |
| `force_ask` on every `mv`/infra command | expected policy | Destructive capability requires confirmation (Antigravity) or is hard-denied (OpenCode shim). Narrow the command or amend scope. |
| OpenCode shim allows everything | `progravity guard` manually | `progravity`/python3 missing from PATH degrades to allow-with-warning. Install both; check `progravity doctor`. |
| `progravity init` skipped files | `installed` vs `skipped` in output | Existing files are never overwritten. Diff and merge manually. |
| `progravity bench run` exits 2 | output JSON | No model credentials: episode recorded INVALID (infrastructure), not a solver failure. |
| Hook denies a legitimate write | `allowed_write_scope` in contract | Read the file first (Rule 1), confirm scope covers it, or amend the contract. |
