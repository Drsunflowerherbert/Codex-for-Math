import Egyptian.Finite
import Mathlib.Algebra.Ring.Parity

namespace Egyptian

/-- Expose a duplicate without making any assumptions about where it occurs. -/
theorem duplicate_extraction {l : List ℕ} (h : ¬l.Nodup) :
    ∃ a t, l.Perm (a :: a :: t) := by
  induction l with
  | nil => exact False.elim (h List.nodup_nil)
  | cons a l ih =>
    by_cases hm : a ∈ l
    · exact ⟨a, l.erase a, (List.perm_cons_erase hm).cons a⟩
    · have ht : ¬l.Nodup := fun hn => h (List.nodup_cons.mpr ⟨hm, hn⟩)
      obtain ⟨b, t, hp⟩ := ih ht
      refine ⟨b, a :: t, (hp.cons a).trans ?_⟩
      exact (List.Perm.swap b a (b :: t)).trans ((List.Perm.swap b a t).cons b)

theorem duplicate_ge_three {a : ℕ} {t : List ℕ} (ha : 0 < a)
    (hx : reciprocalSum (a :: a :: t) < 1) : 3 ≤ a := by
  by_contra h
  have hab : a = 1 ∨ a = 2 := by omega
  have ht := reciprocalSum_nonneg t
  rcases hab with rfl | rfl <;> norm_num at hx <;> linarith

/-- Every admissible duplicate has a positive replacement pair with the same value and
strictly larger denominator sum. The replacement may collide with other entries. -/
theorem replacement_exists (d : ℕ) (hd : 3 ≤ d) :
    ∃ a b : ℕ, 0 < a ∧ 0 < b ∧
      (a : ℝ)⁻¹ + (b : ℝ)⁻¹ = (d : ℝ)⁻¹ + (d : ℝ)⁻¹ ∧ d + d < a + b := by
  obtain ⟨k, he | ho⟩ := Nat.even_or_odd' d
  · subst d
    have hk : 2 ≤ k := by omega
    refine ⟨k + 1, k * (k + 1), by omega, by positivity,
      (even_replacement_identity k (by omega)).symm, ?_⟩
    simpa only [two_mul] using even_replacement_growth k hk
  · subst d
    have hk : 1 ≤ k := by omega
    refine ⟨k + 1, (2 * k + 1) * (k + 1), by omega, by positivity,
      (odd_replacement_identity k).symm, ?_⟩
    simpa only [two_mul] using odd_replacement_growth k hk

/-- One cleanup step preserves positivity, exact length and value and strictly increases
the denominator sum. Distinctness and an arbitrary marker are not step invariants. -/
theorem duplicate_cleanup {l : List ℕ} (hp : ∀ d ∈ l, 0 < d)
    (hx : reciprocalSum l < 1) (hn : ¬l.Nodup) :
    ∃ out : List ℕ, (∀ d ∈ out, 0 < d) ∧ out.length = l.length ∧
      reciprocalSum out = reciprocalSum l ∧ l.sum < out.sum := by
  obtain ⟨d, t, hperm⟩ := duplicate_extraction hn
  have hd : 0 < d := hp d (hperm.mem_iff.mpr (by simp))
  have hdt : reciprocalSum (d :: d :: t) < 1 := by
    rw [← reciprocalSum_perm hperm]
    exact hx
  obtain ⟨a, b, ha, hb, heq, hinc⟩ := replacement_exists d (duplicate_ge_three hd hdt)
  refine ⟨a :: b :: t, ?_, ?_, ?_, ?_⟩
  · intro c hc
    rcases List.mem_cons.mp hc with rfl | hc
    · exact ha
    rcases List.mem_cons.mp hc with rfl | hc
    · exact hb
    · exact hp c (hperm.mem_iff.mpr (by simp [hc]))
  · simpa using hperm.length_eq.symm
  · rw [reciprocalSum_perm hperm]
    simp only [reciprocalSum_cons]
    linarith
  · rw [hperm.sum_eq]
    simp only [List.sum_cons]
    omega

/-- Sort to select a canonical representative of an unordered expansion. -/
def canonical (l : List ℕ) : List ℕ := l.mergeSort (· ≤ ·)

theorem canonical_perm (l : List ℕ) : (canonical l).Perm l :=
  List.mergeSort_perm l _

theorem canonical_mem {l : List ℕ} (hp : ∀ d ∈ l, 0 < d) :
    canonical l ∈ sortedRepresentations l.length (reciprocalSum l) := by
  refine ⟨(canonical_perm l).length_eq, ?_, ?_, reciprocalSum_perm (canonical_perm l)⟩
  · exact fun d hd => hp d ((canonical_perm l).mem_iff.mp hd)
  · exact List.sorted_mergeSort' (· ≤ ·) l

/-- Sorting after a duplicate replacement preserves every finite-state invariant. -/
theorem sorted_duplicate_cleanup {n : ℕ} {x : ℝ} {current : List ℕ}
    (hc : current ∈ sortedRepresentations n x) (hx : x < 1) (hn : ¬current.Nodup) :
    ∃ next : List ℕ, next ∈ sortedRepresentations n x ∧ current.sum < next.sum := by
  have ho1 : reciprocalSum current < 1 := by rw [hc.2.2.2]; exact hx
  obtain ⟨next, hpos, hlen, hvalue, hinc⟩ := duplicate_cleanup hc.2.1 ho1 hn
  refine ⟨canonical next, ?_, ?_⟩
  · have hs := canonical_mem hpos
    rw [hlen, hc.1, hvalue, hc.2.2.2] at hs
    exact hs
  · rw [(canonical_perm next).sum_eq]
    exact hinc

/-- The primary exact-length theorem. No marker or sharp denominator bound is claimed. -/
theorem exact_length_distinct {input : List ℕ} (hp : ∀ d ∈ input, 0 < d)
    (hx0 : 0 < reciprocalSum input) (hx1 : reciprocalSum input < 1) :
    ∃ out : List ℕ, (∀ d ∈ out, 0 < d) ∧ out.Nodup ∧
      out.length = input.length ∧ reciprocalSum out = reciprocalSum input := by
  classical
  let s := sortedRepresentations input.length (reciprocalSum input)
  have hs : s.Finite := finite_sortedRepresentations _ _
  have hne : s.Nonempty := by
    by_cases hi : input = []
    · subst input
      simp at hx0
    · exact ⟨canonical input, canonical_mem hp⟩
  obtain ⟨out, hout, hmax⟩ := Set.exists_max_image s List.sum hs hne
  refine ⟨out, hout.2.1, ?_, hout.1, hout.2.2.2⟩
  by_contra hn
  obtain ⟨next, hnext, hinc⟩ := sorted_duplicate_cleanup hout hx1 hn
  have hb := hmax next hnext
  omega

end Egyptian
