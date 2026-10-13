import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: a23164053f2c7cb1388791d01432fe1b59ea63df65f84caf8a38e61762ebcd81
-- Numeric-only trusted transcription; no parser refinement theorem.
namespace CheckedInput

def problem : InputProblem 1 0 :=
  ({
    a := ![],
    b := ![],
    senses := ![],
    c := ![((1 : ℚ) / 2)],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 1 0)

def point : Fin 1 → ℚ := ![(0 : ℚ)]

def direction : Fin 1 → ℚ := ![(2 : ℚ)]

theorem accepted : checkInputUnbounded problem point direction = true := by decide +kernel

theorem sound : ∀ B : ℝ, ∃ y : Fin 1 → ℝ, InputFeasible problem y ∧ ObjectiveBeyond problem B y :=
  inputUnbounded_sound_real problem point direction accepted

#evidence_definition CheckedInput.problem =
  ({
    a := ![],
    b := ![],
    senses := ![],
    c := ![((1 : ℚ) / 2)],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 1 0)
#evidence_check CheckedInput.accepted : checkInputUnbounded problem point direction = true
#evidence_check CheckedInput.sound : ∀ B : ℝ, ∃ y : Fin 1 → ℝ, InputFeasible problem y ∧ ObjectiveBeyond problem B y
#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]

end CheckedInput
