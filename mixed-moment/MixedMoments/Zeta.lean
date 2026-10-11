import Mathlib
import MixedMoments.Rational
import MixedMoments.Cancellation

/-!
# Analytic Z moments

The measure is the product of Lebesgue measure restricted to the open unit
interval. This removes only the null boundary of the square. All exponents
and series indices are natural numbers.
-/

noncomputable section

open MeasureTheory Set Filter Finset
open scoped Topology

namespace MixedMoments.Zeta

/-- The coefficient obtained by integrating a geometric-series term. -/
def term (i j u : ℕ) : ℝ :=
  1 / (((i + u + 1 : ℕ) : ℝ) * ((j + u + 1 : ℕ) : ℝ))

/-- The convergent numerical series for a Z moment. -/
def series (i j : ℕ) : ℝ := ∑' u, term i j u

/-- Lebesgue measure on the open unit interval. -/
def unitMeasure : Measure ℝ := volume.restrict (Ioo 0 1)

instance : IsFiniteMeasure unitMeasure := by
  unfold unitMeasure
  infer_instance

/-- The measure on the unit square; its boundary has measure zero. -/
def squareMeasure : Measure (ℝ × ℝ) := unitMeasure.prod unitMeasure

/-- The actual rational kernel defining a Z moment. -/
def kernel (i j : ℕ) (p : ℝ × ℝ) : ℝ :=
  p.1 ^ i * p.2 ^ j / (1 - p.1 * p.2)

/-- The actual Lebesgue Z integral. -/
def Z (i j : ℕ) : ℝ := ∫ p, kernel i j p ∂squareMeasure

/-- A term of the geometric expansion of the kernel. -/
def monomial (i j u : ℕ) (p : ℝ × ℝ) : ℝ :=
  p.1 ^ (i + u) * p.2 ^ (j + u)

theorem term_nonneg (i j u : ℕ) : 0 ≤ term i j u := by
  unfold term
  positivity

theorem summable_term (i j : ℕ) : Summable (term i j) := by
  have hp : Summable (fun u : ℕ => 1 / (((u + 1 : ℕ) : ℝ) ^ 2)) := by
    exact (summable_nat_add_iff 1).2
      (Real.summable_one_div_nat_pow.2 (by decide : 1 < 2))
  apply Summable.of_nonneg_of_le (term_nonneg i j) _ hp
  intro u
  unfold term
  apply one_div_le_one_div_of_le
  · positivity
  · have hi : ((u + 1 : ℕ) : ℝ) ≤ ((i + u + 1 : ℕ) : ℝ) := by
      exact_mod_cast (show u + 1 ≤ i + u + 1 by omega)
    have hj : ((u + 1 : ℕ) : ℝ) ≤ ((j + u + 1 : ℕ) : ℝ) := by
      exact_mod_cast (show u + 1 ≤ j + u + 1 by omega)
    simpa only [pow_two] using mul_le_mul hi hj (by positivity) (by positivity)

theorem ae_mem_square :
    ∀ᵐ p ∂squareMeasure, p.1 ∈ Ioo (0 : ℝ) 1 ∧ p.2 ∈ Ioo (0 : ℝ) 1 := by
  unfold squareMeasure unitMeasure
  rw [Measure.prod_restrict]
  exact ae_restrict_mem (measurableSet_Ioo.prod measurableSet_Ioo)

theorem integrable_unit_pow (n : ℕ) : Integrable (fun t : ℝ => t ^ n) unitMeasure := by
  exact ((continuous_id.pow n).continuousOn.integrableOn_Icc
    (μ := volume) (a := (0 : ℝ)) (b := 1)).mono_set Ioo_subset_Icc_self

theorem integral_unit_pow (n : ℕ) :
    (∫ t, t ^ n ∂unitMeasure) = 1 / ((n + 1 : ℕ) : ℝ) := by
  unfold unitMeasure
  rw [← integral_Ioc_eq_integral_Ioo,
    ← intervalIntegral.integral_of_le (by norm_num : (0 : ℝ) ≤ 1),
    integral_pow]
  simp

theorem integrable_monomial (i j u : ℕ) :
    Integrable (monomial i j u) squareMeasure :=
  (integrable_unit_pow (i + u)).mul_prod (integrable_unit_pow (j + u))

theorem integral_monomial (i j u : ℕ) :
    (∫ p, monomial i j u p ∂squareMeasure) = term i j u := by
  unfold monomial squareMeasure term
  rw [integral_prod_mul (fun t : ℝ => t ^ (i + u))
    (fun s : ℝ => s ^ (j + u)), integral_unit_pow, integral_unit_pow]
  ring

theorem ae_monomial_nonneg (i j u : ℕ) :
    0 ≤ᵐ[squareMeasure] monomial i j u := by
  filter_upwards [ae_mem_square] with p hp
  exact mul_nonneg (pow_nonneg hp.1.1.le _) (pow_nonneg hp.2.1.le _)

/-- The geometric expansion is valid at every point of the open square. -/
theorem hasSum_monomial {p : ℝ × ℝ} (hp :
    p.1 ∈ Ioo (0 : ℝ) 1 ∧ p.2 ∈ Ioo (0 : ℝ) 1) (i j : ℕ) :
    HasSum (fun u => monomial i j u p) (kernel i j p) := by
  have hpos : 0 ≤ p.1 * p.2 := mul_nonneg hp.1.1.le hp.2.1.le
  have hlt : p.1 * p.2 < 1 := calc
    p.1 * p.2 < p.1 * 1 := mul_lt_mul_of_pos_left hp.2.2 hp.1.1
    _ < 1 := by simpa using hp.1.2
  have hg := (hasSum_geometric_of_abs_lt_one
    (by rwa [abs_of_nonneg hpos] : |p.1 * p.2| < 1)).mul_left (p.1 ^ i * p.2 ^ j)
  convert hg using 1
  · ext u
    simp only [monomial, pow_add, mul_pow]
    ring

/-- Absolute integrability includes the singular corner: it follows from
summability of the integrals of the nonnegative geometric terms. -/
theorem integrable_kernel (i j : ℕ) : Integrable (kernel i j) squareMeasure := by
  refine ⟨?_, ?_⟩
  · exact (by unfold kernel; fun_prop : Measurable (kernel i j)).aestronglyMeasurable
  · have hnn : 0 ≤ᵐ[squareMeasure] kernel i j := by
      filter_upwards [ae_mem_square] with p hp
      exact (hasSum_monomial hp i j).tsum_eq ▸ tsum_nonneg
        (fun u => mul_nonneg (pow_nonneg hp.1.1.le _) (pow_nonneg hp.2.1.le _))
    rw [hasFiniteIntegral_iff_ofReal hnn]
    have heq : (fun p => ENNReal.ofReal (kernel i j p)) =ᵐ[squareMeasure]
        (fun p => ∑' u, ENNReal.ofReal (monomial i j u p)) := by
      filter_upwards [ae_mem_square] with p hp
      rw [← (hasSum_monomial hp i j).tsum_eq]
      exact ENNReal.ofReal_tsum_of_nonneg
        (fun u => mul_nonneg (pow_nonneg hp.1.1.le _) (pow_nonneg hp.2.1.le _))
        (hasSum_monomial hp i j).summable
    rw [lintegral_congr_ae heq, lintegral_tsum
      (fun u => (integrable_monomial i j u).aestronglyMeasurable.aemeasurable.ennreal_ofReal)]
    have heach (u : ℕ) : (∫⁻ p, ENNReal.ofReal (monomial i j u p) ∂squareMeasure) =
        ENNReal.ofReal (term i j u) := by
      rw [← ofReal_integral_eq_lintegral_ofReal (integrable_monomial i j u)
        (ae_monomial_nonneg i j u), integral_monomial]
    simp_rw [heach]
    rw [← ENNReal.ofReal_tsum_of_nonneg (term_nonneg i j) (summable_term i j)]
    exact ENNReal.ofReal_lt_top

/-- An unconditional identity for the actual Z integral. -/
theorem Z_eq_series (i j : ℕ) : Z i j = series i j := by
  have hn : Summable (fun u => ∫ p, ‖monomial i j u p‖ ∂squareMeasure) := by
    convert summable_term i j using 1
    ext u
    rw [← integral_monomial]
    apply integral_congr_ae
    filter_upwards [ae_monomial_nonneg i j u] with p hp
    exact Real.norm_of_nonneg hp
  unfold Z series
  calc
    (∫ p, kernel i j p ∂squareMeasure) =
        ∫ p, (∑' u, monomial i j u p) ∂squareMeasure := by
      apply integral_congr_ae
      filter_upwards [ae_mem_square] with p hp
      exact (hasSum_monomial hp i j).tsum_eq.symm
    _ = ∑' u, ∫ p, monomial i j u p ∂squareMeasure :=
      (integral_tsum_of_summable_integral_norm (integrable_monomial i j) hn).symm
    _ = ∑' u, term i j u := by simp_rw [integral_monomial]

/-- The product integral agrees with the iterated interval-integral convention. -/
theorem Z_eq_iterated (i j : ℕ) :
    Z i j = ∫ t in (0 : ℝ)..1, ∫ s in (0 : ℝ)..1,
      t ^ i * s ^ j / (1 - t * s) := by
  unfold Z squareMeasure
  rw [integral_prod _ (integrable_kernel i j)]
  simp_rw [unitMeasure, ← integral_Ioc_eq_integral_Ioo,
    ← intervalIntegral.integral_of_le (by norm_num : (0 : ℝ) ≤ 1)]
  rfl

theorem series_symm (i j : ℕ) : series i j = series j i := by
  unfold series term
  simp_rw [mul_comm]

theorem Z_symm (i j : ℕ) : Z i j = Z j i := by
  rw [Z_eq_series, Z_eq_series, series_symm]

/-- The constant ζ₂ is defined by its convergent square reciprocal series. -/
def zeta2 : ℝ := ∑' u : ℕ, 1 / (((u + 1 : ℕ) : ℝ) ^ 2)

/-- Harmonic numbers with an empty initial sum at index zero. -/
def harmonic (n : ℕ) : ℝ := ∑ k ∈ range n, 1 / ((k + 1 : ℕ) : ℝ)

/-- Second-order harmonic numbers. -/
def harmonic2 (n : ℕ) : ℝ := ∑ k ∈ range n, 1 / (((k + 1 : ℕ) : ℝ) ^ 2)

theorem summable_zeta2 : Summable (fun u : ℕ => 1 / (((u + 1 : ℕ) : ℝ) ^ 2)) :=
  (summable_nat_add_iff 1).2
    (Real.summable_one_div_nat_pow.2 (by decide : 1 < 2))

theorem series_diagonal (i : ℕ) : series i i = zeta2 - harmonic2 i := by
  have h := summable_zeta2.sum_add_tsum_nat_add i
  have hshift : (∑' u : ℕ, 1 / (((u + i + 1 : ℕ) : ℝ) ^ 2)) = series i i := by
    unfold series term
    congr 1
    ext u
    rw [Nat.add_comm u i, pow_two]
  rw [hshift] at h
  exact eq_sub_of_add_eq' h

theorem Z_diagonal (i : ℕ) : Z i i = zeta2 - harmonic2 i := by
  rw [Z_eq_series, series_diagonal]

private def reciprocalTail (i d n : ℕ) : ℝ :=
  ∑ k ∈ range d, 1 / ((i + n + k + 1 : ℕ) : ℝ)

private theorem reciprocalTail_sub_succ (i d n : ℕ) :
    reciprocalTail i d n - reciprocalTail i d (n + 1) =
      1 / ((i + n + 1 : ℕ) : ℝ) - 1 / ((i + n + d + 1 : ℕ) : ℝ) := by
  unfold reciprocalTail
  rw [← Finset.sum_sub_distrib]
  simpa [Nat.add_assoc, Nat.add_left_comm, Nat.add_comm] using
    Finset.sum_range_sub' (fun k : ℕ => 1 / ((i + n + k + 1 : ℕ) : ℝ)) d

private theorem tendsto_reciprocalTail (i d : ℕ) :
    Tendsto (reciprocalTail i d) atTop (𝓝 0) := by
  unfold reciprocalTail
  have h := tendsto_finset_sum (range d) (fun k _ =>
    (tendsto_add_atTop_iff_nat (i + k + 1)).2 tendsto_one_div_atTop_nhds_zero_nat)
  simpa [Nat.add_assoc, Nat.add_left_comm, Nat.add_comm] using h

private theorem offset_scaled_term (i d u : ℕ) :
    (d : ℝ) * term i (i + d) u =
      reciprocalTail i d u - reciprocalTail i d (u + 1) := by
  rw [reciprocalTail_sub_succ]
  unfold term
  have ha : ((i + u + 1 : ℕ) : ℝ) ≠ 0 := by positivity
  have hb : ((i + d + u + 1 : ℕ) : ℝ) ≠ 0 := by positivity
  have heq : i + u + d + 1 = i + d + u + 1 := by omega
  rw [heq]
  field_simp
  push_cast
  ring

/-- Off-diagonal evaluation with a positive natural offset. -/
theorem series_add_offset (i d : ℕ) (hd : 0 < d) :
    series i (i + d) = (harmonic (i + d) - harmonic i) / (d : ℝ) := by
  have hp (N : ℕ) :
      (∑ u ∈ range N, (d : ℝ) * term i (i + d) u) =
        reciprocalTail i d 0 - reciprocalTail i d N := by
    simp_rw [offset_scaled_term]
    exact Finset.sum_range_sub' (reciprocalTail i d) N
  have hlim : Tendsto (fun N => ∑ u ∈ range N, (d : ℝ) * term i (i + d) u)
      atTop (𝓝 (reciprocalTail i d 0)) := by
    simp_rw [hp]
    simpa only [sub_zero] using (tendsto_reciprocalTail i d).const_sub
      (reciprocalTail i d 0)
  have hs : HasSum (fun u => (d : ℝ) * term i (i + d) u) (reciprocalTail i d 0) :=
    ((summable_term i (i + d)).mul_left (d : ℝ)).hasSum_iff_tendsto_nat.2 hlim
  have heq : (d : ℝ) * series i (i + d) = reciprocalTail i d 0 :=
    ((summable_term i (i + d)).hasSum.mul_left (d : ℝ)).unique hs
  have htail : reciprocalTail i d 0 = harmonic (i + d) - harmonic i := by
    have h := Finset.sum_range_add (fun k : ℕ => 1 / ((k + 1 : ℕ) : ℝ)) i d
    simpa [reciprocalTail, harmonic] using (eq_sub_of_add_eq' h.symm)
  rw [htail] at heq
  apply (eq_div_iff (by exact_mod_cast hd.ne' : (d : ℝ) ≠ 0)).2
  simpa only [mul_comm] using heq

/-- Off-diagonal formula, with the positive quotient orientation. -/
theorem series_offDiagonal_of_lt {i j : ℕ} (hij : i < j) :
    series i j = (harmonic j - harmonic i) / ((j : ℝ) - (i : ℝ)) := by
  have hsum : i + (j - i) = j := Nat.add_sub_of_le hij.le
  have h := series_add_offset i (j - i) (Nat.sub_pos_of_lt hij)
  rw [hsum] at h
  simpa only [Nat.cast_sub hij.le] using h

/-- The symmetric off-diagonal formula from the study. -/
theorem series_offDiagonal {i j : ℕ} (hij : i ≠ j) :
    series i j = (harmonic i - harmonic j) / ((i : ℝ) - (j : ℝ)) := by
  rcases lt_or_gt_of_ne hij with h | h
  · rw [series_offDiagonal_of_lt h]
    exact (neg_div_neg_eq _ _).symm.trans (by rw [neg_sub, neg_sub])
  · rw [series_symm, series_offDiagonal_of_lt h]

theorem Z_offDiagonal {i j : ℕ} (hij : i ≠ j) :
    Z i j = (harmonic i - harmonic j) / ((i : ℝ) - (j : ℝ)) := by
  rw [Z_eq_series, series_offDiagonal hij]

/-- The sign check in the source is an actual integral equality. -/
theorem Z_zero_one : Z 0 1 = 1 := by
  rw [Z_offDiagonal (by decide : (0 : ℕ) ≠ 1)]
  norm_num [harmonic]

/-- Agreement of the analytic harmonic numbers with the exact rational array. -/
theorem harmonic_cast (n : ℕ) :
    (MixedMoments.harmonic n : ℝ) = harmonic n := by
  simp [MixedMoments.harmonic, harmonic]

theorem harmonicTwo_cast (n : ℕ) :
    (MixedMoments.harmonicTwo n : ℝ) = harmonic2 n := by
  simp [MixedMoments.harmonicTwo, harmonic2]

/-- The source's specified rational/ζ₂ decomposition holds for actual integrals. -/
theorem Z_eq_zRationalPart (i j : ℕ) :
    Z i j = (MixedMoments.zRationalPart i j : ℝ) +
      if i = j then zeta2 else 0 := by
  by_cases h : i = j
  · subst j
    rw [Z_diagonal]
    simp [MixedMoments.zRationalPart, harmonicTwo_cast]
    ring
  · rw [Z_offDiagonal h]
    simp [MixedMoments.zRationalPart, h, harmonic_cast]

/-- A polynomial in the first variable and a monomial in the second. -/
def columnKernel (D : Polynomial ℚ) (j : ℕ) (p : ℝ × ℝ) : ℝ :=
  D.eval₂ (Rat.castHom ℝ) p.1 * p.2 ^ j / (1 - p.1 * p.2)

/-- The actual polynomial Z column, rather than a formal coefficient array. -/
def polynomialColumn (D : Polynomial ℚ) (j : ℕ) : ℝ :=
  ∫ p, columnKernel D j p ∂squareMeasure

theorem columnKernel_eq_sum (D : Polynomial ℚ) (j : ℕ) (p : ℝ × ℝ) :
    columnKernel D j p = ∑ i ∈ D.support, (D.coeff i : ℝ) * kernel i j p := by
  unfold columnKernel
  rw [Polynomial.eval₂_eq_sum, Polynomial.sum_def, Finset.sum_mul, Finset.sum_div]
  apply Finset.sum_congr rfl
  intro i hi
  simp only [Rat.coe_castHom, kernel]
  ring

theorem integrable_columnKernel (D : Polynomial ℚ) (j : ℕ) :
    Integrable (columnKernel D j) squareMeasure := by
  have heq : columnKernel D j =
      fun p => ∑ i ∈ D.support, (D.coeff i : ℝ) * kernel i j p :=
    funext (columnKernel_eq_sum D j)
  rw [heq]
  exact integrable_finset_sum D.support (fun i _ =>
    (integrable_kernel i j).const_mul (D.coeff i : ℝ))

/-- Finite polynomial expansion is justified by the proved integrability of
all constituent monomial kernels. -/
theorem polynomialColumn_eq_sum (D : Polynomial ℚ) (j : ℕ) :
    polynomialColumn D j = ∑ i ∈ D.support, (D.coeff i : ℝ) * Z i j := by
  unfold polynomialColumn
  simp_rw [columnKernel_eq_sum]
  rw [integral_finset_sum D.support (fun i _ =>
    (integrable_kernel i j).const_mul (D.coeff i : ℝ))]
  simp only [integral_const_mul, Z]

/-- A genuine polynomial kernel in both variables. -/
def polynomialKernel (D Q : Polynomial ℚ) (p : ℝ × ℝ) : ℝ :=
  D.eval₂ (Rat.castHom ℝ) p.1 * Q.eval₂ (Rat.castHom ℝ) p.2 /
    (1 - p.1 * p.2)

def polynomialIntegral (D Q : Polynomial ℚ) : ℝ :=
  ∫ p, polynomialKernel D Q p ∂squareMeasure

theorem polynomialKernel_eq_sum (D Q : Polynomial ℚ) (p : ℝ × ℝ) :
    polynomialKernel D Q p = ∑ i ∈ D.support, ∑ j ∈ Q.support,
      ((D.coeff i : ℝ) * (Q.coeff j : ℝ)) * kernel i j p := by
  unfold polynomialKernel
  simp only [Polynomial.eval₂_eq_sum, Polynomial.sum_def]
  simp_rw [Finset.sum_mul, Finset.mul_sum, Finset.sum_div]
  apply Finset.sum_congr rfl
  intro i hi
  apply Finset.sum_congr rfl
  intro j hj
  simp only [Rat.coe_castHom, kernel]
  ring

theorem integrable_polynomialKernel (D Q : Polynomial ℚ) :
    Integrable (polynomialKernel D Q) squareMeasure := by
  have heq : polynomialKernel D Q = fun p =>
      ∑ i ∈ D.support, ∑ j ∈ Q.support,
        ((D.coeff i : ℝ) * (Q.coeff j : ℝ)) * kernel i j p :=
    funext (polynomialKernel_eq_sum D Q)
  rw [heq]
  exact integrable_finset_sum D.support (fun i _ =>
    integrable_finset_sum Q.support (fun j _ =>
      (integrable_kernel i j).const_mul ((D.coeff i : ℝ) * (Q.coeff j : ℝ))))

theorem polynomialIntegral_eq_sum (D Q : Polynomial ℚ) :
    polynomialIntegral D Q = ∑ i ∈ D.support, ∑ j ∈ Q.support,
      ((D.coeff i : ℝ) * (Q.coeff j : ℝ)) * Z i j := by
  unfold polynomialIntegral
  simp_rw [polynomialKernel_eq_sum]
  rw [integral_finset_sum D.support (fun i _ =>
    integrable_finset_sum Q.support (fun j _ =>
      (integrable_kernel i j).const_mul ((D.coeff i : ℝ) * (Q.coeff j : ℝ))))]
  congr 1
  ext i
  rw [integral_finset_sum Q.support (fun j _ =>
    (integrable_kernel i j).const_mul ((D.coeff i : ℝ) * (Q.coeff j : ℝ)))]
  simp only [integral_const_mul, Z]

/-- The same column integral in the source's iterated interval notation. -/
theorem polynomialColumn_eq_iterated (D : Polynomial ℚ) (j : ℕ) :
    polynomialColumn D j = ∫ t in (0 : ℝ)..1, ∫ s in (0 : ℝ)..1,
      D.eval₂ (Rat.castHom ℝ) t * s ^ j / (1 - t * s) := by
  unfold polynomialColumn squareMeasure
  rw [integral_prod _ (integrable_columnKernel D j)]
  simp_rw [unitMeasure, ← integral_Ioc_eq_integral_Ioo,
    ← intervalIntegral.integral_of_le (by norm_num : (0 : ℝ) ≤ 1)]
  rfl

/-- The canonical formal Z coordinates are realized by the actual integral.
The Catalan parameter is arbitrary because the Z coordinates contain no
Catalan component. -/
theorem Z_eq_formalZ (G : ℝ) (i j : ℕ) :
    Z i j = Coordinates.eval G zeta2 (MixedMoments.formalZ i j) := by
  rw [Z_eq_zRationalPart]
  simp only [MixedMoments.formalZ, Coordinates.eval_mk, Rat.cast_zero,
    zero_mul, add_zero]
  split_ifs <;> simp

theorem polynomialColumn_eq_formalZ (G : ℝ) (D : Polynomial ℚ) (j : ℕ) :
    polynomialColumn D j = Coordinates.eval G zeta2 (MixedMoments.polynomialZ D j) := by
  rw [polynomialColumn_eq_sum]
  unfold MixedMoments.polynomialZ
  rw [Coordinates.eval_sum]
  apply Finset.sum_congr rfl
  intro i hi
  rw [Coordinates.eval_smul, Z_eq_formalZ]

end MixedMoments.Zeta
