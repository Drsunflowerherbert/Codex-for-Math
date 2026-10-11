import RadialContact.Inverse

/-!
# Derived refinements

These results are separated from the requested source-specification statements:
reciprocal-radius control, a quantitative inverse bound, and exact constants at
the zero center. No assertion of sharpness is formalized in this file.
-/

namespace RadialContact

open scoped NNReal

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- Reciprocal radii have a simpler Lipschitz estimate. -/
theorem reciprocal_radius_dist_le (c : InteriorCenter E) (v w : UnitSphere E) :
    |(radius c v)⁻¹ - (radius c w)⁻¹| ≤
      ‖(v : E) - (w : E)‖ / (1 - ‖(c : E)‖) := by
  have hr := radius_pos c v
  have hs := radius_pos c w
  have hq : 0 < 1 - ‖(c : E)‖ := sub_pos.mpr c.property
  have hid : (radius c v)⁻¹ - (radius c w)⁻¹ =
      (radius c w - radius c v) / (radius c v * radius c w) := by
    field_simp [hr.ne', hs.ne']
  rw [hid, abs_div, abs_of_pos (mul_pos hr hs), abs_sub_comm]
  apply (div_le_div_iff₀ (mul_pos hr hs) hq).2
  have h := radius_mul_gap_le c v w
  nlinarith

/-- Translation is recovered by multiplying the normalized direction by its norm. -/
theorem norm_smul_direction (c : InteriorCenter E) (x : UnitSphere E) :
    ‖(x : E) - (c : E)‖ • (direction c x : E) = (x : E) - (c : E) := by
  rw [direction_val, smul_smul, mul_inv_cancel₀ (norm_sub_center_pos c x).ne', one_smul]

/-- The normalized inverse is Lipschitz, with no compactness assumption. -/
theorem direction_dist_le (c : InteriorCenter E) (x y : UnitSphere E) :
    ‖(direction c x : E) - (direction c y : E)‖ ≤
      (2 / (1 - ‖(c : E)‖)) * ‖(x : E) - (y : E)‖ := by
  have hq : 0 < 1 - ‖(c : E)‖ := sub_pos.mpr c.property
  have hr := norm_sub_center_pos c x
  have hid : ‖(x : E) - (c : E)‖ •
        ((direction c x : E) - (direction c y : E)) =
      ((x : E) - (y : E)) +
        (‖(y : E) - (c : E)‖ - ‖(x : E) - (c : E)‖) • (direction c y : E) := by
    rw [smul_sub, sub_smul, norm_smul_direction, norm_smul_direction]
    abel
  have hab : |‖(y : E) - (c : E)‖ - ‖(x : E) - (c : E)‖| ≤
      ‖(x : E) - (y : E)‖ := by
    have h := abs_norm_sub_norm_le ((y : E) - (c : E)) ((x : E) - (c : E))
    have he : ((y : E) - (c : E)) - ((x : E) - (c : E)) = (y : E) - (x : E) := by abel
    simpa only [he, norm_sub_rev] using h
  have h : (1 - ‖(c : E)‖) * ‖(direction c x : E) - (direction c y : E)‖ ≤
      2 * ‖(x : E) - (y : E)‖ := by
    calc
      (1 - ‖(c : E)‖) * ‖(direction c x : E) - (direction c y : E)‖ ≤
          ‖(x : E) - (c : E)‖ * ‖(direction c x : E) - (direction c y : E)‖ :=
        mul_le_mul_of_nonneg_right (norm_sub_center_lower c x) (norm_nonneg _)
      _ = ‖‖(x : E) - (c : E)‖ • ((direction c x : E) - (direction c y : E))‖ := by
        rw [norm_smul, Real.norm_eq_abs, abs_of_nonneg hr.le]
      _ ≤ ‖(x : E) - (y : E)‖ +
          |‖(y : E) - (c : E)‖ - ‖(x : E) - (c : E)‖| := by
        rw [hid]
        simpa only [norm_smul, Real.norm_eq_abs, (direction c y).property, mul_one]
          using norm_add_le ((x : E) - (y : E))
            ((‖(y : E) - (c : E)‖ - ‖(x : E) - (c : E)‖) • (direction c y : E))
      _ ≤ 2 * ‖(x : E) - (y : E)‖ := by linarith
  have h' : ‖(direction c x : E) - (direction c y : E)‖ ≤
      (2 * ‖(x : E) - (y : E)‖) / (1 - ‖(c : E)‖) :=
    (le_div_iff₀ hq).2 (by simpa only [mul_comm] using h)
  simpa only [div_mul_eq_mul_div] using h'

noncomputable def directionConstant (c : InteriorCenter E) : ℝ≥0 :=
  ⟨2 / (1 - ‖(c : E)‖), div_nonneg (by norm_num) (sub_pos.mpr c.property).le⟩

theorem direction_lipschitz (c : InteriorCenter E) :
    LipschitzWith (directionConstant c) (direction c) := by
  apply LipschitzWith.of_dist_le_mul
  intro x y
  simpa [directionConstant, Subtype.dist_eq, dist_eq_norm] using direction_dist_le c x y

/-- At zero the radius is constant, so its exact Lipschitz constant is zero. -/
theorem radius_zero_lipschitz : LipschitzWith 0 (radius (zeroCenter (E := E))) := by
  apply LipschitzWith.of_dist_le_mul
  intro v w
  simp

/-- At zero contact is an isometry, including on an empty sphere. -/
theorem contact_zero_isometry : Isometry (contact (zeroCenter (E := E))) := by
  intro v w
  simp

theorem direction_zero_isometry : Isometry (direction (zeroCenter (E := E))) := by
  intro v w
  simp

end RadialContact
