import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Sort
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace Egyptian

/-- Exact reciprocal sum. Denominator positivity is recorded separately. -/
noncomputable def reciprocalSum (l : List ℕ) : ℝ :=
  (l.map (fun d : ℕ => (d : ℝ)⁻¹)).sum

@[simp] theorem reciprocalSum_nil : reciprocalSum [] = 0 := rfl

@[simp] theorem reciprocalSum_cons (a : ℕ) (l : List ℕ) :
    reciprocalSum (a :: l) = (a : ℝ)⁻¹ + reciprocalSum l := rfl

@[simp] theorem reciprocalSum_append (l r : List ℕ) :
    reciprocalSum (l ++ r) = reciprocalSum l + reciprocalSum r := by
  simp [reciprocalSum]

theorem reciprocalSum_perm {l r : List ℕ} (h : l.Perm r) :
    reciprocalSum l = reciprocalSum r := by
  unfold reciprocalSum
  exact (h.map (fun d : ℕ => (d : ℝ)⁻¹)).sum_eq

theorem reciprocalSum_nonneg (l : List ℕ) : 0 ≤ reciprocalSum l := by
  induction l with
  | nil => simp
  | cons a l ih =>
    rw [reciprocalSum_cons]
    exact add_nonneg (inv_nonneg.mpr (Nat.cast_nonneg a)) ih

theorem reciprocalSum_pos {l : List ℕ} (hp : ∀ d ∈ l, 0 < d) (hne : l ≠ []) :
    0 < reciprocalSum l := by
  cases l with
  | nil => exact (hne rfl).elim
  | cons a l =>
    rw [reciprocalSum_cons]
    exact add_pos_of_pos_of_nonneg
      (inv_pos.mpr (Nat.cast_pos.mpr (hp a (by simp)))) (reciprocalSum_nonneg l)

/-- Odd duplicate replacement, with no strict-growth hypothesis needed for the identity. -/
theorem odd_replacement_identity (k : ℕ) :
    ((2 * k + 1 : ℕ) : ℝ)⁻¹ + ((2 * k + 1 : ℕ) : ℝ)⁻¹ =
      ((k + 1 : ℕ) : ℝ)⁻¹ + (((2 * k + 1) * (k + 1) : ℕ) : ℝ)⁻¹ := by
  have hk : (k : ℝ) + 1 ≠ 0 := by positivity
  have hn : 2 * (k : ℝ) + 1 ≠ 0 := by positivity
  push_cast
  field_simp
  ring

/-- Even duplicate replacement; k must be positive because inverse zero is zero. -/
theorem even_replacement_identity (k : ℕ) (hk : 0 < k) :
    ((2 * k : ℕ) : ℝ)⁻¹ + ((2 * k : ℕ) : ℝ)⁻¹ =
      ((k + 1 : ℕ) : ℝ)⁻¹ + ((k * (k + 1) : ℕ) : ℝ)⁻¹ := by
  have hk0 : (k : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hk)
  have hk1 : (k : ℝ) + 1 ≠ 0 := by positivity
  push_cast
  field_simp
  ring

theorem odd_replacement_growth (k : ℕ) (hk : 1 ≤ k) :
    2 * (2 * k + 1) < (k + 1) + (2 * k + 1) * (k + 1) := by
  nlinarith

theorem even_replacement_growth (k : ℕ) (hk : 2 ≤ k) :
    2 * (2 * k) < (k + 1) + k * (k + 1) := by
  nlinarith

end Egyptian
