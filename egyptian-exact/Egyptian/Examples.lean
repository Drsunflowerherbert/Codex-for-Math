import Egyptian.Counterexample

namespace Egyptian

/-- Exact small cleanup example; all arithmetic is checked by Lean. -/
theorem example_two_thirds :
    reciprocalSum [4, 4, 6] = (2 : ℝ) / 3 ∧
      reciprocalSum [3, 4, 12] = reciprocalSum [4, 4, 6] ∧
      ([3, 4, 12] : List ℕ).Nodup ∧
      ([3, 4, 12] : List ℕ).length = ([4, 4, 6] : List ℕ).length := by
  norm_num [reciprocalSum]

/-- Concrete warning that cleanup need not preserve an arbitrary denominator. -/
theorem example_marker_loss :
    (6 : ℕ) ∈ [4, 4, 6] ∧ (6 : ℕ) ∉ [3, 4, 12] ∧
      reciprocalSum [4, 4, 6] = reciprocalSum [3, 4, 12] := by
  norm_num [reciprocalSum]

/-- A permitted cleanup step may create additional repeated entries. -/
theorem example_new_collisions :
    reciprocalSum [6, 10, 10, 30] = reciprocalSum [6, 6, 30, 30] ∧
      ([6, 10, 10, 30] : List ℕ).sum = 56 ∧
      ([6, 6, 30, 30] : List ℕ).sum = 72 := by
  norm_num [reciprocalSum]

/-- A real product-collision case, repaired by factoring the second largest denominator. -/
theorem example_padding_product_collision :
    reciprocalSum [2, 6, 7, 14, 15, 20, 420] = 1 ∧
      reciprocalSum [2, 6, 7, 14, 15, 22, 220, 420] = 1 ∧
      ([2, 6, 7, 14, 15, 22, 220, 420] : List ℕ).Nodup ∧
      ([2, 6, 7, 14, 15, 22, 220, 420] : List ℕ).length =
        ([2, 6, 7, 14, 15, 20, 420] : List ℕ).length + 1 ∧
      (420 : ℕ) ∈ [2, 6, 7, 14, 15, 22, 220, 420] := by
  norm_num [reciprocalSum]

end Egyptian
