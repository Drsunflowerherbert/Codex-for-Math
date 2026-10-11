# Unconditional divergence component

Verified source: `TangentLimit/Divergence.lean` (six new declarations).

The endpoint theorem states

```lean
TangentLimit.not_summable_abs_tan_div_positive :
  ¬ Summable (fun n : ℕ => |Real.tan ((n + 1 : ℕ) : ℝ)| /
    ((n + 1 : ℕ) : ℝ))
```

The real-exponent theorem states

```lean
TangentLimit.not_summable_abs_tan_div_rpow_positive (s : ℝ) (hs : s ≤ 1) :
  ¬ Summable (fun n : ℕ => |Real.tan ((n + 1 : ℕ) : ℝ)| /
    ((n + 1 : ℕ) : ℝ) ^ s)
```

Both are unconditional. Their only input regarding π is the proved irrationality
used by `TangentLimit.NonPole.cos_natCast_ne_zero`, showing integer arguments have
nonzero cosine. There is no `PiDiophantine` argument, hidden assumption, axiom,
`sorry`, or `admit`.

For a non-pole x, |sin x| ≤ |tan x| follows from |cos x| ≤ 1. The sine
subtraction formula then gives

    sin 1 ≤ |tan x| + |tan (x + 1)|.

Here sin 1 is strictly positive since 0 < 1 < π. At positive integer n, divide
this adjacent-pair bound by n+1 and use n ≤ n+1 to obtain

    sin 1 / (n+1) ≤ |tan n| / n + |tan (n+1)| / (n+1).

If the exponent-one series were summable, its one-step shift and their sum
would be summable. The nonnegative comparison above would make a positive
constant times a shifted harmonic series summable, contradicting mathlib's
`Real.not_summable_one_div_natCast`. Overlapping pairs are harmless: each term
occurs at most twice, and summability is closed under shifts and addition.

For s ≤ 1 and positive integer n, n^s ≤ n by monotonicity in the exponent.
Consequently |tan n|/n ≤ |tan n|/n^s. Summability at exponent s would imply
summability at exponent one, already contradicted.

## Verification

From the project directory:

```sh
source scripts/environment.sh
set -o pipefail
lake env lean TangentLimit/Divergence.lean -o .lake/build/lib/lean/TangentLimit/Divergence.olean 2>&1 | tee <historical-workspace>/scratch/divergence/full-build.log
lake env lean <historical-workspace>/scratch/divergence/Audit.lean 2>&1 | tee <historical-workspace>/scratch/divergence/audit.log
```

Both Lean commands completed with exit status zero. The first had no warnings.
Each of the six declarations has exactly the standard axiom set
`[propext, Classical.choice, Quot.sound]` in the independent `#print axioms` audit.
The compact audit records exact checked theorem types; the proof-term audit
additionally printed theorem values.

This component makes no claim about conditional convergence of the signed
series, or summability for s > 1. Integration into the umbrella module and the
full project's inventory/build belong to the implementation.
