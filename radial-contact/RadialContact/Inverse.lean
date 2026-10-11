import RadialContact.Lipschitz
import Mathlib.Topology.Homeomorph.Defs

/-! # The normalized inverse and the resulting sphere homeomorphism -/

namespace RadialContact

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

omit [NormedSpace ℝ E] in
/-- Sphere points stay a positive distance from an interior center. -/
theorem norm_sub_center_lower (c : InteriorCenter E) (x : UnitSphere E) :
    1 - ‖(c : E)‖ ≤ ‖(x : E) - (c : E)‖ := by
  have h := norm_sub_norm_le (x : E) (c : E)
  simpa only [x.property] using h

omit [NormedSpace ℝ E] in
theorem norm_sub_center_pos (c : InteriorCenter E) (x : UnitSphere E) :
    0 < ‖(x : E) - (c : E)‖ :=
  lt_of_lt_of_le (sub_pos.mpr c.property) (norm_sub_center_lower c x)

/-- The inverse direction: translate by -c, then normalize. -/
noncomputable def direction (c : InteriorCenter E) (x : UnitSphere E) : UnitSphere E :=
  ⟨‖(x : E) - (c : E)‖⁻¹ • ((x : E) - (c : E)), by
    rw [norm_smul, norm_inv, Real.norm_eq_abs, abs_of_nonneg (norm_nonneg _)]
    exact inv_mul_cancel₀ (norm_sub_center_pos c x).ne'⟩

@[simp] theorem direction_val (c : InteriorCenter E) (x : UnitSphere E) :
    (direction c x : E) = ‖(x : E) - (c : E)‖⁻¹ • ((x : E) - (c : E)) := rfl

/-- The inverse point provides its contact radius explicitly. -/
theorem radius_direction (c : InteriorCenter E) (x : UnitSphere E) :
    radius c (direction c x) = ‖(x : E) - (c : E)‖ := by
  apply radius_eq_of_contact c (direction c x) (norm_sub_center_pos c x)
  rw [direction_val, smul_smul, mul_inv_cancel₀ (norm_sub_center_pos c x).ne', one_smul]
  have hid : (c : E) + ((x : E) - (c : E)) = (x : E) := by abel
  rw [hid]
  exact x.property

@[simp] theorem contact_direction (c : InteriorCenter E) (x : UnitSphere E) :
    contact c (direction c x) = x := by
  apply Subtype.ext
  rw [contact_val, radius_direction, direction_val, smul_smul,
    mul_inv_cancel₀ (norm_sub_center_pos c x).ne', one_smul]
  abel

@[simp] theorem direction_contact (c : InteriorCenter E) (v : UnitSphere E) :
    direction c (contact c v) = v := by
  apply Subtype.ext
  have hid : (contact c v : E) - (c : E) = radius c v • (v : E) := by
    rw [contact_val]
    abel
  rw [direction_val, hid, norm_smul, Real.norm_eq_abs,
    abs_of_nonneg (radius_pos c v).le, v.property, mul_one, smul_smul,
    inv_mul_cancel₀ (radius_pos c v).ne', one_smul]

theorem direction_continuous (c : InteriorCenter E) : Continuous (direction c) := by
  apply Continuous.subtype_mk
  have h : Continuous (fun x : UnitSphere E => (x : E) - (c : E)) :=
    continuous_subtype_val.sub continuous_const
  exact (h.norm.inv₀ (fun x => (norm_sub_center_pos c x).ne')).smul h

/-- The radial contact and normalized inverse form a homeomorphism, even when
the unit sphere is empty. -/
noncomputable def sphereHomeomorph (c : InteriorCenter E) : UnitSphere E ≃ₜ UnitSphere E where
  toFun := contact c
  invFun := direction c
  left_inv := direction_contact c
  right_inv := contact_direction c
  continuous_toFun := contact_continuous c
  continuous_invFun := direction_continuous c

omit [NormedSpace ℝ E] in
/-- No arbitrary contact direction is chosen when the sphere is empty. -/
theorem unitSphere_isEmpty_of_subsingleton [Subsingleton E] : IsEmpty (UnitSphere E) := by
  refine ⟨fun v => ?_⟩
  have hzero : (v : E) = 0 := Subsingleton.elim _ _
  have h := v.property
  rw [hzero, norm_zero] at h
  exact zero_ne_one h

/-- The zero center exists in every real normed space. -/
def zeroCenter : InteriorCenter E := ⟨0, by simp⟩

omit [NormedSpace ℝ E] in
@[simp] theorem zeroCenter_val : (zeroCenter (E := E) : E) = 0 := rfl

@[simp] theorem radius_zero (v : UnitSphere E) : radius zeroCenter v = 1 := by
  apply radius_eq_of_contact zeroCenter v zero_lt_one
  simpa using v.property

@[simp] theorem contact_zero (v : UnitSphere E) : contact zeroCenter v = v := by
  apply Subtype.ext
  simp

@[simp] theorem direction_zero (x : UnitSphere E) : direction zeroCenter x = x := by
  apply Subtype.ext
  simp [x.property]

end RadialContact
