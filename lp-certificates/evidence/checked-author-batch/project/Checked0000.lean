import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: de17f39dc860659d49d045cb621b7e44202f9d2230725f78320c6a1a5fdaee9e
-- Numeric-only trusted transcription; no parser refinement theorem.
namespace CheckedInput

def problem : InputProblem 2 0 :=
  ({
    a := ![],
    b := ![],
    senses := ![],
    c := ![(0 : ℚ), (0 : ℚ)],
    objectiveSense := ObjectiveSense.minimize
  } : InputProblem 2 0)

def point : Fin 2 → ℚ := ![(7 : ℚ), ((-2 : ℚ) / 3)]

def weights : Fin 0 → ℚ := ![]

theorem accepted : checkInputOptimal problem point weights = true := by decide +kernel

theorem sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 2 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y :=
  inputOptimal_sound_real problem point weights accepted

#evidence_definition CheckedInput.problem =
  ({
    a := ![],
    b := ![],
    senses := ![],
    c := ![(0 : ℚ), (0 : ℚ)],
    objectiveSense := ObjectiveSense.minimize
  } : InputProblem 2 0)
#evidence_check CheckedInput.accepted : checkInputOptimal problem point weights = true
#evidence_check CheckedInput.sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 2 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y
#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]

end CheckedInput
