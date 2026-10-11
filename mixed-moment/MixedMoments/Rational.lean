import Mathlib.Data.Rat.Lemmas
import Mathlib.Data.Int.Basic
import Mathlib.Data.Nat.Choose.Central
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# Rational mixed-moment arrays

This file constructs the exact rational arrays. The definitions do not assert
that these arrays are equal to analytic integrals. Integer differences in the
Taylor kernel are deliberately kept as integers, including negative values.
-/

namespace MixedMoments

open scoped BigOperators

/-- The normalized central binomial sequence, specified by its ratio. -/
def central : ℕ → ℚ
  | 0 => 1
  | n + 1 => central n * (2 * (n : ℚ) + 1) / (2 * (n : ℚ) + 2)

@[simp] theorem central_zero : central 0 = 1 := rfl

theorem central_succ_ratio (n : ℕ) :
    central (n + 1) = central n * (2 * (n : ℚ) + 1) / (2 * (n : ℚ) + 2) := rfl

theorem central_pos (n : ℕ) : 0 < central n := by
  induction n with
  | zero => norm_num [central]
  | succ n ih =>
      rw [central_succ_ratio]
      exact div_pos (mul_pos ih (by positivity)) (by positivity)

theorem central_ne_zero (n : ℕ) : central n ≠ 0 := ne_of_gt (central_pos n)

theorem central_le_one (n : ℕ) : central n ≤ 1 := by
  induction n with
  | zero => norm_num [central]
  | succ n ih =>
      rw [central_succ_ratio]
      apply (div_le_iff₀ (show 0 < 2 * (n : ℚ) + 2 by positivity)).2
      have h := mul_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr ih)
        (show 0 ≤ 2 * (n : ℚ) + 1 by positivity)
      nlinarith only [h]

theorem central_succ_mul (n : ℕ) :
    (2 * (n : ℚ) + 2) * central (n + 1) = (2 * (n : ℚ) + 1) * central n := by
  rw [central_succ_ratio]
  have h : 2 * (n : ℚ) + 2 ≠ 0 := by positivity
  field_simp

theorem central_eq_centralBinom (n : ℕ) :
    central n = (Nat.centralBinom n : ℚ) / 4 ^ n := by
  induction n with
  | zero => norm_num [central]
  | succ n ih =>
      rw [central_succ_ratio, ih]
      have hcast := congrArg (fun k : ℕ => (k : ℚ))
        (Nat.succ_mul_centralBinom_succ n)
      push_cast at hcast
      have hn : (n : ℚ) + 1 ≠ 0 := by positivity
      have hrec : (Nat.centralBinom (n + 1) : ℚ) =
          (2 * (2 * (n : ℚ) + 1) * (Nat.centralBinom n : ℚ)) /
            ((n : ℚ) + 1) := by
        apply (eq_div_iff hn).2
        nlinarith only [hcast]
      rw [hrec, pow_succ]
      have h4 : (4 : ℚ) ^ n ≠ 0 := by positivity
      have hden : 2 * (n : ℚ) + 2 ≠ 0 := by positivity
      field_simp
      ring

theorem central_eq_choose (n : ℕ) :
    central n = (Nat.choose (2 * n) n : ℚ) / 4 ^ n :=
  central_eq_centralBinom n

/-- Zero-extension of the central sequence to negative and odd differences. -/
def kernel (d : ℤ) : ℚ :=
  if d < 0 then 0 else if d % 2 = 0 then central (d.toNat / 2) else 0

theorem kernel_of_neg (d : ℤ) (h : d < 0) : kernel d = 0 := by
  simp [kernel, h]

theorem kernel_of_odd (d : ℤ) (h : d % 2 ≠ 0) : kernel d = 0 := by
  simp [kernel, h]

@[simp] theorem kernel_zero : kernel 0 = 1 := by norm_num [kernel, central]

theorem kernel_even (n : ℕ) : kernel (2 * (n : ℤ)) = central n := by
  have hcast : 2 * (n : ℤ) = ((2 * n : ℕ) : ℤ) := by norm_cast
  have hd : ¬ 2 * (n : ℤ) < 0 := by omega
  have he : (2 * (n : ℤ)) % 2 = 0 := by omega
  rw [kernel, if_neg hd, if_pos he, hcast, Int.toNat_natCast]
  congr 1
  omega

theorem kernel_odd (n : ℕ) : kernel (2 * (n : ℤ) + 1) = 0 := by
  apply kernel_of_odd
  omega

theorem kernel_step (n : ℕ) :
    ((n : ℚ) + 2) * kernel ((n : ℤ) + 2) =
      ((n : ℚ) + 1) * kernel (n : ℤ) := by
  by_cases h : n % 2 = 0
  · have hn : n = 2 * (n / 2) := by omega
    have hx : (n : ℤ) + 2 = 2 * ((n / 2 + 1 : ℕ) : ℤ) := by omega
    have hy : (n : ℤ) = 2 * ((n / 2 : ℕ) : ℤ) := by omega
    have hr : (n : ℚ) = 2 * ((n / 2 : ℕ) : ℚ) := by exact_mod_cast hn
    rw [hx, hy, kernel_even, kernel_even, hr]
    exact central_succ_mul (n / 2)
  · have hx : (n : ℤ) + 2 = 2 * ((n / 2 + 1 : ℕ) : ℤ) + 1 := by omega
    have hy : (n : ℤ) = 2 * ((n / 2 : ℕ) : ℤ) + 1 := by omega
    rw [hx, hy, kernel_odd, kernel_odd]
    simp

theorem kernel_shifted_step (n : ℕ) :
    ((n : ℚ) + 1) * kernel ((n : ℤ) + 1) =
      (n : ℚ) * kernel ((n : ℤ) - 1) := by
  cases n with
  | zero => norm_num [kernel]
  | succ n =>
      have h := kernel_step n
      simpa only [Nat.cast_add, Nat.cast_one, add_sub_cancel_right, add_assoc,
        show (1 : ℚ) + 1 = 2 by norm_num, show (1 : ℤ) + 1 = 2 by norm_num] using h

/-- The rational basic moments, with the two-step recurrence built in. -/
def moment : ℕ → ℚ
  | 0 => 2
  | 1 => 0
  | n + 2 => ((n : ℚ) + 2) * moment n / ((n : ℚ) + 3)

@[simp] theorem moment_zero : moment 0 = 2 := rfl
@[simp] theorem moment_one : moment 1 = 0 := rfl

theorem moment_step (n : ℕ) :
    moment (n + 2) = ((n : ℚ) + 2) * moment n / ((n : ℚ) + 3) := rfl

theorem moment_recurrence (n : ℕ) :
    ((n : ℚ) + 3) * moment (n + 2) = ((n : ℚ) + 2) * moment n := by
  rw [moment_step]
  have h : (n : ℚ) + 3 ≠ 0 := by positivity
  field_simp

theorem moment_odd (r : ℕ) : moment (2 * r + 1) = 0 := by
  induction r with
  | zero => simp
  | succ r ih =>
      have hi : 2 * (r + 1) + 1 = (2 * r + 1) + 2 := by omega
      rw [hi, moment_step, ih]
      simp

theorem moment_even (r : ℕ) :
    moment (2 * r) = 2 / ((2 * (r : ℚ) + 1) * central r) := by
  induction r with
  | zero => norm_num [moment, central]
  | succ r ih =>
      have hi : 2 * (r + 1) = 2 * r + 2 := by omega
      rw [hi, moment_step, ih, central_succ_ratio]
      push_cast
      have hc := central_ne_zero r
      have h₁ : 2 * (r : ℚ) + 1 ≠ 0 := by positivity
      have h₂ : 2 * (r : ℚ) + 2 ≠ 0 := by positivity
      have h₃ : 2 * (r : ℚ) + 3 ≠ 0 := by positivity
      field_simp
      ring

theorem moment_nonneg (n : ℕ) : 0 ≤ moment n := by
  induction n using Nat.twoStepInduction with
  | zero => norm_num [moment]
  | one => norm_num [moment]
  | more n hn _ =>
      rw [moment_step]
      exact div_nonneg (mul_nonneg (by positivity) hn) (by positivity)

theorem moment_eq_if (n : ℕ) :
    moment n = if n % 2 = 0 then
      2 / (((n : ℚ) + 1) * central (n / 2)) else 0 := by
  by_cases h : n % 2 = 0
  · rw [if_pos h]
    have hn : n = 2 * (n / 2) := by omega
    have hr : (n : ℚ) = 2 * ((n / 2 : ℕ) : ℚ) := by exact_mod_cast hn
    calc
      moment n = moment (2 * (n / 2)) := congrArg moment hn
      _ = 2 / ((2 * ((n / 2 : ℕ) : ℚ) + 1) * central (n / 2)) := moment_even (n / 2)
      _ = 2 / (((n : ℚ) + 1) * central (n / 2)) := by rw [hr]
  · rw [if_neg h]
    have hn : n = 2 * (n / 2) + 1 := by omega
    rw [hn, moment_odd]

/-- An explicit zero-extension; only the index `-1` is used in the source recurrence. -/
def momentExt (n : ℤ) : ℚ := if n < 0 then 0 else moment n.toNat

theorem momentExt_of_neg (n : ℤ) (h : n < 0) : momentExt n = 0 := by
  simp [momentExt, h]

@[simp] theorem momentExt_natCast (n : ℕ) : momentExt (n : ℤ) = moment n := by
  simp [momentExt]

@[simp] theorem momentExt_neg_one : momentExt (-1) = 0 := by
  norm_num [momentExt]

/-- The index-one case uses the explicit `m₋₁ = 0` convention. -/
theorem moment_recurrence_positive (n : ℕ) (hn : 1 ≤ n) :
    ((n : ℚ) + 1) * moment n = (n : ℚ) * momentExt ((n : ℤ) - 2) := by
  cases n with
  | zero => omega
  | succ n =>
      cases n with
      | zero => norm_num [moment, momentExt]
      | succ n =>
          have hi : (((n + 1 + 1 : ℕ) : ℤ) - 2) = (n : ℤ) := by omega
          rw [hi, momentExt_natCast]
          norm_num only [Nat.cast_add, Nat.cast_one, add_assoc]
          exact moment_recurrence n

theorem moment_step_le (n : ℕ) : moment (n + 2) ≤ moment n := by
  rw [moment_step]
  apply (div_le_iff₀ (show 0 < (n : ℚ) + 3 by positivity)).2
  nlinarith only [moment_nonneg n]

theorem moment_le_two (n : ℕ) : moment n ≤ 2 := by
  induction n using Nat.twoStepInduction with
  | zero => norm_num [moment]
  | one => norm_num [moment]
  | more n hn _ => exact (moment_step_le n).trans hn

/-- A rational square bound that yields decay after casting to the reals. -/
theorem moment_sq_le (n : ℕ) : moment n ^ 2 ≤ 8 / ((n : ℚ) + 2) := by
  induction n using Nat.twoStepInduction with
  | zero => norm_num [moment]
  | one => norm_num [moment]
  | more n hn _ =>
      rw [moment_step]
      have h₂ : 0 < (n : ℚ) + 2 := by positivity
      have h₃ : 0 < (n : ℚ) + 3 := by positivity
      have h₄ : 0 < (n : ℚ) + 4 := by positivity
      have hcast : (((n + 2 : ℕ) : ℚ) + 2) = (n : ℚ) + 4 := by push_cast; ring
      rw [hcast, div_pow]
      apply (div_le_div_iff₀ (pow_pos h₃ 2) h₄).2
      have hm : moment n ^ 2 * ((n : ℚ) + 2) ≤ 8 := (le_div_iff₀ h₂).mp hn
      calc
        (((n : ℚ) + 2) * moment n) ^ 2 * ((n : ℚ) + 4) =
            (moment n ^ 2 * ((n : ℚ) + 2)) * (((n : ℚ) + 2) * ((n : ℚ) + 4)) := by ring
        _ ≤ 8 * (((n : ℚ) + 2) * ((n : ℚ) + 4)) :=
          mul_le_mul_of_nonneg_right hm (by positivity)
        _ ≤ 8 * ((n : ℚ) + 3) ^ 2 := by nlinarith

/-- The finite two-step telescoping identity underlying rational tail estimates. -/
theorem moment_telescope_step (n : ℕ) :
    moment (n + 2) / ((n : ℚ) + 2) = moment n - moment (n + 2) := by
  rw [moment_step]
  have h₂ : (n : ℚ) + 2 ≠ 0 := by positivity
  have h₃ : (n : ℚ) + 3 ≠ 0 := by positivity
  field_simp
  ring

theorem moment_telescope_positive (n : ℕ) (hn : 1 ≤ n) :
    moment n / (n : ℚ) = momentExt ((n : ℤ) - 2) - moment n := by
  have h : (n : ℚ) ≠ 0 := by exact_mod_cast (show n ≠ 0 by omega)
  have hr := moment_recurrence_positive n hn
  apply (div_eq_iff h).2
  nlinarith only [hr]

theorem moment_finite_telescope (n N : ℕ) :
    ∑ k ∈ Finset.range N, moment (n + k + 2) / (((n + k : ℕ) : ℚ) + 2) =
      moment n + moment (n + 1) - moment (n + N) - moment (n + N + 1) := by
  induction N with
  | zero => simp
  | succ N ih =>
      rw [Finset.sum_range_succ, moment_telescope_step, ih]
      have hi : n + (N + 1) = n + N + 1 := by omega
      have hj : n + (N + 1) + 1 = n + N + 2 := by omega
      rw [hj, hi]
      ring

/-- Rational part of the minus boundary; the Catalan coordinate is separate. -/
def kminus : ℕ → ℚ
  | 0 => 0
  | 1 => 2
  | n + 2 =>
      (((n : ℚ) + 1) * kminus n + moment n + moment (n + 1)) / ((n : ℚ) + 2)

/-- Rational part of the plus boundary; starts at zero at indices zero and one. -/
def kplus : ℕ → ℚ
  | 0 => 0
  | 1 => 0
  | n + 2 => ((n : ℚ) * kplus n + 2 / ((n : ℚ) + 1)) / ((n : ℚ) + 1)

@[simp] theorem kminus_zero : kminus 0 = 0 := rfl
@[simp] theorem kminus_one : kminus 1 = 2 := rfl
@[simp] theorem kplus_zero : kplus 0 = 0 := rfl
@[simp] theorem kplus_one : kplus 1 = 0 := rfl

theorem kminus_step (n : ℕ) :
    kminus (n + 2) =
      (((n : ℚ) + 1) * kminus n + moment n + moment (n + 1)) / ((n : ℚ) + 2) := rfl

theorem kplus_step (n : ℕ) :
    kplus (n + 2) = ((n : ℚ) * kplus n + 2 / ((n : ℚ) + 1)) / ((n : ℚ) + 1) := rfl

theorem kminus_recurrence (n : ℕ) :
    ((n : ℚ) + 2) * kminus (n + 2) =
      ((n : ℚ) + 1) * kminus n + moment n + moment (n + 1) := by
  rw [kminus_step]
  have h : (n : ℚ) + 2 ≠ 0 := by positivity
  field_simp

theorem kplus_recurrence (n : ℕ) :
    ((n : ℚ) + 1) * kplus (n + 2) =
      (n : ℚ) * kplus n + 2 / ((n : ℚ) + 1) := by
  rw [kplus_step]
  have h : (n : ℚ) + 1 ≠ 0 := by positivity
  field_simp

/-- The positive solution of the homogeneous two-step boundary recurrence. -/
def hStar : ℕ → ℚ
  | 0 => 1
  | 1 => 1
  | n + 2 => ((n : ℚ) + 1) * hStar n / ((n : ℚ) + 2)

@[simp] theorem hStar_zero : hStar 0 = 1 := rfl
@[simp] theorem hStar_one : hStar 1 = 1 := rfl

theorem hStar_step (n : ℕ) :
    hStar (n + 2) = ((n : ℚ) + 1) * hStar n / ((n : ℚ) + 2) := rfl

theorem hStar_pos (n : ℕ) : 0 < hStar n := by
  induction n using Nat.twoStepInduction with
  | zero => norm_num [hStar]
  | one => norm_num [hStar]
  | more n hn _ =>
      rw [hStar_step]
      exact div_pos (mul_pos (by positivity) hn) (by positivity)

theorem hStar_ne_zero (n : ℕ) : hStar n ≠ 0 := ne_of_gt (hStar_pos n)

theorem hStar_even (r : ℕ) : hStar (2 * r) = central r := by
  induction r with
  | zero => norm_num [hStar, central]
  | succ r ih =>
      have hi : 2 * (r + 1) = 2 * r + 2 := by omega
      rw [hi, hStar_step, ih, central_succ_ratio]
      push_cast
      ring

theorem hStar_odd (r : ℕ) :
    hStar (2 * r + 1) = 1 / ((2 * (r : ℚ) + 1) * central r) := by
  induction r with
  | zero => norm_num [hStar, central]
  | succ r ih =>
      have hi : 2 * (r + 1) + 1 = (2 * r + 1) + 2 := by omega
      rw [hi, hStar_step, ih, central_succ_ratio]
      push_cast
      have hc := central_ne_zero r
      have h₁ : 2 * (r : ℚ) + 1 ≠ 0 := by positivity
      have h₂ : 2 * (r : ℚ) + 2 ≠ 0 := by positivity
      have h₃ : 2 * (r : ℚ) + 3 ≠ 0 := by positivity
      field_simp
      ring

theorem kminus_even_closed (r : ℕ) :
    kminus (2 * r) = central r *
      ∑ k ∈ Finset.range r,
        2 / ((2 * ((k : ℚ) + 1)) ^ 2 * central (k + 1) ^ 2) := by
  induction r with
  | zero => simp
  | succ r ih =>
      have hi : 2 * (r + 1) = 2 * r + 2 := by omega
      rw [hi, kminus_step, ih, moment_even, moment_odd,
        Finset.sum_range_succ, central_succ_ratio]
      push_cast
      have hc := central_ne_zero r
      have h₁ : 2 * (r : ℚ) + 1 ≠ 0 := by positivity
      have h₂ : 2 * (r : ℚ) + 2 ≠ 0 := by positivity
      have hr : (r : ℚ) + 1 ≠ 0 := by positivity
      field_simp
      ring

theorem kminus_odd_closed (r : ℕ) :
    kminus (2 * r + 1) = hStar (2 * r + 1) *
      ∑ k ∈ Finset.range (r + 1), 2 / (2 * (k : ℚ) + 1) := by
  induction r with
  | zero => norm_num [hStar]
  | succ r ih =>
      have hi : 2 * (r + 1) + 1 = (2 * r + 1) + 2 := by omega
      have he : 2 * r + 1 + 1 = 2 * (r + 1) := by omega
      have hsum := Finset.sum_range_succ
        (fun k : ℕ => (2 : ℚ) / (2 * (k : ℚ) + 1)) (r + 1)
      rw [hi, kminus_step, ih, moment_odd, he, moment_even, hsum, hStar_step]
      rw [hStar_odd, central_succ_ratio]
      push_cast
      have hc := central_ne_zero r
      have h₁ : 2 * (r : ℚ) + 1 ≠ 0 := by positivity
      have h₂ : 2 * (r : ℚ) + 2 ≠ 0 := by positivity
      have h₃ : 2 * (r : ℚ) + 3 ≠ 0 := by positivity
      field_simp
      ring

theorem kplus_odd_closed (r : ℕ) :
    kplus (2 * r + 1) = hStar (2 * r) *
      ∑ k ∈ Finset.range r,
        2 / ((2 * ((k : ℚ) + 1)) ^ 2 * hStar (2 * (k + 1))) := by
  induction r with
  | zero => simp
  | succ r ih =>
      have hi : 2 * (r + 1) + 1 = (2 * r + 1) + 2 := by omega
      have hh : hStar (2 * (r + 1)) =
          (2 * (r : ℚ) + 1) * hStar (2 * r) / (2 * (r : ℚ) + 2) := by
        have he : 2 * (r + 1) = 2 * r + 2 := by omega
        rw [he, hStar_step]
        push_cast
        ring
      rw [hi, kplus_step, ih, Finset.sum_range_succ, hh]
      push_cast
      have hh₀ := hStar_ne_zero (2 * r)
      have h₁ : 2 * (r : ℚ) + 1 ≠ 0 := by positivity
      have h₂ : 2 * (r : ℚ) + 2 ≠ 0 := by positivity
      have hr : (r : ℚ) + 1 ≠ 0 := by positivity
      field_simp
      ring

theorem kplus_even_closed (r : ℕ) :
    kplus (2 * r + 2) = hStar (2 * r + 1) *
      ∑ k ∈ Finset.range (r + 1),
        2 / ((2 * (k : ℚ) + 1) ^ 2 * hStar (2 * k + 1)) := by
  induction r with
  | zero => norm_num [kplus, hStar]
  | succ r ih =>
      have hi : 2 * (r + 1) + 2 = (2 * r + 2) + 2 := by omega
      have hh : hStar (2 * (r + 1) + 1) =
          (2 * (r : ℚ) + 2) * hStar (2 * r + 1) / (2 * (r : ℚ) + 3) := by
        have he : 2 * (r + 1) + 1 = (2 * r + 1) + 2 := by omega
        rw [he, hStar_step]
        push_cast
        ring
      have hsum := Finset.sum_range_succ
        (fun k : ℕ => (2 : ℚ) / ((2 * (k : ℚ) + 1) ^ 2 * hStar (2 * k + 1)))
        (r + 1)
      rw [hi, kplus_step, ih, hsum, hh]
      push_cast
      have hh₀ := hStar_ne_zero (2 * r + 1)
      have h₂ : 2 * (r : ℚ) + 2 ≠ 0 := by positivity
      have h₃ : 2 * (r : ℚ) + 3 ≠ 0 := by positivity
      field_simp
      ring

/-- Finite diagonal reduction of the rational M array. -/
def mRationalPart (i j : ℕ) : ℚ :=
  if j ≤ i then
    kminus (i - j) - ∑ k ∈ Finset.range j, moment (i - j + k) / ((k : ℚ) + 1)
  else
    kplus (j - i) - ∑ k ∈ Finset.range i, moment k / ((j - i + k + 1 : ℕ) : ℚ)

/-- First-order rational harmonic sums, including the empty sum. -/
def harmonic (n : ℕ) : ℚ := ∑ k ∈ Finset.range n, 1 / ((k : ℚ) + 1)

/-- Second-order rational harmonic sums, including the empty sum. -/
def harmonicTwo (n : ℕ) : ℚ := ∑ k ∈ Finset.range n, 1 / ((k : ℚ) + 1) ^ 2

/-- Rational part of Z; subtraction in the denominator occurs in ℚ. -/
def zRationalPart (i j : ℕ) : ℚ :=
  if i = j then -harmonicTwo i else (harmonic i - harmonic j) / ((i : ℚ) - (j : ℚ))

@[simp] theorem harmonic_zero : harmonic 0 = 0 := by simp [harmonic]
@[simp] theorem harmonicTwo_zero : harmonicTwo 0 = 0 := by simp [harmonicTwo]

theorem harmonic_succ (n : ℕ) :
    harmonic (n + 1) = harmonic n + 1 / ((n : ℚ) + 1) := by
  simp [harmonic, Finset.sum_range_succ]

theorem harmonicTwo_succ (n : ℕ) :
    harmonicTwo (n + 1) = harmonicTwo n + 1 / ((n : ℚ) + 1) ^ 2 := by
  simp [harmonicTwo, Finset.sum_range_succ]

@[simp] theorem mRationalPart_right_zero (i : ℕ) : mRationalPart i 0 = kminus i := by
  simp [mRationalPart]

@[simp] theorem mRationalPart_left_zero (j : ℕ) : mRationalPart 0 j = kplus j := by
  cases j with
  | zero => simp [mRationalPart]
  | succ j => simp [mRationalPart]

@[simp] theorem zRationalPart_diagonal (i : ℕ) : zRationalPart i i = -harmonicTwo i := by
  simp [zRationalPart]

/-- The finite rational array obeys the same diagonal recurrence as the M series. -/
theorem mRationalPart_diagonal (i j : ℕ) :
    mRationalPart i j - mRationalPart (i + 1) (j + 1) = moment i / ((j : ℚ) + 1) := by
  by_cases h : j ≤ i
  · have h' : j + 1 ≤ i + 1 := by omega
    have hd : i + 1 - (j + 1) = i - j := by omega
    have hi : i - j + j = i := by omega
    simp only [mRationalPart, if_pos h, if_pos h', hd, Finset.sum_range_succ, hi]
    ring
  · have h' : ¬ j + 1 ≤ i + 1 := by omega
    have hd : j + 1 - (i + 1) = j - i := by omega
    have hj : j - i + i + 1 = j + 1 := by omega
    simp only [mRationalPart, if_neg h, if_neg h', hd, Finset.sum_range_succ, hj]
    simp only [Nat.cast_add, Nat.cast_one]
    ring

/-- A finite diagonal recurrence can be iterated without any limit exchange. -/
theorem finite_diagonal_telescope
    (F : ℕ → ℕ → ℚ) (f : ℕ → ℚ)
    (hstep : ∀ i j, F i j - F (i + 1) (j + 1) = f i / ((j : ℚ) + 1))
    (i j N : ℕ) :
    F i j - F (i + N) (j + N) =
      ∑ k ∈ Finset.range N, f (i + k) / (((j + k : ℕ) : ℚ) + 1) := by
  induction N with
  | zero => simp
  | succ N ih =>
      rw [Finset.sum_range_succ]
      have hs := hstep (i + N) (j + N)
      have hi : i + (N + 1) = i + N + 1 := by omega
      have hj : j + (N + 1) = j + N + 1 := by omega
      rw [hi, hj]
      rw [← ih, ← hs]
      ring

theorem mRationalPart_finite_diagonal (i j N : ℕ) :
    mRationalPart i j - mRationalPart (i + N) (j + N) =
      ∑ k ∈ Finset.range N, moment (i + k) / (((j + k : ℕ) : ℚ) + 1) :=
  finite_diagonal_telescope mRationalPart moment mRationalPart_diagonal i j N

/-- The adjacent diagonal is entirely rational, with explicit index-zero convention. -/
theorem mRationalPart_adjacent_diagonal (i : ℕ) :
    mRationalPart (i + 1) i = momentExt ((i : ℤ) - 1) + moment i := by
  induction i with
  | zero => norm_num [mRationalPart, kminus, moment, momentExt]
  | succ i ih =>
      have hs := mRationalPart_diagonal (i + 1) i
      have ht := moment_telescope_positive (i + 1) (by omega)
      have hi : (((i + 1 : ℕ) : ℤ) - 2) = (i : ℤ) - 1 := by omega
      have hj : (((i + 1 : ℕ) : ℤ) - 1) = (i : ℤ) := by omega
      rw [hi] at ht
      rw [hj, momentExt_natCast]
      norm_num only [Nat.cast_add, Nat.cast_one] at ht
      linarith only [hs, ht, ih]

theorem zRationalPart_symm (i j : ℕ) : zRationalPart i j = zRationalPart j i := by
  by_cases h : i = j
  · subst j
    rfl
  · have h' : j ≠ i := Ne.symm h
    simp only [zRationalPart, if_neg h, if_neg h']
    rw [div_eq_div_iff]
    · ring
    · exact sub_ne_zero.mpr (by exact_mod_cast h)
    · exact sub_ne_zero.mpr (by exact_mod_cast h')

theorem zRationalPart_diagonal_step (i j : ℕ) :
    zRationalPart i j - zRationalPart (i + 1) (j + 1) =
      1 / (((i : ℚ) + 1) * ((j : ℚ) + 1)) := by
  by_cases h : i = j
  · subst j
    simp only [zRationalPart_diagonal, harmonicTwo_succ]
    ring
  · have h' : i + 1 ≠ j + 1 := by omega
    have hd : (i : ℚ) - (j : ℚ) ≠ 0 := sub_ne_zero.mpr (by exact_mod_cast h)
    have hi : (i : ℚ) + 1 ≠ 0 := by positivity
    have hj : (j : ℚ) + 1 ≠ 0 := by positivity
    simp only [zRationalPart, if_neg h, if_neg h', harmonic_succ, Nat.cast_add, Nat.cast_one]
    have hdiff : ((i : ℚ) + 1) - ((j : ℚ) + 1) = (i : ℚ) - (j : ℚ) := by ring
    rw [hdiff]
    field_simp
    ring

theorem zRationalPart_finite_diagonal (i j N : ℕ) :
    zRationalPart i j - zRationalPart (i + N) (j + N) =
      ∑ k ∈ Finset.range N,
        1 / (((i + k : ℕ) : ℚ) + 1) / (((j + k : ℕ) : ℚ) + 1) := by
  apply finite_diagonal_telescope zRationalPart (fun i => 1 / ((i : ℚ) + 1))
  intro i j
  rw [zRationalPart_diagonal_step]
  exact div_mul_eq_div_div 1 ((i : ℚ) + 1) ((j : ℚ) + 1)

end MixedMoments
