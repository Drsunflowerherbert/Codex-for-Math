import Egyptian.Cleanup

namespace Egyptian

theorem two_positive_denominators_sum_one {a b : ℕ} (ha : 0 < a) (hb : 0 < b)
    (he : (a : ℝ)⁻¹ + (b : ℝ)⁻¹ = 1) : a = 2 ∧ b = 2 := by
  have haR : 0 < (a : ℝ) := Nat.cast_pos.mpr ha
  have hbR : 0 < (b : ℝ) := Nat.cast_pos.mpr hb
  have ha2 : 2 ≤ a := by
    by_contra h
    have : a = 1 := by omega
    subst a
    norm_num at he
    have := inv_pos.mpr hbR
    linarith
  have hb2 : 2 ≤ b := by
    by_contra h
    have : b = 1 := by omega
    subst b
    norm_num at he
    have := inv_pos.mpr haR
    linarith
  have heprod : (a : ℝ) + (b : ℝ) = (a : ℝ) * (b : ℝ) := by
    field_simp [ne_of_gt haR, ne_of_gt hbR] at he
    nlinarith
  have ha2R : (2 : ℝ) ≤ a := by exact_mod_cast ha2
  have hb2R : (2 : ℝ) ≤ b := by exact_mod_cast hb2
  have hprod := mul_nonneg (sub_nonneg.mpr ha2R) (sub_nonneg.mpr hb2R)
  have hab : (a : ℝ) + (b : ℝ) ≤ 4 := by nlinarith
  constructor
  · exact_mod_cast (show (a : ℝ) = 2 by linarith)
  · exact_mod_cast (show (b : ℝ) = 2 by linarith)

/-- There is no distinct positive length-two representation of one. -/
theorem no_distinct_two_term_one :
    ¬ ∃ l : List ℕ, (∀ d ∈ l, 0 < d) ∧ l.Nodup ∧ l.length = 2 ∧ reciprocalSum l = 1 := by
  rintro ⟨l, hp, hn, hlen, he⟩
  rcases l with _ | ⟨a, l⟩
  · simp at hlen
  rcases l with _ | ⟨b, l⟩
  · simp at hlen
  have ht : l = [] := List.length_eq_zero_iff.mp (by simpa using hlen)
  subst l
  have ha : 0 < a := hp a (by simp)
  have hb : 0 < b := hp b (by simp)
  have he' : (a : ℝ)⁻¹ + (b : ℝ)⁻¹ = 1 := by simpa using he
  obtain ⟨rfl, rfl⟩ := two_positive_denominators_sum_one ha hb he'
  simp at hn

/-- The original duplicate input [2,2] satisfies the boundary value, but admits no
positive distinct representation with its length and value. -/
theorem boundary_counterexample :
    (∀ d ∈ ([2, 2] : List ℕ), 0 < d) ∧
      reciprocalSum [2, 2] = 1 ∧
      ¬ ∃ out : List ℕ, (∀ d ∈ out, 0 < d) ∧ out.Nodup ∧
        out.length = ([2, 2] : List ℕ).length ∧ reciprocalSum out = reciprocalSum [2, 2] := by
  have hx : reciprocalSum [2, 2] = 1 := by norm_num [reciprocalSum]
  refine ⟨by simp, hx, ?_⟩
  simpa only [List.length_cons, List.length_nil, hx] using no_distinct_two_term_one

end Egyptian
