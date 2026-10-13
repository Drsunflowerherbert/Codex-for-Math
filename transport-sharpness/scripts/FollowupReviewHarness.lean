import TransportSharpness.Measures
import EvidenceHarness

/-! Independent full-type and body review of the actual-measure extension.
Expected terms are handwritten and closed; no theorem is specialized.
The retained finite/scalar declarations are checked by ReviewHarness separately.
-/
namespace TransportSharpness
open MeasureTheory Measure Finset Filter
open scoped ENNReal

#evidence_check TransportSharpness.Point : Type
#evidence_check TransportSharpness.PointPair : Type
#evidence_check TransportSharpness.atomicMeasure : ℝ → ℝ → Measure (ℝ × ℝ)
#evidence_check TransportSharpness.matchingMeasure : ℝ → ℝ → Measure ((ℝ × ℝ) × (ℝ × ℝ))
#evidence_check TransportSharpness.IsMeasureCoupling :
  ℝ → ℝ → Measure ((ℝ × ℝ) × (ℝ × ℝ)) → Prop
#evidence_check TransportSharpness.euclideanSquared : ((ℝ × ℝ) × (ℝ × ℝ)) → ℝ
#evidence_check TransportSharpness.euclideanDistance : (ℝ × ℝ) → (ℝ × ℝ) → ℝ
#evidence_check TransportSharpness.measurePCost : ℝ → ((ℝ × ℝ) × (ℝ × ℝ)) → ℝ≥0∞
#evidence_check TransportSharpness.measureCost : ℝ → Measure ((ℝ × ℝ) × (ℝ × ℝ)) → ℝ≥0∞
#evidence_check TransportSharpness.transportPowerInf : ℝ → ℝ → ℝ → ℝ≥0∞
#evidence_check TransportSharpness.projectionPCost : ℝ → (ℝ × ℝ) → ℝ≥0∞

#evidence_definition TransportSharpness.Point = ℝ × ℝ
#evidence_definition TransportSharpness.PointPair = (ℝ × ℝ) × (ℝ × ℝ)
#evidence_definition TransportSharpness.atomicMeasure = fun a b : ℝ =>
  ∑ i : Fin 3, ENNReal.ofReal (mass a i) • Measure.dirac (targetPoint b i)
#evidence_definition TransportSharpness.matchingMeasure = fun a b : ℝ =>
  ∑ i : Fin 3, ENNReal.ofReal (mass a i) • Measure.dirac (sourcePoint i, targetPoint b i)
#evidence_definition TransportSharpness.IsMeasureCoupling =
  fun (a b : ℝ) (γ : Measure ((ℝ × ℝ) × (ℝ × ℝ))) =>
    Measure.map Prod.fst γ = atomicMeasure a 0 ∧
    Measure.map Prod.snd γ = atomicMeasure a b
#evidence_definition TransportSharpness.euclideanSquared =
  fun z : ((ℝ × ℝ) × (ℝ × ℝ)) =>
    (z.1.1 - z.2.1) ^ 2 + (z.1.2 - z.2.2) ^ 2
#evidence_definition TransportSharpness.euclideanDistance = fun x y : ℝ × ℝ =>
  Real.sqrt (euclideanSquared (x, y))
#evidence_definition TransportSharpness.measurePCost =
  fun (p : ℝ) (z : ((ℝ × ℝ) × (ℝ × ℝ))) =>
    ENNReal.ofReal (euclideanSquared z ^ (p / 2))
#evidence_definition TransportSharpness.measureCost =
  fun (p : ℝ) (γ : Measure ((ℝ × ℝ) × (ℝ × ℝ))) =>
    ∫⁻ z, measurePCost p z ∂γ
#evidence_definition TransportSharpness.transportPowerInf = fun a b p : ℝ =>
  ⨅ (γ : Measure ((ℝ × ℝ) × (ℝ × ℝ))) (_ : IsMeasureCoupling a b γ),
    measureCost p γ
#evidence_definition TransportSharpness.projectionPCost = fun (p : ℝ) (z : ℝ × ℝ) =>
  ENNReal.ofReal ((z.2 ^ 2) ^ (p / 2))

#evidence_check TransportSharpness.atomicMeasure_probability :
  ∀ a b : ℝ, 0 ≤ a → a ≤ 1 → IsProbabilityMeasure (atomicMeasure a b)
#evidence_check TransportSharpness.atomicMeasure_explicit :
  ∀ a b : ℝ,
    atomicMeasure a b =
      ENNReal.ofReal ((1 - a) / 2) • Measure.dirac ((-1 : ℝ), (0 : ℝ)) +
      (ENNReal.ofReal a • Measure.dirac ((0 : ℝ), b) +
       ENNReal.ofReal ((1 - a) / 2) • Measure.dirac ((1 : ℝ), (0 : ℝ)))
#evidence_check TransportSharpness.euclideanSquared_nonnegative :
  ∀ z : ((ℝ × ℝ) × (ℝ × ℝ)), 0 ≤ euclideanSquared z
#evidence_check TransportSharpness.measurePCost_eq_distancePower :
  ∀ (p : ℝ) (z : ((ℝ × ℝ) × (ℝ × ℝ))),
    measurePCost p z = ENNReal.ofReal ((euclideanDistance z.1 z.2) ^ p)
#evidence_check TransportSharpness.sourcePoint_eq_targetPoint_zero :
  ∀ i : Fin 3, sourcePoint i = targetPoint 0 i
#evidence_check TransportSharpness.matchingMeasure_coupling :
  ∀ a b : ℝ, IsMeasureCoupling a b (matchingMeasure a b)
#evidence_check TransportSharpness.actual_coupling_probability :
  ∀ (a b : ℝ) (γ : Measure ((ℝ × ℝ) × (ℝ × ℝ))),
    0 ≤ a → a ≤ 1 → IsMeasureCoupling a b γ → IsProbabilityMeasure γ
#evidence_check TransportSharpness.atomicMeasure_zero_second_ae :
  ∀ a : ℝ, ∀ᵐ z ∂atomicMeasure a 0, z.2 = 0
#evidence_check TransportSharpness.coupling_zero_second_ae :
  ∀ (a b : ℝ) (γ : Measure ((ℝ × ℝ) × (ℝ × ℝ))),
    IsMeasureCoupling a b γ → ∀ᵐ z ∂γ, z.1.2 = 0
#evidence_check TransportSharpness.projectionPCost_measurable :
  ∀ p : ℝ, Measurable (projectionPCost p)
#evidence_check TransportSharpness.measurePCost_measurable :
  ∀ p : ℝ, Measurable (measurePCost p)
#evidence_check TransportSharpness.projectionPCost_le :
  ∀ p : ℝ, 0 < p → ∀ z : ((ℝ × ℝ) × (ℝ × ℝ)),
    z.1.2 = 0 → projectionPCost p z.2 ≤ measurePCost p z
#evidence_check TransportSharpness.atomicMeasure_projection_integral :
  ∀ a b p : ℝ, 0 ≤ a → 0 ≤ b → 0 < p →
    ∫⁻ z, projectionPCost p z ∂atomicMeasure a b = ENNReal.ofReal (a * b ^ p)
#evidence_check TransportSharpness.actual_coupling_lower_bound :
  ∀ (a b p : ℝ) (γ : Measure ((ℝ × ℝ) × (ℝ × ℝ))),
    0 ≤ a → 0 ≤ b → 0 < p → IsMeasureCoupling a b γ →
    ENNReal.ofReal (a * b ^ p) ≤ measureCost p γ
#evidence_check TransportSharpness.matchingMeasure_cost :
  ∀ a b p : ℝ, 0 ≤ a → 0 ≤ b → 0 < p →
    measureCost p (matchingMeasure a b) = ENNReal.ofReal (a * b ^ p)
#evidence_check TransportSharpness.actual_transportPowerInf :
  ∀ a b p : ℝ, 0 ≤ a → 0 ≤ b → 0 < p →
    transportPowerInf a b p = ENNReal.ofReal (a * b ^ p)
#evidence_check TransportSharpness.actual_transportPowerInf_finite :
  ∀ a b p : ℝ, 0 ≤ a → 0 ≤ b → 0 < p → transportPowerInf a b p < (∞ : ℝ≥0∞)
#evidence_check TransportSharpness.actual_transportDistance_eq :
  ∀ a b p : ℝ, 0 ≤ a → 0 ≤ b → 0 < p →
    (transportPowerInf a b p).toReal ^ (1 / p) = targetDistance a b p
#evidence_check TransportSharpness.actual_probability_transport :
  ∀ a b p : ℝ, 0 ≤ a → a ≤ 1 → 0 ≤ b → 1 ≤ p →
    IsProbabilityMeasure (atomicMeasure a 0) ∧
    IsProbabilityMeasure (atomicMeasure a b) ∧
    IsMeasureCoupling a b (matchingMeasure a b) ∧
    IsProbabilityMeasure (matchingMeasure a b) ∧
    measureCost p (matchingMeasure a b) = ENNReal.ofReal (a * b ^ p) ∧
    transportPowerInf a b p = ENNReal.ofReal (a * b ^ p)

end TransportSharpness
