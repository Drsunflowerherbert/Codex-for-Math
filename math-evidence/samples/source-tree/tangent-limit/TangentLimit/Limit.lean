import TangentLimit.Diophantine
import TangentLimit.LimitComparison

/-! # The conditional limit, with the Diophantine hypothesis explicit -/

open Filter

namespace TangentLimit

/-- The exponent-three instance of the explicit hypothesis gives quadratic
growth control for the tangent on all sufficiently large integers. -/
theorem eventually_abs_tan_le_quadratic (h : PiDiophantine) :
    ∀ᶠ n : ℕ in atTop, |Real.tan (n : ℝ)| ≤ 4 * Real.pi * (n : ℝ) ^ 2 := by
  filter_upwards [eventually_tan_le_pole_rpow h 3 (by norm_num),
    eventually_ge_atTop (1 : ℕ)] with n htan hn
  have hq := poleDenom_le_two_mul n hn
  have htan' : |Real.tan (n : ℝ)| ≤ Real.pi * (poleDenom n : ℝ) ^ 2 := by
    simpa only [show (3 : ℝ) - 1 = 2 by norm_num, Real.rpow_two] using htan
  calc
    |Real.tan (n : ℝ)| ≤ Real.pi * (poleDenom n : ℝ) ^ 2 := htan'
    _ ≤ Real.pi * (2 * (n : ℝ)) ^ 2 :=
      mul_le_mul_of_nonneg_left
        (pow_le_pow_left₀ (Nat.cast_nonneg _) hq 2) Real.pi_pos.le
    _ = 4 * Real.pi * (n : ℝ) ^ 2 := by ring

/-- Under `PiDiophantine`, `tan(n)/n³` tends to zero along the naturals.
The zero term is harmless; `tan_div_cube_positive_tendsto_zero` states the
same conclusion with explicitly positive integer arguments. -/
theorem tan_div_cube_tendsto_zero (h : PiDiophantine) :
    Tendsto (fun n : ℕ => Real.tan (n : ℝ) / (n : ℝ) ^ 3) atTop (nhds 0) :=
  tendsto_div_cube_of_eventually_abs_le_sq (eventually_abs_tan_le_quadratic h)

/-- The requested limit with positive integer arguments `n+1`. -/
theorem tan_div_cube_positive_tendsto_zero (h : PiDiophantine) :
    Tendsto (fun n : ℕ => Real.tan ((n + 1 : ℕ) : ℝ) /
      ((n + 1 : ℕ) : ℝ) ^ 3) atTop (nhds 0) :=
  (tan_div_cube_tendsto_zero h).comp (tendsto_add_atTop_nat 1)

end TangentLimit
