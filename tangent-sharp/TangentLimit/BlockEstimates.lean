import TangentLimit.NearestPole
import TangentLimit.Trigonometry
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Weighted tangent block estimates

These algebraic and analytic estimates reduce a weighted finite tangent sum
to reciprocal pole distances. The Diophantine hypothesis is not used here.
-/

namespace TangentLimit

open Finset

/-- A positive block endpoint controls all real-power denominators in the block. -/
theorem sum_abs_tan_div_rpow_le_reciprocal
    (S : Finset ℕ) (N : ℕ) (hN : 0 < N) (s : ℝ) (hs : 0 ≤ s)
    (hindex : ∀ n ∈ S, N ≤ n)
    (hdist : ∀ n ∈ S, 0 < |poleOffset n|) :
    (∑ n ∈ S, |Real.tan (n : ℝ)| / (n : ℝ) ^ s) ≤
      (Real.pi / (2 * (N : ℝ) ^ s)) * (∑ n ∈ S, 1 / |poleOffset n|) := by
  have hNreal : 0 < (N : ℝ) := by exact_mod_cast hN
  rw [mul_sum]
  apply sum_le_sum
  intro n hn
  have hNn : (N : ℝ) ≤ (n : ℝ) := by exact_mod_cast hindex n hn
  have hnreal : 0 < (n : ℝ) := hNreal.trans_le hNn
  have hpow : (N : ℝ) ^ s ≤ (n : ℝ) ^ s :=
    Real.rpow_le_rpow hNreal.le hNn hs
  have ht : |Real.tan (n : ℝ)| ≤ Real.pi / (2 * |poleOffset n|) :=
    tan_le_of_pole_distance (abs_poleOffset_le n) (hdist n hn)
  calc
    |Real.tan (n : ℝ)| / (n : ℝ) ^ s ≤
        |Real.tan (n : ℝ)| / (N : ℝ) ^ s :=
      div_le_div_of_nonneg_left (abs_nonneg _) (Real.rpow_pos_of_pos hNreal s) hpow
    _ ≤ (Real.pi / (2 * |poleOffset n|)) / (N : ℝ) ^ s :=
      div_le_div_of_nonneg_right ht (Real.rpow_nonneg hNreal.le s)
    _ = (Real.pi / (2 * (N : ℝ) ^ s)) * (1 / |poleOffset n|) := by ring

/-- Convert a reciprocal-spacing estimate into a power of the block endpoint. -/
theorem weighted_block_coefficient (c α s N H : ℝ) (hc : 0 < c) (hN : 0 < N) :
    (Real.pi / (2 * N ^ s)) *
        ((2 / ((c / 2) * (3 * N) ^ (1 - α))) * H) =
      ((2 * Real.pi / c) * (3 : ℝ) ^ (α - 1)) * N ^ (α - 1 - s) * H := by
  have h3 : (0 : ℝ) < 3 := by norm_num
  have he : 1 - α = -(α - 1) := by ring
  rw [he, Real.rpow_neg (by positivity : (0 : ℝ) ≤ 3 * N),
    Real.mul_rpow h3.le hN.le, Real.rpow_sub hN (α - 1) s]
  field_simp

end TangentLimit
