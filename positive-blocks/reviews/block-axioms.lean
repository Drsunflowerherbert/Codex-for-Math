import PositiveBlocks.Blocks

/- A standalone compilation and axiom-audit companion for Blocks.lean. -/

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

namespace PositiveBlocks

open Matrix
open scoped ComplexOrder MatrixOrder

variable {m n r : Type*} [Fintype m] [Fintype n] [Fintype r]

example {S : Matrix r r ℂ} (hS : S.PosSemidef)
    (U : Matrix r m ℂ) (V : Matrix r n ℂ) :
    ∃ (X : Matrix r m ℂ) (Y : Matrix r n ℂ),
      Uᴴ * S * U = Xᴴ * X ∧ Uᴴ * S * V = Xᴴ * Y ∧ Vᴴ * S * V = Yᴴ * Y := by
  classical
  have hZ : (CFC.sqrt S)ᴴ * CFC.sqrt S = S := by
    rw [(CFC.sqrt_nonneg S).posSemidef.isHermitian.eq,
      CFC.sqrt_mul_sqrt_self S hS.nonneg]
  refine ⟨CFC.sqrt S * U, CFC.sqrt S * V, ?_, ?_, ?_⟩
  · calc
      Uᴴ * S * U = Uᴴ * ((CFC.sqrt S)ᴴ * CFC.sqrt S) * U := by rw [hZ]
      _ = _ := by simp only [conjTranspose_mul, Matrix.mul_assoc]
  · calc
      Uᴴ * S * V = Uᴴ * ((CFC.sqrt S)ᴴ * CFC.sqrt S) * V := by rw [hZ]
      _ = _ := by simp only [conjTranspose_mul, Matrix.mul_assoc]
  · calc
      Vᴴ * S * V = Vᴴ * ((CFC.sqrt S)ᴴ * CFC.sqrt S) * V := by rw [hZ]
      _ = _ := by simp only [conjTranspose_mul, Matrix.mul_assoc]

end PositiveBlocks
