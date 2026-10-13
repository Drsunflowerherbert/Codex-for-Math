import Mathlib

/-! Finite transport arithmetic. This file does not define Lebesgue-source
Brenier maps or identify their pushforwards; that bridge is documented separately. -/
namespace TransportSharpness

noncomputable section
open Finset

abbrev Atom := Fin 3
abbrev Plan := Atom → Atom → ℝ

def mass (a : ℝ) (i : Atom) : ℝ := if i = 1 then a else (1 - a) / 2

def IsCoupling (a : ℝ) (π : Plan) : Prop :=
  (∀ i j, 0 ≤ π i j) ∧
  (∀ i, ∑ j, π i j = mass a i) ∧
  (∀ j, ∑ i, π i j = mass a j)

def cost (c : Plan) (π : Plan) : ℝ := ∑ i, ∑ j, π i j * c i j

def matching (a : ℝ) : Plan := fun i j => if i = j then mass a i else 0

def sourcePoint (i : Atom) : ℝ × ℝ := if i = 0 then (-1, 0) else if i = 1 then (0, 0) else (1, 0)
def targetPoint (b : ℝ) (j : Atom) : ℝ × ℝ := if j = 0 then (-1, 0) else if j = 1 then (0, b) else (1, 0)

def sqCost (b : ℝ) (i j : Atom) : ℝ :=
  ((sourcePoint i).1 - (targetPoint b j).1) ^ 2 +
    ((sourcePoint i).2 - (targetPoint b j).2) ^ 2

def projectedCost (b : ℝ) (j : Atom) : ℝ := if j = 1 then b ^ 2 else 0

/-- Weak duality for arbitrary finite nonnegative plans with specified marginals. -/
theorem finite_dual_lower_bound (a : ℝ) (π c : Plan) (u v : Atom → ℝ)
    (hπ : IsCoupling a π) (hdual : ∀ i j, u i + v j ≤ c i j) :
    (∑ i, mass a i * u i) + (∑ j, mass a j * v j) ≤ cost c π := by
  rcases hπ with ⟨hn, hr, hc⟩
  calc
    _ = ∑ i, ∑ j, π i j * (u i + v j) := by
      simp_rw [mul_add, sum_add_distrib]
      congr 1
      · simp_rw [← sum_mul, hr]
      · rw [sum_comm]
        simp_rw [← sum_mul, hc]
    _ ≤ cost c π := sum_le_sum fun i _ => sum_le_sum fun j _ =>
      mul_le_mul_of_nonneg_left (hdual i j) (hn i j)

theorem mass_positive (a : ℝ) (ha : 0 < a) (ha1 : a < 1) (i : Atom) :
    0 < mass a i := by
  unfold mass
  split_ifs <;> linarith

theorem mass_sum (a : ℝ) : ∑ i, mass a i = 1 := by
  simp [Fin.sum_univ_succ, mass]
  ring

theorem matching_coupling (a : ℝ) (ha : 0 ≤ a) (ha1 : a ≤ 1) :
    IsCoupling a (matching a) := by
  refine ⟨?_, ?_, ?_⟩
  · intro i j
    simp only [matching]
    split_ifs
    · unfold mass
      split_ifs <;> linarith
    · exact le_rfl
  · intro i
    simp [matching]
  · intro j
    simp [matching]

theorem sqCost_ge_projected (b : ℝ) (i j : Atom) :
    projectedCost b j ≤ sqCost b i j := by
  fin_cases i <;> fin_cases j
  all_goals simp [sqCost, sourcePoint, targetPoint, projectedCost]
  all_goals nlinarith

theorem quadratic_lower_bound (a b : ℝ) (π : Plan) (hπ : IsCoupling a π) :
    a * b ^ 2 ≤ cost (sqCost b) π := by
  have h := finite_dual_lower_bound a π (sqCost b) (fun _ => 0) (projectedCost b)
    hπ (by simpa using sqCost_ge_projected b)
  simpa [Fin.sum_univ_succ, mass, projectedCost] using h

theorem matching_quadratic_cost (a b : ℝ) :
    cost (sqCost b) (matching a) = a * b ^ 2 := by
  simp [cost, Fin.sum_univ_succ, matching, mass, sqCost, sourcePoint, targetPoint]

/-- An attained finite quadratic optimum, stated without any measure-theory bridge. -/
theorem quadratic_minimum (a b : ℝ) (ha : 0 ≤ a) (ha1 : a ≤ 1) :
    IsCoupling a (matching a) ∧ cost (sqCost b) (matching a) = a * b ^ 2 ∧
    ∀ π, IsCoupling a π → a * b ^ 2 ≤ cost (sqCost b) π :=
  ⟨matching_coupling a ha ha1, matching_quadratic_cost a b,
    fun π hπ => quadratic_lower_bound a b π hπ⟩

def commonSource (a b : ℝ) : Plan := fun i j =>
  if i = j then (if i = 1 then a - b / 4 else (1-a)/2 - b/8)
  else if i = 1 ∨ j = 1 then b/8 else 0

def Admissible (a b : ℝ) : Prop := 0 < b ∧ b < a ∧ a + b < 1

theorem commonSource_coupling (a b : ℝ) (hab : Admissible a b) :
    IsCoupling a (commonSource a b) := by
  rcases hab with ⟨hb, hba, hab1⟩
  refine ⟨?_, ?_, ?_⟩
  · intro i j
    fin_cases i <;> fin_cases j <;> simp [commonSource] <;> linarith
  · intro i
    fin_cases i
    all_goals simp [Fin.sum_univ_succ, commonSource, mass]
    all_goals ring
  · intro j
    fin_cases j
    all_goals simp [Fin.sum_univ_succ, commonSource, mass]
    all_goals ring

def mapSquared (a b : ℝ) : ℝ := b / 2 + a * b ^ 2

theorem commonSource_cost (a b : ℝ) :
    cost (sqCost b) (commonSource a b) = mapSquared a b := by
  simp [cost, Fin.sum_univ_succ, commonSource, sqCost, sourcePoint, targetPoint, mapSquared]
  ring

theorem commonSource_strictly_costlier (a b : ℝ) (hb : 0 < b) :
    cost (sqCost b) (matching a) < cost (sqCost b) (commonSource a b) := by
  rw [matching_quadratic_cost, commonSource_cost, mapSquared]
  linarith

theorem shrinking_admissible (a : ℝ) (ha : 0 < a) (ha2 : a < 1/2) :
    Admissible a (a/2) := by
  constructor
  · linarith
  constructor <;> linarith

theorem shrinking_costs (a : ℝ) :
    cost (sqCost (a/2)) (matching a) = a ^ 3 / 4 ∧
    mapSquared a (a/2) = (a + a ^ 3) / 4 := by
  rw [matching_quadratic_cost]
  unfold mapSquared
  constructor <;> ring

/-- The Euclidean p-cost on the explicit two-dimensional atom locations. -/
def pCost (b p : ℝ) (i j : Atom) : ℝ := (sqCost b i j) ^ (p / 2)

def projectedPCost (b p : ℝ) (j : Atom) : ℝ := if j = 1 then b ^ p else 0

theorem square_rpow_half (b p : ℝ) (hb : 0 ≤ b) :
    (b ^ 2) ^ (p / 2) = b ^ p := by
  rw [← Real.rpow_natCast, ← Real.rpow_mul hb]
  congr 1
  ring

theorem pCost_ge_projected (b p : ℝ) (hb : 0 ≤ b) (hp : 0 < p) (i j : Atom) :
    projectedPCost b p j ≤ pCost b p i j := by
  by_cases hj : j = 1
  · subst j
    have h := Real.rpow_le_rpow (sq_nonneg b) (sqCost_ge_projected b i 1)
      (show 0 ≤ p/2 by linarith)
    simpa [pCost, projectedCost, projectedPCost, square_rpow_half b p hb] using h
  · simp only [projectedPCost, if_neg hj, pCost]
    exact Real.rpow_nonneg (by unfold sqCost; positivity) _

theorem pCost_matching (a b p : ℝ) (hb : 0 ≤ b) (hp : 0 < p) :
    cost (pCost b p) (matching a) = a * b ^ p := by
  simp [cost, Fin.sum_univ_succ, matching, mass, pCost, sqCost, sourcePoint,
    targetPoint, Real.zero_rpow (show p/2 ≠ 0 by linarith), square_rpow_half b p hb]

/-- Exact attained finite p-cost optimum; no assumption that p-cost defines the maps. -/
theorem pCost_minimum (a b p : ℝ) (ha : 0 ≤ a) (ha1 : a ≤ 1)
    (hb : 0 ≤ b) (hp : 0 < p) :
    IsCoupling a (matching a) ∧ cost (pCost b p) (matching a) = a * b ^ p ∧
    ∀ π, IsCoupling a π → a * b ^ p ≤ cost (pCost b p) π := by
  refine ⟨matching_coupling a ha ha1, pCost_matching a b p hb hp, ?_⟩
  intro π hπ
  have h := finite_dual_lower_bound a π (pCost b p) (fun _ => 0) (projectedPCost b p)
    hπ (by simpa using pCost_ge_projected b p hb hp)
  simpa [Fin.sum_univ_succ, mass, projectedPCost] using h

end
end TransportSharpness
