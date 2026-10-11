> Historical source review: mathematical statements and verdicts are retained. Quoted hashes identify the original supplied files, which may differ from privacy-normalized public receipts. Original/public hashes are recorded in `publication/SOURCE-MAP.json`; fresh publication checks are separate.

# Analytic Taylor contact through finite polynomials

`MixedMoments/TaylorContact.lean` proves the analytic contact bridge for
rational polynomials. Its result does not require an analytic infinite-series
evaluation theorem or an exchange of a series with a limit or integral.

## The actual contact function and exact filters

For `P D : Polynomial ℚ`, `analyticContactFunction P D x` is exactly

```lean
x * (P.map (Rat.castHom ℝ)).eval x / Real.sqrt (1 - x ^ 2) -
  (D.map (Rat.castHom ℝ)).eval x
```

The real square root is positive near zero. The two proved equivalences are

```lean
analyticContact_nhds_iff_coefficientContact (P D : Polynomial ℚ) (L : ℕ) :
  (analyticContactFunction P D =O[𝓝 0] (fun x => x ^ L)) ↔
    CoefficientContact P D L

analyticContact_right_iff_coefficientContact (P D : Polynomial ℚ) (L : ℕ) :
  (analyticContactFunction P D =O[𝓝[>] 0] (fun x => x ^ L)) ↔
    CoefficientContact P D L
```

The right-neighborhood filter `𝓝[>] 0` is explicit. The forward proof does
not silently replace it with `𝓝 0`. It first proves finite coefficient
vanishing from that one-sided hypothesis; the resulting coefficient condition
then gives the two-sided condition by a separate theorem.

All natural `L`, including zero, are allowed. Order zero imposes an empty
coefficient condition, and the corresponding function is bounded near zero.

## Proof ingredients

`polynomial_coeff_zero_of_isBigO_eval_pow` proves that a real polynomial with
one-sided big-O growth `O(x^L)` has zero coefficients at every `j < L`.
The proof inducts on `L`: continuity and the positive-side limit force the
constant term to vanish, `Polynomial.divX` removes one factor of `X`, and
division by `x` is justified on the positive-side filter. The two-sided
specialization is `polynomial_coeff_zero_of_isBigO_eval_pow_nhds`.

`inverseSqrtApprox L` is the finite polynomial truncation at `L+1` of
`inverseSqrtFormalSeries`. Keeping one extra coefficient ensures the constant
term is one even when `L = 0`.

The algebraic identity in `FormalSquareRoot.lean`,

```lean
(1 - PowerSeries.X ^ 2) * inverseSqrtFormalSeries ^ 2 = 1
```

implies that the polynomial error

```lean
inverseSqrtApproxError C = (1 - Polynomial.X ^ 2) * C ^ 2 - 1
```

has no coefficients below degree `L+1` when `C = inverseSqrtApprox L`.
`inverseSqrtApprox_error_coeff` proves this by the formal truncation APIs.

`inverseSqrtApproximation_isBigO` is a general real-polynomial lemma. If
`C.coeff 0 = 1` and the error has zero coefficients below `L`, then

```lean
(fun x => C.eval x - 1 / Real.sqrt (1 - x ^ 2)) =O[𝓝 0] (fun x => x ^ L)
```

The proof factors the finite error as `X^L * R`. For small real `x`, it uses
the exact algebraic identity

```text
C(x) - 1/sqrt(1-x²)
  = x^L R(x) / (sqrt(1-x²) * (sqrt(1-x²) C(x) + 1)).
```

The denominator is continuous and equals two at zero, so its reciprocal times
`R(x)` is bounded near zero. Positivity of `1-x²` and nonzero denominators are
proved as eventual statements before the field calculation.

`inverseSqrtApproxReal_remainder` applies this result to the cast of the exact
rational truncation. `contactApproximation_coeff` proves that the first
`L+1` coefficients of `X*P*inverseSqrtApprox L-D` are the specified
`polynomialDefect P D j`.

Multiplying the inverse-square-root remainder by the locally bounded function
`x*P(x)` gives the approximation error for the actual contact function.
Adding or subtracting this remainder proves both directions of the contact
equivalence. `polynomial_eval_isBigO_pow_of_coeff_zero` supplies the reverse
polynomial implication by factoring out `X^L`.

## Constructive contact and cancellation

`contactTruncation_analyticContact` proves that the previously constructed
rational polynomial `contactTruncation P L` has the actual two-sided contact
condition of order `L`.

`cancellation_of_analyticContact` combines positive-side big-O contact with
the existing finite cancellation theorem. Its remaining premises explicitly
identify the chosen real arrays with `Coordinates.eval G ζ formalM` and
`Coordinates.eval G ζ formalZ`. Its conclusion gives rational witnesses for
the real polynomial contraction. The theorem assumes no injectivity of the
coordinate evaluation map and no independence or irrationality of constants.

The integral decomposition and boundary values belong to separate modules.
This file has no remaining analytic contact obligation.

## Verification

The source passed both commands under Lean 4.24.0 and pinned mathlib revision
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`:

```sh
bash scripts/with-lean.sh lake env lean MixedMoments/TaylorContact.lean
bash scripts/with-lean.sh lake build MixedMoments.TaylorContact
```

No admitted proofs, new axioms, or `native_decide` are used.
