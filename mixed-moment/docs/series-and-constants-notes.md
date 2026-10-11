> Historical source review: mathematical statements and verdicts are retained. Quoted hashes identify the original supplied files, which may differ from privacy-normalized public receipts. Original/public hashes are recorded in `publication/SOURCE-MAP.json`; fresh publication checks are separate.

# Convergent series and logarithmic constants

`MixedMoments/Series.lean` separates finite algebra, convergence, and actual
infinite sums. Its `momentSeries a i j` is a real `tsum`; it is not defined as
an integral. From nonnegative `a` and

    (n + 3) a(n + 2) = (n + 2) a(n),

`summable_momentSeries` proves convergence for every pair of natural indices.
The proof bounds the tail after two terms by `(i+2)` times the nonnegative
telescoping series `a(i+u)-a(i+u+2)`. Finite partial sums are bounded by
`a(i)+a(i+1)`, so no decay assumption is needed for this convergence proof.

The diagonal identity follows by removing one term. The minus and plus
boundary identities additionally assume `a(n) → 0`; their finite two-step
telescopes retain both tail terms before taking the limit. The plus recurrence
uses `a(0)=2` and `a(1)=0`, and correctly kills the old even boundary at index
two. `momentSeries_adjacent` and `momentSeries_one_zero` give exact rational
boundary values without assuming a transcendental start.

`RationalSeries.lean` casts the rational sequence to reals. The proved bound
`moment(n)^2 ≤ 8/(n+2)` and continuity of the square root establish decay.
Together with rational nonnegativity and recurrence, this discharges all
generic series hypotheses for the canonical rational moments.

`Constants.lean` proves the actual integral

    ∫₀¹ x^n (-log x) dx = 1/(n+1)^2.

The primitive is continuous at zero because `x log x` is continuous there;
its derivative is only invoked in the open interval. Multiplication of the
integrable logarithm by a polynomial proves integrability. This avoids an
unjustified endpoint substitution in a derivative formula.

Geometric expansions then give actual logarithmic integral representations
for the usual alternating odd-square series (Catalan) and the positive
odd-square sum. The sum of integrated absolute values is the convergent
odd-square series, so the alternating exchange is justified. The positive
kernel's integrability is proved through Tonelli and finite ENNReal integral.
Splitting the reciprocal-square series into even and odd terms proves

    ∫₀¹ (-log x)/(1-x²) dx = (3/4) zeta2.

These logarithmic constant identities do not themselves identify the M
boundaries. The separate boundary modules must supply the substitutions from
the original M integrals. No uniqueness of coordinates in `1,G,zeta2` and no
irrationality or independence statement is used anywhere in this layer.
