import MixedMoments.FormalContact
import MixedMoments.FormalSquareRoot

/-!
# Finite analytic contact

This file proves the analytic contact bridge using only finite polynomial
approximations to the inverse square root. Positive-side and two-sided
big-O hypotheses are kept separate throughout.
-/

noncomputable section

open Filter Set Asymptotics
open scoped Topology

namespace MixedMoments

/-- One-sided polynomial big-O contact forces every lower coefficient to vanish. -/
theorem polynomial_coeff_zero_of_isBigO_eval_pow
    (F : Polynomial ℝ) (L : ℕ)
    (h : (fun x : ℝ => F.eval x) =O[𝓝[>] 0] (fun x => x ^ L)) :
    ∀ j < L, F.coeff j = 0 := by
  induction L generalizing F with
  | zero => intro j hj; omega
  | succ L ih =>
    have hpow : Tendsto (fun x : ℝ => x ^ (L + 1)) (𝓝[>] 0) (𝓝 0) := by
      simpa using ((continuous_id.pow (L + 1)).tendsto (0 : ℝ)).mono_left
        nhdsWithin_le_nhds
    have hlim : Tendsto (fun x : ℝ => F.eval x) (𝓝[>] 0) (𝓝 0) :=
      h.trans_tendsto hpow
    have hpoly : Tendsto (fun x : ℝ => F.eval x) (𝓝[>] 0) (𝓝 (F.eval 0)) :=
      (F.continuous.tendsto 0).mono_left nhdsWithin_le_nhds
    have hz : F.coeff 0 = 0 := by
      rw [Polynomial.coeff_zero_eq_eval_zero]
      exact tendsto_nhds_unique hpoly hlim
    have heq (x : ℝ) : F.eval x = x * F.divX.eval x := by
      have hfactor := congrArg (fun P : Polynomial ℝ => P.eval x) (F.X_mul_divX_add)
      simpa [hz] using hfactor.symm
    have hmul : (fun x : ℝ => x * F.divX.eval x) =O[𝓝[>] 0]
        (fun x => x ^ (L + 1)) := h.congr_left heq
    have hne : ∀ᶠ x : ℝ in 𝓝[>] 0, x ≠ 0 := by
      filter_upwards [self_mem_nhdsWithin] with x hx
      exact ne_of_gt hx
    have hdiv : (fun x : ℝ => F.divX.eval x) =O[𝓝[>] 0] (fun x => x ^ L) := by
      have hd := (isBigO_mul_iff_isBigO_div hne).mp hmul
      apply hd.congr' (Eventually.of_forall fun _ => rfl)
      filter_upwards [hne] with x hx
      change x ^ (L + 1) / x = x ^ L
      rw [pow_succ, mul_div_cancel_right₀ _ hx]
    intro j hj
    cases j with
    | zero => exact hz
    | succ j =>
      simpa only [Polynomial.coeff_divX] using ih F.divX hdiv j (by omega)

/-- Two-sided contact is an immediate specialization, with sidedness explicit. -/
theorem polynomial_coeff_zero_of_isBigO_eval_pow_nhds
    (F : Polynomial ℝ) (L : ℕ)
    (h : (fun x : ℝ => F.eval x) =O[𝓝 0] (fun x => x ^ L)) :
    ∀ j < L, F.coeff j = 0 :=
  polynomial_coeff_zero_of_isBigO_eval_pow F L (h.mono nhdsWithin_le_nhds)

/-- One extra coefficient keeps the constant term equal to one even when `L=0`. -/
def inverseSqrtApprox (L : ℕ) : Polynomial ℚ :=
  PowerSeries.trunc (L + 1) inverseSqrtFormalSeries

def inverseSqrtApproxError {R : Type*} [Ring R] (C : Polynomial R) : Polynomial R :=
  (1 - Polynomial.X ^ 2) * C ^ 2 - 1

theorem inverseSqrtApprox_coeff_zero (L : ℕ) : (inverseSqrtApprox L).coeff 0 = 1 := by
  simp [inverseSqrtApprox, PowerSeries.coeff_trunc]

theorem inverseSqrtApprox_error_coeff (L j : ℕ) (hj : j < L + 1) :
    (inverseSqrtApproxError (inverseSqrtApprox L)).coeff j = 0 := by
  let A : Polynomial ℚ := 1 - Polynomial.X ^ 2
  have ht : PowerSeries.trunc (L + 1)
      ((A : PowerSeries ℚ) * (inverseSqrtApprox L : PowerSeries ℚ) ^ 2) =
      PowerSeries.trunc (L + 1) ((A : PowerSeries ℚ) * inverseSqrtFormalSeries ^ 2) := by
    unfold inverseSqrtApprox
    rw [← PowerSeries.trunc_mul_trunc (A : PowerSeries ℚ)
      ((PowerSeries.trunc (L + 1) inverseSqrtFormalSeries : PowerSeries ℚ) ^ 2),
      PowerSeries.trunc_trunc_pow, PowerSeries.trunc_mul_trunc]
  have hA : (A : PowerSeries ℚ) = 1 - PowerSeries.X ^ 2 := by
    simp [A]
  rw [hA, inverseSqrtFormalSeries_square] at ht
  have hc := congrArg (fun P : Polynomial ℚ => P.coeff j) ht
  simp only [PowerSeries.coeff_trunc, if_pos hj] at hc
  have hp : ((A * inverseSqrtApprox L ^ 2 : Polynomial ℚ) : PowerSeries ℚ) =
      (A : PowerSeries ℚ) * (inverseSqrtApprox L : PowerSeries ℚ) ^ 2 := by simp
  rw [← hA, ← hp, Polynomial.coeff_coe] at hc
  have hc' : (A * inverseSqrtApprox L ^ 2).coeff j = (1 : Polynomial ℚ).coeff j := by
    simpa only [PowerSeries.coeff_one, Polynomial.coeff_one] using hc
  change (A * inverseSqrtApprox L ^ 2 - 1).coeff j = 0
  rw [Polynomial.coeff_sub, hc', sub_self]

/-- A finite algebraic square-root approximation has the expected analytic remainder. -/
theorem inverseSqrtApproximation_isBigO (C : Polynomial ℝ) (L : ℕ)
    (hC : C.coeff 0 = 1)
    (herror : ∀ j < L, (inverseSqrtApproxError C).coeff j = 0) :
    (fun x : ℝ => C.eval x - 1 / Real.sqrt (1 - x ^ 2)) =O[𝓝 0]
      (fun x => x ^ L) := by
  obtain ⟨R, hR⟩ := Polynomial.X_pow_dvd_iff.mpr herror
  let den (x : ℝ) := Real.sqrt (1 - x ^ 2) *
    (Real.sqrt (1 - x ^ 2) * C.eval x + 1)
  have hden : Tendsto den (𝓝 0) (𝓝 2) := by
    have hc : Continuous den := by unfold den; fun_prop
    convert hc.tendsto 0 using 1
    norm_num [den, ← Polynomial.coeff_zero_eq_eval_zero, hC]
  have hdenne : ∀ᶠ x in 𝓝 (0 : ℝ), den x ≠ 0 :=
    hden.eventually_ne (by norm_num)
  have hinside : ∀ᶠ x : ℝ in 𝓝 0, 0 < 1 - x ^ 2 := by
    have ht : Tendsto (fun x : ℝ => 1 - x ^ 2) (𝓝 0) (𝓝 1) := by
      simpa using ((continuous_const.sub (continuous_id.pow 2)).tendsto (0 : ℝ))
    exact ht.eventually (Ioi_mem_nhds (by norm_num : (0 : ℝ) < 1))
  have hquot : Tendsto (fun x => R.eval x / den x) (𝓝 0) (𝓝 (R.eval 0 / 2)) :=
    (R.continuous.tendsto 0).div hden (by norm_num)
  have hbound : (fun x : ℝ => x ^ L * (R.eval x / den x)) =O[𝓝 0]
      (fun x => x ^ L) := by
    simpa using (isBigO_refl (fun x : ℝ => x ^ L) (𝓝 0)).mul (hquot.isBigO_one ℝ)
  apply hbound.congr' _ (Eventually.of_forall fun _ => rfl)
  filter_upwards [hdenne, hinside] with x hxden hxpos
  have hxroot : Real.sqrt (1 - x ^ 2) ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr hxpos)
  have hxrootSq : Real.sqrt (1 - x ^ 2) ^ 2 = 1 - x ^ 2 := Real.sq_sqrt hxpos.le
  have he := congrArg (fun P : Polynomial ℝ => P.eval x) hR
  simp only [inverseSqrtApproxError, Polynomial.eval_sub, Polynomial.eval_mul,
    Polynomial.eval_pow, Polynomial.eval_one, Polynomial.eval_X] at he
  dsimp [den] at hxden ⊢
  have hxplus : Real.sqrt (1 - x ^ 2) * C.eval x + 1 ≠ 0 :=
    (mul_ne_zero_iff.mp hxden).2
  have he' : x ^ L * R.eval x = Real.sqrt (1 - x ^ 2) ^ 2 * C.eval x ^ 2 - 1 := by
    rw [hxrootSq]
    exact he.symm
  rw [← mul_div_assoc, he']
  field_simp [hxroot, hxplus]
  ring

def inverseSqrtApproxReal (L : ℕ) : Polynomial ℝ :=
  (inverseSqrtApprox L).map (Rat.castHom ℝ)

theorem inverseSqrtApproxReal_remainder (L : ℕ) :
    (fun x : ℝ => (inverseSqrtApproxReal L).eval x - 1 / Real.sqrt (1 - x ^ 2))
      =O[𝓝 0] (fun x => x ^ L) := by
  apply inverseSqrtApproximation_isBigO
  · simp [inverseSqrtApproxReal, Polynomial.coeff_map, inverseSqrtApprox_coeff_zero]
  · intro j hj
    have heq : inverseSqrtApproxError (inverseSqrtApproxReal L) =
        (inverseSqrtApproxError (inverseSqrtApprox L)).map (Rat.castHom ℝ) := by
      simp [inverseSqrtApproxError, inverseSqrtApproxReal]
    rw [heq, Polynomial.coeff_map, inverseSqrtApprox_error_coeff L j (by omega)]
    simp

/-- A rational polynomial whose lower coefficients encode the actual contact jet. -/
def contactApproximation (P D : Polynomial ℚ) (L : ℕ) : Polynomial ℚ :=
  Polynomial.X * P * inverseSqrtApprox L - D

theorem contactApproximation_coeff (P D : Polynomial ℚ) (L j : ℕ) (hj : j < L + 1) :
    (contactApproximation P D L).coeff j = polynomialDefect P D j := by
  have ht := PowerSeries.trunc_mul_trunc (n := L + 1)
    (PowerSeries.X * (P : PowerSeries ℚ)) inverseSqrtFormalSeries
  have hc := congrArg (fun Q : Polynomial ℚ => Q.coeff j) ht
  simp only [PowerSeries.coeff_trunc, if_pos hj] at hc
  change PowerSeries.coeff j
      (PowerSeries.X * (P : PowerSeries ℚ) * (inverseSqrtApprox L : PowerSeries ℚ)) =
      PowerSeries.coeff j (PowerSeries.X * (P : PowerSeries ℚ) * inverseSqrtFormalSeries) at hc
  have hp : ((Polynomial.X * P * inverseSqrtApprox L : Polynomial ℚ) : PowerSeries ℚ) =
      PowerSeries.X * (P : PowerSeries ℚ) * (inverseSqrtApprox L : PowerSeries ℚ) := by simp
  rw [← hp, Polynomial.coeff_coe] at hc
  rw [← contactCoefficient_eq_powerSeries_coeff] at hc
  simp only [contactApproximation, polynomialDefect, Polynomial.coeff_sub, hc]

/-- The actual real contact function, using the positive real square root. -/
def analyticContactFunction (P D : Polynomial ℚ) (x : ℝ) : ℝ :=
  x * (P.map (Rat.castHom ℝ)).eval x / Real.sqrt (1 - x ^ 2) -
    (D.map (Rat.castHom ℝ)).eval x

/-- Positive-side analytic big-O contact implies the finite coefficient condition.
No conversion from a one-sided filter to a two-sided filter is used. -/
theorem analyticContact_implies_coefficientContact (P D : Polynomial ℚ) (L : ℕ)
    (hcontact : analyticContactFunction P D =O[𝓝[>] 0] (fun x => x ^ L)) :
    CoefficientContact P D L := by
  let F : Polynomial ℝ := (contactApproximation P D L).map (Rat.castHom ℝ)
  have hfactor : (fun x : ℝ => x * (P.map (Rat.castHom ℝ)).eval x)
      =O[𝓝 0] (fun _ => (1 : ℝ)) :=
    ((continuous_id.mul (P.map (Rat.castHom ℝ)).continuous).tendsto 0).isBigO_one ℝ
  have hremainder : (fun x : ℝ => x * (P.map (Rat.castHom ℝ)).eval x *
      ((inverseSqrtApproxReal L).eval x - 1 / Real.sqrt (1 - x ^ 2)))
        =O[𝓝 0] (fun x => x ^ L) := by
    simpa using hfactor.mul (inverseSqrtApproxReal_remainder L)
  have hpoly : (fun x : ℝ => F.eval x) =O[𝓝[>] 0] (fun x => x ^ L) := by
    have hsum := hcontact.add (hremainder.mono nhdsWithin_le_nhds)
    apply hsum.congr_left
    intro x
    simp only [analyticContactFunction, F, contactApproximation, Polynomial.map_sub,
      Polynomial.map_mul, Polynomial.map_X, Polynomial.eval_sub, Polynomial.eval_mul,
      Polynomial.eval_X, inverseSqrtApproxReal]
    rw [div_eq_mul_inv, div_eq_mul_inv]
    ring
  intro j hj
  have hz := polynomial_coeff_zero_of_isBigO_eval_pow F L hpoly j hj
  have hcoeff : ((contactApproximation P D L).coeff j : ℝ) = 0 := by
    simpa [F, Polynomial.coeff_map] using hz
  rw [contactApproximation_coeff P D L j (by omega)] at hcoeff
  exact_mod_cast hcoeff

theorem analyticContact_nhds_implies_coefficientContact (P D : Polynomial ℚ) (L : ℕ)
    (hcontact : analyticContactFunction P D =O[𝓝 0] (fun x => x ^ L)) :
    CoefficientContact P D L :=
  analyticContact_implies_coefficientContact P D L (hcontact.mono nhdsWithin_le_nhds)

theorem polynomial_eval_isBigO_pow_of_coeff_zero (F : Polynomial ℝ) (L : ℕ)
    (h : ∀ j < L, F.coeff j = 0) :
    (fun x : ℝ => F.eval x) =O[𝓝 0] (fun x => x ^ L) := by
  obtain ⟨R, hR⟩ := Polynomial.X_pow_dvd_iff.mpr h
  have ht := (R.continuous.tendsto 0).isBigO_one ℝ
  have hb : (fun x : ℝ => x ^ L * R.eval x) =O[𝓝 0] (fun x => x ^ L) := by
    simpa using (isBigO_refl (fun x : ℝ => x ^ L) (𝓝 0)).mul ht
  apply hb.congr_left
  intro x
  have he := congrArg (fun P : Polynomial ℝ => P.eval x) hR
  simpa only [Polynomial.eval_mul, Polynomial.eval_pow, Polynomial.eval_X] using he.symm

/-- The finite coefficient condition also gives two-sided analytic contact. -/
theorem coefficientContact_implies_analyticContact (P D : Polynomial ℚ) (L : ℕ)
    (hcontact : CoefficientContact P D L) :
    analyticContactFunction P D =O[𝓝 0] (fun x => x ^ L) := by
  let F : Polynomial ℝ := (contactApproximation P D L).map (Rat.castHom ℝ)
  have hF : ∀ j < L, F.coeff j = 0 := by
    intro j hj
    simp only [F, Polynomial.coeff_map]
    rw [contactApproximation_coeff P D L j (by omega), hcontact j hj]
    simp
  have hpoly := polynomial_eval_isBigO_pow_of_coeff_zero F L hF
  have hfactor : (fun x : ℝ => x * (P.map (Rat.castHom ℝ)).eval x)
      =O[𝓝 0] (fun _ => (1 : ℝ)) :=
    ((continuous_id.mul (P.map (Rat.castHom ℝ)).continuous).tendsto 0).isBigO_one ℝ
  have hremainder : (fun x : ℝ => x * (P.map (Rat.castHom ℝ)).eval x *
      ((inverseSqrtApproxReal L).eval x - 1 / Real.sqrt (1 - x ^ 2)))
        =O[𝓝 0] (fun x => x ^ L) := by
    simpa using hfactor.mul (inverseSqrtApproxReal_remainder L)
  apply (hpoly.sub hremainder).congr_left
  intro x
  simp only [analyticContactFunction, F, contactApproximation, Polynomial.map_sub,
    Polynomial.map_mul, Polynomial.map_X, Polynomial.eval_sub, Polynomial.eval_mul,
    Polynomial.eval_X, inverseSqrtApproxReal]
  rw [div_eq_mul_inv, div_eq_mul_inv]
  ring

theorem analyticContact_nhds_iff_coefficientContact (P D : Polynomial ℚ) (L : ℕ) :
    (analyticContactFunction P D =O[𝓝 0] (fun x => x ^ L)) ↔
      CoefficientContact P D L :=
  ⟨analyticContact_nhds_implies_coefficientContact P D L,
    coefficientContact_implies_analyticContact P D L⟩

theorem analyticContact_right_iff_coefficientContact (P D : Polynomial ℚ) (L : ℕ) :
    (analyticContactFunction P D =O[𝓝[>] 0] (fun x => x ^ L)) ↔
      CoefficientContact P D L :=
  ⟨analyticContact_implies_coefficientContact P D L,
    fun h => (coefficientContact_implies_analyticContact P D L h).mono nhdsWithin_le_nhds⟩

theorem contactTruncation_analyticContact (P : Polynomial ℚ) (L : ℕ) :
    analyticContactFunction P (contactTruncation P L) =O[𝓝 0] (fun x => x ^ L) :=
  coefficientContact_implies_analyticContact P (contactTruncation P L) L
    (contactTruncation_contact P L)

/-- Analytic big-O contact is sufficient for cancellation once real-array
decompositions have been established. -/
theorem cancellation_of_analyticContact
    (M Z : ℕ → ℕ → ℝ) (G ζ : ℝ)
    (hM : ∀ i j, M i j = Coordinates.eval G ζ (formalM i j))
    (hZ : ∀ i j, Z i j = Coordinates.eval G ζ (formalZ i j))
    (P D : Polynomial ℚ) (L j : ℕ)
    (hcontact : analyticContactFunction P D =O[𝓝[>] 0] (fun x => x ^ L))
    (hj : j < L) :
    ∃ a b : ℚ,
      realPolynomialContraction M P j -
        (3 / 2 : ℝ) * realPolynomialContraction Z D j =
          (a : ℝ) + (b : ℝ) * G :=
  cancellation_of_decompositions M Z G ζ hM hZ P D L j
    (analyticContact_implies_coefficientContact P D L hcontact) hj

end MixedMoments
