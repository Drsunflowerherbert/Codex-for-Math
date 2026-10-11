import Egyptian.PaddingArithmetic

namespace Egyptian

/-- A prime second-largest denominator rules out both possible marker collisions. -/
theorem prime_collision_obstruction {d M : ℕ} {t : List ℕ}
    (hd : 3 ≤ d)
    (hp : ∀ r ∈ d :: M :: t, 0 < r)
    (hv : reciprocalSum (d :: M :: t) = 1)
    (ht : ∀ r ∈ t, r < d)
    (hM : M = d + 1 ∨ M = d * (d + 1)) : ¬d.Prime := by
  intro hprime
  have hnotA : ¬d ∣ t.prod := by
    apply hprime.prime.not_dvd_prod
    intro r hr
    exact Nat.not_dvd_of_pos_of_lt (hp r (by simp [hr])) (ht r hr)
  have he := commonNumerator_eq_prod hp hv
  change M * t.prod + d * (t.prod + M * commonNumerator t) =
    d * (M * t.prod) at he
  rcases hM with rfl | rfl
  · have htotal : d ∣ (d + 1) * t.prod +
        d * (t.prod + (d + 1) * commonNumerator t) :=
      he.symm ▸ dvd_mul_right d ((d + 1) * t.prod)
    have hpart : d ∣ (d + 1) * t.prod :=
      (Nat.dvd_add_left (dvd_mul_right d
        (t.prod + (d + 1) * commonNumerator t))).mp htotal
    apply hnotA
    apply (Nat.dvd_add_right (dvd_mul_right d t.prod)).mp
    convert hpart using 1; ring
  · have hcancel : ((d + 1) * t.prod + t.prod) +
        d * (d + 1) * commonNumerator t = d * (d + 1) * t.prod := by
      apply Nat.eq_of_mul_eq_mul_left (n := d) (by omega)
      calc
        d * (((d + 1) * t.prod + t.prod) +
            d * (d + 1) * commonNumerator t) =
            d * (d + 1) * t.prod +
              d * (t.prod + d * (d + 1) * commonNumerator t) := by ring
        _ = d * (d * (d + 1) * t.prod) := he
    have hterm : d ∣ d * (d + 1) * commonNumerator t := by
      exact ⟨(d + 1) * commonNumerator t, by ring⟩
    have htotal : d ∣ ((d + 1) * t.prod + t.prod) +
        d * (d + 1) * commonNumerator t := by
      rw [hcancel]
      exact ⟨(d + 1) * t.prod, by ring⟩
    have hpart : d ∣ (d + 1) * t.prod + t.prod :=
      (Nat.dvd_add_left hterm).mp htotal
    have htwo : d ∣ 2 * t.prod := by
      apply (Nat.dvd_add_right (dvd_mul_right d t.prod)).mp
      convert hpart using 1; ring
    rcases hprime.dvd_mul.mp htwo with htwo | hA
    · exact Nat.not_dvd_of_pos_of_lt (by decide : 0 < (2 : ℕ)) (by omega) htwo
    · exact hnotA hA

end Egyptian
