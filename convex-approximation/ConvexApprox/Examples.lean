import ConvexApprox.Approximation

/-!
# Singleton and empty-interior segment examples

The examples use the same outer-error theorem as full-dimensional compact convex sets.
The planar segment is proved to have empty ambient interior.
-/

noncomputable section

namespace ConvexApprox.Examples

open scoped InnerProductSpace

abbrev Plane := EuclideanSpace ℝ (Fin 2)

/-- The horizontal unit direction in the Euclidean plane. -/
def horizontal : Plane := EuclideanSpace.single 0 1

/-- The vertical unit direction in the Euclidean plane. -/
def vertical : Plane := EuclideanSpace.single 1 1

/-- A nontrivial compact convex set with empty ambient interior. -/
def planarSegment : Set Plane := segment ℝ (0 : Plane) horizontal

theorem horizontal_norm : ‖horizontal‖ = 1 := by simp [horizontal]

theorem vertical_norm : ‖vertical‖ = 1 := by simp [vertical]

/-- Both signs of both coordinate directions, to be included in the finite net. -/
def planarAxes : Finset Plane := by
  classical
  exact {horizontal, -horizontal, vertical, -vertical}

theorem planarAxes_unit : ∀ u ∈ planarAxes, ‖u‖ = 1 := by
  classical
  intro u hu
  simp only [planarAxes, Finset.mem_insert, Finset.mem_singleton] at hu
  rcases hu with rfl | rfl | rfl | rfl <;> simp [horizontal, vertical]

/-- Actual finite nets exist containing both signs of both planar axes. -/
theorem exists_planarNet {δ : ℝ} (hδ : 0 < δ) :
    ∃ D : Finset Plane, planarAxes ⊆ D ∧ ConvexApprox.IsChordalNet D δ :=
  ConvexApprox.exists_chordalNet_containing planarAxes planarAxes_unit hδ

theorem planarSegment_nonempty : planarSegment.Nonempty :=
  ⟨0, left_mem_segment ℝ _ _⟩

theorem planarSegment_compact : IsCompact planarSegment := by
  rw [planarSegment, segment_eq_image_lineMap]
  exact isCompact_Icc.image AffineMap.lineMap_continuous

theorem planarSegment_convex : Convex ℝ planarSegment := convex_segment _ _

theorem planarSegment_eq_image :
    planarSegment = (fun a : ℝ => a • horizontal) '' Set.Icc 0 1 := by
  simp [planarSegment, segment_eq_image]

theorem horizontal_mem_planarSegment : horizontal ∈ planarSegment :=
  right_mem_segment ℝ _ _

theorem horizontal_ne_zero : horizontal ≠ (0 : Plane) := by
  intro h
  have hn := horizontal_norm
  rw [h, norm_zero] at hn
  norm_num at hn

theorem planarSegment_diam : Metric.diam planarSegment = 1 := by
  apply le_antisymm
  · apply Metric.diam_le_of_forall_dist_le (by norm_num)
    intro x hx y hy
    rw [planarSegment_eq_image] at hx hy
    obtain ⟨a, ha, rfl⟩ := hx
    obtain ⟨b, hb, rfl⟩ := hy
    rw [dist_eq_norm, ← sub_smul, norm_smul, horizontal_norm,
      Real.norm_eq_abs, mul_one]
    apply abs_le.mpr
    constructor <;> linarith [ha.1, ha.2, hb.1, hb.2]
  · have hdist := Metric.dist_le_diam_of_mem planarSegment_compact.isBounded
      (show (0 : Plane) ∈ planarSegment from left_mem_segment ℝ _ _)
      horizontal_mem_planarSegment
    simpa [dist_eq_norm, horizontal_norm] using hdist

/-- Every point of the segment has zero vertical coordinate. -/
theorem planarSegment_vertical_zero {z : Plane} (hz : z ∈ planarSegment) : z 1 = 0 := by
  obtain ⟨a, b, _, _, _, heq⟩ := hz
  rw [← heq]
  simp [horizontal, EuclideanSpace.single_apply]

/-- The line segment has empty interior in its two-dimensional ambient space. -/
theorem planarSegment_interior_empty : interior planarSegment = ∅ := by
  apply Set.eq_empty_iff_forall_notMem.mpr
  intro z hz
  have hz0 := planarSegment_vertical_zero (interior_subset hz)
  obtain ⟨r, hr, hball⟩ := Metric.mem_nhds_iff.mp (mem_interior_iff_mem_nhds.mp hz)
  let e : Plane := vertical
  have he : ‖e‖ = 1 := vertical_norm
  have hnear : z + (r / 2) • e ∈ Metric.ball z r := by
    rw [Metric.mem_ball, dist_eq_norm, add_sub_cancel_left, norm_smul, he,
      Real.norm_eq_abs, abs_of_pos (by linarith : 0 < r / 2), mul_one]
    linarith
  have hv := planarSegment_vertical_zero (hball hnear)
  have hcoord : (z + (r / 2) • e) 1 = r / 2 := by
    simp [e, vertical, EuclideanSpace.single_apply, hz0]
  rw [hcoord] at hv
  linarith

/-- Supplied finite support inequalities give the exact outer-error bound for a
segment despite its empty ambient interior. -/
theorem planarSegment_infDist_le_exact_outer_error {D : Finset Plane} {δ ε : ℝ}
    (hnet : ConvexApprox.IsChordalNet D δ) (hδ₀ : 0 ≤ δ)
    (hδ : δ < Real.sqrt 2) (hε : 0 ≤ ε) {x : Plane}
    (hslack : ∀ u ∈ D, ⟪u, x⟫_ℝ ≤ ConvexApprox.supportValue planarSegment u + ε) :
    Metric.infDist x planarSegment ≤
      (ε + δ * Real.sqrt (1 - δ ^ 2 / 4)) / (1 - δ ^ 2 / 2) := by
  simpa [planarSegment_diam] using
    ConvexApprox.infDist_le_exact_outer_error planarSegment_compact planarSegment_nonempty
      planarSegment_convex hnet hδ₀ hδ hε hslack

/-- The planar singleton example has no diameter term. -/
theorem planarSingleton_norm_le_outer_error {D : Finset Plane} {δ ε : ℝ} (p : Plane)
    (hnet : ConvexApprox.IsChordalNet D δ) (hδ₀ : 0 ≤ δ) (hδ : δ ^ 2 < 2)
    (hε : 0 ≤ ε) {x : Plane}
    (hslack : ∀ u ∈ D, ⟪u, x⟫_ℝ ≤ ⟪u, p⟫_ℝ + ε) :
    ‖x - p‖ ≤ ε / ConvexApprox.chordalCos δ :=
  ConvexApprox.singleton_norm_le_outer_error p hnet hδ₀ hδ hε hslack

/-- Every closed barrier sublevel of this empty-interior segment is compact. -/
theorem planarSegment_barrier_compact {D : Finset Plane} {δ ε t : ℝ}
    (hnet : ConvexApprox.IsChordalNet D δ) (hδ : δ ^ 2 < 2) (ht : 0 < t) (A : ℝ) :
    IsCompact {x : Plane | ConvexApprox.supportBarrier planarSegment D ε t x ≤ A} :=
  ConvexApprox.isCompact_supportBarrier_sublevel planarSegment_compact planarSegment_nonempty
    hnet hδ ht A

/-- The cardinal margin puts the line segment inside the open barrier sublevel. -/
theorem planarSegment_barrier_lt_one {D : Finset Plane} {ε t : ℝ} (ht : 0 ≤ t)
    (hmargin : (D.card : ℝ) * Real.exp (-t * ε) < 1) {x : Plane}
    (hx : x ∈ planarSegment) : ConvexApprox.supportBarrier planarSegment D ε t x < 1 :=
  ConvexApprox.supportBarrier_lt_one planarSegment_compact planarSegment_nonempty ht hmargin hx

/-- The actual segment barrier has the exact Hausdorff error with diameter one. -/
theorem planarSegment_barrier_hausdorff_error {D : Finset Plane} {δ ε t : ℝ}
    (hnet : ConvexApprox.IsChordalNet D δ) (hδ₀ : 0 ≤ δ) (hδ : δ < Real.sqrt 2)
    (hε : 0 ≤ ε) (ht : 0 < t)
    (hmargin : (D.card : ℝ) * Real.exp (-t * ε) < 1) :
    Metric.hausdorffDist
        {x : Plane | ConvexApprox.supportBarrier planarSegment D ε t x ≤ 1}
        planarSegment ≤
      (ε + δ * Real.sqrt (1 - δ ^ 2 / 4)) / (1 - δ ^ 2 / 2) := by
  simpa [planarSegment_diam] using
    ConvexApprox.supportBarrier_hausdorff_error planarSegment_compact planarSegment_nonempty
      planarSegment_convex hnet hδ₀ hδ hε ht hmargin

/-- The actual singleton barrier has the exact radius bound without a diameter term. -/
theorem planarSingleton_barrier_radius {D : Finset Plane} {δ ε t : ℝ} (p : Plane)
    (hnet : ConvexApprox.IsChordalNet D δ) (hδ₀ : 0 ≤ δ) (hδ : δ ^ 2 < 2)
    (hε : 0 ≤ ε) (ht : 0 < t) {x : Plane}
    (hx : ConvexApprox.supportBarrier ({p} : Set Plane) D ε t x ≤ 1) :
    ‖x - p‖ ≤ ε / ConvexApprox.chordalCos δ := by
  apply ConvexApprox.singleton_norm_le_outer_error p hnet hδ₀ hδ hε
  intro u hu
  simpa [ConvexApprox.supportValue] using
    ConvexApprox.supportBarrier_halfspace ({p} : Set Plane) D ε t ht hx hu

end ConvexApprox.Examples
