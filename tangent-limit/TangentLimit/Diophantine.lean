import TangentLimit.Hypothesis
import TangentLimit.Trigonometry
import TangentLimit.NearestPole
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-!
# Diophantine lower bounds for distances to tangent poles

The hypothesis `PiDiophantine` stays explicit.  The first lemmas are independent
of the nearest-pole construction and apply to any positive real denominator.
-/

namespace TangentLimit

/-- Algebraically express the distance to a pole as an approximation error. -/
theorem pole_distance_identity (x q : ℝ) (hq : 0 < q) :
    |x - q * Real.pi / 2| = (q / 2) * |Real.pi - (2 * x) / q| := by
  have heq : x - q * Real.pi / 2 = -(q / 2) * (Real.pi - (2 * x) / q) := by
    field_simp [ne_of_gt hq]
    ring
  rw [heq, abs_mul, abs_neg, abs_of_pos (div_pos hq (by norm_num))]

/-- A denominator approximation bound gives a lower bound for pole distance. -/
theorem pole_distance_lower_bound (x q ν : ℝ) (hq : 0 < q)
    (happrox : q ^ (-ν) ≤ |Real.pi - (2 * x) / q|) :
    (1 / 2 : ℝ) * q ^ (1 - ν) ≤ |x - q * Real.pi / 2| := by
  rw [pole_distance_identity x q hq]
  have hmul : (q / 2) * q ^ (-ν) ≤ (q / 2) * |Real.pi - (2 * x) / q| :=
    mul_le_mul_of_nonneg_left happrox
      (le_of_lt (div_pos hq (by norm_num : (0 : ℝ) < 2)))
  rw [sub_eq_add_neg, Real.rpow_add hq, Real.rpow_one]
  calc
    (1 / 2 : ℝ) * (q * q ^ (-ν)) = (q / 2) * q ^ (-ν) := by ring
    _ ≤ (q / 2) * |Real.pi - (2 * x) / q| := hmul

/-- The positive reciprocal of the cosine lower bound has the growth exponent. -/
theorem reciprocal_pole_power (q ν : ℝ) (hq : 0 < q) :
    1 / (q ^ (1 - ν) / Real.pi) = Real.pi * q ^ (ν - 1) := by
  have he : 1 - ν = -(ν - 1) := by ring
  rw [he, Real.rpow_neg (le_of_lt hq)]
  simp [div_eq_mul_inv, mul_comm]

/-- The explicit hypothesis supplies a lower bound at every sufficiently large
positive integer denominator, uniformly in the natural-number argument. -/
theorem pole_distance_lower_bound_of_piDiophantine (h : PiDiophantine)
    (ν : ℝ) (hν : 2 < ν) :
    ∃ Q : ℕ, ∀ n q : ℕ, Q ≤ q → 0 < q →
      (1 / 2 : ℝ) * (q : ℝ) ^ (1 - ν) ≤
        |(n : ℝ) - (q : ℝ) * Real.pi / 2| := by
  obtain ⟨Q, hQ⟩ := h ν hν
  refine ⟨Q, ?_⟩
  intro n q hQq hq
  apply pole_distance_lower_bound (n : ℝ) (q : ℝ) ν (by exact_mod_cast hq)
  simpa only [Int.cast_mul, Int.cast_ofNat, Int.cast_natCast] using
    hQ q hQq hq (2 * (n : ℤ))

/-- Combine the chord estimate and a denominator approximation bound. -/
theorem tan_le_pole_power (x ν : ℝ) (k : ℕ)
    (hb : |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2| ≤ Real.pi / 2)
    (happrox : ((2 * k + 1 : ℕ) : ℝ) ^ (-ν) ≤
      |Real.pi - (2 * x) / ((2 * k + 1 : ℕ) : ℝ)|) :
    |Real.tan x| ≤ Real.pi * ((2 * k + 1 : ℕ) : ℝ) ^ (ν - 1) := by
  have hq : (0 : ℝ) < ((2 * k + 1 : ℕ) : ℝ) := by positivity
  have hd := pole_distance_lower_bound x ((2 * k + 1 : ℕ) : ℝ) ν hq happrox
  have hmul := mul_le_mul_of_nonneg_left hd
    (le_of_lt (div_pos (by norm_num : (0 : ℝ) < 2) Real.pi_pos))
  have hcos : ((2 * k + 1 : ℕ) : ℝ) ^ (1 - ν) / Real.pi ≤ |Real.cos x| := by
    calc
      _ = (2 / Real.pi) * ((1 / 2 : ℝ) *
          ((2 * k + 1 : ℕ) : ℝ) ^ (1 - ν)) := by ring
      _ ≤ (2 / Real.pi) *
          |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2| := hmul
      _ ≤ |Real.cos x| := chord_cos_bound x k hb
  have hB : 0 < ((2 * k + 1 : ℕ) : ℝ) ^ (1 - ν) / Real.pi :=
    div_pos (Real.rpow_pos_of_pos hq _) Real.pi_pos
  have ht := tan_le_of_cos_lower_bound hB hcos
  simpa only [reciprocal_pole_power _ ν hq] using ht

/-- The hypothesis produces an eventual tangent growth bound at the nearest
odd denominator.  No proof of `PiDiophantine` is asserted. -/
theorem eventually_tan_le_pole_rpow (h : PiDiophantine)
    (ν : ℝ) (hν : 2 < ν) :
    ∀ᶠ n : ℕ in Filter.atTop,
      |Real.tan (n : ℝ)| ≤ Real.pi * (poleDenom n : ℝ) ^ (ν - 1) := by
  obtain ⟨Q, hQ⟩ := h ν hν
  filter_upwards [eventually_poleDenom_ge Q] with n hn
  have happrox : (poleDenom n : ℝ) ^ (-ν) ≤
      |Real.pi - (2 * (n : ℝ)) / (poleDenom n : ℝ)| := by
    simpa only [Int.cast_mul, Int.cast_ofNat, Int.cast_natCast] using
      hQ (poleDenom n) hn (poleDenom_pos n) (2 * (n : ℤ))
  exact tan_le_pole_power (n : ℝ) ν (poleIndex n)
    (abs_poleOffset_le n) happrox

end TangentLimit
