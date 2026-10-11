# Dyadic summability component

Verified source: `tangent-limit/TangentLimit/DyadicSummability.lean`.

SHA-256: `8407909d22436551d60b8e71e7e88e790c53019c8b1ae647962a9dc755a8132c`.

The source compiles on Lean 4.24.0 and mathlib commit
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.

## Mathematical content

For any real-valued sequence f, the exact identity

```
Σ(n < 2^j) f(n) = f(0) + Σ(k < j) Σ(2^k ≤ n < 2^(k+1)) f(n)
```

is proved by induction using consecutive finite intervals. For nonnegative f,
if each block sum is at most a summable nonnegative g(k), then every finite
initial sum is at most f(0)+Σg. The estimate n≤2^n ensures that every initial
segment is contained in an initial dyadic segment. Bounded nonnegative partial
sums give summability. A separate lemma permits an arbitrary value at f(0) by
changing only that one term and reindexing by n+1.

The harmonic estimate H_(2^j)≤j+1 follows by induction. Doubling introduces
2^j reciprocal terms, each at most 1/2^j, so the increment is at most 1.

For 0≤ρ<1, Σ(j+1)ρ^j is summable by adding the geometric series to the standard
linear-times-geometric series. When β<0, ρ=2^β lies in (0,1), and
(2^j)^β=(2^β)^j. Therefore a block estimate

```
Σ(block j) f(n) ≤ C (2^j)^β H_(2^j),   C≥0, β<0
```

implies summability of f. The direct exported bridge is
`summable_of_dyadic_rpow_harmonic_bound`.

## Verification

Working directory: `<project>`.

Executed successfully:

```bash
source scripts/environment.sh
lake build TangentLimit.DyadicSummability
lake env lean logs/sharp-20261011/components/dyadic/Audit.lean
lake env lean --version
git -C .lake/packages/mathlib rev-parse HEAD
sha256sum TangentLimit/DyadicSummability.lean
```

Fresh logs: `build-final.log`, `audit-final.log`.

The audit checks exact types and runs `#print axioms` on all eleven declarations.
All use only the standard Lean foundations `propext`, `Classical.choice`, and
`Quot.sound`; `nat_le_two_pow` does not require `Classical.choice`.
There is no `sorry`, `admit`, added axiom, or Diophantine assumption in this
standalone infrastructure.

## Scope

This component is complete and compiled. It proves no tangent-specific block
bound. The sharp tangent-series theorem still requires such a bound and its
integration; this module alone does not certify the sharp target.
