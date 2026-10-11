import Mathlib.Analysis.Normed.Module.Basic
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Module
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Radial contact with the unit sphere

All results are over arbitrary real normed spaces; no completeness, dimension,
or convexity strengthening is assumed.
-/

namespace RadialContact

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- Unit directions, defined without assuming that the sphere is inhabited. -/
abbrev UnitSphere (E : Type*) [NormedAddCommGroup E] := {v : E // ‖v‖ = 1}

/-- A center strictly inside the unit ball. -/
abbrev InteriorCenter (E : Type*) [NormedAddCommGroup E] := {c : E // ‖c‖ < 1}

/-- The triangle inequality, written without dividing by a radius. This also
works for zero parameters and does not require unit directions. -/
theorem parameter_comparison {c v w : E} {r s : ℝ}
    (hr : 0 ≤ r) (hrs : r ≤ s)
    (hx : ‖c + r • v‖ = 1) (hy : ‖c + s • w‖ = 1) :
    (s - r) * (1 - ‖c‖) ≤ r * s * ‖v - w‖ := by
  have hs : 0 ≤ s := hr.trans hrs
  have hsr : 0 ≤ s - r := sub_nonneg.mpr hrs
  have hrs0 : 0 ≤ r * s := mul_nonneg hr hs
  have hid : s • (c + r • v) =
      r • (c + s • w) + (s - r) • c + (r * s) • (v - w) := by
    module
  have h : s ≤ r + (s - r) * ‖c‖ + (r * s) * ‖v - w‖ := by
    calc
      s = ‖s • (c + r • v)‖ := by
        simp only [norm_smul, Real.norm_eq_abs, abs_of_nonneg hs, hx, mul_one]
      _ = ‖r • (c + s • w) + (s - r) • c + (r * s) • (v - w)‖ := by rw [hid]
      _ ≤ ‖r • (c + s • w) + (s - r) • c‖ + ‖(r * s) • (v - w)‖ := norm_add_le _ _
      _ ≤ ‖r • (c + s • w)‖ + ‖(s - r) • c‖ + ‖(r * s) • (v - w)‖ :=
        add_le_add_right (norm_add_le _ _) _
      _ = r + (s - r) * ‖c‖ + (r * s) * ‖v - w‖ := by
        simp only [norm_smul, Real.norm_eq_abs, abs_of_nonneg hr,
          abs_of_nonneg hsr, abs_of_nonneg hrs0, hy, mul_one]
  nlinarith

/-- Absolute-value version of the comparison estimate. -/
theorem parameter_abs_comparison {c v w : E} {r s : ℝ}
    (hr : 0 ≤ r) (hs : 0 ≤ s)
    (hx : ‖c + r • v‖ = 1) (hy : ‖c + s • w‖ = 1) :
    |r - s| * (1 - ‖c‖) ≤ r * s * ‖v - w‖ := by
  rcases le_total r s with hrs | hsr
  · have h := parameter_comparison hr hrs hx hy
    simpa only [abs_of_nonpos (sub_nonpos.mpr hrs), neg_sub] using h
  · have h := parameter_comparison hs hsr hy hx
    rw [abs_of_nonneg (sub_nonneg.mpr hsr), mul_comm r s, norm_sub_rev]
    exact h

/-- Positive sphere contact is unique, including for norms with flat faces. -/
theorem positive_contact_unique {c v : E} (hc : ‖c‖ < 1) {r s : ℝ}
    (hr : 0 < r) (hs : 0 < s)
    (hx : ‖c + r • v‖ = 1) (hy : ‖c + s • v‖ = 1) : r = s := by
  have h := parameter_abs_comparison hr.le hs.le hx hy
  simp only [sub_self, norm_zero, mul_zero] at h
  have hq : 0 < 1 - ‖c‖ := sub_pos.mpr hc
  have hle : |r - s| ≤ 0 := (mul_le_mul_iff_left₀ hq).mp (by simpa using h)
  have : |r - s| = 0 := le_antisymm hle (abs_nonneg _)
  exact sub_eq_zero.mp (abs_eq_zero.mp this)

/-- The universal radius interval. -/
theorem positive_contact_bounds {c v : E} (hv : ‖v‖ = 1) {r : ℝ}
    (hr : 0 ≤ r) (hx : ‖c + r • v‖ = 1) :
    1 - ‖c‖ ≤ r ∧ r ≤ 1 + ‖c‖ := by
  have hn : ‖r • v‖ = r := by
    simp [norm_smul, Real.norm_eq_abs, abs_of_nonneg hr, hv]
  have h₁ := norm_add_le c (r • v)
  have h₂ := norm_sub_le (c + r • v) c
  have hid : c + r • v - c = r • v := by abel
  rw [hx, hn] at h₁
  rw [hid, hn, hx] at h₂
  constructor <;> linarith

/-- Existence uses a real compact interval, not compactness or completeness of E. -/
theorem exists_positive_contact {c v : E} (hc : ‖c‖ < 1) (hv : ‖v‖ = 1) :
    ∃ r : ℝ, 0 < r ∧ ‖c + r • v‖ = 1 := by
  have hb : 0 ≤ 1 + ‖c‖ := by positivity
  have hf : Continuous (fun r : ℝ => ‖c + r • v‖) :=
    (continuous_const.add (continuous_id.smul continuous_const)).norm
  have h₀ : ‖c + (0 : ℝ) • v‖ ≤ 1 := by simpa using hc.le
  have h₁ : 1 ≤ ‖c + (1 + ‖c‖) • v‖ := by
    have h := norm_sub_le (c + (1 + ‖c‖) • v) c
    have hid : c + (1 + ‖c‖) • v - c = (1 + ‖c‖) • v := by abel
    rw [hid, norm_smul, hv, Real.norm_eq_abs, abs_of_nonneg hb, mul_one] at h
    linarith
  obtain ⟨r, hr, hx⟩ := intermediate_value_Icc hb hf.continuousOn ⟨h₀, h₁⟩
  refine ⟨r, ?_, hx⟩
  have hl := (positive_contact_bounds hv hr.1 hx).1
  linarith

/-- Exactly one positive contact radius exists for each unit direction. -/
theorem existsUnique_positive_contact {c v : E} (hc : ‖c‖ < 1) (hv : ‖v‖ = 1) :
    ∃! r : ℝ, 0 < r ∧ ‖c + r • v‖ = 1 := by
  obtain ⟨r, hr, hx⟩ := exists_positive_contact hc hv
  exact ⟨r, ⟨hr, hx⟩, fun s hs => positive_contact_unique hc hs.1 hr hs.2 hx⟩

end RadialContact
