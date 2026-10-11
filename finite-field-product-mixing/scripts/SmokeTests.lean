import FiniteFieldMixing

open scoped BigOperators
open FiniteFieldMixing

section PrimeTwo
local instance : Fact (Nat.Prime 2) := ⟨by norm_num⟩

example (z : ZMod 2) :
    1 / (2 : ℝ) ^ 2 ≤ productSumProbability Finset.univ 4 z := by
  apply four_product_probability_lower_bound
  norm_num [Finset.card_univ, ZMod.card]

example (z : ZMod 2) :
    ∃ a b : Fin 4 → ZMod 2,
      (∀ i, a i ∈ (Finset.univ : Finset (ZMod 2))) ∧
      (∀ i, b i ∈ (Finset.univ : Finset (ZMod 2))) ∧ ∑ i, a i * b i = z := by
  apply four_products_cover
  norm_num [Finset.card_univ, ZMod.card]
end PrimeTwo

section PrimeSeven
local instance : Fact (Nat.Prime 7) := ⟨by norm_num⟩

example (z : ZMod 7) :
    1 / (7 : ℝ) ^ 2 ≤ productSumProbability ({1, 2, 3, 5, 6} : Finset (ZMod 7)) 4 z := by
  apply four_product_probability_lower_bound
  decide
end PrimeSeven
