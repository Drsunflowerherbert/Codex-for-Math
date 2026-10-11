import TangentLimit
import EvidenceHarness
open Filter Topology
namespace TangentLimit

#evidence_check TangentLimit.PiDiophantine : Prop
#evidence_check TangentLimit.abs_cos_eq_abs_sin_offset : ∀ (x : ℝ) (k : ℕ), |Real.cos x| =
      |Real.sin (x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2)|
#evidence_check TangentLimit.abs_poleOffset_le : ∀ (n : ℕ), |poleOffset n| ≤ Real.pi / 2
#evidence_check TangentLimit.abs_tan_div_cube_eq : ∀ (n : ℕ), |Real.tan (n : ℝ) / (n : ℝ) ^ 3| = |Real.tan (n : ℝ)| / (n : ℝ) ^ 3
#evidence_check TangentLimit.chord_cos_bound : ∀ (x : ℝ) (k : ℕ)
    (hb : |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2| ≤ Real.pi / 2), (2 / Real.pi) * |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2| ≤
      |Real.cos x|
#evidence_check TangentLimit.cos_intCast_ne_zero : ∀ (n : ℤ), Real.cos (n : ℝ) ≠ 0
#evidence_check TangentLimit.cos_natCast_ne_zero : ∀ (n : ℕ), Real.cos (n : ℝ) ≠ 0
#evidence_check TangentLimit.eventual_abs_tan_div_cube_le_rpow : ∀ (h : PiDiophantine), ∀ᶠ n : ℕ in atTop,
      |Real.tan (n : ℝ)| / (n : ℝ) ^ 3 ≤
        (Real.pi * (2 : ℝ) ^ (3 / 2 : ℝ)) * (n : ℝ) ^ (-(3 / 2 : ℝ))
#evidence_check TangentLimit.eventually_abs_tan_le_quadratic : ∀ (h : PiDiophantine), ∀ᶠ n : ℕ in atTop, |Real.tan (n : ℝ)| ≤ 4 * Real.pi * (n : ℝ) ^ 2
#evidence_check TangentLimit.eventually_poleDenom_ge : ∀ (Q : ℕ), ∀ᶠ n : ℕ in atTop, Q ≤ poleDenom n
#evidence_check TangentLimit.eventually_tan_le_pole_rpow : ∀ (h : PiDiophantine)
    (ν : ℝ) (hν : 2 < ν), ∀ᶠ n : ℕ in Filter.atTop,
      |Real.tan (n : ℝ)| ≤ Real.pi * (poleDenom n : ℝ) ^ (ν - 1)
#evidence_check TangentLimit.lt_poleIndex_add_one_mul_pi : ∀ (n : ℕ), (n : ℝ) < ((poleIndex n : ℝ) + 1) * Real.pi
#evidence_check TangentLimit.poleDenom : ∀ (n : ℕ), ℕ
#evidence_check TangentLimit.poleDenom_le_two_mul : ∀ (n : ℕ) (hn : 1 ≤ n), (poleDenom n : ℝ) ≤ 2 * (n : ℝ)
#evidence_check TangentLimit.poleDenom_odd : ∀ (n : ℕ), Odd (poleDenom n)
#evidence_check TangentLimit.poleDenom_pos : ∀ (n : ℕ), 0 < poleDenom n
#evidence_check TangentLimit.poleIndex : ∀ (n : ℕ), ℕ
#evidence_check TangentLimit.poleIndex_mul_pi_le : ∀ (n : ℕ), (poleIndex n : ℝ) * Real.pi ≤ (n : ℝ)
#evidence_check TangentLimit.poleOffset : ∀ (n : ℕ), ℝ
#evidence_check TangentLimit.poleOffset_nearest : ∀ (n : ℕ) (r : ℤ) (hr : Odd r), |poleOffset n| ≤ |(n : ℝ) - (r : ℝ) * Real.pi / 2|
#evidence_check TangentLimit.pole_distance_identity : ∀ (x q : ℝ) (hq : 0 < q), |x - q * Real.pi / 2| = (q / 2) * |Real.pi - (2 * x) / q|
#evidence_check TangentLimit.pole_distance_lower_bound : ∀ (x q ν : ℝ) (hq : 0 < q)
    (happrox : q ^ (-ν) ≤ |Real.pi - (2 * x) / q|), (1 / 2 : ℝ) * q ^ (1 - ν) ≤ |x - q * Real.pi / 2|
#evidence_check TangentLimit.pole_distance_lower_bound_of_piDiophantine : ∀ (h : PiDiophantine)
    (ν : ℝ) (hν : 2 < ν), ∃ Q : ℕ, ∀ n q : ℕ, Q ≤ q → 0 < q →
      (1 / 2 : ℝ) * (q : ℝ) ^ (1 - ν) ≤
        |(n : ℝ) - (q : ℝ) * Real.pi / 2|
#evidence_check TangentLimit.reciprocal_pole_power : ∀ (q ν : ℝ) (hq : 0 < q), 1 / (q ^ (1 - ν) / Real.pi) = Real.pi * q ^ (ν - 1)
#evidence_check TangentLimit.summable_abs_tan_div_cube : ∀ (h : PiDiophantine), Summable (fun n : ℕ => |Real.tan (n : ℝ)| / (n : ℝ) ^ 3)
#evidence_check TangentLimit.summable_abs_tan_div_cube_positive : ∀ (h : PiDiophantine), Summable (fun n : ℕ => |Real.tan ((n + 1 : ℕ) : ℝ)| /
      ((n + 1 : ℕ) : ℝ) ^ 3)
#evidence_check TangentLimit.summable_abs_tan_div_cube_quotient : ∀ (h : PiDiophantine), Summable (fun n : ℕ => |Real.tan (n : ℝ) / (n : ℝ) ^ 3|)
#evidence_check TangentLimit.summable_abs_tan_div_cube_quotient_positive : ∀ (h : PiDiophantine), Summable (fun n : ℕ => |Real.tan ((n + 1 : ℕ) : ℝ) /
      ((n + 1 : ℕ) : ℝ) ^ 3|)
#evidence_check TangentLimit.summable_tan_div_cube : ∀ (h : PiDiophantine), Summable (fun n : ℕ => Real.tan (n : ℝ) / (n : ℝ) ^ 3)
#evidence_check TangentLimit.summable_tan_div_cube_positive : ∀ (h : PiDiophantine), Summable (fun n : ℕ => Real.tan ((n + 1 : ℕ) : ℝ) /
      ((n + 1 : ℕ) : ℝ) ^ 3)
#evidence_check TangentLimit.tan_div_cube_positive_tendsto_zero : ∀ (h : PiDiophantine), Tendsto (fun n : ℕ => Real.tan ((n + 1 : ℕ) : ℝ) /
      ((n + 1 : ℕ) : ℝ) ^ 3) atTop (nhds 0)
#evidence_check TangentLimit.tan_div_cube_tendsto_zero : ∀ (h : PiDiophantine), Tendsto (fun n : ℕ => Real.tan (n : ℝ) / (n : ℝ) ^ 3) atTop (nhds 0)
#evidence_check TangentLimit.tan_le_of_cos_lower_bound : ∀ {x B : ℝ}
    (hB : 0 < B) (hcos : B ≤ |Real.cos x|), |Real.tan x| ≤ 1 / B
#evidence_check TangentLimit.tan_le_of_pole_distance : ∀ {x : ℝ} {k : ℕ}
    (hb : |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2| ≤ Real.pi / 2)
    (hd : 0 < |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2|), |Real.tan x| ≤
      Real.pi / (2 * |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2|)
#evidence_check TangentLimit.tan_le_pole_power : ∀ (x ν : ℝ) (k : ℕ)
    (hb : |x - ((2 * k + 1 : ℕ) : ℝ) * Real.pi / 2| ≤ Real.pi / 2)
    (happrox : ((2 * k + 1 : ℕ) : ℝ) ^ (-ν) ≤
      |Real.pi - (2 * x) / ((2 * k + 1 : ℕ) : ℝ)|), |Real.tan x| ≤ Real.pi * ((2 * k + 1 : ℕ) : ℝ) ^ (ν - 1)
#evidence_check TangentLimit.tendsto_div_cube_of_eventually_abs_le_sq : ∀ {f : ℕ → ℝ} {C : ℝ}
    (h : ∀ᶠ n in atTop, |f n| ≤ C * (n : ℝ) ^ 2), Tendsto (fun n => f n / (n : ℝ) ^ 3) atTop (nhds 0)
#evidence_check TangentLimit.tendsto_div_cube_positive_of_eventually_abs_le_sq : ∀ {f : ℕ → ℝ} {C : ℝ}
    (h : ∀ᶠ n in atTop, |f (n + 1)| ≤ C * ((n + 1 : ℕ) : ℝ) ^ 2), Tendsto (fun n => f (n + 1) / ((n + 1 : ℕ) : ℝ) ^ 3) atTop (nhds 0)

end TangentLimit
