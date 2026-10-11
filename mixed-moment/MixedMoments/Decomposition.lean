import MixedMoments.Cancellation
import MixedMoments.Series
import MixedMoments.RationalSeries

/-!
# Conditional decomposition from recurrence data

This file proves uniqueness and decomposition for real arrays satisfying
explicit diagonal and boundary recurrences and three boundary values.
It does not prove those boundary values for an integral.
-/

noncomputable section

namespace MixedMoments

theorem formalM_minus_boundary (d : ℕ) :
    ((d : ℚ) + 2) • formalM (d + 2) 0 =
      ((d : ℚ) + 1) • formalM d 0 +
        Coordinates.mk (moment d + moment (d + 1)) 0 0 := by
  have hn : kernel (-(d : ℤ) - 1) = 0 := kernel_of_neg _ (by omega)
  have hn' : kernel (-((d + 2 : ℕ) : ℤ) - 1) = 0 :=
    kernel_of_neg _ (by omega)
  ext n
  fin_cases n
  · change ((d : ℚ) + 2) * mRationalPart (d + 2) 0 =
      ((d : ℚ) + 1) * mRationalPart d 0 + (moment d + moment (d + 1))
    simpa [add_assoc]
      using kminus_recurrence d
  · change ((d : ℚ) + 2) * (4 * kernel (((d + 2 : ℕ) : ℤ) - 0)) =
      ((d : ℚ) + 1) * (4 * kernel ((d : ℤ) - 0)) + 0
    push_cast
    simp only [sub_zero, add_zero]
    nlinarith [kernel_step d]
  · change ((d : ℚ) + 2) * ((3 / 2 : ℚ) * kernel (0 - ((d + 2 : ℕ) : ℤ) - 1)) =
      ((d : ℚ) + 1) * ((3 / 2 : ℚ) * kernel (0 - (d : ℤ) - 1)) + 0
    rw [zero_sub, zero_sub, hn, hn']
    ring

theorem formalM_plus_boundary (d : ℕ) :
    ((d : ℚ) + 1) • formalM 0 (d + 2) =
      (d : ℚ) • formalM 0 d +
        Coordinates.mk (2 / ((d : ℚ) + 1)) 0 0 := by
  have hn : kernel (-((d + 2 : ℕ) : ℤ)) = 0 :=
    kernel_of_neg _ (by omega)
  ext n
  fin_cases n
  · change ((d : ℚ) + 1) * mRationalPart 0 (d + 2) =
      (d : ℚ) * mRationalPart 0 d + 2 / ((d : ℚ) + 1)
    simpa
      using kplus_recurrence d
  · change ((d : ℚ) + 1) * (4 * kernel (0 - ((d + 2 : ℕ) : ℤ))) =
      (d : ℚ) * (4 * kernel (0 - (d : ℤ))) + 0
    simp only [zero_sub]
    rw [hn]
    by_cases hd : d = 0
    · subst d
      norm_num
    · have hn' : kernel (-(d : ℤ)) = 0 := kernel_of_neg _ (by omega)
      rw [hn']
      ring
  · change ((d : ℚ) + 1) * ((3 / 2 : ℚ) * kernel (((d + 2 : ℕ) : ℤ) - 0 - 1)) =
      (d : ℚ) * ((3 / 2 : ℚ) * kernel ((d : ℤ) - 0 - 1)) + 0
    push_cast
    simp only [sub_zero, add_zero]
    have hidx : (d : ℤ) + 2 - 1 = (d : ℤ) + 1 := by ring
    rw [hidx]
    nlinarith [kernel_shifted_step d]

/-- All analytic premises used in the M-array decomposition are visible here. -/
structure MomentRecurrenceData (M : ℕ → ℕ → ℝ) (G ζ : ℝ) : Prop where
  diagonal : ∀ i j,
    M i j - M (i + 1) (j + 1) = (moment i : ℝ) / ((j : ℝ) + 1)
  minusBoundary : ∀ d : ℕ,
    ((d : ℝ) + 2) * M (d + 2) 0 =
      ((d : ℝ) + 1) * M d 0 + (moment d : ℝ) + (moment (d + 1) : ℝ)
  plusBoundary : ∀ d : ℕ,
    ((d : ℝ) + 1) * M 0 (d + 2) =
      (d : ℝ) * M 0 d + 2 / ((d : ℝ) + 1)
  startCatalan : M 0 0 = 4 * G
  startMinus : M 1 0 = 2
  startZeta : M 0 1 = (3 / 2 : ℝ) * ζ

theorem evaluated_formalM_diagonal (G ζ : ℝ) (i j : ℕ) :
    Coordinates.eval G ζ (formalM i j) -
      Coordinates.eval G ζ (formalM (i + 1) (j + 1)) =
        (moment i : ℝ) / ((j : ℝ) + 1) := by
  have h := congrArg (Coordinates.eval G ζ) (formalM_diagonal i j)
  rw [Coordinates.eval_sub, Coordinates.eval_mk] at h
  simpa using h

theorem evaluated_formalM_minus_boundary (G ζ : ℝ) (d : ℕ) :
    ((d : ℝ) + 2) * Coordinates.eval G ζ (formalM (d + 2) 0) =
      ((d : ℝ) + 1) * Coordinates.eval G ζ (formalM d 0) +
        (moment d : ℝ) + (moment (d + 1) : ℝ) := by
  have h := congrArg (Coordinates.eval G ζ) (formalM_minus_boundary d)
  rw [Coordinates.eval_smul, Coordinates.eval_add,
    Coordinates.eval_smul, Coordinates.eval_mk] at h
  simpa [add_assoc] using h

theorem evaluated_formalM_plus_boundary (G ζ : ℝ) (d : ℕ) :
    ((d : ℝ) + 1) * Coordinates.eval G ζ (formalM 0 (d + 2)) =
      (d : ℝ) * Coordinates.eval G ζ (formalM 0 d) + 2 / ((d : ℝ) + 1) := by
  have h := congrArg (Coordinates.eval G ζ) (formalM_plus_boundary d)
  rw [Coordinates.eval_smul, Coordinates.eval_add,
    Coordinates.eval_smul, Coordinates.eval_mk] at h
  simpa using h

theorem evaluated_formalM_recurrence_data (G ζ : ℝ) :
    MomentRecurrenceData (fun i j => Coordinates.eval G ζ (formalM i j)) G ζ := by
  refine ⟨evaluated_formalM_diagonal G ζ,
    evaluated_formalM_minus_boundary G ζ, evaluated_formalM_plus_boundary G ζ,
    ?_, ?_, ?_⟩
  · rw [formalM_zero_zero]
    norm_num
  · rw [formalM_one_zero]
    norm_num
  · rw [formalM_zero_one]
    norm_num

/-- Elementary uniqueness of a two-step recurrence with nonzero leading coefficient. -/
theorem two_step_recurrence_unique (F H a b c : ℕ → ℝ)
    (hzero : F 0 = H 0) (hone : F 1 = H 1)
    (ha : ∀ n, a n ≠ 0)
    (hF : ∀ n, a n * F (n + 2) = b n * F n + c n)
    (hH : ∀ n, a n * H (n + 2) = b n * H n + c n) :
    ∀ n, F n = H n := by
  intro n
  induction n using Nat.twoStepInduction with
  | zero => exact hzero
  | one => exact hone
  | more n hn _ =>
    apply mul_left_cancel₀ (ha n)
    rw [hF, hH, hn]

/-- Diagonal reduction and the two boundaries uniquely determine the whole array. -/
theorem moment_recurrence_data_unique (M H : ℕ → ℕ → ℝ) (G ζ : ℝ)
    (hM : MomentRecurrenceData M G ζ) (hH : MomentRecurrenceData H G ζ) :
    ∀ i j, M i j = H i j := by
  have hminus : ∀ i, M i 0 = H i 0 := by
    apply two_step_recurrence_unique (fun i => M i 0) (fun i => H i 0)
      (fun i => (i : ℝ) + 2) (fun i => (i : ℝ) + 1)
      (fun i => (moment i : ℝ) + (moment (i + 1) : ℝ))
    · exact hM.startCatalan.trans hH.startCatalan.symm
    · exact hM.startMinus.trans hH.startMinus.symm
    · intro n
      positivity
    · intro n
      simpa only [add_assoc] using hM.minusBoundary n
    · intro n
      simpa only [add_assoc] using hH.minusBoundary n
  have hplus : ∀ j, M 0 j = H 0 j := by
    apply two_step_recurrence_unique (fun j => M 0 j) (fun j => H 0 j)
      (fun j => (j : ℝ) + 1) (fun j => (j : ℝ))
      (fun j => 2 / ((j : ℝ) + 1))
    · exact hM.startCatalan.trans hH.startCatalan.symm
    · exact hM.startZeta.trans hH.startZeta.symm
    · intro n
      positivity
    · exact hM.plusBoundary
    · exact hH.plusBoundary
  intro i
  induction i with
  | zero => exact hplus
  | succ i ih =>
    intro j
    cases j with
    | zero => exact hminus (i + 1)
    | succ j =>
      have hm := hM.diagonal i j
      have hh := hH.diagonal i j
      rw [ih j] at hm
      simpa only [Nat.succ_eq_add_one] using (by linarith :
        M (i + 1) (j + 1) = H (i + 1) (j + 1))

/-- Full entry decomposition follows from recurrence data and the three starts. -/
theorem realM_eq_eval_formalM (M : ℕ → ℕ → ℝ) (G ζ : ℝ)
    (hM : MomentRecurrenceData M G ζ) (i j : ℕ) :
    M i j = Coordinates.eval G ζ (formalM i j) :=
  moment_recurrence_data_unique M (fun i j => Coordinates.eval G ζ (formalM i j))
    G ζ hM (evaluated_formalM_recurrence_data G ζ) i j

/-- Conditional cancellation with the M-array decomposition derived from recurrences. -/
theorem cancellation_of_recurrences
    (M Z : ℕ → ℕ → ℝ) (G ζ : ℝ)
    (hM : MomentRecurrenceData M G ζ)
    (hZ : ∀ i j, Z i j = Coordinates.eval G ζ (formalZ i j))
    (P D : Polynomial ℚ) (L j : ℕ)
    (hcontact : CoefficientContact P D L) (hj : j < L) :
    ∃ a b : ℚ,
      realPolynomialContraction M P j -
        (3 / 2 : ℝ) * realPolynomialContraction Z D j =
          (a : ℝ) + (b : ℝ) * G :=
  cancellation_of_decompositions M Z G ζ (realM_eq_eval_formalM M G ζ hM)
    hZ P D L j hcontact hj

/-- The real moment series supplies every recurrence. Only its two independent
boundary constants and decay of the underlying moments remain premises. -/
theorem momentSeries_recurrence_data (a : ℕ → ℝ) (G ζ : ℝ)
    (ha : ∀ n, a n = (moment n : ℝ))
    (hzero : Filter.Tendsto a Filter.atTop (nhds 0))
    (hCatalan : Series.momentSeries a 0 0 = 4 * G)
    (hZeta : Series.momentSeries a 0 1 = (3 / 2 : ℝ) * ζ) :
    MomentRecurrenceData (Series.momentSeries a) G ζ := by
  have hnonneg : ∀ n, 0 ≤ a n := by
    intro n
    rw [ha]
    exact_mod_cast moment_nonneg n
  have hrec : ∀ n : ℕ,
      ((n : ℝ) + 3) * a (n + 2) = ((n : ℝ) + 2) * a n := by
    intro n
    rw [ha, ha]
    exact_mod_cast moment_recurrence n
  have ha0 : a 0 = 2 := by simp [ha]
  have ha1 : a 1 = 0 := by simp [ha]
  refine ⟨?_, ?_, ?_, hCatalan, ?_, hZeta⟩
  · intro i j
    rw [← ha]
    exact Series.momentSeries_diagonal a i j
      (Series.summable_momentSeries a hnonneg hrec i j)
  · intro d
    rw [← ha, ← ha]
    exact Series.minus_boundary_recurrence a hrec hzero d
      (by simpa using Series.summable_momentSeries a hnonneg hrec d 0)
      (by simpa using Series.summable_momentSeries a hnonneg hrec (d + 2) 0)
  · intro d
    apply Series.plus_boundary_recurrence a hrec hzero ha0 ha1 d
    · simpa using Series.summable_momentSeries a hnonneg hrec 0 d
    · convert Series.summable_momentSeries a hnonneg hrec 0 (d + 2) using 1
      ext u
      simp only [Nat.cast_add, Nat.cast_ofNat, zero_add]
      congr 1
      ring
  · exact Series.momentSeries_one_zero a hnonneg hrec hzero ha0 ha1

/-- Universal series decomposition, conditional only on moment identification,
decay, and the two independent boundary constants. -/
theorem momentSeries_eq_eval_formalM (a : ℕ → ℝ) (G ζ : ℝ)
    (ha : ∀ n, a n = (moment n : ℝ))
    (hzero : Filter.Tendsto a Filter.atTop (nhds 0))
    (hCatalan : Series.momentSeries a 0 0 = 4 * G)
    (hZeta : Series.momentSeries a 0 1 = (3 / 2 : ℝ) * ζ)
    (i j : ℕ) :
    Series.momentSeries a i j = Coordinates.eval G ζ (formalM i j) :=
  realM_eq_eval_formalM (Series.momentSeries a) G ζ
    (momentSeries_recurrence_data a G ζ ha hzero hCatalan hZeta) i j

theorem cancellation_of_momentSeries
    (a : ℕ → ℝ) (Z : ℕ → ℕ → ℝ) (G ζ : ℝ)
    (ha : ∀ n, a n = (moment n : ℝ))
    (hzero : Filter.Tendsto a Filter.atTop (nhds 0))
    (hCatalan : Series.momentSeries a 0 0 = 4 * G)
    (hZeta : Series.momentSeries a 0 1 = (3 / 2 : ℝ) * ζ)
    (hZ : ∀ i j, Z i j = Coordinates.eval G ζ (formalZ i j))
    (P D : Polynomial ℚ) (L j : ℕ)
    (hcontact : CoefficientContact P D L) (hj : j < L) :
    ∃ b c : ℚ,
      realPolynomialContraction (Series.momentSeries a) P j -
        (3 / 2 : ℝ) * realPolynomialContraction Z D j =
          (b : ℝ) + (c : ℝ) * G :=
  cancellation_of_recurrences (Series.momentSeries a) Z G ζ
    (momentSeries_recurrence_data a G ζ ha hzero hCatalan hZeta)
    hZ P D L j hcontact hj

/-- For the canonical rational moment series, convergence is proved rather than assumed. -/
theorem realMomentSeries_recurrence_data (G ζ : ℝ)
    (hCatalan : Series.momentSeries realMoment 0 0 = 4 * G)
    (hZeta : Series.momentSeries realMoment 0 1 = (3 / 2 : ℝ) * ζ) :
    MomentRecurrenceData (Series.momentSeries realMoment) G ζ :=
  momentSeries_recurrence_data realMoment G ζ (fun _ => rfl)
    realMoment_tendsto_zero hCatalan hZeta

theorem realMomentSeries_eq_eval_formalM (G ζ : ℝ)
    (hCatalan : Series.momentSeries realMoment 0 0 = 4 * G)
    (hZeta : Series.momentSeries realMoment 0 1 = (3 / 2 : ℝ) * ζ)
    (i j : ℕ) :
    Series.momentSeries realMoment i j = Coordinates.eval G ζ (formalM i j) :=
  realM_eq_eval_formalM (Series.momentSeries realMoment) G ζ
    (realMomentSeries_recurrence_data G ζ hCatalan hZeta) i j

theorem cancellation_of_realMomentSeries
    (Z : ℕ → ℕ → ℝ) (G ζ : ℝ)
    (hCatalan : Series.momentSeries realMoment 0 0 = 4 * G)
    (hZeta : Series.momentSeries realMoment 0 1 = (3 / 2 : ℝ) * ζ)
    (hZ : ∀ i j, Z i j = Coordinates.eval G ζ (formalZ i j))
    (P D : Polynomial ℚ) (L j : ℕ)
    (hcontact : CoefficientContact P D L) (hj : j < L) :
    ∃ a b : ℚ,
      realPolynomialContraction (Series.momentSeries realMoment) P j -
        (3 / 2 : ℝ) * realPolynomialContraction Z D j =
          (a : ℝ) + (b : ℝ) * G :=
  cancellation_of_recurrences (Series.momentSeries realMoment) Z G ζ
    (realMomentSeries_recurrence_data G ζ hCatalan hZeta)
    hZ P D L j hcontact hj

end MixedMoments
