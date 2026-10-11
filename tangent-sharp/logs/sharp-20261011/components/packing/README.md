# Finite reciprocal packing — fresh verified component

Verified at 2026-10-11 03:08:53 UTC from source based on `d00a89dd9ce6c8ef782234d28c93e69cb712c947`.

Source: `TangentLimit/FinitePacking.lean` in `<project>`. The final source uses eight focused imports for finite sorting, finite sums, real arithmetic, and the individual linarith, positivity, and ring tactics; neither `import Mathlib` nor the tactics umbrella remains.

## Public estimate

For any finite set of labels `S`, real offsets `f`, and `δ > 0`, if every `|f i| >= δ` and distinct labels have `|f i - f j| >= δ`, the compiled theorem proves

```
sum_{i in S} 1 / |f i| <= (2 / δ) * sum_{k=0}^{S.card-1} 1 / (k+1).
```

The exact public Lean name is `TangentLimit.sum_reciprocal_abs_le_harmonic`. Its label type is arbitrary, with `DecidableEq`; its hypotheses are explicit. It does not refer to pi, tangent, irrationality, or `PiDiophantine`.

## Proof

On the positive side, `Finset.orderEmbOfFin` gives the strictly increasing order of the real-valued points. The first point is at least δ. Pairwise spacing makes each successive gap at least δ. Induction gives the point with zero-based index k at least `(k+1)δ`. Taking reciprocals and summing gives `H_card / δ`.

For arbitrary labels, spacing and δ > 0 imply injectivity of `f` on the finite set, so the sum and cardinality are preserved by passing to the image. Split labels by `0 <= f i`. Negate the values in the negative part; spacing remains unchanged. Apply the one-sided estimate to each part and enlarge each harmonic cutoff to `S.card`. Adding gives the stated factor 2.

## Commands and evidence

All Lean commands were run after `source scripts/environment.sh` from the project directory.

```
lake env lean TangentLimit/FinitePacking.lean
lake env lean -o .lake/build/lib/lean/TangentLimit/FinitePacking.olean -i .lake/build/lib/lean/TangentLimit/FinitePacking.ilean TangentLimit/FinitePacking.lean
lake env lean logs/sharp-20261011/components/packing/Audit.lean
lake env lean --version
```

The first two commands and the audit returned exit 0. `compile.log` is empty because the successful compiler emitted no diagnostics. `types-and-axioms.log` prints all five exact theorem types and their axiom dependencies. Each has only `[propext, Classical.choice, Quot.sound]`; no `sorryAx` or new axioms occur.

Compiler pin: `leanprover/lean4:v4.24.0`, observed compiler commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`. Mathlib manifest pin: `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.

`SHA256SUMS` records source, compiled object, audit script, and verification logs. This component proves only finite packing. It does not itself prove the sharp tangent-series theorem or apply the geometric block argument.
