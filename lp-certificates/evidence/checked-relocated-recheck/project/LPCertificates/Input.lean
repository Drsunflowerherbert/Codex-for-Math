import LPCertificates.Rational

/-! Original mixed rows and objective senses. Normalization is computed in Lean.
Zero masks retain one slot per original row, and introduce no decision variables.
-/

namespace LPCertificates

inductive RowSense where
  | le | ge | eq
  deriving DecidableEq, Repr

inductive ObjectiveSense where
  | maximize | minimize
  deriving DecidableEq, Repr

structure InputProblem (n r : ℕ) where
  a : Fin r → Fin n → ℚ
  b : Fin r → ℚ
  senses : Fin r → RowSense
  c : Fin n → ℚ
  objectiveSense : ObjectiveSense

variable {n r : ℕ}

def normalizeInput (P : InputProblem n r) : Problem ℚ n r r where
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

def inputInequalityWeights (P : InputProblem n r) (u : Fin r → ℚ) : Fin r → ℚ :=
  fun i => match P.senses i with
    | .le | .ge => u i
    | .eq => 0

def inputEqualityWeights (P : InputProblem n r) (u : Fin r → ℚ) : Fin r → ℚ :=
  fun i => match P.senses i with
    | .eq => u i
    | .le | .ge => 0

def InputFeasible (P : InputProblem n r) (x : Fin n → ℝ) : Prop :=
  ∀ i, match P.senses i with
    | .le => dot (realVector (P.a i)) x ≤ (P.b i : ℝ)
    | .ge => (P.b i : ℝ) ≤ dot (realVector (P.a i)) x
    | .eq => dot (realVector (P.a i)) x = (P.b i : ℝ)

def ObjectiveBound (P : InputProblem n r) (x y : Fin n → ℝ) : Prop :=
  match P.objectiveSense with
    | .maximize => dot (realVector P.c) y ≤ dot (realVector P.c) x
    | .minimize => dot (realVector P.c) x ≤ dot (realVector P.c) y

def ObjectiveBeyond (P : InputProblem n r) (B : ℝ) (y : Fin n → ℝ) : Prop :=
  match P.objectiveSense with
    | .maximize => B < dot (realVector P.c) y
    | .minimize => dot (realVector P.c) y < B

def checkInputOptimal (P : InputProblem n r) (x : Fin n → ℚ) (u : Fin r → ℚ) : Bool :=
  checkOptimal (normalizeInput P) x (inputInequalityWeights P u) (inputEqualityWeights P u)

def checkInputInfeasible (P : InputProblem n r) (u : Fin r → ℚ) : Bool :=
  checkInfeasible (normalizeInput P) (inputInequalityWeights P u) (inputEqualityWeights P u)

def checkInputUnbounded (P : InputProblem n r) (x d : Fin n → ℚ) : Bool :=
  checkUnbounded (normalizeInput P) x d

theorem input_feasible_iff (P : InputProblem n r) (x : Fin n → ℝ) :
    InputFeasible P x ↔ Feasible (realProblem (normalizeInput P)) x := by
  constructor
  · intro hx
    constructor
    · intro i
      have hi := hx i
      cases h : P.senses i
      · simpa [normalizeInput, realProblem, h, realVector, dot] using hi
      · simpa [normalizeInput, realProblem, h, realVector, dot, Finset.sum_neg_distrib] using hi
      · simp [normalizeInput, realProblem, h, dot]
    · intro i
      have hi := hx i
      cases h : P.senses i <;>
        simp_all [normalizeInput, realProblem, realVector, dot]
  · intro hx i
    cases h : P.senses i
    · have hi := hx.1 i
      simpa [InputFeasible, normalizeInput, realProblem, h, realVector, dot] using hi
    · have hi := hx.1 i
      simpa [InputFeasible, normalizeInput, realProblem, h, realVector, dot,
        Finset.sum_neg_distrib] using hi
    · have hi := hx.2 i
      simpa [InputFeasible, normalizeInput, realProblem, h, realVector, dot] using hi

theorem input_objective_bound_iff (P : InputProblem n r) (x y : Fin n → ℝ) :
    dot (realProblem (normalizeInput P)).c y ≤ dot (realProblem (normalizeInput P)).c x ↔
      ObjectiveBound P x y := by
  cases h : P.objectiveSense <;>
    simp [normalizeInput, realProblem, ObjectiveBound, h, realVector, dot,
      Finset.sum_neg_distrib]

theorem inputOptimal_sound_real (P : InputProblem n r) (x : Fin n → ℚ)
    (u : Fin r → ℚ) (h : checkInputOptimal P x u = true) :
    InputFeasible P (realVector x) ∧
      ∀ y : Fin n → ℝ, InputFeasible P y → ObjectiveBound P (realVector x) y := by
  have hc := checkOptimal_sound_real (normalizeInput P) x
    (inputInequalityWeights P u) (inputEqualityWeights P u) h
  refine ⟨(input_feasible_iff P (realVector x)).mpr hc.1, fun y hy => ?_⟩
  exact (input_objective_bound_iff P (realVector x) y).mp
    (hc.2 y ((input_feasible_iff P y).mp hy))

theorem inputInfeasible_sound_real (P : InputProblem n r) (u : Fin r → ℚ)
    (h : checkInputInfeasible P u = true) :
    ¬ ∃ x : Fin n → ℝ, InputFeasible P x := by
  have hc := checkInfeasible_sound_real (normalizeInput P)
    (inputInequalityWeights P u) (inputEqualityWeights P u) h
  rintro ⟨x, hx⟩
  exact hc ⟨x, (input_feasible_iff P x).mp hx⟩

theorem inputUnbounded_sound_real (P : InputProblem n r) (x d : Fin n → ℚ)
    (h : checkInputUnbounded P x d = true) :
    ∀ B : ℝ, ∃ y : Fin n → ℝ, InputFeasible P y ∧ ObjectiveBeyond P B y := by
  have hc := checkUnbounded_sound_real (normalizeInput P) x d h
  intro B
  cases hobj : P.objectiveSense
  · obtain ⟨y, hy, hB⟩ := hc B
    refine ⟨y, (input_feasible_iff P y).mpr hy, ?_⟩
    simpa [ObjectiveBeyond, normalizeInput, realProblem, hobj, realVector, dot] using hB
  · obtain ⟨y, hy, hB⟩ := hc (-B)
    refine ⟨y, (input_feasible_iff P y).mpr hy, ?_⟩
    simpa [ObjectiveBeyond, normalizeInput, realProblem, hobj, realVector, dot,
      Finset.sum_neg_distrib] using hB

end LPCertificates
