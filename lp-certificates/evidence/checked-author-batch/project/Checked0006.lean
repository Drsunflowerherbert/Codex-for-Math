import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: 9b9d97fb32e1e3ca358a836936e09d894c2564db4f810d843d9b7f5752450879
-- Numeric-only trusted transcription; no parser refinement theorem.
namespace CheckedInput

def problem : InputProblem 0 1 :=
  ({
    a := ![![]],
    b := ![(1 : ℚ)],
    senses := ![RowSense.ge],
    c := ![],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 0 1)

def weights : Fin 1 → ℚ := ![(1 : ℚ)]

theorem accepted : checkInputInfeasible problem weights = true := by decide +kernel

theorem sound : ¬ ∃ y : Fin 0 → ℝ, InputFeasible problem y :=
  inputInfeasible_sound_real problem weights accepted

#evidence_definition CheckedInput.problem =
  ({
    a := ![![]],
    b := ![(1 : ℚ)],
    senses := ![RowSense.ge],
    c := ![],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 0 1)
#evidence_check CheckedInput.accepted : checkInputInfeasible problem weights = true
#evidence_check CheckedInput.sound : ¬ ∃ y : Fin 0 → ℝ, InputFeasible problem y
#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]

end CheckedInput
