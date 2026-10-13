import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: d0316520a879726ad1533106b932a18289aaa444088677405c705a0e20132031
-- Numeric-only trusted transcription; no parser refinement theorem.
namespace CheckedInput

def problem : InputProblem 2 3 :=
  ({
    a := ![![(0 : ℚ), (1 : ℚ)], ![(0 : ℚ), (2 : ℚ)], ![(1 : ℚ), (-1 : ℚ)]],
    b := ![(0 : ℚ), (0 : ℚ), (1 : ℚ)],
    senses := ![RowSense.ge, RowSense.ge, RowSense.eq],
    c := ![(-2 : ℚ), (1 : ℚ)],
    objectiveSense := ObjectiveSense.minimize
  } : InputProblem 2 3)

def point : Fin 2 → ℚ := ![(1 : ℚ), (0 : ℚ)]

def direction : Fin 2 → ℚ := ![(1 : ℚ), (1 : ℚ)]

theorem accepted : checkInputUnbounded problem point direction = true := by decide +kernel

theorem sound : ∀ B : ℝ, ∃ y : Fin 2 → ℝ, InputFeasible problem y ∧ ObjectiveBeyond problem B y :=
  inputUnbounded_sound_real problem point direction accepted

#evidence_definition CheckedInput.problem =
  ({
    a := ![![(0 : ℚ), (1 : ℚ)], ![(0 : ℚ), (2 : ℚ)], ![(1 : ℚ), (-1 : ℚ)]],
    b := ![(0 : ℚ), (0 : ℚ), (1 : ℚ)],
    senses := ![RowSense.ge, RowSense.ge, RowSense.eq],
    c := ![(-2 : ℚ), (1 : ℚ)],
    objectiveSense := ObjectiveSense.minimize
  } : InputProblem 2 3)
#evidence_check CheckedInput.accepted : checkInputUnbounded problem point direction = true
#evidence_check CheckedInput.sound : ∀ B : ℝ, ∃ y : Fin 2 → ℝ, InputFeasible problem y ∧ ObjectiveBeyond problem B y
#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]

end CheckedInput
