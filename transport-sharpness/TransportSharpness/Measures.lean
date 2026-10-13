import TransportSharpness.Obstruction

/-! Actual Borel measures and couplings for the two-dimensional atomic targets.
The cost is explicitly Euclidean: the standard product norm is not used.
No theorem here constructs the uniform cube source or its optimal maps. -/
namespace TransportSharpness
noncomputable section
open MeasureTheory Measure Finset Filter
open scoped ENNReal

abbrev Point := ℝ × ℝ
abbrev PointPair := Point × Point

/-- Actual Borel atomic target measure, with central point (0,b). -/
def atomicMeasure (a b : ℝ) : Measure Point :=
  ∑ i : Atom, ENNReal.ofReal (mass a i) • Measure.dirac (targetPoint b i)

/-- Actual Borel coupling matching corresponding atoms. -/
def matchingMeasure (a b : ℝ) : Measure PointPair :=
  ∑ i : Atom, ENNReal.ofReal (mass a i) •
    Measure.dirac (sourcePoint i, targetPoint b i)

/-- The predicate ranges over all Borel measures, not just finite arrays. -/
def IsMeasureCoupling (a b : ℝ) (γ : Measure PointPair) : Prop :=
  Measure.map Prod.fst γ = atomicMeasure a 0 ∧
  Measure.map Prod.snd γ = atomicMeasure a b

/-- Sum of squared Euclidean coordinate differences. -/
def euclideanSquared (z : PointPair) : ℝ :=
  (z.1.1-z.2.1)^2 + (z.1.2-z.2.2)^2

/-- Explicit Euclidean coordinate distance, not the product max distance. -/
def euclideanDistance (x y : Point) : ℝ := Real.sqrt (euclideanSquared (x,y))

def measurePCost (p : ℝ) (z : PointPair) : ℝ≥0∞ :=
  ENNReal.ofReal (euclideanSquared z ^ (p/2))

/-- Nonnegative integral cost of an actual Borel coupling. -/
def measureCost (p : ℝ) (γ : Measure PointPair) : ℝ≥0∞ :=
  ∫⁻ z, measurePCost p z ∂γ

/-- The original all-coupling infimal cost, specialized to these actual targets. -/
def transportPowerInf (a b p : ℝ) : ℝ≥0∞ :=
  ⨅ (γ : Measure PointPair) (_ : IsMeasureCoupling a b γ), measureCost p γ

/-- Projected destination cost, independent of the first marginal. -/
def projectionPCost (p : ℝ) (z : Point) : ℝ≥0∞ :=
  ENNReal.ofReal ((z.2^2) ^ (p/2))

theorem atomicMeasure_probability (a b : ℝ) (ha : 0 ≤ a) (ha1 : a ≤ 1) :
    IsProbabilityMeasure (atomicMeasure a b) := by
  constructor
  simp only [atomicMeasure, Measure.finset_sum_apply, Measure.smul_apply,
    smul_eq_mul, Measure.dirac_apply_of_mem (Set.mem_univ _), mul_one]
  rw [← ENNReal.ofReal_sum_of_nonneg]
  · rw [mass_sum]
    norm_num
  · intro i _
    unfold mass
    split_ifs <;> linarith

theorem atomicMeasure_explicit (a b : ℝ) :
    atomicMeasure a b =
      ENNReal.ofReal ((1-a)/2) • Measure.dirac ((-1:ℝ),(0:ℝ)) +
      (ENNReal.ofReal a • Measure.dirac ((0:ℝ),b) +
       ENNReal.ofReal ((1-a)/2) • Measure.dirac ((1:ℝ),(0:ℝ))) := by
  simp [atomicMeasure, Fin.sum_univ_succ, mass, targetPoint]

theorem euclideanSquared_nonnegative (z : PointPair) : 0 ≤ euclideanSquared z := by
  unfold euclideanSquared
  positivity

theorem measurePCost_eq_distancePower (p : ℝ) (z : PointPair) :
    measurePCost p z = ENNReal.ofReal ((euclideanDistance z.1 z.2)^p) := by
  unfold measurePCost euclideanDistance
  rw [Real.sqrt_eq_rpow, ← Real.rpow_mul (euclideanSquared_nonnegative z)]
  congr 2
  ring

theorem sourcePoint_eq_targetPoint_zero (i : Atom) : sourcePoint i = targetPoint 0 i := by
  fin_cases i <;> rfl

theorem matchingMeasure_coupling (a b : ℝ) : IsMeasureCoupling a b (matchingMeasure a b) := by
  constructor
  · simp [matchingMeasure, atomicMeasure, Fin.sum_univ_succ,
      Measure.map_add _ _ measurable_fst, Measure.map_smul,
      Measure.map_dirac measurable_fst, sourcePoint_eq_targetPoint_zero]
  · simp [matchingMeasure, atomicMeasure, Fin.sum_univ_succ,
      Measure.map_add _ _ measurable_snd, Measure.map_smul,
      Measure.map_dirac measurable_snd]

/-- Marginal probability forces every admissible actual coupling to be probability. -/
theorem actual_coupling_probability (a b : ℝ) (γ : Measure PointPair)
    (ha : 0 ≤ a) (ha1 : a ≤ 1) (hγ : IsMeasureCoupling a b γ) :
    IsProbabilityMeasure γ := by
  apply (Measure.isProbabilityMeasure_map_iff measurable_fst.aemeasurable).mp
  rw [hγ.1]
  exact atomicMeasure_probability a 0 ha ha1

theorem atomicMeasure_zero_second_ae (a : ℝ) :
    ∀ᵐ z ∂atomicMeasure a 0, z.2 = 0 := by
  rw [ae_iff]
  simp [atomicMeasure, Fin.sum_univ_succ, targetPoint]

theorem coupling_zero_second_ae (a b : ℝ) (γ : Measure PointPair)
    (hγ : IsMeasureCoupling a b γ) : ∀ᵐ z ∂γ, z.1.2 = 0 := by
  have h : ∀ᵐ y ∂Measure.map (Prod.fst : PointPair → Point) γ, y.2 = 0 := by
    rw [hγ.1]
    exact atomicMeasure_zero_second_ae a
  exact ae_of_ae_map (μ := γ) (f := Prod.fst) (p := fun y : Point => y.2 = 0)
    measurable_fst.aemeasurable h

theorem projectionPCost_measurable (p : ℝ) : Measurable (projectionPCost p) := by
  unfold projectionPCost
  fun_prop

theorem measurePCost_measurable (p : ℝ) : Measurable (measurePCost p) := by
  unfold measurePCost euclideanSquared
  fun_prop

theorem projectionPCost_le (p : ℝ) (hp : 0 < p) (z : PointPair) (hz : z.1.2 = 0) :
    projectionPCost p z.2 ≤ measurePCost p z := by
  unfold projectionPCost measurePCost
  apply ENNReal.ofReal_le_ofReal
  apply Real.rpow_le_rpow (sq_nonneg z.2.2) _ (by linarith)
  unfold euclideanSquared
  rw [hz]
  nlinarith [sq_nonneg (z.1.1-z.2.1)]

theorem atomicMeasure_projection_integral (a b p : ℝ) (ha : 0 ≤ a)
    (hb : 0 ≤ b) (hp : 0 < p) :
    ∫⁻ z, projectionPCost p z ∂atomicMeasure a b = ENNReal.ofReal (a*b^p) := by
  simp [atomicMeasure, Fin.sum_univ_succ, lintegral_add_measure,
    lintegral_smul_measure, lintegral_dirac, projectionPCost, targetPoint,
    mass, Real.zero_rpow (show p/2 ≠ 0 by linarith), square_rpow_half b p hb,
    ← ENNReal.ofReal_mul ha]

/-- Every actual coupling satisfies the lower bound, with no finite-support premise. -/
theorem actual_coupling_lower_bound (a b p : ℝ) (γ : Measure PointPair)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hp : 0 < p) (hγ : IsMeasureCoupling a b γ) :
    ENNReal.ofReal (a*b^p) ≤ measureCost p γ := by
  calc
    _ = ∫⁻ z, projectionPCost p z ∂atomicMeasure a b :=
      (atomicMeasure_projection_integral a b p ha hb hp).symm
    _ = ∫⁻ z, projectionPCost p z.2 ∂γ := by
      rw [← hγ.2, lintegral_map (projectionPCost_measurable p) measurable_snd]
    _ ≤ _ := lintegral_mono_ae <| (coupling_zero_second_ae a b γ hγ).mono
      fun z hz => projectionPCost_le p hp z hz

theorem matchingMeasure_cost (a b p : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) (hp : 0 < p) :
    measureCost p (matchingMeasure a b) = ENNReal.ofReal (a*b^p) := by
  simp [measureCost, matchingMeasure, Fin.sum_univ_succ, lintegral_add_measure,
    lintegral_smul_measure, lintegral_dirac, measurePCost, euclideanSquared,
    sourcePoint, targetPoint, mass,
    Real.zero_rpow (show p/2 ≠ 0 by linarith), square_rpow_half b p hb,
    ← ENNReal.ofReal_mul ha]

/-- Exact infimum over all Borel coupling measures, attained by matching. -/
theorem actual_transportPowerInf (a b p : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) (hp : 0 < p) :
    transportPowerInf a b p = ENNReal.ofReal (a*b^p) := by
  apply le_antisymm
  · exact iInf_le_of_le (matchingMeasure a b) <|
      iInf_le_of_le (matchingMeasure_coupling a b) (matchingMeasure_cost a b p ha hb hp).le
  · exact le_iInf fun γ => le_iInf fun hγ => actual_coupling_lower_bound a b p γ ha hb hp hγ

/-- The actual nonnegative infimal cost is finite. -/
theorem actual_transportPowerInf_finite (a b p : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hp : 0 < p) : transportPowerInf a b p < ∞ := by
  rw [actual_transportPowerInf a b p ha hb hp]
  exact ENNReal.ofReal_lt_top

/-- Link the actual all-Borel-coupling cost root to the retained scalar distance. -/
theorem actual_transportDistance_eq (a b p : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hp : 0 < p) :
    (transportPowerInf a b p).toReal ^ (1/p) = targetDistance a b p := by
  rw [actual_transportPowerInf a b p ha hb hp,
    ENNReal.toReal_ofReal (mul_nonneg ha (Real.rpow_nonneg hb _)),
    Real.mul_rpow ha (Real.rpow_nonneg hb _), ← Real.rpow_mul hb]
  simp [targetDistance, hp.ne']

/-- Probability-measure specialization of the attained all-coupling cost theorem. -/
theorem actual_probability_transport (a b p : ℝ) (ha : 0 ≤ a) (ha1 : a ≤ 1)
    (hb : 0 ≤ b) (hp : 1 ≤ p) :
    IsProbabilityMeasure (atomicMeasure a 0) ∧
    IsProbabilityMeasure (atomicMeasure a b) ∧
    IsMeasureCoupling a b (matchingMeasure a b) ∧
    IsProbabilityMeasure (matchingMeasure a b) ∧
    measureCost p (matchingMeasure a b) = ENNReal.ofReal (a*b^p) ∧
    transportPowerInf a b p = ENNReal.ofReal (a*b^p) := by
  have hp0 : 0 < p := by linarith
  exact ⟨atomicMeasure_probability a 0 ha ha1, atomicMeasure_probability a b ha ha1,
    matchingMeasure_coupling a b,
    actual_coupling_probability a b (matchingMeasure a b) ha ha1 (matchingMeasure_coupling a b),
    matchingMeasure_cost a b p ha hb hp0, actual_transportPowerInf a b p ha hb hp0⟩

end
end TransportSharpness
