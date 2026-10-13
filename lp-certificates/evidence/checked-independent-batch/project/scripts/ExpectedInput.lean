import EvidenceHarness
import LPCertificates.Input

/-! Independent closed expected types and bodies for the mixed-input layer.
Real feasibility and original-objective conclusions are written out below.
No expected type is recovered from the declaration being checked.
-/

open LPCertificates

/- The independent expected expression is elaborated before the evidence command
captures its kernel environment, so any generated matcher declarations are
already present. It does not refer to normalizeInput. -/
private def expectedNormalizeInput {n r : ℕ} (P : InputProblem n r) : Problem ℚ n r r where
  A := fun i j => match P.senses i with
    | .le => P.a i j
    | .ge => -P.a i j
    | .eq => 0
  b := fun i => match P.senses i with
    | .le => P.b i
    | .ge => -P.b i
    | .eq => 0
  E := fun i j => match P.senses i with
    | .eq => P.a i j
    | .le | .ge => 0
  f := fun i => match P.senses i with
    | .eq => P.b i
    | .le | .ge => 0
  c := fun j => match P.objectiveSense with
    | .maximize => P.c j
    | .minimize => -P.c j

#evidence_definition LPCertificates.normalizeInput = @expectedNormalizeInput

#evidence_definition LPCertificates.inputInequalityWeights =
  fun {n r : ℕ} (P : InputProblem n r) (u : Fin r → ℚ) (i : Fin r) =>
    match P.senses i with
    | .le | .ge => u i
    | .eq => 0

#evidence_definition LPCertificates.inputEqualityWeights =
  fun {n r : ℕ} (P : InputProblem n r) (u : Fin r → ℚ) (i : Fin r) =>
    match P.senses i with
    | .eq => u i
    | .le | .ge => 0

#evidence_definition LPCertificates.InputFeasible =
  fun {n r : ℕ} (P : InputProblem n r) (x : Fin n → ℝ) =>
    ∀ i : Fin r, match P.senses i with
    | .le => (∑ j : Fin n, (P.a i j : ℝ) * x j) ≤ (P.b i : ℝ)
    | .ge => (P.b i : ℝ) ≤ (∑ j : Fin n, (P.a i j : ℝ) * x j)
    | .eq => (∑ j : Fin n, (P.a i j : ℝ) * x j) = (P.b i : ℝ)

#evidence_definition LPCertificates.ObjectiveBound =
  fun {n r : ℕ} (P : InputProblem n r) (x y : Fin n → ℝ) =>
    match P.objectiveSense with
    | .maximize => (∑ j : Fin n, (P.c j : ℝ) * y j) ≤
        (∑ j : Fin n, (P.c j : ℝ) * x j)
    | .minimize => (∑ j : Fin n, (P.c j : ℝ) * x j) ≤
        (∑ j : Fin n, (P.c j : ℝ) * y j)

#evidence_definition LPCertificates.ObjectiveBeyond =
  fun {n r : ℕ} (P : InputProblem n r) (B : ℝ) (y : Fin n → ℝ) =>
    match P.objectiveSense with
    | .maximize => B < (∑ j : Fin n, (P.c j : ℝ) * y j)
    | .minimize => (∑ j : Fin n, (P.c j : ℝ) * y j) < B

#evidence_definition LPCertificates.checkInputOptimal =
  fun {n r : ℕ} (P : InputProblem n r) (x : Fin n → ℚ) (u : Fin r → ℚ) =>
    checkOptimal (normalizeInput P) x
      (inputInequalityWeights P u) (inputEqualityWeights P u)

#evidence_definition LPCertificates.checkInputInfeasible =
  fun {n r : ℕ} (P : InputProblem n r) (u : Fin r → ℚ) =>
    checkInfeasible (normalizeInput P)
      (inputInequalityWeights P u) (inputEqualityWeights P u)

#evidence_definition LPCertificates.checkInputUnbounded =
  fun {n r : ℕ} (P : InputProblem n r) (x d : Fin n → ℚ) =>
    checkUnbounded (normalizeInput P) x d

#evidence_check LPCertificates.inputOptimal_sound_real :
  ∀ {n r : ℕ} (P : InputProblem n r) (x : Fin n → ℚ) (u : Fin r → ℚ),
    checkInputOptimal P x u = true →
    (∀ i : Fin r, match P.senses i with
      | .le => (∑ j : Fin n, (P.a i j : ℝ) * (x j : ℝ)) ≤ (P.b i : ℝ)
      | .ge => (P.b i : ℝ) ≤ (∑ j : Fin n, (P.a i j : ℝ) * (x j : ℝ))
      | .eq => (∑ j : Fin n, (P.a i j : ℝ) * (x j : ℝ)) = (P.b i : ℝ)) ∧
    ∀ y : Fin n → ℝ,
      (∀ i : Fin r, match P.senses i with
        | .le => (∑ j : Fin n, (P.a i j : ℝ) * y j) ≤ (P.b i : ℝ)
        | .ge => (P.b i : ℝ) ≤ (∑ j : Fin n, (P.a i j : ℝ) * y j)
        | .eq => (∑ j : Fin n, (P.a i j : ℝ) * y j) = (P.b i : ℝ)) →
      match P.objectiveSense with
      | .maximize => (∑ j : Fin n, (P.c j : ℝ) * y j) ≤
          (∑ j : Fin n, (P.c j : ℝ) * (x j : ℝ))
      | .minimize => (∑ j : Fin n, (P.c j : ℝ) * (x j : ℝ)) ≤
          (∑ j : Fin n, (P.c j : ℝ) * y j)

#evidence_check LPCertificates.inputInfeasible_sound_real :
  ∀ {n r : ℕ} (P : InputProblem n r) (u : Fin r → ℚ),
    checkInputInfeasible P u = true →
    ¬ ∃ x : Fin n → ℝ,
      ∀ i : Fin r, match P.senses i with
      | .le => (∑ j : Fin n, (P.a i j : ℝ) * x j) ≤ (P.b i : ℝ)
      | .ge => (P.b i : ℝ) ≤ (∑ j : Fin n, (P.a i j : ℝ) * x j)
      | .eq => (∑ j : Fin n, (P.a i j : ℝ) * x j) = (P.b i : ℝ)

#evidence_check LPCertificates.inputUnbounded_sound_real :
  ∀ {n r : ℕ} (P : InputProblem n r) (x d : Fin n → ℚ),
    checkInputUnbounded P x d = true →
    ∀ B : ℝ, ∃ y : Fin n → ℝ,
      (∀ i : Fin r, match P.senses i with
        | .le => (∑ j : Fin n, (P.a i j : ℝ) * y j) ≤ (P.b i : ℝ)
        | .ge => (P.b i : ℝ) ≤ (∑ j : Fin n, (P.a i j : ℝ) * y j)
        | .eq => (∑ j : Fin n, (P.a i j : ℝ) * y j) = (P.b i : ℝ)) ∧
      match P.objectiveSense with
      | .maximize => B < (∑ j : Fin n, (P.c j : ℝ) * y j)
      | .minimize => (∑ j : Fin n, (P.c j : ℝ) * y j) < B

#check LPCertificates.input_feasible_iff
#check LPCertificates.input_objective_bound_iff

#print axioms LPCertificates.input_feasible_iff
#print axioms LPCertificates.input_objective_bound_iff
#print axioms LPCertificates.inputOptimal_sound_real
#print axioms LPCertificates.inputInfeasible_sound_real
#print axioms LPCertificates.inputUnbounded_sound_real

#evidence_replay [Mathlib, EvidenceHarness] targets [
  LPCertificates.inputOptimal_sound_real,
  LPCertificates.inputInfeasible_sound_real,
  LPCertificates.inputUnbounded_sound_real]
