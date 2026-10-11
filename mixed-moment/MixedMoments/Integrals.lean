import Mathlib
import MixedMoments.Rational
import MixedMoments.Series
import MixedMoments.RationalSeries

/-!
# Actual mixed-moment integrals

This file uses Lebesgue interval integrals. The endpoint values use Lean's total
division and square root; they do not affect the integral. No analytic identity
is built into the definitions.
-/

open MeasureTheory Set Filter
open scoped Interval Topology

namespace MixedMoments.Analysis

noncomputable def weight (t : ℝ) : ℝ := |t| / Real.sqrt (1 - t ^ 2)

noncomputable def moment (i : ℕ) : ℝ :=
  ∫ t in (-1 : ℝ)..1, weight t * t ^ i

noncomputable def kernel (i j : ℕ) (t s : ℝ) : ℝ :=
  weight t * t ^ i * s ^ j / (1 - t * s)

noncomputable def M (i j : ℕ) : ℝ :=
  ∫ t in (-1 : ℝ)..1, ∫ s in (0 : ℝ)..1, kernel i j t s

noncomputable def slice (i j : ℕ) (t : ℝ) : ℝ :=
  ∫ s in (0 : ℝ)..1, kernel i j t s

private theorem sqrt_sub_sq_pos {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) :
    0 < Real.sqrt (1 - t ^ 2) := by
  apply Real.sqrt_pos.2
  nlinarith [ht.1, ht.2]

private theorem hasDerivAt_neg_sqrt {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) :
    HasDerivAt (fun x : ℝ => -Real.sqrt (1 - x ^ 2))
      (t / Real.sqrt (1 - t ^ 2)) t := by
  have hsq : 1 - t ^ 2 ≠ 0 := by
    have := sqrt_sub_sq_pos ht
    exact ne_of_gt (Real.sqrt_pos.1 this)
  convert (((hasDerivAt_id t).pow 2).const_sub 1).sqrt hsq |>.neg using 1
  dsimp
  ring

theorem intervalIntegrable_positive_weight :
    IntervalIntegrable (fun t : ℝ => t / Real.sqrt (1 - t ^ 2)) volume 0 1 := by
  apply intervalIntegral.intervalIntegrable_deriv_of_nonneg
    (g := fun t : ℝ => -Real.sqrt (1 - t ^ 2))
  · exact (Real.continuous_sqrt.comp (continuous_const.sub (continuous_id.pow 2))).neg.continuousOn
  · simpa using fun t ht => hasDerivAt_neg_sqrt ht
  · intro t ht
    simp only [min_eq_left zero_le_one, max_eq_right zero_le_one] at ht
    exact div_nonneg ht.1.le (Real.sqrt_nonneg _)

theorem integral_positive_weight :
    (∫ t in (0 : ℝ)..1, t / Real.sqrt (1 - t ^ 2)) = 1 := by
  have h := intervalIntegral.integral_eq_sub_of_hasDerivAt_of_le zero_le_one
    (f := fun t : ℝ => -Real.sqrt (1 - t ^ 2))
    (f' := fun t : ℝ => t / Real.sqrt (1 - t ^ 2))
    (Real.continuous_sqrt.comp (continuous_const.sub (continuous_id.pow 2))).neg.continuousOn
    (fun t ht => hasDerivAt_neg_sqrt ht) intervalIntegrable_positive_weight
  simpa using h

theorem weight_neg (t : ℝ) : weight (-t) = weight t := by
  simp [weight]

theorem momentIntegrand_neg (i : ℕ) (t : ℝ) :
    weight (-t) * (-t) ^ i = (-1 : ℝ) ^ i * (weight t * t ^ i) := by
  rw [weight_neg, neg_pow]
  ring

theorem intervalIntegrable_weight : IntervalIntegrable weight volume (-1) 1 := by
  have hp : IntervalIntegrable weight volume 0 1 := by
    refine intervalIntegrable_positive_weight.congr ?_
    intro t ht
    rw [uIoc_of_le zero_le_one] at ht
    simp [weight, abs_of_nonneg ht.1.le]
  have hn : IntervalIntegrable weight volume (-1) 0 := by
    have h := ((IntervalIntegrable.iff_comp_neg (a := (0 : ℝ)) (b := 1)).mp hp).symm
    simpa only [neg_zero, weight_neg] using h
  exact hn.trans hp

theorem intervalIntegrable_moment (i : ℕ) :
    IntervalIntegrable (fun t : ℝ => weight t * t ^ i) volume (-1) 1 :=
  intervalIntegrable_weight.mul_continuousOn (continuous_id.pow i).continuousOn

theorem moment_reflection (i : ℕ) : moment i = (-1 : ℝ) ^ i * moment i := by
  have h := intervalIntegral.integral_comp_neg (a := (-1 : ℝ)) (b := 1)
    (fun t : ℝ => weight t * t ^ i)
  simp only [momentIntegrand_neg, intervalIntegral.integral_const_mul, neg_neg] at h
  exact h.symm

theorem moment_odd {i : ℕ} (hi : Odd i) : moment i = 0 := by
  have h := moment_reflection i
  rw [hi.neg_one_pow] at h
  linarith

noncomputable def positiveMoment (i : ℕ) : ℝ :=
  ∫ t in (0 : ℝ)..1, (t / Real.sqrt (1 - t ^ 2)) * t ^ i

theorem intervalIntegrable_positiveMoment (i : ℕ) :
    IntervalIntegrable (fun t : ℝ => (t / Real.sqrt (1 - t ^ 2)) * t ^ i)
      volume 0 1 :=
  intervalIntegrable_positive_weight.mul_continuousOn (continuous_id.pow i).continuousOn

theorem moment_eq_positiveMoment (i : ℕ) :
    moment i = (1 + (-1 : ℝ) ^ i) * positiveMoment i := by
  have hp : (∫ t in (0 : ℝ)..1, weight t * t ^ i) = positiveMoment i := by
    apply intervalIntegral.integral_congr
    intro t ht
    rw [uIcc_of_le zero_le_one] at ht
    simp [weight, abs_of_nonneg ht.1]
  have hn : (∫ t in (-1 : ℝ)..0, weight t * t ^ i) =
      (-1 : ℝ) ^ i * positiveMoment i := by
    have h := intervalIntegral.integral_comp_neg (a := (0 : ℝ)) (b := 1)
      (fun t : ℝ => weight t * t ^ i)
    simp only [momentIntegrand_neg, intervalIntegral.integral_const_mul, neg_zero] at h
    rw [← h, hp]
  have hsplit := intervalIntegral.integral_add_adjacent_intervals
    (a := (-1 : ℝ)) (b := 0) (c := 1)
    (intervalIntegrable_moment i |>.mono_set (by simp; intro t ht; exact ⟨ht.1, ht.2.trans zero_le_one⟩))
    (intervalIntegrable_moment i |>.mono_set (by simp; intro t ht; exact ⟨(by linarith [ht.1]), ht.2⟩))
  unfold moment
  rw [← hsplit, hn, hp]
  ring

@[simp] theorem positiveMoment_zero : positiveMoment 0 = 1 := by
  simpa [positiveMoment] using integral_positive_weight

theorem positiveMoment_nonneg (i : ℕ) : 0 ≤ positiveMoment i := by
  apply intervalIntegral.integral_nonneg zero_le_one
  intro t ht
  exact mul_nonneg (div_nonneg ht.1 (Real.sqrt_nonneg _)) (pow_nonneg ht.1 i)

@[simp] theorem moment_zero : moment 0 = 2 := by
  rw [moment_eq_positiveMoment]
  norm_num

private theorem hasDerivAt_moment_primitive (i : ℕ) {t : ℝ}
    (ht : t ∈ Ioo (0 : ℝ) 1) :
    HasDerivAt (fun x : ℝ => x ^ (i + 2) * Real.sqrt (1 - x ^ 2))
      (((i : ℝ) + 2) * ((t / Real.sqrt (1 - t ^ 2)) * t ^ i) -
        ((i : ℝ) + 3) * ((t / Real.sqrt (1 - t ^ 2)) * t ^ (i + 2))) t := by
  have hsqrt : Real.sqrt (1 - t ^ 2) ≠ 0 := (sqrt_sub_sq_pos ht).ne'
  have hd : HasDerivAt (fun x : ℝ => Real.sqrt (1 - x ^ 2))
      (-(t / Real.sqrt (1 - t ^ 2))) t := by
    convert (hasDerivAt_neg_sqrt ht).neg using 1
    funext x
    simp
  have h := ((hasDerivAt_id t).pow (i + 2)).mul
    hd
  convert h using 1
  simp only [id_eq, Pi.pow_apply, Nat.cast_add, Nat.cast_ofNat,
    show i + 2 - 1 = i + 1 by omega, mul_one]
  field_simp [hsqrt]
  have he := Real.sq_sqrt (Real.sqrt_pos.1 (sqrt_sub_sq_pos ht)).le
  rw [he]
  simp only [pow_add, pow_one]
  ring

theorem positiveMoment_recurrence (i : ℕ) :
    ((i : ℝ) + 3) * positiveMoment (i + 2) = ((i : ℝ) + 2) * positiveMoment i := by
  have hfirst := (intervalIntegrable_positiveMoment i).const_mul ((i : ℝ) + 2)
  have hsecond := (intervalIntegrable_positiveMoment (i + 2)).const_mul ((i : ℝ) + 3)
  have hint := hfirst.sub hsecond
  have h := intervalIntegral.integral_eq_sub_of_hasDerivAt_of_le zero_le_one
    (f := fun t : ℝ => t ^ (i + 2) * Real.sqrt (1 - t ^ 2))
    ((continuous_id.pow (i + 2)).mul
      (Real.continuous_sqrt.comp (continuous_const.sub (continuous_id.pow 2)))).continuousOn
    (fun t ht => hasDerivAt_moment_primitive i ht) hint
  rw [intervalIntegral.integral_sub hfirst hsecond] at h
  simp only [intervalIntegral.integral_const_mul] at h
  simp only [one_pow, sub_self, Real.sqrt_zero, mul_zero, zero_pow (by omega : i + 2 ≠ 0),
    zero_mul] at h
  change ((i : ℝ) + 2) * positiveMoment i - ((i : ℝ) + 3) * positiveMoment (i + 2) = 0 at h
  linarith

theorem moment_recurrence (i : ℕ) :
    ((i : ℝ) + 3) * moment (i + 2) = ((i : ℝ) + 2) * moment i := by
  rw [moment_eq_positiveMoment, moment_eq_positiveMoment]
  have hp := positiveMoment_recurrence i
  have hneg : (-1 : ℝ) ^ (i + 2) = (-1 : ℝ) ^ i := by simp [pow_add]
  rw [hneg]
  linear_combination (1 + (-1 : ℝ) ^ i) * hp

@[simp] theorem moment_one : moment 1 = 0 := moment_odd (by decide)

@[simp] theorem moment_two : moment 2 = 4 / 3 := by
  have h := moment_recurrence 0
  norm_num at h
  linarith

/-- The analytic single moments agree with the independently defined rational
sequence. This is a genuine link from integrals to the algebraic layer. -/
theorem moment_eq_rat (i : ℕ) : moment i = (MixedMoments.moment i : ℝ) := by
  induction i using Nat.twoStepInduction with
  | zero => norm_num
  | one => norm_num
  | more i hi _ =>
      have h := moment_recurrence i
      rw [MixedMoments.moment_step]
      push_cast
      rw [← hi]
      rw [eq_div_iff (by positivity : (i : ℝ) + 3 ≠ 0)]
      linarith

theorem moment_rational (i : ℕ) : ∃ q : ℚ, moment i = (q : ℝ) :=
  ⟨MixedMoments.moment i, moment_eq_rat i⟩

theorem weight_nonneg (t : ℝ) : 0 ≤ weight t :=
  div_nonneg (abs_nonneg _) (Real.sqrt_nonneg _)

noncomputable def absoluteMoment (i : ℕ) : ℝ :=
  ∫ t in (-1 : ℝ)..1, weight t * |t| ^ i

theorem intervalIntegrable_absoluteMoment (i : ℕ) :
    IntervalIntegrable (fun t : ℝ => weight t * |t| ^ i) volume (-1) 1 :=
  intervalIntegrable_weight.mul_continuousOn (continuous_abs.pow i).continuousOn

theorem absoluteMoment_eq (i : ℕ) : absoluteMoment i = 2 * positiveMoment i := by
  have hp : (∫ t in (0 : ℝ)..1, weight t * |t| ^ i) = positiveMoment i := by
    apply intervalIntegral.integral_congr
    intro t ht
    rw [uIcc_of_le zero_le_one] at ht
    simp [weight, abs_of_nonneg ht.1]
  have hn : (∫ t in (-1 : ℝ)..0, weight t * |t| ^ i) = positiveMoment i := by
    have h := intervalIntegral.integral_comp_neg (a := (0 : ℝ)) (b := 1)
      (fun t : ℝ => weight t * |t| ^ i)
    simp only [weight_neg, abs_neg, neg_zero] at h
    rw [← h, hp]
  have hsplit := intervalIntegral.integral_add_adjacent_intervals
    (a := (-1 : ℝ)) (b := 0) (c := 1)
    (intervalIntegrable_absoluteMoment i |>.mono_set
      (by simp; intro t ht; exact ⟨ht.1, ht.2.trans zero_le_one⟩))
    (intervalIntegrable_absoluteMoment i |>.mono_set
      (by simp; intro t ht; exact ⟨(by linarith [ht.1]), ht.2⟩))
  unfold absoluteMoment
  rw [← hsplit, hn, hp]
  ring

theorem absoluteMoment_nonneg (i : ℕ) : 0 ≤ absoluteMoment i := by
  rw [absoluteMoment_eq]
  exact mul_nonneg (by norm_num) (positiveMoment_nonneg i)

theorem absoluteMoment_recurrence (i : ℕ) :
    ((i : ℝ) + 3) * absoluteMoment (i + 2) = ((i : ℝ) + 2) * absoluteMoment i := by
  simp only [absoluteMoment_eq]
  linear_combination 2 * positiveMoment_recurrence i

theorem summable_absoluteMoment (i j : ℕ) :
    Summable (fun u : ℕ => absoluteMoment (i + u) / ((j : ℝ) + u + 1)) :=
  MixedMoments.Series.summable_momentSeries absoluteMoment absoluteMoment_nonneg
    absoluteMoment_recurrence i j

noncomputable def momentMeasure : Measure ℝ := volume.restrict (Ioo (-1) 1)

noncomputable def unitMeasure : Measure ℝ := volume.restrict (Ioo 0 1)

instance : IsFiniteMeasure momentMeasure := by
  unfold momentMeasure
  infer_instance

instance : IsFiniteMeasure unitMeasure := by
  unfold unitMeasure
  infer_instance

noncomputable def rectangleMeasure : Measure (ℝ × ℝ) := momentMeasure.prod unitMeasure

noncomputable def productKernel (i j : ℕ) (p : ℝ × ℝ) : ℝ := kernel i j p.1 p.2

noncomputable def monomial (i j u : ℕ) (p : ℝ × ℝ) : ℝ :=
  weight p.1 * p.1 ^ (i + u) * p.2 ^ (j + u)

noncomputable def absoluteMonomial (i j u : ℕ) (p : ℝ × ℝ) : ℝ :=
  weight p.1 * |p.1| ^ (i + u) * p.2 ^ (j + u)

theorem ae_mem_rectangle :
    ∀ᵐ p ∂rectangleMeasure, p.1 ∈ Ioo (-1 : ℝ) 1 ∧ p.2 ∈ Ioo (0 : ℝ) 1 := by
  unfold rectangleMeasure momentMeasure unitMeasure
  rw [Measure.prod_restrict]
  exact ae_restrict_mem (measurableSet_Ioo.prod measurableSet_Ioo)

theorem integrable_weight_pow (n : ℕ) :
    Integrable (fun t : ℝ => weight t * t ^ n) momentMeasure := by
  apply (intervalIntegrable_iff_integrableOn_Ioo_of_le (by norm_num : (-1 : ℝ) ≤ 1)).mp
  exact intervalIntegrable_moment n

theorem integrable_weight_abs_pow (n : ℕ) :
    Integrable (fun t : ℝ => weight t * |t| ^ n) momentMeasure := by
  apply (intervalIntegrable_iff_integrableOn_Ioo_of_le (by norm_num : (-1 : ℝ) ≤ 1)).mp
  exact intervalIntegrable_absoluteMoment n

theorem integrable_unit_pow (n : ℕ) : Integrable (fun s : ℝ => s ^ n) unitMeasure := by
  exact ((continuous_id.pow n).continuousOn.integrableOn_Icc
    (μ := volume) (a := (0 : ℝ)) (b := 1)).mono_set Ioo_subset_Icc_self

theorem integral_weight_pow (n : ℕ) :
    (∫ t, weight t * t ^ n ∂momentMeasure) = moment n := by
  unfold momentMeasure moment
  rw [← integral_Ioc_eq_integral_Ioo,
    ← intervalIntegral.integral_of_le (by norm_num : (-1 : ℝ) ≤ 1)]

theorem integral_weight_abs_pow (n : ℕ) :
    (∫ t, weight t * |t| ^ n ∂momentMeasure) = absoluteMoment n := by
  unfold momentMeasure absoluteMoment
  rw [← integral_Ioc_eq_integral_Ioo,
    ← intervalIntegral.integral_of_le (by norm_num : (-1 : ℝ) ≤ 1)]

theorem integral_unit_pow (n : ℕ) :
    (∫ s, s ^ n ∂unitMeasure) = 1 / ((n : ℝ) + 1) := by
  unfold unitMeasure
  rw [← integral_Ioc_eq_integral_Ioo,
    ← intervalIntegral.integral_of_le zero_le_one, integral_pow]
  simp

theorem integrable_monomial (i j u : ℕ) : Integrable (monomial i j u) rectangleMeasure :=
  (integrable_weight_pow (i + u)).mul_prod (integrable_unit_pow (j + u))

theorem integrable_absoluteMonomial (i j u : ℕ) :
    Integrable (absoluteMonomial i j u) rectangleMeasure :=
  (integrable_weight_abs_pow (i + u)).mul_prod (integrable_unit_pow (j + u))

theorem integral_monomial (i j u : ℕ) :
    (∫ p, monomial i j u p ∂rectangleMeasure) = moment (i + u) / ((j : ℝ) + u + 1) := by
  unfold monomial rectangleMeasure
  rw [integral_prod_mul (fun t : ℝ => weight t * t ^ (i + u))
    (fun s : ℝ => s ^ (j + u)), integral_weight_pow, integral_unit_pow]
  push_cast
  ring

theorem integral_absoluteMonomial (i j u : ℕ) :
    (∫ p, absoluteMonomial i j u p ∂rectangleMeasure) =
      absoluteMoment (i + u) / ((j : ℝ) + u + 1) := by
  unfold absoluteMonomial rectangleMeasure
  rw [integral_prod_mul (fun t : ℝ => weight t * |t| ^ (i + u))
    (fun s : ℝ => s ^ (j + u)), integral_weight_abs_pow, integral_unit_pow]
  push_cast
  ring

theorem ae_absoluteMonomial_nonneg (i j u : ℕ) :
    0 ≤ᵐ[rectangleMeasure] absoluteMonomial i j u := by
  filter_upwards [ae_mem_rectangle] with p hp
  exact mul_nonneg (mul_nonneg (weight_nonneg _) (pow_nonneg (abs_nonneg _) _))
    (pow_nonneg hp.2.1.le _)

theorem integral_norm_monomial (i j u : ℕ) :
    (∫ p, ‖monomial i j u p‖ ∂rectangleMeasure) =
      absoluteMoment (i + u) / ((j : ℝ) + u + 1) := by
  rw [← integral_absoluteMonomial]
  apply integral_congr_ae
  filter_upwards [ae_mem_rectangle] with p hp
  simp [monomial, absoluteMonomial, norm_mul, Real.norm_eq_abs,
    abs_of_nonneg (weight_nonneg _), abs_of_nonneg hp.2.1.le]

theorem summable_integral_norm_monomial (i j : ℕ) :
    Summable (fun u : ℕ => ∫ p, ‖monomial i j u p‖ ∂rectangleMeasure) := by
  simpa only [integral_norm_monomial] using summable_absoluteMoment i j

noncomputable def absoluteKernel (i j : ℕ) (p : ℝ × ℝ) : ℝ :=
  weight p.1 * |p.1| ^ i * p.2 ^ j / (1 - |p.1| * p.2)

private theorem abs_ratio_lt_one {p : ℝ × ℝ}
    (hp : p.1 ∈ Ioo (-1 : ℝ) 1 ∧ p.2 ∈ Ioo (0 : ℝ) 1) :
    |p.1| * p.2 < 1 := by
  have ht : |p.1| < 1 := abs_lt.2 hp.1
  have hm := mul_le_mul_of_nonneg_left hp.2.2.le (abs_nonneg p.1)
  nlinarith

theorem hasSum_monomial {p : ℝ × ℝ}
    (hp : p.1 ∈ Ioo (-1 : ℝ) 1 ∧ p.2 ∈ Ioo (0 : ℝ) 1) (i j : ℕ) :
    HasSum (fun u => monomial i j u p) (productKernel i j p) := by
  have hlt : |p.1 * p.2| < 1 := by
    simpa only [abs_mul, abs_of_nonneg hp.2.1.le] using abs_ratio_lt_one hp
  have hg := (hasSum_geometric_of_abs_lt_one hlt).mul_left
    (weight p.1 * p.1 ^ i * p.2 ^ j)
  convert hg using 1
  ext u
  simp only [monomial, pow_add, mul_pow]
  ring

theorem hasSum_absoluteMonomial {p : ℝ × ℝ}
    (hp : p.1 ∈ Ioo (-1 : ℝ) 1 ∧ p.2 ∈ Ioo (0 : ℝ) 1) (i j : ℕ) :
    HasSum (fun u => absoluteMonomial i j u p) (absoluteKernel i j p) := by
  have hlt : abs (|p.1| * p.2) < 1 := by
    rw [abs_of_nonneg (mul_nonneg (abs_nonneg _) hp.2.1.le)]
    exact abs_ratio_lt_one hp
  have hg := (hasSum_geometric_of_abs_lt_one hlt).mul_left
    (weight p.1 * |p.1| ^ i * p.2 ^ j)
  convert hg using 1
  ext u
  simp only [absoluteMonomial, pow_add, mul_pow]
  ring

theorem integrable_absoluteKernel (i j : ℕ) :
    Integrable (absoluteKernel i j) rectangleMeasure := by
  refine ⟨?_, ?_⟩
  · exact (by unfold absoluteKernel weight; fun_prop : Measurable (absoluteKernel i j)).aestronglyMeasurable
  · have hnn : 0 ≤ᵐ[rectangleMeasure] absoluteKernel i j := by
      filter_upwards [ae_mem_rectangle] with p hp
      exact (hasSum_absoluteMonomial hp i j).tsum_eq ▸ tsum_nonneg
        (fun u => mul_nonneg (mul_nonneg (weight_nonneg _) (pow_nonneg (abs_nonneg _) _))
          (pow_nonneg hp.2.1.le _))
    rw [hasFiniteIntegral_iff_ofReal hnn]
    have heq : (fun p => ENNReal.ofReal (absoluteKernel i j p)) =ᵐ[rectangleMeasure]
        (fun p => ∑' u, ENNReal.ofReal (absoluteMonomial i j u p)) := by
      filter_upwards [ae_mem_rectangle] with p hp
      rw [← (hasSum_absoluteMonomial hp i j).tsum_eq]
      exact ENNReal.ofReal_tsum_of_nonneg
        (fun u => mul_nonneg (mul_nonneg (weight_nonneg _) (pow_nonneg (abs_nonneg _) _))
          (pow_nonneg hp.2.1.le _)) (hasSum_absoluteMonomial hp i j).summable
    rw [lintegral_congr_ae heq, lintegral_tsum
      (fun u => (integrable_absoluteMonomial i j u).aestronglyMeasurable.aemeasurable.ennreal_ofReal)]
    have heach (u : ℕ) :
        (∫⁻ p, ENNReal.ofReal (absoluteMonomial i j u p) ∂rectangleMeasure) =
          ENNReal.ofReal (absoluteMoment (i + u) / ((j : ℝ) + u + 1)) := by
      rw [← ofReal_integral_eq_lintegral_ofReal (integrable_absoluteMonomial i j u)
        (ae_absoluteMonomial_nonneg i j u), integral_absoluteMonomial]
    simp_rw [heach]
    rw [← ENNReal.ofReal_tsum_of_nonneg
      (fun u => div_nonneg (absoluteMoment_nonneg _) (by positivity))
      (summable_absoluteMoment i j)]
    exact ENNReal.ofReal_lt_top

theorem norm_productKernel_le_absoluteKernel {p : ℝ × ℝ}
    (hp : p.1 ∈ Ioo (-1 : ℝ) 1 ∧ p.2 ∈ Ioo (0 : ℝ) 1) (i j : ℕ) :
    ‖productKernel i j p‖ ≤ absoluteKernel i j p := by
  have ha : 0 < 1 - |p.1| * p.2 := sub_pos.2 (abs_ratio_lt_one hp)
  have hle : 1 - |p.1| * p.2 ≤ 1 - p.1 * p.2 := by
    have h := mul_le_mul_of_nonneg_right (le_abs_self p.1) hp.2.1.le
    linarith
  have hd : 0 < 1 - p.1 * p.2 := ha.trans_le hle
  unfold productKernel kernel absoluteKernel
  simp only [Real.norm_eq_abs, abs_div, abs_mul, abs_pow,
    abs_of_nonneg (weight_nonneg _), abs_of_nonneg hp.2.1.le, abs_of_pos hd]
  exact div_le_div_of_nonneg_left
    (mul_nonneg (mul_nonneg (weight_nonneg _) (pow_nonneg (abs_nonneg _) _))
      (pow_nonneg hp.2.1.le _)) ha hle

/-- The singular-corner and negative-half convergence obligations are both
discharged by an integrable, absolutely summable geometric majorant. -/
theorem integrable_productKernel (i j : ℕ) : Integrable (productKernel i j) rectangleMeasure := by
  apply (integrable_absoluteKernel i j).mono'
    (by unfold productKernel kernel weight; fun_prop : Measurable (productKernel i j)).aestronglyMeasurable
  filter_upwards [ae_mem_rectangle] with p hp
  exact norm_productKernel_le_absoluteKernel hp i j

theorem intervalIntegrable_outer_slice (i j : ℕ) :
    IntervalIntegrable (slice i j) volume (-1) 1 := by
  have h := (integrable_productKernel i j).integral_prod_left
  simp_rw [unitMeasure, ← integral_Ioc_eq_integral_Ioo,
    ← intervalIntegral.integral_of_le zero_le_one] at h
  exact (intervalIntegrable_iff_integrableOn_Ioo_of_le (by norm_num : (-1 : ℝ) ≤ 1)).mpr h

theorem M_eq_productIntegral (i j : ℕ) :
    M i j = ∫ p, productKernel i j p ∂rectangleMeasure := by
  change M i j = ∫ p, productKernel i j p ∂momentMeasure.prod unitMeasure
  rw [integral_prod _ (integrable_productKernel i j)]
  simp_rw [momentMeasure, unitMeasure, ← integral_Ioc_eq_integral_Ioo,
    ← intervalIntegral.integral_of_le (by norm_num : (-1 : ℝ) ≤ 1),
    ← intervalIntegral.integral_of_le zero_le_one]
  rfl

theorem M_eq_swappedIntegral (i j : ℕ) :
    M i j = ∫ s in (0 : ℝ)..1, ∫ t in (-1 : ℝ)..1, kernel i j t s := by
  rw [M_eq_productIntegral]
  change (∫ p, productKernel i j p ∂momentMeasure.prod unitMeasure) = _
  rw [integral_prod_symm _ (integrable_productKernel i j)]
  simp_rw [momentMeasure, unitMeasure, ← integral_Ioc_eq_integral_Ioo,
    ← intervalIntegral.integral_of_le (by norm_num : (-1 : ℝ) ≤ 1),
    ← intervalIntegral.integral_of_le zero_le_one]
  rfl

/-- Actual integral-to-series identity, with absolute convergence rather than
pointwise convergence used to justify the interchange. -/
theorem M_eq_series (i j : ℕ) :
    M i j = ∑' u : ℕ, moment (i + u) / ((j : ℝ) + u + 1) := by
  rw [M_eq_productIntegral]
  calc
    (∫ p, productKernel i j p ∂rectangleMeasure) =
        ∫ p, (∑' u, monomial i j u p) ∂rectangleMeasure := by
      apply integral_congr_ae
      filter_upwards [ae_mem_rectangle] with p hp
      exact (hasSum_monomial hp i j).tsum_eq.symm
    _ = ∑' u, ∫ p, monomial i j u p ∂rectangleMeasure :=
      (integral_tsum_of_summable_integral_norm (integrable_monomial i j)
        (summable_integral_norm_monomial i j)).symm
    _ = ∑' u, moment (i + u) / ((j : ℝ) + u + 1) := by
      simp_rw [integral_monomial]

private theorem one_sub_mul_pos {t s : ℝ} (ht : t < 1) (hs : s ∈ Icc (0 : ℝ) 1) :
    0 < 1 - t * s := by
  by_cases hzero : s = 0
  · simp [hzero]
  have hspos : 0 < s := lt_of_le_of_ne hs.1 (Ne.symm hzero)
  have hmul : t * s < s := by simpa using mul_lt_mul_of_pos_right ht hspos
  linarith [hs.2]

theorem intervalIntegrable_slice (i j : ℕ) {t : ℝ} (ht : t ≤ 1) :
    IntervalIntegrable (kernel i j t) volume 0 1 := by
  rcases ht.eq_or_lt with h | h
  · subst t
    have hk : kernel i j 1 = fun _ => 0 := by
      funext s
      simp [kernel, weight]
    rw [hk]
    exact intervalIntegrable_const
  · apply ContinuousOn.intervalIntegrable
    refine (continuousOn_const.mul (continuous_id.pow j).continuousOn).div
      (continuousOn_const.sub (continuousOn_const.mul continuousOn_id)) ?_
    intro s hs
    rw [uIcc_of_le zero_le_one] at hs
    exact (one_sub_mul_pos h hs).ne'

theorem kernel_diagonal {i j : ℕ} {t s : ℝ} (ht : t ≤ 1)
    (hs : s ∈ Icc (0 : ℝ) 1) :
    kernel i j t s - kernel (i + 1) (j + 1) t s = weight t * t ^ i * s ^ j := by
  rcases ht.eq_or_lt with h | h
  · subst t
    simp [kernel, weight]
  · have hd := (one_sub_mul_pos h hs).ne'
    unfold kernel
    simp only [pow_succ]
    field_simp

theorem slice_diagonal (i j : ℕ) {t : ℝ} (ht : t ≤ 1) :
    slice i j t - slice (i + 1) (j + 1) t = weight t * t ^ i / ((j : ℝ) + 1) := by
  unfold slice
  rw [← intervalIntegral.integral_sub (intervalIntegrable_slice i j ht)
    (intervalIntegrable_slice (i + 1) (j + 1) ht)]
  calc
    (∫ s in (0 : ℝ)..1, kernel i j t s - kernel (i + 1) (j + 1) t s) =
        ∫ s in (0 : ℝ)..1, weight t * t ^ i * s ^ j := by
      apply intervalIntegral.integral_congr
      intro s hs
      rw [uIcc_of_le zero_le_one] at hs
      exact kernel_diagonal ht hs
    _ = weight t * t ^ i / ((j : ℝ) + 1) := by
      rw [intervalIntegral.integral_const_mul, integral_pow]
      simp [div_eq_mul_inv]

/-- The actual integral diagonal recurrence. The two hypotheses explicitly
retain the outer integrability obligation. Inner integrability and the kernel
identity are proved above rather than assumed. -/
theorem M_diagonal_of_intervalIntegrable (i j : ℕ)
    (hij : IntervalIntegrable (slice i j) volume (-1) 1)
    (hnext : IntervalIntegrable (slice (i + 1) (j + 1)) volume (-1) 1) :
    M i j - M (i + 1) (j + 1) = moment i / ((j : ℝ) + 1) := by
  change (∫ t in (-1 : ℝ)..1, slice i j t) -
    (∫ t in (-1 : ℝ)..1, slice (i + 1) (j + 1) t) = _
  rw [← intervalIntegral.integral_sub hij hnext]
  calc
    (∫ t in (-1 : ℝ)..1, slice i j t - slice (i + 1) (j + 1) t) =
        ∫ t in (-1 : ℝ)..1, weight t * t ^ i / ((j : ℝ) + 1) := by
      apply intervalIntegral.integral_congr
      intro t ht
      norm_num at ht
      exact slice_diagonal i j ht.2
    _ = moment i / ((j : ℝ) + 1) := by
      rw [intervalIntegral.integral_div]
      rfl

/-- Unconditional diagonal recurrence for the actual double integral. -/
theorem M_diagonal (i j : ℕ) :
    M i j - M (i + 1) (j + 1) = moment i / ((j : ℝ) + 1) :=
  M_diagonal_of_intervalIntegrable i j (intervalIntegrable_outer_slice i j)
    (intervalIntegrable_outer_slice (i + 1) (j + 1))

theorem M_finite_diagonal (i j N : ℕ) :
    M i j - M (i + N) (j + N) =
      ∑ k ∈ Finset.range N, moment (i + k) / ((j : ℝ) + k + 1) := by
  induction N with
  | zero => simp
  | succ N ih =>
      rw [Finset.sum_range_succ]
      have hs := M_diagonal (i + N) (j + N)
      have hi : i + (N + 1) = i + N + 1 := by omega
      have hj : j + (N + 1) = j + N + 1 := by omega
      rw [hi, hj]
      push_cast at hs
      rw [← ih, ← hs]
      ring

theorem moment_nonneg (i : ℕ) : 0 ≤ moment i := by
  rw [moment_eq_rat]
  exact_mod_cast MixedMoments.moment_nonneg i

theorem summable_momentSeries (i j : ℕ) :
    Summable (fun u : ℕ => moment (i + u) / ((j : ℝ) + u + 1)) :=
  MixedMoments.Series.summable_momentSeries moment moment_nonneg moment_recurrence i j

theorem M_eq_momentSeries (i j : ℕ) :
    M i j = MixedMoments.Series.momentSeries moment i j := M_eq_series i j

/-- The whole actual M integral is represented using the independently defined
rational single moments. Evaluation of its two boundary constants is separate. -/
theorem M_eq_rationalMomentSeries (i j : ℕ) :
    M i j = MixedMoments.Series.momentSeries (fun n => (MixedMoments.moment n : ℝ)) i j := by
  rw [M_eq_series]
  simp only [moment_eq_rat]
  rfl

theorem moment_tendsto_zero : Tendsto moment atTop (𝓝 0) := by
  convert MixedMoments.realMoment_tendsto_zero using 1
  funext i
  exact moment_eq_rat i

theorem M_minus_boundary_recurrence (d : ℕ) :
    ((d : ℝ) + 2) * M (d + 2) 0 =
      ((d : ℝ) + 1) * M d 0 + moment d + moment (d + 1) := by
  rw [M_eq_momentSeries, M_eq_momentSeries]
  exact MixedMoments.Series.minus_boundary_recurrence moment moment_recurrence
    moment_tendsto_zero d
    (by simpa using summable_momentSeries d 0)
    (by simpa using summable_momentSeries (d + 2) 0)

theorem M_plus_boundary_recurrence (d : ℕ) :
    ((d : ℝ) + 1) * M 0 (d + 2) =
      (d : ℝ) * M 0 d + 2 / ((d : ℝ) + 1) := by
  rw [M_eq_momentSeries, M_eq_momentSeries]
  exact MixedMoments.Series.plus_boundary_recurrence moment moment_recurrence
    moment_tendsto_zero moment_zero moment_one d
    (by simpa using summable_momentSeries 0 d)
    (by
      convert summable_momentSeries 0 (d + 2) using 1
      ext u
      simp only [Nat.zero_add, Nat.cast_add, Nat.cast_ofNat]
      congr 1
      ring)

@[simp] theorem M_zero_two : M 0 2 = 2 := by
  have h := M_plus_boundary_recurrence 0
  norm_num at h
  exact h

@[simp] theorem M_one_zero : M 1 0 = 2 := by
  have hs := summable_momentSeries 1 0
  simp only [Nat.cast_zero, zero_add] at hs
  have hterm (u : ℕ) : moment (1 + (u + 1)) / ((u + 1 : ℕ) + 1 : ℝ) =
      moment u - moment (u + 2) := by
    have h := MixedMoments.Series.moment_div_index moment moment_recurrence u
    rw [show 1 + (u + 1) = u + 2 by omega]
    push_cast
    convert h using 1
    ring
  have htail := (summable_nat_add_iff 1).mpr hs
  have hdiff : Summable (fun u => moment u - moment (u + 2)) := by
    simpa only [hterm] using htail
  have htel := MixedMoments.Series.tsum_two_step_telescope moment moment_tendsto_zero hdiff
  have hsum := hs.tsum_eq_zero_add
  simp only [Nat.cast_zero, Nat.add_zero, moment_one, zero_div, zero_add] at hsum
  simp only [hterm, moment_zero, moment_one, add_zero] at htel hsum
  rw [M_eq_series]
  simpa using hsum.trans htel

theorem M_two_zero : M 2 0 = 1 + M 0 0 / 2 := by
  have h := M_minus_boundary_recurrence 0
  norm_num at h
  linarith

noncomputable def pairedSlice01 (t : ℝ) : ℝ :=
  ∫ s in (0 : ℝ)..1,
    2 * (t / Real.sqrt (1 - t ^ 2)) * s / (1 - t ^ 2 * s ^ 2)

theorem kernel_zero_one_pair {t s : ℝ} (ht : t ∈ Icc (0 : ℝ) 1)
    (hs : s ∈ Icc (0 : ℝ) 1) :
    kernel 0 1 (-t) s + kernel 0 1 t s =
      2 * (t / Real.sqrt (1 - t ^ 2)) * s / (1 - t ^ 2 * s ^ 2) := by
  by_cases htop : t = 1
  · subst t
    simp [kernel, weight]
  have htlt : t < 1 := lt_of_le_of_ne ht.2 htop
  have hm := (one_sub_mul_pos htlt hs).ne'
  have hp : 1 + t * s ≠ 0 := ne_of_gt (by
    have hnonneg := mul_nonneg ht.1 hs.1
    linarith)
  have hd : 1 - t ^ 2 * s ^ 2 ≠ 0 := by
    have hmul : 1 - t ^ 2 * s ^ 2 = (1 - t * s) * (1 + t * s) := by ring
    rw [hmul]
    exact mul_ne_zero hm hp
  unfold kernel
  rw [weight_neg]
  simp only [pow_zero, pow_one, mul_one, neg_mul, sub_neg_eq_add, weight,
    abs_of_nonneg ht.1]
  field_simp
  ring

theorem slice_zero_one_pair {t : ℝ} (ht : t ∈ Icc (0 : ℝ) 1) :
    slice 0 1 (-t) + slice 0 1 t = pairedSlice01 t := by
  have hneg : -t ≤ 1 := by linarith [ht.1]
  unfold slice pairedSlice01
  rw [← intervalIntegral.integral_add (intervalIntegrable_slice 0 1 hneg)
    (intervalIntegrable_slice 0 1 ht.2)]
  apply intervalIntegral.integral_congr
  intro s hs
  rw [uIcc_of_le zero_le_one] at hs
  exact kernel_zero_one_pair ht hs

private theorem intervalIntegrable_negative_slice01 :
    IntervalIntegrable (slice 0 1) volume (-1) 0 := by
  apply (intervalIntegrable_outer_slice 0 1).mono_set
  norm_num
  intro t ht
  exact ⟨ht.1, ht.2.trans zero_le_one⟩

private theorem intervalIntegrable_positive_slice01 :
    IntervalIntegrable (slice 0 1) volume 0 1 := by
  apply (intervalIntegrable_outer_slice 0 1).mono_set
  norm_num
  intro t ht
  exact ⟨(by linarith [ht.1]), ht.2⟩

private theorem intervalIntegrable_reflected_slice01 :
    IntervalIntegrable (fun t : ℝ => slice 0 1 (-t)) volume 0 1 := by
  have h := ((IntervalIntegrable.iff_comp_neg (a := (-1 : ℝ)) (b := 0)).mp
    intervalIntegrable_negative_slice01).symm
  simpa only [neg_neg, neg_zero] using h

theorem intervalIntegrable_pairedSlice01 :
    IntervalIntegrable pairedSlice01 volume 0 1 := by
  apply (intervalIntegrable_reflected_slice01.add intervalIntegrable_positive_slice01).congr
  intro t ht
  rw [uIoc_of_le zero_le_one] at ht
  exact slice_zero_one_pair ⟨ht.1.le, ht.2⟩

theorem M_zero_one_eq_paired : M 0 1 = ∫ t in (0 : ℝ)..1, pairedSlice01 t := by
  have hsplit := intervalIntegral.integral_add_adjacent_intervals
    intervalIntegrable_negative_slice01 intervalIntegrable_positive_slice01
  have hn := intervalIntegral.integral_comp_neg (a := (0 : ℝ)) (b := 1) (slice 0 1)
  simp only [neg_zero] at hn
  change (∫ t in (-1 : ℝ)..1, slice 0 1 t) = _
  rw [← hsplit, ← hn,
    ← intervalIntegral.integral_add intervalIntegrable_reflected_slice01 intervalIntegrable_positive_slice01]
  apply intervalIntegral.integral_congr
  intro t ht
  rw [uIcc_of_le zero_le_one] at ht
  exact slice_zero_one_pair ht

noncomputable def pairedSlice00 (t : ℝ) : ℝ :=
  ∫ s in (0 : ℝ)..1,
    2 * (t / Real.sqrt (1 - t ^ 2)) / (1 - t ^ 2 * s ^ 2)

theorem kernel_zero_zero_pair {t s : ℝ} (ht : t ∈ Icc (0 : ℝ) 1)
    (hs : s ∈ Icc (0 : ℝ) 1) :
    kernel 0 0 (-t) s + kernel 0 0 t s =
      2 * (t / Real.sqrt (1 - t ^ 2)) / (1 - t ^ 2 * s ^ 2) := by
  by_cases htop : t = 1
  · subst t
    simp [kernel, weight]
  have htlt : t < 1 := lt_of_le_of_ne ht.2 htop
  have hm := (one_sub_mul_pos htlt hs).ne'
  have hp : 1 + t * s ≠ 0 := ne_of_gt (by
    have hnonneg := mul_nonneg ht.1 hs.1
    linarith)
  have hd : 1 - t ^ 2 * s ^ 2 ≠ 0 := by
    have hmul : 1 - t ^ 2 * s ^ 2 = (1 - t * s) * (1 + t * s) := by ring
    rw [hmul]
    exact mul_ne_zero hm hp
  unfold kernel
  rw [weight_neg]
  simp only [pow_zero, mul_one, neg_mul, sub_neg_eq_add, weight, abs_of_nonneg ht.1]
  field_simp
  ring

theorem slice_zero_zero_pair {t : ℝ} (ht : t ∈ Icc (0 : ℝ) 1) :
    slice 0 0 (-t) + slice 0 0 t = pairedSlice00 t := by
  have hneg : -t ≤ 1 := by linarith [ht.1]
  unfold slice pairedSlice00
  rw [← intervalIntegral.integral_add (intervalIntegrable_slice 0 0 hneg)
    (intervalIntegrable_slice 0 0 ht.2)]
  apply intervalIntegral.integral_congr
  intro s hs
  rw [uIcc_of_le zero_le_one] at hs
  exact kernel_zero_zero_pair ht hs

private theorem intervalIntegrable_negative_slice00 :
    IntervalIntegrable (slice 0 0) volume (-1) 0 := by
  apply (intervalIntegrable_outer_slice 0 0).mono_set
  norm_num
  intro t ht
  exact ⟨ht.1, ht.2.trans zero_le_one⟩

private theorem intervalIntegrable_positive_slice00 :
    IntervalIntegrable (slice 0 0) volume 0 1 := by
  apply (intervalIntegrable_outer_slice 0 0).mono_set
  norm_num
  intro t ht
  exact ⟨(by linarith [ht.1]), ht.2⟩

private theorem intervalIntegrable_reflected_slice00 :
    IntervalIntegrable (fun t : ℝ => slice 0 0 (-t)) volume 0 1 := by
  have h := ((IntervalIntegrable.iff_comp_neg (a := (-1 : ℝ)) (b := 0)).mp
    intervalIntegrable_negative_slice00).symm
  simpa only [neg_neg, neg_zero] using h

theorem intervalIntegrable_pairedSlice00 :
    IntervalIntegrable pairedSlice00 volume 0 1 := by
  apply (intervalIntegrable_reflected_slice00.add intervalIntegrable_positive_slice00).congr
  intro t ht
  rw [uIoc_of_le zero_le_one] at ht
  exact slice_zero_zero_pair ⟨ht.1.le, ht.2⟩

theorem M_zero_zero_eq_paired : M 0 0 = ∫ t in (0 : ℝ)..1, pairedSlice00 t := by
  have hsplit := intervalIntegral.integral_add_adjacent_intervals
    intervalIntegrable_negative_slice00 intervalIntegrable_positive_slice00
  have hn := intervalIntegral.integral_comp_neg (a := (0 : ℝ)) (b := 1) (slice 0 0)
  simp only [neg_zero] at hn
  change (∫ t in (-1 : ℝ)..1, slice 0 0 t) = _
  rw [← hsplit, ← hn,
    ← intervalIntegral.integral_add intervalIntegrable_reflected_slice00 intervalIntegrable_positive_slice00]
  apply intervalIntegral.integral_congr
  intro t ht
  rw [uIcc_of_le zero_le_one] at ht
  exact slice_zero_zero_pair ht

theorem slice_zero_zero_positive_eq_log {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) :
    slice 0 0 t = -Real.log (1 - t) / Real.sqrt (1 - t ^ 2) := by
  have htne : t ≠ 0 := ht.1.ne'
  have h := intervalIntegral.integral_comp_sub_mul (a := (0 : ℝ)) (b := 1)
    (fun x : ℝ => x⁻¹) ht.1.ne' 1
  simp only [mul_one, mul_zero, sub_zero, smul_eq_mul] at h
  rw [integral_inv_of_pos (by linarith [ht.2] : 0 < 1 - t) zero_lt_one] at h
  simp only [one_div, Real.log_inv] at h
  unfold slice kernel
  simp only [pow_zero, mul_one, div_eq_mul_inv]
  rw [intervalIntegral.integral_const_mul, h]
  simp only [weight, abs_of_pos ht.1]
  field_simp [htne]

theorem slice_zero_zero_negative_eq_log {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) :
    slice 0 0 (-t) = Real.log (1 + t) / Real.sqrt (1 - t ^ 2) := by
  have htne : t ≠ 0 := ht.1.ne'
  have h := intervalIntegral.integral_comp_add_mul (a := (0 : ℝ)) (b := 1)
    (fun x : ℝ => x⁻¹) ht.1.ne' 1
  simp only [mul_one, mul_zero, add_zero, smul_eq_mul] at h
  rw [integral_inv_of_pos zero_lt_one (by linarith [ht.1] : 0 < 1 + t)] at h
  simp only [div_one] at h
  unfold slice kernel
  rw [weight_neg]
  simp only [pow_zero, mul_one, neg_mul, sub_neg_eq_add, div_eq_mul_inv]
  rw [intervalIntegral.integral_const_mul, h]
  simp only [weight, abs_of_pos ht.1]
  field_simp [htne]

noncomputable def logMarginal00 (t : ℝ) : ℝ :=
  (Real.log (1 + t) - Real.log (1 - t)) / Real.sqrt (1 - t ^ 2)

theorem pairedSlice00_eq_log {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) :
    pairedSlice00 t = logMarginal00 t := by
  rw [← slice_zero_zero_pair ⟨ht.1.le, ht.2.le⟩,
    slice_zero_zero_positive_eq_log ht, slice_zero_zero_negative_eq_log ht]
  unfold logMarginal00
  ring

theorem intervalIntegrable_logMarginal00 :
    IntervalIntegrable logMarginal00 volume 0 1 := by
  rw [intervalIntegrable_iff_integrableOn_Ioo_of_le zero_le_one]
  refine ((intervalIntegrable_iff_integrableOn_Ioo_of_le zero_le_one).mp
    intervalIntegrable_pairedSlice00).congr_fun (fun t ht => pairedSlice00_eq_log ht)
      measurableSet_Ioo

theorem M_zero_zero_eq_logIntegral : M 0 0 = ∫ t in (0 : ℝ)..1, logMarginal00 t := by
  rw [M_zero_zero_eq_paired, intervalIntegral.integral_of_le zero_le_one,
    intervalIntegral.integral_of_le zero_le_one,
    integral_Ioc_eq_integral_Ioo, integral_Ioc_eq_integral_Ioo]
  apply setIntegral_congr_fun measurableSet_Ioo
  intro t ht
  exact pairedSlice00_eq_log ht

/-- A polynomial in the first variable and a monomial in the second. -/
noncomputable def columnKernel (P : Polynomial ℚ) (j : ℕ) (p : ℝ × ℝ) : ℝ :=
  weight p.1 * P.eval₂ (Rat.castHom ℝ) p.1 * p.2 ^ j / (1 - p.1 * p.2)

/-- The actual polynomial column of the M integral. -/
noncomputable def polynomialColumn (P : Polynomial ℚ) (j : ℕ) : ℝ :=
  ∫ p, columnKernel P j p ∂rectangleMeasure

theorem columnKernel_eq_sum (P : Polynomial ℚ) (j : ℕ) (p : ℝ × ℝ) :
    columnKernel P j p = ∑ i ∈ P.support, (P.coeff i : ℝ) * productKernel i j p := by
  unfold columnKernel
  rw [Polynomial.eval₂_eq_sum, Polynomial.sum_def, Finset.mul_sum,
    Finset.sum_mul, Finset.sum_div]
  apply Finset.sum_congr rfl
  intro i hi
  simp only [Rat.coe_castHom, productKernel, kernel]
  ring

theorem integrable_columnKernel (P : Polynomial ℚ) (j : ℕ) :
    Integrable (columnKernel P j) rectangleMeasure := by
  have heq : columnKernel P j =
      fun p => ∑ i ∈ P.support, (P.coeff i : ℝ) * productKernel i j p :=
    funext (columnKernel_eq_sum P j)
  rw [heq]
  exact integrable_finset_sum P.support (fun i _ =>
    (integrable_productKernel i j).const_mul (P.coeff i : ℝ))

/-- Finite expansion of a genuine polynomial integral, with every constituent
kernel already proved absolutely integrable. -/
theorem polynomialColumn_eq_sum (P : Polynomial ℚ) (j : ℕ) :
    polynomialColumn P j = ∑ i ∈ P.support, (P.coeff i : ℝ) * M i j := by
  unfold polynomialColumn
  simp_rw [columnKernel_eq_sum]
  rw [integral_finset_sum P.support (fun i _ =>
    (integrable_productKernel i j).const_mul (P.coeff i : ℝ))]
  simp only [integral_const_mul, ← M_eq_productIntegral]

theorem polynomialColumn_eq_iterated (P : Polynomial ℚ) (j : ℕ) :
    polynomialColumn P j = ∫ t in (-1 : ℝ)..1, ∫ s in (0 : ℝ)..1,
      weight t * P.eval₂ (Rat.castHom ℝ) t * s ^ j / (1 - t * s) := by
  unfold polynomialColumn rectangleMeasure
  rw [integral_prod _ (integrable_columnKernel P j)]
  simp_rw [momentMeasure, unitMeasure, ← integral_Ioc_eq_integral_Ioo,
    ← intervalIntegral.integral_of_le (by norm_num : (-1 : ℝ) ≤ 1),
    ← intervalIntegral.integral_of_le zero_le_one]
  rfl

/-- The source's actual polynomial kernel in both variables. -/
noncomputable def polynomialKernel (P Q : Polynomial ℚ) (p : ℝ × ℝ) : ℝ :=
  weight p.1 * P.eval₂ (Rat.castHom ℝ) p.1 * Q.eval₂ (Rat.castHom ℝ) p.2 /
    (1 - p.1 * p.2)

noncomputable def polynomialIntegral (P Q : Polynomial ℚ) : ℝ :=
  ∫ p, polynomialKernel P Q p ∂rectangleMeasure

theorem polynomialKernel_eq_sum (P Q : Polynomial ℚ) (p : ℝ × ℝ) :
    polynomialKernel P Q p = ∑ i ∈ P.support, ∑ j ∈ Q.support,
      ((P.coeff i : ℝ) * (Q.coeff j : ℝ)) * productKernel i j p := by
  unfold polynomialKernel
  simp only [Polynomial.eval₂_eq_sum, Polynomial.sum_def]
  rw [mul_assoc, Finset.sum_mul, Finset.mul_sum]
  simp_rw [Finset.mul_sum, Finset.sum_div]
  apply Finset.sum_congr rfl
  intro i hi
  apply Finset.sum_congr rfl
  intro j hj
  simp only [Rat.coe_castHom, productKernel, kernel]
  ring

theorem integrable_polynomialKernel (P Q : Polynomial ℚ) :
    Integrable (polynomialKernel P Q) rectangleMeasure := by
  have heq : polynomialKernel P Q = fun p =>
      ∑ i ∈ P.support, ∑ j ∈ Q.support,
        ((P.coeff i : ℝ) * (Q.coeff j : ℝ)) * productKernel i j p :=
    funext (polynomialKernel_eq_sum P Q)
  rw [heq]
  exact integrable_finset_sum P.support (fun i _ =>
    integrable_finset_sum Q.support (fun j _ =>
      (integrable_productKernel i j).const_mul ((P.coeff i : ℝ) * (Q.coeff j : ℝ))))

theorem polynomialIntegral_eq_sum (P Q : Polynomial ℚ) :
    polynomialIntegral P Q = ∑ i ∈ P.support, ∑ j ∈ Q.support,
      ((P.coeff i : ℝ) * (Q.coeff j : ℝ)) * M i j := by
  unfold polynomialIntegral
  simp_rw [polynomialKernel_eq_sum]
  rw [integral_finset_sum P.support (fun i _ =>
    integrable_finset_sum Q.support (fun j _ =>
      (integrable_productKernel i j).const_mul ((P.coeff i : ℝ) * (Q.coeff j : ℝ))))]
  congr 1
  ext i
  rw [integral_finset_sum Q.support (fun j _ =>
    (integrable_productKernel i j).const_mul ((P.coeff i : ℝ) * (Q.coeff j : ℝ)))]
  simp only [integral_const_mul, ← M_eq_productIntegral]

theorem polynomialIntegral_eq_iterated (P Q : Polynomial ℚ) :
    polynomialIntegral P Q = ∫ t in (-1 : ℝ)..1, ∫ s in (0 : ℝ)..1,
      weight t * P.eval₂ (Rat.castHom ℝ) t * Q.eval₂ (Rat.castHom ℝ) s /
        (1 - t * s) := by
  unfold polynomialIntegral rectangleMeasure
  rw [integral_prod _ (integrable_polynomialKernel P Q)]
  simp_rw [momentMeasure, unitMeasure, ← integral_Ioc_eq_integral_Ioo,
    ← intervalIntegral.integral_of_le (by norm_num : (-1 : ℝ) ≤ 1),
    ← intervalIntegral.integral_of_le zero_le_one]
  rfl

end MixedMoments.Analysis
