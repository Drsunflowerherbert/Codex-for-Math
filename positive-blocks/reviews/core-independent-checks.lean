import PositiveBlocks.Corollaries

open scoped Matrix ComplexConjugate ComplexOrder
open Matrix PositiveBlocks

namespace CoreIndependentReview

variable {m n r s : Type*} [Fintype m] [Fintype n] [Fintype r] [Fintype s]

-- The same equality criterion is valid across unrelated Gram row types.
example {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (X' : Matrix s m ℂ) (Y' : Matrix s n ℂ)
    (hA : A = Xᴴ * X) (hB : B = Xᴴ * Y) (hC : C = Yᴴ * Y)
    (hA' : A = X'ᴴ * X') (hB' : B = X'ᴴ * Y') (hC' : C = Y'ᴴ * Y') :
    (X * Xᴴ = Y * Yᴴ) ↔ (X' * X'ᴴ = Y' * Y'ᴴ) := by
  exact (block_hs_sum_eq_iff_of_gram X Y hA hB hC).symm.trans
    (block_hs_sum_eq_iff_of_gram X' Y' hA' hB' hC')

example {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (X' : Matrix s m ℂ) (Y' : Matrix s n ℂ)
    (hA : A = Xᴴ * X) (hB : B = Xᴴ * Y) (hC : C = Yᴴ * Y)
    (hA' : A = X'ᴴ * X') (hB' : B = X'ᴴ * Y') (hC' : C = Y'ᴴ * Y') :
    (hsNorm C • (X * Xᴴ) = hsNorm A • (Y * Yᴴ)) ↔
      (hsNorm C • (X' * X'ᴴ) = hsNorm A • (Y' * Y'ᴴ)) := by
  exact (block_hs_product_eq_iff_of_gram X Y hA hB hC).symm.trans
    (block_hs_product_eq_iff_of_gram X' Y' hA' hB' hC')

-- A zero diagonal block gives product equality, even if C is nonzero.
example {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks (0 : Matrix m m ℂ) B Bᴴ C).PosSemidef) :
    hsSq B = hsNorm (0 : Matrix m m ℂ) * hsNorm C := by
  have hB := block_offdiag_eq_zero_of_left_eq_zero h rfl
  simp [hB]

-- In the same zero-block case, sum equality forces the other block to vanish.
example {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks (0 : Matrix m m ℂ) B Bᴴ C).PosSemidef)
    (hEq : 2 * hsSq B = hsSq (0 : Matrix m m ℂ) + hsSq C) : C = 0 := by
  have hB := block_offdiag_eq_zero_of_left_eq_zero h rfl
  apply (hsSq_eq_zero_iff C).mp
  simpa [hB] using hEq.symm

-- No hidden nonemptiness assumption prevents applying the block theorem.
example {A : Matrix (Fin 0) (Fin 0) ℂ} {B : Matrix (Fin 0) n ℂ}
    {C : Matrix n n ℂ} (h : (fromBlocks A B Bᴴ C).PosSemidef) :
    hsSq B ≤ hsNorm A * hsNorm C := block_hs_product_le h

-- Both compression columns may have arbitrary, different finite types.
example {S : Matrix (Fin 0) (Fin 0) ℂ} (hS : S.PosSemidef)
    (U : Matrix (Fin 0) m ℂ) (V : Matrix (Fin 0) n ℂ) :
    hsSq (Uᴴ * S * V) ≤ hsNorm (Uᴴ * S * U) * hsNorm (Vᴴ * S * V) :=
  compression_hs_product_le hS U V

-- Independent check that the weighted deficit gives study PB3, equation (5).
example (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (ha : 0 < hsNorm (Xᴴ * X)) (hc : 0 < hsNorm (Yᴴ * Y)) :
    hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y) - hsSq (Xᴴ * Y) =
      (hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y) / 2) *
        hsSq ((1 / hsNorm (Xᴴ * X)) • (X * Xᴴ) -
          (1 / hsNorm (Yᴴ * Y)) • (Y * Yᴴ)) := by
  rw [hsSq_weighted_sub, ← hsSq_swap_gram X, ← hsSq_swap_gram Y,
    hsInner_gram, ← hsNorm_sq (Xᴴ * X), ← hsNorm_sq (Yᴴ * Y)]
  field_simp [ne_of_gt ha, ne_of_gt hc]
  ring

end CoreIndependentReview


#print axioms PositiveBlocks.gram_eq_zero_iff
#print axioms PositiveBlocks.gram_hsNorm_eq_zero_iff
#print axioms PositiveBlocks.gram_hsSq_eq_zero_iff
#print axioms PositiveBlocks.gram_sum_gap
#print axioms PositiveBlocks.gram_sum_le
#print axioms PositiveBlocks.gram_sum_eq_iff
#print axioms PositiveBlocks.gram_product_deficit
#print axioms PositiveBlocks.gram_product_le
#print axioms PositiveBlocks.gram_product_eq_iff
#print axioms PositiveBlocks.gram_product_eq_iff_normalized
#print axioms PositiveBlocks.fromBlocks_gram
#print axioms PositiveBlocks.posSemidef_fromBlocks_gram
#print axioms PositiveBlocks.exists_gram_of_posSemidef_fromBlocks
#print axioms PositiveBlocks.posSemidef_fromBlocks_iff_exists_gram
#print axioms PositiveBlocks.block_offdiag_eq_zero_of_left_eq_zero
#print axioms PositiveBlocks.block_offdiag_eq_zero_of_right_eq_zero
#print axioms PositiveBlocks.block_hs_product_le
#print axioms PositiveBlocks.block_hs_sum_le
#print axioms PositiveBlocks.block_hsNorm_product_le
#print axioms PositiveBlocks.block_hsNorm_sum_le
#print axioms PositiveBlocks.block_hs_sum_gap_of_gram
#print axioms PositiveBlocks.block_hsNorm_sum_gap_of_gram
#print axioms PositiveBlocks.block_hs_product_deficit_of_gram
#print axioms PositiveBlocks.block_hs_sum_eq_iff_of_gram
#print axioms PositiveBlocks.block_hs_product_eq_iff_of_gram
#print axioms PositiveBlocks.block_hsNorm_product_eq_iff_of_gram
#print axioms PositiveBlocks.block_hsNorm_sum_eq_iff_of_gram
#print axioms PositiveBlocks.block_hs_product_eq_iff_normalized_of_gram
#print axioms PositiveBlocks.block_hs_sum_gap_exists
#print axioms PositiveBlocks.block_hs_sum_eq_iff_exists_gram
#print axioms PositiveBlocks.block_hs_product_eq_iff_exists_gram
#print axioms PositiveBlocks.block_hsNorm_product_eq_iff_exists_gram
#print axioms PositiveBlocks.block_hsNorm_sum_eq_iff_exists_gram
#print axioms PositiveBlocks.fromBlocks_compression
#print axioms PositiveBlocks.posSemidef_fromBlocks_compression
#print axioms PositiveBlocks.exists_compression_gram
#print axioms PositiveBlocks.compression_hs_product_le
#print axioms PositiveBlocks.compression_hsNorm_product_le
#print axioms PositiveBlocks.compression_hs_sum_le
#print axioms PositiveBlocks.compression_hsNorm_sum_le
#print axioms PositiveBlocks.gram_normalized_product_deficit
#print axioms PositiveBlocks.hs_sum_deficit_decomposition
#print axioms PositiveBlocks.block_sum_eq_iff_product_eq_and_norms_eq
