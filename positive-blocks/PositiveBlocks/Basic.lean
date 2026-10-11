import Mathlib

/-!
# Hilbert–Schmidt quantities for finite complex matrices

The quantities in this file are defined using the trace, independently of any
norm instance on `Matrix`. Rectangular matrices and empty index types are allowed.
-/

open scoped Matrix ComplexConjugate

namespace PositiveBlocks

variable {m n r : Type*} [Fintype m] [Fintype n] [Fintype r]

/-- The squared Hilbert–Schmidt norm, defined directly from the trace. -/
noncomputable def hsSq (M : Matrix m n ℂ) : ℝ :=
  (Matrix.trace (Mᴴ * M)).re

/-- The Hilbert–Schmidt norm, with no dependence on the ambient matrix norm. -/
noncomputable def hsNorm (M : Matrix m n ℂ) : ℝ :=
  Real.sqrt (hsSq M)

/-- The real Hilbert–Schmidt inner product. -/
noncomputable def hsInner (P Q : Matrix m n ℂ) : ℝ :=
  (Matrix.trace (Pᴴ * Q)).re

theorem hsSq_eq_sum (M : Matrix m n ℂ) :
    hsSq M = ∑ i, ∑ j, Complex.normSq (M i j) := by
  simp only [hsSq, Matrix.trace, Matrix.diag_apply, Matrix.mul_apply,
    Matrix.conjTranspose_apply, Complex.re_sum, Complex.mul_re, Complex.star_def,
    Complex.conj_re, Complex.conj_im, neg_mul, sub_neg_eq_add, Complex.normSq_apply]
  rw [Finset.sum_comm]

theorem hsSq_nonneg (M : Matrix m n ℂ) : 0 ≤ hsSq M := by
  rw [hsSq_eq_sum]
  exact Finset.sum_nonneg fun i _ => Finset.sum_nonneg fun j _ =>
    Complex.normSq_nonneg (M i j)

@[simp] theorem hsSq_zero : hsSq (0 : Matrix m n ℂ) = 0 := by
  simp [hsSq]

theorem hsSq_eq_zero_iff (M : Matrix m n ℂ) : hsSq M = 0 ↔ M = 0 := by
  rw [hsSq_eq_sum]
  simp only [Finset.sum_eq_zero_iff_of_nonneg (fun i _ =>
    Finset.sum_nonneg fun j _ => Complex.normSq_nonneg (M i j)),
    Finset.mem_univ, forall_true_left]
  simp only [Finset.sum_eq_zero_iff_of_nonneg (fun j _ => Complex.normSq_nonneg _),
    Finset.mem_univ, forall_true_left, Complex.normSq_eq_zero]
  exact ⟨fun h => by ext i j; exact h i j, fun h i j => by simp [h]⟩

theorem hsNorm_nonneg (M : Matrix m n ℂ) : 0 ≤ hsNorm M :=
  Real.sqrt_nonneg _

theorem hsNorm_sq (M : Matrix m n ℂ) : hsNorm M ^ 2 = hsSq M :=
  Real.sq_sqrt (hsSq_nonneg M)

@[simp] theorem hsNorm_zero : hsNorm (0 : Matrix m n ℂ) = 0 := by
  simp [hsNorm]

theorem hsNorm_eq_zero_iff (M : Matrix m n ℂ) : hsNorm M = 0 ↔ M = 0 := by
  rw [hsNorm, Real.sqrt_eq_zero (hsSq_nonneg M), hsSq_eq_zero_iff]

@[simp] theorem hsInner_self (P : Matrix m n ℂ) : hsInner P P = hsSq P := rfl

theorem hsInner_comm (P Q : Matrix m n ℂ) : hsInner P Q = hsInner Q P := by
  have h := congrArg Complex.re (Matrix.trace_conjTranspose (Pᴴ * Q))
  simpa [hsInner] using h.symm

theorem hsInner_sub_left (P Q R : Matrix m n ℂ) :
    hsInner (P - Q) R = hsInner P R - hsInner Q R := by
  simp [hsInner, Matrix.sub_mul]

theorem hsInner_sub_right (P Q R : Matrix m n ℂ) :
    hsInner P (Q - R) = hsInner P Q - hsInner P R := by
  simp [hsInner, Matrix.mul_sub]

theorem hsInner_real_smul_left (s : ℝ) (P Q : Matrix m n ℂ) :
    hsInner (s • P) Q = s * hsInner P Q := by
  simp [hsInner]

theorem hsInner_real_smul_right (s : ℝ) (P Q : Matrix m n ℂ) :
    hsInner P (s • Q) = s * hsInner P Q := by
  rw [hsInner_comm, hsInner_real_smul_left, hsInner_comm Q P]

theorem hsSq_real_smul (s : ℝ) (M : Matrix m n ℂ) :
    hsSq (s • M) = s ^ 2 * hsSq M := by
  rw [← hsInner_self, hsInner_real_smul_left, hsInner_real_smul_right, hsInner_self]
  ring

theorem hsNorm_real_smul (s : ℝ) (M : Matrix m n ℂ) :
    hsNorm (s • M) = |s| * hsNorm M := by
  rw [hsNorm, hsSq_real_smul, Real.sqrt_mul (sq_nonneg s), Real.sqrt_sq_eq_abs, hsNorm]

theorem hsSq_sub (P Q : Matrix m n ℂ) :
    hsSq (P - Q) = hsSq P + hsSq Q - 2 * hsInner P Q := by
  rw [← hsInner_self, hsInner_sub_left, hsInner_sub_right, hsInner_sub_right,
    hsInner_self, hsInner_self, hsInner_comm Q P]
  ring

theorem hsSq_weighted_sub (s t : ℝ) (P Q : Matrix m n ℂ) :
    hsSq (s • P - t • Q) =
      s ^ 2 * hsSq P + t ^ 2 * hsSq Q - 2 * s * t * hsInner P Q := by
  rw [hsSq_sub, hsSq_real_smul, hsSq_real_smul,
    hsInner_real_smul_left, hsInner_real_smul_right]
  ring

theorem hsSq_swap_gram (X : Matrix m n ℂ) :
    hsSq (Xᴴ * X) = hsSq (X * Xᴴ) := by
  unfold hsSq
  simp only [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
  congr 1
  rw [Matrix.mul_assoc, Matrix.trace_mul_comm Xᴴ]
  simp only [Matrix.mul_assoc]

theorem hsInner_gram (X : Matrix r m ℂ) (Y : Matrix r n ℂ) :
    hsInner (X * Xᴴ) (Y * Yᴴ) = hsSq (Xᴴ * Y) := by
  unfold hsInner hsSq
  simp only [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
  congr 1
  calc
    _ = Matrix.trace ((X * Xᴴ * Y) * Yᴴ) := by simp only [Matrix.mul_assoc]
    _ = Matrix.trace (Yᴴ * (X * Xᴴ * Y)) := Matrix.trace_mul_comm _ _
    _ = _ := by simp only [Matrix.mul_assoc]

open scoped Matrix.Norms.Frobenius in
/-- The trace definition agrees with mathlib's explicitly selected Frobenius norm. -/
theorem hsNorm_eq_frobenius (M : Matrix m n ℂ) : hsNorm M = ‖M‖ := by
  rw [Matrix.frobenius_norm_def, ← Real.sqrt_eq_rpow, hsNorm, hsSq_eq_sum]
  simp only [Complex.normSq_eq_norm_sq, Real.rpow_two]

end PositiveBlocks
