import Lean.Elab.Tactic.Omega

namespace Egyptian.Review

universe u

/-- Core-only orientation check, compiled independently of mathlib setup. -/
theorem bounded_increasing_weight_wellFounded {α : Type u}
    (weight : α → Nat) (bound : Nat) (hbound : ∀ a, weight a ≤ bound) :
    WellFounded (fun next current : α => weight current < weight next) := by
  apply Subrelation.wf (r := (measure (fun a => bound - weight a)).rel)
    (h₂ := (measure (fun a => bound - weight a)).wf)
  intro next current hstep
  change bound - weight next < bound - weight current
  have hn := hbound next
  have hc := hbound current
  omega

/-- A progress rule for every bad state implies existence of a good state.
The state type can be the subtype of a finite invariant state set. -/
theorem terminal_exists_of_bounded_progress {α : Type u}
    (weight : α → Nat) (bound : Nat) (hbound : ∀ a, weight a ≤ bound)
    (good : α → Prop)
    (progress : ∀ current, ¬ good current →
      ∃ next, weight current < weight next) (initial : α) :
    ∃ terminal, good terminal := by
  classical
  have hwf := bounded_increasing_weight_wellFounded weight bound hbound
  apply hwf.induction initial
  intro current ih
  by_cases hg : good current
  · exact ⟨current, hg⟩
  · obtain ⟨next, hn⟩ := progress current hg
    exact ih next hn

#print bounded_increasing_weight_wellFounded
#print axioms bounded_increasing_weight_wellFounded
#print terminal_exists_of_bounded_progress
#print axioms terminal_exists_of_bounded_progress

end Egyptian.Review
