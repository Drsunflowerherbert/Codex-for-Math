import Egyptian.Cleanup

namespace Egyptian

/-- An upper bound converts forward strict natural-weight growth into a descending rank. -/
theorem bounded_increasing_weight_wellFounded {α : Type*} (weight : α → ℕ)
    (bound : ℕ) (hbound : ∀ a, weight a ≤ bound) :
    WellFounded (fun next current : α => weight current < weight next) := by
  apply Subrelation.wf (r := (measure (fun a => bound - weight a)).rel)
    (h₂ := (measure (fun a => bound - weight a)).wf)
  intro next current hstep
  change bound - weight next < bound - weight current
  have hn := hbound next
  have hc := hbound current
  omega

/-- Strict weight growth terminates on a finite state set. The orientation is
R(next,current), and the proof uses a descending natural rank. -/
theorem finite_increasing_weight_wellFounded {α : Type*} (s : Set α) (hs : s.Finite)
    (weight : α → ℕ) :
    WellFounded (fun next current : s => weight current.val < weight next.val) := by
  obtain ⟨bound, hbound⟩ := (hs.image weight).bddAbove
  apply bounded_increasing_weight_wellFounded (fun a : s => weight a.val) bound
  intro a
  exact hbound (Set.mem_image_of_mem weight a.property)

/-- Every sequence of admissible cleanup steps on canonical fixed-length states is
well-founded, independently of any claimed universal iteration count. -/
theorem cleanup_wellFounded (n : ℕ) (x : ℝ) :
    WellFounded (fun next current : sortedRepresentations n x =>
      current.val.sum < next.val.sum) :=
  finite_increasing_weight_wellFounded _ (finite_sortedRepresentations n x) List.sum

end Egyptian
