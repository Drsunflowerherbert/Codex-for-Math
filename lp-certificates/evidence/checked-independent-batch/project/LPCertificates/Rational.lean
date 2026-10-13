import LPCertificates.Core

/-! Executable rational acceptance tests and soundness for the real LP. The JSON
parser is external to this formal model; normalization must match the documented
interface. These tests verify supplied witnesses, and do not search for them. -/

namespace LPCertificates

variable {n m k : ℕ}

instance (P : Problem ℚ n m k) (x : Fin n → ℚ) : Decidable (Feasible P x) :=
  inferInstanceAs (Decidable ((∀ i, dot (P.A i) x ≤ P.b i) ∧
    (∀ i, dot (P.E i) x = P.f i)))

instance (w : Fin m → ℚ) : Decidable (Nonnegative w) :=
  inferInstanceAs (Decidable (∀ i, 0 ≤ w i))

instance (P : Problem ℚ n m k) (w : Fin m → ℚ) (v : Fin k → ℚ) :
    Decidable (DualCertificate P w v) :=
  inferInstanceAs (Decidable (Nonnegative w ∧ ∀ j, combination P w v j = P.c j))

instance (P : Problem ℚ n m k) (x : Fin n → ℚ) (w : Fin m → ℚ) (v : Fin k → ℚ) :
    Decidable (OptimalCertificate P x w v) :=
  inferInstanceAs (Decidable (Feasible P x ∧ DualCertificate P w v ∧
    bound P w v = dot P.c x))

instance (P : Problem ℚ n m k) (w : Fin m → ℚ) (v : Fin k → ℚ) :
    Decidable (InfeasibleCertificate P w v) :=
  inferInstanceAs (Decidable (Nonnegative w ∧ (∀ j, combination P w v j = 0) ∧
    bound P w v < 0))

instance (P : Problem ℚ n m k) (x d : Fin n → ℚ) : Decidable (RayCertificate P x d) :=
  inferInstanceAs (Decidable (Feasible P x ∧ (∀ i, dot (P.A i) d ≤ 0) ∧
    (∀ i, dot (P.E i) d = 0) ∧ 0 < dot P.c d))

def checkOptimal (P : Problem ℚ n m k) (x : Fin n → ℚ)
    (w : Fin m → ℚ) (v : Fin k → ℚ) : Bool := decide (OptimalCertificate P x w v)

def checkInfeasible (P : Problem ℚ n m k) (w : Fin m → ℚ) (v : Fin k → ℚ) : Bool :=
  decide (InfeasibleCertificate P w v)

def checkUnbounded (P : Problem ℚ n m k) (x d : Fin n → ℚ) : Bool :=
  decide (RayCertificate P x d)

def realVector (x : Fin n → ℚ) : Fin n → ℝ := fun j => (x j : ℝ)

def realProblem (P : Problem ℚ n m k) : Problem ℝ n m k where
  A := fun i j => (P.A i j : ℝ)
  b := fun i => (P.b i : ℝ)
  E := fun i j => (P.E i j : ℝ)
  f := fun i => (P.f i : ℝ)
  c := fun j => (P.c j : ℝ)

lemma dot_cast (u v : Fin n → ℚ) :
    dot (realVector u) (realVector v) = ((dot u v : ℚ) : ℝ) := by
  simp [dot, realVector, Rat.cast_sum, Rat.cast_mul]

lemma combination_cast (P : Problem ℚ n m k) (w : Fin m → ℚ)
    (v : Fin k → ℚ) (j : Fin n) :
    combination (realProblem P) (realVector w) (realVector v) j =
      ((combination P w v j : ℚ) : ℝ) := by
  simp [combination, realProblem, realVector, Rat.cast_sum, Rat.cast_mul, Rat.cast_add]

lemma bound_cast (P : Problem ℚ n m k) (w : Fin m → ℚ) (v : Fin k → ℚ) :
    bound (realProblem P) (realVector w) (realVector v) = ((bound P w v : ℚ) : ℝ) := by
  change dot (realVector w) (realVector P.b) + dot (realVector v) (realVector P.f) = _
  rw [dot_cast, dot_cast, ← Rat.cast_add]
  rfl

lemma feasible_cast (P : Problem ℚ n m k) (x : Fin n → ℚ) (hx : Feasible P x) :
    Feasible (realProblem P) (realVector x) := by
  constructor
  · intro i
    change dot (realVector (P.A i)) (realVector x) ≤ (P.b i : ℝ)
    rw [dot_cast]
    exact_mod_cast hx.1 i
  · intro i
    change dot (realVector (P.E i)) (realVector x) = (P.f i : ℝ)
    rw [dot_cast]
    exact_mod_cast hx.2 i

lemma dual_cast (P : Problem ℚ n m k) (w : Fin m → ℚ) (v : Fin k → ℚ)
    (hc : DualCertificate P w v) :
    DualCertificate (realProblem P) (realVector w) (realVector v) := by
  constructor
  · intro i
    change (0 : ℝ) ≤ (w i : ℝ)
    exact_mod_cast hc.1 i
  · intro j
    rw [combination_cast]
    change ((combination P w v j : ℚ) : ℝ) = (P.c j : ℝ)
    exact_mod_cast hc.2 j

theorem checkOptimal_sound_real (P : Problem ℚ n m k) (x : Fin n → ℚ)
    (w : Fin m → ℚ) (v : Fin k → ℚ) (h : checkOptimal P x w v = true) :
    Feasible (realProblem P) (realVector x) ∧
      ∀ y : Fin n → ℝ, Feasible (realProblem P) y →
        dot (realProblem P).c y ≤ dot (realProblem P).c (realVector x) := by
  have hc : OptimalCertificate P x w v := of_decide_eq_true h
  apply optimal_sound (realProblem P) (realVector x) (realVector w) (realVector v)
  refine ⟨feasible_cast P x hc.1, dual_cast P w v hc.2.1, ?_⟩
  change bound (realProblem P) (realVector w) (realVector v) =
    dot (realVector P.c) (realVector x)
  rw [bound_cast, dot_cast]
  exact_mod_cast hc.2.2

theorem checkInfeasible_sound_real (P : Problem ℚ n m k) (w : Fin m → ℚ)
    (v : Fin k → ℚ) (h : checkInfeasible P w v = true) :
    ¬ ∃ x : Fin n → ℝ, Feasible (realProblem P) x := by
  have hc : InfeasibleCertificate P w v := of_decide_eq_true h
  apply infeasible_sound (realProblem P) (realVector w) (realVector v)
  refine ⟨?_, ?_, ?_⟩
  · intro i
    change (0 : ℝ) ≤ (w i : ℝ)
    exact_mod_cast hc.1 i
  · intro j
    rw [combination_cast]
    exact_mod_cast hc.2.1 j
  · rw [bound_cast]
    exact_mod_cast hc.2.2

theorem checkUnbounded_sound_real (P : Problem ℚ n m k) (x d : Fin n → ℚ)
    (h : checkUnbounded P x d = true) :
    ∀ B : ℝ, ∃ y : Fin n → ℝ, Feasible (realProblem P) y ∧ B < dot (realProblem P).c y := by
  have hc : RayCertificate P x d := of_decide_eq_true h
  apply unbounded_sound (realProblem P) (realVector x) (realVector d)
  refine ⟨feasible_cast P x hc.1, ?_, ?_, ?_⟩
  · intro i
    change dot (realVector (P.A i)) (realVector d) ≤ (0 : ℝ)
    rw [dot_cast]
    exact_mod_cast hc.2.1 i
  · intro i
    change dot (realVector (P.E i)) (realVector d) = (0 : ℝ)
    rw [dot_cast]
    exact_mod_cast hc.2.2.1 i
  · change (0 : ℝ) < dot (realVector P.c) (realVector d)
    rw [dot_cast]
    exact_mod_cast hc.2.2.2

end LPCertificates
