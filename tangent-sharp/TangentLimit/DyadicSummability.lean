import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Topology.Algebra.InfiniteSum.Real
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

/-!
# Dyadic summability infrastructure

The dyadic blocks `[2^j, 2^(j+1))` cover the positive integers. This
module converts a summable majorant for their nonnegative block sums into
summability of the original series. It also supplies the elementary bound
`H_(2^j) ≤ j+1`, with the reciprocal terms indexed starting at one.
-/

namespace TangentLimit

open Finset

/-- A finite dyadic decomposition, with the zero term kept separately. -/
theorem sum_range_two_pow_eq (f : ℕ → ℝ) (j : ℕ) :
    ∑ n ∈ range (2 ^ j), f n =
      f 0 + ∑ k ∈ range j, ∑ n ∈ Ico (2 ^ k) (2 ^ (k + 1)), f n := by
  induction j with
  | zero => simp
  | succ j ih =>
      have hle : 2 ^ j ≤ 2 ^ (j + 1) := by
        rw [pow_succ]
        omega
      calc
        ∑ n ∈ range (2 ^ (j + 1)), f n =
            (∑ n ∈ range (2 ^ j), f n) +
              ∑ n ∈ Ico (2 ^ j) (2 ^ (j + 1)), f n :=
          (sum_range_add_sum_Ico f hle).symm
        _ = f 0 + ∑ k ∈ range (j + 1),
              ∑ n ∈ Ico (2 ^ k) (2 ^ (k + 1)), f n := by
          rw [ih, sum_range_succ]
          ring

/-- Every finite initial segment fits in a dyadic initial segment. -/
theorem nat_le_two_pow (n : ℕ) : n ≤ 2 ^ n := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [pow_succ]
      have hpos : 1 ≤ 2 ^ n := Nat.one_le_two_pow
      omega

/-- Nonnegative dyadic block sums bounded by a summable nonnegative sequence
imply summability. The zero term contributes only a finite amount. -/
theorem summable_of_dyadic_block_bound {f g : ℕ → ℝ}
    (hf : ∀ n, 0 ≤ f n) (hg0 : ∀ j, 0 ≤ g j) (hg : Summable g)
    (hblock : ∀ j : ℕ, ∑ n ∈ Ico (2 ^ j) (2 ^ (j + 1)), f n ≤ g j) :
    Summable f := by
  apply summable_of_sum_range_le hf (c := f 0 + ∑' j, g j)
  intro n
  calc
    ∑ k ∈ range n, f k ≤ ∑ k ∈ range (2 ^ n), f k := by
      apply sum_le_sum_of_subset_of_nonneg (range_mono (nat_le_two_pow n))
      intro k _ _
      exact hf k
    _ = f 0 + ∑ j ∈ range n, ∑ k ∈ Ico (2 ^ j) (2 ^ (j + 1)), f k :=
      sum_range_two_pow_eq f n
    _ ≤ f 0 + ∑ j ∈ range n, g j := by
      gcongr with j hj
      exact hblock j
    _ ≤ f 0 + ∑' j, g j := by
      exact add_le_add_left (Summable.sum_le_tsum (range n) (fun j _ => hg0 j) hg) _

/-- A linear factor times a geometric sequence is summable. -/
theorem summable_nat_add_one_mul_geometric {ρ : ℝ} (hρ0 : 0 ≤ ρ) (hρ1 : ρ < 1) :
    Summable (fun j : ℕ => ((j : ℝ) + 1) * ρ ^ j) := by
  have hnorm : ‖ρ‖ < 1 := by simpa [Real.norm_eq_abs, abs_of_nonneg hρ0] using hρ1
  have hlin : Summable (fun j : ℕ => (j : ℝ) * ρ ^ j) := by
    simpa only [pow_one] using summable_pow_mul_geometric_of_norm_lt_one 1 hnorm
  have hgeom : Summable (fun j : ℕ => ρ ^ j) := summable_geometric_of_norm_lt_one hnorm
  simpa only [add_mul, one_mul] using hlin.add hgeom

/-- A geometric block estimate with a linear prefactor implies summability. -/
theorem summable_of_dyadic_geometric_bound {f : ℕ → ℝ} {C ρ : ℝ}
    (hf : ∀ n, 0 ≤ f n) (hC : 0 ≤ C) (hρ0 : 0 ≤ ρ) (hρ1 : ρ < 1)
    (hblock : ∀ j : ℕ, ∑ n ∈ Ico (2 ^ j) (2 ^ (j + 1)), f n ≤
      C * ((j : ℝ) + 1) * ρ ^ j) : Summable f := by
  apply summable_of_dyadic_block_bound hf (g := fun j => C * ((j : ℝ) + 1) * ρ ^ j)
  · intro j
    positivity
  · simpa only [mul_assoc] using
      (summable_nat_add_one_mul_geometric hρ0 hρ1).mul_left C
  · exact hblock

/-- The reciprocals in a doubling block add up to at most one. -/
theorem sum_reciprocal_doubling_block_le_one {N : ℕ} (hN : 0 < N) :
    ∑ k ∈ range N, (1 : ℝ) / ((N + k + 1 : ℕ) : ℝ) ≤ 1 := by
  have hNpos : 0 < (N : ℝ) := by exact_mod_cast hN
  calc
    ∑ k ∈ range N, (1 : ℝ) / ((N + k + 1 : ℕ) : ℝ) ≤
        ∑ _k ∈ range N, (1 : ℝ) / (N : ℝ) := by
      apply sum_le_sum
      intro k _
      apply one_div_le_one_div_of_le hNpos
      exact_mod_cast (show N ≤ N + k + 1 by omega)
    _ = 1 := by
      simp [div_eq_mul_inv, ne_of_gt hNpos]

/-- The dyadic harmonic number is at most the dyadic exponent plus one. -/
theorem harmonic_sum_two_pow_le (j : ℕ) :
    ∑ k ∈ range (2 ^ j), (1 : ℝ) / ((k + 1 : ℕ) : ℝ) ≤ (j : ℝ) + 1 := by
  induction j with
  | zero => simp
  | succ j ih =>
      have hdouble : 2 ^ (j + 1) = 2 ^ j + 2 ^ j := by rw [pow_succ]; omega
      rw [hdouble, sum_range_add]
      have hblock := sum_reciprocal_doubling_block_le_one
        (N := 2 ^ j) (pow_pos (by norm_num : 0 < (2 : ℕ)) j)
      push_cast
      push_cast at hblock ih
      linarith

/-- The zero term may be arbitrary: positivity is needed only on the positive
integers appearing in the blocks. -/
theorem summable_of_dyadic_block_bound_pos {f g : ℕ → ℝ}
    (hf : ∀ n, 0 < n → 0 ≤ f n) (hg0 : ∀ j, 0 ≤ g j) (hg : Summable g)
    (hblock : ∀ j : ℕ, ∑ n ∈ Ico (2 ^ j) (2 ^ (j + 1)), f n ≤ g j) :
    Summable f := by
  let f' : ℕ → ℝ := fun n => if n = 0 then 0 else f n
  have hf' : ∀ n, 0 ≤ f' n := by
    intro n
    by_cases hn : n = 0
    · simp [f', hn]
    · simpa [f', hn] using hf n (Nat.pos_of_ne_zero hn)
  have hblock' : ∀ j : ℕ,
      ∑ n ∈ Ico (2 ^ j) (2 ^ (j + 1)), f' n ≤ g j := by
    intro j
    convert hblock j using 1
    apply sum_congr rfl
    intro n hn
    have hnpos : 0 < n := lt_of_lt_of_le
      (pow_pos (by norm_num : 0 < (2 : ℕ)) j) (mem_Ico.mp hn).1
    simp [f', ne_of_gt hnpos]
  have hs : Summable f' := summable_of_dyadic_block_bound hf' hg0 hg hblock'
  apply (summable_nat_add_iff 1).1
  apply ((summable_nat_add_iff 1).2 hs).congr
  intro n
  simp [f']

/-- Real powers of a dyadic base are a geometric sequence. -/
theorem dyadic_rpow_eq_geometric (β : ℝ) (j : ℕ) :
    ((2 ^ j : ℕ) : ℝ) ^ β = ((2 : ℝ) ^ β) ^ j := by
  rw [Nat.cast_pow, Nat.cast_ofNat,
    ← Real.rpow_natCast_mul (by norm_num : 0 ≤ (2 : ℝ)),
    mul_comm, Real.rpow_mul_natCast (by norm_num : 0 ≤ (2 : ℝ))]

/-- A negative real-power dyadic bound with a linear factor is summable. -/
theorem summable_of_dyadic_rpow_bound {f : ℕ → ℝ} {C β : ℝ}
    (hf : ∀ n, 0 ≤ f n) (hC : 0 ≤ C) (hβ : β < 0)
    (hblock : ∀ j : ℕ, ∑ n ∈ Ico (2 ^ j) (2 ^ (j + 1)), f n ≤
      C * ((2 ^ j : ℕ) : ℝ) ^ β * ((j : ℝ) + 1)) : Summable f := by
  apply summable_of_dyadic_geometric_bound hf hC
    (Real.rpow_nonneg (by norm_num : 0 ≤ (2 : ℝ)) β)
    (Real.rpow_lt_one_of_one_lt_of_neg (by norm_num : 1 < (2 : ℝ)) hβ)
  intro j
  calc
    ∑ n ∈ Ico (2 ^ j) (2 ^ (j + 1)), f n ≤
        C * ((2 ^ j : ℕ) : ℝ) ^ β * ((j : ℝ) + 1) := hblock j
    _ = C * ((j : ℝ) + 1) * ((2 : ℝ) ^ β) ^ j := by
      rw [dyadic_rpow_eq_geometric]
      ring

/-- The harmonic packing bound with a negative real power implies summability.
This is the direct bridge from a dyadic reciprocal-distance estimate. -/
theorem summable_of_dyadic_rpow_harmonic_bound {f : ℕ → ℝ} {C β : ℝ}
    (hf : ∀ n, 0 ≤ f n) (hC : 0 ≤ C) (hβ : β < 0)
    (hblock : ∀ j : ℕ, ∑ n ∈ Ico (2 ^ j) (2 ^ (j + 1)), f n ≤
      C * ((2 ^ j : ℕ) : ℝ) ^ β *
        ∑ k ∈ range (2 ^ j), (1 : ℝ) / ((k + 1 : ℕ) : ℝ)) : Summable f := by
  apply summable_of_dyadic_rpow_bound hf hC hβ
  intro j
  exact (hblock j).trans (mul_le_mul_of_nonneg_left (harmonic_sum_two_pow_le j)
    (mul_nonneg hC (Real.rpow_nonneg (Nat.cast_nonneg _) β)))

end TangentLimit
