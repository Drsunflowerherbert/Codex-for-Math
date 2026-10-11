# Exact-length Egyptian fractions

A standalone Lean 4/mathlib project about replacing repeated positive integer
denominators while preserving the number of terms and their exact reciprocal sum.

## Dependency pins

- Lean `leanprover/lean4:v4.24.0`, official release commit
  `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`.
- mathlib `v4.24.0`, resolved commit
  `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.
- `lake-manifest.json` pins the complete transitive dependency revisions.

In the original formalization environment, all dependencies came from the
official Lean/mathlib repositories and their registry sources. Official sources
and release archives were reachable, but cache endpoints returned proxy HTTP
403. The necessary dependency modules were compiled successfully from source.
Publication-session builds reused provisioned pinned dependencies and freshly
compiled this project's sources; see ../publication/evidence/CURRENT-CHECKS.json.

## Public mathematical contract

`Egyptian.reciprocalSum` uses real arithmetic and natural denominators. Positivity
is an explicit invariant, because Lean defines the inverse of zero to be zero.

`Egyptian.exact_length_distinct` states that a positive-denominator list with
reciprocal sum strictly between zero and one has a positive, distinct list with
the same length and reciprocal sum. No marker-preservation or sharp size bound
is part of this theorem.

`Egyptian.finite_sortedRepresentations` proves finiteness of positive
nondecreasing fixed-length representations for **every real value**. The proof
uses a bounded head denominator and induction on length. Executable enumeration
in the companion script instead requires rational inputs.

Odd duplicates `d = 2k+1` are replaced by `k+1, d(k+1)`, gaining weight `2k²`.
Even duplicates `d = 2k` are replaced by `k+1, k(k+1)`, gaining weight `(k−1)²`.
Every admissible duplicate has `d ≥ 3`. The replacement identities, strict
growth, positivity, length, value, and canonical-state membership are separate
lemmas. Collisions with other entries are allowed.

`Egyptian.cleanup_wellFounded` proves termination using the rank
`maximumStateWeight − currentStateWeight`. Strictly increasing natural weight
alone would not suffice. `Egyptian.boundary_counterexample` formalizes `[2,2]`
at value one and rules out every positive distinct length-two representation
of one.

`Egyptian.pad_one_preserving_denominator` proves that a positive distinct
expansion of one with at least three terms can gain exactly one term while
preserving any one specified input denominator. Its bounded version proves
that an input denominator bound B gives the output bound B(B+1). Both potential
marker collisions, at d+1 and d(d+1), are repaired by a composite factor split.
The prime obstruction and every safe-splitting invariant are compiled lemmas.

## Reproduce

With Lean/elan installed, run:

```sh
lake build
lake env lean Evidence.lean
python3 scripts/check_exact.py
```

`scripts/check.sh` runs the checks and retains logs. It also detects the optional
workspace-local Lean installation used in the original executor. An inaccessible
precompiled cache does not invalidate source builds.

The Python companion supports:

```sh
python3 scripts/exact.py cleanup 4 4 6
python3 scripts/exact.py enumerate 4 2/3
python3 scripts/exact.py pad 420 2 6 7 14 15 20 420
```

It uses `fractions.Fraction`, has no universal iteration guard, and checks exact
invariants at every step. It is a companion program, **not** a formal extraction
or refinement theorem. Observed test iteration counts are not runtime bounds.

## Attribution and transfer provenance

At formalization time, the supplied starter archive was unavailable after two
supported transfer attempts. No source bytes or archive hash were verified then.
The implementation was reconstructed independently from the supplied mathematical
contract. The source archive was `OpenAI-math-research-starter-2026-10-11.zip`,
version 0, expected SHA256
`b87f7e32f3ccbef1bcbbb819b05dafdc1481260925f22689563474467d2555da`.

This publication session retrieved that archive and verified the expected hash.
That does not retroactively change the formalizers' input access or certify
equivalence to the starter records. `evidence/source-transfer.json` preserves this
historical distinction without private identifiers or transport metadata.

The independent reviewer sources and reports are under `review/`. They clearly
distinguish mathematical review from a successful final compiler audit.

## Verification status and remaining goals

All requested mathematical goals, including optional marker-preserving padding
and its coarse bound, have compiled. Independent reviewers accepted the actual
theorem types, finite-state orientation, both marker collision cases, and axiom
outputs. Every reported axiom dependency is among `propext`, `Classical.choice`,
and `Quot.sound`; there is no `sorryAx` or added axiom declaration.

`Evidence.lean` prints actual types and axiom dependencies. `evidence/` retains
milestone builds, final build/check logs, and exact arithmetic checks. `review/` retains independent audit sources,
logs, and source-hash snapshots. The historical source provenance limitation is the
originally unavailable starter ZIP. There are no remaining mathematical goals.

Supplied historical receipts are retained, with privacy sanitation recorded in the
publication manifest. Publication-session checks are under `../publication/evidence/`.
No binaries, installed dependencies, nested checkpoint archive, or caches are
published. The original source and dependency pins are unchanged.
