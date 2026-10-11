import ConvexApprox.Approximation
import ConvexApprox.Construction

/-!
# Certified nested finite-direction approximations

The next error is selected below the preceding inner-tube margin. Parameter decay
alone is not used as an inclusion proof. This construction has no manifold claims.
-/

noncomputable section
open scoped ContDiff
namespace ConvexApprox
variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- All hypotheses for one finite-direction support barrier, with positive resolution. -/
structure BarrierData (K : Set E) where
  directions : Finset E
  resolution : ℝ
  slack : ℝ
  scale : ℝ
  net : IsChordalNet directions resolution
  resolution_pos : 0 < resolution
  resolution_lt : resolution < Real.sqrt 2
  slack_pos : 0 < slack
  scale_pos : 0 < scale
  cardinal_margin : (directions.card : ℝ) * Real.exp (-scale * slack) < 1

def BarrierData.error {K : Set E} (P : BarrierData K) : ℝ :=
  outerErrorBound K P.resolution P.slack

def BarrierData.tubeMargin {K : Set E} (P : BarrierData K) : ℝ :=
  P.slack - Real.log (P.directions.card : ℝ) / P.scale

def BarrierData.openSet {K : Set E} (P : BarrierData K) : Set E :=
  {x | supportBarrier K P.directions P.slack P.scale x < 1}

def BarrierData.closedSet {K : Set E} (P : BarrierData K) : Set E :=
  {x | supportBarrier K P.directions P.slack P.scale x ≤ 1}

omit [InnerProductSpace ℝ E] in
theorem BarrierData.error_nonneg {K : Set E} (P : BarrierData K) : 0 ≤ P.error :=
  outerErrorBound_nonneg P.resolution_pos.le
    (chordal_sq_lt_two P.resolution_pos.le P.resolution_lt) P.slack_pos.le

theorem BarrierData.tubeMargin_pos [Nontrivial E] {K : Set E} (P : BarrierData K) :
    0 < P.tubeMargin := by
  letI : Nonempty {u // u ∈ P.directions} := by
    obtain ⟨u,hu⟩ := P.net.nonempty
    exact ⟨⟨u,hu⟩⟩
  simpa [BarrierData.tubeMargin] using
    (inner_margin_pos (ι := {u // u ∈ P.directions}) (ε := P.slack) P.scale_pos
      (by simpa using P.cardinal_margin))

theorem exists_barrierData_error_lt [FiniteDimensional ℝ E] [Nontrivial E]
    (K : Set E) {ρ : ℝ} (hρ : 0 < ρ) : ∃ P : BarrierData K, P.error < ρ := by
  obtain ⟨D,δ,ε,t,_hA,hnet,hδ,hδlt,hε,ht,hmargin,herr⟩ :=
    exists_outer_parameters_containing K ∅ (by simp) hρ
  exact ⟨⟨D,δ,ε,t,hnet,hδ,hδlt,hε,ht,hmargin⟩, herr⟩

def chosenBarrierData [FiniteDimensional ℝ E] [Nontrivial E]
    (K : Set E) (ρ : ℝ) (hρ : 0 < ρ) : BarrierData K :=
  Classical.choose (exists_barrierData_error_lt K hρ)

theorem chosenBarrierData_error_lt [FiniteDimensional ℝ E] [Nontrivial E]
    (K : Set E) (ρ : ℝ) (hρ : 0 < ρ) : (chosenBarrierData K ρ hρ).error < ρ :=
  Classical.choose_spec (exists_barrierData_error_lt K hρ)

/-- Select each new barrier below half the preceding tube margin and a vanishing target. -/
def nestedBarrierData [FiniteDimensional ℝ E] [Nontrivial E] (K : Set E) : ℕ → BarrierData K
  | 0 => chosenBarrierData K 1 zero_lt_one
  | n+1 =>
    let P := nestedBarrierData K n
    chosenBarrierData K (min (P.tubeMargin / 2) (1 / ((n : ℝ) + 2)))
      (lt_min (half_pos P.tubeMargin_pos) (by positivity))

theorem nestedBarrierData_error_lt [FiniteDimensional ℝ E] [Nontrivial E]
    (K : Set E) (n : ℕ) : (nestedBarrierData K n).error < 1 / ((n : ℝ) + 1) := by
  cases n with
  | zero => simpa [nestedBarrierData] using chosenBarrierData_error_lt K 1 zero_lt_one
  | succ n =>
    have hh := chosenBarrierData_error_lt K
      (min ((nestedBarrierData K n).tubeMargin / 2) (1 / ((n : ℝ) + 2)))
      (lt_min (half_pos (nestedBarrierData K n).tubeMargin_pos) (by positivity))
    have he : ((n+1 : ℕ) : ℝ) + 1 = (n : ℝ) + 2 := by push_cast; ring
    rw [he]
    exact hh.trans_le (min_le_right _ _)

theorem nestedBarrierData_gap [FiniteDimensional ℝ E] [Nontrivial E]
    (K : Set E) (n : ℕ) :
    (nestedBarrierData K (n+1)).error < (nestedBarrierData K n).tubeMargin := by
  have hh := chosenBarrierData_error_lt K
    (min ((nestedBarrierData K n).tubeMargin / 2) (1 / ((n : ℝ) + 2)))
    (lt_min (half_pos (nestedBarrierData K n).tubeMargin_pos) (by positivity))
  have hg : (nestedBarrierData K n).tubeMargin / 2 < (nestedBarrierData K n).tubeMargin := by
    linarith [(nestedBarrierData K n).tubeMargin_pos]
  exact (hh.trans_le (min_le_left _ _)).trans hg

/-- Every closed successor lies in the preceding open barrier set. -/
theorem nestedBarrierData_compactly_nested [FiniteDimensional ℝ E] [Nontrivial E]
    {K : Set E} (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K) (n : ℕ) :
    (nestedBarrierData K (n+1)).closedSet ⊆ (nestedBarrierData K n).openSet := by
  apply supportBarrier_certified_nesting hK hne hconv
    (nestedBarrierData K n).net (nestedBarrierData K (n+1)).net
    (nestedBarrierData K (n+1)).resolution_pos.le
    (chordal_sq_lt_two (nestedBarrierData K (n+1)).resolution_pos.le
      (nestedBarrierData K (n+1)).resolution_lt)
    (nestedBarrierData K (n+1)).slack_pos.le
    (nestedBarrierData K n).scale_pos (nestedBarrierData K (n+1)).scale_pos
  exact nestedBarrierData_gap K n

/-- Each selected closed sublevel is compact and is the closure of its open neighborhood. -/
theorem nestedBarrierData_compact_closure [FiniteDimensional ℝ E] [Nontrivial E]
    {K : Set E} (hK : IsCompact K) (hne : K.Nonempty) (n : ℕ) :
    IsCompact (nestedBarrierData K n).closedSet ∧
      closure (nestedBarrierData K n).openSet = (nestedBarrierData K n).closedSet := by
  let P := nestedBarrierData K n
  exact ⟨isCompact_supportBarrier_sublevel hK hne P.net
      (chordal_sq_lt_two P.resolution_pos.le P.resolution_lt) P.scale_pos 1,
    closure_supportBarrier_lt hK hne P.scale_pos.le P.cardinal_margin⟩

/-- The errors of the actually selected family tend to zero. -/
theorem nestedBarrierData_error_tendsto [FiniteDimensional ℝ E] [Nontrivial E] (K : Set E) :
    Filter.Tendsto (fun n => (nestedBarrierData K n).error) Filter.atTop (nhds 0) := by
  apply squeeze_zero (fun n => (nestedBarrierData K n).error_nonneg)
    (fun n => (nestedBarrierData_error_lt K n).le)
  simpa using tendsto_one_div_add_atTop_nhds_zero_nat

/-- Both intersections recover the original compact convex set. -/
theorem nestedBarrierData_intersections [FiniteDimensional ℝ E] [Nontrivial E]
    {K : Set E} (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K) :
    (⋂ n, (nestedBarrierData K n).openSet) = K ∧
      (⋂ n, (nestedBarrierData K n).closedSet) = K := by
  have hKin : ∀ n, K ⊆ (nestedBarrierData K n).openSet := by
    intro n x hx
    exact supportBarrier_lt_one hK hne (nestedBarrierData K n).scale_pos.le
      (nestedBarrierData K n).cardinal_margin hx
  have hclose : (⋂ n, (nestedBarrierData K n).closedSet) ⊆ K := by
    intro x hx
    by_contra hnot
    have hp : 0 < Metric.infDist x K := (hK.isClosed.notMem_iff_infDist_pos hne).mp hnot
    have he := (nestedBarrierData_error_tendsto K).eventually (gt_mem_nhds hp)
    obtain ⟨n,hn⟩ := he.exists
    have hb : Metric.infDist x K ≤ (nestedBarrierData K n).error := by
      apply infDist_le_outerErrorBound hK hne hconv (nestedBarrierData K n).net
        (nestedBarrierData K n).resolution_pos.le
        (chordal_sq_lt_two (nestedBarrierData K n).resolution_pos.le
          (nestedBarrierData K n).resolution_lt) (nestedBarrierData K n).slack_pos.le
      intro u hu
      exact supportBarrier_halfspace K _ _ _ (nestedBarrierData K n).scale_pos
        (Set.mem_iInter.mp hx n) hu
    exact (not_lt_of_ge hb) hn
  constructor
  · apply subset_antisymm
    · exact Set.Subset.trans (by
        intro x hx
        exact Set.mem_iInter.mpr (fun n => show x ∈ (nestedBarrierData K n).closedSet from
          (show supportBarrier K _ _ _ x < 1 from Set.mem_iInter.mp hx n).le)) hclose
    · exact Set.subset_iInter hKin
  · apply subset_antisymm hclose
    exact Set.subset_iInter (fun n x hx => show x ∈ (nestedBarrierData K n).closedSet from
      (show supportBarrier K _ _ _ x < 1 from hKin n hx).le)

/-- Every barrier-data certificate gives the exact Hausdorff control. -/
theorem BarrierData.hausdorff_error {K : Set E} (P : BarrierData K)
    (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K) :
    Metric.hausdorffDist P.closedSet K ≤ P.error := by
  simpa [BarrierData.closedSet, BarrierData.error, outerErrorBound, chordalSin, chordalCos]
    using supportBarrier_hausdorff_error hK hne hconv P.net P.resolution_pos.le
      P.resolution_lt P.slack_pos.le P.scale_pos P.cardinal_margin

/-- The actually chosen compactly nested neighborhoods converge in Hausdorff distance. -/
theorem nestedBarrierData_hausdorff_tendsto [FiniteDimensional ℝ E] [Nontrivial E]
    {K : Set E} (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K) :
    Filter.Tendsto (fun n => Metric.hausdorffDist (nestedBarrierData K n).closedSet K)
      Filter.atTop (nhds 0) :=
  squeeze_zero (fun _ => Metric.hausdorffDist_nonneg)
    (fun n => (nestedBarrierData K n).hausdorff_error hK hne hconv)
    (nestedBarrierData_error_tendsto K)

/-- Arbitrarily close compact outer approximations, with a smooth strictly convex
barrier and all data carrying their explicit validity hypotheses. -/
theorem exists_smooth_outer_approximation [FiniteDimensional ℝ E] [Nontrivial E]
    {K : Set E} (hK : IsCompact K) (hne : K.Nonempty) (hconv : Convex ℝ K)
    {ρ : ℝ} (hρ : 0 < ρ) :
    ∃ P : BarrierData K,
      ContDiff ℝ ∞ (supportBarrier K P.directions P.slack P.scale) ∧
      StrictConvexOn ℝ Set.univ (supportBarrier K P.directions P.slack P.scale) ∧
      IsOpen P.openSet ∧ K ⊆ P.openSet ∧ IsCompact P.closedSet ∧
      closure P.openSet = P.closedSet ∧ Metric.hausdorffDist P.closedSet K < ρ := by
  obtain ⟨P,herr⟩ := exists_barrierData_error_lt K hρ
  have hh := supportBarrier_outer_approximation hK hne hconv P.net
    P.resolution_pos.le P.resolution_lt P.slack_pos P.scale_pos P.cardinal_margin
  exact ⟨P, hh.1, hh.2.1, hh.2.2.1, hh.2.2.2.1, hh.2.2.2.2.1,
    hh.2.2.2.2.2.1, (P.hausdorff_error hK hne hconv).trans_lt herr⟩

end ConvexApprox
