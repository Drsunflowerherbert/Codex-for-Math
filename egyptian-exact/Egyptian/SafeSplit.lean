import Egyptian.PaddingArithmetic

namespace Egyptian

theorem safe_split {d u v : ℕ} {t : List ℕ}
    (hp : ∀ r ∈ d :: t, 0 < r) (hn : (d :: t).Nodup)
    (hu : 0 < u) (hv : 0 < v) (huv : u ≠ v)
    (hut : u ∉ t) (hvt : v ∉ t)
    (he : (d : ℝ)⁻¹ = (u : ℝ)⁻¹ + (v : ℝ)⁻¹) :
    (∀ r ∈ u :: v :: t, 0 < r) ∧ (u :: v :: t).Nodup ∧
      (u :: v :: t).length = (d :: t).length + 1 ∧
      reciprocalSum (u :: v :: t) = reciprocalSum (d :: t) := by
  refine ⟨?_, ?_, by simp, ?_⟩
  · intro r hr
    rcases List.mem_cons.mp hr with rfl | hr
    · exact hu
    rcases List.mem_cons.mp hr with rfl | hr
    · exact hv
    · exact hp r (by simp [hr])
  · apply List.nodup_cons.mpr
    refine ⟨by simp [huv, hut], List.nodup_cons.mpr ⟨hvt, hn.tail⟩⟩
  · simp only [reciprocalSum_cons]
    linarith

theorem denominator_ge_two_of_one {l : List ℕ} (hp : ∀ d ∈ l, 0 < d)
    (hlen : 2 ≤ l.length) (hv : reciprocalSum l = 1) {d : ℕ} (hd : d ∈ l) :
    2 ≤ d := by
  by_contra h
  have hd1 : d = 1 := by have := hp d hd; omega
  have hperm := List.perm_cons_erase hd
  have htpos : ∀ r ∈ l.erase d, 0 < r := fun r hr =>
    hp r (hperm.mem_iff.mpr (by simp [hr]))
  have htne : l.erase d ≠ [] := by
    intro he
    have heq := hperm.length_eq
    simp [he] at heq
    omega
  have ht := reciprocalSum_pos htpos htne
  rw [reciprocalSum_perm hperm, hd1, reciprocalSum_cons] at hv
  rw [hd1] at ht
  norm_num at hv
  linarith

/-- A split of the second largest denominator that avoids the retained maximum.
Only the two possible ordinary-split collisions require a composite factor repair. -/
theorem padding_pair (d M : ℕ) (hd : 3 ≤ d) (hdM : d < M)
    (hc : M = d + 1 ∨ M = d * (d + 1) → ¬d.Prime) :
    ∃ u v : ℕ, d < u ∧ u < v ∧ u ≠ M ∧ v ≠ M ∧
      u ≤ M * (M + 1) ∧ v ≤ M * (M + 1) ∧
      (d : ℝ)⁻¹ = (u : ℝ)⁻¹ + (v : ℝ)⁻¹ := by
  by_cases hcollision : M = d + 1 ∨ M = d * (d + 1)
  · obtain ⟨a, b, had, hbd, hab⟩ := (Nat.not_prime_iff_exists_mul_eq (by omega : 2 ≤ d)).mp
      (hc hcollision)
    have ha2 : 2 ≤ a := by
      by_contra h
      have : a = 0 ∨ a = 1 := by omega
      rcases this with rfl | rfl <;> simp at hab <;> omega
    have hb2 : 2 ≤ b := by
      by_contra h
      have : b = 0 ∨ b = 1 := by omega
      rcases this with rfl | rfl <;> simp at hab <;> omega
    have hu : d < a * (b + 1) := by nlinarith
    have huv : a * (b + 1) < d * (b + 1) := by
      apply Nat.mul_lt_mul_of_pos_right
      · exact had
      · omega
    have hvbound : d * (b + 1) ≤ M * (M + 1) :=
      Nat.mul_le_mul (by omega) (by omega)
    have hum : a * (b + 1) ≠ M ∧ d * (b + 1) ≠ M := by
      rcases hcollision with hM | hM
      · have huM : M < a * (b + 1) := by rw [hM]; nlinarith
        exact ⟨ne_of_gt huM, ne_of_gt (lt_trans huM huv)⟩
      · have hvM : d * (b + 1) < M := by
          rw [hM]
          exact Nat.mul_lt_mul_of_pos_left (by omega) (by omega)
        exact ⟨ne_of_lt (lt_trans huv hvM), ne_of_lt hvM⟩
    refine ⟨a * (b + 1), d * (b + 1), hu, huv, hum.1, hum.2,
      le_trans (le_of_lt huv) hvbound, hvbound, ?_⟩
    simpa only [hab] using factor_split_identity a b (by omega) (by omega)
  · have huv : d + 1 < d * (d + 1) := by nlinarith
    have hvbound : d * (d + 1) ≤ M * (M + 1) := Nat.mul_le_mul (by omega) (by omega)
    exact ⟨d + 1, d * (d + 1), by omega, huv,
      (fun h => hcollision (Or.inl h.symm)),
      (fun h => hcollision (Or.inr h.symm)),
      le_trans (le_of_lt huv) hvbound, hvbound, unit_split_identity d (by omega)⟩

end Egyptian
