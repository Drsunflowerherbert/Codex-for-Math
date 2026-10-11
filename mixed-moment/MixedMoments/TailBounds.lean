import MixedMoments.Series

/-! Quantified analytic tail bounds from exact moment recurrences. -/

namespace MixedMoments.Series
open Filter Finset
open scoped Topology

private theorem add_ratio_le_max {A B x : ℝ} (hB : 0 < B) (hx : 0 ≤ x) :
    (A + x) / (B + x) ≤ max 1 (A / B) := by
  have hden : 0 < B + x := by linarith
  by_cases h : A ≤ B
  · apply le_trans _ (le_max_left _ _)
    apply (div_le_one hden).mpr
    linarith
  · apply le_trans _ (le_max_right _ _)
    apply (div_le_div_iff₀ hden hB).mpr
    nlinarith

theorem momentSeries_upper_bound (a : ℕ → ℝ)
    (hnonneg : ∀ n, 0 ≤ a n)
    (hrec : ∀ n : ℕ, ((n : ℝ) + 3) * a (n + 2) = ((n : ℝ) + 2) * a n)
    (hzero : Tendsto a atTop (𝓝 0)) (k j : ℕ) :
    momentSeries a (k + 2) j ≤
      max 1 (((k : ℝ) + 2) / ((j : ℝ) + 1)) * (a k + a (k + 1)) := by
  let C : ℝ := max 1 (((k : ℝ) + 2) / ((j : ℝ) + 1))
  have hterm (u : ℕ) :
      a (k + 2 + u) / ((j : ℝ) + u + 1) ≤
        C * (a (k + u) - a (k + (u + 2))) := by
    have ht := moment_div_index a hrec (k + u)
    have he : k + 2 + u = k + u + 2 := by omega
    have he' : k + (u + 2) = k + u + 2 := by omega
    rw [he, he', ← ht]
    push_cast
    have hq : (k : ℝ) + u + 2 ≠ 0 := by positivity
    have hid : a (k + u + 2) / ((j : ℝ) + u + 1) =
        (((k : ℝ) + 2 + u) / ((j : ℝ) + 1 + u)) *
          (a (k + u + 2) / ((k : ℝ) + u + 2)) := by
      field_simp
      ring
    rw [hid]
    apply mul_le_mul_of_nonneg_right
    · exact add_ratio_le_max (by positivity) (Nat.cast_nonneg u)
    · exact div_nonneg (hnonneg _) (by positivity)
  have hdiff : Summable (fun u => a (k + u) - a (k + (u + 2))) := by
    have hs := summable_momentSeries a hnonneg hrec (k + 2) (k + 1)
    convert hs using 1
    ext u
    rw [show k + (u + 2) = k + u + 2 by omega, ← moment_div_index a hrec (k + u)]
    congr 1 <;> simp [add_comm, add_left_comm, add_assoc] <;> norm_num
  have hz : Tendsto (fun u => a (k + u)) atTop (𝓝 0) := by
    simpa only [Nat.add_comm] using hzero.comp (tendsto_add_atTop_nat k)
  have htel := tsum_two_step_telescope (fun u => a (k + u)) hz hdiff
  have hle := (summable_momentSeries a hnonneg hrec (k + 2) j).tsum_le_tsum hterm
    (hdiff.mul_left C)
  rw [tsum_mul_left, htel] at hle
  simpa only [momentSeries, Nat.add_zero] using hle

theorem momentSeries_tail (a : ℕ → ℝ)
    (hnonneg : ∀ n, 0 ≤ a n)
    (hrec : ∀ n : ℕ, ((n : ℝ) + 3) * a (n + 2) = ((n : ℝ) + 2) * a n)
    (i j N : ℕ) :
    momentSeries a i j - (∑ u ∈ range N, a (i + u) / ((j : ℝ) + u + 1)) =
      momentSeries a (i + N) (j + N) := by
  have h := (summable_momentSeries a hnonneg hrec i j).sum_add_tsum_nat_add N
  have he : (∑' u : ℕ, a (i + (u + N)) / ((j : ℝ) + (u + N : ℕ) + 1)) =
      momentSeries a (i + N) (j + N) := by
    apply tsum_congr
    intro u
    simp [add_comm, add_left_comm, add_assoc]
  rw [he] at h
  unfold momentSeries at *
  linarith

/-- The source's rational tail estimate, in the range avoiding negative indices.
The extra case `i+N=1` needs the separate `a(-1)=0` convention and `a(1)=0`. -/
theorem momentSeries_tail_bound (a : ℕ → ℝ)
    (hnonneg : ∀ n, 0 ≤ a n)
    (hrec : ∀ n : ℕ, ((n : ℝ) + 3) * a (n + 2) = ((n : ℝ) + 2) * a n)
    (hzero : Tendsto a atTop (𝓝 0)) (i j N : ℕ) (hN : 2 ≤ i + N) :
    let tail := momentSeries a i j - (∑ u ∈ range N, a (i + u) / ((j : ℝ) + u + 1))
    0 ≤ tail ∧ tail ≤
      max 1 (((i + N : ℕ) : ℝ) / (((j + N : ℕ) : ℝ) + 1)) *
        (a (i + N - 2) + a (i + N - 1)) := by
  dsimp only
  rw [momentSeries_tail a hnonneg hrec]
  constructor
  · exact tsum_nonneg (fun u => div_nonneg (hnonneg _) (by positivity))
  · have h := momentSeries_upper_bound a hnonneg hrec hzero (i + N - 2) (j + N)
    have hk : i + N - 2 + 2 = i + N := by omega
    have hk' : i + N - 2 + 1 = i + N - 1 := by omega
    have hcast : ((i + N - 2 : ℕ) : ℝ) + 2 = ((i + N : ℕ) : ℝ) := by
      exact_mod_cast hk
    simpa only [hk, hk', hcast] using h

end MixedMoments.Series
