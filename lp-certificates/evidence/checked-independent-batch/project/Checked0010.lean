import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: e48cddadb9bad0928f44c28a91da3b1d47a5319fc977ffd10b72dc5b99df6b6e
-- Numeric-only trusted transcription; no parser refinement theorem.
namespace CheckedInput

def problem : InputProblem 2 2 :=
  ({
    a := ![![(0 : ℚ), (1 : ℚ)], ![(1 : ℚ), (0 : ℚ)]],
    b := ![(1 : ℚ), (0 : ℚ)],
    senses := ![RowSense.eq, RowSense.le],
    c := ![(-3 : ℚ), (2 : ℚ)],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 2 2)

def point : Fin 2 → ℚ := ![(-2 : ℚ), (1 : ℚ)]

def direction : Fin 2 → ℚ := ![(-1 : ℚ), (0 : ℚ)]

theorem accepted : checkInputUnbounded problem point direction = true := by decide +kernel

theorem sound : ∀ B : ℝ, ∃ y : Fin 2 → ℝ, InputFeasible problem y ∧ ObjectiveBeyond problem B y :=
  inputUnbounded_sound_real problem point direction accepted

#evidence_definition CheckedInput.problem =
  ({
    a := ![![(0 : ℚ), (1 : ℚ)], ![(1 : ℚ), (0 : ℚ)]],
    b := ![(1 : ℚ), (0 : ℚ)],
    senses := ![RowSense.eq, RowSense.le],
    c := ![(-3 : ℚ), (2 : ℚ)],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 2 2)
#evidence_check CheckedInput.accepted : checkInputUnbounded problem point direction = true
#evidence_check CheckedInput.sound : ∀ B : ℝ, ∃ y : Fin 2 → ℝ, InputFeasible problem y ∧ ObjectiveBeyond problem B y
#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]

end CheckedInput
