import FiniteFieldMixing.Fourier
import FiniteFieldMixing.Counting

/-!
# Exact finite probability normalization

The sample space for `k` products consists of `2*k` independent coordinates
uniform on `H`. Its size is `H.card^(2*k)`. Natural convolution counts retain
each ordered tuple's multiplicity, even when several tuples give the same
product or sum. Dividing by this size gives the uniform sampling probability.
-/

noncomputable section
open scoped BigOperators

namespace FiniteFieldMixing

variable {p : ℕ} [Fact p.Prime]

/-- The probability mass function of one independent uniform product. -/
def productDensity (H : Finset (ZMod p)) (z : ZMod p) : ℂ :=
  (productCount H z : ℂ) / (H.card : ℂ) ^ 2

/-- Exact probability of the sum of `k` independent ordered products. -/
def productSumProbability (H : Finset (ZMod p)) (k : ℕ) (z : ZMod p) : ℝ :=
  (convolutionCount H k z : ℝ) / (H.card : ℝ) ^ (2 * k)

/-- The normalized convolution count is exactly an event cardinality divided
by the cardinality of the independent uniform Cartesian sample space. -/
theorem productSumProbability_eq_tuple_probability
    (H : Finset (ZMod p)) (k : ℕ) (z : ZMod p) :
    productSumProbability H k z =
      (tupleCount H k z : ℝ) / (Fintype.card (TupleSpace H k) : ℝ) := by
  rw [productSumProbability, convolutionCount_eq_tupleCount, tupleSpace_card, Nat.cast_pow]

/-- Natural convolution agrees with complex convolution after casting. -/
theorem convolution_natCast (f g : ZMod p → ℕ) (z : ZMod p) :
    convolution (fun x => (f x : ℂ)) (fun x => (g x : ℂ)) z =
      (natConvolution f g z : ℂ) := by
  simp [convolution, natConvolution]

/-- The iterated natural counts are precisely the iterated complex convolution. -/
theorem convolutionPow_natCast (H : Finset (ZMod p)) (k : ℕ) (z : ZMod p) :
    convolutionPow (fun x => (productCount H x : ℂ)) k z =
      (convolutionCount H k z : ℂ) := by
  induction k generalizing z with
  | zero => simp [convolutionPow, convolutionCount]
  | succ k ih =>
      simp only [convolutionPow, convolutionCount_succ]
      have hfun : convolutionPow (fun x => (productCount H x : ℂ)) k =
          fun x => (convolutionCount H k x : ℂ) := funext ih
      rw [hfun, convolution_natCast]

/-- Normalized convolution retains the exact count denominator. -/
theorem convolutionPow_productDensity (H : Finset (ZMod p)) (k : ℕ)
    (z : ZMod p) :
    convolutionPow (productDensity H) k z =
      (convolutionCount H k z : ℂ) / (H.card : ℂ) ^ (2 * k) := by
  change convolutionPow (fun x => (productCount H x : ℂ) / (H.card : ℂ) ^ 2) k z = _
  rw [convolutionPow_div, convolutionPow_natCast, ← pow_mul]

/-- Taking the real part recovers the exact uniform probability. -/
theorem productSumProbability_eq_re (H : Finset (ZMod p)) (k : ℕ)
    (z : ZMod p) :
    productSumProbability H k z = (convolutionPow (productDensity H) k z).re := by
  rw [convolutionPow_productDensity]
  change (convolutionCount H k z : ℝ) / (H.card : ℝ) ^ (2 * k) = _
  rw [← Complex.ofReal_natCast, ← Complex.ofReal_natCast,
    ← Complex.ofReal_pow, ← Complex.ofReal_div, Complex.ofReal_re]

/-- Every exact probability is nonnegative. -/
theorem productSumProbability_nonneg (H : Finset (ZMod p)) (k : ℕ)
    (z : ZMod p) : 0 ≤ productSumProbability H k z := by
  exact div_nonneg (Nat.cast_nonneg _) (pow_nonneg (Nat.cast_nonneg _) _)

/-- Nonempty sampling sets give total probability one. -/
theorem productSumProbability_sum (H : Finset (ZMod p)) (hH : H.Nonempty)
    (k : ℕ) : ∑ z, productSumProbability H k z = 1 := by
  have hh : (H.card : ℝ) ≠ 0 := by exact_mod_cast hH.card_ne_zero
  simp only [productSumProbability, ← Finset.sum_div]
  rw [← Nat.cast_sum, convolutionCount_sum, Nat.cast_pow]
  exact div_self (pow_ne_zero _ hh)

/-- Positive probability supplies an actual ordered product-sum tuple. -/
theorem productSumProbability_pos_iff (H : Finset (ZMod p)) (hH : H.Nonempty)
    (k : ℕ) (z : ZMod p) :
    0 < productSumProbability H k z ↔
      ∃ a b : Fin k → ZMod p,
        (∀ i, a i ∈ H) ∧ (∀ i, b i ∈ H) ∧ ∑ i, a i * b i = z := by
  have hh : 0 < (H.card : ℝ) := by exact_mod_cast hH.card_pos
  rw [productSumProbability, div_pos_iff_of_pos_right (pow_pos hh _)]
  rw [Nat.cast_pos, convolutionCount_pos_iff]

end FiniteFieldMixing
