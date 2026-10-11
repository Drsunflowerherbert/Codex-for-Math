import Mathlib.Analysis.Normed.Group.Continuity
import Mathlib.Order.Filter.AtTopBot.Archimedean
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Tactic.FieldSimp

namespace TangentLimit

open Filter Topology

/-- An eventual quadratic bound implies decay after division by a cube.

The bound itself forces any admissible constant to have the required sign;
no separate nonnegativity assumption on `C` is needed. -/
theorem tendsto_div_cube_of_eventually_abs_le_sq {f : ℕ → ℝ} {C : ℝ}
    (h : ∀ᶠ n in atTop, |f n| ≤ C * (n : ℝ) ^ 2) :
    Tendsto (fun n => f n / (n : ℝ) ^ 3) atTop (nhds 0) := by
  have hcomparison : ∀ᶠ n in atTop,
      ‖f n / (n : ℝ) ^ 3‖ ≤ C / (n : ℝ) := by
    filter_upwards [h, eventually_ge_atTop 1] with n hbound hn
    have hnpos : 0 < (n : ℝ) := by
      exact Nat.cast_pos.mpr (lt_of_lt_of_le Nat.zero_lt_one hn)
    rw [Real.norm_eq_abs, abs_div, abs_of_pos (pow_pos hnpos 3)]
    calc
      |f n| / (n : ℝ) ^ 3 ≤ (C * (n : ℝ) ^ 2) / (n : ℝ) ^ 3 :=
        (div_le_div_iff_of_pos_right (pow_pos hnpos 3)).2 hbound
      _ = C / (n : ℝ) := by
        field_simp [ne_of_gt hnpos]
  exact squeeze_zero_norm' hcomparison
    (tendsto_const_nhds.div_atTop tendsto_natCast_atTop_atTop)

/-- The positive-integer version obtained by enumerating the indices as `n+1`. -/
theorem tendsto_div_cube_positive_of_eventually_abs_le_sq {f : ℕ → ℝ} {C : ℝ}
    (h : ∀ᶠ n in atTop, |f (n + 1)| ≤ C * ((n + 1 : ℕ) : ℝ) ^ 2) :
    Tendsto (fun n => f (n + 1) / ((n + 1 : ℕ) : ℝ) ^ 3) atTop (nhds 0) := by
  have hbound : ∀ᶠ n in atTop, |f n| ≤ C * (n : ℝ) ^ 2 := by
    obtain ⟨N, hN⟩ := (eventually_atTop.1 h)
    filter_upwards [eventually_ge_atTop (N + 1)] with n hn
    obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hn
    simpa [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using
      hN (N + k) (Nat.le_add_right N k)
  exact (tendsto_div_cube_of_eventually_abs_le_sq hbound).comp
    (tendsto_add_atTop_nat 1)

end TangentLimit
