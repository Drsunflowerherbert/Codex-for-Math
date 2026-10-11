import TangentLimit.Diophantine
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

/-!
# Uniform separation of signed tangent-pole offsets

All approximation estimates in this file are explicit hypotheses.  A finite
block of integer arguments below `2 * N` has uniformly positive pole distances
and uniformly separated signed offsets.  The proof handles equal pole indices
separately; different pole indices use a positive natural denominator after
orienting their difference.
-/

noncomputable section

namespace TangentLimit

/-- The distance scale for a block of arguments below `2 * N`. -/
def blockDelta (c α : ℝ) (N : ℕ) : ℝ :=
  (c / 2) * (3 * (N : ℝ)) ^ (1 - α)

theorem blockDelta_pos {c α : ℝ} {N : ℕ} (hc : 0 < c) (hN : 1 ≤ N) :
    0 < blockDelta c α N := by
  unfold blockDelta
  have hN' : (0 : ℝ) < (N : ℝ) := by exact_mod_cast (by omega : 0 < N)
  exact mul_pos (by linarith) (Real.rpow_pos_of_pos (by positivity) _)

theorem blockDelta_le_half {c α : ℝ} {N : ℕ}
    (hc : 0 < c) (hc1 : c ≤ 1) (hα : 2 < α) (hN : 1 ≤ N) :
    blockDelta c α N ≤ 1 / 2 := by
  have hN' : (1 : ℝ) ≤ (N : ℝ) := by exact_mod_cast hN
  have hp : (3 * (N : ℝ)) ^ (1 - α) ≤ 1 :=
    Real.rpow_le_one_of_one_le_of_nonpos (by linarith) (by linarith)
  calc
    blockDelta c α N ≤ (c / 2) * 1 :=
      mul_le_mul_of_nonneg_left hp (by positivity)
    _ ≤ 1 / 2 := by linarith

/-- The chosen pole index for an argument below `2 * N` is below `N`. -/
theorem poleIndex_lt_of_lt_two_mul {N n : ℕ} (hn : n < 2 * N) :
    poleIndex n < N := by
  have hfloor := poleIndex_mul_pi_le n
  have hk : (0 : ℝ) ≤ (poleIndex n : ℝ) := by positivity
  have hmul : 2 * (poleIndex n : ℝ) ≤ (poleIndex n : ℝ) * Real.pi := by
    nlinarith [mul_nonneg hk (show 0 ≤ Real.pi - 2 by linarith [Real.pi_gt_three])]
  have hn' : (n : ℝ) < 2 * (N : ℝ) := by exact_mod_cast hn
  have hkN : (poleIndex n : ℝ) < (N : ℝ) := by linarith
  exact_mod_cast hkN

theorem poleDenom_le_three_mul {N n : ℕ} (hn : n < 2 * N) :
    poleDenom n ≤ 3 * N := by
  have hk := poleIndex_lt_of_lt_two_mul hn
  unfold poleDenom
  omega

/-- A uniform integer approximation estimate bounds every pole distance in a
block, including arguments near the first pole. -/
theorem blockDelta_le_abs_poleOffset {c α : ℝ} {N n : ℕ}
    (hc0 : 0 < c) (hα : 2 < α) (_hN : 1 ≤ N) (hn : n < 2 * N)
    (hc : ∀ q : ℕ, 0 < q → ∀ p : ℤ,
      c * (q : ℝ) ^ (1 - α) ≤ |(q : ℝ) * Real.pi - (p : ℝ)|) :
    blockDelta c α N ≤ |poleOffset n| := by
  have hq := poleDenom_pos n
  have hq' : (0 : ℝ) < (poleDenom n : ℝ) := by exact_mod_cast hq
  have hqN : (poleDenom n : ℝ) ≤ 3 * (N : ℝ) := by
    exact_mod_cast poleDenom_le_three_mul hn
  have hp := Real.rpow_le_rpow_of_nonpos hq' hqN (show 1 - α ≤ 0 by linarith)
  have ha := hc (poleDenom n) hq (2 * (n : ℤ))
  have hid : |(poleDenom n : ℝ) * Real.pi - ((2 * (n : ℤ) : ℤ) : ℝ)| =
      2 * |poleOffset n| := by
    have heq : (poleDenom n : ℝ) * Real.pi - ((2 * (n : ℤ) : ℤ) : ℝ) =
        -2 * poleOffset n := by
      simp only [Int.cast_mul, Int.cast_ofNat, Int.cast_natCast, poleOffset]
      ring
    rw [heq, abs_mul]
    norm_num
  rw [hid] at ha
  have hm := mul_le_mul_of_nonneg_left hp (show 0 ≤ c / 2 by positivity)
  change (c / 2) * (3 * (N : ℝ)) ^ (1 - α) ≤ |poleOffset n|
  nlinarith

private theorem one_le_abs_natCast_sub {n m : ℕ} (hnm : n ≠ m) :
    (1 : ℝ) ≤ |(n : ℝ) - (m : ℝ)| := by
  rcases lt_or_gt_of_ne hnm with hlt | hgt
  · have h : (n : ℝ) + 1 ≤ (m : ℝ) := by
      exact_mod_cast (by omega : n + 1 ≤ m)
    rw [abs_of_nonpos (by linarith)]
    linarith
  · have h : (m : ℝ) + 1 ≤ (n : ℝ) := by
      exact_mod_cast (by omega : m + 1 ≤ n)
    rw [abs_of_nonneg (by linarith)]
    linarith

private theorem blockDelta_le_abs_poleOffset_sub_of_index_lt
    {c α : ℝ} {N n m : ℕ}
    (hc0 : 0 < c) (hα : 2 < α) (hN : 1 ≤ N)
    (hkn : poleIndex n < N) (hkmn : poleIndex m < poleIndex n)
    (hc : ∀ q : ℕ, 0 < q → ∀ p : ℤ,
      c * (q : ℝ) ^ (1 - α) ≤ |(q : ℝ) * Real.pi - (p : ℝ)|) :
    blockDelta c α N ≤ |poleOffset n - poleOffset m| := by
  let q : ℕ := poleIndex n - poleIndex m
  have hq : 0 < q := by dsimp [q]; omega
  have hqN : q ≤ 3 * N := by dsimp [q]; omega
  have hq' : (0 : ℝ) < (q : ℝ) := by exact_mod_cast hq
  have hqN' : (q : ℝ) ≤ 3 * (N : ℝ) := by exact_mod_cast hqN
  have hp := Real.rpow_le_rpow_of_nonpos hq' hqN' (show 1 - α ≤ 0 by linarith)
  have ha := hc q hq ((n : ℤ) - (m : ℤ))
  have hid : (q : ℝ) * Real.pi - (((n : ℤ) - (m : ℤ) : ℤ) : ℝ) =
      -(poleOffset n - poleOffset m) := by
    dsimp [q]
    simp only [Nat.cast_sub hkmn.le, Int.cast_sub, Int.cast_natCast,
      poleOffset, poleDenom, Nat.cast_add, Nat.cast_mul, Nat.cast_ofNat]
    ring
  rw [hid, abs_neg] at ha
  have hm := mul_le_mul_of_nonneg_left hp hc0.le
  have hpow : 0 ≤ (3 * (N : ℝ)) ^ (1 - α) := Real.rpow_nonneg (by positivity) _
  change (c / 2) * (3 * (N : ℝ)) ^ (1 - α) ≤ |poleOffset n - poleOffset m|
  nlinarith

/-- Distinct signed pole offsets in a block are separated by `blockDelta`.
Equal pole indices are handled by integer spacing; both orientations of a
nonzero index difference are reduced to a positive natural denominator. -/
theorem blockDelta_le_abs_poleOffset_sub {c α : ℝ} {N n m : ℕ}
    (hc0 : 0 < c) (hc1 : c ≤ 1) (hα : 2 < α) (hN : 1 ≤ N)
    (hn : n < 2 * N) (hm : m < 2 * N) (hnm : n ≠ m)
    (hc : ∀ q : ℕ, 0 < q → ∀ p : ℤ,
      c * (q : ℝ) ^ (1 - α) ≤ |(q : ℝ) * Real.pi - (p : ℝ)|) :
    blockDelta c α N ≤ |poleOffset n - poleOffset m| := by
  have hkn := poleIndex_lt_of_lt_two_mul hn
  have hkm := poleIndex_lt_of_lt_two_mul hm
  rcases lt_trichotomy (poleIndex n) (poleIndex m) with hlt | heq | hgt
  · rw [abs_sub_comm]
    exact blockDelta_le_abs_poleOffset_sub_of_index_lt hc0 hα hN hkm hlt hc
  · have hoff : poleOffset n - poleOffset m = (n : ℝ) - (m : ℝ) := by
      simp [poleOffset, poleDenom, heq]
    rw [hoff]
    exact (blockDelta_le_half hc0 hc1 hα hN).trans
      (by linarith [one_le_abs_natCast_sub hnm])
  · exact blockDelta_le_abs_poleOffset_sub_of_index_lt hc0 hα hN hkn hgt hc

end TangentLimit
