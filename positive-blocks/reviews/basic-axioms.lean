import PositiveBlocks.Basic

#print axioms PositiveBlocks.hsSq_eq_sum
#print axioms PositiveBlocks.hsSq_nonneg
#print axioms PositiveBlocks.hsSq_eq_zero_iff
#print axioms PositiveBlocks.hsNorm_sq
#print axioms PositiveBlocks.hsNorm_eq_zero_iff
#print axioms PositiveBlocks.hsSq_weighted_sub
#print axioms PositiveBlocks.hsSq_swap_gram
#print axioms PositiveBlocks.hsInner_gram
#print axioms PositiveBlocks.hsNorm_eq_frobenius

set_option pp.explicit true in
#check PositiveBlocks.hsNorm_eq_frobenius
