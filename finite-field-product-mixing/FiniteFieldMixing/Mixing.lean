import FiniteFieldMixing.Bilinear
import FiniteFieldMixing.FourierBounds
import FiniteFieldMixing.Normalization
import FiniteFieldMixing.Threshold

/-!
# Product-sum mixing and four-product covering

All final results use the standard additive character internally. The sampling
probability is the exact ordered-tuple count divided by `H.card^(2*k)`;
no spectral estimate is an additional hypothesis of the main theorems.
-/

noncomputable section
open scoped BigOperators

namespace FiniteFieldMixing

variable {p : ℕ} [Fact p.Prime]

/-- The requested normalized rectangular nonzero-frequency estimate. -/
theorem uniform_product_fourier_bound
    (A B : Finset (ZMod p)) (hA : A.Nonempty) (hB : B.Nonempty)
    (r : ZMod p) (hr : r ≠ 0) :
    ‖normalizedProductCoeff ZMod.stdAddChar A B r‖ ≤
      Real.sqrt ((p : ℝ) / ((A.card : ℝ) * (B.card : ℝ))) :=
  normalizedProductCoeff_norm_le_sqrt ZMod.stdAddChar
    (ZMod.isPrimitive_stdAddChar p) A B hA hB r hr

/-- The Fourier coefficient of the exact product density is the bilinear average. -/
theorem productDensity_coeff (χ : AddChar (ZMod p) ℂ)
    (H : Finset (ZMod p)) (r : ZMod p) :
    coeff χ (productDensity H) r = normalizedProductCoeff χ H H r := by
  unfold coeff productDensity
  simp_rw [div_mul_eq_mul_div]
  rw [← Finset.sum_div, productCount_weighted_sum]
  simp only [normalizedProductCoeff, bilinearSum, pow_two, mul_assoc]

/-- Character-independent lower bound for `k` independent uniform products. -/
theorem productSumProbability_lower_bound
    (H : Finset (ZMod p)) (hH : H.Nonempty) (k : ℕ) (z : ZMod p) :
    (1 - ((p : ℝ) - 1) * (Real.sqrt (p : ℝ) / (H.card : ℝ)) ^ k) / (p : ℝ) ≤
      productSumProbability H k z := by
  let χ : AddChar (ZMod p) ℂ := ZMod.stdAddChar
  have hχ : χ.IsPrimitive := ZMod.isPrimitive_stdAddChar p
  have hzero : coeff χ (productDensity H) 0 = ((1 : ℝ) : ℂ) := by
    rw [productDensity_coeff, normalizedProductCoeff_zero χ H H hH hH]
    rfl
  have hbound : ∀ t ≠ 0,
      ‖coeff χ (productDensity H) t‖ ≤ Real.sqrt (p : ℝ) / (H.card : ℝ) := by
    intro t ht
    rw [productDensity_coeff]
    exact normalizedProductCoeff_self_norm_le χ hχ H hH t ht
  simpa only [one_pow, ← productSumProbability_eq_re] using
    convolutionPow_re_lower_bound χ hχ (productDensity H) 1
      (Real.sqrt (p : ℝ) / (H.card : ℝ)) hzero hbound k z

/-- The strict Fourier criterion gives a witness for every residue. -/
theorem productSum_cover_of_strict_bound
    (H : Finset (ZMod p)) (hH : H.Nonempty) (k : ℕ)
    (hmix : ((p : ℝ) - 1) * (Real.sqrt (p : ℝ) / (H.card : ℝ)) ^ k < 1)
    (z : ZMod p) :
    ∃ a b : Fin k → ZMod p,
      (∀ i, a i ∈ H) ∧ (∀ i, b i ∈ H) ∧ ∑ i, a i * b i = z := by
  apply (productSumProbability_pos_iff H hH k z).mp
  have hp : (0 : ℝ) < p := by exact_mod_cast (Nat.Prime.pos Fact.out)
  have hlower : 0 <
      (1 - ((p : ℝ) - 1) * (Real.sqrt (p : ℝ) / (H.card : ℝ)) ^ k) / (p : ℝ) :=
    div_pos (sub_pos.mpr hmix) hp
  exact lt_of_lt_of_le hlower (productSumProbability_lower_bound H hH k z)

/-- A fourth-power density threshold forces nonemptiness. -/
theorem nonempty_of_fourth_power_threshold
    (H : Finset (ZMod p)) (hsize : p ^ 3 ≤ H.card ^ 4) : H.Nonempty := by
  apply Finset.card_pos.mp
  have hp : 0 < p ^ 3 := pow_pos (Nat.Prime.pos Fact.out) 3
  by_contra hn
  have hz : H.card = 0 := Nat.eq_zero_of_not_pos hn
  simp only [hz, zero_pow (by decide : 4 ≠ 0)] at hsize
  omega

/-- At the non-strict fourth-power threshold, every residue has probability `≥ 1/p²`. -/
theorem four_product_probability_lower_bound
    (H : Finset (ZMod p)) (hsize : p ^ 3 ≤ H.card ^ 4) (z : ZMod p) :
    1 / (p : ℝ) ^ 2 ≤ productSumProbability H 4 z := by
  have hH : H.Nonempty := nonempty_of_fourth_power_threshold H hsize
  exact le_trans
    (diagonal_threshold_nat p H.card (Nat.Prime.one_le Fact.out) hsize)
    (productSumProbability_lower_bound H hH 4 z)

/-- Every residue is a sum of four products of elements of `H`, with repetition allowed. -/
theorem four_products_cover
    (H : Finset (ZMod p)) (hsize : p ^ 3 ≤ H.card ^ 4) (z : ZMod p) :
    ∃ a b : Fin 4 → ZMod p,
      (∀ i, a i ∈ H) ∧ (∀ i, b i ∈ H) ∧ ∑ i, a i * b i = z := by
  have hH : H.Nonempty := nonempty_of_fourth_power_threshold H hsize
  apply (productSumProbability_pos_iff H hH 4 z).mp
  have hp : (0 : ℝ) < p := by exact_mod_cast (Nat.Prime.pos Fact.out)
  have hpos : (0 : ℝ) < 1 / (p : ℝ) ^ 2 := by positivity
  exact lt_of_lt_of_le hpos (four_product_probability_lower_bound H hsize z)

end FiniteFieldMixing
