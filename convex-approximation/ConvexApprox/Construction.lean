import ConvexApprox.Sublevels
import ConvexApprox.OuterApprox

/-!
# Arbitrary-accuracy choice of the existing barrier parameters

This module implements the reviewed small-parameter selection. It does not assert
analytic manifold or sphere-parametrization results. Nontriviality is explicit where
we use a nonempty direction net and the logarithmic cardinal-margin equivalence.
-/

noncomputable section

namespace ConvexApprox

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Finite nets containing a prescribed unit family have independent positive
slack and scale with strict cardinal margin and arbitrarily small exact error.
No compactness is needed for numerical parameter selection alone. -/
theorem exists_outer_parameters_containing [FiniteDimensional ℝ E] [Nontrivial E]
    (K : Set E) (A : Finset E) (hA : ∀ u ∈ A, ‖u‖ = 1)
    {ρ : ℝ} (hρ : 0 < ρ) :
    ∃ (D : Finset E) (δ ε t : ℝ), A ⊆ D ∧ IsChordalNet D δ ∧
      0 < δ ∧ δ < Real.sqrt 2 ∧ 0 < ε ∧ 0 < t ∧
      (D.card : ℝ) * Real.exp (-t * ε) < 1 ∧ outerErrorBound K δ ε < ρ := by
  classical
  let L : ℝ := Metric.diam K
  have hL : 0 ≤ L := Metric.diam_nonneg
  let δ : ℝ := min (1 / 2) (ρ / (8 * (1 + L)))
  let ε : ℝ := ρ / 8
  have hden : 0 < 8 * (1 + L) := by positivity
  have hδ : 0 < δ := lt_min (by norm_num) (div_pos hρ hden)
  have hδsmall : δ ≤ 1 / 2 := min_le_left _ _
  have hδscaled : δ * (8 * (1 + L)) ≤ ρ :=
    (le_div_iff₀ hden).mp (min_le_right _ _)
  have hδL : δ * L ≤ ρ / 8 := by nlinarith
  have hδsq : δ ^ 2 ≤ (1 / 2 : ℝ) ^ 2 :=
    (sq_le_sq₀ hδ.le (by norm_num)).mpr hδsmall
  have hδsq_lt : δ ^ 2 < 2 := by nlinarith
  have hδsqrt : δ < Real.sqrt 2 := by
    have hs : (Real.sqrt 2) ^ 2 = (2 : ℝ) := Real.sq_sqrt (by norm_num)
    nlinarith [Real.sqrt_nonneg (2 : ℝ)]
  have hε : 0 < ε := div_pos hρ (by norm_num)
  have hc : 0 < chordalCos δ := chordalCos_pos hδsq_lt
  have hclower : 1 / 2 ≤ chordalCos δ := by
    unfold chordalCos
    nlinarith
  have hsinL : chordalSin δ * L ≤ δ * L :=
    mul_le_mul_of_nonneg_right (chordalSin_le hδ.le) hL
  have herr : outerErrorBound K δ ε < ρ := by
    have hnum : ε + chordalSin δ * L ≤ ρ / 4 := by dsimp [ε]; linarith
    have hprod := mul_le_mul_of_nonneg_left hclower hρ.le
    unfold outerErrorBound
    apply (div_lt_iff₀ hc).mpr
    change ε + chordalSin δ * L < ρ * chordalCos δ
    linarith
  obtain ⟨D, hAD, hnet⟩ := exists_chordalNet_containing A hA hδ
  let t : ℝ := max 1 (Real.log (D.card : ℝ) / ε + 1)
  have ht : 0 < t := lt_of_lt_of_le zero_lt_one (le_max_left _ _)
  have htlog : Real.log (D.card : ℝ) / ε < t := by
    have h := le_max_right (1 : ℝ) (Real.log (D.card : ℝ) / ε + 1)
    change Real.log (D.card : ℝ) / ε + 1 ≤ t at h
    linarith
  have hlog : Real.log (D.card : ℝ) < t * ε := (div_lt_iff₀ hε).mp htlog
  letI : Nonempty {u // u ∈ D} := by
    obtain ⟨u, hu⟩ := hnet.nonempty
    exact ⟨⟨u, hu⟩⟩
  have hmargin : (D.card : ℝ) * Real.exp (-t * ε) < 1 := by
    simpa using (cardinal_margin_iff (ι := {u // u ∈ D}) ε t).mpr (by simpa using hlog)
  exact ⟨D, δ, ε, t, hAD, hnet, hδ, hδsqrt, hε, ht, hmargin, herr⟩

end ConvexApprox
