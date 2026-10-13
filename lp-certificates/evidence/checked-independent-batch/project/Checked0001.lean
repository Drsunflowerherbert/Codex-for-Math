import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: 9181439e9e032cbda9d9ff8a094b4b344023fc1efe9b157be8a317ffe9c412b9
-- Numeric-only trusted transcription; no parser refinement theorem.
namespace CheckedInput

def problem : InputProblem 1 2 :=
  ({
    a := ![![(1 : ℚ)], ![(1 : ℚ)]],
    b := ![(0 : ℚ), (1 : ℚ)],
    senses := ![RowSense.le, RowSense.ge],
    c := ![(0 : ℚ)],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 1 2)

def weights : Fin 2 → ℚ := ![(1 : ℚ), (1 : ℚ)]

theorem accepted : checkInputInfeasible problem weights = true := by decide +kernel

theorem sound : ¬ ∃ y : Fin 1 → ℝ, InputFeasible problem y :=
  inputInfeasible_sound_real problem weights accepted

#evidence_definition CheckedInput.problem =
  ({
    a := ![![(1 : ℚ)], ![(1 : ℚ)]],
    b := ![(0 : ℚ), (1 : ℚ)],
    senses := ![RowSense.le, RowSense.ge],
    c := ![(0 : ℚ)],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 1 2)
#evidence_check CheckedInput.accepted : checkInputInfeasible problem weights = true
#evidence_check CheckedInput.sound : ¬ ∃ y : Fin 1 → ℝ, InputFeasible problem y
#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]

end CheckedInput
