> Historical source review: mathematical statements and verdicts are retained. Quoted hashes identify the original supplied files, which may differ from privacy-normalized public receipts. Original/public hashes are recorded in `publication/SOURCE-MAP.json`; fresh publication checks are separate.

# Cancellation core: scope and theorem interfaces

`MixedMoments/Cancellation.lean` works in the free rational coordinate space
`Coordinates := Fin 3 → ℚ`. Its three named projections are `rational`,
`catalan`, and `zetaTwo`. Componentwise addition and rational scalar
multiplication come from the function-space module instances.

`Coordinates.eval G ζ` sends a coordinate vector to `a + b*G + c*ζ` for
arbitrary real numbers `G` and `ζ`. Addition, subtraction, scalar
multiplication, and finite sums commute with this evaluation. No theorem
requires this map to be injective. A nonzero formal coordinate is consequently
not a proof of nonmembership of the evaluated real value in a rational span.

## Exact algebraic definitions

`formalM` and `formalZ` use `mRationalPart`, `zRationalPart`, and the
integer-indexed `kernel` from `Rational.lean`. Every difference in a kernel
argument is computed in `ℤ`. Negative differences are not truncated to zero
before applying the kernel.

For `P D : Polynomial ℚ`, finite support sums define `polynomialM`,
`polynomialZ`, and `formalEntry`. The finite convolution
`contactCoefficient P j` is the specified coefficient for the contact
condition; `polynomialDefect P D j` subtracts `D.coeff j` from it.

The unconditional theorem `formal_entry_zeta_coordinate` states

```lean
∀ (P D : Polynomial ℚ) (j : ℕ),
  (formalEntry P D j).zetaTwo = (3 / 2 : ℚ) * polynomialDefect P D j
```

`exact_defect_identity` evaluates this formal identity, with explicit finite
rational sums `rationalWitness P D j` and `catalanWitness P j`.

## Finite contact and cancellation

`CoefficientContact P D L` is exactly

```lean
∀ j < L, polynomialDefect P D j = 0
```

`coefficient_contact_cancellation_explicit` proves, for every `j < L`,

```lean
Coordinates.eval G ζ (formalEntry P D j) =
  (rationalWitness P D j : ℝ) + (catalanWitness P j : ℝ) * G
```

`coefficient_contact_cancellation` also exposes the corresponding existential
rational witnesses. This works for every natural `L`; `L = 0` gives an empty
range of columns.

`contactTruncation P L` constructs a rational polynomial by summing the first
`L` monomials with coefficients `contactCoefficient P j`.
`contactTruncation_coeff` proves its coefficient formula, and
`contactTruncation_contact` proves that it satisfies the finite contact
condition. These are quantified Lean proofs, rather than imports of the
Python certificate output.

`paired_entry_zeta_coordinate` proves the analogous identity after contraction
against a second rational polynomial `Q`. `paired_cancellation` requires only
the scalar condition `pairedDefect P D Q = 0`.
`paired_cancellation_of_contact` supplies that condition when every exponent
in `Q.support` is less than `L`.

## Explicit analytic transfer

`realPolynomialContraction A P j` is a finite contraction of an arbitrary real
array `A`. Its name does not claim that `A` is an integral.

`cancellation_of_decompositions` assumes the two entrywise identities

```lean
∀ i j, M i j = Coordinates.eval G ζ (formalM i j)
∀ i j, Z i j = Coordinates.eval G ζ (formalZ i j)
```

It then proves the real contraction cancellation with explicit rational
witnesses, assuming `CoefficientContact P D L` and `j < L`.

`Decomposition.lean` proves the first entrywise identity from explicit diagonal
and boundary recurrences plus the starts `M 0 0 = 4*G`, `M 1 0 = 2`, and
`M 0 1 = (3/2)*ζ`. The assumptions are packaged in the proposition
`MomentRecurrenceData`; they are explicit fields, not axioms.

`moment_recurrence_data_unique` proves uniqueness of the entire real array
from this data, and `realM_eq_eval_formalM` applies it to the evaluated formal
array. `cancellation_of_recurrences` then removes the entrywise M-decomposition
premise from the cancellation theorem.

`momentSeries_recurrence_data` instantiates the data for the actual infinite
series `Series.momentSeries a`: the moment identification and decay are
explicit hypotheses, summability follows from the established nonnegativity
and recurrence, and the value at `(1,0)` is proved by telescoping.
`realMomentSeries_recurrence_data` specializes to the canonical cast of the
rational moment sequence, whose decay is proved in `RationalSeries.lean`.
`realMomentSeries_eq_eval_formalM` therefore has only two remaining premises:

```lean
Series.momentSeries realMoment 0 0 = 4 * G
Series.momentSeries realMoment 0 1 = (3 / 2 : ℝ) * ζ
```

`cancellation_of_realMomentSeries` uses these two premises plus the Z-array
decomposition and finite coefficient contact. The separate integral module
may identify an actual integral with this series.

## Formal power-series meaning of contact

`FormalContact.lean` defines `inverseSqrtFormalSeries` as the genuine rational
formal power series with coefficients `kernel (n : ℤ)`, and

```lean
formalContactSeries P D =
  PowerSeries.X * (P : PowerSeries ℚ) * inverseSqrtFormalSeries -
    (D : PowerSeries ℚ)
```

`contactCoefficient_eq_powerSeries_coeff` proves the finite convolution is
exactly the coefficient of `X*P*inverseSqrtFormalSeries`.
`polynomialDefect_eq_formalContactSeries_coeff` proves the corresponding
defect identity. `coefficientContact_iff_formalContactSeries` identifies
finite contact with vanishing of the first `L` coefficients of this formal
power series. These statements use the polynomial and formal-power-series
operations, rather than treating the convolution as an uninterpreted function.

`TaylorContact.lean` now separately proves the analytic bridge by finite
polynomial approximation. It identifies `CoefficientContact` with both
two-sided big-O contact at zero and contact from the positive side of zero.
See `taylor-contact-notes.md` for the exact filters and proof interfaces.
Actual integral boundary constant evaluations remain independent of this
coefficient argument; their status belongs to the integral and boundary
modules. The formal-series identity alone is not used as a substitute for
the analytic bridge.

## Exact checks and build

The source contains proved low-index coordinate values for
`M(0,0)`, `M(0,1)`, `M(1,0)`, `M(0,2)`, `M(2,0)`, `Z(0,1)`, and `Z(1,1)`.
For `P = 1`, `D = X`, the finite contact condition is proved at order three,
and the first four formal entries are proved to be

| Column | Rational | Catalan | Zeta two |
|---|---:|---:|---:|
| 0 | -3/2 | 4 | 0 |
| 1 | 3/2 | 0 | 0 |
| 2 | 5/4 | 0 | 0 |
| 3 | -1/8 | 0 | 3/4 |

`one_X_entry_three_zeta_nonzero` proves the final coordinate is nonzero; it
does not assert any independence of real constants. This checks the strict
column bound.

The verified toolchain is Lean 4.24.0 with mathlib revision
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The actual cancellation source has
passed

```sh
bash scripts/with-lean.sh lake env lean MixedMoments/Cancellation.lean
bash scripts/with-lean.sh lake build MixedMoments.Cancellation
bash scripts/with-lean.sh lake build MixedMoments.Decomposition MixedMoments.FormalContact MixedMoments.TaylorContact
```

No `sorry`, `admit`, new axioms, or `native_decide` are present in this source.
The finite algebra is independent of any irrationality assertion about
Catalan's constant.
