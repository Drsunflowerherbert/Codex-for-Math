import Mathlib
import MixedMoments.Rational

namespace MixedMoments

noncomputable section

/-- The free rational coordinate space with basis `1`, `G`, `ζ₂`.
Evaluation into the reals need not be injective. -/
abbrev Coordinates := Fin 3 → ℚ

namespace Coordinates

def rational (v : Coordinates) : ℚ := v 0
def catalan (v : Coordinates) : ℚ := v 1
def zetaTwo (v : Coordinates) : ℚ := v 2

def mk (a b c : ℚ) : Coordinates := ![a, b, c]

@[simp] theorem rational_mk (a b c : ℚ) : (mk a b c).rational = a := rfl
@[simp] theorem catalan_mk (a b c : ℚ) : (mk a b c).catalan = b := rfl
@[simp] theorem zetaTwo_mk (a b c : ℚ) : (mk a b c).zetaTwo = c := rfl

noncomputable def eval (G ζ : ℝ) (v : Coordinates) : ℝ :=
  (v.rational : ℝ) + (v.catalan : ℝ) * G + (v.zetaTwo : ℝ) * ζ

@[simp] theorem eval_mk (G ζ : ℝ) (a b c : ℚ) :
    eval G ζ (mk a b c) = (a : ℝ) + (b : ℝ) * G + (c : ℝ) * ζ := rfl

theorem eval_add (G ζ : ℝ) (v w : Coordinates) :
    eval G ζ (v + w) = eval G ζ v + eval G ζ w := by
  simp only [eval, rational, catalan, zetaTwo, Pi.add_apply, Rat.cast_add]
  ring

theorem eval_sub (G ζ : ℝ) (v w : Coordinates) :
    eval G ζ (v - w) = eval G ζ v - eval G ζ w := by
  simp only [eval, rational, catalan, zetaTwo, Pi.sub_apply, Rat.cast_sub]
  ring

theorem eval_smul (G ζ : ℝ) (q : ℚ) (v : Coordinates) :
    eval G ζ (q • v) = (q : ℝ) * eval G ζ v := by
  simp only [eval, rational, catalan, zetaTwo, Pi.smul_apply,
    smul_eq_mul, Rat.cast_mul]
  ring

@[simp] theorem eval_zero (G ζ : ℝ) : eval G ζ 0 = 0 := by
  simp [eval, rational, catalan, zetaTwo]

theorem eval_sum {ι : Type*} (G ζ : ℝ) (s : Finset ι) (f : ι → Coordinates) :
    eval G ζ (∑ i ∈ s, f i) = ∑ i ∈ s, eval G ζ (f i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert i s hi ih => simp [Finset.sum_insert hi, eval_add, ih]

theorem eval_of_zetaTwo_eq_zero (G ζ : ℝ) (v : Coordinates)
    (h : v.zetaTwo = 0) :
    eval G ζ v = (v.rational : ℝ) + (v.catalan : ℝ) * G := by
  simp [eval, h]

end Coordinates

/-- Specified coordinates of the mixed-moment array, before real evaluation. -/
def formalM (i j : ℕ) : Coordinates := Coordinates.mk
  (mRationalPart i j)
  (4 * kernel ((i : ℤ) - (j : ℤ)))
  ((3 / 2 : ℚ) * kernel ((j : ℤ) - (i : ℤ) - 1))

/-- Specified coordinates of the square-kernel array, before real evaluation. -/
def formalZ (i j : ℕ) : Coordinates := Coordinates.mk
  (zRationalPart i j) 0 (if i = j then 1 else 0)

def polynomialM (P : Polynomial ℚ) (j : ℕ) : Coordinates :=
  ∑ i ∈ P.support, P.coeff i • formalM i j

def polynomialZ (D : Polynomial ℚ) (j : ℕ) : Coordinates :=
  ∑ i ∈ D.support, D.coeff i • formalZ i j

def formalEntry (P D : Polynomial ℚ) (j : ℕ) : Coordinates :=
  polynomialM P j - (3 / 2 : ℚ) • polynomialZ D j

/-- Finite convolution giving the specified coefficient of `t P / sqrt(1-t²)`.
The identification with an analytic Taylor coefficient is a separate obligation. -/
def contactCoefficient (P : Polynomial ℚ) (j : ℕ) : ℚ :=
  ∑ i ∈ P.support, P.coeff i * kernel ((j : ℤ) - (i : ℤ) - 1)

def polynomialDefect (P D : Polynomial ℚ) (j : ℕ) : ℚ :=
  contactCoefficient P j - D.coeff j

/-- Algebraic contact means vanishing of the first `L` specified coefficients. -/
def CoefficientContact (P D : Polynomial ℚ) (L : ℕ) : Prop :=
  ∀ j < L, polynomialDefect P D j = 0

theorem polynomialM_zetaTwo (P : Polynomial ℚ) (j : ℕ) :
    (polynomialM P j).zetaTwo = (3 / 2 : ℚ) * contactCoefficient P j := by
  simp only [polynomialM, Coordinates.zetaTwo, Finset.sum_apply,
    Pi.smul_apply, smul_eq_mul, formalM, Coordinates.mk,
    Matrix.cons_val]
  unfold contactCoefficient
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i hi
  ring

theorem polynomialZ_zetaTwo (D : Polynomial ℚ) (j : ℕ) :
    (polynomialZ D j).zetaTwo = D.coeff j := by
  classical
  simp only [polynomialZ, Coordinates.zetaTwo, Finset.sum_apply,
    Pi.smul_apply, smul_eq_mul, formalZ, Coordinates.mk,
    Matrix.cons_val]
  simp only [mul_ite, mul_one, mul_zero, Finset.sum_ite_eq']
  split_ifs with h
  · rfl
  · exact (Polynomial.notMem_support_iff.mp h).symm

/-- The exact defect identity is unconditional and quantified over all rational polynomials. -/
theorem formal_entry_zeta_coordinate (P D : Polynomial ℚ) (j : ℕ) :
    (formalEntry P D j).zetaTwo = (3 / 2 : ℚ) * polynomialDefect P D j := by
  change (polynomialM P j).zetaTwo -
    (3 / 2 : ℚ) * (polynomialZ D j).zetaTwo = _
  rw [polynomialM_zetaTwo, polynomialZ_zetaTwo]
  unfold polynomialDefect
  ring

theorem contact_cancels_zeta_coordinate (P D : Polynomial ℚ) (L j : ℕ)
    (hcontact : CoefficientContact P D L) (hj : j < L) :
    (formalEntry P D j).zetaTwo = 0 := by
  rw [formal_entry_zeta_coordinate, hcontact j hj, mul_zero]

theorem coefficient_contact_cancellation (P D : Polynomial ℚ) (L j : ℕ)
    (G ζ : ℝ) (hcontact : CoefficientContact P D L) (hj : j < L) :
    ∃ a b : ℚ, Coordinates.eval G ζ (formalEntry P D j) =
      (a : ℝ) + (b : ℝ) * G := by
  exact ⟨(formalEntry P D j).rational, (formalEntry P D j).catalan,
    Coordinates.eval_of_zetaTwo_eq_zero G ζ _
      (contact_cancels_zeta_coordinate P D L j hcontact hj)⟩

/-- The exact contact polynomial of order `L`, defined using a finite sum. -/
def contactTruncation (P : Polynomial ℚ) (L : ℕ) : Polynomial ℚ :=
  ∑ j ∈ Finset.range L, Polynomial.monomial j (contactCoefficient P j)

theorem contactTruncation_coeff (P : Polynomial ℚ) (L j : ℕ) :
    (contactTruncation P L).coeff j =
      if j < L then contactCoefficient P j else 0 := by
  classical
  simp [contactTruncation, Polynomial.finset_sum_coeff, Polynomial.coeff_monomial,
    Finset.sum_ite_eq', Finset.mem_range]

theorem contactTruncation_contact (P : Polynomial ℚ) (L : ℕ) :
    CoefficientContact P (contactTruncation P L) L := by
  intro j hj
  simp [polynomialDefect, contactTruncation_coeff, hj]

/-- Explicit rational witness for the constant coordinate of the contracted entry. -/
def rationalWitness (P D : Polynomial ℚ) (j : ℕ) : ℚ :=
  (∑ i ∈ P.support, P.coeff i * mRationalPart i j) -
    (3 / 2 : ℚ) * (∑ i ∈ D.support, D.coeff i * zRationalPart i j)

/-- Explicit rational witness for the Catalan coordinate of the contracted entry. -/
def catalanWitness (P : Polynomial ℚ) (j : ℕ) : ℚ :=
  4 * (∑ i ∈ P.support, P.coeff i * kernel ((i : ℤ) - (j : ℤ)))

theorem formalEntry_rational (P D : Polynomial ℚ) (j : ℕ) :
    (formalEntry P D j).rational = rationalWitness P D j := by
  simp [formalEntry, rationalWitness, polynomialM, polynomialZ,
    formalM, formalZ, Coordinates.rational, Coordinates.mk,
    Finset.sum_apply, Pi.smul_apply, smul_eq_mul]

theorem formalEntry_catalan (P D : Polynomial ℚ) (j : ℕ) :
    (formalEntry P D j).catalan = catalanWitness P j := by
  simp only [formalEntry, Coordinates.catalan, Pi.sub_apply, Pi.smul_apply,
    smul_eq_mul, polynomialM, polynomialZ, Finset.sum_apply,
    formalM, formalZ, Coordinates.mk, Matrix.cons_val]
  simp only [mul_zero, Finset.sum_const_zero, sub_zero]
  unfold catalanWitness
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i hi
  ring

theorem exact_defect_identity (P D : Polynomial ℚ) (j : ℕ) (G ζ : ℝ) :
    Coordinates.eval G ζ (formalEntry P D j) =
      (rationalWitness P D j : ℝ) + (catalanWitness P j : ℝ) * G +
        ((3 / 2 : ℚ) * polynomialDefect P D j : ℚ) * ζ := by
  unfold Coordinates.eval
  rw [formalEntry_rational, formalEntry_catalan, formal_entry_zeta_coordinate]

theorem coefficient_contact_cancellation_explicit (P D : Polynomial ℚ)
    (L j : ℕ) (G ζ : ℝ) (hcontact : CoefficientContact P D L) (hj : j < L) :
    Coordinates.eval G ζ (formalEntry P D j) =
      (rationalWitness P D j : ℝ) + (catalanWitness P j : ℝ) * G := by
  rw [exact_defect_identity, hcontact j hj]
  simp

/-- Finite real contraction of an arbitrary array; this name makes no integral claim. -/
def realPolynomialContraction (A : ℕ → ℕ → ℝ) (P : Polynomial ℚ) (j : ℕ) : ℝ :=
  ∑ i ∈ P.support, (P.coeff i : ℝ) * A i j

theorem realPolynomialContraction_eq_eval (A : ℕ → ℕ → ℝ)
    (V : ℕ → ℕ → Coordinates) (G ζ : ℝ)
    (hA : ∀ i j, A i j = Coordinates.eval G ζ (V i j))
    (P : Polynomial ℚ) (j : ℕ) :
    realPolynomialContraction A P j =
      Coordinates.eval G ζ (∑ i ∈ P.support, P.coeff i • V i j) := by
  rw [Coordinates.eval_sum]
  apply Finset.sum_congr rfl
  intro i hi
  rw [Coordinates.eval_smul, hA]

/-- Conditional analytic transfer. Every real-array identification is an explicit
hypothesis; neither integral evaluation nor analytic Taylor contact is asserted here. -/
theorem cancellation_of_decompositions
    (M Z : ℕ → ℕ → ℝ) (G ζ : ℝ)
    (hM : ∀ i j, M i j = Coordinates.eval G ζ (formalM i j))
    (hZ : ∀ i j, Z i j = Coordinates.eval G ζ (formalZ i j))
    (P D : Polynomial ℚ) (L j : ℕ)
    (hcontact : CoefficientContact P D L) (hj : j < L) :
    ∃ a b : ℚ,
      realPolynomialContraction M P j -
        (3 / 2 : ℝ) * realPolynomialContraction Z D j =
          (a : ℝ) + (b : ℝ) * G := by
  refine ⟨rationalWitness P D j, catalanWitness P j, ?_⟩
  rw [realPolynomialContraction_eq_eval M formalM G ζ hM,
    realPolynomialContraction_eq_eval Z formalZ G ζ hZ]
  change Coordinates.eval G ζ (polynomialM P j) -
    (3 / 2 : ℝ) * Coordinates.eval G ζ (polynomialZ D j) = _
  have hfactor : ((3 / 2 : ℚ) : ℝ) = (3 / 2 : ℝ) := by norm_num
  rw [← hfactor, ← Coordinates.eval_smul, ← Coordinates.eval_sub]
  exact coefficient_contact_cancellation_explicit P D L j G ζ hcontact hj

/-- Contraction in the second polynomial variable. -/
def pairedEntry (P D Q : Polynomial ℚ) : Coordinates :=
  ∑ j ∈ Q.support, Q.coeff j • formalEntry P D j

def pairedDefect (P D Q : Polynomial ℚ) : ℚ :=
  ∑ j ∈ Q.support, Q.coeff j * polynomialDefect P D j

theorem paired_entry_zeta_coordinate (P D Q : Polynomial ℚ) :
    (pairedEntry P D Q).zetaTwo = (3 / 2 : ℚ) * pairedDefect P D Q := by
  simp only [pairedEntry, Coordinates.zetaTwo, Finset.sum_apply,
    Pi.smul_apply, smul_eq_mul]
  change (∑ j ∈ Q.support, Q.coeff j * (formalEntry P D j).zetaTwo) = _
  simp only [formal_entry_zeta_coordinate]
  unfold pairedDefect
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i hi
  ring

theorem paired_cancellation (P D Q : Polynomial ℚ) (G ζ : ℝ)
    (hdefect : pairedDefect P D Q = 0) :
    ∃ a b : ℚ, Coordinates.eval G ζ (pairedEntry P D Q) =
      (a : ℝ) + (b : ℝ) * G := by
  refine ⟨(pairedEntry P D Q).rational, (pairedEntry P D Q).catalan, ?_⟩
  apply Coordinates.eval_of_zetaTwo_eq_zero
  rw [paired_entry_zeta_coordinate, hdefect, mul_zero]

theorem paired_cancellation_of_contact (P D Q : Polynomial ℚ) (L : ℕ)
    (G ζ : ℝ) (hcontact : CoefficientContact P D L)
    (hQ : ∀ j ∈ Q.support, j < L) :
    ∃ a b : ℚ, Coordinates.eval G ζ (pairedEntry P D Q) =
      (a : ℝ) + (b : ℝ) * G := by
  apply paired_cancellation
  unfold pairedDefect
  apply Finset.sum_eq_zero
  intro j hj
  rw [hcontact j (hQ j hj), mul_zero]

theorem paired_cancellation_of_natDegree_lt (P D Q : Polynomial ℚ) (L : ℕ)
    (G ζ : ℝ) (hcontact : CoefficientContact P D L) (hQ : Q.natDegree < L) :
    ∃ a b : ℚ, Coordinates.eval G ζ (pairedEntry P D Q) =
      (a : ℝ) + (b : ℝ) * G := by
  apply paired_cancellation_of_contact P D Q L G ζ hcontact
  intro j hj
  exact (Polynomial.le_natDegree_of_mem_supp j hj).trans_lt hQ

/-- Finite diagonal reduction keeps both irrational-constant coordinates fixed. -/
theorem formalM_diagonal (i j : ℕ) :
    formalM i j - formalM (i + 1) (j + 1) =
      Coordinates.mk (moment i / ((j : ℚ) + 1)) 0 0 := by
  ext n
  fin_cases n
  · simpa [formalM, Coordinates.mk] using mRationalPart_diagonal i j
  · simp [formalM, Coordinates.mk]
  · simp [formalM, Coordinates.mk]

theorem support_one_eq : (1 : Polynomial ℚ).support = {0} := by
  simpa using Polynomial.support_X_pow (R := ℚ) one_ne_zero 0

@[simp] theorem polynomialM_one (j : ℕ) : polynomialM 1 j = formalM 0 j := by
  simp [polynomialM, support_one_eq]

@[simp] theorem polynomialZ_X (j : ℕ) :
    polynomialZ Polynomial.X j = formalZ 1 j := by
  simp [polynomialZ, Polynomial.support_X one_ne_zero]

theorem formalEntry_one_X (j : ℕ) :
    formalEntry 1 Polynomial.X j = formalM 0 j - (3 / 2 : ℚ) • formalZ 1 j := by
  simp [formalEntry]

theorem formalM_zero_zero : formalM 0 0 = Coordinates.mk 0 4 0 := by
  ext n
  fin_cases n <;> norm_num [formalM, Coordinates.mk, mRationalPart, kernel, central]

theorem formalM_zero_one : formalM 0 1 = Coordinates.mk 0 0 (3 / 2) := by
  ext n
  fin_cases n <;> norm_num [formalM, Coordinates.mk, mRationalPart, kernel, central]

theorem formalM_one_zero : formalM 1 0 = Coordinates.mk 2 0 0 := by
  ext n
  fin_cases n <;> norm_num [formalM, Coordinates.mk, mRationalPart, kernel, central]

theorem formalM_zero_two : formalM 0 2 = Coordinates.mk 2 0 0 := by
  ext n
  fin_cases n <;> norm_num [formalM, Coordinates.mk, mRationalPart, kernel, central, kplus]

theorem formalM_two_zero : formalM 2 0 = Coordinates.mk 1 2 0 := by
  ext n
  fin_cases n <;>
    norm_num [formalM, Coordinates.mk, mRationalPart, kernel, Int.toNat, central, kminus]

theorem formalZ_zero_one : formalZ 0 1 = Coordinates.mk 1 0 0 := by
  ext n
  fin_cases n <;>
    norm_num [formalZ, Coordinates.mk, zRationalPart, harmonic, Finset.sum_range_succ]

theorem formalZ_one_one : formalZ 1 1 = Coordinates.mk (-1) 0 1 := by
  ext n
  fin_cases n <;>
    norm_num [formalZ, Coordinates.mk, zRationalPart, harmonicTwo, Finset.sum_range_succ]

theorem one_X_contact_three : CoefficientContact 1 Polynomial.X 3 := by
  intro j hj
  interval_cases j <;>
    norm_num [polynomialDefect, contactCoefficient, support_one_eq,
      kernel, central, Polynomial.coeff_X]

theorem one_X_entry_zero : formalEntry 1 Polynomial.X 0 = Coordinates.mk (-3 / 2) 4 0 := by
  rw [formalEntry_one_X, formalM_zero_zero]
  ext n
  fin_cases n <;>
    norm_num [formalZ, Coordinates.mk, zRationalPart, harmonic, Finset.sum_range_succ]

theorem one_X_entry_one : formalEntry 1 Polynomial.X 1 = Coordinates.mk (3 / 2) 0 0 := by
  rw [formalEntry_one_X, formalM_zero_one, formalZ_one_one]
  ext n
  fin_cases n <;> norm_num [Coordinates.mk]

theorem one_X_entry_two : formalEntry 1 Polynomial.X 2 = Coordinates.mk (5 / 4) 0 0 := by
  rw [formalEntry_one_X, formalM_zero_two]
  ext n
  fin_cases n <;>
    norm_num [formalZ, Coordinates.mk, zRationalPart, harmonic, Finset.sum_range_succ]

/-- The strict column bound is essential: at `j=L=3`, the formal zeta coordinate survives. -/
theorem one_X_entry_three :
    formalEntry 1 Polynomial.X 3 = Coordinates.mk (-1 / 8) 0 (3 / 4) := by
  rw [formalEntry_one_X]
  ext n
  fin_cases n <;>
    norm_num [formalM, formalZ, Coordinates.mk, mRationalPart, zRationalPart,
      kernel, Int.toNat, central, kplus, harmonic, Finset.sum_range_succ]

theorem one_X_entry_three_zeta_nonzero :
    (formalEntry 1 Polynomial.X 3).zetaTwo ≠ 0 := by
  rw [one_X_entry_three, Coordinates.zetaTwo_mk]
  norm_num

end

end MixedMoments
