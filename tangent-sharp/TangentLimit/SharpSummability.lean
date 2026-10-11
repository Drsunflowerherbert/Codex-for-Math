import TangentLimit.UniformDiophantine
import TangentLimit.PoleSpacing
import TangentLimit.FinitePacking
import TangentLimit.BlockEstimates
import TangentLimit.DyadicSummability
import TangentLimit.Divergence

/-!
# The sharp absolute summability threshold

The sufficient direction retains `PiDiophantine` as an explicit theorem
argument. The necessary direction uses the separate unconditional divergence
theorem. No assertion about conditional convergence of the signed series is
made here.
-/

namespace TangentLimit

open Finset

/-- Uniform approximation and signed spacing give a harmonic bound for every
weighted block. The single constant is independent of `N` and `s`. -/
theorem abs_tan_rpow_block_bound (h : PiDiophantine) (α : ℝ) (hα : 2 < α) :
    ∃ C : ℝ, 0 < C ∧ ∀ s : ℝ, 0 ≤ s → ∀ N : ℕ, 1 ≤ N →
      (∑ n ∈ Ico N (2 * N), |Real.tan (n : ℝ)| / (n : ℝ) ^ s) ≤
        C * (N : ℝ) ^ (α - 1 - s) *
          (∑ k ∈ range N, 1 / ((k + 1 : ℕ) : ℝ)) := by
  obtain ⟨c, hc0, hc1, hc⟩ := piDiophantine_uniform h α hα
  refine ⟨(2 * Real.pi / c) * (3 : ℝ) ^ (α - 1), by positivity, ?_⟩
  intro s hs N hN
  have hNreal : 0 < (N : ℝ) := by exact_mod_cast (by omega : 0 < N)
  have hδ := blockDelta_pos (α := α) hc0 hN
  have haway : ∀ n ∈ Ico N (2 * N), blockDelta c α N ≤ |poleOffset n| := by
    intro n hn
    exact blockDelta_le_abs_poleOffset hc0 hα hN (mem_Ico.mp hn).2 hc
  have hsep : ∀ n ∈ Ico N (2 * N), ∀ m ∈ Ico N (2 * N), n ≠ m →
      blockDelta c α N ≤ |poleOffset n - poleOffset m| := by
    intro n hn m hm hnm
    exact blockDelta_le_abs_poleOffset_sub hc0 hc1 hα hN
      (mem_Ico.mp hn).2 (mem_Ico.mp hm).2 hnm hc
  have hpack := sum_reciprocal_abs_le_harmonic (Ico N (2 * N)) poleOffset
    (blockDelta c α N) hδ haway hsep
  have hcard : (Ico N (2 * N)).card = N := by simp; omega
  rw [hcard] at hpack
  calc
    _ ≤ (Real.pi / (2 * (N : ℝ) ^ s)) *
          (∑ n ∈ Ico N (2 * N), 1 / |poleOffset n|) :=
      sum_abs_tan_div_rpow_le_reciprocal _ _ (by omega) s hs
        (fun n hn => (mem_Ico.mp hn).1) (fun n hn => hδ.trans_le (haway n hn))
    _ ≤ (Real.pi / (2 * (N : ℝ) ^ s)) *
          ((2 / blockDelta c α N) * ∑ k ∈ range N, 1 / ((k + 1 : ℕ) : ℝ)) :=
      mul_le_mul_of_nonneg_left hpack (by positivity)
    _ = _ := weighted_block_coefficient c α s (N : ℝ) _ hc0 hNreal

/-- Under the explicit Diophantine hypothesis, absolute summability holds for
every real exponent strictly greater than one. -/
theorem summable_abs_tan_div_rpow (h : PiDiophantine) (s : ℝ) (hs : 1 < s) :
    Summable (fun n : ℕ => |Real.tan (n : ℝ)| / (n : ℝ) ^ s) := by
  let α : ℝ := (s + 3) / 2
  have hα : 2 < α := by dsimp [α]; linarith
  have hβ : α - 1 - s < 0 := by dsimp [α]; linarith
  obtain ⟨C, hC, hblock⟩ := abs_tan_rpow_block_bound h α hα
  apply summable_of_dyadic_rpow_harmonic_bound (C := C) (β := α - 1 - s)
    (fun n => div_nonneg (abs_nonneg _) (Real.rpow_nonneg (Nat.cast_nonneg _) _))
    hC.le hβ
  intro j
  have hN : 1 ≤ 2 ^ j := Nat.one_le_two_pow
  have hj := hblock s (by linarith) (2 ^ j) hN
  have hend : 2 ^ (j + 1) = 2 * 2 ^ j := by rw [pow_succ]; omega
  simpa only [hend] using hj

/-- The sufficient direction enumerated by the positive integers. -/
theorem summable_abs_tan_div_rpow_positive (h : PiDiophantine) (s : ℝ) (hs : 1 < s) :
    Summable (fun n : ℕ => |Real.tan ((n + 1 : ℕ) : ℝ)| /
      ((n + 1 : ℕ) : ℝ) ^ s) :=
  (summable_nat_add_iff 1).2 (summable_abs_tan_div_rpow h s hs)

/-- The sharp threshold for absolute summability over the positive integers.
Only sufficiency uses `PiDiophantine`; necessity is unconditional. -/
theorem summable_abs_tan_div_rpow_positive_iff (h : PiDiophantine) (s : ℝ) :
    Summable (fun n : ℕ => |Real.tan ((n + 1 : ℕ) : ℝ)| /
      ((n + 1 : ℕ) : ℝ) ^ s) ↔ 1 < s := by
  constructor
  · intro hsumm
    by_contra hs
    exact not_summable_abs_tan_div_rpow_positive s (le_of_not_gt hs) hsumm
  · exact summable_abs_tan_div_rpow_positive h s

end TangentLimit
