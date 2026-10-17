# PROGRAVITY — Antigravity Rules

When executing coding tasks, follow the PROGRAVITY skill loaded from `skills/progravity/SKILL.md`.

## Non-Negotiable (6 invariants -- canonical: `skills/progravity/SKILL.md`)

1. **Ground before mutating** -- read target + tests + callers before editing
2. **Stay in declared scope** -- writes outside `allowed_write_scope` denied
3. **Completion needs evidence** -- fresh Progravity-owned validator PASS only
4. **Never exact-retry a failure** -- change diagnosis, context, or strategy
5. **Satisfy the contract** -- criteria + required validators gate completion
6. **Say what you can't verify** -- mark unverifiable claims explicitly

## Tier Classification

Planning is conditional (`progravity decide --signals '{...}'`):
`direct` (trivial) / `compact` (dependent changes) / `deep` (security,
migration, broad blast radius) / `replan` (assumptions invalidated).
No universal ceremony. See `skills/progravity/SKILL.md` (canonical).

## Verification

Run these and cite the output:
- TypeScript: `tsc --noEmit && eslint . && vitest run`
- Python: `mypy . && ruff check . && pytest`
- Rust: `cargo check && cargo clippy && cargo test`
- Go: `go vet ./... && go test ./...`

## Output Format

```
## What Changed
[files, behavior]

## Evidence
[command output]

## Why
[rationale]
```

---

## Conditional Roles

Default to one agent. Load the investigator, verifier, or impact-auditor role
from `plugins/progravity-antigravity/agents/` only when its condition in
`skills/progravity/references/delegation.md` is met.

## Deep-Dive Resources

Load when complexity requires:
- `skills/progravity/resources/anti-rationalization.md` — defense against shortcuts
- `skills/progravity/resources/verification-engine.md` — proof-based verification
- `skills/progravity/resources/memory-protocol.md` — cross-session context
- `skills/progravity/resources/adversarial-critique.md` — attack your own plan
- `skills/progravity/resources/tool-orchestration.md` — tool patterns
- `skills/progravity/resources/gemini-native.md` — Gemini optimizations
