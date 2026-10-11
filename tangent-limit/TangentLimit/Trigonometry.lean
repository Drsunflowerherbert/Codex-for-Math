import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Tangent bounds from distance to an odd multiple of π/2

These lemmas are independent of the Diophantine hypothesis.  The pole index is
a natural number, so its associated odd integer is `2 * k + 1`.
-/

namespace TangentLimit

/-- Translating by an odd multiple of `π / 2` turns cosine into sine,
up to a sign which disappears under absolute value. -/
theorem abs_cos_eq_abs_sin_offset (x : ℝ) (k : ℕ) :
    |Real.cos x| =
      |Real.sin (x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2)| := by
  have hoffset : x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2 =
      (x - Real.pi / 2) - (k : ℝ) * Real.pi := by
    push_cast
    ring
  rw [hoffset, Real.sin_sub_nat_mul_pi, Real.sin_sub_pi_div_two,
    abs_mul, abs_pow]
  simp

/-- The sine chord bound controls cosine by the distance to the selected pole. -/
theorem chord_cos_bound (x : ℝ) (k : ℕ)
    (hb : |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2| ≤ Real.pi / 2) :
    (2 / Real.pi) * |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2| ≤
      |Real.cos x| := by
  rw [abs_cos_eq_abs_sin_offset x k]
  exact Real.mul_abs_le_abs_sin hb

/-- A positive lower bound for the absolute cosine gives an upper bound for
the absolute tangent. -/
theorem tan_le_of_cos_lower_bound {x B : ℝ}
    (hB : 0 < B) (hcos : B ≤ |Real.cos x|) :
    |Real.tan x| ≤ 1 / B := by
  have hcos_pos : 0 < |Real.cos x| := hB.trans_le hcos
  rw [Real.tan_eq_sin_div_cos, abs_div]
  calc
    |Real.sin x| / |Real.cos x| ≤ 1 / |Real.cos x| :=
      div_le_div_of_nonneg_right (Real.abs_sin_le_one x) (le_of_lt hcos_pos)
    _ ≤ 1 / B :=
      div_le_div_of_nonneg_left (by norm_num : (0 : ℝ) ≤ 1) hB hcos

/-- Within half a period, a positive pole distance gives the usual reciprocal
distance estimate for tangent. -/
theorem tan_le_of_pole_distance {x : ℝ} {k : ℕ}
    (hb : |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2| ≤ Real.pi / 2)
    (hd : 0 < |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2|) :
    |Real.tan x| ≤
      Real.pi / (2 * |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2|) := by
  have hB : 0 < (2 / Real.pi) *
      |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2| :=
    mul_pos (div_pos (by norm_num) Real.pi_pos) hd
  have h := tan_le_of_cos_lower_bound hB (chord_cos_bound x k hb)
  have hinv : 1 / ((2 / Real.pi) *
      |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2|) =
      Real.pi / (2 * |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2|) := by
    field_simp [ne_of_gt Real.pi_pos, ne_of_gt hd]
  simpa only [hinv] using h

end TangentLimit
