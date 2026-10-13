import TransportSharpness
import EvidenceHarness

/-!
Independent statement and definition-body review for the finite/scalar core.
Every expected term below is closed. No target theorem is specialized, and no
expected theorem type is obtained by reading a target's type programmatically.
The ordinary Lebesgue-source/Brenier bridge is outside this harness.
-/
namespace TransportSharpness
open Finset

#evidence_check TransportSharpness.Atom : Type
#evidence_check TransportSharpness.Plan : Type
#evidence_check TransportSharpness.mass : ℝ → Fin 3 → ℝ
#evidence_check TransportSharpness.IsCoupling : ℝ → (Fin 3 → Fin 3 → ℝ) → Prop
#evidence_check TransportSharpness.cost : (Fin 3 → Fin 3 → ℝ) → (Fin 3 → Fin 3 → ℝ) → ℝ
#evidence_check TransportSharpness.matching : ℝ → Fin 3 → Fin 3 → ℝ
#evidence_check TransportSharpness.sourcePoint : Fin 3 → ℝ × ℝ
#evidence_check TransportSharpness.targetPoint : ℝ → Fin 3 → ℝ × ℝ
#evidence_check TransportSharpness.sqCost : ℝ → Fin 3 → Fin 3 → ℝ
#evidence_check TransportSharpness.projectedCost : ℝ → Fin 3 → ℝ
#evidence_check TransportSharpness.commonSource : ℝ → ℝ → Fin 3 → Fin 3 → ℝ
#evidence_check TransportSharpness.Admissible : ℝ → ℝ → Prop
#evidence_check TransportSharpness.mapSquared : ℝ → ℝ → ℝ
#evidence_check TransportSharpness.pCost : ℝ → ℝ → Fin 3 → Fin 3 → ℝ
#evidence_check TransportSharpness.projectedPCost : ℝ → ℝ → Fin 3 → ℝ
#evidence_check TransportSharpness.mapSize : ℝ → ℝ → ℝ
#evidence_check TransportSharpness.targetDistance : ℝ → ℝ → ℝ → ℝ
#evidence_check TransportSharpness.ceiling : ℝ → ℝ
#evidence_check TransportSharpness.exponent : ℝ → ℝ → ℝ

#evidence_definition TransportSharpness.Atom = Fin 3
#evidence_definition TransportSharpness.Plan = Fin 3 → Fin 3 → ℝ
#evidence_definition TransportSharpness.mass = fun (a : ℝ) (i : Fin 3) =>
  if i = 1 then a else (1 - a) / 2
#evidence_definition TransportSharpness.IsCoupling = fun (a : ℝ) (π : Fin 3 → Fin 3 → ℝ) =>
  (∀ i j, 0 ≤ π i j) ∧ (∀ i, ∑ j, π i j = mass a i) ∧
  (∀ j, ∑ i, π i j = mass a j)
#evidence_definition TransportSharpness.cost = fun (c π : Fin 3 → Fin 3 → ℝ) =>
  ∑ i, ∑ j, π i j * c i j
#evidence_definition TransportSharpness.matching = fun (a : ℝ) (i j : Fin 3) =>
  if i = j then mass a i else 0
#evidence_definition TransportSharpness.sourcePoint = fun i : Fin 3 =>
  if i = 0 then ((-1 : ℝ), (0 : ℝ)) else if i = 1 then (0, 0) else (1, 0)
#evidence_definition TransportSharpness.targetPoint = fun (b : ℝ) (j : Fin 3) =>
  if j = 0 then ((-1 : ℝ), (0 : ℝ)) else if j = 1 then (0, b) else (1, 0)
#evidence_definition TransportSharpness.sqCost = fun (b : ℝ) (i j : Fin 3) =>
  ((sourcePoint i).1 - (targetPoint b j).1) ^ 2 +
  ((sourcePoint i).2 - (targetPoint b j).2) ^ 2
#evidence_definition TransportSharpness.projectedCost = fun (b : ℝ) (j : Fin 3) =>
  if j = 1 then b ^ 2 else 0
#evidence_definition TransportSharpness.commonSource = fun (a b : ℝ) (i j : Fin 3) =>
  if i = j then (if i = 1 then a - b / 4 else (1 - a) / 2 - b / 8)
  else if i = 1 ∨ j = 1 then b / 8 else 0
#evidence_definition TransportSharpness.Admissible = fun a b : ℝ =>
  0 < b ∧ b < a ∧ a + b < 1
#evidence_definition TransportSharpness.mapSquared = fun a b : ℝ => b / 2 + a * b ^ 2
#evidence_definition TransportSharpness.pCost = fun (b p : ℝ) (i j : Fin 3) =>
  (sqCost b i j) ^ (p / 2)
#evidence_definition TransportSharpness.projectedPCost = fun (b p : ℝ) (j : Fin 3) =>
  if j = 1 then b ^ p else 0
#evidence_definition TransportSharpness.mapSize = fun a b : ℝ => Real.sqrt (mapSquared a b)
#evidence_definition TransportSharpness.targetDistance = fun a b p : ℝ => a ^ (1 / p) * b
#evidence_definition TransportSharpness.ceiling = fun p : ℝ => p / (2 * (p + 1))
#evidence_definition TransportSharpness.exponent = fun p α : ℝ => 1 / 2 - α * (1 + 1 / p)

#evidence_check TransportSharpness.finite_dual_lower_bound :
  ∀ (a : ℝ) (π c : Fin 3 → Fin 3 → ℝ) (u v : Fin 3 → ℝ),
    IsCoupling a π → (∀ i j, u i + v j ≤ c i j) →
    (∑ i, mass a i * u i) + (∑ j, mass a j * v j) ≤ cost c π
#evidence_check TransportSharpness.mass_positive :
  ∀ (a : ℝ), 0 < a → a < 1 → ∀ i : Fin 3, 0 < mass a i
#evidence_check TransportSharpness.mass_sum : ∀ a : ℝ, ∑ i, mass a i = 1
#evidence_check TransportSharpness.matching_coupling :
  ∀ a : ℝ, 0 ≤ a → a ≤ 1 → IsCoupling a (matching a)
#evidence_check TransportSharpness.sqCost_ge_projected :
  ∀ (b : ℝ) (i j : Fin 3), projectedCost b j ≤ sqCost b i j
#evidence_check TransportSharpness.quadratic_lower_bound :
  ∀ (a b : ℝ) (π : Fin 3 → Fin 3 → ℝ), IsCoupling a π →
    a * b ^ 2 ≤ cost (sqCost b) π
#evidence_check TransportSharpness.matching_quadratic_cost :
  ∀ a b : ℝ, cost (sqCost b) (matching a) = a * b ^ 2
#evidence_check TransportSharpness.quadratic_minimum :
  ∀ a b : ℝ, 0 ≤ a → a ≤ 1 →
    IsCoupling a (matching a) ∧ cost (sqCost b) (matching a) = a * b ^ 2 ∧
    ∀ π, IsCoupling a π → a * b ^ 2 ≤ cost (sqCost b) π
#evidence_check TransportSharpness.commonSource_coupling :
  ∀ a b : ℝ, Admissible a b → IsCoupling a (commonSource a b)
#evidence_check TransportSharpness.commonSource_cost :
  ∀ a b : ℝ, cost (sqCost b) (commonSource a b) = mapSquared a b
#evidence_check TransportSharpness.commonSource_strictly_costlier :
  ∀ a b : ℝ, 0 < b → cost (sqCost b) (matching a) < cost (sqCost b) (commonSource a b)
#evidence_check TransportSharpness.shrinking_admissible :
  ∀ a : ℝ, 0 < a → a < 1 / 2 → Admissible a (a / 2)
#evidence_check TransportSharpness.shrinking_costs :
  ∀ a : ℝ, cost (sqCost (a / 2)) (matching a) = a ^ 3 / 4 ∧
    mapSquared a (a / 2) = (a + a ^ 3) / 4
#evidence_check TransportSharpness.square_rpow_half :
  ∀ b p : ℝ, 0 ≤ b → (b ^ 2) ^ (p / 2) = b ^ p
#evidence_check TransportSharpness.pCost_ge_projected :
  ∀ b p : ℝ, 0 ≤ b → 0 < p → ∀ i j : Fin 3,
    projectedPCost b p j ≤ pCost b p i j
#evidence_check TransportSharpness.pCost_matching :
  ∀ a b p : ℝ, 0 ≤ b → 0 < p → cost (pCost b p) (matching a) = a * b ^ p
#evidence_check TransportSharpness.pCost_minimum :
  ∀ a b p : ℝ, 0 ≤ a → a ≤ 1 → 0 ≤ b → 0 < p →
    IsCoupling a (matching a) ∧ cost (pCost b p) (matching a) = a * b ^ p ∧
    ∀ π, IsCoupling a π → a * b ^ p ≤ cost (pCost b p) π
#evidence_check TransportSharpness.exponent_negative :
  ∀ p α : ℝ, 0 < p → ceiling p < α → exponent p α < 0
#evidence_check TransportSharpness.targetDistance_positive :
  ∀ a b p : ℝ, 0 < a → 0 < b → 0 < targetDistance a b p
#evidence_check TransportSharpness.targetDistance_power :
  ∀ a b p : ℝ, 0 < a → 0 ≤ b → p ≠ 0 → (targetDistance a b p) ^ p = a * b ^ p
#evidence_check TransportSharpness.targetDistance_shrinking :
  ∀ a p : ℝ, 0 < a → targetDistance a (a / 2) p = a ^ (1 + 1 / p) / 2
#evidence_check TransportSharpness.mapSize_shrinking_lower :
  ∀ a : ℝ, 0 < a → Real.sqrt a / 2 ≤ mapSize a (a / 2)
#evidence_check TransportSharpness.shrinking_ratio_lower :
  ∀ a p α : ℝ, 0 < a → (2 : ℝ) ^ α / 2 * a ^ (exponent p α) ≤
    mapSize a (a / 2) / (targetDistance a (a / 2) p) ^ α
#evidence_check TransportSharpness.ceiling_values : ceiling 2 = 1 / 3 ∧ ceiling 1 = 1 / 4
#evidence_check TransportSharpness.shrinking_exceeds_constant :
  ∀ p α C : ℝ, 1 ≤ p → ceiling p < α →
    ∃ a : ℝ, 0 < a ∧ a < 1 / 2 ∧ Admissible a (a / 2) ∧
      C * (targetDistance a (a / 2) p) ^ α < mapSize a (a / 2)
#evidence_check TransportSharpness.W2_exceeds_constant :
  ∀ α C : ℝ, 1 / 3 < α →
    ∃ a : ℝ, 0 < a ∧ a < 1 / 2 ∧ Admissible a (a / 2) ∧
      C * (targetDistance a (a / 2) 2) ^ α < mapSize a (a / 2)
#evidence_check TransportSharpness.mapSize_fixed_lower :
  ∀ a b : ℝ, 0 ≤ a → 0 < b → Real.sqrt b / Real.sqrt 2 ≤ mapSize a b
#evidence_check TransportSharpness.fixed_ratio_lower :
  ∀ a b p α : ℝ, 0 < a → 0 < b →
    ((a ^ (1 / p)) ^ (-α) / Real.sqrt 2) * b ^ (1 / 2 - α) ≤
      mapSize a b / (targetDistance a b p) ^ α
#evidence_check TransportSharpness.fixed_mass_exceeds_constant :
  ∀ a p α C : ℝ, 0 < a → a < 1 → 1 / 2 < α →
    ∃ b : ℝ, Admissible a b ∧ C * (targetDistance a b p) ^ α < mapSize a b

end TransportSharpness
