import Egyptian.Basic
import Mathlib.Data.Real.Archimedean
import Mathlib.Data.Set.Finite.Lattice
import Mathlib.Data.Set.Finite.Lemmas

namespace Egyptian

/-- Canonical finite states: positive nondecreasing lists of fixed length and value. -/
def sortedRepresentations (n : ℕ) (x : ℝ) : Set (List ℕ) :=
  {l | l.length = n ∧ (∀ d ∈ l, 0 < d) ∧ l.Pairwise (· ≤ ·) ∧ reciprocalSum l = x}

theorem reciprocalSum_le_length_mul_inv {a : ℕ} (ha : 0 < a) (l : List ℕ)
    (hmin : ∀ d ∈ l, a ≤ d) :
    reciprocalSum l ≤ (l.length : ℝ) * (a : ℝ)⁻¹ := by
  induction l with
  | nil => simp
  | cons d l ih =>
    have had : a ≤ d := hmin d (by simp)
    have haR : 0 < (a : ℝ) := Nat.cast_pos.mpr ha
    have hadR : (a : ℝ) ≤ (d : ℝ) := Nat.cast_le.mpr had
    have hd : (d : ℝ)⁻¹ ≤ (a : ℝ)⁻¹ := by
      simpa only [one_div] using (one_div_le_one_div_of_le haR hadR)
    have ht := ih (fun b hb => hmin b (by simp [hb]))
    simp only [reciprocalSum_cons, List.length_cons, Nat.cast_add, Nat.cast_one]
    nlinarith

/-- Sorted representations are finite for every real value, including zero and negative values.
This is a finiteness assertion, not executable enumeration for arbitrary real inputs. -/
theorem finite_sortedRepresentations (n : ℕ) (x : ℝ) :
    (sortedRepresentations n x).Finite := by
  induction n generalizing x with
  | zero =>
    apply (Set.finite_singleton ([] : List ℕ)).subset
    intro l hl
    have : l.length = 0 := hl.1
    simpa using List.length_eq_zero_iff.mp this
  | succ n ih =>
    by_cases hx : 0 < x
    · obtain ⟨B, hB⟩ := exists_nat_gt (((n + 1 : ℕ) : ℝ) / x)
      have hBx : ((n + 1 : ℕ) : ℝ) < (B : ℝ) * x :=
        (div_lt_iff₀ hx).mp hB
      have hs : (⋃ a : Fin B,
          List.cons (a : ℕ) '' sortedRepresentations n (x - ((a : ℕ) : ℝ)⁻¹)).Finite :=
        Set.finite_iUnion fun a => (ih _).image (List.cons (a : ℕ))
      apply hs.subset
      intro l hl
      rcases hl with ⟨hlen, hp, hsorted, hsum⟩
      cases l with
      | nil => simp at hlen
      | cons a t =>
        have ha : 0 < a := hp a (by simp)
        have hst := List.pairwise_cons.mp hsorted
        have hmin : ∀ d ∈ a :: t, a ≤ d := by
          intro d hd
          rcases List.mem_cons.mp hd with rfl | hd
          · exact le_rfl
          · exact hst.1 d hd
        have hb := reciprocalSum_le_length_mul_inv ha (a :: t) hmin
        rw [hsum, hlen] at hb
        have hab : x * (a : ℝ) ≤ ((n + 1 : ℕ) : ℝ) := by
          have hm := mul_le_mul_of_nonneg_right hb (Nat.cast_nonneg a)
          have ha0 : (a : ℝ) ≠ 0 := ne_of_gt (Nat.cast_pos.mpr ha)
          simpa only [mul_assoc, inv_mul_cancel₀ ha0,
            mul_one] using hm
        have haB : a < B := by
          have : (a : ℝ) < B := by nlinarith
          exact_mod_cast this
        have ht : t ∈ sortedRepresentations n (x - (a : ℝ)⁻¹) := by
          refine ⟨by simpa using hlen, ?_, hst.2, ?_⟩
          · exact fun d hd => hp d (by simp [hd])
          · simp only [reciprocalSum_cons] at hsum
            linarith
        exact Set.mem_iUnion.mpr ⟨⟨a, haB⟩, Set.mem_image_of_mem _ ht⟩
    · apply Set.finite_empty.subset
      intro l hl
      have hne : l ≠ [] := by
        intro he
        have := hl.1
        simp [he] at this
      have hp := reciprocalSum_pos hl.2.1 hne
      rw [hl.2.2.2] at hp
      exact (hx hp).elim

end Egyptian
