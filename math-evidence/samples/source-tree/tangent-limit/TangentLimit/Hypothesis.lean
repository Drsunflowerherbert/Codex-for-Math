import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# The explicit, unproved Diophantine hypothesis

No instance of this proposition is supplied by this project. All conclusions
take it as a theorem argument.
-/

namespace TangentLimit

/-- For each real exponent greater than two, all sufficiently large positive
integer denominators satisfy the stated lower bound, for every integer numerator. -/
def PiDiophantine : Prop :=
  ∀ ν : ℝ, 2 < ν → ∃ Q : ℕ, ∀ q : ℕ, Q ≤ q → 0 < q →
    ∀ p : ℤ, (q : ℝ) ^ (-ν) ≤ |Real.pi - (p : ℝ) / (q : ℝ)|

end TangentLimit
