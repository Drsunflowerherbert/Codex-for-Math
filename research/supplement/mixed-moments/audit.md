# Independent audit of mixed moments and Taylor cancellation

Scope: the absolute-convergence paragraph and the subsection “Moment evaluation and cancellation” in `catalog/sources/preprints_Catalans-constant-is-irrational-September-24-2026_build_sections_foundations.tex`.

## Result

No incorrect identity or missing mathematical hypothesis was found in the scoped text. The assertions are valid for nonnegative integer indices, the stated zero convention for `c`, and the rational/integer row coefficients used in the manuscript. The negative-index definition of `M^0` is explicitly an algebraic convention, not an additional integral.

The phrase “coefficient of ζ(2)” should be understood as the coefficient in the displayed, specified decomposition. Uniqueness of a decomposition in `Q + QG + Qζ(2)` is neither assumed nor needed. In particular, a nonzero displayed coefficient of ζ(2) does not by itself prove that the value is outside `Q + QG`.

## Absolute convergence and interchange

Put `u = |t|`. On either half of the `t` interval, the sum of the absolute values of the geometric-series terms is bounded, after integrating in `s`, by

    (u / sqrt(1-u²)) ∫₀¹ ds/(1-us)
      = -log(1-u)/sqrt(1-u²).

This is integrable: it is `O(u)` near zero and `O((1-u)^(-1/2)|log(1-u)|)` near one. Hence Tonelli applied to the absolute values justifies all geometric-series interchanges for M, including the negative half of the interval. Bounded polynomial factors merely change the constant. For Z the corresponding majorant is `-log(1-u)/u`, again integrable.

## Moments and recurrences

Symmetry gives `m_i = 0` for odd nonnegative `i`. For even `i`, integration by parts on `(0,1)` gives

    (i+1)m_i = i m_{i-2},  m₀ = 2,
    m_i = 2 / ((i+1)c_(i/2)).

The `i=1` instance is also correct with the manuscript's `m₋₁ = 0` convention. Dominated convergence gives `m_i → 0` as `i → ∞`.

The geometric series gives

    M(i,j) = Σ_{u≥0} m_(i+u)/(j+u+1),
    M(i,j) - M(i+1,j+1) = m_i/(j+1).

For the minus boundary, the termwise identity is

    [d m_(d+u) - (d-1)m_(d+u-2)]/(u+1)
      = m_(d+u-2) - m_(d+u).

Summing gives `m_(d-2)+m_(d-1)`. This proves the recurrence for `d≥2`. The same identity at `d=1`, with the zero multiplier omitted, gives `K⁻₁=m₋₁+m₀=2`.

For the plus boundary, shifting the first series by two yields, for `u≥2`,

    [(d-1)m_(u-2) - (d-2)m_u]/(d+u-1)
      = m_(u-2)-m_u.

These terms sum to 2. The only nonzero unpaired boundary term is `-2(d-2)/(d-1)`. Their total is `2/(d-1)`, as claimed. In particular `K⁺₂=2`; the recurrence at `d=2` intentionally eliminates the `K⁺₀` start.

## Boundary constants

Pairing the positive and negative halves and substituting `t=sin θ` gives

    K⁻₀ = ∫₀^{π/2} log((1+sin θ)/(1-sin θ)) dθ
         = -4∫₀^{π/4} log(tan v) dv
         = 4∫₀¹ (-log x)/(1+x²) dx = 4G.

The geometric-series calculation in the last integral is legitimate, for example because the integrals of the absolute values of the individual terms sum to `Σ(2k+1)^(-2)<∞`.

There is a shorter independent evaluation of the other start, avoiding arcsine and a separate proof of the Basel sum. Pairing `t=±u` gives

    K⁺₁ = ∫₀¹ [2u/sqrt(1-u²)] ∫₀¹ s/(1-u²s²) ds du
         = -∫₀¹ log(1-u²)/(u sqrt(1-u²)) du.

With `x=sqrt(1-u²)` this becomes

    K⁺₁ = -2∫₀¹ log x/(1-x²) dx
         = 2 Σ_{k≥0} 1/(2k+1)²
         = (3/2)ζ(2).

All terms in this final series expansion are nonnegative, so Tonelli suffices. The manuscript's longer arcsine proof and its Abel/dominated-convergence proof of `π²/4=(3/2)ζ(2)` are also correct.

## Diagonal reduction and decomposition

Iterating the diagonal difference identity from `(i-j,0)` to `(i,j)`, when `i≥j`, produces exactly

    K⁻_(i-j) - Σ_{k=1}^j m_(i-j+k-1)/k.

Iterating from `(0,j-i)`, when `i<j`, produces exactly

    K⁺_(j-i) - Σ_{k=j-i+1}^j m_(k-(j-i)-1)/k.

Thus both displayed formulas for `M^0` have the correct ranges and signs. The rational starts and these formulas uniquely determine the array.

The minus recurrence propagates its even homogeneous start by `c_(d/2)`; its odd start is already rational. On the plus boundary, the even positive indices have no homogeneous start because the `d=2` coefficient is zero, and the odd indices propagate `K⁺₁` by `c_((d-1)/2)`. The diagonal reductions preserve the index difference. This establishes exactly

    M(i,j) = M^0(i,j) + 4G c_((i-j)/2)
                         + (3/2)ζ(2)c_((j-i-1)/2).

Partial fractions in the absolutely convergent series for Z give the displayed off-diagonal harmonic-number formula; on the diagonal the result is `ζ(2)-B_i^(2)`. No boundary case is missing.

## Explicit rational boundary arrays

For both parity classes, the stated definition gives

    H*_(z+2)/H*_z = (z+1)/(z+2).

Dividing the minus recurrence at `z≥2` by `zH*_z`, its additive increment is

    2/[z²(H*_z)²]  if z is even,
    2/z            if z is odd.

The even base is `k⁻₀=0`. The odd base is `k⁻₁/H*₁=2`, exactly the `z=1` summand. Thus both minus formulas, including empty sums, follow.

Write `a_u=k⁺_(u+1)`. Its recurrence is

    a_u = ((u-1)/u)a_(u-2) + 2/u².

Dividing by `H*_u` gives the increment `2/(u²H*_u)`. The even base is `a₀=0`, and the odd base is `a₁=2`, again the `z=1` summand. This proves the claimed plus formula, also at `u=0` and `u=1`.

## Taylor cancellation and the correct counterexample claims

For rational polynomials P and D, the specified decomposition is

    M(P,j) - (3/2)Z(D,j)
      = q_j + 4G α_j + (3/2)ζ(2)β_j,

where `q_j, α_j, β_j` are rational and

    α_j = Σ_i [t^i]P · c_((i-j)/2),
    β_j = [t^j](tP/sqrt(1-t²) - D).

Consequently Taylor contact of order L makes the displayed ζ(2) coefficient vanish for all `0≤j<L`. The manuscript uses only this sufficient implication and does not assume any independence of constants.

If contact is dropped, take `P=0`, `D=t^j`. The value is

    (3/2)B_j^(2) - (3/2)ζ(2),

which is irrational, and its ζ(2) coefficient does not cancel. To preserve the manuscript's support bounds while testing contact alone, one can take `j=A+1`, which lies in the raw column range for every positive integer N. This establishes failure of the rationality conclusion under the hypothetical assumption `G∈Q`; it does not establish unconditionally that the value is outside `Q+QG`.

If the strict column bound is dropped, the simple example `P=1`, `D=t`, `L=3` has

    tP/sqrt(1-t²)-D = (1/2)t³ + O(t⁵),

but at `j=L=3` its entry is `(3/4)ζ(2)-1/8`, again irrational. The same distinction about `Q+QG` applies.

For the actual manuscript rows, the first uncanceled coefficient in row r occurs exactly at `j=L+r`:

    tR_r/f = 2^(g-r) t^(L+r) + O(t^(L+r+1)).

In particular row 0 has nonzero displayed ζ(2) coefficient `3·2^(g-1)` at `j=L`. For rows `r>0`, cancellation continues beyond `j=L-1`; the common bound `j<L` is sufficient for every row but is not the exact contact bound for each individual row.

No claim about irrationality of G, independence of G and ζ(2), or formal proof-system verification is made by this audit.
