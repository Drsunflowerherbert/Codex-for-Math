import Egyptian

set_option pp.funBinderTypes true

/- Independent audit harness: print the actual elaborated public theorem types
and the axioms used by each requested mathematical milestone. -/

#print Egyptian.reciprocalSum
#print Egyptian.sortedRepresentations

#check Egyptian.odd_replacement_identity
#print axioms Egyptian.odd_replacement_identity
#check Egyptian.even_replacement_identity
#print axioms Egyptian.even_replacement_identity
#check Egyptian.odd_replacement_growth
#print axioms Egyptian.odd_replacement_growth
#check Egyptian.even_replacement_growth
#print axioms Egyptian.even_replacement_growth
#check Egyptian.finite_sortedRepresentations
#print axioms Egyptian.finite_sortedRepresentations
#check Egyptian.duplicate_extraction
#print axioms Egyptian.duplicate_extraction
#check Egyptian.duplicate_ge_three
#print axioms Egyptian.duplicate_ge_three
#check Egyptian.replacement_exists
#print axioms Egyptian.replacement_exists
#check Egyptian.duplicate_cleanup
#print axioms Egyptian.duplicate_cleanup
#check Egyptian.canonical_perm
#print axioms Egyptian.canonical_perm
#check Egyptian.canonical_mem
#print axioms Egyptian.canonical_mem
#check Egyptian.sorted_duplicate_cleanup
#print axioms Egyptian.sorted_duplicate_cleanup
#check Egyptian.exact_length_distinct
#print axioms Egyptian.exact_length_distinct
#check Egyptian.bounded_increasing_weight_wellFounded
#print axioms Egyptian.bounded_increasing_weight_wellFounded
#check Egyptian.finite_increasing_weight_wellFounded
#print axioms Egyptian.finite_increasing_weight_wellFounded
#check Egyptian.cleanup_wellFounded
#print axioms Egyptian.cleanup_wellFounded
#check Egyptian.two_positive_denominators_sum_one
#print axioms Egyptian.two_positive_denominators_sum_one
#check Egyptian.no_distinct_two_term_one
#print axioms Egyptian.no_distinct_two_term_one
#check Egyptian.boundary_counterexample
#print axioms Egyptian.boundary_counterexample
