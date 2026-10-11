import Mathlib.Analysis.Matrix.Order
import Mathlib.Data.Matrix.ColumnRowPartitioned
import PositiveBlocks.Gram

/-!
# Gram factorizations of positive block matrices

Every positive semidefinite complex block matrix admits a rectangular Gram
factorization.  The row index of the factors is the sum of the two block index
types, so no rank or invertibility assumption is needed.
-/

namespace PositiveBlocks

open Matrix
open scoped ComplexOrder MatrixOrder

variable {m n r : Type*} [Fintype m] [Fintype n] [Fintype r]

omit [Fintype m] [Fintype n] in
/-- The Gram matrix of a pair of rectangular matrices, in block form. -/
theorem fromBlocks_gram (X : Matrix r m ℂ) (Y : Matrix r n ℂ) :
    fromBlocks (Xᴴ * X) (Xᴴ * Y) (Xᴴ * Y)ᴴ (Yᴴ * Y) =
      (fromCols X Y)ᴴ * fromCols X Y := by
  rw [conjTranspose_fromCols_eq_fromRows_conjTranspose,
    fromRows_mul_fromCols, conjTranspose_mul, conjTranspose_conjTranspose]

/-- A block matrix assembled from any two rectangular Gram factors is positive
semidefinite. -/
theorem posSemidef_fromBlocks_gram (X : Matrix r m ℂ) (Y : Matrix r n ℂ) :
    (fromBlocks (Xᴴ * X) (Xᴴ * Y) (Xᴴ * Y)ᴴ (Yᴴ * Y)).PosSemidef := by
  rw [fromBlocks_gram]
  exact posSemidef_conjTranspose_mul_self (fromCols X Y)

/-- A positive semidefinite block matrix has a common rectangular Gram
factorization.  This also covers empty block index types. -/
theorem exists_gram_of_posSemidef_fromBlocks
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks A B Bᴴ C).PosSemidef) :
    ∃ (X : Matrix (m ⊕ n) m ℂ) (Y : Matrix (m ⊕ n) n ℂ),
      A = Xᴴ * X ∧ B = Xᴴ * Y ∧ C = Yᴴ * Y := by
  classical
  let Z : Matrix (m ⊕ n) (m ⊕ n) ℂ := CFC.sqrt (fromBlocks A B Bᴴ C)
  have hZ : fromBlocks A B Bᴴ C = Zᴴ * Z := by
    dsimp [Z]
    rw [(CFC.sqrt_nonneg (fromBlocks A B Bᴴ C)).posSemidef.isHermitian.eq,
      CFC.sqrt_mul_sqrt_self (fromBlocks A B Bᴴ C) h.nonneg]
  refine ⟨Z.submatrix id Sum.inl, Z.submatrix id Sum.inr, ?_, ?_, ?_⟩
  all_goals
    rw [conjTranspose_submatrix,
      ← submatrix_mul _ _ _ id _ Function.bijective_id]
    rw [← hZ]
    rfl

/-- Positivity of a complex block matrix is equivalent to a common rectangular
Gram factorization of its three independent blocks. -/
theorem posSemidef_fromBlocks_iff_exists_gram
    (A : Matrix m m ℂ) (B : Matrix m n ℂ) (C : Matrix n n ℂ) :
    (fromBlocks A B Bᴴ C).PosSemidef ↔
      ∃ (X : Matrix (m ⊕ n) m ℂ) (Y : Matrix (m ⊕ n) n ℂ),
        A = Xᴴ * X ∧ B = Xᴴ * Y ∧ C = Yᴴ * Y := by
  refine ⟨exists_gram_of_posSemidef_fromBlocks, ?_⟩
  rintro ⟨X, Y, rfl, rfl, rfl⟩
  exact posSemidef_fromBlocks_gram X Y

/-- If the first diagonal block of a positive semidefinite block matrix is
zero, its off-diagonal block is zero. -/
theorem block_offdiag_eq_zero_of_left_eq_zero
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks A B Bᴴ C).PosSemidef) (hA : A = 0) : B = 0 := by
  obtain ⟨X, Y, hX, hB, _⟩ := exists_gram_of_posSemidef_fromBlocks h
  have hX0 : X = 0 := trace_conjTranspose_mul_self_eq_zero_iff.mp (by
    rw [← hX, hA, trace_zero])
  simpa [hX0] using hB

/-- If the second diagonal block of a positive semidefinite block matrix is
zero, its off-diagonal block is zero. -/
theorem block_offdiag_eq_zero_of_right_eq_zero
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks A B Bᴴ C).PosSemidef) (hC : C = 0) : B = 0 := by
  obtain ⟨X, Y, _, hB, hY⟩ := exists_gram_of_posSemidef_fromBlocks h
  have hY0 : Y = 0 := trace_conjTranspose_mul_self_eq_zero_iff.mp (by
    rw [← hY, hC, trace_zero])
  simpa [hY0] using hB

/-- The sharp product estimate for a positive semidefinite complex block
matrix, including vanishing diagonal blocks. -/
theorem block_hs_product_le
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks A B Bᴴ C).PosSemidef) :
    hsSq B ≤ hsNorm A * hsNorm C := by
  obtain ⟨X, Y, rfl, rfl, rfl⟩ := exists_gram_of_posSemidef_fromBlocks h
  exact gram_product_le X Y

/-- The sharp sum estimate for a positive semidefinite complex block matrix. -/
theorem block_hs_sum_le
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks A B Bᴴ C).PosSemidef) :
    2 * hsSq B ≤ hsSq A + hsSq C := by
  obtain ⟨X, Y, rfl, rfl, rfl⟩ := exists_gram_of_posSemidef_fromBlocks h
  exact gram_sum_le X Y

/-- The product estimate in Hilbert–Schmidt norm notation. -/
theorem block_hsNorm_product_le
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks A B Bᴴ C).PosSemidef) :
    hsNorm B ^ 2 ≤ hsNorm A * hsNorm C := by
  rw [hsNorm_sq]
  exact block_hs_product_le h

/-- The sum estimate in Hilbert–Schmidt norm notation. -/
theorem block_hsNorm_sum_le
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks A B Bᴴ C).PosSemidef) :
    2 * hsNorm B ^ 2 ≤ hsNorm A ^ 2 + hsNorm C ^ 2 := by
  simp only [hsNorm_sq]
  exact block_hs_sum_le h

/-- The exact sum gap, evaluated in any common Gram factorization. -/
theorem block_hs_sum_gap_of_gram
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (hA : A = Xᴴ * X) (hB : B = Xᴴ * Y) (hC : C = Yᴴ * Y) :
    hsSq A + hsSq C - 2 * hsSq B = hsSq (X * Xᴴ - Y * Yᴴ) := by
  rw [hA, hB, hC]
  exact gram_sum_gap X Y

/-- The exact sum gap in Hilbert–Schmidt norm notation. -/
theorem block_hsNorm_sum_gap_of_gram
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (hA : A = Xᴴ * X) (hB : B = Xᴴ * Y) (hC : C = Yᴴ * Y) :
    hsNorm A ^ 2 + hsNorm C ^ 2 - 2 * hsNorm B ^ 2 =
      hsNorm (X * Xᴴ - Y * Yᴴ) ^ 2 := by
  simp only [hsNorm_sq]
  exact block_hs_sum_gap_of_gram X Y hA hB hC

/-- The product gap is measured by a weighted squared Hilbert–Schmidt
distance in any common Gram factorization. -/
theorem block_hs_product_deficit_of_gram
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (hA : A = Xᴴ * X) (hB : B = Xᴴ * Y) (hC : C = Yᴴ * Y) :
    hsSq (hsNorm C • (X * Xᴴ) - hsNorm A • (Y * Yᴴ)) =
      2 * hsNorm A * hsNorm C * (hsNorm A * hsNorm C - hsSq B) := by
  rw [hA, hB, hC]
  exact gram_product_deficit X Y

/-- Sum equality can be checked in every common Gram factorization, whatever
its finite row type. -/
theorem block_hs_sum_eq_iff_of_gram
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (hA : A = Xᴴ * X) (hB : B = Xᴴ * Y) (hC : C = Yᴴ * Y) :
    (2 * hsSq B = hsSq A + hsSq C) ↔ X * Xᴴ = Y * Yᴴ := by
  rw [hA, hB, hC]
  exact gram_sum_eq_iff X Y

/-- Product equality can be checked in every common Gram factorization.
The weighted criterion includes all zero cases. -/
theorem block_hs_product_eq_iff_of_gram
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (hA : A = Xᴴ * X) (hB : B = Xᴴ * Y) (hC : C = Yᴴ * Y) :
    (hsSq B = hsNorm A * hsNorm C) ↔
      hsNorm C • (X * Xᴴ) = hsNorm A • (Y * Yᴴ) := by
  rw [hA, hB, hC]
  exact gram_product_eq_iff X Y

/-- Product equality in Hilbert–Schmidt norm notation, with a criterion valid
for every common Gram factorization and all zero cases. -/
theorem block_hsNorm_product_eq_iff_of_gram
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (hA : A = Xᴴ * X) (hB : B = Xᴴ * Y) (hC : C = Yᴴ * Y) :
    (hsNorm B ^ 2 = hsNorm A * hsNorm C) ↔
      hsNorm C • (X * Xᴴ) = hsNorm A • (Y * Yᴴ) := by
  rw [hsNorm_sq]
  exact block_hs_product_eq_iff_of_gram X Y hA hB hC

/-- Sum equality in Hilbert–Schmidt norm notation, with a criterion valid for
every common Gram factorization. -/
theorem block_hsNorm_sum_eq_iff_of_gram
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (hA : A = Xᴴ * X) (hB : B = Xᴴ * Y) (hC : C = Yᴴ * Y) :
    (2 * hsNorm B ^ 2 = hsNorm A ^ 2 + hsNorm C ^ 2) ↔ X * Xᴴ = Y * Yᴴ := by
  simp only [hsNorm_sq]
  exact block_hs_sum_eq_iff_of_gram X Y hA hB hC

/-- When both diagonal norms are positive, product equality is equality of
the normalized row Gram matrices in any common Gram factorization. -/
theorem block_hs_product_eq_iff_normalized_of_gram
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (hA : A = Xᴴ * X) (hB : B = Xᴴ * Y) (hC : C = Yᴴ * Y)
    (ha : 0 < hsNorm A) (hc : 0 < hsNorm C) :
    (hsSq B = hsNorm A * hsNorm C) ↔
      (1 / hsNorm A) • (X * Xᴴ) = (1 / hsNorm C) • (Y * Yᴴ) := by
  rw [hA, hB, hC]
  rw [hA] at ha
  rw [hC] at hc
  exact gram_product_eq_iff_normalized X Y ha hc

/-- A positive block matrix admits factors that realize its exact sum gap. -/
theorem block_hs_sum_gap_exists
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks A B Bᴴ C).PosSemidef) :
    ∃ (X : Matrix (m ⊕ n) m ℂ) (Y : Matrix (m ⊕ n) n ℂ),
      A = Xᴴ * X ∧ B = Xᴴ * Y ∧ C = Yᴴ * Y ∧
        hsSq A + hsSq C - 2 * hsSq B = hsSq (X * Xᴴ - Y * Yᴴ) := by
  obtain ⟨X, Y, hA, hB, hC⟩ := exists_gram_of_posSemidef_fromBlocks h
  exact ⟨X, Y, hA, hB, hC, block_hs_sum_gap_of_gram X Y hA hB hC⟩

/-- Sum equality is the existence of common Gram factors with equal row
Gram matrices. -/
theorem block_hs_sum_eq_iff_exists_gram
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks A B Bᴴ C).PosSemidef) :
    (2 * hsSq B = hsSq A + hsSq C) ↔
      ∃ (X : Matrix (m ⊕ n) m ℂ) (Y : Matrix (m ⊕ n) n ℂ),
        A = Xᴴ * X ∧ B = Xᴴ * Y ∧ C = Yᴴ * Y ∧ X * Xᴴ = Y * Yᴴ := by
  constructor
  · intro hEq
    obtain ⟨X, Y, hA, hB, hC⟩ := exists_gram_of_posSemidef_fromBlocks h
    exact ⟨X, Y, hA, hB, hC, (block_hs_sum_eq_iff_of_gram X Y hA hB hC).mp hEq⟩
  · rintro ⟨X, Y, hA, hB, hC, hEq⟩
    exact (block_hs_sum_eq_iff_of_gram X Y hA hB hC).mpr hEq

/-- Product equality is the existence of common Gram factors whose row Gram
matrices satisfy the weighted proportionality criterion. -/
theorem block_hs_product_eq_iff_exists_gram
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks A B Bᴴ C).PosSemidef) :
    (hsSq B = hsNorm A * hsNorm C) ↔
      ∃ (X : Matrix (m ⊕ n) m ℂ) (Y : Matrix (m ⊕ n) n ℂ),
        A = Xᴴ * X ∧ B = Xᴴ * Y ∧ C = Yᴴ * Y ∧
          hsNorm C • (X * Xᴴ) = hsNorm A • (Y * Yᴴ) := by
  constructor
  · intro hEq
    obtain ⟨X, Y, hA, hB, hC⟩ := exists_gram_of_posSemidef_fromBlocks h
    exact ⟨X, Y, hA, hB, hC, (block_hs_product_eq_iff_of_gram X Y hA hB hC).mp hEq⟩
  · rintro ⟨X, Y, hA, hB, hC, hEq⟩
    exact (block_hs_product_eq_iff_of_gram X Y hA hB hC).mpr hEq

/-- Product equality in norm notation is the existence of a Gram
factorization satisfying weighted proportionality. -/
theorem block_hsNorm_product_eq_iff_exists_gram
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks A B Bᴴ C).PosSemidef) :
    (hsNorm B ^ 2 = hsNorm A * hsNorm C) ↔
      ∃ (X : Matrix (m ⊕ n) m ℂ) (Y : Matrix (m ⊕ n) n ℂ),
        A = Xᴴ * X ∧ B = Xᴴ * Y ∧ C = Yᴴ * Y ∧
          hsNorm C • (X * Xᴴ) = hsNorm A • (Y * Yᴴ) := by
  rw [hsNorm_sq]
  exact block_hs_product_eq_iff_exists_gram h

/-- Sum equality in norm notation is the existence of a Gram factorization
with equal row Gram matrices. -/
theorem block_hsNorm_sum_eq_iff_exists_gram
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (fromBlocks A B Bᴴ C).PosSemidef) :
    (2 * hsNorm B ^ 2 = hsNorm A ^ 2 + hsNorm C ^ 2) ↔
      ∃ (X : Matrix (m ⊕ n) m ℂ) (Y : Matrix (m ⊕ n) n ℂ),
        A = Xᴴ * X ∧ B = Xᴴ * Y ∧ C = Yᴴ * Y ∧ X * Xᴴ = Y * Yᴴ := by
  simp only [hsNorm_sq]
  exact block_hs_sum_eq_iff_exists_gram h

omit [Fintype m] [Fintype n] in
/-- The block matrix of simultaneous compressions of a Hermitian matrix is
itself a single compression. -/
theorem fromBlocks_compression (S : Matrix r r ℂ) (hS : S.IsHermitian)
    (U : Matrix r m ℂ) (V : Matrix r n ℂ) :
    fromBlocks (Uᴴ * S * U) (Uᴴ * S * V) (Uᴴ * S * V)ᴴ (Vᴴ * S * V) =
      (fromCols U V)ᴴ * S * fromCols U V := by
  have hB : (Uᴴ * S * V)ᴴ = Vᴴ * S * U := by
    simp only [conjTranspose_mul, conjTranspose_conjTranspose, hS.eq, Matrix.mul_assoc]
  rw [hB, conjTranspose_fromCols_eq_fromRows_conjTranspose,
    fromRows_mul, fromRows_mul_fromCols]

/-- Simultaneous rectangular compressions of a positive semidefinite matrix
form a positive semidefinite block matrix. -/
theorem posSemidef_fromBlocks_compression {S : Matrix r r ℂ} (hS : S.PosSemidef)
    (U : Matrix r m ℂ) (V : Matrix r n ℂ) :
    (fromBlocks (Uᴴ * S * U) (Uᴴ * S * V) (Uᴴ * S * V)ᴴ
      (Vᴴ * S * V)).PosSemidef := by
  rw [fromBlocks_compression S hS.isHermitian U V]
  exact hS.conjTranspose_mul_mul_same (fromCols U V)

omit [Fintype m] [Fintype n] in
/-- Compressions of a positive semidefinite matrix have common Gram factors
with the same row index type as that matrix. -/
theorem exists_compression_gram {S : Matrix r r ℂ} (hS : S.PosSemidef)
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

/-- The product estimate for arbitrary rectangular compressions of a positive
semidefinite matrix. -/
theorem compression_hs_product_le {S : Matrix r r ℂ} (hS : S.PosSemidef)
    (U : Matrix r m ℂ) (V : Matrix r n ℂ) :
    hsSq (Uᴴ * S * V) ≤ hsNorm (Uᴴ * S * U) * hsNorm (Vᴴ * S * V) :=
  block_hs_product_le (posSemidef_fromBlocks_compression hS U V)

/-- The compression product estimate in Hilbert–Schmidt norm notation. -/
theorem compression_hsNorm_product_le {S : Matrix r r ℂ} (hS : S.PosSemidef)
    (U : Matrix r m ℂ) (V : Matrix r n ℂ) :
    hsNorm (Uᴴ * S * V) ^ 2 ≤ hsNorm (Uᴴ * S * U) * hsNorm (Vᴴ * S * V) :=
  block_hsNorm_product_le (posSemidef_fromBlocks_compression hS U V)

/-- The sum estimate for arbitrary rectangular compressions of a positive
semidefinite matrix. -/
theorem compression_hs_sum_le {S : Matrix r r ℂ} (hS : S.PosSemidef)
    (U : Matrix r m ℂ) (V : Matrix r n ℂ) :
    2 * hsSq (Uᴴ * S * V) ≤ hsSq (Uᴴ * S * U) + hsSq (Vᴴ * S * V) :=
  block_hs_sum_le (posSemidef_fromBlocks_compression hS U V)

/-- The compression sum estimate in Hilbert–Schmidt norm notation. -/
theorem compression_hsNorm_sum_le {S : Matrix r r ℂ} (hS : S.PosSemidef)
    (U : Matrix r m ℂ) (V : Matrix r n ℂ) :
    2 * hsNorm (Uᴴ * S * V) ^ 2 ≤
      hsNorm (Uᴴ * S * U) ^ 2 + hsNorm (Vᴴ * S * V) ^ 2 :=
  block_hsNorm_sum_le (posSemidef_fromBlocks_compression hS U V)

end PositiveBlocks
