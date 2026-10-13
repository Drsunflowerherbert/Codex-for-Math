import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: 732b0c0505f89afbfe24ae0949f834e2c2322cc2043ba17281041449f91cc5b0
-- Numeric-only trusted transcription; no parser refinement theorem.
namespace CheckedInput

def problem : InputProblem 2 5 :=
  ({
    a := ![![(1 : ℚ), (1 : ℚ)], ![(2 : ℚ), (2 : ℚ)], ![(1 : ℚ), (0 : ℚ)], ![(0 : ℚ), (1 : ℚ)], ![(1 : ℚ), (-1 : ℚ)]],
    b := ![(4 : ℚ), (8 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)],
    senses := ![RowSense.le, RowSense.le, RowSense.ge, RowSense.ge, RowSense.eq],
    c := ![(3 : ℚ), (2 : ℚ)],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 2 5)

def point : Fin 2 → ℚ := ![(2 : ℚ), (2 : ℚ)]

def weights : Fin 5 → ℚ := ![(1 : ℚ), ((3 : ℚ) / 4), (0 : ℚ), (0 : ℚ), ((1 : ℚ) / 2)]

theorem accepted : checkInputOptimal problem point weights = true := by decide +kernel

theorem sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 2 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y :=
  inputOptimal_sound_real problem point weights accepted

#evidence_definition CheckedInput.problem =
  ({
    a := ![![(1 : ℚ), (1 : ℚ)], ![(2 : ℚ), (2 : ℚ)], ![(1 : ℚ), (0 : ℚ)], ![(0 : ℚ), (1 : ℚ)], ![(1 : ℚ), (-1 : ℚ)]],
    b := ![(4 : ℚ), (8 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)],
    senses := ![RowSense.le, RowSense.le, RowSense.ge, RowSense.ge, RowSense.eq],
    c := ![(3 : ℚ), (2 : ℚ)],
    objectiveSense := ObjectiveSense.maximize
  } : InputProblem 2 5)
#evidence_check CheckedInput.accepted : checkInputOptimal problem point weights = true
#evidence_check CheckedInput.sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 2 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y
#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]

end CheckedInput
