import Mathlib.Algebra.Order.Floor.Semiring
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Order.Filter.AtTopBot.Defs
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# A nearest tangent pole

The positive odd denominator `poleDenom n` is obtained by choosing the odd
integer at the center of the even interval containing `2 * n / π`.
-/

open Filter

noncomputable section

namespace TangentLimit

def poleIndex (n : ℕ) : ℕ := Nat.floor ((n : ℝ) / Real.pi)

def poleDenom (n : ℕ) : ℕ := 2 * poleIndex n + 1

def poleOffset (n : ℕ) : ℝ := (n : ℝ) - (poleDenom n : ℝ) * Real.pi / 2

theorem poleDenom_pos (n : ℕ) : 0 < poleDenom n := by
  unfold poleDenom
  omega

theorem poleDenom_odd (n : ℕ) : Odd (poleDenom n) := by
  exact ⟨poleIndex n, by simp [poleDenom, two_mul]⟩

theorem poleIndex_mul_pi_le (n : ℕ) : (poleIndex n : ℝ) * Real.pi ≤ (n : ℝ) := by
  have h := Nat.floor_le (show 0 ≤ (n : ℝ) / Real.pi by positivity)
  change (poleIndex n : ℝ) ≤ (n : ℝ) / Real.pi at h
  exact (le_div_iff₀ Real.pi_pos).mp h

theorem lt_poleIndex_add_one_mul_pi (n : ℕ) :
    (n : ℝ) < ((poleIndex n : ℝ) + 1) * Real.pi := by
  have h := Nat.lt_floor_add_one ((n : ℝ) / Real.pi)
  change (n : ℝ) / Real.pi < (poleIndex n : ℝ) + 1 at h
  exact (div_lt_iff₀ Real.pi_pos).mp h

theorem abs_poleOffset_le (n : ℕ) : |poleOffset n| ≤ Real.pi / 2 := by
  have hl := poleIndex_mul_pi_le n
  have hu := lt_poleIndex_add_one_mul_pi n
  rw [abs_le]
  unfold poleOffset poleDenom
  push_cast
  constructor <;> nlinarith

theorem poleDenom_le_two_mul (n : ℕ) (hn : 1 ≤ n) :
    (poleDenom n : ℝ) ≤ 2 * (n : ℝ) := by
  have hfloor := poleIndex_mul_pi_le n
  have hk : 0 ≤ (poleIndex n : ℝ) := by positivity
  have hn' : 1 ≤ (n : ℝ) := by exact_mod_cast hn
  have hpi : 2 < Real.pi := by linarith [Real.pi_gt_three]
  unfold poleDenom
  push_cast
  nlinarith

theorem eventually_poleDenom_ge (Q : ℕ) :
    ∀ᶠ n : ℕ in atTop, Q ≤ poleDenom n := by
  filter_upwards [eventually_ge_atTop (4 * (Q + 1))] with n hn
  by_contra hq
  have hk : poleIndex n + 1 ≤ Q := by
    unfold poleDenom at hq
    omega
  have hn' : (4 : ℝ) * ((Q : ℝ) + 1) ≤ (n : ℝ) := by exact_mod_cast hn
  have hk' : (poleIndex n : ℝ) + 1 ≤ (Q : ℝ) := by exact_mod_cast hk
  have hp : 0 < (poleIndex n : ℝ) + 1 := by positivity
  have hu := lt_poleIndex_add_one_mul_pi n
  nlinarith [Real.pi_lt_four]

/-- The selected pole is at least as close as every pole with an odd integer
denominator. This includes both endpoints, where nearest poles can tie. -/
theorem poleOffset_nearest (n : ℕ) (r : ℤ) (hr : Odd r) :
    |poleOffset n| ≤ |(n : ℝ) - (r : ℝ) * Real.pi / 2| := by
  obtain ⟨j, hj⟩ := hr
  have hr' : (r : ℝ) = 2 * (j : ℝ) + 1 := by
    rw [hj]
    push_cast
    ring
  have hcases : j ≤ (poleIndex n : ℤ) - 1 ∨
      j = (poleIndex n : ℤ) ∨ (poleIndex n : ℤ) + 1 ≤ j := by omega
  rcases hcases with hjlo | hjeq | hjhi
  · have hjlo' : (j : ℝ) ≤ (poleIndex n : ℝ) - 1 := by exact_mod_cast hjlo
    have hm := mul_le_mul_of_nonneg_right hjlo' Real.pi_pos.le
    have hl := poleIndex_mul_pi_le n
    have hdist : Real.pi / 2 ≤ (n : ℝ) - (r : ℝ) * Real.pi / 2 := by
      rw [hr']
      nlinarith
    exact (abs_poleOffset_le n).trans (hdist.trans (le_abs_self _))
  · have heq : (r : ℝ) = (poleDenom n : ℝ) := by
      rw [hr', hjeq]
      simp [poleDenom]
    simp [poleOffset, heq]
  · have hjhi' : (poleIndex n : ℝ) + 1 ≤ (j : ℝ) := by exact_mod_cast hjhi
    have hm := mul_le_mul_of_nonneg_right hjhi' Real.pi_pos.le
    have hu := lt_poleIndex_add_one_mul_pi n
    have hdist : Real.pi / 2 ≤ -((n : ℝ) - (r : ℝ) * Real.pi / 2) := by
      rw [hr']
      nlinarith
    exact (abs_poleOffset_le n).trans (hdist.trans (neg_le_abs _))

end TangentLimit
