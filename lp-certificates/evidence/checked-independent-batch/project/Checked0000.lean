import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: 794b487665af27e5a7066deb6ec1b0c4b0ecc46d48e2035f17cefc6090fa550b
-- Numeric-only trusted transcription; no parser refinement theorem.
namespace CheckedInput

def problem : InputProblem 2 2 :=
  ({
    a := ![![(1 : ℚ), (1 : ℚ)], ![(2 : ℚ), (2 : ℚ)]],
    b := ![(0 : ℚ), (1 : ℚ)],
    senses := ![RowSense.eq, RowSense.eq],
    c := ![(3 : ℚ), (-4 : ℚ)],
    objectiveSense := ObjectiveSense.minimize
  } : InputProblem 2 2)

def weights : Fin 2 → ℚ := ![(2 : ℚ), (-1 : ℚ)]

theorem accepted : checkInputInfeasible problem weights = true := by decide +kernel

theorem sound : ¬ ∃ y : Fin 2 → ℝ, InputFeasible problem y :=
  inputInfeasible_sound_real problem weights accepted

#evidence_definition CheckedInput.problem =
  ({
    a := ![![(1 : ℚ), (1 : ℚ)], ![(2 : ℚ), (2 : ℚ)]],
    b := ![(0 : ℚ), (1 : ℚ)],
    senses := ![RowSense.eq, RowSense.eq],
    c := ![(3 : ℚ), (-4 : ℚ)],
    objectiveSense := ObjectiveSense.minimize
  } : InputProblem 2 2)
#evidence_check CheckedInput.accepted : checkInputInfeasible problem weights = true
#evidence_check CheckedInput.sound : ¬ ∃ y : Fin 2 → ℝ, InputFeasible problem y
#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]

end CheckedInput
