import Mathlib

namespace FiniteFieldMixing

/-- The scalar estimate converting a fourth-power error bound into a positive
normalized count. -/
theorem threshold_from_fourth_power (p ε : ℝ) (hp : 1 ≤ p)
    (hε : ε ^ 4 ≤ 1 / p) :
    1 / p ^ 2 ≤ (1 - (p - 1) * ε ^ 4) / p := by
  have hp_pos : 0 < p := lt_of_lt_of_le zero_lt_one hp
  have hp_ne : p ≠ 0 := ne_of_gt hp_pos
  have hmul : (p - 1) * ε ^ 4 ≤ (p - 1) * (1 / p) :=
    mul_le_mul_of_nonneg_left hε (sub_nonneg.mpr hp)
  apply (le_div_iff₀ hp_pos).2
  have hid : (1 / p ^ 2) * p = 1 - (p - 1) * (1 / p) := by
    field_simp
    ring
  rw [hid]
  linarith

/-- A rectangular cardinality threshold controls the fourth power of the
square-root Fourier error. -/
theorem sqrt_ratio_fourth_power_le (p n : ℝ) (hp : 1 ≤ p) (hn : 0 < n)
    (hsize : p ^ 3 ≤ n ^ 2) :
    (Real.sqrt (p / n)) ^ 4 ≤ 1 / p := by
  have hp_pos : 0 < p := lt_of_lt_of_le zero_lt_one hp
  have hsqrt : (Real.sqrt (p / n)) ^ 2 = p / n :=
    Real.sq_sqrt (div_nonneg (le_of_lt hp_pos) (le_of_lt hn))
  have hfourth : (Real.sqrt (p / n)) ^ 4 = p ^ 2 / n ^ 2 := by
    calc
      (Real.sqrt (p / n)) ^ 4 = ((Real.sqrt (p / n)) ^ 2) ^ 2 := by ring
      _ = (p / n) ^ 2 := by rw [hsqrt]
      _ = p ^ 2 / n ^ 2 := div_pow _ _ _
  rw [hfourth]
  apply (div_le_div_iff₀ (sq_pos_of_pos hn) hp_pos).2
  nlinarith [hsize]

/-- If the product of two cardinalities is at least `p^(3/2)`, the
fourth-power spectral estimate leaves at least `1 / p²`. -/
theorem rectangular_threshold (p n : ℝ) (hp : 1 ≤ p) (hn : 0 < n)
    (hsize : p ^ 3 ≤ n ^ 2) :
    1 / p ^ 2 ≤ (1 - (p - 1) * (Real.sqrt (p / n)) ^ 4) / p :=
  threshold_from_fourth_power p (Real.sqrt (p / n)) hp
    (sqrt_ratio_fourth_power_le p n hp hn hsize)

/-- The rectangular Fourier error specializes to `sqrt p / h` when both
cardinalities are `h`. -/
theorem sqrt_div_mul_self (p h : ℝ) (hp : 0 ≤ p) (hh : 0 < h) :
    Real.sqrt (p / (h * h)) = Real.sqrt p / h := by
  rw [Real.sqrt_div hp, Real.sqrt_mul_self (le_of_lt hh)]

/-- The diagonal fourth-power cardinality threshold. -/
theorem diagonal_threshold (p h : ℝ) (hp : 1 ≤ p) (hh : 0 < h)
    (hsize : p ^ 3 ≤ h ^ 4) :
    1 / p ^ 2 ≤ (1 - (p - 1) * (Real.sqrt p / h) ^ 4) / p := by
  have hhprod : 0 < h * h := mul_pos hh hh
  have hrect : p ^ 3 ≤ (h * h) ^ 2 := by nlinarith [hsize]
  simpa only [sqrt_div_mul_self p h (by linarith) hh] using
    rectangular_threshold p (h * h) hp hhprod hrect

/-- Natural-number cardinalities can be used directly, and positivity of the
cardinality follows from the threshold. -/
theorem rectangular_threshold_nat (p n : ℕ) (hp : 1 ≤ p)
    (hsize : p ^ 3 ≤ n ^ 2) :
    1 / (p : ℝ) ^ 2 ≤
      (1 - ((p : ℝ) - 1) * (Real.sqrt ((p : ℝ) / (n : ℝ))) ^ 4) / (p : ℝ) := by
  have hp_pos : 0 < p := lt_of_lt_of_le Nat.zero_lt_one hp
  have hn_pow : 0 < n ^ 2 := lt_of_lt_of_le (pow_pos hp_pos 3) hsize
  have hn_pos : 0 < n := by
    by_contra hn
    have hn_zero : n = 0 := Nat.eq_zero_of_not_pos hn
    simp [hn_zero] at hn_pow
  apply rectangular_threshold p n
  · exact_mod_cast hp
  · exact_mod_cast hn_pos
  · exact_mod_cast hsize

/-- Natural-number version of the diagonal cardinality threshold. -/
theorem diagonal_threshold_nat (p h : ℕ) (hp : 1 ≤ p)
    (hsize : p ^ 3 ≤ h ^ 4) :
    1 / (p : ℝ) ^ 2 ≤
      (1 - ((p : ℝ) - 1) * (Real.sqrt (p : ℝ) / (h : ℝ)) ^ 4) / (p : ℝ) := by
  have hp_pos : 0 < p := lt_of_lt_of_le Nat.zero_lt_one hp
  have hh_pow : 0 < h ^ 4 := lt_of_lt_of_le (pow_pos hp_pos 3) hsize
  have hh_pos : 0 < h := by
    by_contra hh
    have hh_zero : h = 0 := Nat.eq_zero_of_not_pos hh
    simp [hh_zero] at hh_pow
  apply diagonal_threshold p h
  · exact_mod_cast hp
  · exact_mod_cast hh_pos
  · exact_mod_cast hsize

end FiniteFieldMixing
