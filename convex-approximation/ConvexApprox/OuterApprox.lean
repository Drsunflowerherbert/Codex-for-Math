import ConvexApprox.Geometry
import ConvexApprox.Quantitative

/-!
# Quantitative outer approximation from finite support inequalities

For a nonempty compact convex set, a chordal net and independent nonnegative support
slack give the exact one-sided distance bound. The Hausdorff version additionally
requires inclusion of the original set. No ambient interior assumption is used.
-/

noncomputable section

namespace ConvexApprox

open scoped InnerProductSpace

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- The exact quantitative bound, separating support slack from net resolution. -/
def outerErrorBound (K : Set E) (δ ε : ℝ) : ℝ :=
  (ε + chordalSin δ * Metric.diam K) / chordalCos δ

omit [InnerProductSpace ℝ E] in
theorem outerErrorBound_nonneg {K : Set E} {δ ε : ℝ}
    (hδ₀ : 0 ≤ δ) (hδ : δ ^ 2 < 2) (hε : 0 ≤ ε) :
    0 ≤ outerErrorBound K δ ε := by
  exact div_nonneg (add_nonneg hε (mul_nonneg (chordalSin_nonneg hδ₀) Metric.diam_nonneg))
    (le_of_lt (chordalCos_pos hδ))

/-- Every point satisfying the finite support inequalities lies within the exact
error of the compact convex set. This includes lower-dimensional sets and singletons. -/
theorem infDist_le_outerErrorBound {K : Set E} {D : Finset E} {δ ε : ℝ}
    (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K)
    (hnet : IsChordalNet D δ) (hδ₀ : 0 ≤ δ) (hδ : δ ^ 2 < 2) (hε : 0 ≤ ε)
    {x : E} (hslack : ∀ u ∈ D, ⟪u, x⟫_ℝ ≤ supportValue K u + ε) :
    Metric.infDist x K ≤ outerErrorBound K δ ε := by
  obtain ⟨w, hw, heq, hnormal⟩ := nearest_point_normal hK hne hconv x
  rw [heq]
  by_cases hz : x - w = 0
  · simpa [hz] using outerErrorBound_nonneg (K := K) hδ₀ hδ hε
  have hr : 0 < ‖x - w‖ := norm_pos_iff.mpr hz
  let ν : E := ‖x - w‖⁻¹ • (x - w)
  have hν : ‖ν‖ = 1 := by
    simp [ν, norm_smul, ne_of_gt hr]
  obtain ⟨u, hu, huν⟩ := hnet.2 ν hν
  obtain ⟨v, hv, hsupport⟩ := exists_supportValue_eq hK hne u
  have hx : x - w = ‖x - w‖ • ν := by
    simp [ν, smul_smul, ne_of_gt hr]
  have hn : ⟪ν, v - w⟫_ℝ ≤ 0 := by
    dsimp [ν]
    rw [real_inner_smul_left]
    exact mul_nonpos_of_nonneg_of_nonpos (le_of_lt (inv_pos.mpr hr)) (hnormal v hv)
  have hL : ‖v - w‖ ≤ Metric.diam K := by
    simpa [dist_eq_norm] using Metric.dist_le_diam_of_mem hK.isBounded hv hw
  have hs : ⟪u, x⟫_ℝ ≤ ⟪u, v⟫_ℝ + ε := by
    simpa [hsupport] using hslack u hu
  exact local_outer_error (hnet.1 u hu) hν huν hδ hr.le hx hn hL hs

/-- Set-level inclusion in the closed metric tube with the exact error. -/
theorem outer_set_subset_tube {K C : Set E} {D : Finset E} {δ ε : ℝ}
    (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K)
    (hnet : IsChordalNet D δ) (hδ₀ : 0 ≤ δ) (hδ : δ ^ 2 < 2) (hε : 0 ≤ ε)
    (hslack : ∀ x ∈ C, ∀ u ∈ D, ⟪u, x⟫_ℝ ≤ supportValue K u + ε) :
    C ⊆ {x | Metric.infDist x K ≤ outerErrorBound K δ ε} := by
  intro x hx
  exact infDist_le_outerErrorBound hK hne hconv hnet hδ₀ hδ hε (hslack x hx)

/-- With inclusion of the original set, the same expression bounds the Hausdorff
error. The inclusion hypothesis is visible and cannot be inferred from arbitrary slack. -/
theorem hausdorffDist_le_outerErrorBound {K C : Set E} {D : Finset E} {δ ε : ℝ}
    (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K)
    (hnet : IsChordalNet D δ) (hδ₀ : 0 ≤ δ) (hδ : δ ^ 2 < 2) (hε : 0 ≤ ε)
    (hincl : K ⊆ C)
    (hslack : ∀ x ∈ C, ∀ u ∈ D, ⟪u, x⟫_ℝ ≤ supportValue K u + ε) :
    Metric.hausdorffDist C K ≤ outerErrorBound K δ ε := by
  apply Metric.hausdorffDist_le_of_infDist (outerErrorBound_nonneg hδ₀ hδ hε)
  · intro x hx
    exact infDist_le_outerErrorBound hK hne hconv hnet hδ₀ hδ hε (hslack x hx)
  · intro x hx
    rw [Metric.infDist_zero_of_mem (hincl hx)]
    exact outerErrorBound_nonneg hδ₀ hδ hε

omit [InnerProductSpace ℝ E] in
/-- The weaker numerator obtained by replacing the exact sine constant by δ. -/
theorem outerErrorBound_le_simple {K : Set E} {δ ε : ℝ}
    (hδ₀ : 0 ≤ δ) (hδ : δ ^ 2 < 2) :
    outerErrorBound K δ ε ≤ (ε + δ * Metric.diam K) / chordalCos δ := by
  apply div_le_div_of_nonneg_right _ (le_of_lt (chordalCos_pos hδ))
  exact add_le_add_left (mul_le_mul_of_nonneg_right (chordalSin_le hδ₀)
    Metric.diam_nonneg) ε

/-- The published exact formula with the chordal interval written as
`0 ≤ δ < sqrt 2`. -/
theorem infDist_le_exact_outer_error {K : Set E} {D : Finset E} {δ ε : ℝ}
    (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K)
    (hnet : IsChordalNet D δ) (hδ₀ : 0 ≤ δ) (hδ : δ < Real.sqrt 2) (hε : 0 ≤ ε)
    {x : E} (hslack : ∀ u ∈ D, ⟪u, x⟫_ℝ ≤ supportValue K u + ε) :
    Metric.infDist x K ≤
      (ε + δ * Real.sqrt (1 - δ ^ 2 / 4) * Metric.diam K) / (1 - δ ^ 2 / 2) := by
  simpa [outerErrorBound, chordalSin, chordalCos] using
    infDist_le_outerErrorBound hK hne hconv hnet hδ₀ (chordal_sq_lt_two hδ₀ hδ) hε hslack

/-- The exact Hausdorff formula for an outer set satisfying the finite support inequalities. -/
theorem hausdorffDist_le_exact_outer_error {K C : Set E} {D : Finset E} {δ ε : ℝ}
    (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K)
    (hnet : IsChordalNet D δ) (hδ₀ : 0 ≤ δ) (hδ : δ < Real.sqrt 2) (hε : 0 ≤ ε)
    (hincl : K ⊆ C)
    (hslack : ∀ x ∈ C, ∀ u ∈ D, ⟪u, x⟫_ℝ ≤ supportValue K u + ε) :
    Metric.hausdorffDist C K ≤
      (ε + δ * Real.sqrt (1 - δ ^ 2 / 4) * Metric.diam K) / (1 - δ ^ 2 / 2) := by
  simpa [outerErrorBound, chordalSin, chordalCos] using
    hausdorffDist_le_outerErrorBound hK hne hconv hnet hδ₀
      (chordal_sq_lt_two hδ₀ hδ) hε hincl hslack

/-- A singleton has zero diameter, so the geometric term vanishes exactly. -/
theorem singleton_norm_le_outer_error {D : Finset E} {δ ε : ℝ} (p : E)
    (hnet : IsChordalNet D δ) (hδ₀ : 0 ≤ δ) (hδ : δ ^ 2 < 2) (hε : 0 ≤ ε)
    {x : E} (hslack : ∀ u ∈ D, ⟪u, x⟫_ℝ ≤ ⟪u, p⟫_ℝ + ε) :
    ‖x - p‖ ≤ ε / chordalCos δ := by
  have hs : ∀ u ∈ D, ⟪u, x⟫_ℝ ≤ supportValue ({p} : Set E) u + ε := by
    intro u hu
    simpa [supportValue] using hslack u hu
  simpa [Metric.infDist_singleton, dist_eq_norm, outerErrorBound] using
    infDist_le_outerErrorBound isCompact_singleton (Set.singleton_nonempty p)
      (convex_singleton p) hnet hδ₀ hδ hε hs

end ConvexApprox
