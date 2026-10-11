import PositiveBlocks.Blocks

/-!
# Sharp equality witnesses in every nonempty block dimension
-/

open scoped Matrix ComplexOrder

namespace PositiveBlocks

variable {m n : Type*} [Fintype m] [Fintype n] [DecidableEq m] [DecidableEq n]

/-- The squared HS norm of a matrix with one nonzero entry. -/
theorem hsSq_single (i : m) (j : n) (z : ℂ) :
    hsSq (Matrix.single i j z) = Complex.normSq z := by
  simp only [hsSq_eq_sum, Matrix.single, Matrix.of_apply, apply_ite,
    Complex.normSq_zero]
  simp [ite_and]

/-- Zero padding of the scalar equality example is positive in arbitrary
nonempty block dimensions. The selected entries supply the nonempty witnesses. -/
theorem single_sharp_block_posSemidef (i : m) (j : n) :
    (Matrix.fromBlocks (Matrix.single i i (1 : ℂ)) (Matrix.single i j (1 : ℂ))
      (Matrix.single i j (1 : ℂ))ᴴ (Matrix.single j j (1 : ℂ))).PosSemidef := by
  simpa only [Matrix.conjTranspose_single, star_one, Matrix.single_mul_single_same,
    one_mul] using
    posSemidef_fromBlocks_gram
      (Matrix.single (0 : Fin 1) i (1 : ℂ)) (Matrix.single (0 : Fin 1) j (1 : ℂ))

/-- Every nonempty pair of block dimensions has a PSD equality witness with
all three squared HS norms equal to one. -/
theorem exists_sharp_block [Nonempty m] [Nonempty n] :
    ∃ (A : Matrix m m ℂ) (B : Matrix m n ℂ) (C : Matrix n n ℂ),
      (Matrix.fromBlocks A B Bᴴ C).PosSemidef ∧
      hsSq A = 1 ∧ hsSq B = 1 ∧ hsSq C = 1 := by
  classical
  let i : m := Classical.choice inferInstance
  let j : n := Classical.choice inferInstance
  refine ⟨Matrix.single i i 1, Matrix.single i j 1, Matrix.single j j 1,
    single_sharp_block_posSemidef i j, ?_, ?_, ?_⟩
  all_goals norm_num [hsSq_single]

end PositiveBlocks
