import EvidenceHarness
import LPCertificates

/-!
Independent expected-value harness. The closed expected types below spell out
the real inequalities, equalities and objectives; they are not generated from
the declarations under test. Rational acceptance bodies are separately compared
with the intended finite arithmetic predicates.

The published EvidenceHarness is used unchanged. Its replay is a replay of the
entire local declaration closure against Mathlib by the same Lean kernel, not an
independent kernel implementation or an external JSON/Python refinement proof.
-/

open LPCertificates

#evidence_definition LPCertificates.checkOptimal =
  fun {n m k : ℕ} (P : Problem ℚ n m k) (x : Fin n → ℚ)
      (w : Fin m → ℚ) (v : Fin k → ℚ) =>
    decide (
      ((∀ i : Fin m, (∑ j : Fin n, P.A i j * x j) ≤ P.b i) ∧
        (∀ i : Fin k, (∑ j : Fin n, P.E i j * x j) = P.f i)) ∧
      ((∀ i : Fin m, 0 ≤ w i) ∧
        (∀ j : Fin n,
          (∑ i : Fin m, w i * P.A i j) +
            (∑ i : Fin k, v i * P.E i j) = P.c j)) ∧
      (∑ i : Fin m, w i * P.b i) + (∑ i : Fin k, v i * P.f i) =
        (∑ j : Fin n, P.c j * x j))

#evidence_definition LPCertificates.checkInfeasible =
  fun {n m k : ℕ} (P : Problem ℚ n m k)
      (w : Fin m → ℚ) (v : Fin k → ℚ) =>
    decide (
      (∀ i : Fin m, 0 ≤ w i) ∧
      (∀ j : Fin n,
        (∑ i : Fin m, w i * P.A i j) +
          (∑ i : Fin k, v i * P.E i j) = 0) ∧
      (∑ i : Fin m, w i * P.b i) + (∑ i : Fin k, v i * P.f i) < 0)

#evidence_definition LPCertificates.checkUnbounded =
  fun {n m k : ℕ} (P : Problem ℚ n m k)
      (x d : Fin n → ℚ) =>
    decide (
      ((∀ i : Fin m, (∑ j : Fin n, P.A i j * x j) ≤ P.b i) ∧
        (∀ i : Fin k, (∑ j : Fin n, P.E i j * x j) = P.f i)) ∧
      (∀ i : Fin m, (∑ j : Fin n, P.A i j * d j) ≤ 0) ∧
      (∀ i : Fin k, (∑ j : Fin n, P.E i j * d j) = 0) ∧
      0 < (∑ j : Fin n, P.c j * d j))

#evidence_definition LPCertificates.realVector =
  fun {n : ℕ} (x : Fin n → ℚ) (j : Fin n) => (x j : ℝ)

#evidence_definition LPCertificates.realProblem =
  fun {n m k : ℕ} (P : Problem ℚ n m k) =>
    ({ A := fun i j => (P.A i j : ℝ)
       b := fun i => (P.b i : ℝ)
       E := fun i j => (P.E i j : ℝ)
       f := fun i => (P.f i : ℝ)
       c := fun j => (P.c j : ℝ) } : Problem ℝ n m k)

#evidence_check LPCertificates.checkOptimal_sound_real :
  ∀ {n m k : ℕ} (P : Problem ℚ n m k) (x : Fin n → ℚ)
    (w : Fin m → ℚ) (v : Fin k → ℚ),
    checkOptimal P x w v = true →
    ((∀ i : Fin m,
        (∑ j : Fin n, (P.A i j : ℝ) * (x j : ℝ)) ≤ (P.b i : ℝ)) ∧
      (∀ i : Fin k,
        (∑ j : Fin n, (P.E i j : ℝ) * (x j : ℝ)) = (P.f i : ℝ))) ∧
    ∀ y : Fin n → ℝ,
      ((∀ i : Fin m,
          (∑ j : Fin n, (P.A i j : ℝ) * y j) ≤ (P.b i : ℝ)) ∧
        (∀ i : Fin k,
          (∑ j : Fin n, (P.E i j : ℝ) * y j) = (P.f i : ℝ))) →
      (∑ j : Fin n, (P.c j : ℝ) * y j) ≤
        (∑ j : Fin n, (P.c j : ℝ) * (x j : ℝ))

#evidence_check LPCertificates.checkInfeasible_sound_real :
  ∀ {n m k : ℕ} (P : Problem ℚ n m k)
    (w : Fin m → ℚ) (v : Fin k → ℚ),
    checkInfeasible P w v = true →
    ¬ ∃ x : Fin n → ℝ,
      (∀ i : Fin m,
        (∑ j : Fin n, (P.A i j : ℝ) * x j) ≤ (P.b i : ℝ)) ∧
      (∀ i : Fin k,
        (∑ j : Fin n, (P.E i j : ℝ) * x j) = (P.f i : ℝ))

#evidence_check LPCertificates.checkUnbounded_sound_real :
  ∀ {n m k : ℕ} (P : Problem ℚ n m k) (x d : Fin n → ℚ),
    checkUnbounded P x d = true →
    ∀ B : ℝ, ∃ y : Fin n → ℝ,
      ((∀ i : Fin m,
          (∑ j : Fin n, (P.A i j : ℝ) * y j) ≤ (P.b i : ℝ)) ∧
        (∀ i : Fin k,
          (∑ j : Fin n, (P.E i j : ℝ) * y j) = (P.f i : ℝ))) ∧
      B < (∑ j : Fin n, (P.c j : ℝ) * y j)

#check LPCertificates.combination_bound
#check LPCertificates.weak_duality
#check LPCertificates.optimal_sound
#check LPCertificates.infeasible_sound
#check LPCertificates.ray_feasible
#check LPCertificates.ray_objective
#check LPCertificates.unbounded_sound
#check LPCertificates.duality_gap
#check LPCertificates.complementary_slackness

#print axioms LPCertificates.checkOptimal_sound_real
#print axioms LPCertificates.checkInfeasible_sound_real
#print axioms LPCertificates.checkUnbounded_sound_real
#print axioms LPCertificates.complementary_slackness

#evidence_replay [Mathlib, EvidenceHarness] targets [
  LPCertificates.checkOptimal_sound_real,
  LPCertificates.checkInfeasible_sound_real,
  LPCertificates.checkUnbounded_sound_real]
