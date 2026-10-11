import Mathlib

/-!
# Recurrences for convergent moment series

These results concern actual real infinite sums, not integrals. Every required
summability and moment-decay hypothesis is explicit. An integral instantiation
must separately prove its series representation and these hypotheses.
-/

namespace MixedMoments.Series

open Filter Finset
open scoped Topology

noncomputable def momentSeries (a : ℕ → ℝ) (i j : ℕ) : ℝ :=
  ∑' u : ℕ, a (i + u) / ((j : ℝ) + u + 1)

theorem momentSeries_diagonal (a : ℕ → ℝ) (i j : ℕ)
    (hs : Summable (fun u : ℕ => a (i + u) / ((j : ℝ) + u + 1))) :
    momentSeries a i j - momentSeries a (i + 1) (j + 1) = a i / ((j : ℝ) + 1) := by
  have h := hs.tsum_eq_zero_add
  have heq : (∑' u : ℕ, a (i + (u + 1)) / ((j : ℝ) + (u + 1 : ℕ) + 1)) =
      momentSeries a (i + 1) (j + 1) := by
    apply tsum_congr
    intro u
    simp [add_left_comm, add_comm]
  simp only [Nat.cast_zero, add_zero] at h
  rw [heq] at h
  exact sub_eq_iff_eq_add.mpr (by simpa [momentSeries, add_comm] using h)

theorem finite_two_step_telescope (f : ℕ → ℝ) (N : ℕ) :
    ∑ n ∈ range N, (f n - f (n + 2)) = f 0 + f 1 - f N - f (N + 1) := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [sum_range_succ, ih]
    ring

theorem tsum_two_step_telescope (f : ℕ → ℝ)
    (hzero : Tendsto f atTop (𝓝 0))
    (hs : Summable (fun n => f n - f (n + 2))) :
    ∑' n, (f n - f (n + 2)) = f 0 + f 1 := by
  have hshift : Tendsto (fun n => f (n + 1)) atTop (𝓝 0) :=
    hzero.comp (tendsto_add_atTop_nat 1)
  have hlim : Tendsto (fun N => f 0 + f 1 - f N - f (N + 1))
      atTop (𝓝 (f 0 + f 1 - 0 - 0)) :=
    (tendsto_const_nhds.sub hzero).sub hshift
  have hlim' : Tendsto (fun N => ∑ n ∈ range N, (f n - f (n + 2)))
      atTop (𝓝 (f 0 + f 1)) := by
    simpa only [finite_two_step_telescope, sub_zero] using hlim
  exact tendsto_nhds_unique hs.tendsto_sum_tsum_nat hlim'

theorem minus_boundary_term (a : ℕ → ℝ)
    (hrec : ∀ n : ℕ, ((n : ℝ) + 3) * a (n + 2) = ((n : ℝ) + 2) * a n)
    (d u : ℕ) :
    ((d : ℝ) + 2) * (a (d + 2 + u) / ((u : ℝ) + 1)) -
      ((d : ℝ) + 1) * (a (d + u) / ((u : ℝ) + 1)) =
      a (d + u) - a (d + (u + 2)) := by
  have hr := hrec (d + u)
  simp only [Nat.cast_add] at hr
  have hne : (u : ℝ) + 1 ≠ 0 := by positivity
  have he : d + 2 + u = d + u + 2 := by omega
  have he' : d + (u + 2) = d + u + 2 := by omega
  rw [he, he']
  field_simp
  nlinarith [hr]

/-- The minus-boundary recurrence follows from the moment recurrence, decay,
and summability. No boundary constant evaluation is assumed or concluded. -/
theorem minus_boundary_recurrence (a : ℕ → ℝ)
    (hrec : ∀ n : ℕ, ((n : ℝ) + 3) * a (n + 2) = ((n : ℝ) + 2) * a n)
    (hzero : Tendsto a atTop (𝓝 0)) (d : ℕ)
    (hs0 : Summable (fun u : ℕ => a (d + u) / ((u : ℝ) + 1)))
    (hs2 : Summable (fun u : ℕ => a (d + 2 + u) / ((u : ℝ) + 1))) :
    ((d : ℝ) + 2) * momentSeries a (d + 2) 0 =
      ((d : ℝ) + 1) * momentSeries a d 0 + a d + a (d + 1) := by
  have ht : ∀ u, ((d : ℝ) + 2) * (a (d + 2 + u) / ((u : ℝ) + 1)) -
      ((d : ℝ) + 1) * (a (d + u) / ((u : ℝ) + 1)) =
      a (d + u) - a (d + (u + 2)) := minus_boundary_term a hrec d
  have hs : Summable (fun u => a (d + u) - a (d + (u + 2))) := by
    simpa only [ht] using (hs2.mul_left ((d : ℝ) + 2)).sub
      (hs0.mul_left ((d : ℝ) + 1))
  have hz : Tendsto (fun u => a (d + u)) atTop (𝓝 0) := by
    simpa only [Nat.add_comm] using hzero.comp (tendsto_add_atTop_nat d)
  have htel := tsum_two_step_telescope (fun u => a (d + u)) hz hs
  have hsum : (∑' u : ℕ, (((d : ℝ) + 2) * (a (d + 2 + u) / ((u : ℝ) + 1)) -
      ((d : ℝ) + 1) * (a (d + u) / ((u : ℝ) + 1)))) = a d + a (d + 1) := by
    simpa only [ht, Nat.add_zero] using htel
  rw [Summable.tsum_sub (hs2.mul_left _) (hs0.mul_left _), tsum_mul_left, tsum_mul_left] at hsum
  simp only [momentSeries, Nat.cast_zero, zero_add]
  linarith

theorem plus_boundary_term (a : ℕ → ℝ)
    (hrec : ∀ n : ℕ, ((n : ℝ) + 3) * a (n + 2) = ((n : ℝ) + 2) * a n)
    (d u : ℕ) :
    ((d : ℝ) + 1) * (a u / ((d : ℝ) + u + 3)) -
      (d : ℝ) * (a (u + 2) / ((d : ℝ) + u + 3)) = a u - a (u + 2) := by
  have hr := hrec u
  have hne : (d : ℝ) + u + 3 ≠ 0 := by positivity
  field_simp
  nlinarith [hr]

theorem momentSeries_shift_two (a : ℕ → ℝ) (d : ℕ)
    (hs : Summable (fun u : ℕ => a u / ((d : ℝ) + u + 1))) :
    momentSeries a 0 d = a 0 / ((d : ℝ) + 1) + a 1 / ((d : ℝ) + 2) +
      momentSeries a 2 (d + 2) := by
  have h := hs.sum_add_tsum_nat_add 2
  have heq : (∑' u : ℕ, a (u + 2) / ((d : ℝ) + (u + 2 : ℕ) + 1)) =
      momentSeries a 2 (d + 2) := by
    apply tsum_congr
    intro u
    simp [add_comm, add_left_comm]
  rw [heq] at h
  convert h.symm using 1 <;>
    norm_num [momentSeries, Finset.sum_range_succ, add_assoc, add_comm, add_left_comm]

/-- At d=0 the previous even plus-boundary value has zero coefficient.
The two series summability hypotheses are necessary premises, not definitions. -/
theorem plus_boundary_recurrence (a : ℕ → ℝ)
    (hrec : ∀ n : ℕ, ((n : ℝ) + 3) * a (n + 2) = ((n : ℝ) + 2) * a n)
    (hzero : Tendsto a atTop (𝓝 0))
    (ha0 : a 0 = 2) (ha1 : a 1 = 0) (d : ℕ)
    (hs0 : Summable (fun u : ℕ => a u / ((d : ℝ) + u + 1)))
    (hs2 : Summable (fun u : ℕ => a u / ((d : ℝ) + u + 3))) :
    ((d : ℝ) + 1) * momentSeries a 0 (d + 2) =
      (d : ℝ) * momentSeries a 0 d + 2 / ((d : ℝ) + 1) := by
  have hstail : Summable (fun u : ℕ => a (u + 2) / ((d : ℝ) + u + 3)) := by
    have h := (summable_nat_add_iff 2).mpr hs0
    convert h using 1
    ext u
    simp only [Nat.cast_add, Nat.cast_ofNat]
    congr 1; ring
  have ht := plus_boundary_term a hrec d
  have hs : Summable (fun u => a u - a (u + 2)) := by
    simpa only [ht] using (hs2.mul_left ((d : ℝ) + 1)).sub (hstail.mul_left (d : ℝ))
  have hsum : (∑' u : ℕ, (((d : ℝ) + 1) * (a u / ((d : ℝ) + u + 3)) -
      (d : ℝ) * (a (u + 2) / ((d : ℝ) + u + 3)))) = 2 := by
    simpa only [ht, ha0, ha1, add_zero] using tsum_two_step_telescope a hzero hs
  rw [Summable.tsum_sub (hs2.mul_left _) (hstail.mul_left _),
    tsum_mul_left, tsum_mul_left] at hsum
  have hshift := momentSeries_shift_two a d hs0
  have hm0 : momentSeries a 0 (d + 2) = ∑' u : ℕ, a u / ((d : ℝ) + u + 3) := by
    apply tsum_congr
    intro u
    simp [add_comm, add_left_comm, add_assoc]; norm_num
  have hm2 : momentSeries a 2 (d + 2) = ∑' u : ℕ, a (u + 2) / ((d : ℝ) + u + 3) := by
    apply tsum_congr
    intro u
    simp [add_comm, add_left_comm, add_assoc]; norm_num
  rw [hm0]
  rw [hm2, ha0, ha1, zero_div, add_zero] at hshift
  have hne : (d : ℝ) + 1 ≠ 0 := by positivity
  have hid : (d : ℝ) * (2 / ((d : ℝ) + 1)) + 2 / ((d : ℝ) + 1) = 2 := by
    field_simp
  nlinarith [hshift, hid]

theorem moment_div_index (a : ℕ → ℝ)
    (hrec : ∀ n : ℕ, ((n : ℝ) + 3) * a (n + 2) = ((n : ℝ) + 2) * a n)
    (n : ℕ) : a (n + 2) / ((n : ℝ) + 2) = a n - a (n + 2) := by
  have hr := hrec n
  have hne : (n : ℝ) + 2 ≠ 0 := by positivity
  field_simp
  nlinarith

/-- All the series converge from nonnegative basic moments and their recurrence.
The proof uses a finite telescoping majorant; no endpoint limit is used here. -/
theorem summable_momentSeries (a : ℕ → ℝ)
    (hnonneg : ∀ n, 0 ≤ a n)
    (hrec : ∀ n : ℕ, ((n : ℝ) + 3) * a (n + 2) = ((n : ℝ) + 2) * a n)
    (i j : ℕ) : Summable (fun u : ℕ => a (i + u) / ((j : ℝ) + u + 1)) := by
  have hdiff : Summable (fun u => a (i + u) - a (i + (u + 2))) := by
    apply summable_of_sum_range_le (c := a i + a (i + 1))
    · intro u
      have hr := moment_div_index a hrec (i + u)
      have hz : 0 ≤ a (i + u + 2) / (((i + u : ℕ) : ℝ) + 2) :=
        div_nonneg (hnonneg _) (by positivity)
      simpa only [Nat.add_assoc] using hr ▸ hz
    · intro N
      rw [finite_two_step_telescope (fun u => a (i + u))]
      simp only [Nat.add_zero]
      linarith [hnonneg (i + N), hnonneg (i + (N + 1))]
  have hmajor : ∀ u : ℕ,
      a (i + (u + 2)) / ((j : ℝ) + (u + 2 : ℕ) + 1) ≤
      ((i : ℝ) + 2) * (a (i + u) - a (i + (u + 2))) := by
    intro u
    have hr := moment_div_index a hrec (i + u)
    have he : i + (u + 2) = i + u + 2 := by omega
    rw [he, ← hr]
    push_cast
    have hA : 0 ≤ a (i + u + 2) := hnonneg _
    have hp : 0 < (j : ℝ) + (u + 2) + 1 := by positivity
    have hq : 0 < (i : ℝ) + u + 2 := by positivity
    have hratio : (i : ℝ) + u + 2 ≤ ((i : ℝ) + 2) * ((j : ℝ) + (u + 2) + 1) := by
      nlinarith [Nat.cast_nonneg (α := ℝ) i, Nat.cast_nonneg (α := ℝ) j,
        Nat.cast_nonneg (α := ℝ) u]
    apply (div_le_iff₀ hp).mpr
    rw [mul_assoc, div_mul_eq_mul_div, ← mul_div_assoc]
    apply (le_div_iff₀ hq).mpr
    nlinarith [mul_le_mul_of_nonneg_left hratio hA]
  have htail : Summable (fun u : ℕ => a (i + (u + 2)) / ((j : ℝ) + (u + 2 : ℕ) + 1)) :=
    (hdiff.mul_left ((i : ℝ) + 2)).of_nonneg_of_le
      (fun u => div_nonneg (hnonneg _) (by positivity)) hmajor
  exact (summable_nat_add_iff 2).mp htail

theorem momentSeries_adjacent (a : ℕ → ℝ)
    (hnonneg : ∀ n, 0 ≤ a n)
    (hrec : ∀ n : ℕ, ((n : ℝ) + 3) * a (n + 2) = ((n : ℝ) + 2) * a n)
    (hzero : Tendsto a atTop (𝓝 0)) (k : ℕ) :
    momentSeries a (k + 2) (k + 1) = a k + a (k + 1) := by
  have heq : ∀ u : ℕ,
      a (k + 2 + u) / (((k + 1 : ℕ) : ℝ) + u + 1) =
        a (k + u) - a (k + (u + 2)) := by
    intro u
    convert moment_div_index a hrec (k + u) using 1
    simp [add_comm, add_left_comm, add_assoc]
    norm_num
  have hs : Summable (fun u => a (k + u) - a (k + (u + 2))) := by
    simpa only [heq] using summable_momentSeries a hnonneg hrec (k + 2) (k + 1)
  have hz : Tendsto (fun u => a (k + u)) atTop (𝓝 0) := by
    simpa only [Nat.add_comm] using hzero.comp (tendsto_add_atTop_nat k)
  simpa only [momentSeries, heq, Nat.add_zero] using
    tsum_two_step_telescope (fun u => a (k + u)) hz hs

theorem momentSeries_one_zero (a : ℕ → ℝ)
    (hnonneg : ∀ n, 0 ≤ a n)
    (hrec : ∀ n : ℕ, ((n : ℝ) + 3) * a (n + 2) = ((n : ℝ) + 2) * a n)
    (hzero : Tendsto a atTop (𝓝 0)) (ha0 : a 0 = 2) (ha1 : a 1 = 0) :
    momentSeries a 1 0 = 2 := by
  have hd := momentSeries_diagonal a 1 0 (summable_momentSeries a hnonneg hrec 1 0)
  have ha := momentSeries_adjacent a hnonneg hrec hzero 0
  norm_num [ha0, ha1] at hd ha
  linarith

end MixedMoments.Series
