import Mathlib.Analysis.Fourier.ZMod

/-!
# Finite Fourier inversion and additive convolution

The Fourier convention is `coeff χ f t = ∑ x, f x * χ (t * x)`.
The character is arbitrary; only inversion requires primitivity.
-/

open scoped BigOperators
open Finset

namespace FiniteFieldMixing

variable {p : ℕ} [Fact p.Prime]

/-- The (unnormalized) Fourier coefficient of a complex-valued density. -/
noncomputable def coeff (χ : AddChar (ZMod p) ℂ) (f : ZMod p → ℂ)
    (t : ZMod p) : ℂ :=
  ∑ x, f x * χ (t * x)

/-- Additive convolution on the prime field, with counting measure. -/
noncomputable def convolution (f g : ZMod p → ℂ) (z : ZMod p) : ℂ :=
  ∑ x, f x * g (z - x)

/-- Repeated convolution, including the point mass at zero for zero factors. -/
noncomputable def convolutionPow (f : ZMod p → ℂ) : ℕ → ZMod p → ℂ
  | 0 => fun z => if z = 0 then 1 else 0
  | n + 1 => convolution (convolutionPow f n) f

@[simp] theorem coeff_zero (χ : AddChar (ZMod p) ℂ) (f : ZMod p → ℂ) :
    coeff χ f 0 = ∑ x, f x := by
  simp [coeff]

/-- Primitive-character orthogonality, in the normalization used below. -/
theorem character_sum (χ : AddChar (ZMod p) ℂ) (hχ : χ.IsPrimitive)
    (b : ZMod p) :
    ∑ t, χ (t * b) = if b = 0 then (p : ℂ) else 0 := by
  simpa only [ZMod.card, Nat.cast_ite, Nat.cast_zero] using AddChar.sum_mulShift b hχ

/-- Fourier inversion without denominators. -/
theorem fourier_inversion_mul (χ : AddChar (ZMod p) ℂ) (hχ : χ.IsPrimitive)
    (f : ZMod p → ℂ) (z : ZMod p) :
    (p : ℂ) * f z = ∑ t, coeff χ f t * χ (-(t * z)) := by
  symm
  calc
    ∑ t, coeff χ f t * χ (-(t * z)) =
        ∑ t, ∑ x, f x * χ (t * (x - z)) := by
      simp only [coeff, Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro t ht
      apply Finset.sum_congr rfl
      intro x hx
      rw [mul_assoc, ← AddChar.map_add_eq_mul]
      congr 2
      ring
    _ = ∑ x, f x * ∑ t, χ (t * (x - z)) := by
      rw [Finset.sum_comm]
      simp only [Finset.mul_sum]
    _ = (p : ℂ) * f z := by
      simp [character_sum χ hχ, sub_eq_zero, mul_comm]

/-- Fourier inversion in the standard `1 / p` normalization. -/
theorem fourier_inversion (χ : AddChar (ZMod p) ℂ) (hχ : χ.IsPrimitive)
    (f : ZMod p → ℂ) (z : ZMod p) :
    f z = (p : ℂ)⁻¹ * ∑ t, coeff χ f t * χ (-(t * z)) := by
  rw [← fourier_inversion_mul χ hχ f z, ← mul_assoc, inv_mul_cancel₀]
  · simp
  · exact_mod_cast (NeZero.ne p)

/-- The Fourier transform sends additive convolution to pointwise multiplication. -/
theorem coeff_convolution (χ : AddChar (ZMod p) ℂ) (f g : ZMod p → ℂ)
    (t : ZMod p) :
    coeff χ (convolution f g) t = coeff χ f t * coeff χ g t := by
  classical
  simp only [coeff, convolution, Finset.sum_mul]
  rw [Finset.sum_comm]
  simp only [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro x hx
  symm
  refine Fintype.sum_equiv (Equiv.addLeft x) _ _ ?_
  intro z
  change f x * χ (t * x) * (g z * χ (t * z)) =
    f x * g (x + z - x) * χ (t * (x + z))
  rw [show t * (x + z) = t * x + t * z by ring, AddChar.map_add_eq_mul]
  simp only [add_sub_cancel_left]
  ring

@[simp] theorem coeff_pointMass (χ : AddChar (ZMod p) ℂ) (t : ZMod p) :
    coeff χ (fun z => if z = 0 then 1 else 0) t = 1 := by
  simp [coeff]

/-- Convolution powers raise every Fourier coefficient to the same power. -/
@[simp] theorem coeff_convolutionPow (χ : AddChar (ZMod p) ℂ)
    (f : ZMod p → ℂ) (n : ℕ) (t : ZMod p) :
    coeff χ (convolutionPow f n) t = coeff χ f t ^ n := by
  induction n with
  | zero => simp [convolutionPow]
  | succ n ih => rw [convolutionPow, coeff_convolution, ih, pow_succ]

/-- Total mass multiplies under convolution. -/
theorem convolution_sum (f g : ZMod p → ℂ) :
    ∑ z, convolution f g z = (∑ x, f x) * ∑ y, g y := by
  simpa only [coeff_zero] using
    coeff_convolution (1 : AddChar (ZMod p) ℂ) f g 0

/-- The total mass of a convolution power is the corresponding power of the mass. -/
theorem convolutionPow_sum (f : ZMod p → ℂ) (n : ℕ) :
    ∑ z, convolutionPow f n z = (∑ x, f x) ^ n := by
  simpa only [coeff_zero] using
    coeff_convolutionPow (1 : AddChar (ZMod p) ℂ) f n 0

/-- Scaling the density scales each Fourier coefficient. -/
theorem coeff_const_mul (χ : AddChar (ZMod p) ℂ) (c : ℂ)
    (f : ZMod p → ℂ) (t : ZMod p) :
    coeff χ (fun x => c * f x) t = c * coeff χ f t := by
  simp only [coeff, Finset.mul_sum, mul_assoc]

/-- Scaling both inputs to convolution scales their product. -/
theorem convolution_const_mul (c d : ℂ) (f g : ZMod p → ℂ) (z : ZMod p) :
    convolution (fun x => c * f x) (fun x => d * g x) z =
      (c * d) * convolution f g z := by
  simp only [convolution, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro x hx
  ring

/-- A scalar pulled from every factor acquires the number of factors as exponent. -/
theorem convolutionPow_const_mul (c : ℂ) (f : ZMod p → ℂ) (n : ℕ) (z : ZMod p) :
    convolutionPow (fun x => c * f x) n z = c ^ n * convolutionPow f n z := by
  induction n generalizing z with
  | zero => simp [convolutionPow]
  | succ n ih =>
      calc
        convolutionPow (fun x => c * f x) (n + 1) z =
            convolution (fun x => c ^ n * convolutionPow f n x)
              (fun x => c * f x) z := by
          simp only [convolutionPow, convolution, ih]
        _ = (c ^ n * c) * convolution (convolutionPow f n) f z :=
          convolution_const_mul (c ^ n) c (convolutionPow f n) f z
        _ = c ^ (n + 1) * convolutionPow f (n + 1) z := by
          rw [pow_succ, convolutionPow]

/-- In particular, normalizing each input divides the convolution power by the
corresponding power of its normalizing constant. -/
theorem convolutionPow_div (c : ℂ) (f : ZMod p → ℂ) (n : ℕ) (z : ZMod p) :
    convolutionPow (fun x => f x / c) n z = convolutionPow f n z / c ^ n := by
  simpa only [div_eq_mul_inv, mul_comm, inv_pow] using
    convolutionPow_const_mul c⁻¹ f n z

end FiniteFieldMixing
