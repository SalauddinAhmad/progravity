# Progravity OpenCode Adapter

First-class OpenCode support via native surfaces: AGENTS.md invariants,
Agent Skills, custom agents, `permission` configuration, and a JS plugin
shim (`tool.execute.before`) backed by the same Python policy engine as
Antigravity. Installed and verified against OpenCode 1.18.x (`permission`
schema). OpenCode v2 uses a different `permissions`-array schema; see
"Capability differences".

## What `progravity init --host opencode` installs

- `.agents/skills/progravity/` + `progravity-highstakes/` (shared with Antigravity discovery)
- `.opencode/agents/{investigator,reviewer,impact-auditor,test-adversary}.md`
- `.opencode/plugins/progravity.js` (enforcement shim)
- `opencode.json` permission profile (merged, never clobbered; unparseable
  configs and `opencode.jsonc`-only projects are left untouched with a
  `warnings` entry for manual merge)
- `AGENTS.md` invariant block (idempotent markers)
- `.progravity/opencode-contract.json` (workspace contract for the shim)

## Capability differences (honest)

- No lifecycle hooks: OpenCode has `tool.execute.before` (block by
  throwing) but no Stop-gate equivalent. Completion gating runs manually
  via `progravity summarize` + validator evidence, not automatic denial.
- `force_ask` resolves to hard deny in the shim (no ask channel).
- Evidence ledger integration is manual (`progravity validator`, `progravity
  repro`); the shim enforces policy only, it does not record sessions.
- The shim shells to `progravity guard` (python3 required). If unreachable,
  calls are allowed with a logged warning -- run `progravity doctor`.
- Session isolation is per-workspace-contract, not per-conversation.
