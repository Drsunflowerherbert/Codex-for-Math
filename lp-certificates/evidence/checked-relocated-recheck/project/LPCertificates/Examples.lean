import LPCertificates.Rational

/-! Hand-transcribed exact examples. Matching JSON fixtures are reviewed separately;
there is no formally proved JSON parser or extraction relation. `decide` generates
kernel-checked proofs; no native evaluation oracle is used. -/

namespace LPCertificates

def mixedRedundant : Problem ℚ 2 4 1 where
  A := ![![1, 1], ![2, 2], ![-1, 0], ![0, -1]]
  b := ![4, 8, 0, 0]
  E := ![![1, -1]]
  f := ![0]
  c := ![3, 2]

theorem mixedRedundant_accepts :
    checkOptimal mixedRedundant ![2, 2] ![1, 3/4, 0, 0] ![1/2] = true := by decide +kernel

theorem mixedRedundant_alternative_accepts :
    checkOptimal mixedRedundant ![2, 2] ![5/2, 0, 0, 0] ![1/2] = true := by decide +kernel

theorem mixedRedundant_real_optimal :
    Feasible (realProblem mixedRedundant) (realVector ![2, 2]) ∧
    ∀ y : Fin 2 → ℝ, Feasible (realProblem mixedRedundant) y →
      dot (realProblem mixedRedundant).c y ≤ dot (realProblem mixedRedundant).c (realVector ![2, 2]) :=
  checkOptimal_sound_real mixedRedundant ![2, 2] ![1, 3/4, 0, 0] ![1/2]
    mixedRedundant_accepts

theorem negative_multiplier_rejected :
    checkOptimal mixedRedundant ![2, 2] ![-1, 7/4, 0, 0] ![1/2] = false := by decide +kernel

theorem infeasible_point_rejected :
    checkOptimal mixedRedundant ![3, 3] ![1, 3/4, 0, 0] ![1/2] = false := by decide +kernel

def singletonMin : Problem ℚ 1 1 1 where
  A := ![![-1]]
  b := ![0]
  E := ![![3]]
  f := ![1]
  c := ![-3/2]

theorem singletonMin_accepts :
    checkOptimal singletonMin ![1/3] ![0] ![-1/2] = true := by decide +kernel

def contradiction : Problem ℚ 1 2 0 where
  A := ![![1], ![-1]]
  b := ![0, -1]
  E := ![]
  f := ![]
  c := ![0]

theorem contradiction_accepts : checkInfeasible contradiction ![1, 1] ![] = true := by decide +kernel

theorem contradiction_real_infeasible :
    ¬ ∃ x : Fin 1 → ℝ, Feasible (realProblem contradiction) x :=
  checkInfeasible_sound_real contradiction ![1, 1] ![] contradiction_accepts

theorem nonstrict_contradiction_rejected :
    checkInfeasible contradiction ![0, 0] ![] = false := by decide +kernel

def equalityContradiction : Problem ℚ 2 0 2 where
  A := ![]
  b := ![]
  E := ![![1, 1], ![2, 2]]
  f := ![0, 1]
  c := ![-3, 4]

theorem equalityContradiction_accepts :
    checkInfeasible equalityContradiction ![] ![2, -1] = true := by decide +kernel

def lineRayMin : Problem ℚ 2 2 1 where
  A := ![![0, -1], ![0, -2]]
  b := ![0, 0]
  E := ![![1, -1]]
  f := ![1]
  c := ![2, -1]

theorem lineRayMin_accepts :
    checkUnbounded lineRayMin ![1, 0] ![1, 1] = true := by decide +kernel

theorem lineRayMin_real_unbounded :
    ∀ B : ℝ, ∃ y : Fin 2 → ℝ, Feasible (realProblem lineRayMin) y ∧
      B < dot (realProblem lineRayMin).c y :=
  checkUnbounded_sound_real lineRayMin ![1, 0] ![1, 1] lineRayMin_accepts

theorem zero_gain_rejected : checkUnbounded lineRayMin ![1, 0] ![0, 0] = false := by decide +kernel

theorem bad_base_rejected : checkUnbounded lineRayMin ![0, 0] ![1, 1] = false := by decide +kernel

theorem bad_direction_rejected :
    checkUnbounded lineRayMin ![1, 0] ![1, 0] = false := by decide +kernel

def zeroVariableFeasible : Problem ℚ 0 1 1 where
  A := ![![]]
  b := ![0]
  E := ![![]]
  f := ![0]
  c := ![]

theorem zeroVariableFeasible_accepts :
    checkOptimal zeroVariableFeasible ![] ![0] ![-7] = true := by decide +kernel

def zeroVariableInfeasible : Problem ℚ 0 1 0 where
  A := ![![]]
  b := ![-1]
  E := ![]
  f := ![]
  c := ![]

theorem zeroVariableInfeasible_accepts :
    checkInfeasible zeroVariableInfeasible ![1] ![] = true := by decide +kernel

def freeRay : Problem ℚ 1 0 0 where
  A := ![]
  b := ![]
  E := ![]
  f := ![]
  c := ![1/2]

theorem freeRay_accepts : checkUnbounded freeRay ![0] ![2] = true := by decide +kernel

def constantNoRows : Problem ℚ 2 0 0 where
  A := ![]
  b := ![]
  E := ![]
  f := ![]
  c := ![0, 0]

theorem constantNoRows_accepts :
    checkOptimal constantNoRows ![7, -2/3] ![] ![] = true := by decide +kernel

end LPCertificates
