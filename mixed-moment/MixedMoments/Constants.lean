import Mathlib
import MixedMoments.Zeta

/-! Actual logarithmic integral representations for the constants.
These identities alone do not identify the M boundary integrals with them. -/

noncomputable section
open MeasureTheory Set Filter Finset
open scoped Topology
namespace MixedMoments.Constants

def logMoment (n : ℕ) (x : ℝ) : ℝ := x ^ n * (-Real.log x)

def logPrimitive (n : ℕ) (x : ℝ) : ℝ :=
  x ^ n * (x * Real.log x) / ((n : ℝ) + 1) -
    x ^ (n + 1) / ((n : ℝ) + 1) ^ 2

theorem continuous_logPrimitive (n : ℕ) : Continuous (logPrimitive n) :=
  ((continuous_id.pow n).mul Real.continuous_mul_log).div_const _ |>.sub
    ((continuous_id.pow (n + 1)).div_const _)

theorem hasDerivAt_logPrimitive (n : ℕ) {x : ℝ} (hx : 0 < x) :
    HasDerivAt (logPrimitive n) (x ^ n * Real.log x) x := by
  have hn : (n : ℝ) + 1 ≠ 0 := by positivity
  have hx0 : x ≠ 0 := ne_of_gt hx
  have hpow := (hasDerivAt_id x).pow (n + 1)
  have hlog := Real.hasDerivAt_log hx0
  have h := (hpow.mul hlog).div_const ((n : ℝ) + 1) |>.sub
    (hpow.div_const (((n : ℝ) + 1) ^ 2))
  convert h using 1
  · ext t
    dsimp only [Pi.mul_apply, Pi.pow_apply, Pi.sub_apply, id_eq]
    unfold logPrimitive
    rw [pow_succ]
    ring
  · simp only [Nat.cast_add, Nat.cast_one, Nat.add_sub_cancel, mul_one]
    dsimp only [Pi.mul_apply, Pi.pow_apply, Pi.sub_apply, id_eq]
    rw [pow_succ]
    field_simp
    ring

theorem intervalIntegrable_logMoment (n : ℕ) :
    IntervalIntegrable (logMoment n) volume 0 1 := by
  exact intervalIntegral.intervalIntegrable_log'.neg.continuousOn_mul
    (continuous_id.pow n).continuousOn

theorem integral_logMoment (n : ℕ) :
    (∫ x in (0 : ℝ)..1, logMoment n x) = 1 / ((n : ℝ) + 1) ^ 2 := by
  have hint : IntervalIntegrable (fun x : ℝ => x ^ n * Real.log x) volume 0 1 :=
    intervalIntegral.intervalIntegrable_log'.continuousOn_mul (continuous_id.pow n).continuousOn
  have h := intervalIntegral.integral_eq_sub_of_hasDerivAt_of_le zero_le_one
    (continuous_logPrimitive n).continuousOn
    (fun x hx => hasDerivAt_logPrimitive n hx.1) hint
  have he : logMoment n = fun x : ℝ => -(x ^ n * Real.log x) := by
    ext x
    simp [logMoment]
  rw [he, intervalIntegral.integral_neg, h]
  simp [logPrimitive, zero_pow (by omega : n + 1 ≠ 0)]

def unitMeasure : Measure ℝ := volume.restrict (Ioo 0 1)

theorem ae_mem_unit : ∀ᵐ x ∂unitMeasure, x ∈ Ioo (0 : ℝ) 1 :=
  ae_restrict_mem measurableSet_Ioo

theorem logMoment_nonneg {x : ℝ} (hx : x ∈ Ioo (0 : ℝ) 1) (n : ℕ) :
    0 ≤ logMoment n x :=
  mul_nonneg (pow_nonneg hx.1.le _) (neg_nonneg.mpr (Real.log_nonpos hx.1.le hx.2.le))

theorem integrable_logMoment (n : ℕ) : Integrable (logMoment n) unitMeasure :=
  (intervalIntegrable_logMoment n).1.mono_set Ioo_subset_Ioc_self

theorem integral_logMoment_unit (n : ℕ) :
    (∫ x, logMoment n x ∂unitMeasure) = 1 / ((n : ℝ) + 1) ^ 2 := by
  unfold unitMeasure
  rw [← integral_Ioc_eq_integral_Ioo,
    ← intervalIntegral.integral_of_le zero_le_one, integral_logMoment]

/-- Catalan's constant, defined by its usual absolutely convergent series. -/
def catalan : ℝ := ∑' n : ℕ, (-1 : ℝ) ^ n / ((2 * n : ℕ) + 1 : ℝ) ^ 2

def catalanTerm (n : ℕ) (x : ℝ) : ℝ := (-1 : ℝ) ^ n * logMoment (2 * n) x

def zetaLogKernel (x : ℝ) : ℝ := -Real.log x / (1 - x ^ 2)

theorem summable_odd_reciprocal_sq :
    Summable (fun n : ℕ => 1 / ((2 * n : ℕ) + 1 : ℝ) ^ 2) := by
  have h := (Real.summable_one_div_nat_pow.mpr (by decide : 1 < 2)).comp_injective
    (show Function.Injective (fun n : ℕ => 2 * n + 1) by intro a b h; dsimp at h; omega)
  simpa only [Function.comp_def, Nat.cast_add, Nat.cast_one] using h

theorem integral_catalanTerm (n : ℕ) :
    (∫ x, catalanTerm n x ∂unitMeasure) = (-1 : ℝ) ^ n / ((2 * n : ℕ) + 1 : ℝ) ^ 2 := by
  simp only [catalanTerm, integral_const_mul, integral_logMoment_unit]
  ring

theorem integral_norm_catalanTerm (n : ℕ) :
    (∫ x, ‖catalanTerm n x‖ ∂unitMeasure) = 1 / ((2 * n : ℕ) + 1 : ℝ) ^ 2 := by
  rw [← integral_logMoment_unit]
  apply integral_congr_ae
  filter_upwards [ae_mem_unit] with x hx
  simp [catalanTerm, norm_mul, norm_pow, Real.norm_of_nonneg (logMoment_nonneg hx _)]

theorem hasSum_catalanTerm {x : ℝ} (hx : x ∈ Ioo (0 : ℝ) 1) :
    HasSum (fun n => catalanTerm n x) (-Real.log x / (1 + x ^ 2)) := by
  have hh : |-(x ^ 2)| < 1 := by
    rw [abs_neg, abs_of_nonneg (sq_nonneg _)]
    nlinarith [hx.1, hx.2]
  have h := (hasSum_geometric_of_abs_lt_one hh).mul_left (-Real.log x)
  convert h using 1
  · ext n
    simp only [catalanTerm, logMoment]
    rw [show (-x ^ 2) ^ n = (-1 : ℝ) ^ n * (x ^ 2) ^ n by rw [neg_pow]]
    simp only [← pow_mul]
    ring
  · simp only [sub_neg_eq_add, div_eq_mul_inv]

theorem integral_catalan_kernel :
    (∫ x, -Real.log x / (1 + x ^ 2) ∂unitMeasure) = catalan := by
  have hn : Summable (fun n => ∫ x, ‖catalanTerm n x‖ ∂unitMeasure) := by
    simpa only [integral_norm_catalanTerm] using summable_odd_reciprocal_sq
  calc
    (∫ x, -Real.log x / (1 + x ^ 2) ∂unitMeasure) =
        ∫ x, ∑' n, catalanTerm n x ∂unitMeasure := by
      apply integral_congr_ae
      filter_upwards [ae_mem_unit] with x hx
      exact (hasSum_catalanTerm hx).tsum_eq.symm
    _ = ∑' n, ∫ x, catalanTerm n x ∂unitMeasure :=
      (integral_tsum_of_summable_integral_norm
        (fun n => (integrable_logMoment (2 * n)).const_mul _) hn).symm
    _ = catalan := by simp only [catalan, integral_catalanTerm]

theorem integrable_catalan_kernel :
    Integrable (fun x : ℝ => -Real.log x / (1 + x ^ 2)) unitMeasure := by
  apply (integrable_logMoment 0).mono'
    (by fun_prop : Measurable (fun x : ℝ => -Real.log x / (1 + x ^ 2))).aestronglyMeasurable
  filter_upwards [ae_mem_unit] with x hx
  have hlog : 0 ≤ -Real.log x := neg_nonneg.mpr (Real.log_nonpos hx.1.le hx.2.le)
  rw [Real.norm_of_nonneg (div_nonneg hlog (by positivity))]
  simpa [logMoment] using div_le_self hlog (show (1 : ℝ) ≤ 1 + x ^ 2 by nlinarith)

theorem hasSum_logEven {x : ℝ} (hx : x ∈ Ioo (0 : ℝ) 1) :
    HasSum (fun n => logMoment (2 * n) x) (zetaLogKernel x) := by
  have hh : |x ^ 2| < 1 := by
    rw [abs_of_nonneg (sq_nonneg _)]
    nlinarith [hx.1, hx.2]
  have h := (hasSum_geometric_of_abs_lt_one hh).mul_left (-Real.log x)
  convert h using 1
  · ext n
    simp only [logMoment, pow_mul]
    ring

theorem integrable_zetaLogKernel : Integrable zetaLogKernel unitMeasure := by
  have hnn : 0 ≤ᵐ[unitMeasure] zetaLogKernel := by
    filter_upwards [ae_mem_unit] with x hx
    exact (hasSum_logEven hx).tsum_eq ▸ tsum_nonneg (fun n => logMoment_nonneg hx _)
  refine ⟨(by unfold zetaLogKernel; fun_prop : Measurable zetaLogKernel).aestronglyMeasurable, ?_⟩
  rw [hasFiniteIntegral_iff_ofReal hnn]
  have heq : (fun x => ENNReal.ofReal (zetaLogKernel x)) =ᵐ[unitMeasure]
      (fun x => ∑' n, ENNReal.ofReal (logMoment (2 * n) x)) := by
    filter_upwards [ae_mem_unit] with x hx
    rw [← (hasSum_logEven hx).tsum_eq]
    exact ENNReal.ofReal_tsum_of_nonneg (fun n => logMoment_nonneg hx _)
      (hasSum_logEven hx).summable
  rw [lintegral_congr_ae heq, lintegral_tsum
    (fun n => (integrable_logMoment (2 * n)).aestronglyMeasurable.aemeasurable.ennreal_ofReal)]
  have heach (n : ℕ) : (∫⁻ x, ENNReal.ofReal (logMoment (2 * n) x) ∂unitMeasure) =
      ENNReal.ofReal (1 / ((2 * n : ℕ) + 1 : ℝ) ^ 2) := by
    rw [← ofReal_integral_eq_lintegral_ofReal (integrable_logMoment (2 * n))
      (ae_mem_unit.mono (fun x hx => logMoment_nonneg hx _)), integral_logMoment_unit]
  simp_rw [heach]
  rw [← ENNReal.ofReal_tsum_of_nonneg (fun n => by positivity) summable_odd_reciprocal_sq]
  exact ENNReal.ofReal_lt_top

theorem integral_zetaLogKernel_series :
    (∫ x, zetaLogKernel x ∂unitMeasure) = ∑' n : ℕ, 1 / ((2 * n : ℕ) + 1 : ℝ) ^ 2 := by
  have hn : Summable (fun n => ∫ x, ‖logMoment (2 * n) x‖ ∂unitMeasure) := by
    convert summable_odd_reciprocal_sq using 1
    ext n
    rw [← integral_logMoment_unit]
    apply integral_congr_ae
    filter_upwards [ae_mem_unit] with x hx
    exact Real.norm_of_nonneg (logMoment_nonneg hx _)
  calc
    (∫ x, zetaLogKernel x ∂unitMeasure) =
        ∫ x, ∑' n, logMoment (2 * n) x ∂unitMeasure := by
      apply integral_congr_ae
      filter_upwards [ae_mem_unit] with x hx
      exact (hasSum_logEven hx).tsum_eq.symm
    _ = ∑' n, ∫ x, logMoment (2 * n) x ∂unitMeasure :=
      (integral_tsum_of_summable_integral_norm (fun n => integrable_logMoment (2 * n)) hn).symm
    _ = ∑' n : ℕ, 1 / ((2 * n : ℕ) + 1 : ℝ) ^ 2 := by simp_rw [integral_logMoment_unit]

theorem intervalIntegrable_zetaLogKernel : IntervalIntegrable zetaLogKernel volume 0 1 :=
  (intervalIntegrable_iff_integrableOn_Ioo_of_le zero_le_one).mpr integrable_zetaLogKernel

theorem odd_reciprocal_sq_eq :
    (∑' n : ℕ, 1 / ((2 * n : ℕ) + 1 : ℝ) ^ 2) = (3 / 4 : ℝ) * Zeta.zeta2 := by
  have he : Summable (fun n : ℕ => 1 / (((2 * n + 1 : ℕ) : ℝ) ^ 2)) := by
    simpa only [Nat.cast_add, Nat.cast_one] using summable_odd_reciprocal_sq
  have ho : Summable (fun n : ℕ => 1 / (((2 * n + 1 + 1 : ℕ) : ℝ) ^ 2)) := by
    have h := Zeta.summable_zeta2.comp_injective
      (show Function.Injective (fun n : ℕ => 2 * n + 1) by intro a b h; dsimp at h; omega)
    exact h
  have hsplit := tsum_even_add_odd (f := fun n : ℕ => 1 / (((n + 1 : ℕ) : ℝ) ^ 2)) he ho
  have hterm (n : ℕ) : 1 / (((2 * n + 1 + 1 : ℕ) : ℝ) ^ 2) =
      (1 / 4 : ℝ) * (1 / (((n + 1 : ℕ) : ℝ) ^ 2)) := by
    push_cast
    have hn : (n : ℝ) + 1 ≠ 0 := by positivity
    have hn' : 2 * (n : ℝ) + 1 + 1 ≠ 0 := by positivity
    field_simp
    ring
  simp_rw [hterm] at hsplit
  rw [tsum_mul_left] at hsplit
  change (∑' n : ℕ, 1 / (((2 * n + 1 : ℕ) : ℝ) ^ 2)) +
    (1 / 4 : ℝ) * Zeta.zeta2 = Zeta.zeta2 at hsplit
  simp only [Nat.cast_add, Nat.cast_one] at hsplit
  linarith

theorem integral_zetaLogKernel :
    (∫ x in (0 : ℝ)..1, zetaLogKernel x) = (3 / 4 : ℝ) * Zeta.zeta2 := by
  rw [intervalIntegral.integral_of_le zero_le_one, integral_Ioc_eq_integral_Ioo]
  change (∫ x, zetaLogKernel x ∂unitMeasure) = _
  rw [integral_zetaLogKernel_series, odd_reciprocal_sq_eq]

theorem intervalIntegrable_catalan_kernel :
    IntervalIntegrable (fun x : ℝ => -Real.log x / (1 + x ^ 2)) volume 0 1 :=
  (intervalIntegrable_iff_integrableOn_Ioo_of_le zero_le_one).mpr integrable_catalan_kernel

theorem integral_catalan_kernel_interval :
    (∫ x in (0 : ℝ)..1, -Real.log x / (1 + x ^ 2)) = catalan := by
  rw [intervalIntegral.integral_of_le zero_le_one, integral_Ioc_eq_integral_Ioo]
  exact integral_catalan_kernel

end MixedMoments.Constants
