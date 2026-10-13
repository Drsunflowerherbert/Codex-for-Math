import TransportSharpness.Finite

/-! Scalar obstruction from the audited exact finite-atomic formulas.
No theorem in this module alone constructs a Lebesgue-source optimal map. -/
namespace TransportSharpness
noncomputable section
open Filter

/-- Value of the map norm after the separately documented cell integration. -/
def mapSize (a b : ℝ) : ℝ := Real.sqrt (mapSquared a b)

/-- Value of the finite target Wp distance when a,b>0. -/
def targetDistance (a b p : ℝ) : ℝ := a ^ (1/p) * b

def ceiling (p : ℝ) : ℝ := p / (2 * (p + 1))

def exponent (p α : ℝ) : ℝ := 1/2 - α * (1 + 1/p)

theorem exponent_negative (p α : ℝ) (hp : 0 < p) (hα : ceiling p < α) :
    exponent p α < 0 := by
  unfold ceiling at hα
  have hden : 0 < 2*(p+1) := by linarith
  have hmul := (div_lt_iff₀ hden).mp hα
  unfold exponent
  apply (mul_lt_mul_iff_left₀ hp).mp
  field_simp
  nlinarith

theorem targetDistance_positive (a b p : ℝ) (ha : 0 < a) (hb : 0 < b) :
    0 < targetDistance a b p := by
  exact mul_pos (Real.rpow_pos_of_pos ha _) hb

theorem targetDistance_power (a b p : ℝ) (ha : 0 < a) (hb : 0 ≤ b) (hp : p ≠ 0) :
    (targetDistance a b p) ^ p = a * b ^ p := by
  unfold targetDistance
  rw [Real.mul_rpow (Real.rpow_nonneg ha.le _) hb, ← Real.rpow_mul ha.le]
  simp [hp]

theorem targetDistance_shrinking (a p : ℝ) (ha : 0 < a) :
    targetDistance a (a/2) p = a ^ (1+1/p) / 2 := by
  unfold targetDistance
  rw [Real.rpow_add ha, Real.rpow_one]
  ring

theorem mapSize_shrinking_lower (a : ℝ) (ha : 0 < a) :
    Real.sqrt a / 2 ≤ mapSize a (a/2) := by
  unfold mapSize mapSquared
  apply (Real.le_sqrt (by positivity) (by positivity)).mpr
  have hsq := Real.sq_sqrt ha.le
  nlinarith [sq_nonneg a]

/-- Lower bound with the exact exponent; holds for all real alpha and positive a. -/
theorem shrinking_ratio_lower (a p α : ℝ) (ha : 0 < a) :
    (2:ℝ) ^ α / 2 * a ^ (exponent p α) ≤
    mapSize a (a/2) / (targetDistance a (a/2) p) ^ α := by
  have hd : 0 < (targetDistance a (a/2) p) ^ α :=
    Real.rpow_pos_of_pos (targetDistance_positive a (a/2) p ha (by linarith)) _
  calc
    _ = (Real.sqrt a / 2) / (targetDistance a (a/2) p) ^ α := by
      rw [targetDistance_shrinking a p ha, Real.div_rpow (Real.rpow_nonneg ha.le _)
        (by norm_num), ← Real.rpow_mul ha.le, Real.sqrt_eq_rpow,
        exponent, Real.rpow_sub ha]
      field_simp
    _ ≤ _ := div_le_div_of_nonneg_right (mapSize_shrinking_lower a ha) hd.le

/-- Algebraic exponent identity distinguishes the finite-p ceiling. -/
theorem ceiling_values : ceiling 2 = 1/3 ∧ ceiling 1 = 1/4 := by
  norm_num [ceiling]

/-- For every proposed uniform constant a shrinking-mass pair violates it.
This theorem uses the explicit scalar formulas, rather than abstract Wp or maps. -/
theorem shrinking_exceeds_constant (p α C : ℝ) (hp : 1 ≤ p) (hα : ceiling p < α) :
    ∃ a : ℝ, 0 < a ∧ a < 1/2 ∧ Admissible a (a/2) ∧
      C * (targetDistance a (a/2) p) ^ α < mapSize a (a/2) := by
  have hexp := exponent_negative p α (by linarith) hα
  have hlim : Tendsto (fun t : ℝ => (2:ℝ) ^ α / 2 * t ^ (-exponent p α)) atTop atTop :=
    (tendsto_rpow_atTop (neg_pos.mpr hexp)).const_mul_atTop (by positivity)
  obtain ⟨t, ht2, hbig⟩ := ((eventually_gt_atTop (2:ℝ)).and
    (hlim.eventually (eventually_gt_atTop C))).exists
  have ht : 0 < t := by linarith
  have ha : 0 < t⁻¹ := inv_pos.mpr ht
  have ha2 : t⁻¹ < 1/2 := by
    have h := one_div_lt_one_div_of_lt (by norm_num : (0:ℝ) < 2) ht2
    simpa only [one_div] using h
  refine ⟨t⁻¹, ha, ha2, shrinking_admissible t⁻¹ ha ha2, ?_⟩
  have hlo := shrinking_ratio_lower t⁻¹ p α ha
  rw [← Real.rpow_neg_eq_inv_rpow] at hlo
  have hratio := lt_of_lt_of_le hbig hlo
  exact (lt_div_iff₀ (Real.rpow_pos_of_pos
    (targetDistance_positive t⁻¹ (t⁻¹/2) p ha (by linarith)) α)).mp hratio

/-- W2 exponent ceiling specialized in the scalar core. -/
theorem W2_exceeds_constant (α C : ℝ) (hα : 1/3 < α) :
    ∃ a : ℝ, 0 < a ∧ a < 1/2 ∧ Admissible a (a/2) ∧
      C * (targetDistance a (a/2) 2) ^ α < mapSize a (a/2) := by
  apply shrinking_exceeds_constant 2 α C (by norm_num)
  rw [ceiling_values.1]
  exact hα

/-- Fixed central mass has a different exponent; b alone shrinks. -/
theorem mapSize_fixed_lower (a b : ℝ) (ha : 0 ≤ a) (hb : 0 < b) :
    Real.sqrt b / Real.sqrt 2 ≤ mapSize a b := by
  unfold mapSize mapSquared
  have hb2 : 0 ≤ b/2 := by positivity
  have hm : b/2 ≤ b/2 + a*b^2 := by nlinarith [sq_nonneg b]
  calc
    _ = Real.sqrt (b/2) := by rw [Real.sqrt_div hb.le]
    _ ≤ _ := Real.sqrt_le_sqrt hm

/-- Exact lower bound for the fixed-mass scalar family. -/
theorem fixed_ratio_lower (a b p α : ℝ) (ha : 0 < a) (hb : 0 < b) :
    ((a ^ (1/p)) ^ (-α) / Real.sqrt 2) * b ^ (1/2 - α) ≤
      mapSize a b / (targetDistance a b p) ^ α := by
  have hd := Real.rpow_pos_of_pos (targetDistance_positive a b p ha hb) α
  calc
    _ = (Real.sqrt b / Real.sqrt 2) / (targetDistance a b p) ^ α := by
      rw [Real.rpow_neg (Real.rpow_nonneg ha.le _), Real.rpow_sub hb,
        Real.sqrt_eq_rpow b, targetDistance, Real.mul_rpow (Real.rpow_nonneg ha.le _) hb.le]
      field_simp
    _ ≤ _ := div_le_div_of_nonneg_right (mapSize_fixed_lower a b ha.le hb) hd.le

/-- A uniform lower atom-mass bound does not support exponents above 1/2.
The statement again concerns the exact scalar formulas and finite matrix domain. -/
theorem fixed_mass_exceeds_constant (a p α C : ℝ) (ha : 0 < a) (ha1 : a < 1)
    (hα : 1/2 < α) :
    ∃ b : ℝ, Admissible a b ∧
      C * (targetDistance a b p) ^ α < mapSize a b := by
  have hlim : Tendsto
      (fun t : ℝ => ((a ^ (1/p)) ^ (-α) / Real.sqrt 2) * t ^ (-(1/2-α)))
      atTop atTop :=
    (tendsto_rpow_atTop (by linarith : 0 < -(1/2-α))).const_mul_atTop (by positivity)
  obtain ⟨t, hta, ht1a, hbig⟩ := ((eventually_gt_atTop (1/a)).and
    ((eventually_gt_atTop (1/(1-a))).and (hlim.eventually (eventually_gt_atTop C)))).exists
  have ht : 0 < t := lt_trans (by positivity : 0 < 1/a) hta
  have hb : 0 < t⁻¹ := inv_pos.mpr ht
  have hba : t⁻¹ < a := by
    simpa only [one_div] using (one_div_lt ht ha).mpr hta
  have hba1 : t⁻¹ < 1-a := by
    simpa only [one_div] using (one_div_lt ht (by linarith : 0 < 1-a)).mpr ht1a
  refine ⟨t⁻¹, ⟨hb, hba, by linarith⟩, ?_⟩
  have hlo := fixed_ratio_lower a t⁻¹ p α ha hb
  rw [← Real.rpow_neg_eq_inv_rpow] at hlo
  exact (lt_div_iff₀ (Real.rpow_pos_of_pos (targetDistance_positive a t⁻¹ p ha hb) α)).mp
    (lt_of_lt_of_le hbig hlo)

end
end TransportSharpness
