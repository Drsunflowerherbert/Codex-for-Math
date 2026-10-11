import Mathlib.Analysis.SpecialFunctions.Trigonometric.Complex
import Mathlib.Analysis.Real.Pi.Irrational
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/-!
# Integer arguments are not tangent poles

This elementary fact uses mathlib's proved irrationality of `Real.pi`.
It does not use or prove the project's explicit Diophantine hypothesis.
-/

namespace TangentLimit

/-- Every integer argument has nonzero cosine, so the classical tangent is
defined there. -/
theorem cos_intCast_ne_zero (n : ℤ) : Real.cos (n : ℝ) ≠ 0 := by
  intro hn
  obtain ⟨k, hk⟩ := Real.cos_eq_zero_iff.mp hn
  have hden : ((2 * k + 1 : ℤ) : ℝ) ≠ 0 := by
    exact_mod_cast (show (2 * k + 1 : ℤ) ≠ 0 by omega)
  apply Irrational.ne_rational irrational_pi (2 * n) (2 * k + 1)
  apply (eq_div_iff hden).2
  push_cast
  nlinarith [hk]

/-- In particular, no natural-number argument is a tangent pole, including
all finitely many terms before an eventual estimate starts. -/
theorem cos_natCast_ne_zero (n : ℕ) : Real.cos (n : ℝ) ≠ 0 := by
  simpa only [Int.cast_natCast] using cos_intCast_ne_zero (n : ℤ)

end TangentLimit
