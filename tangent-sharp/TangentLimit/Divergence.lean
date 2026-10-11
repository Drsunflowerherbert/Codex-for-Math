import TangentLimit.NonPole
import Mathlib.Analysis.PSeries
import Mathlib.Analysis.Normed.Group.InfiniteSum
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Unconditional divergence of the absolute tangent series

Consecutive integer arguments cannot both have arbitrarily small tangent:
their absolute tangents sum to at least `sin 1`.  Comparing the resulting
weighted pairs with the harmonic series proves divergence at every real
exponent at most one.  Only the proved irrationality of π used in `NonPole`
is needed; no Diophantine hypothesis is present.
-/

namespace TangentLimit

/-- At a non-pole, division by a cosine of absolute value at most one can
only increase the absolute sine. -/
theorem abs_sin_le_abs_tan {x : ℝ} (hx : Real.cos x ≠ 0) :
    |Real.sin x| ≤ |Real.tan x| := by
  rw [Real.tan_eq_sin_div_cos, abs_div]
  apply (le_div_iff₀ (abs_pos.mpr hx)).2
  nlinarith [abs_nonneg (Real.sin x), Real.abs_cos_le_one x]

/-- A positive constant in the adjacent-tangent lower bound. -/
theorem sin_one_pos : 0 < Real.sin 1 :=
  Real.sin_pos_of_pos_of_lt_pi (by norm_num) (by linarith [Real.two_le_pi])

/-- The sine subtraction formula and `|cos| ≤ 1` give an adjacent lower
bound at any two non-poles separated by one. -/
theorem sin_one_le_abs_tan_add {x : ℝ}
    (hx : Real.cos x ≠ 0) (hx1 : Real.cos (x + 1) ≠ 0) :
    Real.sin 1 ≤ |Real.tan x| + |Real.tan (x + 1)| := by
  have hsin : |Real.sin 1| ≤ |Real.sin (x + 1)| + |Real.sin x| := by
    calc
      |Real.sin 1| = |Real.sin ((x + 1) - x)| := by congr 2; ring
      _ = |Real.sin (x + 1) * Real.cos x - Real.cos (x + 1) * Real.sin x| := by
        rw [Real.sin_sub]
      _ ≤ |Real.sin (x + 1) * Real.cos x| + |Real.cos (x + 1) * Real.sin x| :=
        abs_sub _ _
      _ = |Real.sin (x + 1)| * |Real.cos x| +
          |Real.cos (x + 1)| * |Real.sin x| := by rw [abs_mul, abs_mul]
      _ ≤ |Real.sin (x + 1)| + |Real.sin x| := by
        nlinarith [Real.abs_cos_le_one x, Real.abs_cos_le_one (x + 1),
          abs_nonneg (Real.sin x), abs_nonneg (Real.sin (x + 1))]
  have h := add_le_add (abs_sin_le_abs_tan hx1) (abs_sin_le_abs_tan hx)
  rw [abs_of_nonneg sin_one_pos.le] at hsin
  linarith

/-- In particular, the lower bound holds at every consecutive pair of
natural-number arguments, unconditionally. -/
theorem sin_one_le_abs_tan_nat_add (n : ℕ) :
    Real.sin 1 ≤ |Real.tan (n : ℝ)| + |Real.tan ((n + 1 : ℕ) : ℝ)| := by
  have h := sin_one_le_abs_tan_add (cos_natCast_ne_zero n)
    (by simpa only [Nat.cast_add, Nat.cast_one] using cos_natCast_ne_zero (n + 1))
  simpa only [Nat.cast_add, Nat.cast_one] using h

/-- The absolute tangent series at exponent one diverges.  If it were
summable, adding its one-step shift and using the adjacent lower bound would
make a positive constant times the harmonic series summable. -/
theorem not_summable_abs_tan_div_positive :
    ¬ Summable (fun n : ℕ => |Real.tan ((n + 1 : ℕ) : ℝ)| /
      ((n + 1 : ℕ) : ℝ)) := by
  intro h
  have hshift : Summable (fun n : ℕ => |Real.tan ((n + 2 : ℕ) : ℝ)| /
      ((n + 2 : ℕ) : ℝ)) := by
    simpa only [Nat.add_assoc, show (1 + 1 : ℕ) = 2 by rfl] using
      (summable_nat_add_iff 1).2 h
  have hmajor := h.add hshift
  have hcomparison : Summable (fun n : ℕ => Real.sin 1 / ((n + 2 : ℕ) : ℝ)) := by
    apply hmajor.of_nonneg_of_le
    · intro n
      exact div_nonneg sin_one_pos.le (Nat.cast_nonneg _)
    · intro n
      have hn1 : 0 < ((n + 1 : ℕ) : ℝ) := by positivity
      have hn12 : ((n + 1 : ℕ) : ℝ) ≤ ((n + 2 : ℕ) : ℝ) := by
        exact_mod_cast (show n + 1 ≤ n + 2 by omega)
      have hpair : Real.sin 1 ≤ |Real.tan ((n + 1 : ℕ) : ℝ)| +
          |Real.tan ((n + 2 : ℕ) : ℝ)| := by
        simpa only [Nat.add_assoc, show (1 + 1 : ℕ) = 2 by rfl] using
          sin_one_le_abs_tan_nat_add (n + 1)
      calc
        Real.sin 1 / ((n + 2 : ℕ) : ℝ) ≤
            (|Real.tan ((n + 1 : ℕ) : ℝ)| +
              |Real.tan ((n + 2 : ℕ) : ℝ)|) / ((n + 2 : ℕ) : ℝ) :=
          div_le_div_of_nonneg_right hpair (Nat.cast_nonneg _)
        _ = |Real.tan ((n + 1 : ℕ) : ℝ)| / ((n + 2 : ℕ) : ℝ) +
            |Real.tan ((n + 2 : ℕ) : ℝ)| / ((n + 2 : ℕ) : ℝ) := add_div _ _ _
        _ ≤ |Real.tan ((n + 1 : ℕ) : ℝ)| / ((n + 1 : ℕ) : ℝ) +
            |Real.tan ((n + 2 : ℕ) : ℝ)| / ((n + 2 : ℕ) : ℝ) :=
          add_le_add_right
            (div_le_div_of_nonneg_left (abs_nonneg _) hn1 hn12) _
  have hharm : Summable (fun n : ℕ => 1 / ((n + 2 : ℕ) : ℝ)) := by
    apply (summable_mul_left_iff (ne_of_gt sin_one_pos)).1
    simpa only [mul_one_div] using hcomparison
  exact Real.not_summable_one_div_natCast ((summable_nat_add_iff 2).1 hharm)

/-- Unconditional divergence of the absolute tangent series over positive
integers for every real exponent at most one. -/
theorem not_summable_abs_tan_div_rpow_positive (s : ℝ) (hs : s ≤ 1) :
    ¬ Summable (fun n : ℕ => |Real.tan ((n + 1 : ℕ) : ℝ)| /
      ((n + 1 : ℕ) : ℝ) ^ s) := by
  intro h
  apply not_summable_abs_tan_div_positive
  apply h.of_nonneg_of_le
  · intro n
    exact div_nonneg (abs_nonneg _) (Nat.cast_nonneg _)
  · intro n
    have hn1 : 1 ≤ ((n + 1 : ℕ) : ℝ) := by
      exact_mod_cast (show 1 ≤ n + 1 by omega)
    have hnpos : 0 < ((n + 1 : ℕ) : ℝ) := by positivity
    have hpow : ((n + 1 : ℕ) : ℝ) ^ s ≤ ((n + 1 : ℕ) : ℝ) := by
      simpa only [Real.rpow_one] using Real.rpow_le_rpow_of_exponent_le hn1 hs
    exact div_le_div_of_nonneg_left (abs_nonneg _)
      (Real.rpow_pos_of_pos hnpos s) hpow

end TangentLimit
