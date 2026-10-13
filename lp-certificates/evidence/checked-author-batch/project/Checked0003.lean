import LPCertificates.Input
import EvidenceHarness

open LPCertificates
-- Original strict JSON SHA-256: 072b73cb1b1be6f1916c32e33f26436bed587bc6ff1c814c0764cf240d577cc6
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
