import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: 88cd1b3c18d3989c872248fc379e2759e9cd5f6b747682de9ff884b67f24a306
-- Numeric-only trusted transcription; no parser refinement theorem.
namespace CheckedInput

def problem : InputProblem 0 2 :=
  ({
    a := ![![], ![]],
    b := ![(0 : ℚ), (0 : ℚ)],
    senses := ![RowSense.le, RowSense.eq],
    c := ![],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 0 2)

def point : Fin 0 → ℚ := ![]

def weights : Fin 2 → ℚ := ![(0 : ℚ), (-7 : ℚ)]

theorem accepted : checkInputOptimal problem point weights = true := by decide +kernel

theorem sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 0 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y :=
  inputOptimal_sound_real problem point weights accepted

#evidence_definition CheckedInput.problem =
  ({
    a := ![![], ![]],
    b := ![(0 : ℚ), (0 : ℚ)],
    senses := ![RowSense.le, RowSense.eq],
    c := ![],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 0 2)
#evidence_check CheckedInput.accepted : checkInputOptimal problem point weights = true
#evidence_check CheckedInput.sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 0 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y
#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]

end CheckedInput
