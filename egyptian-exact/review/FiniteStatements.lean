import Egyptian.Finite

#check Egyptian.sortedRepresentations
#print Egyptian.sortedRepresentations
#check @Egyptian.finite_sortedRepresentations
#print axioms Egyptian.finite_sortedRepresentations

-- Independent elaboration check: no positivity or rationality hypothesis on x.
example (n : ℕ) (x : ℝ) : (Egyptian.sortedRepresentations n x).Finite :=
  Egyptian.finite_sortedRepresentations n x
