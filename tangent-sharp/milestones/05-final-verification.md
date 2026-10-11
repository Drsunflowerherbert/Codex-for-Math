# Milestone 5: final project verification

The default whole-project `lake build` passed cleanly: 2547 jobs in the build
graph, with dependency artifacts from the pinned official cache. Compiler and
mathlib commits appear in `logs/final-build.log`.

`scripts/TheoremInventory.lean` printed all 37 project declarations and their
axiom dependencies. `logs/final-theorem-inventory.log` is the compiler output;
`docs/theorem-statements.md` retains a readable copy. The hypothesis itself is
printed explicitly. Only `propext`, `Classical.choice`, and `Quot.sound` occur.

The source audit passed for the umbrella and all eight source modules. No
placeholder proof or added axiom declaration was found. A separate review
checked the mathematics, hypothesis quantifiers, nearest-pole property,
positive-index theorem meanings, source chain, and direct compiler inventories;
see `docs/independent-review.md` for its scope and conclusions.

Setup was rerun successfully and retained the dependency manifest byte for byte.
All relevant starter-archive manifest entries matched; reference notes remain
distinct from the present compiled proof evidence.

The source distribution contains proof sources, pinned configuration and
dependency manifest, reproduction scripts, complete mathematical proof,
compiler logs, theorem statements, review, progress records, and timestamped
milestone records. The original local session retains compressed snapshots;
those archives are excluded from this reviewed publication subset. Compiler binaries and dependency caches are fetched by
setup and are excluded from the distribution. No blocker remains.
