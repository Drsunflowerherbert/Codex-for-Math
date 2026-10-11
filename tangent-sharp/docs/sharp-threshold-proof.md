# Sharp absolute tangent series threshold

Under the explicit hypothesis `TangentLimit.PiDiophantine`, the positive-integer
series `Σ |tan n| / n^s` is summable exactly when the real exponent `s` is
strictly greater than one. Nonsummability for `s ≤ 1` is unconditional and uses
only the standard proved irrationality of π. These results are compiled in
Lean 4.24.0 against the pinned mathlib revision. They make no assertion about
conditional convergence of the signed tangent series.

## Hypothesis and theorem statements

The original hypothesis is preserved unchanged:

```lean
def PiDiophantine : Prop :=
  ∀ ν : ℝ, 2 < ν → ∃ Q : ℕ, ∀ q : ℕ, Q ≤ q → 0 < q →
    ∀ p : ℤ, (q : ℝ) ^ (-ν) ≤
      |Real.pi - (p : ℝ) / (q : ℝ)|
```

No proof or instance of this hypothesis is supplied. The final statements are:

```lean
theorem summable_abs_tan_div_rpow_positive_iff
    (h : PiDiophantine) (s : ℝ) :
    Summable (fun n : ℕ =>
      |Real.tan ((n + 1 : ℕ) : ℝ)| /
        ((n + 1 : ℕ) : ℝ) ^ s) ↔ 1 < s

theorem not_summable_abs_tan_div_rpow_positive
    (s : ℝ) (hs : s ≤ 1) :
    ¬ Summable (fun n : ℕ =>
      |Real.tan ((n + 1 : ℕ) : ℝ)| /
        ((n + 1 : ℕ) : ℝ) ^ s)
```

The `n+1` indexing enumerates exactly the positive integers. All real powers
in this series have positive bases. The sufficient direction also has a
natural-index version; its zero term is harmless under Lean's totalized
division. The proof of the sharp equivalence invokes the separate unconditional
divergence theorem for the necessary direction.

## Uniform control of exceptional denominators

Fix `α > 2`. For an irrational real number `x`, let `k = floor x` and set
`ε = min (x-k) (k+1-x)`. Irrationality gives `k < x < k+1`, hence `ε > 0`.
Every integer `p` lies at or below `k`, or at or above `k+1`; therefore
`ε ≤ |x-p|`, uniformly over all integer numerators.

Apply this observation to `x = qπ` for each positive exceptional denominator
below the cutoff supplied by `PiDiophantine`. Induction over the finite cutoff
takes positive minima and proves a single constant `0 < c ≤ 1` such that

```text
c q^(1-α) ≤ |qπ-p|   for every positive natural q and every integer p.  (1)
```

Above the cutoff, multiplying the original approximation inequality by `q`
gives (1), since `c ≤ 1`. Below the cutoff, the finite minimum gives it. Thus
no small denominator or negative numerator is omitted.

Formal lemmas: `irrational_integer_distance`, `pi_integer_distance`,
`pi_finite_denominator_bound`, and `piDiophantine_uniform` in
`UniformDiophantine.lean`.

## Distances and signed spacing on a block

For an integer `N ≥ 1`, consider `N ≤ n < 2N`. Reuse the original definitions

```text
k_n = floor(n/π),  q_n = 2k_n+1,  d_n = n-q_nπ/2.
```

The floor inequalities give `|d_n| ≤ π/2`. Since `π > 2` and `n < 2N`,
`k_n < N`, hence `0 < q_n ≤ 3N`. Define

```text
δ_N = (c/2)(3N)^(1-α) > 0.
```

Apply (1) with denominator `q_n` and numerator `2n`:

```text
2|d_n| = |q_nπ-2n| ≥ c q_n^(1-α) ≥ c(3N)^(1-α).
```

The last inequality uses `1-α < 0`. Consequently every distance is at least
`δ_N`. Also `δ_N ≤ 1/2` because `c ≤ 1`, `3N ≥ 1`, and the exponent is negative.

For distinct `n,m` in the block,

```text
d_n-d_m = (n-m) - (k_n-k_m)π.
```

If the pole indices are equal, the absolute difference is a nonzero integer,
so it is at least `1 ≥ δ_N`. Otherwise orient the pair so `k_n > k_m`, put
`q = k_n-k_m > 0`, and use the integer numerator `p = n-m`. Since `q < N`,
(1) bounds the absolute difference below by `c(3N)^(1-α) = 2δ_N`.
The opposite orientation follows by symmetry of absolute difference.

Thus distinct signed offsets are `δ_N` separated. The proof separates the
equal-index case explicitly and never applies (1) to denominator zero.
Formal lemmas are in `PoleSpacing.lean`.

## Harmonic packing and the weighted block bound

For any finite family of real points separated from zero and one another by
`δ > 0`, split them according to sign. On either side, order their distances
in increasing order. The first is at least `δ`; each successive distance
increases by at least `δ`. The point of rank `j`, starting at zero, therefore
has distance at least `(j+1)δ`.

Writing `H_M = Σ(k=0,…,M-1) 1/(k+1)`, the two sides give

```text
Σ(i∈S) 1/|f_i| ≤ (2/δ) H_card(S).                         (2)
```

`FinitePacking.lean` proves this for arbitrary labels, deriving injectivity
from the separation assumption. The ordering proof uses a finite order
embedding, then reindexes the sum without losing any multiplicities.

The original analytic estimate gives
`|tan n| ≤ π/(2|d_n|)`. For `s ≥ 0` and `n ≥ N > 0`,
`n^s ≥ N^s`. The block has exactly `N` integers, so (2) implies

```text
Σ(N≤n<2N) |tan n|/n^s ≤ C N^(α-1-s) H_N,
C = (2π/c) 3^(α-1) > 0.                                  (3)
```

The constant is independent of both `N` and `s`. Formal lemmas:
`sum_abs_tan_div_rpow_le_reciprocal`, `weighted_block_coefficient`, and
`abs_tan_rpow_block_bound`.

## Summability above one

For `s > 1`, choose `α = (s+3)/2`. Then `2 < α < s+1`, so
`β = α-1-s = (1-s)/2 < 0`. On `N = 2^j`, (3) becomes
`C(2^j)^β H_(2^j)`.

The `2^j` new reciprocals in doubling a harmonic cutoff have sum at most one.
Induction proves `H_(2^j) ≤ j+1`. Real-power identities give
`(2^j)^β = ρ^j`, where `ρ = 2^β` satisfies `0 < ρ < 1`.
The sequence `(j+1)ρ^j` is summable, by adding a geometric series and a
linear-factor geometric series.

`DyadicSummability.lean` proves the exact finite decomposition

```text
Σ(n<2^j) f(n) = f(0) + Σ(k<j) Σ(2^k≤n<2^(k+1)) f(n).
```

Every finite initial segment lies within a dyadic initial segment. For
nonnegative `f`, the summable block majorant bounds all partial sums and
therefore proves `Summable f`. This proved bridge connects the finite block
estimate to the original series; no monotonicity of the tangent terms is
assumed. `SharpSummability.lean` then shifts to positive-integer indexing.

## Unconditional divergence at and below one

Standard irrationality of π proves `cos n ≠ 0` at every integer argument,
as already established in the original `NonPole.lean`. At a nonpole,
`|sin x| ≤ |tan x|`, since `|cos x| ≤ 1`. The sine subtraction identity,
the triangle inequality, and cosine bounds give

```text
0 < sin 1 ≤ |tan n| + |tan(n+1)|.                          (4)
```

Suppose the absolute series at exponent one were summable. Its one-step
shift would be summable too. Adding the two series and using (4) with the
larger denominator yields the summable majorant

```text
sin 1/(n+2) ≤ |tan(n+1)|/(n+1) + |tan(n+2)|/(n+2).
```

This would make a positive multiple of a shifted harmonic series summable,
contradicting harmonic divergence. Overlapping pairs cause no issue because
the proof adds two summable series directly.

For every real `s ≤ 1`, including negative `s`, positive integers satisfy
`n^s ≤ n`. Hence the exponent-one absolute terms are bounded above by the
exponent-`s` terms. Summability at exponent `s` would imply the already
disproved summability at exponent one. `Divergence.lean` imports no project
Diophantine module and keeps this direction unconditional.

## Evidence and scope

The source derives from commit `d00a89dd9ce6c8ef782234d28c93e69cb712c947`
on the user's original `codex/tangent-limit` branch. The extension was developed
on the separate local branch `codex/tangent-sharp-20261011`; no push, PR, merge,
credential change, or permission change occurred.

The prior ordinary proof and source/rebuild checkpoint Pages were read through
supported Page tools. Their historical compiler logs are not used as fresh
evidence. This run generated its own baseline build, fresh source elaboration,
compiler type and axiom inventories, integrated builds, and independent review.
See `sharp-verification.md` and `sharp-independent-review.md` for the fresh
evidence and limitations.
