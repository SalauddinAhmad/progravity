# Plugin System

Community extensions for PROGRAVITY. Each plugin is a self-contained skill
that loads on top of the base PROGRAVITY protocol.

---

## Available Plugins

| Plugin | Purpose | Load When |
|--------|---------|-----------|
| [progravity-security](./progravity-security/SKILL.md) | Deep security review mode | Working on auth, input, db, API |
| [progravity-perf](./progravity-perf/SKILL.md) | Performance analysis mode | Optimizing hot paths, benchmarking |
| [progravity-typescript](../skills/progravity-typescript/SKILL.md) | TypeScript patterns | Any TypeScript project |
| [progravity-python](../skills/progravity-python/SKILL.md) | Python patterns | Any Python project |

---

## How to Use a Plugin

Add to your `GEMINI.md` or `AGENTS.md`:

```
When executing coding tasks, follow PROGRAVITY from skills/progravity/SKILL.md.
For security-related tasks, also load plugins/progravity-security/SKILL.md.
```

Or reference directly in your task:

```
Review this auth module for security issues.
Load: skills/progravity/SKILL.md + plugins/progravity-security/SKILL.md
```

---

## Build Your Own Plugin

A PROGRAVITY plugin is any markdown file with YAML frontmatter:

```markdown
---
name: progravity-[your-domain]
description: One-line description of what this plugin adds.
triggers:
  - keyword1
  - keyword2
---

# PROGRAVITY — [Domain] Extension

Extends base PROGRAVITY with [domain]-specific patterns.
Load `skills/progravity/SKILL.md` first, then this file.

## [Domain] Recon Additions
[what to check beyond standard recon]

## [Domain] Verification
[additional checks beyond standard verify chain]

## [Domain] Anti-Patterns
[domain-specific anti-patterns]

## [Domain] Patterns
[domain-specific best practices]
```

### Plugin Rules
1. Plugins extend — never override — base PROGRAVITY rules
2. All 5 core rules still apply
3. Tier classification still applies
4. VERDICT: PASS/FAIL still required
5. Plugins add recon, patterns, and verification — not new rule systems

### Submitting a Plugin

1. Create `plugins/progravity-[name]/SKILL.md`
2. Test it on 3+ real tasks (include evidence in PR)
3. Add to the table in this README
4. PR with `VERDICT: PASS` in description

---

## Plugin Ideas (open for contribution)

- `progravity-go` — Go-specific patterns (goroutines, channels, defer)
- `progravity-rust` — Rust patterns (lifetimes, ownership, unsafe)
- `progravity-react` — React patterns (hooks, state, effect cleanup)
- `progravity-sql` — Schema migration and query optimization
- `progravity-docker` — Container and orchestration patterns
- `progravity-api` — REST/GraphQL API design patterns
- `progravity-mobile` — React Native / Flutter patterns
- `progravity-ml` — ML/AI model training and evaluation patterns
