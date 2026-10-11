# Sharp absolute tangent series threshold

This extension proves in Lean that, assuming the original explicit
`TangentLimit.PiDiophantine` hypothesis, `Σ(n≥1) |tan n|/n^s` is summable
exactly for real `s > 1`. A separate theorem proves nonsummability for all real
`s ≤ 1` unconditionally, using only the standard irrationality of π.

```lean
import TangentLimit

#check TangentLimit.summable_abs_tan_div_rpow_positive_iff
#check TangentLimit.not_summable_abs_tan_div_rpow_positive
```

This standalone extended copy preserves the original cubic proof modules,
hypothesis, and dependency pins. The repository original in ../tangent-limit
is unchanged. The import entry point and inventory are extended here only. No proof or instance of `PiDiophantine` is supplied. This extension
makes no claim about conditional convergence of the signed series.

## Verification and reproduction

Lean 4.24.0 and mathlib commit
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7` are pinned in the original project.
From the `tangent-sharp` directory:

```bash
bash scripts/setup.sh
bash scripts/verify-sharp.sh
```

The extension verifier preserves the dependency manifest and writes fresh logs
under `.cache/research/verify-sharp`, separately from the original historical
logs. It builds the complete library, prints every exported declaration type
and its axiom dependencies, audits the two private spacing helpers, and scans
the source for placeholders and added axioms. An optional first argument
selects another untracked log directory.

The saved run audited 78 source declarations: 76 exported declarations and two
private lemmas. All dependencies are subsets of `propext`, `Classical.choice`,
and `Quot.sound`; there is no `sorryAx`.

## Source and evidence

| File | Role |
| --- | --- |
| `TangentLimit/UniformDiophantine.lean` | Uniform positive bound over every positive denominator and all integer numerators |
| `TangentLimit/PoleSpacing.lean` | Block pole distances and separation of signed offsets |
| `TangentLimit/FinitePacking.lean` | Reusable harmonic reciprocal packing bound |
| `TangentLimit/BlockEstimates.lean` | Analytic weighting and real-power algebra |
| `TangentLimit/DyadicSummability.lean` | Harmonic dyadic bound and proved summability bridge |
| `TangentLimit/Divergence.lean` | Unconditional divergence for real exponents at most one |
| `TangentLimit/SharpSummability.lean` | Block estimate and sharp equivalence |

The readable ordinary proof is in `docs/sharp-threshold-proof.md`.
Fresh commands, exact theorem types, pins, hashes, and verification scope are
described in `docs/sharp-verification.md`. Independent review is recorded in
`docs/sharp-independent-review.md`. Saved fresh logs are in `logs/sharp-20261011`.

Historical cubic notes are retained in `BASELINE-README.md` and
`BASELINE-PROGRESS.md` and under `docs/`; their original scope does not limit the
separate sharp extension. Supplied archive hashes and local source-commit
provenance are historical records. Current publication integrity uses
`../publication/FILES.json`, and fresh publication checks are under
`../publication/evidence/`. No proof of `PiDiophantine` is supplied.
