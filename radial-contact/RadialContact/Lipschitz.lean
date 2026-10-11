import RadialContact.Basic
import Mathlib.Topology.MetricSpace.Lipschitz
import Mathlib.Tactic.FieldSimp

/-! # Radius and contact maps, with the requested quantitative estimates -/

namespace RadialContact

open scoped NNReal

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- The unique positive radius. Its domain can be empty. -/
noncomputable def radius (c : InteriorCenter E) (v : UnitSphere E) : ℝ :=
  Classical.choose (exists_positive_contact c.property v.property)

theorem radius_pos (c : InteriorCenter E) (v : UnitSphere E) : 0 < radius c v :=
  (Classical.choose_spec (exists_positive_contact c.property v.property)).1

theorem norm_contact (c : InteriorCenter E) (v : UnitSphere E) :
    ‖(c : E) + radius c v • (v : E)‖ = 1 :=
  (Classical.choose_spec (exists_positive_contact c.property v.property)).2

theorem radius_bounds (c : InteriorCenter E) (v : UnitSphere E) :
    1 - ‖(c : E)‖ ≤ radius c v ∧ radius c v ≤ 1 + ‖(c : E)‖ :=
  positive_contact_bounds v.property (radius_pos c v).le (norm_contact c v)

theorem radius_eq_of_contact (c : InteriorCenter E) (v : UnitSphere E)
    {r : ℝ} (hr : 0 < r) (hx : ‖(c : E) + r • (v : E)‖ = 1) :
    radius c v = r :=
  positive_contact_unique c.property (radius_pos c v) hr (norm_contact c v) hx

/-- Contact with the unit sphere along the ray from c in direction v. -/
noncomputable def contact (c : InteriorCenter E) (v : UnitSphere E) : UnitSphere E :=
  ⟨(c : E) + radius c v • (v : E), norm_contact c v⟩

@[simp] theorem contact_val (c : InteriorCenter E) (v : UnitSphere E) :
    (contact c v : E) = (c : E) + radius c v • (v : E) := rfl

/-- A stronger intermediate estimate retaining the two individual radii. -/
theorem radius_mul_gap_le (c : InteriorCenter E) (v w : UnitSphere E) :
    |radius c v - radius c w| * (1 - ‖(c : E)‖) ≤
      radius c v * radius c w * ‖(v : E) - (w : E)‖ :=
  parameter_abs_comparison (radius_pos c v).le (radius_pos c w).le
    (norm_contact c v) (norm_contact c w)

/-- The radius Lipschitz estimate requested in the mathematical specification. -/
theorem radius_dist_le (c : InteriorCenter E) (v w : UnitSphere E) :
    |radius c v - radius c w| ≤
      ((1 + ‖(c : E)‖) ^ 2 / (1 - ‖(c : E)‖)) * ‖(v : E) - (w : E)‖ := by
  have hq : 0 < 1 - ‖(c : E)‖ := sub_pos.mpr c.property
  have hp : radius c v * radius c w ≤ (1 + ‖(c : E)‖) ^ 2 := by
    calc
      radius c v * radius c w ≤ (1 + ‖(c : E)‖) * (1 + ‖(c : E)‖) :=
        mul_le_mul (radius_bounds c v).2 (radius_bounds c w).2
          (radius_pos c w).le (by positivity)
      _ = (1 + ‖(c : E)‖) ^ 2 := by ring
  have h := (radius_mul_gap_le c v w).trans
    (mul_le_mul_of_nonneg_right hp (norm_nonneg _))
  have h' := (le_div_iff₀ hq).2 h
  simpa only [div_mul_eq_mul_div] using h'

/-- The contact-map estimate requested in the mathematical specification. -/
theorem contact_dist_le (c : InteriorCenter E) (v w : UnitSphere E) :
    ‖(contact c v : E) - (contact c w : E)‖ ≤
      (2 * (1 + ‖(c : E)‖) / (1 - ‖(c : E)‖)) * ‖(v : E) - (w : E)‖ := by
  have hq : 0 < 1 - ‖(c : E)‖ := sub_pos.mpr c.property
  have hid : (contact c v : E) - (contact c w : E) =
      radius c v • ((v : E) - (w : E)) +
        (radius c v - radius c w) • (w : E) := by
    simp only [contact_val]
    module
  calc
    ‖(contact c v : E) - (contact c w : E)‖ ≤
        ‖radius c v • ((v : E) - (w : E))‖ +
          ‖(radius c v - radius c w) • (w : E)‖ := by
      rw [hid]
      exact norm_add_le _ _
    _ = radius c v * ‖(v : E) - (w : E)‖ + |radius c v - radius c w| := by
      simp [norm_smul, Real.norm_eq_abs, abs_of_nonneg (radius_pos c v).le, w.property]
    _ ≤ (1 + ‖(c : E)‖) * ‖(v : E) - (w : E)‖ +
        ((1 + ‖(c : E)‖) ^ 2 / (1 - ‖(c : E)‖)) * ‖(v : E) - (w : E)‖ :=
      add_le_add (mul_le_mul_of_nonneg_right (radius_bounds c v).2 (norm_nonneg _))
        (radius_dist_le c v w)
    _ = (2 * (1 + ‖(c : E)‖) / (1 - ‖(c : E)‖)) * ‖(v : E) - (w : E)‖ := by
      field_simp [hq.ne']
      ring

/-- Nonnegative radius Lipschitz constant. -/
noncomputable def radiusConstant (c : InteriorCenter E) : ℝ≥0 :=
  ⟨(1 + ‖(c : E)‖) ^ 2 / (1 - ‖(c : E)‖),
    div_nonneg (sq_nonneg _) (sub_pos.mpr c.property).le⟩

/-- Nonnegative contact Lipschitz constant. -/
noncomputable def contactConstant (c : InteriorCenter E) : ℝ≥0 :=
  ⟨2 * (1 + ‖(c : E)‖) / (1 - ‖(c : E)‖),
    div_nonneg (by positivity) (sub_pos.mpr c.property).le⟩

theorem radius_lipschitz (c : InteriorCenter E) :
    LipschitzWith (radiusConstant c) (radius c) := by
  apply LipschitzWith.of_dist_le_mul
  intro v w
  simpa [dist_eq_norm, Real.norm_eq_abs, radiusConstant, Subtype.dist_eq] using radius_dist_le c v w

theorem contact_lipschitz (c : InteriorCenter E) :
    LipschitzWith (contactConstant c) (contact c) := by
  apply LipschitzWith.of_dist_le_mul
  intro v w
  simpa [dist_eq_norm, contactConstant, Subtype.dist_eq] using contact_dist_le c v w

theorem radius_continuous (c : InteriorCenter E) : Continuous (radius c) :=
  (radius_lipschitz c).continuous

theorem contact_continuous (c : InteriorCenter E) : Continuous (contact c) :=
  (contact_lipschitz c).continuous

end RadialContact
