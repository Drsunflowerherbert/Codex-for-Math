import ConvexApprox.Sublevels
import ConvexApprox.OuterApprox

/-!
# Finite-direction smooth outer approximation

This module connects the compiled finite exponential barrier to attained supports of a
nonempty compact convex set. Ambient interior is never assumed. Analytic manifold or
sphere parametrization claims are outside the compiled scope.
-/

noncomputable section
open scoped BigOperators InnerProductSpace ContDiff
namespace ConvexApprox
variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- The support barrier with independent support slack and positive scale. -/
def supportBarrier (K : Set E) (D : Finset E) (ε t : ℝ) : E → ℝ :=
  directionalBarrier (fun u : {u // u ∈ D} => (u : E))
    (fun u => supportValue K (u : E)) ε t

/-- The usual finite-direction sum formula. -/
theorem supportBarrier_eq_sum (K : Set E) (D : Finset E) (ε t : ℝ) (x : E) :
    supportBarrier K D ε t x =
      ∑ u ∈ D, Real.exp (t * (⟪u,x⟫_ℝ - supportValue K u - ε)) := by
  exact Finset.sum_coe_sort D (fun u : E => Real.exp (t * (⟪u,x⟫_ℝ - supportValue K u - ε)))

/-- CLM representation imports derivative, Hessian and regular-level results. -/
theorem supportBarrier_eq_barrier (K : Set E) (D : Finset E) (ε t : ℝ) :
    supportBarrier K D ε t =
      barrier (fun u : {u // u ∈ D} => t • innerSL ℝ (u : E))
        (fun u => t * (supportValue K (u : E) + ε)) := by
  exact directionalBarrier_eq_barrier _ _ _ _

theorem contDiff_supportBarrier (K : Set E) (D : Finset E) (ε t : ℝ)
    {n : WithTop ℕ∞} : ContDiff ℝ n (supportBarrier K D ε t) :=
  contDiff_directionalBarrier _ _ _ _

theorem supportBarrier_halfspace (K : Set E) (D : Finset E) (ε t : ℝ)
    {x : E} (ht : 0 < t) (hx : supportBarrier K D ε t x ≤ 1)
    {u : E} (hu : u ∈ D) : ⟪u,x⟫_ℝ ≤ supportValue K u + ε :=
  directionalBarrier_halfspace _ _ _ _ x ht hx ⟨u,hu⟩

/-- Nonempty compact K lies strictly inside under the exact cardinal margin. -/
theorem supportBarrier_lt_one {K : Set E} {D : Finset E} {ε t : ℝ}
    (hK : IsCompact K) (hne : K.Nonempty) (ht : 0 ≤ t)
    (hmargin : (D.card : ℝ) * Real.exp (-t * ε) < 1) {x : E} (hx : x ∈ K) :
    supportBarrier K D ε t x < 1 := by
  apply directionalBarrier_lt_one_of_support (ι := {u // u ∈ D}) _ _ ε t x ht
    (fun u => inner_le_supportValue hK hne (u : E) hx)
  simpa using hmargin

/-- The positive net-cover bound, including the zero vector. -/
theorem net_positive_cover [Nontrivial E] {D : Finset E} {δ : ℝ}
    (hnet : IsChordalNet D δ) :
    ∀ y : E, ∃ u : {u // u ∈ D}, chordalCos δ * ‖y‖ ≤ ⟪(u : E),y⟫_ℝ := by
  intro y
  by_cases hy : y = 0
  · obtain ⟨u,hu⟩ := hnet.nonempty
    exact ⟨⟨u,hu⟩, by simp [hy]⟩
  · obtain ⟨u,hu,hge⟩ := hnet.exists_inner_ge_norm hy
    exact ⟨⟨u,hu⟩, hge⟩

/-- An attained support differs from an anchor by at most the diameter. -/
theorem supportValue_sub_inner_le_diam {K : Set E} (hK : IsCompact K) (hne : K.Nonempty)
    {p u : E} (hp : p ∈ K) (hu : ‖u‖ = 1) :
    supportValue K u - ⟪u,p⟫_ℝ ≤ Metric.diam K := by
  obtain ⟨v,hv,heq⟩ := exists_supportValue_eq hK hne u
  rw [heq, ← inner_sub_right]
  have hi := real_inner_le_norm u (v-p)
  rw [hu, one_mul] at hi
  exact hi.trans (by simpa [dist_eq_norm] using Metric.dist_le_diam_of_mem hK.isBounded hv hp)

/-- Exponential lower bound: a quantitative coercivity certificate. -/
theorem exp_lower_supportBarrier [Nontrivial E] {K : Set E} {D : Finset E}
    {δ ε t : ℝ} (hK : IsCompact K) (hne : K.Nonempty) (hnet : IsChordalNet D δ)
    (ht : 0 ≤ t) {p : E} (hp : p ∈ K) (x : E) :
    Real.exp (t * (chordalCos δ * ‖x-p‖ - Metric.diam K - ε)) ≤
      supportBarrier K D ε t x := by
  apply exp_lower_directionalBarrier _ _ _ _ _ _ p x ht (net_positive_cover hnet)
  intro u
  exact supportValue_sub_inner_le_diam hK hne hp (hnet.1 u u.property)

/-- All closed sublevels are compact; K may have empty ambient interior. -/
theorem isCompact_supportBarrier_sublevel [FiniteDimensional ℝ E] [Nontrivial E]
    {K : Set E} {D : Finset E} {δ ε t : ℝ} (hK : IsCompact K) (hne : K.Nonempty)
    (hnet : IsChordalNet D δ) (hδ : δ ^ 2 < 2) (ht : 0 < t) (A : ℝ) :
    IsCompact {x : E | supportBarrier K D ε t x ≤ A} := by
  obtain ⟨p,hp⟩ := hne
  have hne : K.Nonempty := ⟨p,hp⟩
  apply isCompact_directionalBarrier_sublevel _ _ ε t (chordalCos δ) (Metric.diam K)
    A p ht (chordalCos_pos hδ) (net_positive_cover hnet)
  intro u
  exact supportValue_sub_inner_le_diam hK hne hp (hnet.1 u u.property)

theorem tendsto_supportBarrier_atTop [Nontrivial E] {K : Set E} {D : Finset E}
    {δ ε t : ℝ} (hK : IsCompact K) (hne : K.Nonempty) (hnet : IsChordalNet D δ)
    (hδ : δ ^ 2 < 2) (ht : 0 < t) :
    Filter.Tendsto (supportBarrier K D ε t) (Bornology.cobounded E) Filter.atTop := by
  obtain ⟨p,hp⟩ := hne
  have hne : K.Nonempty := ⟨p,hp⟩
  apply tendsto_directionalBarrier_atTop _ _ ε t (chordalCos δ) (Metric.diam K)
    p ht (chordalCos_pos hδ) (net_positive_cover hnet)
  intro u
  exact supportValue_sub_inner_le_diam hK hne hp (hnet.1 u u.property)

/-- The explicit open inner tube follows from the exact positive margin. -/
theorem supportBarrier_inner_tube [Nontrivial E] {K : Set E} {D : Finset E}
    {δ ε t : ℝ} (hK : IsCompact K) (hne : K.Nonempty) (hnet : IsChordalNet D δ)
    (ht : 0 < t) {x : E}
    (hx : Metric.infDist x K < ε - Real.log (D.card : ℝ) / t) :
    supportBarrier K D ε t x < 1 := by
  obtain ⟨w,hw,hd⟩ := hK.exists_infDist_eq_dist hne x
  letI : Nonempty {u // u ∈ D} := by
    obtain ⟨u,hu⟩ := hnet.nonempty
    exact ⟨⟨u,hu⟩⟩
  apply directionalBarrier_tube (ι := {u // u ∈ D}) _ _ ε t (ε - Real.log (D.card : ℝ) / t) x w ht
    (fun u => hnet.1 u u.property)
    (fun u => inner_le_supportValue hK hne (u : E) hw)
  · simpa [hd, dist_eq_norm] using hx
  · simpa using (inner_margin_cardinal_eq (ι := {u // u ∈ D}) (ε := ε) ht.ne').le

/-- Strict convexity follows from a fine net and nonzero scale. -/
theorem strictConvexOn_supportBarrier {K : Set E} {D : Finset E} {δ ε t : ℝ}
    (hnet : IsChordalNet D δ) (hδ : δ ^ 2 < 2) (ht : t ≠ 0) :
    StrictConvexOn ℝ Set.univ (supportBarrier K D ε t) := by
  apply strictConvexOn_directionalBarrier (ι := {u // u ∈ D}) _ _ _ _ ht
  intro v hv
  obtain ⟨u,hu,hpos⟩ := hnet.exists_inner_pos hδ hv
  exact ⟨⟨u,hu⟩, hpos.ne'⟩

/-- The barrier closed sublevel has the exact one-sided quantitative error. -/
theorem supportBarrier_outer_error {K : Set E} {D : Finset E} {δ ε t : ℝ}
    (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K)
    (hnet : IsChordalNet D δ) (hδ₀ : 0 ≤ δ) (hδ : δ < Real.sqrt 2)
    (hε : 0 ≤ ε) (ht : 0 < t) {x : E} (hx : supportBarrier K D ε t x ≤ 1) :
    Metric.infDist x K ≤
      (ε + δ * Real.sqrt (1 - δ ^ 2 / 4) * Metric.diam K) / (1 - δ ^ 2 / 2) := by
  apply infDist_le_exact_outer_error hK hne hconv hnet hδ₀ hδ hε
  intro u hu
  exact supportBarrier_halfspace K D ε t ht hx hu

/-- The exact Hausdorff estimate includes the strict cardinal margin explicitly. -/
theorem supportBarrier_hausdorff_error {K : Set E} {D : Finset E} {δ ε t : ℝ}
    (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K)
    (hnet : IsChordalNet D δ) (hδ₀ : 0 ≤ δ) (hδ : δ < Real.sqrt 2)
    (hε : 0 ≤ ε) (ht : 0 < t) (hmargin : (D.card : ℝ) * Real.exp (-t * ε) < 1) :
    Metric.hausdorffDist {x : E | supportBarrier K D ε t x ≤ 1} K ≤
      (ε + δ * Real.sqrt (1 - δ ^ 2 / 4) * Metric.diam K) / (1 - δ ^ 2 / 2) := by
  apply hausdorffDist_le_exact_outer_error hK hne hconv hnet hδ₀ hδ hε
  · intro x hx
    exact (supportBarrier_lt_one hK hne ht.le hmargin hx).le
  · intro x hx u hu
    exact supportBarrier_halfspace K D ε t ht hx hu

/-- The closure of the open support sublevel is its closed sublevel. -/
theorem closure_supportBarrier_lt {K : Set E} {D : Finset E} {ε t : ℝ}
    (hK : IsCompact K) (hne : K.Nonempty) (ht : 0 ≤ t)
    (hmargin : (D.card : ℝ) * Real.exp (-t * ε) < 1) :
    closure {x : E | supportBarrier K D ε t x < 1} =
      {x : E | supportBarrier K D ε t x ≤ 1} := by
  obtain ⟨p,hp⟩ := hne
  have hne : K.Nonempty := ⟨p,hp⟩
  have ha := supportBarrier_lt_one hK hne ht hmargin hp
  rw [supportBarrier_eq_barrier] at ha ⊢
  exact closure_barrier_lt _ _ p 1 ha

theorem frontier_supportBarrier_lt {K : Set E} {D : Finset E} {ε t : ℝ}
    (hK : IsCompact K) (hne : K.Nonempty) (ht : 0 ≤ t)
    (hmargin : (D.card : ℝ) * Real.exp (-t * ε) < 1) :
    frontier {x : E | supportBarrier K D ε t x < 1} =
      {x : E | supportBarrier K D ε t x = 1} := by
  obtain ⟨p,hp⟩ := hne
  have hne : K.Nonempty := ⟨p,hp⟩
  have ha := supportBarrier_lt_one hK hne ht hmargin hp
  rw [supportBarrier_eq_barrier] at ha ⊢
  exact frontier_barrier_lt _ _ p 1 ha

/-- The actual Frechet derivative is nonzero at level one. -/
theorem fderiv_supportBarrier_ne_zero {K : Set E} {D : Finset E} {ε t : ℝ}
    (hK : IsCompact K) (hne : K.Nonempty) (ht : 0 ≤ t)
    (hmargin : (D.card : ℝ) * Real.exp (-t * ε) < 1)
    {x : E} (hx : supportBarrier K D ε t x = 1) :
    fderiv ℝ (supportBarrier K D ε t) x ≠ 0 := by
  obtain ⟨p,hp⟩ := hne
  have hne : K.Nonempty := ⟨p,hp⟩
  have ha := supportBarrier_lt_one hK hne ht hmargin hp
  rw [supportBarrier_eq_barrier] at ha hx ⊢
  rw [fderiv_barrier]
  exact barrierDeriv_ne_zero_of_level _ _ p x 1 ha hx

/-- An error bound below the preceding inner margin certifies one nesting step. -/
theorem supportBarrier_certified_nesting [Nontrivial E]
    {K : Set E} {D₁ D₂ : Finset E} {δ₁ δ₂ ε₁ ε₂ t₁ t₂ : ℝ}
    (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K)
    (hnet₁ : IsChordalNet D₁ δ₁) (hnet₂ : IsChordalNet D₂ δ₂)
    (hδ₂₀ : 0 ≤ δ₂) (hδ₂ : δ₂ ^ 2 < 2) (hε₂ : 0 ≤ ε₂)
    (ht₁ : 0 < t₁) (ht₂ : 0 < t₂)
    (hgap : outerErrorBound K δ₂ ε₂ < ε₁ - Real.log (D₁.card : ℝ) / t₁) :
    {x : E | supportBarrier K D₂ ε₂ t₂ x ≤ 1} ⊆
      {x : E | supportBarrier K D₁ ε₁ t₁ x < 1} := by
  intro x hx
  apply supportBarrier_inner_tube hK hne hnet₁ ht₁
  apply lt_of_le_of_lt _ hgap
  apply infDist_le_outerErrorBound hK hne hconv hnet₂ hδ₂₀ hδ₂ hε₂
  intro u hu
  exact supportBarrier_halfspace K D₂ ε₂ t₂ ht₂ hx hu

/-- The actual second derivative is positive on each nonzero vector. This is pointwise,
not a claim of a globally uniform strong-convexity modulus. -/
theorem supportBarrier_hessian_pos {K : Set E} {D : Finset E} {δ ε t : ℝ}
    (hnet : IsChordalNet D δ) (hδ : δ ^ 2 < 2) (ht : t ≠ 0)
    (x v : E) (hv : v ≠ 0) :
    0 < (fderiv ℝ (fun z => fderiv ℝ (supportBarrier K D ε t) z) x) v v := by
  rw [supportBarrier_eq_barrier, fderiv_fderiv_barrier]
  apply barrierHessian_pos _ _ _ x v hv
  intro y hy
  obtain ⟨u,hu,hpos⟩ := hnet.exists_inner_pos hδ hy
  exact ⟨⟨u,hu⟩, by simpa using mul_ne_zero ht hpos.ne'⟩

/-- Main reusable smooth outer-approximation certificate with all geometric and
scale hypotheses visible. It covers singletons and lower-dimensional convex sets. -/
theorem supportBarrier_outer_approximation [FiniteDimensional ℝ E] [Nontrivial E]
    {K : Set E} {D : Finset E} {δ ε t : ℝ}
    (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K)
    (hnet : IsChordalNet D δ) (hδ₀ : 0 ≤ δ) (hδ : δ < Real.sqrt 2)
    (hε : 0 < ε) (ht : 0 < t) (hmargin : (D.card : ℝ) * Real.exp (-t * ε) < 1) :
    ContDiff ℝ ∞ (supportBarrier K D ε t) ∧
    StrictConvexOn ℝ Set.univ (supportBarrier K D ε t) ∧
    IsOpen {x : E | supportBarrier K D ε t x < 1} ∧
    K ⊆ {x : E | supportBarrier K D ε t x < 1} ∧
    IsCompact {x : E | supportBarrier K D ε t x ≤ 1} ∧
    closure {x : E | supportBarrier K D ε t x < 1} =
      {x : E | supportBarrier K D ε t x ≤ 1} ∧
    frontier {x : E | supportBarrier K D ε t x < 1} =
      {x : E | supportBarrier K D ε t x = 1} ∧
    (∀ x : E, supportBarrier K D ε t x = 1 →
      fderiv ℝ (supportBarrier K D ε t) x ≠ 0) ∧
    Metric.hausdorffDist {x : E | supportBarrier K D ε t x ≤ 1} K ≤
      (ε + δ * Real.sqrt (1 - δ ^ 2 / 4) * Metric.diam K) / (1 - δ ^ 2 / 2) := by
  have hs := chordal_sq_lt_two hδ₀ hδ
  refine ⟨contDiff_supportBarrier _ _ _ _, strictConvexOn_supportBarrier hnet hs ht.ne',
    isOpen_lt (contDiff_supportBarrier K D ε t (n := 0)).continuous continuous_const,
    ?_, isCompact_supportBarrier_sublevel hK hne hnet hs ht 1,
    closure_supportBarrier_lt hK hne ht.le hmargin,
    frontier_supportBarrier_lt hK hne ht.le hmargin, ?_,
    supportBarrier_hausdorff_error hK hne hconv hnet hδ₀ hδ hε.le ht hmargin⟩
  · intro x hx
    exact supportBarrier_lt_one hK hne ht.le hmargin hx
  · intro x hx
    exact fderiv_supportBarrier_ne_zero hK hne ht.le hmargin hx

/-- Every open chord of the closed sublevel lies in the open sublevel. -/
theorem supportBarrier_open_chord {K : Set E} {D : Finset E} {δ ε t : ℝ}
    (hnet : IsChordalNet D δ) (hδ : δ ^ 2 < 2) (ht : t ≠ 0)
    {x y : E} (hx : supportBarrier K D ε t x ≤ 1)
    (hy : supportBarrier K D ε t y ≤ 1) (hxy : x ≠ y)
    {a b : ℝ} (ha : 0 < a) (hb : 0 < b) (hab : a + b = 1) :
    supportBarrier K D ε t (a • x + b • y) < 1 := by
  have hi := (strictConvexOn_supportBarrier (K := K) (ε := ε) hnet hδ ht).2
    (Set.mem_univ x) (Set.mem_univ y) hxy ha hb hab
  simp only [smul_eq_mul] at hi
  have hax := mul_le_mul_of_nonneg_left hx ha.le
  have hby := mul_le_mul_of_nonneg_left hy hb.le
  linarith

/-- A fine net makes the closed support sublevel strictly convex as a set. -/
theorem strictConvex_supportBarrier_closed {K : Set E} {D : Finset E} {δ ε t : ℝ}
    (hnet : IsChordalNet D δ) (hδ : δ ^ 2 < 2) (ht : t ≠ 0) :
    StrictConvex ℝ {x : E | supportBarrier K D ε t x ≤ 1} := by
  have hopen : IsOpen {x : E | supportBarrier K D ε t x < 1} :=
    isOpen_lt (contDiff_supportBarrier K D ε t (n := 0)).continuous continuous_const
  have hsub : {x : E | supportBarrier K D ε t x < 1} ⊆
      interior {x : E | supportBarrier K D ε t x ≤ 1} :=
    interior_maximal (fun _ hx => (show supportBarrier K D ε t _ < 1 from hx).le) hopen
  intro x hx y hy hxy a b ha hb hab
  apply hsub
  exact supportBarrier_open_chord hnet hδ ht hx hy hxy ha hb hab

/-- The open sublevel is convex. -/
theorem convex_supportBarrier_open (K : Set E) (D : Finset E) (ε t : ℝ) :
    Convex ℝ {x : E | supportBarrier K D ε t x < 1} := by
  simpa using (convexOn_directionalBarrier
    (fun u : {u // u ∈ D} => (u : E))
    (fun u => supportValue K (u : E)) ε t).convex_lt 1

end ConvexApprox
