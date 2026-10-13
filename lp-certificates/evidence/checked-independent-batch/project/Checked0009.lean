import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: 0330573e32bcb7650dd4fecc98f9e3da1150a2fa2f2d5eeac8b9fcdbbe57405f
-- Numeric-only trusted transcription; no parser refinement theorem.
namespace CheckedInput

def problem : InputProblem 2 5 :=
  ({
    a := ![![(1 : ℚ), (-1 : ℚ)], ![(1 : ℚ), (0 : ℚ)], ![(2 : ℚ), (-2 : ℚ)], ![(3 : ℚ), (3 : ℚ)], ![(1 : ℚ), (0 : ℚ)]],
    b := ![(0 : ℚ), (1 : ℚ), (0 : ℚ), (6 : ℚ), (4 : ℚ)],
    senses := ![RowSense.eq, RowSense.ge, RowSense.eq, RowSense.ge, RowSense.le],
    c := ![(1 : ℚ), (2 : ℚ)],
    objectiveSense := ObjectiveSense.minimize
  } : InputProblem 2 5)

def point : Fin 2 → ℚ := ![(1 : ℚ), (1 : ℚ)]

def weights : Fin 5 → ℚ := ![(2 : ℚ), (3 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

theorem accepted : checkInputOptimal problem point weights = true := by decide +kernel

theorem sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 2 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y :=
  inputOptimal_sound_real problem point weights accepted

#evidence_definition CheckedInput.problem =
  ({
    a := ![![(1 : ℚ), (-1 : ℚ)], ![(1 : ℚ), (0 : ℚ)], ![(2 : ℚ), (-2 : ℚ)], ![(3 : ℚ), (3 : ℚ)], ![(1 : ℚ), (0 : ℚ)]],
    b := ![(0 : ℚ), (1 : ℚ), (0 : ℚ), (6 : ℚ), (4 : ℚ)],
    senses := ![RowSense.eq, RowSense.ge, RowSense.eq, RowSense.ge, RowSense.le],
    c := ![(1 : ℚ), (2 : ℚ)],
    objectiveSense := ObjectiveSense.minimize
  } : InputProblem 2 5)
#evidence_check CheckedInput.accepted : checkInputOptimal problem point weights = true
#evidence_check CheckedInput.sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 2 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y
#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]

end CheckedInput
