import ConvexApprox.Barrier
import Mathlib
noncomputable section
open scoped BigOperators InnerProductSpace
namespace ConvexApprox
variable {E ι : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [Fintype ι]
def directionalBarrier (u : ι → E) (h : ι → ℝ) (ε t : ℝ) (x : E) : ℝ :=
  ∑ i, Real.exp (t * (⟪u i, x⟫_ℝ - h i - ε))

theorem directionalBarrier_le (u : ι → E) (h : ι → ℝ) (ε t r : ℝ) (x : E)
    (ht : 0 ≤ t) (hdef : ∀ i, ⟪u i, x⟫_ℝ - h i ≤ r) :
    directionalBarrier u h ε t x ≤ (Fintype.card ι : ℝ) * Real.exp (t * (r - ε)) := by
  unfold directionalBarrier
  calc
    _ ≤ ∑ _i : ι, Real.exp (t * (r - ε)) := by
      apply Finset.sum_le_sum
      intro i hi
      apply Real.exp_le_exp.mpr
      exact mul_le_mul_of_nonneg_left (by linarith [hdef i]) ht
    _ = _ := by simp

theorem directionalBarrier_halfspace (u : ι → E) (h : ι → ℝ) (ε t : ℝ) (x : E)
    (ht : 0 < t) (hx : directionalBarrier u h ε t x ≤ 1) (i : ι) :
    ⟪u i, x⟫_ℝ ≤ h i + ε := by
  have hs : Real.exp (t * (⟪u i, x⟫_ℝ - h i - ε)) ≤ directionalBarrier u h ε t x := by
    unfold directionalBarrier
    exact Finset.single_le_sum (fun j _ => (Real.exp_pos (t * (⟪u j,x⟫_ℝ - h j - ε))).le) (Finset.mem_univ i)
  have he : t * (⟪u i, x⟫_ℝ - h i - ε) ≤ 0 :=
    Real.exp_le_one_iff.mp (hs.trans hx)
  nlinarith

theorem directionalBarrier_tube (u : ι → E) (h : ι → ℝ) (ε t η : ℝ) (x w : E)
    (ht : 0 < t) (hu : ∀ i, ‖u i‖ = 1) (hw : ∀ i, ⟪u i,w⟫_ℝ ≤ h i)
    (hd : ‖x-w‖ < η)
    (hmargin : (Fintype.card ι : ℝ) * Real.exp (t * (η - ε)) ≤ 1)
    [Nonempty ι] : directionalBarrier u h ε t x < 1 := by
  have hdef : ∀ i, ⟪u i,x⟫_ℝ - h i ≤ ‖x-w‖ := by
    intro i
    have hi := real_inner_le_norm (u i) (x-w)
    rw [hu i, one_mul, inner_sub_right] at hi
    linarith [hw i]
  have hb := directionalBarrier_le u h ε t ‖x-w‖ x ht.le hdef
  have hc : (0 : ℝ) < Fintype.card ι := by exact_mod_cast Fintype.card_pos
  have hs : (Fintype.card ι : ℝ) * Real.exp (t * (‖x-w‖ - ε)) <
      (Fintype.card ι : ℝ) * Real.exp (t * (η - ε)) := by
    apply mul_lt_mul_of_pos_left _ hc
    apply Real.exp_lt_exp.mpr
    exact mul_lt_mul_of_pos_left (by linarith) ht
  exact (hb.trans_lt hs).trans_le hmargin
/-- Realize the directional construction in the generic CLM barrier API. -/
theorem directionalBarrier_eq_barrier (u : ι → E) (h : ι → ℝ) (ε t : ℝ) :
    directionalBarrier u h ε t =
      barrier (fun i => t • innerSL ℝ (u i)) (fun i => t * (h i + ε)) := by
  funext x
  simp only [directionalBarrier, barrier, ContinuousLinearMap.smul_apply, innerSL_apply,
    smul_eq_mul]
  congr 1
  funext i
  congr 1
  ring

/-- Smoothness in every finite order and at infinity. -/
theorem contDiff_directionalBarrier (u : ι → E) (h : ι → ℝ) (ε t : ℝ)
    {n : WithTop ℕ∞} : ContDiff ℝ n (directionalBarrier u h ε t) := by
  rw [directionalBarrier_eq_barrier]
  exact contDiff_barrier _ _

/-- Finite exponential sublevels are convex. -/
theorem convexOn_directionalBarrier (u : ι → E) (h : ι → ℝ) (ε t : ℝ) :
    ConvexOn ℝ Set.univ (directionalBarrier u h ε t) := by
  rw [directionalBarrier_eq_barrier]
  exact convexOn_barrier _ _

/-- Direction separation and nonzero scale imply strict convexity. -/
theorem strictConvexOn_directionalBarrier (u : ι → E) (h : ι → ℝ) (ε t : ℝ)
    (ht : t ≠ 0) (hsep : ∀ v : E, v ≠ 0 → ∃ i, ⟪u i,v⟫_ℝ ≠ 0) :
    StrictConvexOn ℝ Set.univ (directionalBarrier u h ε t) := by
  rw [directionalBarrier_eq_barrier]
  apply strictConvexOn_barrier
  intro v hv
  obtain ⟨i, hi⟩ := hsep v hv
  exact ⟨i, by simpa using mul_ne_zero ht hi⟩

/-- A supported point belongs to the open sublevel under the strict cardinal margin. -/
theorem directionalBarrier_lt_one_of_support (u : ι → E) (h : ι → ℝ) (ε t : ℝ)
    (x : E) (ht : 0 ≤ t) (hx : ∀ i, ⟪u i,x⟫_ℝ ≤ h i)
    (hmargin : (Fintype.card ι : ℝ) * Real.exp (-t * ε) < 1) :
    directionalBarrier u h ε t x < 1 := by
  have hb := directionalBarrier_le u h ε t 0 x ht (fun i => by linarith [hx i])
  have he : t * (0 - ε) = -t * ε := by ring
  rw [he] at hb
  exact hb.trans_lt hmargin

/-- The finite sum dominates a single exponential using directional positivity. -/
theorem exp_lower_directionalBarrier (u : ι → E) (h : ι → ℝ) (ε t c R : ℝ)
    (p x : E) (ht : 0 ≤ t)
    (hcover : ∀ y : E, ∃ i, c * ‖y‖ ≤ ⟪u i,y⟫_ℝ)
    (hsupport : ∀ i, h i - ⟪u i,p⟫_ℝ ≤ R) :
    Real.exp (t * (c * ‖x-p‖ - R - ε)) ≤ directionalBarrier u h ε t x := by
  obtain ⟨i, hi⟩ := hcover (x-p)
  have he : c * ‖x-p‖ - R - ε ≤ ⟪u i,x⟫_ℝ - h i - ε := by
    rw [inner_sub_right] at hi
    linarith [hsupport i]
  calc
    _ ≤ Real.exp (t * (⟪u i,x⟫_ℝ - h i - ε)) :=
      Real.exp_le_exp.mpr (mul_le_mul_of_nonneg_left he ht)
    _ ≤ directionalBarrier u h ε t x := by
      unfold directionalBarrier
      exact Finset.single_le_sum
        (fun j _ => (Real.exp_pos (t * (⟪u j,x⟫_ℝ - h j - ε))).le)
        (Finset.mem_univ i)

/-- An explicit radius for every real closed sublevel (the log argument is at least one). -/
theorem directionalBarrier_sublevel_radius (u : ι → E) (h : ι → ℝ) (ε t c R A : ℝ)
    (p x : E) (ht : 0 < t) (hc : 0 < c)
    (hcover : ∀ y : E, ∃ i, c * ‖y‖ ≤ ⟪u i,y⟫_ℝ)
    (hsupport : ∀ i, h i - ⟪u i,p⟫_ℝ ≤ R)
    (hx : directionalBarrier u h ε t x ≤ A) :
    ‖x-p‖ ≤ (R + ε + Real.log (max A 1) / t) / c := by
  have hex := (exp_lower_directionalBarrier u h ε t c R p x ht.le hcover hsupport).trans
    (hx.trans (le_max_left A 1))
  have hp : 0 < max A 1 := lt_of_lt_of_le zero_lt_one (le_max_right A 1)
  have he : t * (c * ‖x-p‖ - R - ε) ≤ Real.log (max A 1) := by
    apply Real.exp_le_exp.mp
    simpa [Real.exp_log hp] using hex
  apply (le_div_iff₀ hc).mpr
  have he' : c * ‖x-p‖ - R - ε ≤ Real.log (max A 1) / t := by
    apply (le_div_iff₀ ht).mpr
    nlinarith [he]
  nlinarith

/-- Positively covering directions make the barrier tend to infinity at infinity. -/
theorem tendsto_directionalBarrier_atTop (u : ι → E) (h : ι → ℝ) (ε t c R : ℝ)
    (p : E) (ht : 0 < t) (hc : 0 < c)
    (hcover : ∀ y : E, ∃ i, c * ‖y‖ ≤ ⟪u i,y⟫_ℝ)
    (hsupport : ∀ i, h i - ⟪u i,p⟫_ℝ ≤ R) :
    Filter.Tendsto (directionalBarrier u h ε t) (Bornology.cobounded E) Filter.atTop := by
  have hn : Filter.Tendsto (fun x : E => ‖x-p‖) (Bornology.cobounded E) Filter.atTop := by
    apply Filter.tendsto_atTop_mono (fun x => norm_sub_norm_le x p)
    simpa [sub_eq_add_neg] using
      Filter.tendsto_atTop_add_const_right (Bornology.cobounded E) (-‖p‖) (tendsto_norm_cobounded_atTop (E := E))
  have hl : Filter.Tendsto (fun x : E => c * ‖x-p‖ - R - ε)
      (Bornology.cobounded E) Filter.atTop := by
    convert Filter.tendsto_atTop_add_const_right (Bornology.cobounded E) (-R-ε) (hn.const_mul_atTop hc) using 1
    simp only [sub_eq_add_neg, add_assoc]
  exact Filter.tendsto_atTop_mono
    (fun x => exp_lower_directionalBarrier u h ε t c R p x ht.le hcover hsupport)
    (Real.tendsto_exp_atTop.comp (hl.const_mul_atTop ht))

/-- Every closed sublevel is compact in a proper ambient space. -/
theorem isCompact_directionalBarrier_sublevel [ProperSpace E]
    (u : ι → E) (h : ι → ℝ) (ε t c R A : ℝ) (p : E) (ht : 0 < t) (hc : 0 < c)
    (hcover : ∀ y : E, ∃ i, c * ‖y‖ ≤ ⟪u i,y⟫_ℝ)
    (hsupport : ∀ i, h i - ⟪u i,p⟫_ℝ ≤ R) :
    IsCompact {x : E | directionalBarrier u h ε t x ≤ A} := by
  apply Metric.isCompact_of_isClosed_isBounded
  · exact isClosed_le (contDiff_directionalBarrier u h ε t (n := 0)).continuous continuous_const
  · apply (Metric.isBounded_iff_subset_closedBall p).mpr
    refine ⟨(R + ε + Real.log (max A 1) / t) / c, ?_⟩
    intro x hx
    rw [Metric.mem_closedBall, dist_eq_norm]
    exact directionalBarrier_sublevel_radius u h ε t c R A p x ht hc hcover hsupport hx

/-- The strict cardinal margin is equivalent to the usual logarithmic scale bound. -/
theorem cardinal_margin_iff [Nonempty ι] (ε t : ℝ) :
    (Fintype.card ι : ℝ) * Real.exp (-t * ε) < 1 ↔
      Real.log (Fintype.card ι) < t * ε := by
  have hN : (0 : ℝ) < Fintype.card ι := by exact_mod_cast Fintype.card_pos
  have he : (Fintype.card ι : ℝ) * Real.exp (-t * ε) =
      Real.exp (Real.log (Fintype.card ι) - t * ε) := by
    rw [sub_eq_add_neg, Real.exp_add, Real.exp_log hN]
    congr 1
    ring_nf
  rw [he, Real.exp_lt_one_iff]
  constructor <;> intro hh <;> linarith

/-- The explicit inner-tube margin is positive under the strict cardinal condition. -/
theorem inner_margin_pos [Nonempty ι] {ε t : ℝ} (ht : 0 < t)
    (hmargin : (Fintype.card ι : ℝ) * Real.exp (-t * ε) < 1) :
    0 < ε - Real.log (Fintype.card ι) / t := by
  have h := (cardinal_margin_iff (ι := ι) ε t).mp hmargin
  have hd : Real.log (Fintype.card ι) / t < ε :=
    (div_lt_iff₀ ht).mpr (by simpa [mul_comm] using h)
  linarith

/-- The explicit tube radius exactly saturates the nonstrict exponential estimate. -/
theorem inner_margin_cardinal_eq [Nonempty ι] {ε t : ℝ} (ht : t ≠ 0) :
    (Fintype.card ι : ℝ) *
      Real.exp (t * ((ε - Real.log (Fintype.card ι) / t) - ε)) = 1 := by
  have hN : (0 : ℝ) < Fintype.card ι := by exact_mod_cast Fintype.card_pos
  have he : t * ((ε - Real.log (Fintype.card ι) / t) - ε) =
      -Real.log (Fintype.card ι) := by field_simp; ring
  rw [he, Real.exp_neg, Real.exp_log hN, mul_inv_cancel₀ hN.ne']

end ConvexApprox
