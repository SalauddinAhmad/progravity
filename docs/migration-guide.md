# Migrating to PROGRAVITY

Start with **Core**. It is project-local, portable, and reversible:

```bash
npx skills add SalauddinAhmad/progravity --skill progravity --agent antigravity --yes
```

Then use it on one bounded task and inspect the result. Keep project-specific rules that do not conflict with its read-before-write and evidence policies.

Choose **Native** only when you want Antigravity hook-based workflow checks. It is a separate plugin rather than a replacement for Core. Follow [install.md](install.md) and use `agy plugin uninstall progravity-native` to remove it.

PROGRAVITY does not replace Antigravity permissions, sandboxing, review, or CI.
