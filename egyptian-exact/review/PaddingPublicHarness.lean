import Egyptian.Padding

/- Independent review harness: print the actual compiled theorem interfaces and
all helper/public axiom dependencies, and check the two requested public types. -/

open Egyptian

#check @commonNumerator_spec
#check @commonNumerator_eq_prod
#check @unit_split_identity
#check @factor_split_identity
#check @prime_collision_obstruction
#check @safe_split
#check @denominator_ge_two_of_one
#check @padding_pair
#check @expose_top_two
#check @padding_from_top_two
#check @pad_one_preserving_denominator_bounded
#check @pad_one_preserving_denominator

#print axioms commonNumerator_spec
#print axioms commonNumerator_eq_prod
#print axioms unit_split_identity
#print axioms factor_split_identity
#print axioms prime_collision_obstruction
#print axioms safe_split
#print axioms denominator_ge_two_of_one
#print axioms padding_pair
#print axioms expose_top_two
#print axioms padding_from_top_two
#print axioms pad_one_preserving_denominator_bounded
#print axioms pad_one_preserving_denominator

example (input : List ℕ) (marker B : ℕ)
    (positive : ∀ d ∈ input, 0 < d) (distinct : input.Nodup)
    (atLeastThree : 3 ≤ input.length) (sumOne : reciprocalSum input = 1)
    (markerPresent : marker ∈ input) (bound : ∀ d ∈ input, d ≤ B) :
    ∃ out : List ℕ, (∀ d ∈ out, 0 < d) ∧ out.Nodup ∧
      out.length = input.length + 1 ∧ reciprocalSum out = 1 ∧ marker ∈ out ∧
      (∀ d ∈ out, d ≤ B * (B + 1)) :=
  @pad_one_preserving_denominator_bounded input marker B positive distinct
    atLeastThree sumOne markerPresent bound

example (input : List ℕ) (marker : ℕ)
    (positive : ∀ d ∈ input, 0 < d) (distinct : input.Nodup)
    (atLeastThree : 3 ≤ input.length) (sumOne : reciprocalSum input = 1)
    (markerPresent : marker ∈ input) :
    ∃ out : List ℕ, (∀ d ∈ out, 0 < d) ∧ out.Nodup ∧
      out.length = input.length + 1 ∧ reciprocalSum out = 1 ∧ marker ∈ out :=
  @pad_one_preserving_denominator input marker positive distinct atLeastThree
    sumOne markerPresent
