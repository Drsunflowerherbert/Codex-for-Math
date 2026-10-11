import PositiveBlocks.Blocks
import PositiveBlocks.NormalForm

/-!
# Equality classification for positive block matrices

For nonzero diagonal blocks, equality in the Hilbert–Schmidt product estimate
holds exactly in the positive common-support normal form. The global theorem
keeps the two zero diagonal cases explicit.
-/

open scoped Matrix ComplexConjugate ComplexOrder

namespace PositiveBlocks

variable {m n : Type*} [Fintype m] [Fintype n]

/-- For a positive semidefinite block matrix with nonzero diagonal blocks,
product equality is equivalent to the positive common-support normal form. -/
theorem block_hs_product_eq_iff_commonSupportNormalForm
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (Matrix.fromBlocks A B Bᴴ C).PosSemidef) (hA0 : A ≠ 0) (hC0 : C ≠ 0) :
    (hsSq B = hsNorm A * hsNorm C) ↔ HasCommonSupportNormalForm A B C := by
  classical
  obtain ⟨X, Y, rfl, rfl, rfl⟩ := exists_gram_of_posSemidef_fromBlocks h
  have hX0 : X ≠ 0 := fun hX => hA0 (by simp [hX])
  have hY0 : Y ≠ 0 := fun hY => hC0 (by simp [hY])
  exact gram_product_eq_iff_commonSupportNormalForm X Y hX0 hY0

/-- For nonzero diagonal blocks, product equality in norm notation is
equivalent to the positive common-support normal form. -/
theorem block_hsNorm_product_eq_iff_commonSupportNormalForm
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (Matrix.fromBlocks A B Bᴴ C).PosSemidef) (hA0 : A ≠ 0) (hC0 : C ≠ 0) :
    (hsNorm B ^ 2 = hsNorm A * hsNorm C) ↔ HasCommonSupportNormalForm A B C := by
  rw [hsNorm_sq]
  exact block_hs_product_eq_iff_commonSupportNormalForm h hA0 hC0

/-- The complete product equality classification for a positive block matrix.
Either diagonal block may vanish; otherwise equality has the nonzero positive
common-support normal form. -/
theorem block_hs_product_eq_iff_zero_or_commonSupportNormalForm
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (Matrix.fromBlocks A B Bᴴ C).PosSemidef) :
    (hsSq B = hsNorm A * hsNorm C) ↔
      A = 0 ∨ C = 0 ∨ HasCommonSupportNormalForm A B C := by
  classical
  obtain ⟨X, Y, rfl, rfl, rfl⟩ := exists_gram_of_posSemidef_fromBlocks h
  simpa only [gram_eq_zero_iff] using
    gram_product_eq_iff_zero_or_commonSupportNormalForm X Y

/-- The complete product equality classification in Hilbert–Schmidt norm
notation, including both zero diagonal cases. -/
theorem block_hsNorm_product_eq_iff_zero_or_commonSupportNormalForm
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (Matrix.fromBlocks A B Bᴴ C).PosSemidef) :
    (hsNorm B ^ 2 = hsNorm A * hsNorm C) ↔
      A = 0 ∨ C = 0 ∨ HasCommonSupportNormalForm A B C := by
  rw [hsNorm_sq]
  exact block_hs_product_eq_iff_zero_or_commonSupportNormalForm h

/-- Nonzero product equality forces a common positive rank bounded by both
block dimensions. -/
theorem block_hs_product_eq_ranks
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (Matrix.fromBlocks A B Bᴴ C).PosSemidef) (hA0 : A ≠ 0) (hC0 : C ≠ 0)
    (hEq : hsSq B = hsNorm A * hsNorm C) :
    A.rank = B.rank ∧ A.rank = C.rank ∧ 0 < A.rank ∧
      A.rank ≤ min (Fintype.card m) (Fintype.card n) := by
  have hr := ((block_hs_product_eq_iff_commonSupportNormalForm h hA0 hC0).mp hEq).rank_eq
  exact ⟨hr.1, hr.2.1, hr.2.2.1, le_min hr.2.2.2.1 hr.2.2.2.2⟩

/-- The common rank consequence of nonzero product equality in norm notation. -/
theorem block_hsNorm_product_eq_ranks
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (Matrix.fromBlocks A B Bᴴ C).PosSemidef) (hA0 : A ≠ 0) (hC0 : C ≠ 0)
    (hEq : hsNorm B ^ 2 = hsNorm A * hsNorm C) :
    A.rank = B.rank ∧ A.rank = C.rank ∧ 0 < A.rank ∧
      A.rank ≤ min (Fintype.card m) (Fintype.card n) := by
  rw [hsNorm_sq] at hEq
  exact block_hs_product_eq_ranks h hA0 hC0 hEq

/-- A nonzero product equality case admits an explicit positive normal form
whose support dimension does not exceed either block dimension. -/
theorem block_hsNorm_product_eq_exists_bounded_normalForm
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (Matrix.fromBlocks A B Bᴴ C).PosSemidef) (hA0 : A ≠ 0) (hC0 : C ≠ 0)
    (hEq : hsNorm B ^ 2 = hsNorm A * hsNorm C) :
    ∃ (k : ℕ) (_ : 0 < k) (_ : k ≤ min (Fintype.card m) (Fintype.card n))
      (U : Matrix m (Fin k) ℂ) (V : Matrix n (Fin k) ℂ)
      (H : Matrix (Fin k) (Fin k) ℂ) (t : ℝ),
      H.PosDef ∧ 0 < t ∧ Uᴴ * U = 1 ∧ Vᴴ * V = 1 ∧
        A = U * H * Uᴴ ∧ B = Real.sqrt t • (U * H * Vᴴ) ∧
        C = t • (V * H * Vᴴ) := by
  obtain ⟨k, hk, U, V, H, t, hH, ht, hU, hV, hA, hB, hC⟩ :=
    (block_hsNorm_product_eq_iff_commonSupportNormalForm h hA0 hC0).mp hEq
  have hkm : k ≤ Fintype.card m := by simpa using isometry_card_le U hU
  have hkn : k ≤ Fintype.card n := by simpa using isometry_card_le V hV
  exact ⟨k, hk, le_min hkm hkn, U, V, H, t, hH, ht, hU, hV, hA, hB, hC⟩

end PositiveBlocks
