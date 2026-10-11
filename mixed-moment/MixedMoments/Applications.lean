import MixedMoments.Decomposition
import MixedMoments.BoundaryCatalan
import MixedMoments.BoundaryZeta
import MixedMoments.TailBounds
import MixedMoments.TaylorContact

/-! Actual integral instantiations of the rational cancellation core. -/

noncomputable section
namespace MixedMoments
open scoped Topology

/-- All recurrence hypotheses and both transcendental starts are proved for
these actual integrals; this construction assumes no decomposition identity. -/
theorem actualMomentRecurrenceData :
    MomentRecurrenceData Analysis.M Constants.catalan Zeta.zeta2 := by
  refine ⟨?_, ?_, Analysis.M_plus_boundary_recurrence,
    Analysis.M_zero_zero_eq_catalan, Analysis.M_one_zero, BoundaryZeta.M_zero_one⟩
  · intro i j
    simpa only [Analysis.moment_eq_rat] using Analysis.M_diagonal i j
  · intro d
    simpa only [Analysis.moment_eq_rat] using Analysis.M_minus_boundary_recurrence d

/-- Unconditional realization of the specified three rational coordinates
by the actual absolutely integrable M kernel. -/
theorem M_eq_formalM (i j : ℕ) :
    Analysis.M i j = Coordinates.eval Constants.catalan Zeta.zeta2 (formalM i j) :=
  realM_eq_eval_formalM Analysis.M Constants.catalan Zeta.zeta2 actualMomentRecurrenceData i j

theorem M_polynomialColumn_eq_formalM (P : Polynomial ℚ) (j : ℕ) :
    Analysis.polynomialColumn P j =
      Coordinates.eval Constants.catalan Zeta.zeta2 (polynomialM P j) := by
  rw [Analysis.polynomialColumn_eq_sum]
  unfold polynomialM
  rw [Coordinates.eval_sum]
  apply Finset.sum_congr rfl
  intro i hi
  rw [Coordinates.eval_smul, M_eq_formalM]

/-- Exact defect formula for the original polynomial column integrals. -/
theorem integral_exact_defect (P D : Polynomial ℚ) (j : ℕ) :
    Analysis.polynomialColumn P j - (3 / 2 : ℝ) * Zeta.polynomialColumn D j =
      (rationalWitness P D j : ℝ) + (catalanWitness P j : ℝ) * Constants.catalan +
        ((3 / 2 : ℚ) * polynomialDefect P D j : ℚ) * Zeta.zeta2 := by
  rw [M_polynomialColumn_eq_formalM, Zeta.polynomialColumn_eq_formalZ Constants.catalan]
  have h := exact_defect_identity P D j Constants.catalan Zeta.zeta2
  simpa only [formalEntry, Coordinates.eval_sub, Coordinates.eval_smul,
    Rat.cast_div, Rat.cast_ofNat] using h

/-- The sufficient cancellation theorem for actual integrals, under a finite
coefficient contact hypothesis. No arithmetic independence is assumed. -/
theorem integral_cancellation_of_coefficientContact (P D : Polynomial ℚ) (L j : ℕ)
    (hcontact : CoefficientContact P D L) (hj : j < L) :
    Analysis.polynomialColumn P j - (3 / 2 : ℝ) * Zeta.polynomialColumn D j =
      (rationalWitness P D j : ℝ) + (catalanWitness P j : ℝ) * Constants.catalan := by
  rw [integral_exact_defect, hcontact j hj]
  simp

theorem integral_cancellation_witnesses (P D : Polynomial ℚ) (L j : ℕ)
    (hcontact : CoefficientContact P D L) (hj : j < L) :
    ∃ a b : ℚ, Analysis.polynomialColumn P j - (3 / 2 : ℝ) * Zeta.polynomialColumn D j =
      (a : ℝ) + (b : ℝ) * Constants.catalan :=
  ⟨rationalWitness P D j, catalanWitness P j,
    integral_cancellation_of_coefficientContact P D L j hcontact hj⟩

/-- Positive-side big-O contact gives the explicit rational affine formula
for the actual polynomial column integrals. -/
theorem integral_cancellation_of_analyticContact (P D : Polynomial ℚ) (L j : ℕ)
    (hcontact : analyticContactFunction P D =O[𝓝[>] 0] (fun x => x ^ L))
    (hj : j < L) :
    Analysis.polynomialColumn P j - (3 / 2 : ℝ) * Zeta.polynomialColumn D j =
      (rationalWitness P D j : ℝ) + (catalanWitness P j : ℝ) * Constants.catalan :=
  integral_cancellation_of_coefficientContact P D L j
    (analyticContact_implies_coefficientContact P D L hcontact) hj

/-- Two-sided big-O contact is sufficient for the same actual-integral formula. -/
theorem integral_cancellation_of_analyticContact_nhds (P D : Polynomial ℚ) (L j : ℕ)
    (hcontact : analyticContactFunction P D =O[𝓝 0] (fun x => x ^ L))
    (hj : j < L) :
    Analysis.polynomialColumn P j - (3 / 2 : ℝ) * Zeta.polynomialColumn D j =
      (rationalWitness P D j : ℝ) + (catalanWitness P j : ℝ) * Constants.catalan :=
  integral_cancellation_of_coefficientContact P D L j
    (analyticContact_nhds_implies_coefficientContact P D L hcontact) hj

theorem integral_analyticContact_witnesses (P D : Polynomial ℚ) (L j : ℕ)
    (hcontact : analyticContactFunction P D =O[𝓝[>] 0] (fun x => x ^ L))
    (hj : j < L) :
    ∃ a b : ℚ, Analysis.polynomialColumn P j - (3 / 2 : ℝ) * Zeta.polynomialColumn D j =
      (a : ℝ) + (b : ℝ) * Constants.catalan :=
  ⟨rationalWitness P D j, catalanWitness P j,
    integral_cancellation_of_analyticContact P D L j hcontact hj⟩

end MixedMoments
