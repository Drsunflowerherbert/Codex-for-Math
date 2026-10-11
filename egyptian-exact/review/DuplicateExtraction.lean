import Std

namespace EgyptianReview

/-- A repeated entry can be exposed as two leading copies by a permutation. -/
theorem duplicate_extraction {l : List Nat} (h : ¬l.Nodup) :
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

#print axioms duplicate_extraction

end EgyptianReview
