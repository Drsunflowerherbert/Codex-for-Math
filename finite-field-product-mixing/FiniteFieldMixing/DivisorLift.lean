import FiniteFieldMixing.Mixing

/-!
# Lifting four products to positive divisors

The covering theorem at residue zero gives a positive integral multiple of the
prime when the residue set is the image of positive divisors.
-/

noncomputable section
open scoped BigOperators

namespace FiniteFieldMixing

variable {p : ℕ} [Fact p.Prime]

/-- Lift the residue-zero covering witness through an arbitrary finite set of
natural numbers. -/
theorem four_product_nat_lift (D : Finset ℕ)
    (hsize : p ^ 3 ≤ (D.image (Nat.cast : ℕ → ZMod p)).card ^ 4) :
    ∃ a b : Fin 4 → ℕ,
      (∀ i, a i ∈ D) ∧ (∀ i, b i ∈ D) ∧ p ∣ ∑ i, a i * b i := by
  classical
  obtain ⟨a₀, b₀, ha₀, hb₀, hsum⟩ :=
    four_products_cover (D.image (Nat.cast : ℕ → ZMod p)) hsize 0
  have ha_lift : ∀ i, ∃ a : ℕ, a ∈ D ∧ (a : ZMod p) = a₀ i := by
    intro i
    exact Finset.mem_image.mp (ha₀ i)
  have hb_lift : ∀ i, ∃ b : ℕ, b ∈ D ∧ (b : ZMod p) = b₀ i := by
    intro i
    exact Finset.mem_image.mp (hb₀ i)
  choose a haD ha_cast using ha_lift
  choose b hbD hb_cast using hb_lift
  refine ⟨a, b, haD, hbD, ?_⟩
  apply (ZMod.natCast_eq_zero_iff _ p).mp
  push_cast
  simpa only [ha_cast, hb_cast] using hsum

/-- A dense residue image of positive divisors yields four positive products
whose sum is a positive multiple of the prime. Every product divides `Q²`. -/
theorem divisor_four_product_lift (Q : ℕ) (_hQ : 0 < Q) (D : Finset ℕ)
    (hD : ∀ d ∈ D, 0 < d ∧ d ∣ Q)
    (hsize : p ^ 3 ≤ (D.image (Nat.cast : ℕ → ZMod p)).card ^ 4) :
    ∃ (a b : Fin 4 → ℕ) (m : ℕ),
      (∀ i, a i ∈ D) ∧ (∀ i, b i ∈ D) ∧ 0 < m ∧
      (∑ i, a i * b i = p * m) ∧ (∀ i, a i * b i ∣ Q ^ 2) := by
  obtain ⟨a, b, ha, hb, hdiv⟩ := four_product_nat_lift D hsize
  obtain ⟨m, hsum⟩ := hdiv
  have hsum_pos : 0 < ∑ i, a i * b i := by
    apply Finset.sum_pos
    · intro i _
      exact Nat.mul_pos (hD (a i) (ha i)).1 (hD (b i) (hb i)).1
    · exact Finset.univ_nonempty
  have hm : 0 < m := by
    by_contra hm
    have hm_zero : m = 0 := Nat.eq_zero_of_not_pos hm
    simp [hsum, hm_zero] at hsum_pos
  refine ⟨a, b, m, ha, hb, hm, hsum, ?_⟩
  intro i
  simpa only [pow_two] using mul_dvd_mul (hD (a i) (ha i)).2 (hD (b i) (hb i)).2

/-- Divide the integral four-product identity by its positive multiplier. -/
theorem rational_lift_four_products (a b : Fin 4 → ℕ) (p m : ℕ)
    (hm : 0 < m) (hs : ∑ i, a i * b i = p * m) :
    (p : ℚ) = ∑ i, ((a i * b i : ℕ) : ℚ) / (m : ℚ) := by
  have hmQ : (m : ℚ) ≠ 0 := by exact_mod_cast Nat.ne_of_gt hm
  have hsQ : (∑ i, ((a i * b i : ℕ) : ℚ)) = (p : ℚ) * (m : ℚ) := by
    exact_mod_cast hs
  rw [← Finset.sum_div, hsQ]
  exact (mul_div_cancel_right₀ (p : ℚ) hmQ).symm

/-- The local rational identity provided by a dense image of positive divisors.
The four factors and products may repeat. -/
theorem divisor_four_product_rational_lift (Q : ℕ) (hQ : 0 < Q) (D : Finset ℕ)
    (hD : ∀ d ∈ D, 0 < d ∧ d ∣ Q)
    (hsize : p ^ 3 ≤ (D.image (Nat.cast : ℕ → ZMod p)).card ^ 4) :
    ∃ (a b : Fin 4 → ℕ) (m : ℕ),
      (∀ i, a i ∈ D) ∧ (∀ i, b i ∈ D) ∧ 0 < m ∧
      (∑ i, a i * b i = p * m) ∧ (∀ i, a i * b i ∣ Q ^ 2) ∧
      (p : ℚ) = ∑ i, ((a i * b i : ℕ) : ℚ) / (m : ℚ) := by
  obtain ⟨a, b, m, ha, hb, hm, hsum, hprod⟩ :=
    divisor_four_product_lift Q hQ D hD hsize
  exact ⟨a, b, m, ha, hb, hm, hsum, hprod, rational_lift_four_products a b p m hm hsum⟩

end FiniteFieldMixing
