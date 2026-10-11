import Mathlib

noncomputable section

open scoped BigOperators
open Set

namespace ConvexApprox

variable {E ι : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [Fintype ι]

/-- A finite exponential barrier determined by continuous real linear forms. -/
def barrier (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x : E) : ℝ :=
  ∑ i, Real.exp (L i x - b i)

/-- The first Fréchet derivative of the exponential barrier. -/
def barrierDeriv (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x : E) : E →L[ℝ] ℝ :=
  ∑ i, Real.exp (L i x - b i) • L i

/-- The second Fréchet derivative of the exponential barrier. -/
def barrierHessian (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x : E) :
    E →L[ℝ] E →L[ℝ] ℝ :=
  ∑ i, Real.exp (L i x - b i) • (L i).smulRight (L i)

theorem hasFDerivAt_barrier (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x : E) :
    HasFDerivAt (barrier L b) (barrierDeriv L b x) x := by
  exact HasFDerivAt.fun_sum fun i _ => ((L i).hasFDerivAt.sub_const (b i)).exp

theorem hasFDerivAt_barrierDeriv (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x : E) :
    HasFDerivAt (barrierDeriv L b) (barrierHessian L b x) x := by
  unfold barrierDeriv barrierHessian
  apply HasFDerivAt.fun_sum
  intro i hi
  convert (((L i).hasFDerivAt.sub_const (b i)).exp.smul_const (L i)) using 1
  ext y z
  simp [mul_assoc]

theorem fderiv_barrier (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x : E) :
    fderiv ℝ (barrier L b) x = barrierDeriv L b x :=
  (hasFDerivAt_barrier L b x).fderiv

theorem fderiv_barrierDeriv (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x : E) :
    fderiv ℝ (barrierDeriv L b) x = barrierHessian L b x :=
  (hasFDerivAt_barrierDeriv L b x).fderiv

theorem barrierDeriv_apply (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x y : E) :
    barrierDeriv L b x y = ∑ i, Real.exp (L i x - b i) * L i y := by
  simp [barrierDeriv]

theorem barrierHessian_apply (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x y z : E) :
    barrierHessian L b x y z = ∑ i, Real.exp (L i x - b i) * L i y * L i z := by
  simp [barrierHessian, mul_assoc]

theorem barrierHessian_diag (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x y : E) :
    barrierHessian L b x y y = ∑ i, Real.exp (L i x - b i) * (L i y) ^ 2 := by
  simp [barrierHessian_apply, pow_two, mul_assoc]

theorem contDiff_barrier (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ)
    {n : WithTop ℕ∞} : ContDiff ℝ n (barrier L b) := by
  exact ContDiff.sum fun i _ => ((L i).contDiff.sub contDiff_const).exp

theorem fderiv_fderiv_barrier (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x : E) :
    fderiv ℝ (fun z => fderiv ℝ (barrier L b) z) x = barrierHessian L b x := by
  simp only [fderiv_barrier, fderiv_barrierDeriv]

theorem barrierHessian_symmetric (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x y z : E) :
    barrierHessian L b x y z = barrierHessian L b x z y := by
  simp only [barrierHessian_apply]
  apply Finset.sum_congr rfl
  intro i hi
  rw [mul_assoc, mul_assoc, mul_comm (L i y) (L i z)]

theorem barrierHessian_nonneg (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x y : E) :
    0 ≤ barrierHessian L b x y y := by
  rw [barrierHessian_diag]
  exact Finset.sum_nonneg fun i _ =>
    mul_nonneg (Real.exp_pos _).le (sq_nonneg _)

theorem barrierHessian_pos_of_exists (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x y : E)
    (hy : ∃ i, L i y ≠ 0) :
    0 < barrierHessian L b x y y := by
  rw [barrierHessian_diag]
  apply Finset.sum_pos'
  · exact fun i _ => mul_nonneg (Real.exp_pos _).le (sq_nonneg _)
  · obtain ⟨i, hi⟩ := hy
    exact ⟨i, Finset.mem_univ _, mul_pos (Real.exp_pos _) (sq_pos_of_ne_zero hi)⟩

theorem barrierHessian_pos (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ)
    (hL : ∀ y : E, y ≠ 0 → ∃ i, L i y ≠ 0) (x y : E) (hy : y ≠ 0) :
    0 < barrierHessian L b x y y :=
  barrierHessian_pos_of_exists L b x y (hL y hy)


lemma affineCombination (L : E →L[ℝ] ℝ) (d : ℝ) (x y : E) (a c : ℝ)
    (h : a + c = 1) : L (a • x + c • y) - d = a * (L x - d) + c * (L y - d) := by
  simp only [map_add, map_smul, smul_eq_mul]
  have hd := congrArg (fun z : ℝ => z * d) h
  nlinarith
lemma convexOn_barrier (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) :
    ConvexOn ℝ Set.univ (barrier L b) := by
  refine ⟨convex_univ, ?_⟩
  intro x hx y hy a c ha hc hac
  simp only [barrier, smul_eq_mul, Finset.mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_le_sum
  intro i hi
  rw [affineCombination (L i) (b i) x y a c hac]
  exact convexOn_exp.2 (mem_univ _) (mem_univ _) ha hc hac
lemma strictConvexOn_barrier (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ)
    (hsep : ∀ v : E, v ≠ 0 → ∃ i, L i v ≠ 0) :
    StrictConvexOn ℝ Set.univ (barrier L b) := by
  refine ⟨convex_univ, ?_⟩
  intro x hx y hy hxy a c ha hc hac
  simp only [barrier, smul_eq_mul, Finset.mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_lt_sum
  · intro i hi
    rw [affineCombination (L i) (b i) x y a c hac]
    exact convexOn_exp.2 (mem_univ _) (mem_univ _) ha.le hc.le hac
  · obtain ⟨i, hi⟩ := hsep (x - y) (sub_ne_zero.mpr hxy)
    refine ⟨i, Finset.mem_univ _, ?_⟩
    rw [affineCombination (L i) (b i) x y a c hac]
    apply strictConvexOn_exp.2 (mem_univ _) (mem_univ _) _ ha hc hac
    intro heq
    apply hi
    rw [map_sub]
    linarith

/-- The affine tangent at any point lies below the finite exponential barrier. -/
theorem barrier_supporting (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ) (x y : E) :
    barrier L b x + barrierDeriv L b x (y - x) ≤ barrier L b y := by
  rw [barrierDeriv_apply]
  unfold barrier
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_le_sum
  intro i hi
  rw [map_sub]
  have h := mul_le_mul_of_nonneg_left
    (Real.add_one_le_exp ((L i y - b i) - (L i x - b i)))
    (Real.exp_pos (L i x - b i)).le
  rw [← Real.exp_add] at h
  have he : (L i x - b i) + ((L i y - b i) - (L i x - b i)) = L i y - b i := by ring
  rw [he] at h
  nlinarith

/-- With a strict sublevel anchor, the derivative is positive in the outward radial direction
at every point of the level. No separation assumption is needed for this implication. -/
theorem barrierDeriv_apply_pos_of_level (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ)
    (p x : E) (c : ℝ) (hp : barrier L b p < c) (hx : barrier L b x = c) :
    0 < barrierDeriv L b x (x - p) := by
  have h := barrier_supporting L b x p
  have he : barrierDeriv L b x (p - x) = -barrierDeriv L b x (x - p) := by
    rw [map_sub, map_sub]
    ring
  rw [he, hx] at h
  linarith

/-- Every nonempty strict sublevel has a regular boundary level. -/
theorem barrierDeriv_ne_zero_of_level (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ)
    (p x : E) (c : ℝ) (hp : barrier L b p < c) (hx : barrier L b x = c) :
    barrierDeriv L b x ≠ 0 := by
  intro h
  have hpos := barrierDeriv_apply_pos_of_level L b p x c hp hx
  simp [h] at hpos

/-- The closed sublevel is the closure of the open sublevel, provided the latter has an anchor. -/
theorem closure_barrier_lt (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ)
    (p : E) (c : ℝ) (hp : barrier L b p < c) :
    closure {x : E | barrier L b x < c} = {x : E | barrier L b x ≤ c} := by
  apply subset_antisymm
  · exact closure_lt_subset_le (contDiff_barrier L b (n := 0)).continuous continuous_const
  · intro x hx
    apply closure_mono (s := openSegment ℝ p x) (t := {x : E | barrier L b x < c}) ?_
      (segment_subset_closure_openSegment (right_mem_segment ℝ p x))
    intro z hz
    obtain ⟨a, d, ha, hd, had, rfl⟩ := hz
    have h := (convexOn_barrier L b).2 (mem_univ p) (mem_univ x) ha.le hd.le had
    simp only [smul_eq_mul] at h
    have hpa := mul_lt_mul_of_pos_left hp ha
    have hxd := mul_le_mul_of_nonneg_left hx hd.le
    have hsum : a * c + d * c = c := by nlinarith [congrArg (fun r : ℝ => r * c) had]
    dsimp only [mem_setOf_eq] at hx ⊢
    linarith

/-- The boundary of the open sublevel is exactly the level set when a strict anchor exists. -/
theorem frontier_barrier_lt (L : ι → E →L[ℝ] ℝ) (b : ι → ℝ)
    (p : E) (c : ℝ) (hp : barrier L b p < c) :
    frontier {x : E | barrier L b x < c} = {x : E | barrier L b x = c} := by
  have hopen : IsOpen {x : E | barrier L b x < c} :=
    isOpen_lt (contDiff_barrier L b (n := 0)).continuous continuous_const
  rw [hopen.frontier_eq, closure_barrier_lt L b p c hp]
  ext x
  simp only [mem_diff, mem_setOf_eq, not_lt]
  exact le_antisymm_iff.symm

end ConvexApprox
