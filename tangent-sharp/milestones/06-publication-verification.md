# Milestone 6: final publication copy verified

The standalone publication copy was prepared under `tangent-limit/` on a fresh
`codex/tangent-limit` branch for the supplied GitHub repository. The repository
was empty when inspected, so no existing files or history were replaced.

All eight final Lean source modules were rebuilt in a fresh project build
directory using the exact pinned mathlib package cache. The complete build
passed cleanly, and `scripts/TheoremInventory.lean` audited all 37 declarations.
Only `propext`, `Classical.choice`, and `Quot.sound` occur; the source scan found
no proof placeholder or added axiom declaration. See `logs/final-build.log`,
`logs/final-theorem-inventory.log`, and `logs/source-audit.log`.

The π-approximation hypothesis remains explicit and unproved. Both positive
integer limit and absolute-series statements actually compiled. No GitHub CI
execution is claimed; these are executed local build and audit results.

Reproduction helpers were made portable by using an explicit or project-local
Elan installation and relative checkpoint checksum filenames. A relocated
checkpoint passed checksum verification. The Lean proof source itself was
unchanged from the earlier passing project.

The staged publication subset was inspected for credentials, private
configuration, unrelated data, caches, downloaded dependencies, temporary files,
and binary session archives before committing. Relevant source attribution and
ordinary proof reference notes were retained, with their verification scope
stated. The original full working-session artifacts remain local.
