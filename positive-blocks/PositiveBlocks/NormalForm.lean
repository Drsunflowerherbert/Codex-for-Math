import PositiveBlocks.Gram

/-!
# Common-support normal forms

Rectangular isometries preserve the Hilbert–Schmidt norm and matrix rank. A
positive common-support form produces a PSD equality case. Conversely, spectral
compression to the nonzero eigenvalues and an inverse square root on that support
construct the form from proportional left Gram matrices.

The nonzero equality classification has support dimension equal to each block's
rank and scale equal to the ratio of the diagonal HS norms. The final equality
classification handles either zero factor separately. No inverse of an ambient
Gram matrix is taken.
-/

open scoped Matrix ComplexConjugate ComplexOrder

namespace PositiveBlocks

variable {m n p k : Type*}
  [Fintype m] [Fintype n] [Fintype p] [Fintype k]

/-- Left multiplication by an isometry preserves the squared HS norm. -/
theorem hsSq_isometry_mul [DecidableEq k]
    (U : Matrix m k ℂ) (hU : Uᴴ * U = 1) (M : Matrix k n ℂ) :
    hsSq (U * M) = hsSq M := by
  unfold hsSq
  rw [Matrix.conjTranspose_mul]
  simp only [Matrix.mul_assoc, ← Matrix.mul_assoc Uᴴ U M, hU, Matrix.one_mul]

/-- Right multiplication by an isometry's adjoint preserves the squared HS norm. -/
theorem hsSq_mul_isometry_conjTranspose [DecidableEq k]
    (V : Matrix n k ℂ) (hV : Vᴴ * V = 1) (M : Matrix m k ℂ) :
    hsSq (M * Vᴴ) = hsSq M := by
  unfold hsSq
  rw [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
  rw [Matrix.trace_mul_cycle]
  simp only [Matrix.mul_assoc, hV, Matrix.one_mul]
  rw [Matrix.trace_mul_comm]

/-- Rectangular isometries on both sides preserve the squared HS norm. -/
theorem hsSq_isometry_mul_mul_conjTranspose [DecidableEq k] [DecidableEq p]
    (U : Matrix m k ℂ) (V : Matrix n p ℂ)
    (hU : Uᴴ * U = 1) (hV : Vᴴ * V = 1) (M : Matrix k p ℂ) :
    hsSq (U * M * Vᴴ) = hsSq M := by
  rw [hsSq_mul_isometry_conjTranspose V hV, hsSq_isometry_mul U hU]

theorem hsNorm_isometry_mul [DecidableEq k]
    (U : Matrix m k ℂ) (hU : Uᴴ * U = 1) (M : Matrix k n ℂ) :
    hsNorm (U * M) = hsNorm M := by
  simp only [hsNorm, hsSq_isometry_mul U hU]

theorem hsNorm_mul_isometry_conjTranspose [DecidableEq k]
    (V : Matrix n k ℂ) (hV : Vᴴ * V = 1) (M : Matrix m k ℂ) :
    hsNorm (M * Vᴴ) = hsNorm M := by
  simp only [hsNorm, hsSq_mul_isometry_conjTranspose V hV]

/-- The Hilbert–Schmidt norm is invariant under rectangular isometries. -/
theorem hsNorm_isometry_mul_mul_conjTranspose [DecidableEq k] [DecidableEq p]
    (U : Matrix m k ℂ) (V : Matrix n p ℂ)
    (hU : Uᴴ * U = 1) (hV : Vᴴ * V = 1) (M : Matrix k p ℂ) :
    hsNorm (U * M * Vᴴ) = hsNorm M := by
  simp only [hsNorm, hsSq_isometry_mul_mul_conjTranspose U V hU hV]

/-- A common-support normal form produces a positive semidefinite block matrix.
The isometry assumptions are only needed for the norm equality, not positivity. -/
theorem normalForm_posSemidef
    (U : Matrix m k ℂ) (V : Matrix n k ℂ) (H : Matrix k k ℂ)
    (hH : H.PosSemidef) (t : ℝ) (ht : 0 ≤ t) :
    (Matrix.fromBlocks (U * H * Uᴴ) (Real.sqrt t • (U * H * Vᴴ))
      (Real.sqrt t • (V * H * Uᴴ)) (t • (V * H * Vᴴ))).PosSemidef := by
  have h := hH.mul_mul_conjTranspose_same (Matrix.fromRows U (Real.sqrt t • V))
  rw [Matrix.conjTranspose_fromRows_eq_fromCols_conjTranspose,
    Matrix.fromRows_mul, Matrix.fromRows_mul_fromCols] at h
  simpa only [Matrix.conjTranspose_smul, star_trivial,
    Matrix.smul_mul, Matrix.mul_smul,
    smul_smul, Real.mul_self_sqrt ht] using h

/-- The common-support normal form attains equality in the HS product bound.
This identity does not require positivity of the common matrix. -/
theorem normalForm_hsNorm_eq [DecidableEq k]
    (U : Matrix m k ℂ) (V : Matrix n k ℂ) (H : Matrix k k ℂ)
    (hU : Uᴴ * U = 1) (hV : Vᴴ * V = 1) (t : ℝ) (ht : 0 ≤ t) :
    hsNorm (Real.sqrt t • (U * H * Vᴴ)) ^ 2 =
      hsNorm (U * H * Uᴴ) * hsNorm (t • (V * H * Vᴴ)) := by
  simp only [hsNorm_real_smul, abs_of_nonneg (Real.sqrt_nonneg t), abs_of_nonneg ht,
    hsNorm_isometry_mul_mul_conjTranspose U V hU hV,
    hsNorm_isometry_mul_mul_conjTranspose U U hU hU,
    hsNorm_isometry_mul_mul_conjTranspose V V hV hV, mul_pow, Real.sq_sqrt ht]
  ring

/-- A rectangular isometry has rank equal to its source dimension. -/
theorem isometry_rank [DecidableEq k] (U : Matrix m k ℂ) (hU : Uᴴ * U = 1) :
    U.rank = Fintype.card k := by
  rw [← Matrix.rank_conjTranspose_mul_self U, hU, Matrix.rank_one]

/-- An isometry's source dimension cannot exceed its target dimension. -/
theorem isometry_card_le [DecidableEq k] (U : Matrix m k ℂ) (hU : Uᴴ * U = 1) :
    Fintype.card k ≤ Fintype.card m := by
  rw [← isometry_rank U hU]
  exact U.rank_le_card_height

/-- Rectangular isometries on both sides preserve matrix rank. -/
theorem rank_isometry_mul_mul_conjTranspose [DecidableEq k] [DecidableEq p]
    (U : Matrix m k ℂ) (V : Matrix n p ℂ)
    (hU : Uᴴ * U = 1) (hV : Vᴴ * V = 1) (M : Matrix k p ℂ) :
    (U * M * Vᴴ).rank = M.rank := by
  apply Nat.le_antisymm
  · exact (Matrix.rank_mul_le_left _ _).trans (Matrix.rank_mul_le_right _ _)
  · have hrec : Uᴴ * (U * M * Vᴴ) * V = M := by
      calc
        Uᴴ * (U * M * Vᴴ) * V = (Uᴴ * U) * M * (Vᴴ * V) := by
          simp only [Matrix.mul_assoc]
        _ = M := by rw [hU, hV, Matrix.one_mul, Matrix.mul_one]
    calc
      M.rank = (Uᴴ * (U * M * Vᴴ) * V).rank := congrArg Matrix.rank hrec.symm
      _ ≤ (U * M * Vᴴ).rank :=
        (Matrix.rank_mul_le_left _ _).trans (Matrix.rank_mul_le_right _ _)

/-- A matrix with a left inverse preserves rank under congruence. -/
theorem rank_congruence_of_leftInverse [DecidableEq k]
    (T : Matrix m k ℂ) (L : Matrix k m ℂ) (hLT : L * T = 1)
    (H : Matrix k k ℂ) : (T * H * Tᴴ).rank = H.rank := by
  apply Nat.le_antisymm
  · exact (Matrix.rank_mul_le_left _ _).trans (Matrix.rank_mul_le_right _ _)
  · have hrec : L * (T * H * Tᴴ) * Lᴴ = H := by
      calc
        L * (T * H * Tᴴ) * Lᴴ = (L * T) * H * (L * T)ᴴ := by
          simp only [Matrix.conjTranspose_mul, Matrix.mul_assoc]
        _ = H := by rw [hLT, Matrix.conjTranspose_one, Matrix.one_mul, Matrix.mul_one]
    calc
      H.rank = (L * (T * H * Tᴴ) * Lᴴ).rank := congrArg Matrix.rank hrec.symm
      _ ≤ (T * H * Tᴴ).rank :=
        (Matrix.rank_mul_le_left _ _).trans (Matrix.rank_mul_le_right _ _)

/-- The full block matrix of a common-support form also has support rank. -/
theorem normalForm_block_rank [DecidableEq k]
    (U : Matrix m k ℂ) (V : Matrix n k ℂ) (H : Matrix k k ℂ)
    (hU : Uᴴ * U = 1) (hH : H.PosDef) (t : ℝ) (ht : 0 ≤ t) :
    (Matrix.fromBlocks (U * H * Uᴴ) (Real.sqrt t • (U * H * Vᴴ))
      (Real.sqrt t • (V * H * Uᴴ)) (t • (V * H * Vᴴ))).rank = Fintype.card k := by
  let T := Matrix.fromRows U (Real.sqrt t • V)
  let L := Matrix.fromCols Uᴴ (0 : Matrix k n ℂ)
  have hLT : L * T = 1 := by
    dsimp [L, T]
    rw [Matrix.fromCols_mul_fromRows, Matrix.zero_mul, add_zero, hU]
  have hform : T * H * Tᴴ =
      Matrix.fromBlocks (U * H * Uᴴ) (Real.sqrt t • (U * H * Vᴴ))
        (Real.sqrt t • (V * H * Uᴴ)) (t • (V * H * Vᴴ)) := by
    dsimp [T]
    rw [Matrix.conjTranspose_fromRows_eq_fromCols_conjTranspose,
      Matrix.fromRows_mul, Matrix.fromRows_mul_fromCols]
    simp only [Matrix.conjTranspose_smul, star_trivial, Matrix.smul_mul,
      Matrix.mul_smul, smul_smul, Real.mul_self_sqrt ht]
  rw [← hform, rank_congruence_of_leftInverse T L hLT H]
  exact Matrix.rank_of_isUnit _ hH.isUnit

/-- Each block in a positive common-support form has exactly the support rank. -/
theorem normalForm_ranks [DecidableEq k]
    (U : Matrix m k ℂ) (V : Matrix n k ℂ) (H : Matrix k k ℂ)
    (hU : Uᴴ * U = 1) (hV : Vᴴ * V = 1) (hH : H.PosDef)
    (t : ℝ) (ht : 0 < t) :
    (U * H * Uᴴ).rank = Fintype.card k ∧
      (Real.sqrt t • (U * H * Vᴴ)).rank = Fintype.card k ∧
      (t • (V * H * Vᴴ)).rank = Fintype.card k := by
  have hr (s : ℝ) (hs : 0 < s) (U' : Matrix m k ℂ) (V' : Matrix n k ℂ)
      (hU' : U'ᴴ * U' = 1) (hV' : V'ᴴ * V' = 1) :
      (s • (U' * H * V'ᴴ)).rank = Fintype.card k := by
    have heq : s • (U' * H * V'ᴴ) = U' * (s • H) * V'ᴴ := by
      simp only [Matrix.mul_smul, Matrix.smul_mul]
    rw [heq, rank_isometry_mul_mul_conjTranspose U' V' hU' hV']
    exact Matrix.rank_of_isUnit _ (hH.smul hs).isUnit
  refine ⟨?_, hr (Real.sqrt t) (Real.sqrt_pos.mpr ht) U V hU hV, ?_⟩
  · rw [rank_isometry_mul_mul_conjTranspose U U hU hU]
    exact Matrix.rank_of_isUnit _ hH.isUnit
  · have heq : t • (V * H * Vᴴ) = V * (t • H) * Vᴴ := by
      simp only [Matrix.mul_smul, Matrix.smul_mul]
    rw [heq, rank_isometry_mul_mul_conjTranspose V V hV hV]
    exact Matrix.rank_of_isUnit _ (hH.smul ht).isUnit

/-- Existence of a nonzero common-support representation.

The explicit condition `0 < k` excludes the simultaneous-zero case. Separate
zero branches are necessary for a complete equality classification. -/
def HasCommonSupportNormalForm
    (A : Matrix m m ℂ) (B : Matrix m n ℂ) (C : Matrix n n ℂ) : Prop :=
  ∃ (k : ℕ) (_ : 0 < k) (U : Matrix m (Fin k) ℂ) (V : Matrix n (Fin k) ℂ)
    (H : Matrix (Fin k) (Fin k) ℂ) (t : ℝ),
    H.PosDef ∧ 0 < t ∧ Uᴴ * U = 1 ∧ Vᴴ * V = 1 ∧
    A = U * H * Uᴴ ∧ B = Real.sqrt t • (U * H * Vᴴ) ∧
    C = t • (V * H * Vᴴ)

/-- Every positive common-support normal form is a PSD equality case. -/
theorem HasCommonSupportNormalForm.posSemidef_and_hsNorm_eq
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : HasCommonSupportNormalForm A B C) :
    (Matrix.fromBlocks A B Bᴴ C).PosSemidef ∧
      hsNorm B ^ 2 = hsNorm A * hsNorm C := by
  obtain ⟨k, hk, U, V, H, t, hH, ht, hU, hV, rfl, rfl, rfl⟩ := h
  constructor
  · simpa only [Matrix.conjTranspose_smul, star_trivial, Matrix.conjTranspose_mul,
      Matrix.conjTranspose_conjTranspose, hH.isHermitian.eq, Matrix.mul_assoc] using
      normalForm_posSemidef U V H hH.posSemidef t ht.le
  · exact normalForm_hsNorm_eq U V H hU hV t ht.le

/-- In a nonzero normal form, all three block ranks coincide and are positive. -/
theorem HasCommonSupportNormalForm.rank_eq
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : HasCommonSupportNormalForm A B C) :
    A.rank = B.rank ∧ A.rank = C.rank ∧ 0 < A.rank ∧
      A.rank ≤ Fintype.card m ∧ A.rank ≤ Fintype.card n := by
  obtain ⟨k, hk, U, V, H, t, hH, ht, hU, hV, rfl, rfl, rfl⟩ := h
  obtain ⟨hA, hB, hC⟩ := normalForm_ranks U V H hU hV hH t ht
  rw [hA, hB, hC, Fintype.card_fin]
  exact ⟨rfl, rfl, hk, by simpa using isometry_card_le U hU,
    by simpa using isometry_card_le V hV⟩

/-- The common support can be indexed by the rank of the first block. -/
theorem HasCommonSupportNormalForm.exists_rank_witness
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : HasCommonSupportNormalForm A B C) :
    ∃ (U : Matrix m (Fin A.rank) ℂ) (V : Matrix n (Fin A.rank) ℂ)
      (H : Matrix (Fin A.rank) (Fin A.rank) ℂ) (t : ℝ),
      H.PosDef ∧ 0 < t ∧ Uᴴ * U = 1 ∧ Vᴴ * V = 1 ∧
      A = U * H * Uᴴ ∧ B = Real.sqrt t • (U * H * Vᴴ) ∧
      C = t • (V * H * Vᴴ) := by
  obtain ⟨k, hk, U, V, H, t, hH, ht, hU, hV, hA, hB, hC⟩ := h
  have hr : A.rank = k := by
    rw [hA]
    simpa only [Fintype.card_fin] using (normalForm_ranks U V H hU hV hH t ht).1
  subst k
  exact ⟨U, V, H, t, hH, ht, hU, hV, hA, hB, hC⟩

/-- All three blocks of a positive-dimensional common-support form are nonzero. -/
theorem HasCommonSupportNormalForm.ne_zero
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : HasCommonSupportNormalForm A B C) : A ≠ 0 ∧ B ≠ 0 ∧ C ≠ 0 := by
  obtain ⟨hAB, hAC, hA, _, _⟩ := h.rank_eq
  refine ⟨?_, ?_, ?_⟩
  · intro hz
    simp only [hz, Matrix.rank_zero, lt_self_iff_false] at hA
  · intro hz
    simp only [hAB, hz, Matrix.rank_zero, lt_self_iff_false] at hA
  · intro hz
    simp only [hAC, hz, Matrix.rank_zero, lt_self_iff_false] at hA

/-- The full PSD block matrix has the same rank as each block in the normal form. -/
theorem HasCommonSupportNormalForm.block_rank
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : HasCommonSupportNormalForm A B C) :
    (Matrix.fromBlocks A B Bᴴ C).rank = A.rank := by
  obtain ⟨k, hk, U, V, H, t, hH, ht, hU, hV, rfl, rfl, rfl⟩ := h
  rw [(normalForm_ranks U V H hU hV hH t ht).1]
  simpa only [Matrix.conjTranspose_smul, star_trivial, Matrix.conjTranspose_mul,
    Matrix.conjTranspose_conjTranspose, hH.isHermitian.eq, Matrix.mul_assoc] using
    normalForm_block_rank U V H hU hH t ht.le

/-- The scale in a normal form is exactly the ratio of the diagonal HS norms.
This version fixes both the support dimension and the scale canonically. -/
theorem HasCommonSupportNormalForm.exists_normRatio_witness
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : HasCommonSupportNormalForm A B C) :
    ∃ (U : Matrix m (Fin A.rank) ℂ) (V : Matrix n (Fin A.rank) ℂ)
      (H : Matrix (Fin A.rank) (Fin A.rank) ℂ),
      H.PosDef ∧ Uᴴ * U = 1 ∧ Vᴴ * V = 1 ∧ A = U * H * Uᴴ ∧
      B = Real.sqrt (hsNorm C / hsNorm A) • (U * H * Vᴴ) ∧
      C = (hsNorm C / hsNorm A) • (V * H * Vᴴ) := by
  obtain ⟨U, V, H, t, hH, ht, hU, hV, hA, hB, hC⟩ := h.exists_rank_witness
  have ha0 : hsNorm A ≠ 0 := fun hz => h.ne_zero.1 ((hsNorm_eq_zero_iff A).mp hz)
  have hnorm : hsNorm C = t * hsNorm A := by
    rw [hA, hC, hsNorm_real_smul, abs_of_pos ht,
      hsNorm_isometry_mul_mul_conjTranspose U U hU hU,
      hsNorm_isometry_mul_mul_conjTranspose V V hV hV]
  have hratio : hsNorm C / hsNorm A = t := by
    rw [hnorm, mul_div_cancel_right₀ t ha0]
  exact ⟨U, V, H, hH, hU, hV, hA, by simpa only [hratio] using hB,
    by simpa only [hratio] using hC⟩

section Construction

open scoped MatrixOrder

omit [Fintype k] in
/-- Any selection of columns from a unitary matrix is an isometry. -/
theorem unitary_columns_isometry {r : Type*} [Fintype r] [DecidableEq r]
    [DecidableEq k] (E : Matrix.unitaryGroup r ℂ) (f : k → r)
    (hf : Function.Injective f) :
    (E.val.submatrix id f)ᴴ * (E.val.submatrix id f) = 1 := by
  rw [Matrix.conjTranspose_submatrix,
    ← Matrix.submatrix_mul _ _ _ id _ Function.bijective_id]
  rw [← Matrix.star_eq_conjTranspose, unitary.coe_star_mul_self]
  exact Matrix.submatrix_one _ hf

/-- Removing zero diagonal coefficients does not change spectral reconstruction. -/
theorem restrict_diagonal_support {r : Type*} [Fintype r] [DecidableEq r]
    (E : Matrix r r ℂ) (d : r → ℝ)
    (p : r → Prop) [DecidablePred p] (hzero : ∀ i, ¬p i → d i = 0) :
    let W := E.submatrix id (Subtype.val : {i // p i} → r)
    W * Matrix.diagonal (fun i : {i // p i} => (d i.val : ℂ)) * Wᴴ =
      E * Matrix.diagonal (fun i => (d i : ℂ)) * Eᴴ := by
  classical
  dsimp only
  ext i j
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply,
    Matrix.submatrix_apply, id_eq, Matrix.diagonal_apply, mul_ite, mul_zero,
    Finset.sum_ite_eq', Finset.mem_univ, if_true]
  symm
  apply Finset.sum_congr_set {i | p i}
  · intro x hx
    rfl
  · intro x hx
    simp [hzero x hx]

/-- A nonzero PSD matrix has a positive-definite compression to its support. -/
theorem exists_posDef_compression {r : Type*} [Fintype r] [DecidableEq r]
    (P : Matrix r r ℂ) (hP : P.PosSemidef) (hP0 : P ≠ 0) :
    ∃ (k : ℕ) (_ : 0 < k) (W : Matrix r (Fin k) ℂ)
      (H : Matrix (Fin k) (Fin k) ℂ),
      Wᴴ * W = 1 ∧ H.PosDef ∧ P = W * H * Wᴴ := by
  classical
  let d := hP.isHermitian.eigenvalues
  let E := hP.isHermitian.eigenvectorUnitary
  let I := {i : r // d i ≠ 0}
  let W : Matrix r I ℂ := E.val.submatrix id Subtype.val
  let H : Matrix I I ℂ := Matrix.diagonal (fun i => (d i.val : ℂ))
  have hform : P = W * H * Wᴴ := by
    rw [restrict_diagonal_support E.val d (fun i => d i ≠ 0) (by simp)]
    simpa only [Matrix.star_eq_conjTranspose, Function.comp_def] using
      hP.isHermitian.spectral_theorem
  have hcard : 0 < Fintype.card I := by
    apply Nat.pos_of_ne_zero
    intro hz
    haveI : IsEmpty I := Fintype.card_eq_zero_iff.mp hz
    have hW0 : W = 0 := by ext i j; exact isEmptyElim j
    exact hP0 (by simpa [hW0] using hform)
  let e : Fin (Fintype.card I) ≃ I := (Fintype.equivFin I).symm
  let W' := W.submatrix id e
  let H' := H.submatrix e e
  refine ⟨Fintype.card I, hcard, W', H', ?_, ?_, ?_⟩
  · exact unitary_columns_isometry E (Subtype.val ∘ e)
      (Subtype.val_injective.comp e.injective)
  · dsimp [H', H]
    rw [Matrix.submatrix_diagonal_equiv]
    apply Matrix.posDef_diagonal_iff.mpr
    intro i
    have hd : 0 < d (e i).val :=
      lt_of_le_of_ne (hP.eigenvalues_nonneg _) (Ne.symm (e i).property)
    change (0 : ℂ) < (d (e i).val : ℂ)
    exact_mod_cast hd
  · dsimp [W', H']
    rw [Matrix.conjTranspose_submatrix, Matrix.submatrix_mul_equiv,
      Matrix.submatrix_mul_equiv]
    simpa only [Matrix.submatrix_id_id] using hform

/-- A positive-definite matrix has a Hermitian inverse square root. -/
theorem exists_invSqrt [DecidableEq k] (H : Matrix k k ℂ) (hH : H.PosDef) :
    ∃ L : Matrix k k ℂ, L.IsHermitian ∧ L * H * L = 1 := by
  let S := CFC.sqrt H
  have hS : S.PosDef := hH.posDef_sqrt
  have hdet : IsUnit S.det := (Matrix.isUnit_iff_isUnit_det S).mp hS.isUnit
  refine ⟨S⁻¹, hS.inv.isHermitian, ?_⟩
  have hsq : S * S = H := CFC.sqrt_mul_sqrt_self H hH.posSemidef.nonneg
  rw [← hsq, ← Matrix.mul_assoc, Matrix.nonsing_inv_mul S hdet,
    Matrix.one_mul, Matrix.mul_nonsing_inv S hdet]

/-- A projection fixing a left Gram matrix fixes its factor. -/
theorem projection_fixes_factor {r : Type*} [Fintype r] [DecidableEq r]
    (X : Matrix r m ℂ) (E : Matrix r r ℂ)
    (h : E * (X * Xᴴ) = X * Xᴴ) : E * X = X := by
  have hz : (E - 1) * (X * Xᴴ) = 0 := by
    rw [Matrix.sub_mul, h, Matrix.one_mul, sub_self]
  have := (Matrix.mul_self_mul_conjTranspose_eq_zero X (E - 1)).mp hz
  simpa only [Matrix.sub_mul, Matrix.one_mul, sub_eq_zero] using this

/-- Isometric support compression yields a rectangular isometry. -/
theorem gramCompression_isometry {r : Type*} [Fintype r] [DecidableEq k]
    (X : Matrix r m ℂ) (W : Matrix r k ℂ) (H L : Matrix k k ℂ)
    (hW : Wᴴ * W = 1) (hX : X * Xᴴ = W * H * Wᴴ)
    (hL : L.IsHermitian) (hLHL : L * H * L = 1) :
    (Xᴴ * W * L)ᴴ * (Xᴴ * W * L) = 1 := by
  have hc : Wᴴ * (X * Xᴴ) * W = H := by
    rw [hX]
    calc
      Wᴴ * (W * H * Wᴴ) * W = (Wᴴ * W) * H * (Wᴴ * W) := by
        simp only [Matrix.mul_assoc]
      _ = H := by rw [hW, Matrix.one_mul, Matrix.mul_one]
  calc
    (Xᴴ * W * L)ᴴ * (Xᴴ * W * L) = L * (Wᴴ * (X * Xᴴ) * W) * L := by
      simp only [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
        hL.eq, Matrix.mul_assoc]
    _ = 1 := by rw [hc, hLHL]

omit [Fintype m] [Fintype n] in
/-- The support projection recovers all cross Gram products. -/
theorem gramCompression_cross {r : Type*} [Fintype r] [DecidableEq k]
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ) (W : Matrix r k ℂ)
    (H L : Matrix k k ℂ) (hL : L.IsHermitian) (hLHL : L * H * L = 1)
    (hY : (W * Wᴴ) * Y = Y) :
    (Xᴴ * W * L) * H * (Yᴴ * W * L)ᴴ = Xᴴ * Y := by
  classical
  calc
    (Xᴴ * W * L) * H * (Yᴴ * W * L)ᴴ =
        Xᴴ * W * (L * H * L) * Wᴴ * Y := by
      simp only [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
        hL.eq, Matrix.mul_assoc]
    _ = Xᴴ * ((W * Wᴴ) * Y) := by rw [hLHL, Matrix.mul_one]; simp [Matrix.mul_assoc]
    _ = Xᴴ * Y := by rw [hY]

/-- Proportional nonzero left Gram matrices admit a common-support normal form. -/
theorem hasCommonSupportNormalForm_of_gram_proportional
    {r : Type*} [Fintype r] [DecidableEq r]
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ) (hX0 : X ≠ 0)
    (t : ℝ) (ht : 0 < t) (hQ : Y * Yᴴ = t • (X * Xᴴ)) :
    HasCommonSupportNormalForm (Xᴴ * X) (Xᴴ * Y) (Yᴴ * Y) := by
  classical
  have hP0 : X * Xᴴ ≠ 0 := fun h => hX0 (Matrix.self_mul_conjTranspose_eq_zero.mp h)
  obtain ⟨k, hk, W, H, hW, hH, hP⟩ :=
    exists_posDef_compression (X * Xᴴ) (Matrix.posSemidef_self_mul_conjTranspose X) hP0
  obtain ⟨L, hL, hLHL⟩ := exists_invSqrt H hH
  let Z : Matrix r n ℂ := (Real.sqrt t)⁻¹ • Y
  have hs0 : Real.sqrt t ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr ht)
  have hZ : Z * Zᴴ = X * Xᴴ := by
    dsimp [Z]
    simp only [Matrix.conjTranspose_smul, star_trivial, Matrix.smul_mul,
      Matrix.mul_smul, smul_smul, hQ]
    have hc : (Real.sqrt t)⁻¹ * (Real.sqrt t)⁻¹ * t = 1 := by
      rw [← mul_inv_rev, Real.mul_self_sqrt ht.le, inv_mul_cancel₀ (ne_of_gt ht)]
    rw [← mul_assoc, hc, one_smul]
  have hY : Y = Real.sqrt t • Z := by simp [Z, smul_smul, hs0]
  have hEP : (W * Wᴴ) * (X * Xᴴ) = X * Xᴴ := by
    calc
      (W * Wᴴ) * (X * Xᴴ) = W * (Wᴴ * W) * H * Wᴴ := by
        rw [hP]
        simp only [Matrix.mul_assoc]
      _ = X * Xᴴ := by rw [hW, Matrix.mul_one, ← hP]
  have hEX : (W * Wᴴ) * X = X := projection_fixes_factor X (W * Wᴴ) hEP
  have hEZ : (W * Wᴴ) * Z = Z :=
    projection_fixes_factor Z (W * Wᴴ) (by simpa only [hZ] using hEP)
  let U := Xᴴ * W * L
  let V := Zᴴ * W * L
  refine ⟨k, hk, U, V, H, t, hH, ht,
    gramCompression_isometry X W H L hW hP hL hLHL,
    gramCompression_isometry Z W H L hW (hZ.trans hP) hL hLHL, ?_, ?_, ?_⟩
  · exact (gramCompression_cross X X W H L hL hLHL hEX).symm
  · calc
      Xᴴ * Y = Real.sqrt t • (Xᴴ * Z) := by rw [hY, Matrix.mul_smul]
      _ = Real.sqrt t • (U * H * Vᴴ) := by
        rw [gramCompression_cross X Z W H L hL hLHL hEZ]
  · calc
      Yᴴ * Y = t • (Zᴴ * Z) := by
        conv_lhs => rw [hY]
        simp only [Matrix.conjTranspose_smul, star_trivial, Matrix.smul_mul,
          Matrix.mul_smul, smul_smul, Real.mul_self_sqrt ht.le]
      _ = t • (V * H * Vᴴ) := by
        rw [gramCompression_cross Z Z W H L hL hLHL hEZ]

end Construction

/-- For nonzero Gram factors, equality holds exactly in the common-support form. -/
theorem gram_product_eq_iff_commonSupportNormalForm
    {r : Type*} [Fintype r] [DecidableEq r]
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ) (hX0 : X ≠ 0) (hY0 : Y ≠ 0) :
    (hsSq (Xᴴ * Y) = hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y)) ↔
      HasCommonSupportNormalForm (Xᴴ * X) (Xᴴ * Y) (Yᴴ * Y) := by
  constructor
  · intro heq
    have ha : 0 < hsNorm (Xᴴ * X) := lt_of_le_of_ne (hsNorm_nonneg _)
      (Ne.symm (fun h => hX0 ((gram_hsNorm_eq_zero_iff X).mp h)))
    have hc : 0 < hsNorm (Yᴴ * Y) := lt_of_le_of_ne (hsNorm_nonneg _)
      (Ne.symm (fun h => hY0 ((gram_hsNorm_eq_zero_iff Y).mp h)))
    apply hasCommonSupportNormalForm_of_gram_proportional X Y hX0
      (hsNorm (Yᴴ * Y) / hsNorm (Xᴴ * X)) (div_pos hc ha)
    have h := congrArg (fun M : Matrix r r ℂ => (hsNorm (Xᴴ * X))⁻¹ • M)
      ((gram_product_eq_iff X Y).mp heq)
    simpa only [smul_smul, inv_mul_cancel₀ (ne_of_gt ha), one_smul,
      div_eq_mul_inv, mul_comm] using h.symm
  · intro h
    simpa only [hsNorm_sq] using h.posSemidef_and_hsNorm_eq.2

/-- Complete Gram equality classification, including either zero factor. -/
theorem gram_product_eq_iff_zero_or_commonSupportNormalForm
    {r : Type*} [Fintype r] [DecidableEq r]
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ) :
    (hsSq (Xᴴ * Y) = hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y)) ↔
      X = 0 ∨ Y = 0 ∨ HasCommonSupportNormalForm (Xᴴ * X) (Xᴴ * Y) (Yᴴ * Y) := by
  by_cases hX : X = 0
  · simp [hX]
  by_cases hY : Y = 0
  · simp [hY]
  simp only [hX, hY, false_or]
  exact gram_product_eq_iff_commonSupportNormalForm X Y hX hY

/-- Nonzero equality cases have equal factor ranks and a common support fitting
inside the common row space and both column spaces. -/
theorem gram_product_eq_rank_eq
    {r : Type*} [Fintype r] [DecidableEq r]
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ) (hX0 : X ≠ 0) (hY0 : Y ≠ 0)
    (heq : hsSq (Xᴴ * Y) = hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y)) :
    X.rank = Y.rank ∧ 0 < X.rank ∧ X.rank ≤ Fintype.card r ∧
      X.rank ≤ Fintype.card m ∧ X.rank ≤ Fintype.card n := by
  have h := ((gram_product_eq_iff_commonSupportNormalForm X Y hX0 hY0).mp heq).rank_eq
  simp only [Matrix.rank_conjTranspose_mul_self] at h
  exact ⟨h.2.1, h.2.2.1, X.rank_le_card_height, h.2.2.2.1, h.2.2.2.2⟩

end PositiveBlocks
