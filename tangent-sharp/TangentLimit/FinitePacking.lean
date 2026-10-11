import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Finset.Sort
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Reciprocal packing on the real line

Points separated from zero and from one another by `δ` have a harmonic, rather
than linear, bound for their total reciprocal distance to zero.  No tangent or
Diophantine assumptions enter this finite combinatorial estimate.
-/

namespace TangentLimit

open scoped BigOperators

/-- The `k`th positive point in an ordered separated finite set is at least
`(k + 1) * δ` away from zero. -/
theorem ordered_separated_lower_bound (S : Finset ℝ) (δ : ℝ)
    (haway : ∀ x ∈ S, δ ≤ x)
    (hsep : ∀ x ∈ S, ∀ y ∈ S, x ≠ y → δ ≤ |x - y|)
    (k : Fin S.card) :
    ((k.val + 1 : ℕ) : ℝ) * δ ≤ S.orderEmbOfFin rfl k := by
  have h : ∀ n (hn : n < S.card),
      ((n + 1 : ℕ) : ℝ) * δ ≤ S.orderEmbOfFin rfl ⟨n, hn⟩ := by
    intro n
    induction n with
    | zero =>
      intro hn
      simpa using haway _ (S.orderEmbOfFin_mem rfl ⟨0, hn⟩)
    | succ n ih =>
      intro hn
      have hn' : n < S.card := by omega
      have hab : S.orderEmbOfFin rfl ⟨n, hn'⟩ <
          S.orderEmbOfFin rfl ⟨n + 1, hn⟩ :=
        (S.orderEmbOfFin rfl).strictMono (by simp)
      have hgap := hsep _ (S.orderEmbOfFin_mem rfl ⟨n + 1, hn⟩)
        _ (S.orderEmbOfFin_mem rfl ⟨n, hn'⟩) (ne_of_gt hab)
      rw [abs_of_pos (sub_pos.mpr hab)] at hgap
      have hprev := ih hn'
      push_cast at *
      linarith
  exact h k.val k.isLt

/-- One side of zero contributes at most `H_card / δ`. -/
theorem sum_reciprocal_le_harmonic_of_positive (S : Finset ℝ) (δ : ℝ)
    (hδ : 0 < δ) (haway : ∀ x ∈ S, δ ≤ x)
    (hsep : ∀ x ∈ S, ∀ y ∈ S, x ≠ y → δ ≤ |x - y|) :
    (∑ x ∈ S, 1 / x) ≤
      (1 / δ) * ∑ k ∈ Finset.range S.card, 1 / ((k + 1 : ℕ) : ℝ) := by
  classical
  calc
    (∑ x ∈ S, 1 / x) =
        ∑ k : Fin S.card, 1 / S.orderEmbOfFin rfl k := by
      have hmap := Finset.sum_map Finset.univ (S.orderEmbOfFin rfl).toEmbedding
        (fun x : ℝ => 1 / x)
      rw [S.map_orderEmbOfFin_univ rfl] at hmap
      exact hmap
    _ ≤ ∑ k : Fin S.card, (1 / δ) * (1 / ((k.val + 1 : ℕ) : ℝ)) := by
      apply Finset.sum_le_sum
      intro k _
      have hpos : 0 < ((k.val + 1 : ℕ) : ℝ) * δ :=
        mul_pos (by positivity) hδ
      calc
        _ ≤ 1 / (((k.val + 1 : ℕ) : ℝ) * δ) :=
          one_div_le_one_div_of_le hpos (ordered_separated_lower_bound S δ haway hsep k)
        _ = _ := by simp [div_eq_mul_inv, mul_comm, mul_left_comm]
    _ = (1 / δ) * ∑ k ∈ Finset.range S.card, 1 / ((k + 1 : ℕ) : ℝ) := by
      rw [← Finset.mul_sum]
      congr 1
      exact Fin.sum_univ_eq_sum_range (fun k : ℕ => 1 / ((k + 1 : ℕ) : ℝ)) S.card

/-- The same one-sided estimate with arbitrary labels for the points. -/
theorem sum_reciprocal_le_harmonic_of_positive_on {ι : Type*} [DecidableEq ι]
    (S : Finset ι) (f : ι → ℝ) (δ : ℝ)
    (hδ : 0 < δ) (haway : ∀ i ∈ S, δ ≤ f i)
    (hsep : ∀ i ∈ S, ∀ j ∈ S, i ≠ j → δ ≤ |f i - f j|) :
    (∑ i ∈ S, 1 / f i) ≤
      (1 / δ) * ∑ k ∈ Finset.range S.card, 1 / ((k + 1 : ℕ) : ℝ) := by
  classical
  have hinj : Set.InjOn f S := by
    intro i hi j hj hij
    by_contra hne
    have h := hsep i hi j hj hne
    rw [hij, sub_self, abs_zero] at h
    linarith
  have haway' : ∀ x ∈ S.image f, δ ≤ x := by
    intro x hx
    obtain ⟨i, hi, rfl⟩ := Finset.mem_image.mp hx
    exact haway i hi
  have hsep' : ∀ x ∈ S.image f, ∀ y ∈ S.image f, x ≠ y → δ ≤ |x - y| := by
    intro x hx y hy hxy
    obtain ⟨i, hi, rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨j, hj, rfl⟩ := Finset.mem_image.mp hy
    apply hsep i hi j hj
    intro hij
    exact hxy (congrArg f hij)
  have h := sum_reciprocal_le_harmonic_of_positive (S.image f) δ hδ haway' hsep'
  rw [Finset.sum_image hinj, Finset.card_image_of_injOn hinj] at h
  exact h

/-- Harmonic partial sums increase with their natural-number cutoff. -/
theorem harmonic_sum_mono {m n : ℕ} (hmn : m ≤ n) :
    (∑ k ∈ Finset.range m, (1 : ℝ) / ((k + 1 : ℕ) : ℝ)) ≤
      ∑ k ∈ Finset.range n, (1 : ℝ) / ((k + 1 : ℕ) : ℝ) := by
  apply Finset.sum_le_sum_of_subset_of_nonneg (Finset.range_mono hmn)
  intro k _ _
  positivity

/-- A finite set of signed points, separated from zero and one another by
`δ`, has total reciprocal distance at most `2 * H_card / δ`. -/
theorem sum_reciprocal_abs_le_harmonic {ι : Type*} [DecidableEq ι]
    (S : Finset ι) (f : ι → ℝ) (δ : ℝ) (hδ : 0 < δ)
    (haway : ∀ i ∈ S, δ ≤ |f i|)
    (hsep : ∀ i ∈ S, ∀ j ∈ S, i ≠ j → δ ≤ |f i - f j|) :
    (∑ i ∈ S, 1 / |f i|) ≤
      (2 / δ) * ∑ k ∈ Finset.range S.card, 1 / ((k + 1 : ℕ) : ℝ) := by
  classical
  let P := S.filter (fun i => 0 ≤ f i)
  let Q := S.filter (fun i => ¬ 0 ≤ f i)
  have hP : (∑ i ∈ P, 1 / |f i|) ≤
      (1 / δ) * ∑ k ∈ Finset.range S.card, 1 / ((k + 1 : ℕ) : ℝ) := by
    have hp := sum_reciprocal_le_harmonic_of_positive_on P f δ hδ
      (by
        intro i hi
        obtain ⟨hiS, hip⟩ := Finset.mem_filter.mp hi
        simpa [abs_of_nonneg hip] using haway i hiS)
      (by
        intro i hi j hj hij
        exact hsep i (Finset.mem_filter.mp hi).1 j (Finset.mem_filter.mp hj).1 hij)
    calc
      _ = ∑ i ∈ P, 1 / f i := by
        apply Finset.sum_congr rfl
        intro i hi
        rw [abs_of_nonneg (Finset.mem_filter.mp hi).2]
      _ ≤ (1 / δ) * ∑ k ∈ Finset.range P.card, 1 / ((k + 1 : ℕ) : ℝ) := hp
      _ ≤ _ := mul_le_mul_of_nonneg_left
        (harmonic_sum_mono (Finset.card_filter_le S _)) (by positivity)
  have hQ : (∑ i ∈ Q, 1 / |f i|) ≤
      (1 / δ) * ∑ k ∈ Finset.range S.card, 1 / ((k + 1 : ℕ) : ℝ) := by
    have hq := sum_reciprocal_le_harmonic_of_positive_on Q (fun i => -f i) δ hδ
      (by
        intro i hi
        obtain ⟨hiS, hiq⟩ := Finset.mem_filter.mp hi
        simpa [abs_of_neg (lt_of_not_ge hiq)] using haway i hiS)
      (by
        intro i hi j hj hij
        have h := hsep i (Finset.mem_filter.mp hi).1 j (Finset.mem_filter.mp hj).1 hij
        simpa only [neg_sub_neg, abs_sub_comm] using h)
    calc
      _ = ∑ i ∈ Q, 1 / (-f i) := by
        apply Finset.sum_congr rfl
        intro i hi
        rw [abs_of_neg (lt_of_not_ge (Finset.mem_filter.mp hi).2)]
      _ ≤ (1 / δ) * ∑ k ∈ Finset.range Q.card, 1 / ((k + 1 : ℕ) : ℝ) := hq
      _ ≤ _ := mul_le_mul_of_nonneg_left
        (harmonic_sum_mono (Finset.card_filter_le S _)) (by positivity)
  have hsplit : (∑ i ∈ P, 1 / |f i|) + (∑ i ∈ Q, 1 / |f i|) =
      ∑ i ∈ S, 1 / |f i| :=
    Finset.sum_filter_add_sum_filter_not S (fun i => 0 ≤ f i) (fun i => 1 / |f i|)
  rw [← hsplit]
  calc
    _ ≤ _ := add_le_add hP hQ
    _ = _ := by ring

end TangentLimit
