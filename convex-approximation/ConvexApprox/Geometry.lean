import Mathlib

/-!
# Compact support and finite chordal direction nets

These facts use no interior assumption on the compact convex set.  Finite-dimensionality
is needed only to construct a finite net of the unit sphere; the support and nearest-point
lemmas apply in any real inner-product space.
-/

namespace ConvexApprox

open scoped InnerProductSpace

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Unit directions forming a finite net in Euclidean (chordal) distance. -/
def IsChordalNet (D : Finset E) (δ : ℝ) : Prop :=
  (∀ u ∈ D, ‖u‖ = 1) ∧ ∀ v : E, ‖v‖ = 1 → ∃ u ∈ D, ‖u - v‖ ≤ δ

/-- Support value, used below only with the explicit compactness and nonemptiness hypotheses. -/
noncomputable def supportValue (K : Set E) (u : E) : ℝ :=
  sSup ((fun v : E => ⟪u, v⟫_ℝ) '' K)

/-- Every linear support functional attains its maximum on a nonempty compact set. -/
theorem exists_support_maximizer {K : Set E} (hK : IsCompact K) (hne : K.Nonempty)
    (u : E) : ∃ v ∈ K, ∀ w ∈ K, ⟪u, w⟫_ℝ ≤ ⟪u, v⟫_ℝ := by
  exact hK.exists_isMaxOn hne
    (show Continuous (fun w : E => ⟪u, w⟫_ℝ) from by fun_prop).continuousOn

theorem exists_supportValue_eq {K : Set E} (hK : IsCompact K) (hne : K.Nonempty)
    (u : E) : ∃ v ∈ K, supportValue K u = ⟪u, v⟫_ℝ := by
  obtain ⟨v, hv, hmax⟩ := exists_support_maximizer hK hne u
  refine ⟨v, hv, ?_⟩
  exact (show IsGreatest ((fun w : E => ⟪u, w⟫_ℝ) '' K) ⟪u, v⟫_ℝ from
    ⟨⟨v, hv, rfl⟩, by rintro _ ⟨w, hw, rfl⟩; exact hmax w hw⟩).csSup_eq

theorem inner_le_supportValue {K : Set E} (hK : IsCompact K) (hne : K.Nonempty)
    (u : E) {v : E} (hv : v ∈ K) : ⟪u, v⟫_ℝ ≤ supportValue K u := by
  obtain ⟨w, hw, hmax⟩ := exists_support_maximizer hK hne u
  have heq : supportValue K u = ⟪u, w⟫_ℝ :=
    (show IsGreatest ((fun v : E => ⟪u, v⟫_ℝ) '' K) ⟪u, w⟫_ℝ from
      ⟨⟨w, hw, rfl⟩, by rintro _ ⟨v, hv, rfl⟩; exact hmax v hv⟩).csSup_eq
  rw [heq]
  exact hmax v hv

/-- A compact convex set has a nearest point whose residual is a supporting normal. -/
theorem nearest_point_normal {K : Set E} (hK : IsCompact K) (hne : K.Nonempty)
    (hconv : Convex ℝ K) (x : E) :
    ∃ w ∈ K, Metric.infDist x K = ‖x - w‖ ∧
      ∀ v ∈ K, ⟪x - w, v - w⟫_ℝ ≤ 0 := by
  obtain ⟨w, hw, heq⟩ := hK.exists_infDist_eq_dist hne x
  have heq' : Metric.infDist x K = ‖x - w‖ := by simpa [dist_eq_norm] using heq
  refine ⟨w, hw, heq', ?_⟩
  apply (norm_eq_iInf_iff_real_inner_le_zero hconv hw).mp
  simpa [Metric.infDist_eq_iInf, dist_eq_norm] using heq'.symm

/-- A finite chordal net can contain any prescribed finite family of unit directions. -/
theorem exists_chordalNet_containing [FiniteDimensional ℝ E] (A : Finset E)
    (hA : ∀ u ∈ A, ‖u‖ = 1) {δ : ℝ} (hδ : 0 < δ) :
    ∃ D : Finset E, A ⊆ D ∧ IsChordalNet D δ := by
  classical
  obtain ⟨S, hS, hfinite, hcover⟩ :=
    (isCompact_sphere (0 : E) (1 : ℝ)).finite_cover_balls hδ
  refine ⟨A ∪ hfinite.toFinset, Finset.subset_union_left, ?_, ?_⟩
  · intro u hu
    rcases Finset.mem_union.mp hu with hu | hu
    · exact hA u hu
    · simpa [Metric.mem_sphere, dist_eq_norm] using hS (hfinite.mem_toFinset.mp hu)
  · intro v hv
    have hvs : v ∈ Metric.sphere (0 : E) 1 := by simpa [Metric.mem_sphere, dist_eq_norm]
    obtain ⟨u, hu, hdist⟩ := Set.mem_iUnion₂.mp (hcover hvs)
    refine ⟨u, Finset.mem_union_right _ (hfinite.mem_toFinset.mpr hu), ?_⟩
    have hd : dist v u < δ := hdist
    simpa [dist_eq_norm, norm_sub_rev] using hd.le

/-- The exact positive-direction constant associated with a chordal net. -/
theorem IsChordalNet.exists_inner_ge {D : Finset E} {δ : ℝ} (hD : IsChordalNet D δ)
    {v : E} (hv : ‖v‖ = 1) : ∃ u ∈ D, 1 - δ ^ 2 / 2 ≤ ⟪u, v⟫_ℝ := by
  obtain ⟨u, hu, huv⟩ := hD.2 v hv
  refine ⟨u, hu, ?_⟩
  have heq := norm_sub_sq_real u v
  rw [hD.1 u hu, hv] at heq
  have hδ : 0 ≤ δ := (norm_nonneg _).trans huv
  nlinarith [norm_nonneg (u - v)]

/-- Scaling the unit-direction bound gives a quantitative positive spanning bound. -/
theorem IsChordalNet.exists_inner_ge_norm {D : Finset E} {δ : ℝ}
    (hD : IsChordalNet D δ) {v : E} (hv : v ≠ 0) :
    ∃ u ∈ D, (1 - δ ^ 2 / 2) * ‖v‖ ≤ ⟪u, v⟫_ℝ := by
  have hn : 0 < ‖v‖ := norm_pos_iff.mpr hv
  have hunit : ‖‖v‖⁻¹ • v‖ = 1 := by
    rw [norm_smul, Real.norm_eq_abs, abs_of_pos (inv_pos.mpr hn), inv_mul_cancel₀ hn.ne']
  obtain ⟨u, hu, hge⟩ := hD.exists_inner_ge hunit
  refine ⟨u, hu, ?_⟩
  rw [real_inner_smul_right] at hge
  have hmul := mul_le_mul_of_nonneg_left hge hn.le
  calc
    (1 - δ ^ 2 / 2) * ‖v‖ = ‖v‖ * (1 - δ ^ 2 / 2) := mul_comm _ _
    _ ≤ ‖v‖ * (‖v‖⁻¹ * ⟪u, v⟫_ℝ) := hmul
    _ = ⟪u, v⟫_ℝ := by rw [← mul_assoc, mul_inv_cancel₀ hn.ne', one_mul]

/-- A fine chordal net detects each nonzero vector by a strictly positive inner product. -/
theorem IsChordalNet.exists_inner_pos {D : Finset E} {δ : ℝ} (hD : IsChordalNet D δ)
    (hδ : δ ^ 2 < 2) {v : E} (hv : v ≠ 0) : ∃ u ∈ D, 0 < ⟪u, v⟫_ℝ := by
  obtain ⟨u, hu, hge⟩ := hD.exists_inner_ge_norm hv
  refine ⟨u, hu, ?_⟩
  have hc : 0 < 1 - δ ^ 2 / 2 := by linarith
  exact (mul_pos hc (norm_pos_iff.mpr hv)).trans_le hge

/-- The finite directions separate points as linear functionals. -/
theorem IsChordalNet.separates_points {D : Finset E} {δ : ℝ} (hD : IsChordalNet D δ)
    (hδ : δ ^ 2 < 2) {x y : E} (hxy : x ≠ y) :
    ∃ u ∈ D, ⟪u, x⟫_ℝ ≠ ⟪u, y⟫_ℝ := by
  obtain ⟨u, hu, hpos⟩ := hD.exists_inner_pos hδ (sub_ne_zero.mpr hxy)
  refine ⟨u, hu, ?_⟩
  rw [inner_sub_right] at hpos
  exact ne_of_gt (sub_pos.mp hpos)

/-- A vector orthogonal to all directions in a fine net is zero. -/
theorem IsChordalNet.eq_zero_of_inner_eq_zero {D : Finset E} {δ : ℝ}
    (hD : IsChordalNet D δ) (hδ : δ ^ 2 < 2) {v : E}
    (hv : ∀ u ∈ D, ⟪u, v⟫_ℝ = 0) : v = 0 := by
  by_contra hne
  obtain ⟨u, hu, hp⟩ := hD.exists_inner_pos hδ hne
  rw [hv u hu] at hp
  exact lt_irrefl _ hp

/-- In positive dimension the unit-sphere net is nonempty. -/
theorem IsChordalNet.nonempty [Nontrivial E] {D : Finset E} {δ : ℝ}
    (hD : IsChordalNet D δ) : D.Nonempty := by
  obtain ⟨v, hv⟩ := exists_ne (0 : E)
  have hn : 0 < ‖v‖ := norm_pos_iff.mpr hv
  have hunit : ‖‖v‖⁻¹ • v‖ = 1 := by
    rw [norm_smul, Real.norm_eq_abs, abs_of_pos (inv_pos.mpr hn), inv_mul_cancel₀ hn.ne']
  obtain ⟨u, hu, _⟩ := hD.2 _ hunit
  exact ⟨u, hu⟩

/-- A fine net in positive dimension has at least two directions. -/
theorem IsChordalNet.two_le_card [Nontrivial E] {D : Finset E} {δ : ℝ}
    (hD : IsChordalNet D δ) (hδ : δ ^ 2 < 2) : 2 ≤ D.card := by
  classical
  obtain ⟨u, hu⟩ := hD.nonempty
  have hu0 : u ≠ 0 := by intro h; simpa [h] using hD.1 u hu
  obtain ⟨v, hv, hpos⟩ := hD.exists_inner_pos hδ (neg_ne_zero.mpr hu0)
  have huv : u ≠ v := by
    intro h
    subst v
    rw [inner_neg_right, real_inner_self_eq_norm_sq, hD.1 u hu] at hpos
    norm_num at hpos
  have hins : {u, v} ⊆ D := by
    intro z hz
    simp only [Finset.mem_insert, Finset.mem_singleton] at hz
    rcases hz with rfl | rfl
    · exact hu
    · exact hv
  have hcard := Finset.card_le_card hins
  simpa [huv] using hcard

/-- Fine finite chordal nets span the whole ambient finite-dimensional space. -/
theorem IsChordalNet.span_eq_top [FiniteDimensional ℝ E] {D : Finset E} {δ : ℝ}
    (hD : IsChordalNet D δ) (hδ : δ ^ 2 < 2) : Submodule.span ℝ (D : Set E) = ⊤ := by
  apply (Submodule.orthogonal_eq_bot_iff).mp
  apply le_antisymm
  · intro v hv
    change v = 0
    apply hD.eq_zero_of_inner_eq_zero hδ
    intro u hu
    exact Submodule.inner_right_of_mem_orthogonal
      (Submodule.subset_span (show u ∈ (D : Set E) from hu)) hv
  · exact bot_le

end ConvexApprox
