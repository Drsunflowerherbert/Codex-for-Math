import TangentLimit.Limit
import Mathlib.Analysis.PSeries
import Mathlib.Analysis.Normed.Group.InfiniteSum
import Mathlib.Tactic.NormNum

/-!
# Conditional absolute convergence of the integer tangent series

The explicit hypothesis `PiDiophantine` is used at exponent `5 / 2`.
The nearest-pole estimate then gives a summable `n ^ (-3 / 2)` majorant.
-/

namespace TangentLimit

open Filter

/-- The exponent `5 / 2` instance gives a summable eventual majorant after
division by the cube of the positive integer argument. -/
theorem eventual_abs_tan_div_cube_le_rpow (h : PiDiophantine) :
    ∀ᶠ n : ℕ in atTop,
      |Real.tan (n : ℝ)| / (n : ℝ) ^ 3 ≤
        (Real.pi * (2 : ℝ) ^ (3 / 2 : ℝ)) * (n : ℝ) ^ (-(3 / 2 : ℝ)) := by
  filter_upwards [eventually_tan_le_pole_rpow h (5 / 2) (by norm_num),
    eventually_ge_atTop (1 : ℕ)] with n htan hn
  have hnpos : 0 < (n : ℝ) := by exact_mod_cast (lt_of_lt_of_le Nat.zero_lt_one hn)
  have htan' : |Real.tan (n : ℝ)| ≤ Real.pi * (poleDenom n : ℝ) ^ (3 / 2 : ℝ) := by
    simpa only [show (5 / 2 : ℝ) - 1 = 3 / 2 by norm_num] using htan
  have hqpow : (poleDenom n : ℝ) ^ (3 / 2 : ℝ) ≤
      (2 * (n : ℝ)) ^ (3 / 2 : ℝ) :=
    Real.rpow_le_rpow (Nat.cast_nonneg _) (poleDenom_le_two_mul n hn) (by norm_num)
  have hquot : (n : ℝ) ^ (3 / 2 : ℝ) / (n : ℝ) ^ 3 =
      (n : ℝ) ^ (-(3 / 2 : ℝ)) := by
    rw [← Real.rpow_sub_natCast (ne_of_gt hnpos) (3 / 2 : ℝ) 3]
    norm_num
  calc
    |Real.tan (n : ℝ)| / (n : ℝ) ^ 3 ≤
        (Real.pi * (poleDenom n : ℝ) ^ (3 / 2 : ℝ)) / (n : ℝ) ^ 3 :=
      (div_le_div_iff_of_pos_right (pow_pos hnpos 3)).2 htan'
    _ ≤ (Real.pi * (2 * (n : ℝ)) ^ (3 / 2 : ℝ)) / (n : ℝ) ^ 3 :=
      (div_le_div_iff_of_pos_right (pow_pos hnpos 3)).2
        (mul_le_mul_of_nonneg_left hqpow Real.pi_pos.le)
    _ = (Real.pi * (2 : ℝ) ^ (3 / 2 : ℝ)) *
        ((n : ℝ) ^ (3 / 2 : ℝ) / (n : ℝ) ^ 3) := by
      rw [Real.mul_rpow (by norm_num : (0 : ℝ) ≤ 2) hnpos.le]
      ring
    _ = (Real.pi * (2 : ℝ) ^ (3 / 2 : ℝ)) * (n : ℝ) ^ (-(3 / 2 : ℝ)) := by
      rw [hquot]

/-- Under the explicit hypothesis, the series of nonnegative absolute tangent
terms divided by the integer cube is summable. -/
theorem summable_abs_tan_div_cube (h : PiDiophantine) :
    Summable (fun n : ℕ => |Real.tan (n : ℝ)| / (n : ℝ) ^ 3) := by
  have hp : Summable (fun n : ℕ => (n : ℝ) ^ (-(3 / 2 : ℝ))) :=
    Real.summable_nat_rpow.mpr (by norm_num)
  have hmajor : Summable (fun n : ℕ =>
      (Real.pi * (2 : ℝ) ^ (3 / 2 : ℝ)) * (n : ℝ) ^ (-(3 / 2 : ℝ))) :=
    Summable.mul_left _ hp
  apply hmajor.of_norm_bounded_eventually_nat
  filter_upwards [eventual_abs_tan_div_cube_le_rpow h] with n hn
  have hnonneg : 0 ≤ |Real.tan (n : ℝ)| / (n : ℝ) ^ 3 :=
    div_nonneg (abs_nonneg _) (pow_nonneg (Nat.cast_nonneg _) 3)
  simpa only [Real.norm_eq_abs, abs_of_nonneg hnonneg] using hn

/-- The absolute series enumerated by the positive integers `n+1`. -/
theorem summable_abs_tan_div_cube_positive (h : PiDiophantine) :
    Summable (fun n : ℕ => |Real.tan ((n + 1 : ℕ) : ℝ)| /
      ((n + 1 : ℕ) : ℝ) ^ 3) := by
  exact (summable_nat_add_iff 1).2 (summable_abs_tan_div_cube h)

/-- The natural cube denominator is nonnegative, including the harmless zero
index under Lean's totalized division. -/
theorem abs_tan_div_cube_eq (n : ℕ) :
    |Real.tan (n : ℝ) / (n : ℝ) ^ 3| = |Real.tan (n : ℝ)| / (n : ℝ) ^ 3 := by
  have hden : 0 ≤ (n : ℝ) ^ 3 := pow_nonneg (Nat.cast_nonneg n) 3
  rw [abs_div, abs_of_nonneg hden]

/-- Absolute convergence stated with the absolute value outside the quotient. -/
theorem summable_abs_tan_div_cube_quotient (h : PiDiophantine) :
    Summable (fun n : ℕ => |Real.tan (n : ℝ) / (n : ℝ) ^ 3|) := by
  simpa only [abs_tan_div_cube_eq] using summable_abs_tan_div_cube h

/-- Absolute convergence of the original signed tangent series implies its
ordinary summability. -/
theorem summable_tan_div_cube (h : PiDiophantine) :
    Summable (fun n : ℕ => Real.tan (n : ℝ) / (n : ℝ) ^ 3) := by
  apply Summable.of_norm
  simpa only [Real.norm_eq_abs] using summable_abs_tan_div_cube_quotient h

/-- Absolute convergence of the quotient over explicitly positive arguments. -/
theorem summable_abs_tan_div_cube_quotient_positive (h : PiDiophantine) :
    Summable (fun n : ℕ => |Real.tan ((n + 1 : ℕ) : ℝ) /
      ((n + 1 : ℕ) : ℝ) ^ 3|) := by
  exact (summable_nat_add_iff 1).2 (summable_abs_tan_div_cube_quotient h)

/-- Ordinary convergence over explicitly positive integer arguments. -/
theorem summable_tan_div_cube_positive (h : PiDiophantine) :
    Summable (fun n : ℕ => Real.tan ((n + 1 : ℕ) : ℝ) /
      ((n + 1 : ℕ) : ℝ) ^ 3) := by
  exact (summable_nat_add_iff 1).2 (summable_tan_div_cube h)

end TangentLimit
