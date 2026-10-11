import Mathlib
import MixedMoments.Constants
import MixedMoments.Integrals

/-!
# The independent zeta boundary integral

The square-root substitution is proved on the closed interval with derivatives
only on its interior. Its endpoint singularities are treated using proved
integrability, rather than a formal substitution at a singular endpoint.
-/

noncomputable section

open MeasureTheory Set Filter
open scoped Topology Interval

namespace MixedMoments.BoundaryZeta

/-- The involution of the unit interval used in the zeta boundary substitution. -/
def complementSqrt (t : ℝ) : ℝ := Real.sqrt (1 - t ^ 2)

private theorem square_gap_pos {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) :
    0 < 1 - t ^ 2 := by
  nlinarith [ht.1, ht.2]

private theorem inner_den_pos {u s : ℝ} (hu : u ∈ Ioo (0 : ℝ) 1)
    (hs : s ∈ Icc (0 : ℝ) 1) : 0 < 1 - u ^ 2 * s ^ 2 := by
  have hu2 : u ^ 2 < 1 := by nlinarith [hu.1, hu.2]
  have hs2 : s ^ 2 ≤ 1 := by nlinarith [hs.1, hs.2]
  nlinarith [sq_nonneg u, sq_nonneg s,
    mul_le_mul_of_nonneg_left hs2 (sq_nonneg u)]

/-- The inner rational integral in the paired M(0,1) kernel. -/
theorem integral_inner {u : ℝ} (hu : u ∈ Ioo (0 : ℝ) 1) :
    (∫ s in (0 : ℝ)..1, s / (1 - u ^ 2 * s ^ 2)) =
      -Real.log (1 - u ^ 2) / (2 * u ^ 2) := by
  have huc : u ≠ 0 := ne_of_gt hu.1
  have hcont : ContinuousOn (fun s : ℝ => s / (1 - u ^ 2 * s ^ 2))
      (uIcc (0 : ℝ) 1) := by
    rw [uIcc_of_le zero_le_one]
    apply continuous_id.continuousOn.div
      (continuous_const.sub (continuous_const.mul (continuous_id.pow 2))).continuousOn
    intro s hs
    exact (inner_den_pos hu hs).ne'
  have hder (s : ℝ) (hs : s ∈ uIcc (0 : ℝ) 1) :
      HasDerivAt (fun x : ℝ => -Real.log (1 - u ^ 2 * x ^ 2) / (2 * u ^ 2))
        (s / (1 - u ^ 2 * s ^ 2)) s := by
    rw [uIcc_of_le zero_le_one] at hs
    have hd := (inner_den_pos hu hs).ne'
    convert ((((hasDerivAt_id s).pow 2).const_mul (u ^ 2)).const_sub 1).log hd
      |>.neg |>.div_const (2 * u ^ 2) using 1
    dsimp
    field_simp
  have h := intervalIntegral.integral_eq_sub_of_hasDerivAt hder hcont.intervalIntegrable
  simpa using h

theorem complementSqrt_mem_Icc {t : ℝ} (_ht : t ∈ Icc (0 : ℝ) 1) :
    complementSqrt t ∈ Icc (0 : ℝ) 1 := by
  refine ⟨Real.sqrt_nonneg _, ?_⟩
  have h : 1 - t ^ 2 ≤ 1 := by nlinarith [sq_nonneg t]
  simpa [complementSqrt] using Real.sqrt_le_sqrt h

theorem complementSqrt_mem_Ioo {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) :
    complementSqrt t ∈ Ioo (0 : ℝ) 1 := by
  refine ⟨Real.sqrt_pos.2 (square_gap_pos ht), ?_⟩
  have h : 1 - t ^ 2 < 1 := by nlinarith [ht.1]
  simpa [complementSqrt] using Real.sqrt_lt_sqrt (square_gap_pos ht).le h

theorem complementSqrt_sq {t : ℝ} (ht : t ∈ Icc (0 : ℝ) 1) :
    complementSqrt t ^ 2 = 1 - t ^ 2 := by
  exact Real.sq_sqrt (by nlinarith [ht.1, ht.2])

theorem complementSqrt_involutive {t : ℝ} (ht : t ∈ Icc (0 : ℝ) 1) :
    complementSqrt (complementSqrt t) = t := by
  unfold complementSqrt
  rw [Real.sq_sqrt (by nlinarith [ht.1, ht.2]), sub_sub_cancel,
    Real.sqrt_sq_eq_abs, abs_of_nonneg ht.1]

theorem complementSqrt_image_Icc :
    complementSqrt '' Icc (0 : ℝ) 1 = Icc (0 : ℝ) 1 := by
  apply Set.Subset.antisymm
  · rintro _ ⟨t, ht, rfl⟩
    exact complementSqrt_mem_Icc ht
  · intro t ht
    exact ⟨complementSqrt t, complementSqrt_mem_Icc ht, complementSqrt_involutive ht⟩

theorem hasDerivAt_complementSqrt {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) :
    HasDerivAt complementSqrt (-t / complementSqrt t) t := by
  have hgap := (square_gap_pos ht).ne'
  convert (((hasDerivAt_id t).pow 2).const_sub 1).sqrt hgap using 1
  dsimp [complementSqrt]
  ring

theorem continuousOn_zetaLogKernel :
    ContinuousOn Constants.zetaLogKernel (Ioo (0 : ℝ) 1) := by
  intro t ht
  exact (((Real.continuousAt_log (ne_of_gt ht.1)).neg).div
    (continuous_const.sub (continuous_id.pow 2)).continuousAt
    (square_gap_pos ht).ne').continuousWithinAt

/-- The paired slice has a logarithmic formula on the interior. -/
theorem pairedSlice01_eq {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) :
    Analysis.pairedSlice01 t =
      -Real.log (1 - t ^ 2) / (t * complementSqrt t) := by
  unfold Analysis.pairedSlice01
  simp_rw [mul_div_assoc]
  rw [intervalIntegral.integral_const_mul, integral_inner ht]
  have ht0 : t ≠ 0 := ne_of_gt ht.1
  unfold complementSqrt
  field_simp

/-- The transformed integrand agrees at the endpoints as well, where Lean's
total division assigns zero and the values have no effect on the integral. -/
theorem substitution_integrand_eq {t : ℝ} (ht : t ∈ Icc (0 : ℝ) 1) :
    Constants.zetaLogKernel (complementSqrt t) * (-t / complementSqrt t) =
      (-1 / 2 : ℝ) * Analysis.pairedSlice01 t := by
  by_cases h0 : t = 0
  · subst t
    simp [complementSqrt, Constants.zetaLogKernel, Analysis.pairedSlice01]
  by_cases h1 : t = 1
  · subst t
    simp [complementSqrt, Constants.zetaLogKernel, Analysis.pairedSlice01]
  have hti : t ∈ Ioo (0 : ℝ) 1 :=
    ⟨lt_of_le_of_ne ht.1 (Ne.symm h0), lt_of_le_of_ne ht.2 h1⟩
  rw [pairedSlice01_eq hti]
  unfold Constants.zetaLogKernel complementSqrt
  rw [Real.sq_sqrt (square_gap_pos hti).le, Real.log_sqrt (square_gap_pos hti).le]
  have ht0 : t ≠ 0 := ne_of_gt hti.1
  have hs0 : Real.sqrt (1 - t ^ 2) ≠ 0 := ne_of_gt (Real.sqrt_pos.2 (square_gap_pos hti))
  field_simp
  ring

/-- The square-root change of variables supplies the independent zeta boundary
integral. Both transformed and target integrability are proved beforehand. -/
theorem integral_pairedSlice01 :
    (∫ t in (0 : ℝ)..1, Analysis.pairedSlice01 t) =
      2 * ∫ x in (0 : ℝ)..1, Constants.zetaLogKernel x := by
  have hf : ContinuousOn complementSqrt (uIcc (0 : ℝ) 1) :=
    (Real.continuous_sqrt.comp (continuous_const.sub (continuous_id.pow 2))).continuousOn
  have hfder : ∀ t ∈ Ioo (min (0 : ℝ) 1) (max (0 : ℝ) 1),
      HasDerivWithinAt complementSqrt (-t / complementSqrt t) (Ioi t) t := by
    intro t ht
    simp only [min_eq_left zero_le_one, max_eq_right zero_le_one] at ht
    exact (hasDerivAt_complementSqrt ht).hasDerivWithinAt
  have hgcont : ContinuousOn Constants.zetaLogKernel
      (complementSqrt '' Ioo (min (0 : ℝ) 1) (max (0 : ℝ) 1)) := by
    apply continuousOn_zetaLogKernel.mono
    rintro _ ⟨t, ht, rfl⟩
    simp only [min_eq_left zero_le_one, max_eq_right zero_le_one] at ht
    exact complementSqrt_mem_Ioo ht
  have hg1 : IntegrableOn Constants.zetaLogKernel
      (complementSqrt '' uIcc (0 : ℝ) 1) := by
    rw [uIcc_of_le zero_le_one, complementSqrt_image_Icc]
    exact (intervalIntegrable_iff_integrableOn_Icc_of_le zero_le_one).1
      Constants.intervalIntegrable_zetaLogKernel
  have hi : IntervalIntegrable
      (fun t => Constants.zetaLogKernel (complementSqrt t) * (-t / complementSqrt t))
      volume 0 1 := by
    apply (Analysis.intervalIntegrable_pairedSlice01.const_mul (-1 / 2 : ℝ)).congr
    intro t ht
    rw [uIoc_of_le zero_le_one] at ht
    exact (substitution_integrand_eq ⟨ht.1.le, ht.2⟩).symm
  have hg2 : IntegrableOn
      (fun t => Constants.zetaLogKernel (complementSqrt t) * (-t / complementSqrt t))
      (uIcc (0 : ℝ) 1) := by
    rw [uIcc_of_le zero_le_one]
    exact (intervalIntegrable_iff_integrableOn_Icc_of_le zero_le_one).1 hi
  have h := intervalIntegral.integral_comp_mul_deriv''' hf hfder hgcont hg1 hg2
  have heq : (∫ t in (0 : ℝ)..1,
      Constants.zetaLogKernel (complementSqrt t) * (-t / complementSqrt t)) =
      (-1 / 2 : ℝ) * ∫ t in (0 : ℝ)..1, Analysis.pairedSlice01 t := by
    rw [← intervalIntegral.integral_const_mul]
    apply intervalIntegral.integral_congr
    intro t ht
    rw [uIcc_of_le zero_le_one] at ht
    exact substitution_integrand_eq ht
  change (∫ t in (0 : ℝ)..1,
      Constants.zetaLogKernel (complementSqrt t) * (-t / complementSqrt t)) =
      ∫ x in complementSqrt 0..complementSqrt 1, Constants.zetaLogKernel x at h
  rw [heq] at h
  simp only [complementSqrt, zero_pow (by decide : 2 ≠ 0), sub_zero, Real.sqrt_one,
    one_pow, sub_self, Real.sqrt_zero] at h
  rw [intervalIntegral.integral_symm (a := (0 : ℝ)) (b := 1)
    (f := Constants.zetaLogKernel)] at h
  linarith

/-- The actual M(0,1) boundary integral, with no realization hypothesis. -/
theorem M_zero_one_eq_logIntegral :
    Analysis.M 0 1 = 2 * ∫ x in (0 : ℝ)..1, Constants.zetaLogKernel x := by
  rw [Analysis.M_zero_one_eq_paired, integral_pairedSlice01]

/-- The independent zeta boundary start required by the moment decomposition. -/
theorem M_zero_one : Analysis.M 0 1 = (3 / 2 : ℝ) * Zeta.zeta2 := by
  rw [M_zero_one_eq_logIntegral, Constants.integral_zetaLogKernel]
  ring

end MixedMoments.BoundaryZeta
