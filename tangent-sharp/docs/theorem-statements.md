# Compiled theorem statements and axiom inventory

All declarations below were printed by the pinned Lean 4.24.0 compiler
against the final publication source. The visible hypothesis is unproved and
remains an explicit theorem argument. Exact mathlib commit:
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.

Compiler output from `scripts/TheoremInventory.lean`:

```text
def TangentLimit.PiDiophantine : Prop :=
∀ (ν : ℝ), 2 < ν → ∃ Q, ∀ (q : ℕ), Q ≤ q → 0 < q → ∀ (p : ℤ), ↑q ^ (-ν) ≤ |Real.pi - ↑p / ↑q|
TangentLimit.pole_distance_identity (x q : ℝ) (hq : 0 < q) : |x - q * Real.pi / 2| = q / 2 * |Real.pi - 2 * x / q|
TangentLimit.pole_distance_lower_bound (x q ν : ℝ) (hq : 0 < q) (happrox : q ^ (-ν) ≤ |Real.pi - 2 * x / q|) :
  1 / 2 * q ^ (1 - ν) ≤ |x - q * Real.pi / 2|
TangentLimit.reciprocal_pole_power (q ν : ℝ) (hq : 0 < q) : 1 / (q ^ (1 - ν) / Real.pi) = Real.pi * q ^ (ν - 1)
TangentLimit.pole_distance_lower_bound_of_piDiophantine (h : TangentLimit.PiDiophantine) (ν : ℝ) (hν : 2 < ν) :
  ∃ Q, ∀ (n q : ℕ), Q ≤ q → 0 < q → 1 / 2 * ↑q ^ (1 - ν) ≤ |↑n - ↑q * Real.pi / 2|
TangentLimit.tan_le_pole_power (x ν : ℝ) (k : ℕ) (hb : |x - ↑(2 * k + 1) * Real.pi / 2| ≤ Real.pi / 2)
  (happrox : ↑(2 * k + 1) ^ (-ν) ≤ |Real.pi - 2 * x / ↑(2 * k + 1)|) : |Real.tan x| ≤ Real.pi * ↑(2 * k + 1) ^ (ν - 1)
TangentLimit.eventually_tan_le_pole_rpow (h : TangentLimit.PiDiophantine) (ν : ℝ) (hν : 2 < ν) :
  ∀ᶠ (n : ℕ) in Filter.atTop, |Real.tan ↑n| ≤ Real.pi * ↑(TangentLimit.poleDenom n) ^ (ν - 1)
TangentLimit.PiDiophantine : Prop
TangentLimit.eventually_abs_tan_le_quadratic (h : TangentLimit.PiDiophantine) :
  ∀ᶠ (n : ℕ) in Filter.atTop, |Real.tan ↑n| ≤ 4 * Real.pi * ↑n ^ 2
TangentLimit.tan_div_cube_tendsto_zero (h : TangentLimit.PiDiophantine) :
  Filter.Tendsto (fun n => Real.tan ↑n / ↑n ^ 3) Filter.atTop (nhds 0)
TangentLimit.tan_div_cube_positive_tendsto_zero (h : TangentLimit.PiDiophantine) :
  Filter.Tendsto (fun n => Real.tan ↑(n + 1) / ↑(n + 1) ^ 3) Filter.atTop (nhds 0)
TangentLimit.tendsto_div_cube_of_eventually_abs_le_sq {f : ℕ → ℝ} {C : ℝ}
  (h : ∀ᶠ (n : ℕ) in Filter.atTop, |f n| ≤ C * ↑n ^ 2) : Filter.Tendsto (fun n => f n / ↑n ^ 3) Filter.atTop (nhds 0)
TangentLimit.tendsto_div_cube_positive_of_eventually_abs_le_sq {f : ℕ → ℝ} {C : ℝ}
  (h : ∀ᶠ (n : ℕ) in Filter.atTop, |f (n + 1)| ≤ C * ↑(n + 1) ^ 2) :
  Filter.Tendsto (fun n => f (n + 1) / ↑(n + 1) ^ 3) Filter.atTop (nhds 0)
TangentLimit.poleIndex (n : ℕ) : ℕ
TangentLimit.poleDenom (n : ℕ) : ℕ
TangentLimit.poleOffset (n : ℕ) : ℝ
TangentLimit.poleDenom_pos (n : ℕ) : 0 < TangentLimit.poleDenom n
TangentLimit.poleDenom_odd (n : ℕ) : Odd (TangentLimit.poleDenom n)
TangentLimit.poleIndex_mul_pi_le (n : ℕ) : ↑(TangentLimit.poleIndex n) * Real.pi ≤ ↑n
TangentLimit.lt_poleIndex_add_one_mul_pi (n : ℕ) : ↑n < (↑(TangentLimit.poleIndex n) + 1) * Real.pi
TangentLimit.abs_poleOffset_le (n : ℕ) : |TangentLimit.poleOffset n| ≤ Real.pi / 2
TangentLimit.poleDenom_le_two_mul (n : ℕ) (hn : 1 ≤ n) : ↑(TangentLimit.poleDenom n) ≤ 2 * ↑n
TangentLimit.eventually_poleDenom_ge (Q : ℕ) : ∀ᶠ (n : ℕ) in Filter.atTop, Q ≤ TangentLimit.poleDenom n
TangentLimit.poleOffset_nearest (n : ℕ) (r : ℤ) (hr : Odd r) : |TangentLimit.poleOffset n| ≤ |↑n - ↑r * Real.pi / 2|
TangentLimit.cos_intCast_ne_zero (n : ℤ) : Real.cos ↑n ≠ 0
TangentLimit.cos_natCast_ne_zero (n : ℕ) : Real.cos ↑n ≠ 0
TangentLimit.eventual_abs_tan_div_cube_le_rpow (h : TangentLimit.PiDiophantine) :
  ∀ᶠ (n : ℕ) in Filter.atTop, |Real.tan ↑n| / ↑n ^ 3 ≤ Real.pi * 2 ^ (3 / 2) * ↑n ^ (-(3 / 2))
TangentLimit.summable_abs_tan_div_cube (h : TangentLimit.PiDiophantine) : Summable fun n => |Real.tan ↑n| / ↑n ^ 3
TangentLimit.summable_abs_tan_div_cube_positive (h : TangentLimit.PiDiophantine) :
  Summable fun n => |Real.tan ↑(n + 1)| / ↑(n + 1) ^ 3
TangentLimit.abs_tan_div_cube_eq (n : ℕ) : |Real.tan ↑n / ↑n ^ 3| = |Real.tan ↑n| / ↑n ^ 3
TangentLimit.summable_abs_tan_div_cube_quotient (h : TangentLimit.PiDiophantine) :
  Summable fun n => |Real.tan ↑n / ↑n ^ 3|
TangentLimit.summable_tan_div_cube (h : TangentLimit.PiDiophantine) : Summable fun n => Real.tan ↑n / ↑n ^ 3
TangentLimit.summable_abs_tan_div_cube_quotient_positive (h : TangentLimit.PiDiophantine) :
  Summable fun n => |Real.tan ↑(n + 1) / ↑(n + 1) ^ 3|
TangentLimit.summable_tan_div_cube_positive (h : TangentLimit.PiDiophantine) :
  Summable fun n => Real.tan ↑(n + 1) / ↑(n + 1) ^ 3
TangentLimit.abs_cos_eq_abs_sin_offset (x : ℝ) (k : ℕ) : |Real.cos x| = |Real.sin (x - ↑(2 * k + 1) * Real.pi / 2)|
TangentLimit.chord_cos_bound (x : ℝ) (k : ℕ) (hb : |x - ↑(2 * k + 1) * Real.pi / 2| ≤ Real.pi / 2) :
  2 / Real.pi * |x - ↑(2 * k + 1) * Real.pi / 2| ≤ |Real.cos x|
TangentLimit.tan_le_of_cos_lower_bound {x B : ℝ} (hB : 0 < B) (hcos : B ≤ |Real.cos x|) : |Real.tan x| ≤ 1 / B
TangentLimit.tan_le_of_pole_distance {x : ℝ} {k : ℕ} (hb : |x - ↑(2 * k + 1) * Real.pi / 2| ≤ Real.pi / 2)
  (hd : 0 < |x - ↑(2 * k + 1) * Real.pi / 2|) : |Real.tan x| ≤ Real.pi / (2 * |x - ↑(2 * k + 1) * Real.pi / 2|)
'TangentLimit.pole_distance_identity' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.pole_distance_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.reciprocal_pole_power' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.pole_distance_lower_bound_of_piDiophantine' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.tan_le_pole_power' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.eventually_tan_le_pole_rpow' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.PiDiophantine' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.eventually_abs_tan_le_quadratic' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.tan_div_cube_tendsto_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.tan_div_cube_positive_tendsto_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.tendsto_div_cube_of_eventually_abs_le_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.tendsto_div_cube_positive_of_eventually_abs_le_sq' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
'TangentLimit.poleIndex' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.poleDenom' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.poleOffset' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.poleDenom_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.poleDenom_odd' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.poleIndex_mul_pi_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.lt_poleIndex_add_one_mul_pi' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.abs_poleOffset_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.poleDenom_le_two_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.eventually_poleDenom_ge' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.poleOffset_nearest' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.cos_intCast_ne_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.cos_natCast_ne_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.eventual_abs_tan_div_cube_le_rpow' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.summable_abs_tan_div_cube' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.summable_abs_tan_div_cube_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.abs_tan_div_cube_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.summable_abs_tan_div_cube_quotient' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.summable_tan_div_cube' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.summable_abs_tan_div_cube_quotient_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.summable_tan_div_cube_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.abs_cos_eq_abs_sin_offset' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.chord_cos_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.tan_le_of_cos_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'TangentLimit.tan_le_of_pole_distance' depends on axioms: [propext, Classical.choice, Quot.sound]
```
