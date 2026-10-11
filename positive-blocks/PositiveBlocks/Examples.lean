import PositiveBlocks.Basic
import PositiveBlocks.Blocks

/-!
# Exact examples

Small kernel-checked examples complement the independent Gaussian-rational
regression suite. All entries and squared Hilbert–Schmidt norms are exact.
-/

namespace PositiveBlocks.Examples

open Matrix
open scoped ComplexOrder

def scalarOne : Matrix (Fin 1) (Fin 1) ℂ := !![1]

def scalarPhase : Matrix (Fin 1) (Fin 1) ℂ := !![2 * Complex.I]

theorem scalar_sharp_values :
    hsSq scalarOne = 1 ∧ hsNorm scalarOne = 1 := by
  constructor
  · norm_num [hsSq_eq_sum, scalarOne, Fin.sum_univ_succ, Complex.normSq_apply]
  · norm_num [hsNorm, hsSq_eq_sum, scalarOne, Fin.sum_univ_succ, Complex.normSq_apply]

theorem scalar_complex_value : hsSq scalarPhase = 4 := by
  norm_num [hsSq_eq_sum, scalarPhase, Fin.sum_univ_succ, Complex.normSq_apply]

theorem scalarOne_gram : scalarOneᴴ * scalarOne = scalarOne := by
  ext i j
  fin_cases i
  fin_cases j
  norm_num [scalarOne, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_succ]

theorem scalar_sharp_positive :
    (Matrix.fromBlocks scalarOne scalarOne scalarOneᴴ scalarOne).PosSemidef := by
  simpa only [scalarOne_gram] using posSemidef_fromBlocks_gram scalarOne scalarOne

/-- Any universal coefficient in the product bound is at least one. -/
theorem product_coefficient_ge_one (K : ℝ)
    (h : ∀ (A B C : Matrix (Fin 1) (Fin 1) ℂ),
      (Matrix.fromBlocks A B Bᴴ C).PosSemidef →
      hsSq B ≤ K * hsNorm A * hsNorm C) : 1 ≤ K := by
  have hh := h scalarOne scalarOne scalarOne scalar_sharp_positive
  simpa only [scalar_sharp_values.1, scalar_sharp_values.2, mul_one] using hh

/-- Any universal coefficient on the left of the sum bound is at most two. -/
theorem sum_coefficient_le_two (K : ℝ)
    (h : ∀ (A B C : Matrix (Fin 1) (Fin 1) ℂ),
      (Matrix.fromBlocks A B Bᴴ C).PosSemidef →
      K * hsSq B ≤ hsSq A + hsSq C) : K ≤ 2 := by
  have hh := h scalarOne scalarOne scalarOne scalar_sharp_positive
  norm_num only [scalar_sharp_values.1, mul_one] at hh
  exact hh

def rectangularX : Matrix (Fin 2) (Fin 2) ℂ := !![1, 0; 0, 2]

def rectangularY : Matrix (Fin 2) (Fin 3) ℂ :=
  !![1, 0, 0; 0, 2 * Complex.I, 0]

def rectangularA : Matrix (Fin 2) (Fin 2) ℂ := !![1, 0; 0, 4]

def rectangularB : Matrix (Fin 2) (Fin 3) ℂ :=
  !![1, 0, 0; 0, 4 * Complex.I, 0]

def rectangularC : Matrix (Fin 3) (Fin 3) ℂ :=
  !![1, 0, 0; 0, 4, 0; 0, 0, 0]

theorem rectangular_gram :
    rectangularA = rectangularXᴴ * rectangularX ∧
    rectangularB = rectangularXᴴ * rectangularY ∧
    rectangularC = rectangularYᴴ * rectangularY := by
  constructor
  · ext i j
    fin_cases i <;> fin_cases j <;>
      norm_num [rectangularA, rectangularX, Matrix.mul_apply,
        Matrix.conjTranspose_apply, Fin.sum_univ_succ, map_ofNat]
  · constructor
    · ext i j
      fin_cases i <;> fin_cases j <;>
        norm_num [rectangularB, rectangularX, rectangularY, Matrix.mul_apply,
          Matrix.conjTranspose_apply, Fin.sum_univ_succ, map_ofNat]
      ring
    · ext i j
      fin_cases i <;> fin_cases j <;>
        norm_num [rectangularC, rectangularY, Matrix.mul_apply,
          Matrix.conjTranspose_apply, Fin.sum_univ_succ, map_ofNat]
      ring_nf
      norm_num [Complex.I_sq]

theorem rectangular_positive :
    (Matrix.fromBlocks rectangularA rectangularB rectangularBᴴ rectangularC).PosSemidef := by
  rcases rectangular_gram with ⟨hA, hB, hC⟩
  rw [hA, hB, hC]
  exact posSemidef_fromBlocks_gram rectangularX rectangularY

theorem rectangular_squared_norms :
    hsSq rectangularA = 17 ∧ hsSq rectangularB = 17 ∧ hsSq rectangularC = 17 := by
  norm_num [hsSq_eq_sum, rectangularA, rectangularB, rectangularC,
    Fin.sum_univ_succ, Complex.normSq_apply]

theorem rectangular_sum_and_product_equality :
    2 * hsSq rectangularB = hsSq rectangularA + hsSq rectangularC ∧
    hsSq rectangularB = hsNorm rectangularA * hsNorm rectangularC := by
  rcases rectangular_squared_norms with ⟨hA, hB, hC⟩
  constructor
  · norm_num [hA, hB, hC]
  · have hAC : hsNorm rectangularA = hsNorm rectangularC := by
      simp only [hsNorm, hA, hC]
    rw [hB, ← hAC, ← pow_two, hsNorm_sq, hA]

theorem zero_rectangular : hsSq (0 : Matrix (Fin 2) (Fin 3) ℂ) = 0 := hsSq_zero

theorem empty_columns (M : Matrix (Fin 2) (Fin 0) ℂ) : hsNorm M = 0 := by
  apply (hsNorm_eq_zero_iff M).2
  ext i j
  exact Fin.elim0 j

end PositiveBlocks.Examples
