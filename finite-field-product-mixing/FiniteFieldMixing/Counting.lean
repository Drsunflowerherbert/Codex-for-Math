import Mathlib

open scoped BigOperators

namespace FiniteFieldMixing

variable {p : ℕ} [NeZero p]

/-- Number of ordered pairs from `H` with a prescribed product. -/
def productCount (H : Finset (ZMod p)) (x : ZMod p) : ℕ :=
  ((H ×ˢ H).filter (fun ab => ab.1 * ab.2 = x)).card

/-- Additive convolution of natural-valued functions. -/
def natConvolution (f g : ZMod p → ℕ) (x : ZMod p) : ℕ :=
  ∑ y, f y * g (x - y)

/-- Counts of sums of `k` independent ordered products from `H`. -/
def convolutionCount (H : Finset (ZMod p)) : ℕ → ZMod p → ℕ
  | 0, x => if x = 0 then 1 else 0
  | k + 1, x => natConvolution (convolutionCount H k) (productCount H) x

@[simp] theorem convolutionCount_zero (H : Finset (ZMod p)) (x : ZMod p) :
    convolutionCount H 0 x = if x = 0 then 1 else 0 := rfl

@[simp] theorem convolutionCount_succ (H : Finset (ZMod p)) (k : ℕ) (x : ZMod p) :
    convolutionCount H (k + 1) x =
      natConvolution (convolutionCount H k) (productCount H) x := rfl

/-- The product fibers partition the Cartesian square. -/
theorem productCount_sum (H : Finset (ZMod p)) :
    ∑ x, productCount H x = H.card ^ 2 := by
  unfold productCount
  rw [Finset.sum_card_fiberwise_eq_card_filter]
  simp [pow_two]

/-- Summing a function against product multiplicities equals summing over pairs. -/
theorem productCount_weighted_sum {R : Type*} [Semiring R]
    (H : Finset (ZMod p)) (F : ZMod p → R) :
    ∑ x, (productCount H x : R) * F x = ∑ a ∈ H, ∑ b ∈ H, F (a * b) := by
  calc
    ∑ x, (productCount H x : R) * F x =
        ∑ x, ∑ ab ∈ (H ×ˢ H).filter (fun ab => ab.1 * ab.2 = x),
          F (ab.1 * ab.2) := by
      apply Finset.sum_congr rfl
      intro x hx
      rw [productCount, ← nsmul_eq_mul, ← Finset.sum_const]
      apply Finset.sum_congr rfl
      intro ab hab
      rw [(Finset.mem_filter.mp hab).2]
    _ = ∑ ab ∈ H ×ˢ H, F (ab.1 * ab.2) :=
      Finset.sum_fiberwise (H ×ˢ H) (fun ab => ab.1 * ab.2) _
    _ = ∑ a ∈ H, ∑ b ∈ H, F (a * b) := Finset.sum_product _ _ _

/-- The same weighted identity on the subtype of admissible pairs. -/
theorem productCount_weighted_sum_pairs {R : Type*} [Semiring R]
    (H : Finset (ZMod p)) (F : ZMod p → R) :
    ∑ x, (productCount H x : R) * F x =
      ∑ ab : ↥(H ×ˢ H), F (ab.val.1 * ab.val.2) := by
  rw [Finset.univ_eq_attach, Finset.sum_attach (H ×ˢ H) (fun ab => F (ab.1 * ab.2)),
    Finset.sum_product H H (fun ab => F (ab.1 * ab.2))]
  exact productCount_weighted_sum H F

omit [NeZero p] in
/-- A positive product fiber supplies an ordered pair in `H`. -/
theorem productCount_pos_iff (H : Finset (ZMod p)) (x : ZMod p) :
    0 < productCount H x ↔ ∃ a ∈ H, ∃ b ∈ H, a * b = x := by
  simp only [productCount, Finset.card_pos, Finset.Nonempty, Finset.mem_filter,
    Prod.exists]
  aesop

/-- A positive natural convolution has a positive summand. -/
theorem natConvolution_pos_iff (f g : ZMod p → ℕ) (x : ZMod p) :
    0 < natConvolution f g x ↔ ∃ y, 0 < f y ∧ 0 < g (x - y) := by
  simp [natConvolution, Finset.sum_pos_iff, Nat.pos_iff_ne_zero]

/-- Additive convolution is commutative. -/
theorem natConvolution_comm (f g : ZMod p → ℕ) (t : ZMod p) :
    natConvolution f g t = natConvolution g f t := by
  unfold natConvolution
  refine Fintype.sum_equiv (Equiv.subLeft t) _ _ ?_
  intro x
  simp [mul_comm]

/-- Translation preserves the sum of a function over all residues. -/
theorem sum_sub_right (f : ZMod p → ℕ) (y : ZMod p) :
    ∑ x, f (x - y) = ∑ x, f x := by
  exact Fintype.sum_equiv (Equiv.subRight y) _ _ (fun _ => rfl)

/-- The total mass of a convolution is the product of the masses. -/
theorem natConvolution_sum (f g : ZMod p → ℕ) :
    ∑ x, natConvolution f g x = (∑ x, f x) * ∑ x, g x := by
  unfold natConvolution
  rw [Finset.sum_comm]
  simp_rw [← Finset.mul_sum, sum_sub_right]
  rw [Finset.sum_mul]

/-- Exactly `H.card ^ (2*k)` ordered samples underlie the count. -/
theorem convolutionCount_sum (H : Finset (ZMod p)) (k : ℕ) :
    ∑ x, convolutionCount H k x = H.card ^ (2 * k) := by
  induction k with
  | zero => simp [convolutionCount]
  | succ k ih =>
      simp only [convolutionCount_succ]
      rw [natConvolution_sum, ih, productCount_sum]
      rw [Nat.mul_succ, pow_add]

/-- The finite sample space of `k` ordered admissible pairs. -/
abbrev TupleSpace (H : Finset (ZMod p)) (k : ℕ) := Fin k → ↥(H ×ˢ H)

/-- The product-sum statistic on the finite sample space. -/
def tupleSum {H : Finset (ZMod p)} {k : ℕ} (v : TupleSpace H k) : ZMod p :=
  ∑ i, (v i).val.1 * (v i).val.2

/-- The actual cardinality of the event that the product-sum is `t`. -/
def tupleCount (H : Finset (ZMod p)) (k : ℕ) (t : ZMod p) : ℕ :=
  (Finset.univ.filter (fun v : TupleSpace H k => tupleSum v = t)).card

omit [NeZero p] in
/-- The Cartesian sample space has the expected cardinality. -/
theorem tupleSpace_card (H : Finset (ZMod p)) (k : ℕ) :
    Fintype.card (TupleSpace H k) = H.card ^ (2 * k) := by
  change Fintype.card (Fin k → ↥(H ×ˢ H)) = _
  rw [Fintype.card_fun, Fintype.card_coe, Finset.card_product H H, Fintype.card_fin]
  rw [← pow_two, ← pow_mul]

omit [NeZero p] in
theorem tupleCount_eq_sum (H : Finset (ZMod p)) (k : ℕ) (t : ZMod p) :
    tupleCount H k t = ∑ v : TupleSpace H k, if tupleSum v = t then 1 else 0 := by
  classical
  simpa only [tupleCount, Nat.cast_id] using
    (Finset.sum_boole (R := ℕ) (fun v : TupleSpace H k => tupleSum v = t) Finset.univ).symm

omit [NeZero p] in
@[simp] theorem tupleCount_zero (H : Finset (ZMod p)) (t : ZMod p) :
    tupleCount H 0 t = if t = 0 then 1 else 0 := by
  classical
  rw [tupleCount_eq_sum]
  simp [tupleSum, eq_comm]

/-- Splitting off the first coordinate gives the convolution recurrence. -/
theorem tupleCount_succ (H : Finset (ZMod p)) (k : ℕ) (t : ZMod p) :
    tupleCount H (k + 1) t = natConvolution (tupleCount H k) (productCount H) t := by
  classical
  rw [tupleCount_eq_sum]
  calc
    (∑ v : TupleSpace H (k + 1), if tupleSum v = t then 1 else 0) =
        ∑ ab : ↥(H ×ˢ H), ∑ v : TupleSpace H k,
          if tupleSum (Fin.cons ab v) = t then 1 else 0 := by
      calc
        _ = ∑ w : ↥(H ×ˢ H) × TupleSpace H k,
            if tupleSum (Fin.cons w.1 w.2) = t then 1 else 0 := by
          symm
          exact Fintype.sum_equiv
            (Fin.consEquiv (fun _ : Fin (k + 1) => ↥(H ×ˢ H)))
            _ _ (fun _ => rfl)
        _ = _ := Fintype.sum_prod_type _
    _ = ∑ ab : ↥(H ×ˢ H), tupleCount H k (t - ab.val.1 * ab.val.2) := by
      apply Finset.sum_congr rfl
      intro ab hab
      rw [tupleCount_eq_sum]
      apply Finset.sum_congr rfl
      intro v hv
      simp only [tupleSum, Fin.sum_univ_succ, Fin.cons_zero, Fin.cons_succ]
      simp only [eq_sub_iff_add_eq']
    _ = natConvolution (productCount H) (tupleCount H k) t := by
      exact (productCount_weighted_sum_pairs H (fun x => tupleCount H k (t - x))).symm
    _ = natConvolution (tupleCount H k) (productCount H) t :=
      natConvolution_comm _ _ _

/-- The recursively defined convolution count equals the cardinality of its event. -/
theorem convolutionCount_eq_tupleCount (H : Finset (ZMod p)) (k : ℕ) (t : ZMod p) :
    convolutionCount H k t = tupleCount H k t := by
  induction k generalizing t with
  | zero => simp
  | succ k ih =>
      rw [convolutionCount_succ, tupleCount_succ]
      simp only [natConvolution, ih]

/-- Positive convolution counts are precisely the existence of tuples. -/
theorem convolutionCount_pos_iff (H : Finset (ZMod p)) (k : ℕ) (t : ZMod p) :
    0 < convolutionCount H k t ↔
      ∃ a b : Fin k → ZMod p,
        (∀ i, a i ∈ H) ∧ (∀ i, b i ∈ H) ∧ ∑ i, a i * b i = t := by
  induction k generalizing t with
  | zero =>
      simp only [convolutionCount_zero]
      constructor
      · intro ht
        have ht0 : t = 0 := by split_ifs at ht with h <;> simp_all
        refine ⟨Fin.elim0, Fin.elim0, ?_, ?_, ?_⟩
        · intro i; exact Fin.elim0 i
        · intro i; exact Fin.elim0 i
        · simp [ht0]
      · rintro ⟨a, b, _, _, hab⟩
        have ht0 : t = 0 := by simpa using hab.symm
        simp [ht0]
  | succ k ih =>
      rw [convolutionCount_succ, natConvolution_pos_iff]
      constructor
      · rintro ⟨x, hx, htx⟩
        obtain ⟨a, b, ha, hb, hab⟩ := (ih x).mp hx
        obtain ⟨u, hu, v, hv, huv⟩ := (productCount_pos_iff H (t - x)).mp htx
        refine ⟨Fin.cons u a, Fin.cons v b, ?_, ?_, ?_⟩
        · intro i; refine Fin.cases hu (fun j => ?_) i
          simpa using ha j
        · intro i; refine Fin.cases hv (fun j => ?_) i
          simpa using hb j
        · simp only [Fin.sum_univ_succ, Fin.cons_zero, Fin.cons_succ]
          rw [huv, hab]
          exact sub_add_cancel t x
      · rintro ⟨a, b, ha, hb, hab⟩
        let x : ZMod p := ∑ i : Fin k, a i.succ * b i.succ
        refine ⟨x, (ih x).mpr ?_, (productCount_pos_iff H (t - x)).mpr ?_⟩
        · exact ⟨fun i => a i.succ, fun i => b i.succ,
            fun i => ha i.succ, fun i => hb i.succ, rfl⟩
        · refine ⟨a 0, ha 0, b 0, hb 0, ?_⟩
          have hsum : a 0 * b 0 + x = t := by
            simpa only [Fin.sum_univ_succ] using hab
          exact eq_sub_of_add_eq hsum

/-- The witness interface used by the four-product covering theorem. -/
theorem four_products_of_count_pos (H : Finset (ZMod p)) (t : ZMod p)
    (ht : 0 < convolutionCount H 4 t) :
    ∃ a b : Fin 4 → ZMod p,
      (∀ i, a i ∈ H) ∧ (∀ i, b i ∈ H) ∧ ∑ i, a i * b i = t :=
  (convolutionCount_pos_iff H 4 t).mp ht

end FiniteFieldMixing
