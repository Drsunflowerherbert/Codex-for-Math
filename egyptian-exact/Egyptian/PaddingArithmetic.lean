import Egyptian.Counterexample
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.List.Prime

namespace Egyptian

/-- A natural common numerator over the product of all denominators. -/
def commonNumerator : List ℕ → ℕ
  | [] => 0
  | d :: t => t.prod + d * commonNumerator t

theorem commonNumerator_spec {l : List ℕ} (hp : ∀ d ∈ l, 0 < d) :
    (commonNumerator l : ℝ) = (l.prod : ℝ) * reciprocalSum l := by
  induction l with
  | nil => simp [commonNumerator]
  | cons d t ih =>
    have hd : (d : ℝ) ≠ 0 := ne_of_gt (Nat.cast_pos.mpr (hp d (by simp)))
    have ht := ih (fun a ha => hp a (by simp [ha]))
    simp only [commonNumerator, List.prod_cons, Nat.cast_add, Nat.cast_mul, reciprocalSum_cons]
    rw [ht]
    field_simp

theorem commonNumerator_eq_prod {l : List ℕ} (hp : ∀ d ∈ l, 0 < d)
    (hv : reciprocalSum l = 1) : commonNumerator l = l.prod := by
  have hs := commonNumerator_spec hp
  rw [hv, mul_one] at hs
  exact_mod_cast hs

theorem unit_split_identity (d : ℕ) (hd : 0 < d) :
    (d : ℝ)⁻¹ = ((d + 1 : ℕ) : ℝ)⁻¹ + ((d * (d + 1) : ℕ) : ℝ)⁻¹ := by
  have hd0 : (d : ℝ) ≠ 0 := ne_of_gt (Nat.cast_pos.mpr hd)
  have hd1 : (d : ℝ) + 1 ≠ 0 := by positivity
  push_cast
  field_simp

theorem factor_split_identity (a b : ℕ) (ha : 0 < a) (hb : 0 < b) :
    ((a * b : ℕ) : ℝ)⁻¹ = ((a * (b + 1) : ℕ) : ℝ)⁻¹ +
      ((a * b * (b + 1) : ℕ) : ℝ)⁻¹ := by
  have ha0 : (a : ℝ) ≠ 0 := ne_of_gt (Nat.cast_pos.mpr ha)
  have hb0 : (b : ℝ) ≠ 0 := ne_of_gt (Nat.cast_pos.mpr hb)
  have hb1 : (b : ℝ) + 1 ≠ 0 := by positivity
  push_cast
  field_simp

end Egyptian
