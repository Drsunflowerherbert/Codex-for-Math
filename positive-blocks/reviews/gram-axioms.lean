import PositiveBlocks.Intrinsic

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
#print axioms PositiveBlocks.gram_proportional_mul_conjTranspose
#print axioms PositiveBlocks.gram_proportional_conjTranspose_mul
#print axioms PositiveBlocks.gram_proportional_intertwine
#print axioms PositiveBlocks.gram_proportional_intrinsic
#print axioms PositiveBlocks.gram_product_eq_proportional
#print axioms PositiveBlocks.gram_product_eq_intrinsic
#print axioms PositiveBlocks.gram_product_normalized_deficit
#print axioms PositiveBlocks.gram_product_eq_iff_mul_conjTranspose
#print axioms PositiveBlocks.gram_product_eq_iff_intrinsic
#print axioms PositiveBlocks.gram_sum_eq_iff_intrinsic
#print axioms PositiveBlocks.block_hs_product_eq_iff_mul_conjTranspose
#print axioms PositiveBlocks.block_hs_product_eq_iff_intrinsic
#print axioms PositiveBlocks.block_hs_sum_eq_iff_intrinsic
#print axioms PositiveBlocks.block_hs_product_normalized_deficit_of_gram

open scoped Matrix ComplexConjugate

example (X : Matrix (Fin 0) (Fin 2) ℂ) (Y : Matrix (Fin 0) (Fin 3) ℂ) :
    PositiveBlocks.hsSq (Xᴴ * Y) ≤
      PositiveBlocks.hsNorm (Xᴴ * X) * PositiveBlocks.hsNorm (Yᴴ * Y) :=
  PositiveBlocks.gram_product_le X Y

example (X : Matrix (Fin 2) (Fin 0) ℂ) (Y : Matrix (Fin 2) (Fin 3) ℂ) :
    (PositiveBlocks.hsSq (Xᴴ * Y) =
      PositiveBlocks.hsNorm (Xᴴ * X) * PositiveBlocks.hsNorm (Yᴴ * Y)) ↔
      PositiveBlocks.hsNorm (Yᴴ * Y) • (X * Xᴴ) =
        PositiveBlocks.hsNorm (Xᴴ * X) • (Y * Yᴴ) :=
  PositiveBlocks.gram_product_eq_iff X Y
