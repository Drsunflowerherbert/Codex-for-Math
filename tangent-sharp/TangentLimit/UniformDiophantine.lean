import TangentLimit.Hypothesis
import Mathlib.Analysis.Real.Pi.Irrational
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# A uniform lower bound at every positive denominator

The eventual approximation hypothesis has finitely many exceptional denominators.
For each such denominator, irrationality of pi supplies a strictly positive gap
from every integer, uniformly in the integer numerator. Taking a finite minimum
of these gaps produces one positive constant for all positive denominators.
No proof of `PiDiophantine` is supplied or used implicitly.
-/

namespace TangentLimit

/-- An irrational real number has a positive distance from the integer lattice.
The two neighbors of its floor suffice to control every integer. -/
theorem irrational_integer_distance (x : ℝ) (hx : Irrational x) :
    ∃ ε : ℝ, 0 < ε ∧ ∀ p : ℤ, ε ≤ |x - (p : ℝ)| := by
  let k : ℤ := Int.floor x
  have hk : (k : ℝ) < x :=
    lt_of_le_of_ne (Int.floor_le x) (Ne.symm (hx.ne_int k))
  have hk1 : x < (k : ℝ) + 1 := Int.lt_floor_add_one x
  refine ⟨min (x - (k : ℝ)) ((k : ℝ) + 1 - x),
    lt_min (sub_pos.mpr hk) (sub_pos.mpr hk1), ?_⟩
  intro p
  by_cases hp : p ≤ k
  · have hpr : (p : ℝ) ≤ (k : ℝ) := by exact_mod_cast hp
    rw [abs_of_nonneg (by linarith : 0 ≤ x - (p : ℝ))]
    exact (min_le_left _ _).trans (by linarith)
  · have hpr : (k : ℝ) + 1 ≤ (p : ℝ) := by
      exact_mod_cast (show k + 1 ≤ p by omega)
    rw [abs_of_nonpos (by linarith : x - (p : ℝ) ≤ 0)]
    exact (min_le_right _ _).trans (by linarith)

/-- Every positive integer multiple of pi has a positive gap from every integer.
This lemma is unconditional and uses only mathlib's irrationality of pi. -/
theorem pi_integer_distance (q : ℕ) (hq : 0 < q) :
    ∃ ε : ℝ, 0 < ε ∧ ∀ p : ℤ,
      ε ≤ |(q : ℝ) * Real.pi - (p : ℝ)| :=
  irrational_integer_distance _ (irrational_pi.natCast_mul (Nat.ne_of_gt hq))

/-- Any finite set of positive denominators admits a single positive lower-bound
constant for the weighted integer distances. -/
theorem pi_finite_denominator_bound (Q : ℕ) (α : ℝ) :
    ∃ c : ℝ, 0 < c ∧ c ≤ 1 ∧ ∀ q : ℕ, q < Q → 0 < q → ∀ p : ℤ,
      c * (q : ℝ) ^ (1 - α) ≤ |(q : ℝ) * Real.pi - (p : ℝ)| := by
  induction Q with
  | zero =>
      refine ⟨1, by norm_num, le_rfl, ?_⟩
      intro q hq
      omega
  | succ Q ih =>
      obtain ⟨c, hc, hc1, hbound⟩ := ih
      by_cases hQ : 0 < Q
      · obtain ⟨ε, hε, hgap⟩ := pi_integer_distance Q hQ
        have hw : 0 < (Q : ℝ) ^ (1 - α) :=
          Real.rpow_pos_of_pos (by exact_mod_cast hQ) _
        refine ⟨min c (ε / (Q : ℝ) ^ (1 - α)),
          lt_min hc (div_pos hε hw), (min_le_left _ _).trans hc1, ?_⟩
        intro q hq hqpos p
        by_cases hqQ : q < Q
        · exact (mul_le_mul_of_nonneg_right (min_le_left _ _)
            (Real.rpow_nonneg (Nat.cast_nonneg q) _)).trans (hbound q hqQ hqpos p)
        · have heq : q = Q := by omega
          subst q
          calc
            min c (ε / (Q : ℝ) ^ (1 - α)) * (Q : ℝ) ^ (1 - α)
                ≤ (ε / (Q : ℝ) ^ (1 - α)) * (Q : ℝ) ^ (1 - α) :=
              mul_le_mul_of_nonneg_right (min_le_right _ _) hw.le
            _ = ε := div_mul_cancel₀ _ (ne_of_gt hw)
            _ ≤ |(Q : ℝ) * Real.pi - (p : ℝ)| := hgap p
      · refine ⟨c, hc, hc1, ?_⟩
        intro q hq hqpos p
        exact hbound q (by omega) hqpos p

/-- The explicit eventual hypothesis extends to every positive denominator with
one positive constant, uniformly in all integer numerators. -/
theorem piDiophantine_uniform (h : PiDiophantine) (α : ℝ) (hα : 2 < α) :
    ∃ c : ℝ, 0 < c ∧ c ≤ 1 ∧ ∀ q : ℕ, 0 < q → ∀ p : ℤ,
      c * (q : ℝ) ^ (1 - α) ≤ |(q : ℝ) * Real.pi - (p : ℝ)| := by
  obtain ⟨Q, hQ⟩ := h α hα
  obtain ⟨c, hc, hc1, hfinite⟩ := pi_finite_denominator_bound Q α
  refine ⟨c, hc, hc1, ?_⟩
  intro q hq p
  by_cases hqQ : q < Q
  · exact hfinite q hqQ hq p
  · have hqr : (0 : ℝ) < (q : ℝ) := by exact_mod_cast hq
    have hbound := hQ q (by omega) hq p
    have hm := mul_le_mul_of_nonneg_left hbound hqr.le
    have hident : (q : ℝ) * |Real.pi - (p : ℝ) / (q : ℝ)| =
        |(q : ℝ) * Real.pi - (p : ℝ)| := by
      have heq : (q : ℝ) * (Real.pi - (p : ℝ) / (q : ℝ)) =
          (q : ℝ) * Real.pi - (p : ℝ) := by
        rw [mul_sub, mul_div_cancel₀ _ (ne_of_gt hqr)]
      rw [← heq, abs_mul, abs_of_pos hqr]
    have hpower : (q : ℝ) ^ (1 - α) = (q : ℝ) * (q : ℝ) ^ (-α) := by
      rw [sub_eq_add_neg, Real.rpow_add hqr, Real.rpow_one]
    calc
      c * (q : ℝ) ^ (1 - α) ≤ 1 * (q : ℝ) ^ (1 - α) :=
        mul_le_mul_of_nonneg_right hc1 (Real.rpow_nonneg hqr.le _)
      _ = (q : ℝ) * (q : ℝ) ^ (-α) := by rw [one_mul, hpower]
      _ ≤ (q : ℝ) * |Real.pi - (p : ℝ) / (q : ℝ)| := hm
      _ = |(q : ℝ) * Real.pi - (p : ℝ)| := hident

end TangentLimit
