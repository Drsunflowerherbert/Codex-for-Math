import MixedMoments.FormalContact
import Mathlib.RingTheory.PowerSeries.Derivative

/-! The central-binomial formal series is the inverse square root with constant
term one. This is an algebraic identity; real analytic evaluation is separate. -/

noncomputable section
namespace MixedMoments

@[simp] theorem inverseSqrtFormalSeries_constantCoeff :
    PowerSeries.constantCoeff inverseSqrtFormalSeries = 1 := by
  simp [inverseSqrtFormalSeries]

@[simp] theorem inverseSqrtFormalSeries_coeff (n : ℕ) :
    PowerSeries.coeff n inverseSqrtFormalSeries = kernel (n : ℤ) := by
  simp [inverseSqrtFormalSeries]

theorem inverseSqrtFormalSeries_differential :
    (1 - PowerSeries.X ^ 2) * PowerSeries.derivative ℚ inverseSqrtFormalSeries =
      PowerSeries.X * inverseSqrtFormalSeries := by
  ext n
  rw [sub_mul, one_mul, map_sub, PowerSeries.coeff_derivative]
  nth_rw 2 [← pow_one (PowerSeries.X : PowerSeries ℚ)]
  rw [PowerSeries.coeff_X_pow_mul', PowerSeries.coeff_X_pow_mul']
  rcases n with _ | _ | n
  · norm_num [inverseSqrtFormalSeries_coeff, kernel]
  · norm_num [PowerSeries.coeff_derivative, inverseSqrtFormalSeries_coeff, kernel, Int.toNat, central]
  · have hs := kernel_step (n + 1)
    simp only [Nat.cast_add, Nat.cast_one] at hs
    simp only [show 2 ≤ n + 1 + 1 by omega, show 1 ≤ n + 1 + 1 by omega,
      if_true, show n + 1 + 1 - 2 = n by omega, show n + 1 + 1 - 1 = n + 1 by omega,
      PowerSeries.coeff_derivative, inverseSqrtFormalSeries_coeff, Nat.cast_add, Nat.cast_one]
    have he : (n : ℤ) + 1 + 1 + 1 = (n : ℤ) + 1 + 2 := by ring
    rw [he]
    nlinarith [hs]

theorem inverseSqrtFormalSeries_square :
    (1 - PowerSeries.X ^ 2) * inverseSqrtFormalSeries ^ 2 = (1 : PowerSeries ℚ) := by
  apply PowerSeries.derivative.ext
  · have hd := inverseSqrtFormalSeries_differential
    have hmul := congrArg (fun q : PowerSeries ℚ => 2 * inverseSqrtFormalSeries * q) hd
    simp only [pow_two] at *
    simp only [Derivation.map_one_eq_zero, map_sub, Derivation.leibniz, PowerSeries.derivative_X,
      mul_one, smul_eq_mul]
    linear_combination hmul
  · simp

end MixedMoments
