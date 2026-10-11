import MixedMoments.Cancellation

noncomputable section

namespace MixedMoments

/-- Formal inverse-square-root series, with odd coefficients explicitly zero.
An analytic evaluation identity is a separate theorem. -/
def inverseSqrtFormalSeries : PowerSeries ℚ := PowerSeries.mk (fun n => kernel (n : ℤ))

def formalContactSeries (P D : Polynomial ℚ) : PowerSeries ℚ :=
  PowerSeries.X * (P : PowerSeries ℚ) * inverseSqrtFormalSeries - (D : PowerSeries ℚ)

theorem contactCoefficient_add (P Q : Polynomial ℚ) (j : ℕ) :
    contactCoefficient (P + Q) j = contactCoefficient P j + contactCoefficient Q j := by
  change (P + Q).sum (fun i p => p * kernel ((j : ℤ) - (i : ℤ) - 1)) =
    P.sum (fun i p => p * kernel ((j : ℤ) - (i : ℤ) - 1)) +
    Q.sum (fun i p => p * kernel ((j : ℤ) - (i : ℤ) - 1))
  exact Polynomial.sum_add_index P Q _ (by intro i; simp) (by intro i p q; ring)

theorem contactCoefficient_monomial (i j : ℕ) (p : ℚ) :
    contactCoefficient (Polynomial.monomial i p) j =
      p * kernel ((j : ℤ) - (i : ℤ) - 1) := by
  change (Polynomial.monomial i p).sum
    (fun k q => q * kernel ((j : ℤ) - (k : ℤ) - 1)) = _
  rw [Polynomial.sum_monomial_index]
  simp

theorem coeff_shifted_inverseSqrtFormalSeries (i j : ℕ) :
    PowerSeries.coeff j
      (PowerSeries.X ^ (i + 1) * inverseSqrtFormalSeries) =
        kernel ((j : ℤ) - (i : ℤ) - 1) := by
  rw [PowerSeries.coeff_X_pow_mul']
  by_cases h : i + 1 ≤ j
  · rw [if_pos h, inverseSqrtFormalSeries, PowerSeries.coeff_mk]
    congr 1
    omega
  · rw [if_neg h]
    exact (kernel_of_neg _ (by omega)).symm

theorem contactCoefficient_eq_powerSeries_coeff (P : Polynomial ℚ) (j : ℕ) :
    contactCoefficient P j =
      PowerSeries.coeff j
        (PowerSeries.X * (P : PowerSeries ℚ) * inverseSqrtFormalSeries) := by
  induction P using Polynomial.induction_on' with
  | add P Q ihP ihQ =>
    rw [contactCoefficient_add, Polynomial.coe_add, mul_add, add_mul, map_add,
      ← ihP, ← ihQ]
  | monomial i p =>
    rw [contactCoefficient_monomial, ← Polynomial.C_mul_X_pow_eq_monomial,
      Polynomial.coe_mul, Polynomial.coe_C, Polynomial.coe_pow, Polynomial.coe_X]
    have h : PowerSeries.X * (PowerSeries.C p * PowerSeries.X ^ i) *
        inverseSqrtFormalSeries =
          PowerSeries.C p * (PowerSeries.X ^ (i + 1) * inverseSqrtFormalSeries) := by
      rw [pow_succ]
      ring
    rw [h, PowerSeries.coeff_C_mul, coeff_shifted_inverseSqrtFormalSeries]

theorem polynomialDefect_eq_formalContactSeries_coeff (P D : Polynomial ℚ) (j : ℕ) :
    polynomialDefect P D j = PowerSeries.coeff j (formalContactSeries P D) := by
  simp only [polynomialDefect, formalContactSeries, map_sub, Polynomial.coeff_coe,
    contactCoefficient_eq_powerSeries_coeff]

theorem coefficientContact_iff_formalContactSeries (P D : Polynomial ℚ) (L : ℕ) :
    CoefficientContact P D L ↔
      ∀ j < L, PowerSeries.coeff j (formalContactSeries P D) = 0 := by
  simp only [CoefficientContact, polynomialDefect_eq_formalContactSeries_coeff]

end MixedMoments
