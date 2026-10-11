import PositiveBlocks.Blocks

/-!
# Exact normalized deficits and comparison of equality cases
-/

open scoped Matrix ComplexConjugate ComplexOrder

namespace PositiveBlocks

variable {r m n : Type*} [Fintype r] [Fintype m] [Fintype n]

/-- The exact normalized product deficit, for positive diagonal norms. -/
theorem gram_normalized_product_deficit (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (ha : 0 < hsNorm (Xᴴ * X)) (hc : 0 < hsNorm (Yᴴ * Y)) :
    hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y) - hsSq (Xᴴ * Y) =
      (hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y) / 2) *
        hsSq ((1 / hsNorm (Xᴴ * X)) • (X * Xᴴ) -
          (1 / hsNorm (Yᴴ * Y)) • (Y * Yᴴ)) := by
  rw [hsSq_weighted_sub, ← hsSq_swap_gram X, ← hsSq_swap_gram Y,
    hsInner_gram, ← hsNorm_sq (Xᴴ * X), ← hsNorm_sq (Yᴴ * Y)]
  field_simp [ne_of_gt ha, ne_of_gt hc]
  ring

/-- The sum deficit separates the norm imbalance and the product deficit. -/
theorem hs_sum_deficit_decomposition (A : Matrix m m ℂ) (B : Matrix m n ℂ)
    (C : Matrix n n ℂ) :
    hsSq A + hsSq C - 2 * hsSq B =
      (hsNorm A - hsNorm C) ^ 2 + 2 * (hsNorm A * hsNorm C - hsSq B) := by
  rw [← hsNorm_sq A, ← hsNorm_sq C]
  ring

/-- A positive block attains sum equality exactly when it attains product
equality and its two diagonal Hilbert–Schmidt norms agree. -/
theorem block_sum_eq_iff_product_eq_and_norms_eq
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (Matrix.fromBlocks A B Bᴴ C).PosSemidef) :
    (2 * hsSq B = hsSq A + hsSq C) ↔
      hsSq B = hsNorm A * hsNorm C ∧ hsNorm A = hsNorm C := by
  have hp := block_hs_product_le h
  have ha := hsNorm_sq A
  have hc := hsNorm_sq C
  constructor
  · intro he
    have hd := sq_nonneg (hsNorm A - hsNorm C)
    have hn : hsNorm A = hsNorm C := by nlinarith
    exact ⟨by nlinarith, hn⟩
  · rintro ⟨he, hn⟩
    nlinarith

end PositiveBlocks
