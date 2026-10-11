import PositiveBlocks.Basic

/-!
# Sharp Hilbert–Schmidt inequalities for Gram blocks

For rectangular complex matrices `X` and `Y` with the same row type, the
three Gram blocks are `Xᴴ * X`, `Xᴴ * Y`, and `Yᴴ * Y`. Their sum deficit is
the squared Hilbert–Schmidt distance between `X * Xᴴ` and `Y * Yᴴ`.
The product inequality and its equality condition include the zero cases.
No index type is required to be nonempty.
-/

open scoped Matrix ComplexConjugate ComplexOrder

namespace PositiveBlocks

variable {r m n : Type*} [Fintype r] [Fintype m] [Fintype n]

omit [Fintype m] in
/-- A Gram matrix vanishes exactly when its rectangular factor vanishes. -/
theorem gram_eq_zero_iff (X : Matrix r m ℂ) : Xᴴ * X = 0 ↔ X = 0 :=
  Matrix.conjTranspose_mul_self_eq_zero

/-- The Hilbert–Schmidt norm of a Gram matrix detects the zero factor. -/
theorem gram_hsNorm_eq_zero_iff (X : Matrix r m ℂ) :
    hsNorm (Xᴴ * X) = 0 ↔ X = 0 :=
  (hsNorm_eq_zero_iff _).trans (gram_eq_zero_iff X)

/-- The squared Hilbert–Schmidt norm of a Gram matrix detects the zero factor. -/
theorem gram_hsSq_eq_zero_iff (X : Matrix r m ℂ) :
    hsSq (Xᴴ * X) = 0 ↔ X = 0 :=
  (hsSq_eq_zero_iff _).trans (gram_eq_zero_iff X)

/-- The exact sum deficit is the squared distance of the two row Gram matrices. -/
theorem gram_sum_gap (X : Matrix r m ℂ) (Y : Matrix r n ℂ) :
    hsSq (Xᴴ * X) + hsSq (Yᴴ * Y) - 2 * hsSq (Xᴴ * Y) =
      hsSq (X * Xᴴ - Y * Yᴴ) := by
  rw [hsSq_sub, ← hsSq_swap_gram X, ← hsSq_swap_gram Y, hsInner_gram]

/-- The sharp sum inequality for Gram blocks. -/
theorem gram_sum_le (X : Matrix r m ℂ) (Y : Matrix r n ℂ) :
    2 * hsSq (Xᴴ * Y) ≤ hsSq (Xᴴ * X) + hsSq (Yᴴ * Y) := by
  have h := hsSq_nonneg (X * Xᴴ - Y * Yᴴ)
  rw [← gram_sum_gap X Y] at h
  linarith

/-- Equality in the sum inequality is equality of the row Gram matrices. -/
theorem gram_sum_eq_iff (X : Matrix r m ℂ) (Y : Matrix r n ℂ) :
    (2 * hsSq (Xᴴ * Y) = hsSq (Xᴴ * X) + hsSq (Yᴴ * Y)) ↔
      X * Xᴴ = Y * Yᴴ := by
  calc
    (2 * hsSq (Xᴴ * Y) = hsSq (Xᴴ * X) + hsSq (Yᴴ * Y)) ↔
        hsSq (X * Xᴴ - Y * Yᴴ) = 0 := by
      rw [← gram_sum_gap X Y]
      constructor <;> intro h <;> linarith
    _ ↔ X * Xᴴ = Y * Yᴴ := (hsSq_eq_zero_iff _).trans sub_eq_zero

/-- The weighted squared distance is an exact multiple of the product deficit. -/
theorem gram_product_deficit (X : Matrix r m ℂ) (Y : Matrix r n ℂ) :
    hsSq (hsNorm (Yᴴ * Y) • (X * Xᴴ) - hsNorm (Xᴴ * X) • (Y * Yᴴ)) =
      2 * hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y) *
        (hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y) - hsSq (Xᴴ * Y)) := by
  rw [hsSq_weighted_sub, ← hsSq_swap_gram X, ← hsSq_swap_gram Y,
    hsInner_gram, ← hsNorm_sq (Xᴴ * X), ← hsNorm_sq (Yᴴ * Y)]
  ring

/-- The sharp product inequality for Gram blocks, including zero factors. -/
theorem gram_product_le (X : Matrix r m ℂ) (Y : Matrix r n ℂ) :
    hsSq (Xᴴ * Y) ≤ hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y) := by
  by_cases hx : hsNorm (Xᴴ * X) = 0
  · have hX := (gram_hsNorm_eq_zero_iff X).mp hx
    subst X
    simp
  by_cases hy : hsNorm (Yᴴ * Y) = 0
  · have hY := (gram_hsNorm_eq_zero_iff Y).mp hy
    subst Y
    simp
  have ha : 0 < hsNorm (Xᴴ * X) :=
    lt_of_le_of_ne (hsNorm_nonneg _) (Ne.symm hx)
  have hc : 0 < hsNorm (Yᴴ * Y) :=
    lt_of_le_of_ne (hsNorm_nonneg _) (Ne.symm hy)
  have hpos := mul_pos ha hc
  have hnonneg := hsSq_nonneg
    (hsNorm (Yᴴ * Y) • (X * Xᴴ) - hsNorm (Xᴴ * X) • (Y * Yᴴ))
  rw [gram_product_deficit] at hnonneg
  nlinarith

/-- Equality in the product inequality is proportionality of row Gram matrices.
The weighted formulation remains exact when either norm is zero. -/
theorem gram_product_eq_iff (X : Matrix r m ℂ) (Y : Matrix r n ℂ) :
    (hsSq (Xᴴ * Y) = hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y)) ↔
      hsNorm (Yᴴ * Y) • (X * Xᴴ) = hsNorm (Xᴴ * X) • (Y * Yᴴ) := by
  by_cases hx : hsNorm (Xᴴ * X) = 0
  · have hX := (gram_hsNorm_eq_zero_iff X).mp hx
    subst X
    simp
  by_cases hy : hsNorm (Yᴴ * Y) = 0
  · have hY := (gram_hsNorm_eq_zero_iff Y).mp hy
    subst Y
    simp
  have ha : 0 < hsNorm (Xᴴ * X) :=
    lt_of_le_of_ne (hsNorm_nonneg _) (Ne.symm hx)
  have hc : 0 < hsNorm (Yᴴ * Y) :=
    lt_of_le_of_ne (hsNorm_nonneg _) (Ne.symm hy)
  have hpos := mul_pos ha hc
  calc
    (hsSq (Xᴴ * Y) = hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y)) ↔
        hsSq (hsNorm (Yᴴ * Y) • (X * Xᴴ) -
          hsNorm (Xᴴ * X) • (Y * Yᴴ)) = 0 := by
      rw [gram_product_deficit]
      constructor
      · intro h
        rw [h]
        ring
      · intro h
        nlinarith
    _ ↔ hsNorm (Yᴴ * Y) • (X * Xᴴ) = hsNorm (Xᴴ * X) • (Y * Yᴴ) :=
      (hsSq_eq_zero_iff _).trans sub_eq_zero

private theorem scaled_eq_iff_normalized_eq
    {V : Type*} [AddCommGroup V] [Module ℝ V]
    {P Q : V} {a c : ℝ} (ha : 0 < a) (hc : 0 < c) :
    c • P = a • Q ↔ (1 / a) • P = (1 / c) • Q := by
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hc0 : c ≠ 0 := ne_of_gt hc
  constructor
  · intro h
    have hh := congrArg (fun X : V => a⁻¹ • c⁻¹ • X) h
    simpa [one_div, smul_smul, mul_comm, mul_left_comm, mul_assoc, ha0, hc0] using hh
  · intro h
    have hh := congrArg (fun X : V => (a * c) • X) h
    have hca : (a * c) * (1 / a) = c := by field_simp
    have hac : (a * c) * (1 / c) = a := by field_simp
    simpa only [smul_smul, hca, hac] using hh

/-- For positive diagonal norms, product equality is equality of the normalized
row Gram matrices. -/
theorem gram_product_eq_iff_normalized (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (ha : 0 < hsNorm (Xᴴ * X)) (hc : 0 < hsNorm (Yᴴ * Y)) :
    (hsSq (Xᴴ * Y) = hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y)) ↔
      (1 / hsNorm (Xᴴ * X)) • (X * Xᴴ) =
        (1 / hsNorm (Yᴴ * Y)) • (Y * Yᴴ) :=
  (gram_product_eq_iff X Y).trans (scaled_eq_iff_normalized_eq ha hc)

end PositiveBlocks
