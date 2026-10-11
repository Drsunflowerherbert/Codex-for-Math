import PositiveBlocks.Blocks

/-!
# Intrinsic identities in product equality cases

Proportional row Gram matrices give identities in the original three Gram
blocks. These polynomial identities do not need inverses of the block matrices.
-/

open scoped Matrix ComplexConjugate ComplexOrder

namespace PositiveBlocks

variable {r m n : Type*} [Fintype r] [Fintype m] [Fintype n]

/-- Proportional row Gram matrices determine the left off-diagonal square. -/
theorem gram_proportional_mul_conjTranspose
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ) (t : ℝ)
    (hQ : Y * Yᴴ = t • (X * Xᴴ)) :
    (Xᴴ * Y) * (Xᴴ * Y)ᴴ = t • ((Xᴴ * X) * (Xᴴ * X)) := by
  rw [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
  calc
    (Xᴴ * Y) * (Yᴴ * X) = Xᴴ * (Y * Yᴴ) * X := by
      simp only [Matrix.mul_assoc]
    _ = Xᴴ * (t • (X * Xᴴ)) * X := by rw [hQ]
    _ = t • ((Xᴴ * X) * (Xᴴ * X)) := by
      simp only [Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_assoc]

/-- Proportional row Gram matrices determine the right diagonal square. -/
theorem gram_proportional_conjTranspose_mul
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ) (t : ℝ)
    (hQ : Y * Yᴴ = t • (X * Xᴴ)) :
    (Yᴴ * Y) * (Yᴴ * Y) = t • ((Xᴴ * Y)ᴴ * (Xᴴ * Y)) := by
  rw [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
  calc
    (Yᴴ * Y) * (Yᴴ * Y) = Yᴴ * (Y * Yᴴ) * Y := by
      simp only [Matrix.mul_assoc]
    _ = Yᴴ * (t • (X * Xᴴ)) * Y := by rw [hQ]
    _ = t • ((Yᴴ * X) * (Xᴴ * Y)) := by
      simp only [Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_assoc]

/-- Product equality makes the off-diagonal block intertwine the diagonal blocks. -/
theorem gram_proportional_intertwine
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ) (t : ℝ)
    (hQ : Y * Yᴴ = t • (X * Xᴴ)) :
    (Xᴴ * Y) * (Yᴴ * Y) = t • ((Xᴴ * X) * (Xᴴ * Y)) := by
  calc
    (Xᴴ * Y) * (Yᴴ * Y) = Xᴴ * (Y * Yᴴ) * Y := by
      simp only [Matrix.mul_assoc]
    _ = Xᴴ * (t • (X * Xᴴ)) * Y := by rw [hQ]
    _ = t • ((Xᴴ * X) * (Xᴴ * Y)) := by
      simp only [Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_assoc]

/-- All three intrinsic polynomial identities of proportional Gram blocks. -/
theorem gram_proportional_intrinsic
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ) (t : ℝ)
    (hQ : Y * Yᴴ = t • (X * Xᴴ)) :
    (Xᴴ * Y) * (Xᴴ * Y)ᴴ = t • ((Xᴴ * X) * (Xᴴ * X)) ∧
      (Yᴴ * Y) * (Yᴴ * Y) = t • ((Xᴴ * Y)ᴴ * (Xᴴ * Y)) ∧
      (Xᴴ * Y) * (Yᴴ * Y) = t • ((Xᴴ * X) * (Xᴴ * Y)) :=
  ⟨gram_proportional_mul_conjTranspose X Y t hQ,
    gram_proportional_conjTranspose_mul X Y t hQ,
    gram_proportional_intertwine X Y t hQ⟩

/-- With a positive left diagonal norm, the proportionality constant in a
product equality case is the ratio of the diagonal norms. -/
theorem gram_product_eq_proportional
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (ha : 0 < hsNorm (Xᴴ * X))
    (he : hsSq (Xᴴ * Y) = hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y)) :
    Y * Yᴴ = (hsNorm (Yᴴ * Y) / hsNorm (Xᴴ * X)) • (X * Xᴴ) := by
  have ha0 : hsNorm (Xᴴ * X) ≠ 0 := ne_of_gt ha
  have h := (gram_product_eq_iff X Y).mp he
  have hh := congrArg (fun Z : Matrix r r ℂ => (hsNorm (Xᴴ * X))⁻¹ • Z) h.symm
  simpa [smul_smul, div_eq_mul_inv, mul_comm, ha0] using hh

/-- Product equality implies the three intrinsic identities with the norm ratio. -/
theorem gram_product_eq_intrinsic
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (ha : 0 < hsNorm (Xᴴ * X))
    (he : hsSq (Xᴴ * Y) = hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y)) :
    (Xᴴ * Y) * (Xᴴ * Y)ᴴ =
        (hsNorm (Yᴴ * Y) / hsNorm (Xᴴ * X)) • ((Xᴴ * X) * (Xᴴ * X)) ∧
      (Yᴴ * Y) * (Yᴴ * Y) =
        (hsNorm (Yᴴ * Y) / hsNorm (Xᴴ * X)) • ((Xᴴ * Y)ᴴ * (Xᴴ * Y)) ∧
      (Xᴴ * Y) * (Yᴴ * Y) =
        (hsNorm (Yᴴ * Y) / hsNorm (Xᴴ * X)) • ((Xᴴ * X) * (Xᴴ * Y)) :=
  gram_proportional_intrinsic X Y _ (gram_product_eq_proportional X Y ha he)

/-- The normalized squared distance measures the product deficit exactly. -/
theorem gram_product_normalized_deficit
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (ha : 0 < hsNorm (Xᴴ * X)) (hc : 0 < hsNorm (Yᴴ * Y)) :
    hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y) - hsSq (Xᴴ * Y) =
      (hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y) / 2) *
        hsSq ((1 / hsNorm (Xᴴ * X)) • (X * Xᴴ) -
          (1 / hsNorm (Yᴴ * Y)) • (Y * Yᴴ)) := by
  rw [hsSq_weighted_sub, ← hsSq_swap_gram X, ← hsSq_swap_gram Y,
    hsInner_gram, ← hsNorm_sq (Xᴴ * X), ← hsNorm_sq (Yᴴ * Y)]
  field_simp [ne_of_gt ha, ne_of_gt hc]; ring

private theorem trace_mul_conjTranspose_re (M : Matrix m n ℂ) :
    (Matrix.trace (M * Mᴴ)).re = hsSq M := by
  rw [Matrix.trace_mul_comm]
  rfl

private theorem trace_gram_sq_re (X : Matrix r m ℂ) :
    (Matrix.trace ((Xᴴ * X) * (Xᴴ * X))).re = hsSq (Xᴴ * X) := by
  simp only [hsSq, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]

private theorem trace_real_smul_re (t : ℝ) (M : Matrix m m ℂ) :
    (Matrix.trace (t • M)).re = t * (Matrix.trace M).re := by
  rw [Matrix.trace_smul, Complex.smul_re]
  rfl

/-- At the fixed norm ratio, the left square identity alone characterizes
product equality. -/
theorem gram_product_eq_iff_mul_conjTranspose
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (ha : 0 < hsNorm (Xᴴ * X)) :
    (hsSq (Xᴴ * Y) = hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y)) ↔
      (Xᴴ * Y) * (Xᴴ * Y)ᴴ =
        (hsNorm (Yᴴ * Y) / hsNorm (Xᴴ * X)) • ((Xᴴ * X) * (Xᴴ * X)) := by
  constructor
  · intro he
    exact (gram_product_eq_intrinsic X Y ha he).1
  · intro hi
    have h := congrArg (fun M : Matrix m m ℂ => (Matrix.trace M).re) hi
    dsimp only at h
    rw [trace_mul_conjTranspose_re, trace_real_smul_re, trace_gram_sq_re,
      ← hsNorm_sq (Xᴴ * X)] at h
    calc
      hsSq (Xᴴ * Y) =
          (hsNorm (Yᴴ * Y) / hsNorm (Xᴴ * X)) * hsNorm (Xᴴ * X) ^ 2 := h
      _ = hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y) := by
        field_simp [ne_of_gt ha]

/-- The three intrinsic polynomial identities characterize product equality. -/
theorem gram_product_eq_iff_intrinsic
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (ha : 0 < hsNorm (Xᴴ * X)) :
    (hsSq (Xᴴ * Y) = hsNorm (Xᴴ * X) * hsNorm (Yᴴ * Y)) ↔
      ((Xᴴ * Y) * (Xᴴ * Y)ᴴ =
          (hsNorm (Yᴴ * Y) / hsNorm (Xᴴ * X)) • ((Xᴴ * X) * (Xᴴ * X)) ∧
        (Yᴴ * Y) * (Yᴴ * Y) =
          (hsNorm (Yᴴ * Y) / hsNorm (Xᴴ * X)) • ((Xᴴ * Y)ᴴ * (Xᴴ * Y)) ∧
        (Xᴴ * Y) * (Yᴴ * Y) =
          (hsNorm (Yᴴ * Y) / hsNorm (Xᴴ * X)) • ((Xᴴ * X) * (Xᴴ * Y))) := by
  exact ⟨gram_product_eq_intrinsic X Y ha,
    fun hi => (gram_product_eq_iff_mul_conjTranspose X Y ha).mpr hi.1⟩

/-- Sum equality is equivalent to the three unscaled block identities. -/
theorem gram_sum_eq_iff_intrinsic
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ) :
    (2 * hsSq (Xᴴ * Y) = hsSq (Xᴴ * X) + hsSq (Yᴴ * Y)) ↔
      ((Xᴴ * Y) * (Xᴴ * Y)ᴴ = (Xᴴ * X) * (Xᴴ * X) ∧
        (Yᴴ * Y) * (Yᴴ * Y) = (Xᴴ * Y)ᴴ * (Xᴴ * Y) ∧
        (Xᴴ * Y) * (Yᴴ * Y) = (Xᴴ * X) * (Xᴴ * Y)) := by
  constructor
  · intro he
    have hQ : Y * Yᴴ = (1 : ℝ) • (X * Xᴴ) := by
      simpa only [one_smul] using ((gram_sum_eq_iff X Y).mp he).symm
    simpa only [one_smul] using gram_proportional_intrinsic X Y 1 hQ
  · intro hi
    have hA := congrArg (fun M : Matrix m m ℂ => (Matrix.trace M).re) hi.1
    dsimp only at hA
    rw [trace_mul_conjTranspose_re, trace_gram_sq_re] at hA
    have hC := congrArg (fun M : Matrix n n ℂ => (Matrix.trace M).re) hi.2.1
    dsimp only at hC
    rw [trace_gram_sq_re] at hC
    change hsSq (Yᴴ * Y) = hsSq (Xᴴ * Y) at hC
    linarith

/-- For a positive block matrix and the fixed norm ratio, the left square
identity alone is equivalent to product equality. -/
theorem block_hs_product_eq_iff_mul_conjTranspose
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (Matrix.fromBlocks A B Bᴴ C).PosSemidef) (ha : 0 < hsNorm A) :
    (hsSq B = hsNorm A * hsNorm C) ↔
      B * Bᴴ = (hsNorm C / hsNorm A) • (A * A) := by
  obtain ⟨X, Y, rfl, rfl, rfl⟩ := exists_gram_of_posSemidef_fromBlocks h
  exact gram_product_eq_iff_mul_conjTranspose X Y ha

/-- Product equality for a positive block matrix has an intrinsic criterion,
without choosing Gram factors in the statement. -/
theorem block_hs_product_eq_iff_intrinsic
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (Matrix.fromBlocks A B Bᴴ C).PosSemidef) (ha : 0 < hsNorm A) :
    (hsSq B = hsNorm A * hsNorm C) ↔
      (B * Bᴴ = (hsNorm C / hsNorm A) • (A * A) ∧
        C * C = (hsNorm C / hsNorm A) • (Bᴴ * B) ∧
        B * C = (hsNorm C / hsNorm A) • (A * B)) := by
  obtain ⟨X, Y, rfl, rfl, rfl⟩ := exists_gram_of_posSemidef_fromBlocks h
  exact gram_product_eq_iff_intrinsic X Y ha

/-- Sum equality for a positive block matrix has an intrinsic criterion,
including all zero cases. -/
theorem block_hs_sum_eq_iff_intrinsic
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (h : (Matrix.fromBlocks A B Bᴴ C).PosSemidef) :
    (2 * hsSq B = hsSq A + hsSq C) ↔
      (B * Bᴴ = A * A ∧ C * C = Bᴴ * B ∧ B * C = A * B) := by
  obtain ⟨X, Y, rfl, rfl, rfl⟩ := exists_gram_of_posSemidef_fromBlocks h
  exact gram_sum_eq_iff_intrinsic X Y

/-- The exact normalized deficit in any common Gram factorization. -/
theorem block_hs_product_normalized_deficit_of_gram
    {A : Matrix m m ℂ} {B : Matrix m n ℂ} {C : Matrix n n ℂ}
    (X : Matrix r m ℂ) (Y : Matrix r n ℂ)
    (hA : A = Xᴴ * X) (hB : B = Xᴴ * Y) (hC : C = Yᴴ * Y)
    (ha : 0 < hsNorm A) (hc : 0 < hsNorm C) :
    hsNorm A * hsNorm C - hsSq B = (hsNorm A * hsNorm C / 2) *
      hsSq ((1 / hsNorm A) • (X * Xᴴ) - (1 / hsNorm C) • (Y * Yᴴ)) := by
  rw [hA, hB, hC]
  rw [hA] at ha
  rw [hC] at hc
  exact gram_product_normalized_deficit X Y ha hc

end PositiveBlocks
