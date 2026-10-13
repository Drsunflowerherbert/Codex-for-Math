import Mathlib

/-! Sufficient LP certificates. Variables are free; bounds must be explicit rows.
All inequalities are normalized to `A x ≤ b`; equality multipliers are free.
The objective is maximization. Minimization is represented by negating its objective.
-/

namespace LPCertificates

variable {α : Type*} [Field α] [LinearOrder α] [IsStrictOrderedRing α] {n m k : ℕ}

def dot (u v : Fin n → α) : α := ∑ j, u j * v j

structure Problem (α : Type*) (n m k : ℕ) where
  A : Fin m → Fin n → α
  b : Fin m → α
  E : Fin k → Fin n → α
  f : Fin k → α
  c : Fin n → α

def Feasible (P : Problem α n m k) (x : Fin n → α) : Prop :=
  (∀ i, dot (P.A i) x ≤ P.b i) ∧ (∀ i, dot (P.E i) x = P.f i)

def Nonnegative (w : Fin m → α) : Prop := ∀ i, 0 ≤ w i

def combination (P : Problem α n m k) (w : Fin m → α) (v : Fin k → α)
    (j : Fin n) : α := (∑ i, w i * P.A i j) + ∑ i, v i * P.E i j

def bound (P : Problem α n m k) (w : Fin m → α) (v : Fin k → α) : α :=
  dot w P.b + dot v P.f

def DualCertificate (P : Problem α n m k) (w : Fin m → α) (v : Fin k → α) : Prop :=
  Nonnegative w ∧ ∀ j, combination P w v j = P.c j

def OptimalCertificate (P : Problem α n m k) (x : Fin n → α)
    (w : Fin m → α) (v : Fin k → α) : Prop :=
  Feasible P x ∧ DualCertificate P w v ∧ bound P w v = dot P.c x

def InfeasibleCertificate (P : Problem α n m k)
    (w : Fin m → α) (v : Fin k → α) : Prop :=
  Nonnegative w ∧ (∀ j, combination P w v j = 0) ∧ bound P w v < 0

def RayCertificate (P : Problem α n m k) (x d : Fin n → α) : Prop :=
  Feasible P x ∧ (∀ i, dot (P.A i) d ≤ 0) ∧
    (∀ i, dot (P.E i) d = 0) ∧ 0 < dot P.c d

omit [LinearOrder α] [IsStrictOrderedRing α] in
lemma dot_add (u v x : Fin n → α) :
    dot (fun j => u j + v j) x = dot u x + dot v x := by
  simp [dot, add_mul, Finset.sum_add_distrib]

omit [LinearOrder α] [IsStrictOrderedRing α] in
lemma dot_add_right (a x d : Fin n → α) :
    dot a (fun j => x j + d j) = dot a x + dot a d := by
  simp [dot, mul_add, Finset.sum_add_distrib]

omit [LinearOrder α] [IsStrictOrderedRing α] in
lemma dot_smul_right (a d : Fin n → α) (t : α) :
    dot a (fun j => t * d j) = t * dot a d := by
  simp [dot, Finset.mul_sum, mul_left_comm]

omit [LinearOrder α] [IsStrictOrderedRing α] in
lemma weighted_dot (A : Fin m → Fin n → α) (w : Fin m → α) (x : Fin n → α) :
    (∑ i, w i * dot (A i) x) = dot (fun j => ∑ i, w i * A i j) x := by
  simp only [dot, Finset.mul_sum, Finset.sum_mul, mul_assoc]
  exact Finset.sum_comm

omit [LinearOrder α] [IsStrictOrderedRing α] in
lemma combination_dot (P : Problem α n m k) (w : Fin m → α)
    (v : Fin k → α) (x : Fin n → α) :
    dot (combination P w v) x =
      (∑ i, w i * dot (P.A i) x) + ∑ i, v i * dot (P.E i) x := by
  change dot (fun j => (∑ i, w i * P.A i j) + ∑ i, v i * P.E i j) x = _
  rw [dot_add, ← weighted_dot, ← weighted_dot]

theorem combination_bound (P : Problem α n m k) (w : Fin m → α)
    (v : Fin k → α) (hw : Nonnegative w) (x : Fin n → α) (hx : Feasible P x) :
    dot (combination P w v) x ≤ bound P w v := by
  rw [combination_dot]
  apply add_le_add
  · exact Finset.sum_le_sum fun i _ => mul_le_mul_of_nonneg_left (hx.1 i) (hw i)
  · exact le_of_eq (Finset.sum_congr rfl fun i _ => congrArg (fun z => v i * z) (hx.2 i))

theorem weak_duality (P : Problem α n m k) (w : Fin m → α) (v : Fin k → α)
    (hc : DualCertificate P w v) (x : Fin n → α) (hx : Feasible P x) :
    dot P.c x ≤ bound P w v := by
  have he : combination P w v = P.c := funext hc.2
  rw [← he]
  exact combination_bound P w v hc.1 x hx

theorem optimal_sound (P : Problem α n m k) (x : Fin n → α)
    (w : Fin m → α) (v : Fin k → α) (hc : OptimalCertificate P x w v) :
    Feasible P x ∧ ∀ y, Feasible P y → dot P.c y ≤ dot P.c x := by
  refine ⟨hc.1, fun y hy => ?_⟩
  rw [← hc.2.2]
  exact weak_duality P w v hc.2.1 y hy

theorem infeasible_sound (P : Problem α n m k) (w : Fin m → α)
    (v : Fin k → α) (hc : InfeasibleCertificate P w v) :
    ¬ ∃ x, Feasible P x := by
  rintro ⟨x, hx⟩
  have h := combination_bound P w v hc.1 x hx
  have hz : dot (combination P w v) x = 0 := by simp [dot, hc.2.1]
  rw [hz] at h
  exact (not_lt_of_ge h) hc.2.2

theorem ray_feasible (P : Problem α n m k) (x d : Fin n → α)
    (hc : RayCertificate P x d) (t : α) (ht : 0 ≤ t) :
    Feasible P (fun j => x j + t * d j) := by
  constructor
  · intro i
    rw [dot_add_right, dot_smul_right]
    have htd : t * dot (P.A i) d ≤ 0 := mul_nonpos_of_nonneg_of_nonpos ht (hc.2.1 i)
    linarith [hc.1.1 i]
  · intro i
    rw [dot_add_right, dot_smul_right, hc.2.2.1 i, mul_zero, add_zero]
    exact hc.1.2 i

omit [LinearOrder α] [IsStrictOrderedRing α] in
theorem ray_objective (P : Problem α n m k) (x d : Fin n → α) (t : α) :
    dot P.c (fun j => x j + t * d j) = dot P.c x + t * dot P.c d := by
  rw [dot_add_right, dot_smul_right]

theorem unbounded_sound (P : Problem α n m k) (x d : Fin n → α)
    (hc : RayCertificate P x d) :
    ∀ B : α, ∃ y, Feasible P y ∧ B < dot P.c y := by
  intro B
  let t : α := max 0 ((B - dot P.c x) / dot P.c d) + 1
  have hp : 0 < dot P.c d := hc.2.2.2
  have ht : 0 ≤ t := by dsimp [t]; positivity
  refine ⟨fun j => x j + t * d j, ray_feasible P x d hc t ht, ?_⟩
  rw [ray_objective]
  have hmax : (B - dot P.c x) / dot P.c d < t := by
    dsimp [t]
    have := le_max_right (0 : α) ((B - dot P.c x) / dot P.c d)
    linarith
  have := (div_lt_iff₀ hp).mp hmax
  linarith

omit [IsStrictOrderedRing α] in
theorem duality_gap (P : Problem α n m k) (w : Fin m → α) (v : Fin k → α)
    (hc : DualCertificate P w v) (x : Fin n → α) (hx : Feasible P x) :
    bound P w v - dot P.c x = ∑ i, w i * (P.b i - dot (P.A i) x) := by
  have he : combination P w v = P.c := funext hc.2
  rw [← he, combination_dot]
  simp only [bound, dot, mul_sub, Finset.sum_sub_distrib]
  have heq : (∑ i, v i * (∑ j, P.E i j * x j)) = ∑ i, v i * P.f i :=
    Finset.sum_congr rfl fun i _ => congrArg (fun z => v i * z) (hx.2 i)
  rw [heq]
  ring

theorem complementary_slackness (P : Problem α n m k) (w : Fin m → α)
    (v : Fin k → α) (hc : DualCertificate P w v) (x : Fin n → α)
    (hx : Feasible P x) :
    bound P w v = dot P.c x ↔ ∀ i, w i * (P.b i - dot (P.A i) x) = 0 := by
  rw [← sub_eq_zero, duality_gap P w v hc x hx]
  exact Finset.sum_eq_zero_iff_of_nonneg
    (fun i _ => mul_nonneg (hc.1 i) (sub_nonneg.mpr (hx.1 i))) |>.trans (by simp)

end LPCertificates
