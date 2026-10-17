# Quickstart

Progravity in 60 seconds, per host. Research preview: comparative
performance is not yet measured.

## Antigravity Core (portable skill, recommended start)

```bash
npx skills add SalauddinAhmad/progravity --skill progravity --agent antigravity --yes
python3 .agents/skills/progravity/scripts/doctor.py
```

Say: `Use Progravity to fix this bug and verify the result.`

## Antigravity Native (hook enforcement)

```bash
git clone --depth 1 https://github.com/SalauddinAhmad/progravity.git
cd Progravity
bash scripts/build-native-bundle.sh
agy plugin install "$PWD/dist/progravity-antigravity"
agy plugin validate "$PWD/dist/progravity-antigravity"
```

## OpenCode

Requires `progravity` on PATH (`pip install progravity`) and python3.

```bash
cd your-project
progravity init --host opencode --profile balanced
```

This installs the skills, least-privilege agents, the enforcement shim,
a permission profile, AGENTS.md invariants, and a workspace contract.
Verify with `progravity doctor`. Profiles: `fast`, `balanced`, `strict`.

## Verify it works

```bash
progravity doctor                                   # checkout/installed/project scopes
progravity decide --signals '{"trivial": true}'     # policy record
progravity validators --root . --depth targeted    # discovered validators
```

Next: `docs/concepts.md` for the model, `docs/hosts.md` for host differences.
