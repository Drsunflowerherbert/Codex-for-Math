import Egyptian.SafeSplit
import Egyptian.PaddingCollision

namespace Egyptian

/-- Expose the two largest distinct denominators. A sum-one expansion of at least
three terms has second largest denominator at least three. -/
theorem expose_top_two {input : List ℕ} (hp : ∀ r ∈ input, 0 < r)
    (hn : input.Nodup) (hlen : 3 ≤ input.length) (hv : reciprocalSum input = 1) :
    ∃ M d : ℕ, ∃ t : List ℕ, input.Perm (M :: d :: t) ∧
      3 ≤ d ∧ d < M ∧ (∀ r ∈ t, r < d) := by
  obtain ⟨s, hperm, hsorted⟩ :
      ∃ s : List ℕ, s.Perm input ∧ s.Pairwise (· ≥ ·) :=
    ⟨input.mergeSort (· ≥ ·), List.mergeSort_perm input _,
      List.sorted_mergeSort' (· ≥ ·) input⟩
  have hpos : ∀ r ∈ s, 0 < r := fun r hr => hp r (hperm.mem_iff.mp hr)
  have hnodup : s.Nodup := hperm.nodup_iff.mpr hn
  have hvalue : reciprocalSum s = 1 := by rw [reciprocalSum_perm hperm]; exact hv
  have hlength : 3 ≤ s.length := by rw [hperm.length_eq]; exact hlen
  have hstrict : s.Pairwise (· > ·) := List.Sorted.gt_of_ge hsorted hnodup
  cases s with
  | nil => simp at hlength
  | cons M s =>
    cases s with
    | nil => simp at hlength
    | cons d t =>
      have htne : t ≠ [] := by intro he; simp [he] at hlength
      obtain ⟨c, hc⟩ := List.exists_mem_of_ne_nil t htne
      have htop := List.pairwise_cons.mp hstrict
      have hsecond := List.pairwise_cons.mp htop.2
      have hc2 : 2 ≤ c := denominator_ge_two_of_one hpos (by omega) hvalue (by simp [hc])
      have hcd : c < d := hsecond.1 c hc
      exact ⟨M, d, t, hperm.symm, by omega, htop.1 d (by simp), hsecond.1⟩

/-- Padding after exposing the top two denominators, with an exact marker and a
coarse bound. The composite split repairs either ordinary-split collision. -/
theorem padding_from_top_two {M d marker : ℕ} {t : List ℕ}
    (hp : ∀ r ∈ M :: d :: t, 0 < r) (hn : (M :: d :: t).Nodup)
    (hv : reciprocalSum (M :: d :: t) = 1) (hd : 3 ≤ d) (hdM : d < M)
    (ht : ∀ r ∈ t, r < d) (hm : marker ∈ M :: d :: t) :
    ∃ out : List ℕ, (∀ r ∈ out, 0 < r) ∧ out.Nodup ∧
      out.length = (M :: d :: t).length + 1 ∧ reciprocalSum out = 1 ∧
      marker ∈ out ∧ (∀ r ∈ out, r ≤ M * (M + 1)) := by
  have hMbound : M ≤ M * (M + 1) := by nlinarith
  have hMpos : 0 < M := by omega
  by_cases hmarker : marker = M
  · have hperm : (M :: d :: t).Perm (d :: M :: t) := List.Perm.swap d M t
    have hp' : ∀ r ∈ d :: M :: t, 0 < r := fun r hr => hp r (hperm.mem_iff.mpr hr)
    have hn' : (d :: M :: t).Nodup := hperm.nodup_iff.mp hn
    have hv' : reciprocalSum (d :: M :: t) = 1 := by rw [← reciprocalSum_perm hperm]; exact hv
    obtain ⟨u, v, hdu, huv, huM, hvM, hubound, hvbound, he⟩ :=
      padding_pair d M hd hdM (fun hc => prime_collision_obstruction hd hp' hv' ht hc)
    have hut : u ∉ M :: t := by
      intro hu
      rcases List.mem_cons.mp hu with hu | hu
      · exact huM hu
      · have := ht u hu; omega
    have hvt : v ∉ M :: t := by
      intro hv
      rcases List.mem_cons.mp hv with hv | hv
      · exact hvM hv
      · have := ht v hv; omega
    obtain ⟨hpos, hnodup, hlength, hvalue⟩ :=
      safe_split hp' hn' (by omega : 0 < u) (by omega : 0 < v) (ne_of_lt huv) hut hvt he
    refine ⟨u :: v :: M :: t, hpos, hnodup, hlength,
      hvalue.trans hv', by simp [hmarker], ?_⟩
    intro r hr
    rcases List.mem_cons.mp hr with rfl | hr
    · exact hubound
    rcases List.mem_cons.mp hr with rfl | hr
    · exact hvbound
    rcases List.mem_cons.mp hr with rfl | hr
    · exact hMbound
    · exact le_trans (le_of_lt (lt_trans (ht r hr) hdM)) hMbound
  · have hupper : ∀ r ∈ d :: t, r < M := by
      intro r hr
      rcases List.mem_cons.mp hr with rfl | hr
      · exact hdM
      · exact lt_trans (ht r hr) hdM
    have huv : M + 1 < M * (M + 1) := by nlinarith
    have hut : M + 1 ∉ d :: t := by intro h; have := hupper _ h; omega
    have hvt : M * (M + 1) ∉ d :: t := by intro h; have := hupper _ h; omega
    obtain ⟨hpos, hnodup, hlength, hvalue⟩ :=
      safe_split hp hn (by omega : 0 < M + 1) (by positivity : 0 < M * (M + 1))
        (ne_of_lt huv) hut hvt (unit_split_identity M (by omega))
    have hmt : marker ∈ d :: t := (List.mem_cons.mp hm).resolve_left hmarker
    refine ⟨(M + 1) :: (M * (M + 1)) :: d :: t, hpos, hnodup, hlength,
      hvalue.trans hv, by simp [hmt], ?_⟩
    intro r hr
    rcases List.mem_cons.mp hr with rfl | hr
    · exact le_of_lt huv
    rcases List.mem_cons.mp hr with rfl | hr
    · exact le_rfl
    · exact le_trans (le_of_lt (hupper r hr)) hMbound

end Egyptian
