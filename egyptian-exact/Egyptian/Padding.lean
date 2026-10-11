import Egyptian.PaddingSelection

namespace Egyptian

/-- Pad a distinct expansion of one by exactly one term while preserving one
specified denominator. Every new denominator is at most B(B+1) when B bounds
the input denominators. This is a coarse bound, not a sharp size theorem. -/
theorem pad_one_preserving_denominator_bounded {input : List ℕ} {marker B : ℕ}
    (hp : ∀ d ∈ input, 0 < d) (hn : input.Nodup) (hlen : 3 ≤ input.length)
    (hv : reciprocalSum input = 1) (hm : marker ∈ input)
    (hbound : ∀ d ∈ input, d ≤ B) :
    ∃ out : List ℕ, (∀ d ∈ out, 0 < d) ∧ out.Nodup ∧
      out.length = input.length + 1 ∧ reciprocalSum out = 1 ∧ marker ∈ out ∧
      (∀ d ∈ out, d ≤ B * (B + 1)) := by
  obtain ⟨M, d, t, hperm, hd, hdM, ht⟩ := expose_top_two hp hn hlen hv
  have hp' : ∀ r ∈ M :: d :: t, 0 < r := fun r hr => hp r (hperm.mem_iff.mpr hr)
  have hn' : (M :: d :: t).Nodup := hperm.nodup_iff.mp hn
  have hv' : reciprocalSum (M :: d :: t) = 1 := by rw [← reciprocalSum_perm hperm]; exact hv
  have hm' : marker ∈ M :: d :: t := hperm.mem_iff.mp hm
  have hMB : M ≤ B := hbound M (hperm.mem_iff.mpr (by simp))
  obtain ⟨out, hpos, hnodup, hlength, hvalue, hmarker, hmax⟩ :=
    padding_from_top_two hp' hn' hv' hd hdM ht hm'
  refine ⟨out, hpos, hnodup, ?_, hvalue, hmarker, ?_⟩
  · rw [← hperm.length_eq] at hlength
    exact hlength
  · intro r hr
    exact le_trans (hmax r hr) (Nat.mul_le_mul hMB (Nat.add_le_add_right hMB 1))

/-- The public padding theorem, without a caller-supplied denominator bound. -/
theorem pad_one_preserving_denominator {input : List ℕ} {marker : ℕ}
    (hp : ∀ d ∈ input, 0 < d) (hn : input.Nodup) (hlen : 3 ≤ input.length)
    (hv : reciprocalSum input = 1) (hm : marker ∈ input) :
    ∃ out : List ℕ, (∀ d ∈ out, 0 < d) ∧ out.Nodup ∧
      out.length = input.length + 1 ∧ reciprocalSum out = 1 ∧ marker ∈ out := by
  have hbound : ∀ d ∈ input, d ≤ input.sum := fun _ hd => List.le_sum_of_mem hd
  obtain ⟨out, hpos, hnodup, hlength, hvalue, hmarker, _⟩ :=
    pad_one_preserving_denominator_bounded hp hn hlen hv hm hbound
  exact ⟨out, hpos, hnodup, hlength, hvalue, hmarker⟩

end Egyptian
