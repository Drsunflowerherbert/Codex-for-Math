import MixedMoments.Integrals
import MixedMoments.Constants

open MeasureTheory Set
open scoped Interval

namespace MixedMoments.BoundaryCatalan

/-- The Cayley substitution carrying `(0, 1)` to itself in reverse order. -/
noncomputable def cayley (x : ℝ) : ℝ := (1 - x ^ 2) / (1 + x ^ 2)

@[simp] theorem cayley_zero : cayley 0 = 1 := by norm_num [cayley]
@[simp] theorem cayley_one : cayley 1 = 0 := by norm_num [cayley]

theorem continuous_cayley : Continuous cayley := by
  unfold cayley
  exact (continuous_const.sub (continuous_id.pow 2)).div
    (continuous_const.add (continuous_id.pow 2)) (by intro x; positivity)

theorem hasDerivAt_cayley (x : ℝ) :
    HasDerivAt cayley (-4 * x / (1 + x ^ 2) ^ 2) x := by
  have hd : 1 + x ^ 2 ≠ 0 := by positivity
  have hsq : HasDerivAt (fun y : ℝ => y ^ 2) (2 * x) x := by
    simpa using (hasDerivAt_id x).pow 2
  have h : HasDerivAt cayley
      (((0 - 2 * x) * (1 + x ^ 2) - (1 - x ^ 2) * (0 + 2 * x)) /
        (1 + x ^ 2) ^ 2) x :=
    ((hasDerivAt_const x (1 : ℝ)).sub hsq).div
      ((hasDerivAt_const x (1 : ℝ)).add hsq) hd
  convert h using 1
  ring

theorem deriv_cayley (x : ℝ) :
    deriv cayley x = -4 * x / (1 + x ^ 2) ^ 2 := (hasDerivAt_cayley x).deriv

theorem cayley_pos {x : ℝ} (hx : x ∈ Set.Ioo (0 : ℝ) 1) : 0 < cayley x := by
  have hx2 : x ^ 2 < 1 := by
    nlinarith [mul_pos hx.1 (sub_pos.mpr hx.2)]
  exact div_pos (sub_pos.mpr hx2) (by positivity)

theorem cayley_lt_one {x : ℝ} (hx : x ∈ Set.Ioo (0 : ℝ) 1) : cayley x < 1 := by
  unfold cayley
  have hd : 0 < 1 + x ^ 2 := by positivity
  apply (div_lt_one hd).2
  have hxp : 0 < x := hx.1
  nlinarith [sq_pos_of_pos hxp]

theorem cayley_mem_Ioo {x : ℝ} (hx : x ∈ Set.Ioo (0 : ℝ) 1) :
    cayley x ∈ Set.Ioo (0 : ℝ) 1 := ⟨cayley_pos hx, cayley_lt_one hx⟩

theorem sqrt_one_sub_cayley_sq {x : ℝ} (hx : x ∈ Set.Ioo (0 : ℝ) 1) :
    Real.sqrt (1 - cayley x ^ 2) = 2 * x / (1 + x ^ 2) := by
  have hd : 1 + x ^ 2 ≠ 0 := by positivity
  have hsq : 1 - cayley x ^ 2 = (2 * x / (1 + x ^ 2)) ^ 2 := by
    unfold cayley
    field_simp
    ring
  rw [hsq, Real.sqrt_sq]
  exact div_nonneg (mul_nonneg (by norm_num) hx.1.le) (by positivity)

theorem log_cayley_ratio {x : ℝ} (hx : x ∈ Set.Ioo (0 : ℝ) 1) :
    Real.log (1 + cayley x) - Real.log (1 - cayley x) = -2 * Real.log x := by
  have hxp : 0 < x := hx.1
  have hd : 1 + x ^ 2 ≠ 0 := by positivity
  have hp : 1 + cayley x = 2 / (1 + x ^ 2) := by
    unfold cayley
    field_simp
    ring
  have hm : 1 - cayley x = (2 * x ^ 2) / (1 + x ^ 2) := by
    unfold cayley
    field_simp
    ring
  rw [hp, hm, Real.log_div (by norm_num : (2 : ℝ) ≠ 0) hd,
    Real.log_div (by positivity : 2 * x ^ 2 ≠ 0) hd,
    Real.log_mul (by norm_num : (2 : ℝ) ≠ 0) (by positivity : x ^ 2 ≠ 0),
    Real.log_pow]
  norm_num

theorem cayley_transformed_integrand {x : ℝ} (hx : x ∈ Set.Ioo (0 : ℝ) 1) :
    ((Real.log (1 + cayley x) - Real.log (1 - cayley x)) /
      Real.sqrt (1 - cayley x ^ 2)) * (-4 * x / (1 + x ^ 2) ^ 2) =
      -4 * (-Real.log x / (1 + x ^ 2)) := by
  rw [log_cayley_ratio hx, sqrt_one_sub_cayley_sq hx]
  have hx0 : x ≠ 0 := ne_of_gt hx.1
  have hd : 1 + x ^ 2 ≠ 0 := by positivity
  field_simp

theorem cayley_transformed_integrand_deriv {x : ℝ} (hx : x ∈ Set.Ioo (0 : ℝ) 1) :
    ((Real.log (1 + cayley x) - Real.log (1 - cayley x)) /
      Real.sqrt (1 - cayley x ^ 2)) * deriv cayley x =
      -4 * (-Real.log x / (1 + x ^ 2)) := by
  rw [(hasDerivAt_cayley x).deriv]
  exact cayley_transformed_integrand hx

theorem cayley_mem_Icc {x : ℝ} (hx : x ∈ Icc (0 : ℝ) 1) :
    cayley x ∈ Icc (0 : ℝ) 1 := by
  unfold cayley
  have hd : 0 < 1 + x ^ 2 := by positivity
  constructor
  · apply div_nonneg _ hd.le
    nlinarith [hx.1, hx.2]
  · apply (div_le_one hd).2
    nlinarith [sq_nonneg x]

theorem continuousOn_logMarginal00 :
    ContinuousOn Analysis.logMarginal00 (Ioo (0 : ℝ) 1) := by
  have hp : ContinuousOn (fun t : ℝ => Real.log (1 + t)) (Ioo (0 : ℝ) 1) :=
    (continuousOn_const.add continuousOn_id).log
      (by intro t ht; exact ne_of_gt (by dsimp only [id_eq]; linarith [ht.1]))
  have hm : ContinuousOn (fun t : ℝ => Real.log (1 - t)) (Ioo (0 : ℝ) 1) :=
    (continuousOn_const.sub continuousOn_id).log
      (by intro t ht; exact ne_of_gt (by dsimp only [id_eq]; linarith [ht.2]))
  exact (hp.sub hm).div
    (Real.continuous_sqrt.comp (continuous_const.sub (continuous_id.pow 2))).continuousOn
    (by
      intro t ht
      exact ne_of_gt (Real.sqrt_pos.mpr (by nlinarith [ht.1, ht.2])))

theorem transformed_logMarginal00 {x : ℝ} (hx : x ∈ Icc (0 : ℝ) 1) :
    Analysis.logMarginal00 (cayley x) * (-4 * x / (1 + x ^ 2) ^ 2) =
      -4 * (-Real.log x / (1 + x ^ 2)) := by
  by_cases hzero : x = 0
  · subst x
    norm_num [Analysis.logMarginal00]
  by_cases hone : x = 1
  · subst x
    norm_num [Analysis.logMarginal00]
  exact cayley_transformed_integrand ⟨lt_of_le_of_ne hx.1 (Ne.symm hzero),
    lt_of_le_of_ne hx.2 hone⟩

theorem intervalIntegrable_transformed_logMarginal00 :
    IntervalIntegrable
      (fun x : ℝ => Analysis.logMarginal00 (cayley x) * (-4 * x / (1 + x ^ 2) ^ 2))
      volume 0 1 := by
  apply (Constants.intervalIntegrable_catalan_kernel.const_mul (-4)).congr
  intro x hx
  rw [uIoc_of_le zero_le_one] at hx
  exact (transformed_logMarginal00 ⟨hx.1.le, hx.2⟩).symm

/-- The rational substitution is valid for the singular endpoint integral. -/
theorem integral_logMarginal00 :
    (∫ t in (0 : ℝ)..1, Analysis.logMarginal00 t) = 4 * Constants.catalan := by
  have himage : cayley '' Icc (0 : ℝ) 1 ⊆ Icc (0 : ℝ) 1 := by
    rintro t ⟨x, hx, rfl⟩
    exact cayley_mem_Icc hx
  have hinner : cayley '' Ioo (0 : ℝ) 1 ⊆ Ioo (0 : ℝ) 1 := by
    rintro t ⟨x, hx, rfl⟩
    exact cayley_mem_Ioo hx
  have hg1 : IntegrableOn Analysis.logMarginal00 (cayley '' uIcc (0 : ℝ) 1) := by
    rw [uIcc_of_le zero_le_one]
    exact ((intervalIntegrable_iff_integrableOn_Icc_of_le zero_le_one).mp
      Analysis.intervalIntegrable_logMarginal00).mono_set himage
  have hg2 : IntegrableOn
      (fun x : ℝ => (Analysis.logMarginal00 ∘ cayley) x * (-4 * x / (1 + x ^ 2) ^ 2))
      (uIcc (0 : ℝ) 1) := by
    rw [uIcc_of_le zero_le_one]
    exact (intervalIntegrable_iff_integrableOn_Icc_of_le zero_le_one).mp
      intervalIntegrable_transformed_logMarginal00
  have hsub := intervalIntegral.integral_comp_mul_deriv'''
    (a := (0 : ℝ)) (b := 1) (f := cayley)
    (f' := fun x : ℝ => -4 * x / (1 + x ^ 2) ^ 2)
    (g := Analysis.logMarginal00) continuous_cayley.continuousOn
    (by
      intro x _
      exact (hasDerivAt_cayley x).hasDerivWithinAt)
    (by
      simpa only [min_eq_left zero_le_one, max_eq_right zero_le_one]
        using continuousOn_logMarginal00.mono hinner)
    hg1 hg2
  have hleft :
      (∫ x in (0 : ℝ)..1,
        (Analysis.logMarginal00 ∘ cayley) x * (-4 * x / (1 + x ^ 2) ^ 2)) =
        -4 * Constants.catalan := by
    calc
      _ = ∫ x in (0 : ℝ)..1, -4 * (-Real.log x / (1 + x ^ 2)) := by
        apply intervalIntegral.integral_congr
        intro x hx
        rw [uIcc_of_le zero_le_one] at hx
        exact transformed_logMarginal00 hx
      _ = -4 * (∫ x in (0 : ℝ)..1, -Real.log x / (1 + x ^ 2)) :=
        intervalIntegral.integral_const_mul _ _
      _ = -4 * Constants.catalan := by rw [Constants.integral_catalan_kernel_interval]
  rw [cayley_zero, cayley_one] at hsub
  rw [hleft, intervalIntegral.integral_symm (a := (0 : ℝ)) (b := 1)
    (f := Analysis.logMarginal00)] at hsub
  linarith

end MixedMoments.BoundaryCatalan

namespace MixedMoments.Analysis

/-- The Catalan boundary value for the actual absolutely convergent double integral. -/
theorem M_zero_zero_eq_catalan : M 0 0 = 4 * Constants.catalan := by
  rw [M_zero_zero_eq_logIntegral, BoundaryCatalan.integral_logMarginal00]

end MixedMoments.Analysis
