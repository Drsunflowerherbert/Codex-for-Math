import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: 7b936aa9d61590c2cd49ff916f5455ac1d8d66b79d79d8e51b1772c8af585ed9
-- Numeric-only trusted transcription; no parser refinement theorem.
namespace CheckedInput

def problem : InputProblem 0 0 :=
  ({
    a := ![],
    b := ![],
    senses := ![],
    c := ![],
    objectiveSense := ObjectiveSense.minimize
  } : InputProblem 0 0)

def point : Fin 0 → ℚ := ![]

def weights : Fin 0 → ℚ := ![]

theorem accepted : checkInputOptimal problem point weights = true := by decide +kernel

theorem sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 0 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y :=
  inputOptimal_sound_real problem point weights accepted

#evidence_definition CheckedInput.problem =
  ({
    a := ![],
    b := ![],
    senses := ![],
    c := ![],
    objectiveSense := ObjectiveSense.minimize
  } : InputProblem 0 0)
#evidence_check CheckedInput.accepted : checkInputOptimal problem point weights = true
#evidence_check CheckedInput.sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 0 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y
#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]

end CheckedInput
