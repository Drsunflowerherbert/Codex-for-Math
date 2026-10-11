import MixedMoments.Rational
import MixedMoments.Series

/-! Convergence of the exact rational moments, after their canonical real cast.
This is a series theorem; it does not define the actual integrals. -/

namespace MixedMoments
open Filter
open scoped Topology

noncomputable def realMoment (n : ℕ) : ℝ := (moment n : ℝ)

theorem realMoment_nonneg (n : ℕ) : 0 ≤ realMoment n := by
  unfold realMoment
  exact_mod_cast moment_nonneg n

theorem realMoment_recurrence (n : ℕ) :
    ((n : ℝ) + 3) * realMoment (n + 2) = ((n : ℝ) + 2) * realMoment n := by
  unfold realMoment
  exact_mod_cast moment_recurrence n

theorem realMoment_tendsto_zero : Tendsto realMoment atTop (𝓝 0) := by
  have hb (n : ℕ) : (realMoment n) ^ 2 ≤ 8 / ((n : ℝ) + 2) := by
    unfold realMoment
    have h : ((moment n ^ 2 : ℚ) : ℝ) ≤ ((8 / ((n : ℚ) + 2) : ℚ) : ℝ) :=
      Rat.cast_le.mpr (moment_sq_le n)
    push_cast at h
    exact h
  have hinf : Tendsto (fun n : ℕ => (n : ℝ) + 2) atTop atTop := by
    exact tendsto_atTop_add_const_right _ 2 tendsto_natCast_atTop_atTop
  have hbound : Tendsto (fun n : ℕ => 8 / ((n : ℝ) + 2)) atTop (𝓝 0) :=
    tendsto_const_nhds.div_atTop hinf
  have hs := squeeze_zero (fun n => sq_nonneg (realMoment n)) hb hbound
  have ht := Real.continuous_sqrt.continuousAt.tendsto.comp hs
  simpa only [Function.comp_def, Real.sqrt_sq (realMoment_nonneg _), Real.sqrt_zero] using ht

theorem summable_realMoment (i j : ℕ) :
    Summable (fun u : ℕ => realMoment (i + u) / ((j : ℝ) + u + 1)) :=
  Series.summable_momentSeries realMoment realMoment_nonneg realMoment_recurrence i j

end MixedMoments
