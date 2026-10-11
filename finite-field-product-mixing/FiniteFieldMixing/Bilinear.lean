import Mathlib

/-!
# Bilinear character sums over a prime field

The exact energy identity is the orthogonality input to the rectangular
Cauchy–Schwarz bound. Normalizing gives the characteristic coefficient of
the product of independent uniform samples from two nonempty finite sets.
-/

noncomputable section

open scoped BigOperators ComplexConjugate

namespace FiniteFieldMixing

variable {p : ℕ} [Fact p.Prime]

/-- The unnormalized bilinear additive-character sum. -/
def bilinearSum (ψ : AddChar (ZMod p) ℂ) (A B : Finset (ZMod p))
    (r : ZMod p) : ℂ :=
  ∑ a ∈ A, ∑ b ∈ B, ψ (r * a * b)

/-- The characteristic coefficient of the product of two independent
uniform samples from `A` and `B`. -/
def normalizedProductCoeff (ψ : AddChar (ZMod p) ℂ)
    (A B : Finset (ZMod p)) (r : ZMod p) : ℂ :=
  bilinearSum ψ A B r / ((A.card : ℂ) * (B.card : ℂ))

/-- The coefficient agrees with expectation on the full Cartesian sample
space. In particular, equal products are counted with their multiplicities. -/
theorem normalizedProductCoeff_eq_uniform_expect
    (ψ : AddChar (ZMod p) ℂ) (A B : Finset (ZMod p)) (r : ZMod p) :
    normalizedProductCoeff ψ A B r =
      𝔼 z : A × B, ψ (r * (z.1 : ZMod p) * (z.2 : ZMod p)) := by
  classical
  rw [Fintype.expect_eq_sum_div_card]
  have hsum : (∑ z : A × B,
      ψ (r * (z.1 : ZMod p) * (z.2 : ZMod p))) = bilinearSum ψ A B r := by
    rw [Fintype.sum_prod_type]
    calc
      _ = ∑ a : A, ∑ b ∈ B, ψ (r * (a : ZMod p) * b) := by
        apply Finset.sum_congr rfl
        intro a ha
        exact Finset.sum_coe_sort B (fun b => ψ (r * (a : ZMod p) * b))
      _ = _ := Finset.sum_coe_sort A (fun a => ∑ b ∈ B, ψ (r * a * b))
  rw [hsum]
  simp only [normalizedProductCoeff, Fintype.card_prod, Fintype.card_coe, Nat.cast_mul]

/-- Additive-character orthogonality makes the full-field energy exact. -/
theorem bilinear_energy (ψ : AddChar (ZMod p) ℂ) (hψ : ψ.IsPrimitive)
    (B : Finset (ZMod p)) (r : ZMod p) (hr : r ≠ 0) :
    (∑ a : ZMod p, ‖∑ b ∈ B, ψ (r * a * b)‖ ^ 2) =
      (p : ℝ) * (B.card : ℝ) := by
  classical
  apply Complex.ofReal_injective
  calc
    ((∑ a : ZMod p, ‖∑ b ∈ B, ψ (r * a * b)‖ ^ 2 : ℝ) : ℂ) =
        ∑ a : ZMod p, (∑ b ∈ B, ψ (r * a * b)) *
          conj (∑ b ∈ B, ψ (r * a * b)) := by
      simp only [Complex.ofReal_sum, ← Complex.normSq_eq_norm_sq, Complex.mul_conj]
    _ = ∑ a : ZMod p, ∑ b ∈ B, ∑ c ∈ B,
        ψ (a * (r * (b - c))) := by
      simp only [map_sum, Finset.sum_mul_sum]
      apply Finset.sum_congr rfl
      intro a ha
      apply Finset.sum_congr rfl
      intro b hb
      apply Finset.sum_congr rfl
      intro c hc
      rw [← ψ.map_neg_eq_conj, ← ψ.map_add_eq_mul]
      congr 1
      ring
    _ = ∑ b ∈ B, ∑ c ∈ B, ∑ a : ZMod p,
        ψ (a * (r * (b - c))) := by
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro b hb
      rw [Finset.sum_comm]
    _ = ∑ b ∈ B, ∑ c ∈ B, if b = c then (p : ℂ) else 0 := by
      simp [AddChar.sum_mulShift _ hψ, hr, mul_eq_zero, sub_eq_zero, ZMod.card]
    _ = (((p : ℝ) * (B.card : ℝ) : ℝ) : ℂ) := by
      simp [Finset.sum_ite_eq, mul_comm]

/-- The squared rectangular bilinear bound, without square roots or
nonemptiness hypotheses. -/
theorem bilinearSum_norm_sq_le (ψ : AddChar (ZMod p) ℂ) (hψ : ψ.IsPrimitive)
    (A B : Finset (ZMod p)) (r : ZMod p) (hr : r ≠ 0) :
    ‖bilinearSum ψ A B r‖ ^ 2 ≤
      (A.card : ℝ) * (p : ℝ) * (B.card : ℝ) := by
  classical
  let T : ZMod p → ℂ := fun a => ∑ b ∈ B, ψ (r * a * b)
  have hnorm : ‖∑ a ∈ A, T a‖ ≤ ∑ a ∈ A, ‖T a‖ := norm_sum_le _ _
  have hsum_nonneg : 0 ≤ ∑ a ∈ A, ‖T a‖ :=
    Finset.sum_nonneg fun _ _ => norm_nonneg _
  have hcs : (∑ a ∈ A, ‖T a‖) ^ 2 ≤
      (A.card : ℝ) * ∑ a ∈ A, ‖T a‖ ^ 2 := by
    simpa using Finset.sum_mul_sq_le_sq_mul_sq A
      (fun _ : ZMod p => (1 : ℝ)) (fun a => ‖T a‖)
  have henergy : (∑ a ∈ A, ‖T a‖ ^ 2) ≤
      (p : ℝ) * (B.card : ℝ) := by
    calc
      _ ≤ ∑ a : ZMod p, ‖T a‖ ^ 2 :=
        Finset.sum_le_univ_sum_of_nonneg fun _ => sq_nonneg _
      _ = _ := bilinear_energy ψ hψ B r hr
  calc
    ‖bilinearSum ψ A B r‖ ^ 2 = ‖∑ a ∈ A, T a‖ ^ 2 := rfl
    _ ≤ (∑ a ∈ A, ‖T a‖) ^ 2 := by nlinarith [norm_nonneg (∑ a ∈ A, T a)]
    _ ≤ (A.card : ℝ) * ∑ a ∈ A, ‖T a‖ ^ 2 := hcs
    _ ≤ (A.card : ℝ) * ((p : ℝ) * (B.card : ℝ)) :=
      mul_le_mul_of_nonneg_left henergy (Nat.cast_nonneg _)
    _ = _ := by ring

/-- The unnormalized rectangular estimate. -/
theorem bilinearSum_norm_le_sqrt (ψ : AddChar (ZMod p) ℂ) (hψ : ψ.IsPrimitive)
    (A B : Finset (ZMod p)) (r : ZMod p) (hr : r ≠ 0) :
    ‖bilinearSum ψ A B r‖ ≤
      Real.sqrt ((A.card : ℝ) * (p : ℝ) * (B.card : ℝ)) := by
  apply (Real.le_sqrt (norm_nonneg _) (by positivity)).2
  exact bilinearSum_norm_sq_le ψ hψ A B r hr

/-- The normalized rectangular estimate. -/
theorem normalizedProductCoeff_norm_le_sqrt
    (ψ : AddChar (ZMod p) ℂ) (hψ : ψ.IsPrimitive)
    (A B : Finset (ZMod p)) (hA : A.Nonempty) (hB : B.Nonempty)
    (r : ZMod p) (hr : r ≠ 0) :
    ‖normalizedProductCoeff ψ A B r‖ ≤
      Real.sqrt ((p : ℝ) / ((A.card : ℝ) * (B.card : ℝ))) := by
  have ha : (0 : ℝ) < A.card := by exact_mod_cast hA.card_pos
  have hb : (0 : ℝ) < B.card := by exact_mod_cast hB.card_pos
  have hd : (0 : ℝ) < (A.card : ℝ) * (B.card : ℝ) := mul_pos ha hb
  rw [normalizedProductCoeff, norm_div, norm_mul,
    Complex.norm_natCast, Complex.norm_natCast]
  apply (Real.le_sqrt (by positivity) (by positivity)).2
  rw [div_pow]
  apply (div_le_iff₀ (pow_pos hd 2)).2
  have heq : ((p : ℝ) / ((A.card : ℝ) * (B.card : ℝ))) *
      ((A.card : ℝ) * (B.card : ℝ)) ^ 2 =
      (A.card : ℝ) * (p : ℝ) * (B.card : ℝ) := by
    field_simp
  rw [heq]
  exact bilinearSum_norm_sq_le ψ hψ A B r hr

/-- The normalized estimate when both samples use the same finite set. -/
theorem normalizedProductCoeff_self_norm_le
    (ψ : AddChar (ZMod p) ℂ) (hψ : ψ.IsPrimitive)
    (H : Finset (ZMod p)) (hH : H.Nonempty)
    (r : ZMod p) (hr : r ≠ 0) :
    ‖normalizedProductCoeff ψ H H r‖ ≤ Real.sqrt (p : ℝ) / (H.card : ℝ) := by
  have h := normalizedProductCoeff_norm_le_sqrt ψ hψ H H hH hH r hr
  have hcard : (0 : ℝ) ≤ H.card := Nat.cast_nonneg _
  simpa [← pow_two, Real.sqrt_div, Real.sqrt_sq hcard] using h

/-- The zero-frequency coefficient is one. -/
theorem normalizedProductCoeff_zero (ψ : AddChar (ZMod p) ℂ)
    (A B : Finset (ZMod p)) (hA : A.Nonempty) (hB : B.Nonempty) :
    normalizedProductCoeff ψ A B 0 = 1 := by
  have ha : (A.card : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hA.card_ne_zero
  have hb : (B.card : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hB.card_ne_zero
  simp [normalizedProductCoeff, bilinearSum, nsmul_eq_mul, ha, hb]

end FiniteFieldMixing
