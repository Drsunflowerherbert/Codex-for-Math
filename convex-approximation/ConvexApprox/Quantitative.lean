import Mathlib

/-!
# Exact quantitative directional error

The lemmas in this file formalize the elementary inner-product estimates in
Section 5 of the reviewed convex-approximation study.  They keep geometric
support slack independent of the chordal resolution of the direction net.
-/

noncomputable section

namespace ConvexApprox

open scoped InnerProductSpace

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- The exact cosine constant associated with a chordal resolution. -/
def chordalCos (δ : ℝ) : ℝ := 1 - δ ^ 2 / 2

/-- The tangential error constant associated with a chordal resolution. -/
def chordalSin (δ : ℝ) : ℝ := δ * Real.sqrt (1 - δ ^ 2 / 4)

theorem chordalCos_pos {δ : ℝ} (hδ : δ ^ 2 < 2) : 0 < chordalCos δ := by
  unfold chordalCos
  linarith

theorem chordal_sq_lt_two {δ : ℝ} (hδ₀ : 0 ≤ δ) (hδ : δ < Real.sqrt 2) :
    δ ^ 2 < 2 := by
  have hs : (Real.sqrt 2) ^ 2 = (2 : ℝ) := Real.sq_sqrt (by norm_num)
  nlinarith [Real.sqrt_nonneg (2 : ℝ)]

/-- Chordal distance between unit vectors determines their inner product. -/
theorem unit_inner_eq_one_sub_half_sq {u v : E} (hu : ‖u‖ = 1) (hv : ‖v‖ = 1) :
    ⟪u, v⟫_ℝ = 1 - ‖u - v‖ ^ 2 / 2 := by
  have h := norm_sub_sq_real u v
  rw [hu, hv] at h
  nlinarith

/-- The exact positive direction constant supplied by a chordal net. -/
theorem chordalCos_le_inner {u v : E} {δ : ℝ}
    (hu : ‖u‖ = 1) (hv : ‖v‖ = 1) (huv : ‖u - v‖ ≤ δ) :
    chordalCos δ ≤ ⟪u, v⟫_ℝ := by
  have hδ₀ : 0 ≤ δ := (norm_nonneg _).trans huv
  rw [unit_inner_eq_one_sub_half_sq hu hv]
  unfold chordalCos
  nlinarith [norm_nonneg (u - v)]

/-- The squared norm of the tangential component of a unit direction. -/
theorem unit_tangent_norm_sq {u v : E} (hu : ‖u‖ = 1) (hv : ‖v‖ = 1) :
    ‖u - ⟪u, v⟫_ℝ • v‖ ^ 2 = 1 - ⟪u, v⟫_ℝ ^ 2 := by
  rw [norm_sub_sq_real, hu, norm_smul, hv, Real.norm_eq_abs,
    real_inner_smul_right]
  nlinarith [sq_abs ⟪u, v⟫_ℝ]

theorem chordalSin_nonneg {δ : ℝ} (hδ : 0 ≤ δ) : 0 ≤ chordalSin δ := by
  exact mul_nonneg hδ (Real.sqrt_nonneg _)

theorem chordalSin_sq {δ : ℝ} (hδ : δ ^ 2 ≤ 4) :
    chordalSin δ ^ 2 = 1 - chordalCos δ ^ 2 := by
  have hs : (Real.sqrt (1 - δ ^ 2 / 4)) ^ 2 = 1 - δ ^ 2 / 4 :=
    Real.sq_sqrt (by linarith)
  unfold chordalSin chordalCos
  rw [mul_pow, hs]
  ring

/-- The tangential part is bounded by the exact chordal sine constant. -/
theorem unit_tangent_norm_le_chordalSin {u v : E} {δ : ℝ}
    (hu : ‖u‖ = 1) (hv : ‖v‖ = 1) (huv : ‖u - v‖ ≤ δ) (hδ : δ ^ 2 < 2) :
    ‖u - ⟪u, v⟫_ℝ • v‖ ≤ chordalSin δ := by
  have hδ₀ : 0 ≤ δ := (norm_nonneg _).trans huv
  have hc := chordalCos_pos hδ
  have ha := chordalCos_le_inner hu hv huv
  have hn := norm_nonneg (u - ⟪u, v⟫_ℝ • v)
  have hs := chordalSin_nonneg hδ₀
  have ht := unit_tangent_norm_sq hu hv
  have hss := chordalSin_sq (δ := δ) (by linarith)
  nlinarith

/-- The exact tangential constant is at most the chordal resolution. -/
theorem chordalSin_le {δ : ℝ} (hδ : 0 ≤ δ) : chordalSin δ ≤ δ := by
  have hs : Real.sqrt (1 - δ ^ 2 / 4) ≤ 1 :=
    Real.sqrt_le_one.mpr (by nlinarith [sq_nonneg δ])
  simpa [chordalSin] using mul_le_mul_of_nonneg_left hs hδ

/-- The support displacement has only a tangential contribution: the normal
component is nonpositive, and its coefficient is positive. -/
theorem support_displacement_le_chordalSin {u ν v w : E} {δ L : ℝ}
    (hu : ‖u‖ = 1) (hν : ‖ν‖ = 1) (huν : ‖u - ν‖ ≤ δ)
    (hδ : δ ^ 2 < 2) (hnormal : ⟪ν, v - w⟫_ℝ ≤ 0) (hL : ‖v - w‖ ≤ L) :
    ⟪u, v - w⟫_ℝ ≤ chordalSin δ * L := by
  have hδ₀ : 0 ≤ δ := (norm_nonneg _).trans huν
  have ha : 0 ≤ ⟪u, ν⟫_ℝ :=
    (le_of_lt (chordalCos_pos hδ)).trans (chordalCos_le_inner hu hν huν)
  have hnormal' : ⟪u, ν⟫_ℝ * ⟪ν, v - w⟫_ℝ ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos ha hnormal
  have hsplit : ⟪u - ⟪u, ν⟫_ℝ • ν, v - w⟫_ℝ =
      ⟪u, v - w⟫_ℝ - ⟪u, ν⟫_ℝ * ⟪ν, v - w⟫_ℝ := by
    rw [inner_sub_left, real_inner_smul_left]
  have hCS := real_inner_le_norm (u - ⟪u, ν⟫_ℝ • ν) (v - w)
  have hmul : ‖u - ⟪u, ν⟫_ℝ • ν‖ * ‖v - w‖ ≤ chordalSin δ * L := by
    calc
      _ ≤ chordalSin δ * ‖v - w‖ :=
        mul_le_mul_of_nonneg_right (unit_tangent_norm_le_chordalSin hu hν huν hδ)
          (norm_nonneg _)
      _ ≤ _ := mul_le_mul_of_nonneg_left hL (chordalSin_nonneg hδ₀)
  linarith

/-- Exact local outer error, with independent support slack and chordal
resolution. The point displacement is a nonnegative multiple of the unit
normal. No interior or full-dimensional assumption is needed. -/
theorem local_outer_error {u ν x v w : E} {δ ε L r : ℝ}
    (hu : ‖u‖ = 1) (hν : ‖ν‖ = 1) (huν : ‖u - ν‖ ≤ δ)
    (hδ : δ ^ 2 < 2) (hr : 0 ≤ r) (hx : x - w = r • ν)
    (hnormal : ⟪ν, v - w⟫_ℝ ≤ 0) (hL : ‖v - w‖ ≤ L)
    (hslack : ⟪u, x⟫_ℝ ≤ ⟪u, v⟫_ℝ + ε) :
    r ≤ (ε + chordalSin δ * L) / chordalCos δ := by
  have hc := chordalCos_pos hδ
  have ha := chordalCos_le_inner hu hν huν
  have hcr : chordalCos δ * r ≤ ⟪u, ν⟫_ℝ * r :=
    mul_le_mul_of_nonneg_right ha hr
  have hsupport := support_displacement_le_chordalSin hu hν huν hδ hnormal hL
  have hslack' : ⟪u, x - w⟫_ℝ ≤ ⟪u, v - w⟫_ℝ + ε := by
    simp only [inner_sub_right]
    linarith
  have hxinner : ⟪u, x - w⟫_ℝ = r * ⟪u, ν⟫_ℝ := by
    rw [hx, real_inner_smul_right]
  apply (le_div_iff₀ hc).mpr
  nlinarith

end ConvexApprox
