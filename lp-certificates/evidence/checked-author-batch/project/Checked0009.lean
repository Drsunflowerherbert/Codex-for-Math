import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: 5a5de45c186cae9a39039218046ce832493fec15f444e91a5be82069a8b7f75d
-- Numeric-only trusted transcription; no parser refinement theorem.
namespace CheckedInput

def problem : InputProblem 2 4 :=
  ({
    a := ![![(1 : ℚ), (1 : ℚ)], ![(1 : ℚ), (0 : ℚ)], ![(0 : ℚ), (1 : ℚ)], ![(1 : ℚ), (-1 : ℚ)]],
    b := ![(4 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)],
    senses := ![RowSense.le, RowSense.ge, RowSense.ge, RowSense.eq],
    c := ![(3 : ℚ), (2 : ℚ)],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 2 4)

def point : Fin 2 → ℚ := ![(2 : ℚ), (2 : ℚ)]

def weights : Fin 4 → ℚ := ![((5 : ℚ) / 2), (0 : ℚ), (0 : ℚ), ((1 : ℚ) / 2)]

theorem accepted : checkInputOptimal problem point weights = true := by decide +kernel

theorem sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 2 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y :=
  inputOptimal_sound_real problem point weights accepted

#evidence_definition CheckedInput.problem =
  ({
    a := ![![(1 : ℚ), (1 : ℚ)], ![(1 : ℚ), (0 : ℚ)], ![(0 : ℚ), (1 : ℚ)], ![(1 : ℚ), (-1 : ℚ)]],
    b := ![(4 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)],
    senses := ![RowSense.le, RowSense.ge, RowSense.ge, RowSense.eq],
    c := ![(3 : ℚ), (2 : ℚ)],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 2 4)
#evidence_check CheckedInput.accepted : checkInputOptimal problem point weights = true
#evidence_check CheckedInput.sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 2 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y
#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]

end CheckedInput
