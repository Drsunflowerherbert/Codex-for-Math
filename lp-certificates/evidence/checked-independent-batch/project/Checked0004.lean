import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: cb55a77035eeaaf89afcbe345111f5dbd612cd82393b37359c2cf9cecc882b85
-- Numeric-only trusted transcription; no parser refinement theorem.
namespace CheckedInput

def problem : InputProblem 1 2 :=
  ({
    a := ![![(1 : ℚ)], ![(3 : ℚ)]],
    b := ![(0 : ℚ), (1 : ℚ)],
    senses := ![RowSense.ge, RowSense.eq],
    c := ![((3 : ℚ) / 2)],
    objectiveSense := ObjectiveSense.minimize
  } : InputProblem 1 2)

def point : Fin 1 → ℚ := ![((1 : ℚ) / 3)]

def weights : Fin 2 → ℚ := ![(0 : ℚ), ((-1 : ℚ) / 2)]

theorem accepted : checkInputOptimal problem point weights = true := by decide +kernel

theorem sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 1 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y :=
  inputOptimal_sound_real problem point weights accepted

#evidence_definition CheckedInput.problem =
  ({
    a := ![![(1 : ℚ)], ![(3 : ℚ)]],
    b := ![(0 : ℚ), (1 : ℚ)],
    senses := ![RowSense.ge, RowSense.eq],
    c := ![((3 : ℚ) / 2)],
    objectiveSense := ObjectiveSense.minimize
  } : InputProblem 1 2)
#evidence_check CheckedInput.accepted : checkInputOptimal problem point weights = true
#evidence_check CheckedInput.sound : InputFeasible problem (realVector point) ∧
  ∀ y : Fin 1 → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y
#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]

end CheckedInput
