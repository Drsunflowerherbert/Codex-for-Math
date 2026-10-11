import FiniteFieldMixing.Fourier

/-!
# Fourier bounds for finite-field convolution powers

Small nonzero Fourier coefficients bound the distance from the mean and give a
pointwise lower bound for the real part. The convolution versions apply these
bounds after raising each Fourier coefficient to the convolution exponent.
-/

open Finset
open scoped BigOperators

namespace FiniteFieldMixing
variable {p : ℕ} [Fact p.Prime]

/-- Bound the nonconstant part of an inverse Fourier expansion. -/
lemma norm_sub_mass_le_of_expansion
    (χ : AddChar (ZMod p) ℂ) (a : ZMod p → ℂ) (v M : ℂ) (C : ℝ) (z : ZMod p)
    (hv : (p : ℂ) * v = ∑ t, a t * χ (-(t * z)))
    (hzero : a 0 = M) (hbound : ∀ t ≠ 0, ‖a t‖ ≤ C) :
    ‖(p : ℂ) * v - M‖ ≤ ((p : ℝ) - 1) * C := by
  classical
  have hsplit : (p : ℂ) * v - M =
      ∑ t ∈ (Finset.univ : Finset (ZMod p)).erase 0, a t * χ (-(t * z)) := by
    rw [hv, ← Finset.sum_erase_add _ _ (Finset.mem_univ (0 : ZMod p))]
    simp [hzero]
  rw [hsplit]
  calc
    ‖∑ t ∈ (Finset.univ : Finset (ZMod p)).erase 0, a t * χ (-(t * z))‖
        ≤ ∑ t ∈ (Finset.univ : Finset (ZMod p)).erase 0, ‖a t * χ (-(t * z))‖ := norm_sum_le _ _
    _ ≤ ∑ t ∈ (Finset.univ : Finset (ZMod p)).erase 0, C := by
      apply Finset.sum_le_sum
      intro t ht
      simpa using hbound t (Finset.mem_erase.mp ht).1
    _ = ((p : ℝ) - 1) * C := by
      simp only [Finset.sum_const, Finset.card_erase_of_mem (Finset.mem_univ _),
        Finset.card_univ, ZMod.card, nsmul_eq_mul]
      rw [Nat.cast_sub (Nat.Prime.one_le Fact.out), Nat.cast_one]

/-- The inverse expansion bounds the real part using the zero coefficient as mass. -/
lemma re_lower_bound_of_expansion
    (χ : AddChar (ZMod p) ℂ) (a : ZMod p → ℂ) (v : ℂ) (M C : ℝ) (z : ZMod p)
    (hv : (p : ℂ) * v = ∑ t, a t * χ (-(t * z)))
    (hzero : a 0 = (M : ℂ)) (hbound : ∀ t ≠ 0, ‖a t‖ ≤ C) :
    (M - ((p : ℝ) - 1) * C) / (p : ℝ) ≤ v.re := by
  have hnorm := norm_sub_mass_le_of_expansion χ a v (M : ℂ) C z hv hzero hbound
  have hre := (abs_le.mp (Complex.abs_re_le_norm ((p : ℂ) * v - (M : ℂ)))).1
  have hp : (0 : ℝ) < p := Nat.cast_pos.mpr (Nat.Prime.pos Fact.out)
  apply (div_le_iff₀ hp).mpr
  simp only [Complex.sub_re, Complex.mul_re, Complex.natCast_re, Complex.natCast_im,
    zero_mul, sub_zero, Complex.ofReal_re] at hre
  nlinarith

/-- A bound on all nontrivial Fourier coefficients controls deviation from the mean. -/
theorem norm_sub_mean_le
    (χ : AddChar (ZMod p) ℂ) (hχ : χ.IsPrimitive) (f : ZMod p → ℂ)
    (M : ℂ) (C : ℝ) (hzero : coeff χ f 0 = M)
    (hbound : ∀ t ≠ 0, ‖coeff χ f t‖ ≤ C) (z : ZMod p) :
    ‖f z - M / (p : ℂ)‖ ≤ ((p : ℝ) - 1) / (p : ℝ) * C := by
  have hnorm := norm_sub_mass_le_of_expansion χ (coeff χ f) (f z) M C z
    (fourier_inversion_mul χ hχ f z) hzero hbound
  have hp : (0 : ℝ) < p := Nat.cast_pos.mpr (Nat.Prime.pos Fact.out)
  have hpC : (p : ℂ) ≠ 0 := by exact_mod_cast (Nat.Prime.ne_zero Fact.out)
  have heq : (p : ℂ) * (f z - M / (p : ℂ)) = (p : ℂ) * f z - M := by
    field_simp
  rw [← heq, norm_mul, Complex.norm_natCast] at hnorm
  calc
    ‖f z - M / (p : ℂ)‖ ≤ ((p : ℝ) - 1) * C / (p : ℝ) := by
      apply (le_div_iff₀ hp).mpr
      nlinarith
    _ = ((p : ℝ) - 1) / (p : ℝ) * C := by ring

/-- Fourier inversion gives a real lower bound from the mass and nonzero coefficients. -/
theorem re_lower_bound_of_coeff_bound
    (χ : AddChar (ZMod p) ℂ) (hχ : χ.IsPrimitive) (f : ZMod p → ℂ)
    (M C : ℝ) (hzero : coeff χ f 0 = (M : ℂ))
    (hbound : ∀ t ≠ 0, ‖coeff χ f t‖ ≤ C) (z : ZMod p) :
    (M - ((p : ℝ) - 1) * C) / (p : ℝ) ≤ (f z).re :=
  re_lower_bound_of_expansion χ (coeff χ f) (f z) M C z
    (fourier_inversion_mul χ hχ f z) hzero hbound

/-- A probability density with small nonzero coefficients is close to uniform. -/
theorem norm_sub_uniform_le
    (χ : AddChar (ZMod p) ℂ) (hχ : χ.IsPrimitive) (f : ZMod p → ℂ)
    (β : ℝ) (hmass : ∑ x, f x = 1)
    (hbound : ∀ t ≠ 0, ‖coeff χ f t‖ ≤ β) (z : ZMod p) :
    ‖f z - (p : ℂ)⁻¹‖ ≤ ((p : ℝ) - 1) / (p : ℝ) * β := by
  simpa only [one_div] using norm_sub_mean_le χ hχ f 1 β
    (by simpa only [coeff_zero] using hmass) hbound z

/-- Repeated convolution raises the nonzero Fourier bound to the same power. -/
theorem coeff_convolutionPow_norm_le
    (χ : AddChar (ZMod p) ℂ) (f : ZMod p → ℂ) (β : ℝ)
    (hbound : ∀ t ≠ 0, ‖coeff χ f t‖ ≤ β) (n : ℕ) (t : ZMod p) (ht : t ≠ 0) :
    ‖coeff χ (convolutionPow f n) t‖ ≤ β ^ n := by
  rw [coeff_convolutionPow, norm_pow]
  exact pow_le_pow_left₀ (norm_nonneg _) (hbound t ht) n

/-- Quantitative uniform mixing for a convolution power of a probability density. -/
theorem convolutionPow_norm_sub_uniform_le
    (χ : AddChar (ZMod p) ℂ) (hχ : χ.IsPrimitive) (f : ZMod p → ℂ)
    (β : ℝ) (hmass : ∑ x, f x = 1)
    (hbound : ∀ t ≠ 0, ‖coeff χ f t‖ ≤ β) (n : ℕ) (z : ZMod p) :
    ‖convolutionPow f n z - (p : ℂ)⁻¹‖ ≤ ((p : ℝ) - 1) / (p : ℝ) * β ^ n := by
  apply norm_sub_uniform_le χ hχ (convolutionPow f n) (β ^ n)
  · rw [convolutionPow_sum, hmass, one_pow]
  · exact coeff_convolutionPow_norm_le χ f β hbound n

/-- The mass form of the lower bound for repeated convolution. -/
theorem convolutionPow_re_lower_bound
    (χ : AddChar (ZMod p) ℂ) (hχ : χ.IsPrimitive) (f : ZMod p → ℂ)
    (M C : ℝ) (hzero : coeff χ f 0 = (M : ℂ))
    (hbound : ∀ t ≠ 0, ‖coeff χ f t‖ ≤ C) (n : ℕ) (z : ZMod p) :
    (M ^ n - ((p : ℝ) - 1) * C ^ n) / (p : ℝ) ≤ (convolutionPow f n z).re := by
  apply re_lower_bound_of_coeff_bound χ hχ (convolutionPow f n) (M ^ n) (C ^ n)
  · rw [coeff_convolutionPow, hzero, Complex.ofReal_pow]
  · exact coeff_convolutionPow_norm_le χ f C hbound n

end FiniteFieldMixing
