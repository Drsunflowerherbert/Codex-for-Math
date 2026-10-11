# Milestone 2: reusable lemmas compiled

All reusable source modules have compiled under pinned Lean 4.24.0 and mathlib
commit `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` (v4.24.0):

- `Hypothesis.lean`: the visible proposition, with no supplied instance.
- `NearestPole.lean`: construction, positivity, oddness, bounded pole distance,
  linear denominator bound, eventual growth, and actual nearest-pole property.
- `Trigonometry.lean`: cosine/offset identity, sine chord bound, tangent bounds.
- `Diophantine.lean`: error-distance algebra and the eventual exponent bound.
- `LimitComparison.lean`: generic limit from eventual quadratic growth.
- `NonPole.lean`: standard irrationality of π excludes every integer cosine zero.

Clean compilation logs: `nearest-pole-04.log`, `trigonometry-03.log`,
`diophantine-04.log`, `limit-comparison-05.log`, `nonpole-03.log` under `logs/`.
The compiler-generated shared declaration and axiom inventory is
`logs/milestone-02-theorem-inventory.log`.

No placeholder proofs or added axioms are present. Audited dependencies are the
standard Lean foundational axioms `propext`, `Classical.choice`, and `Quot.sound`.
The main limit theorem is the next compilation target; it has not passed at this
milestone. The absolute-convergence extension has not begun.

Historical blocker: v4.19.0's Azure cache host was rejected by the environment.
The exact v4.24.0 official alternate cache was verified and all 7335 files were
downloaded and unpacked without failure. Historical logs and initial snapshots
are preserved.
