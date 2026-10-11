import Mathlib.Data.Set.Finite.Lemmas
import Lean.Elab.Tactic.Omega

namespace Egyptian.Review

/-- Independent termination audit: the relation places the next (larger-weight)
state before its current state, as required for well-founded recursion. -/
theorem finite_increasing_weight_wellFounded {α : Type*} {s : Set α}
    (hs : s.Finite) (weight : α → ℕ) :
    WellFounded (fun next current : s => weight current.val < weight next.val) := by
  classical
  obtain ⟨bound, hb⟩ :=
    Set.exists_upper_bound_image (weight '' s) (fun n : ℕ => n) (hs.image weight)
  have hbound (a : s) : weight a.val ≤ bound := by
    exact hb (weight a.val) (Set.mem_image_of_mem weight a.property)
  apply Subrelation.wf (r := (measure (fun a : s => bound - weight a.val)).rel)
    (h₂ := (measure (fun a : s => bound - weight a.val)).wf)
  intro next current hstep
  change bound - weight next.val < bound - weight current.val
  have hn := hbound next
  have hc := hbound current
  omega

/-- The subtype is essential: ambient states with unbounded weight need not
terminate. Every next state supplied to recursion must carry membership in s. -/
theorem finite_increasing_weight_induction {α : Type*} {s : Set α}
    (hs : s.Finite) (weight : α → ℕ) (P : s → Prop)
    (step : ∀ current, (∀ next, weight current.val < weight next.val → P next) → P current) :
    ∀ current, P current := by
  intro current
  exact (finite_increasing_weight_wellFounded hs weight).induction current step

#check @finite_increasing_weight_wellFounded
#check @finite_increasing_weight_induction
#print axioms finite_increasing_weight_wellFounded
#print axioms finite_increasing_weight_induction

end Egyptian.Review
