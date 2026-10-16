import Comparator.Solution

/-!
Private audit harness for HolomorphicAnosov commit
65f2b33a7309de661a8500e4642e5609a537a8ff.

This file imports the actual solution, NOT Comparator.Challenge. The latter is a separate
specification module containing placeholders and duplicate public theorem names.

The four propositions below reproduce the full mathematical types in Challenge/Solution,
including the explicit HomotopyTorusRigidity premise. Each of the four actual targets and
four public wrappers must inhabit the corresponding full type. These checks therefore do
more than establish that declarations with the right names happen to exist.

No new axioms, admitted proofs, proof automation, or compiler-trusted evaluation are used.
-/

open scoped ContDiff
open HolomorphicAnosov

universe u

namespace HolomorphicAnosovAudit

attribute [local instance] HolomorphicAnosov.complex_isManifold_real

/-- Exact Theorem A interface, conditional on the explicit topological premise. -/
def StatementA : Prop :=
  ∀ {d : ℕ} {X : Type u}
    [TopologicalSpace X] [ChartedSpace (ComplexModel d) X]
    [IsCompactComplexManifold d X]
    (f : Biholomorph d d X X) (a : AnosovDatum f)
    (hcodim : HasComplexRankOne a.splitting.stable.toDistribution ∨
      HasComplexRankOne a.splitting.unstable.toDistribution)
    (HS : HomotopyTorusRigidity.{u}),
    HasHyperbolicComplexTorusModel (d := d) (fun x ↦ f x)

/-- Exact Theorem 1.1 interface, including real dimension 2d and the HS premise. -/
def Statement11 : Prop :=
  ∀ {d : ℕ} {X : Type u}
    [TopologicalSpace X] [ChartedSpace (ComplexModel d) X]
    [IsCompactComplexManifold d X]
    (hd : 2 ≤ d) (f : Biholomorph d d X X) (a : AnosovDatum f)
    (hstable : HasComplexRankOne a.splitting.stable.toDistribution)
    (HS : HomotopyTorusRigidity.{u}),
    HyperbolicRealToralConjugacy (2 * d) X (fun x ↦ f x)

/-- Exact Theorem 1.2 interface. There is deliberately NO HS premise. -/
def Statement12 : Prop :=
  ∀ {d : ℕ} {X : Type u}
    [TopologicalSpace X] [ChartedSpace (ComplexModel d) X]
    [IsCompactComplexManifold d X]
    (f : Biholomorph d d X X) (a : AnosovDatum f)
    (hStable : ∃ (r : ℕ) (P : (x : X) → Submodule ℂ (TangentSpace (complexModel d) x)),
      IsHolomorphicTangentSubbundle r P ∧ ∀ x : X,
        ((P x).restrictScalars ℝ).map
          (complexTangentToReal d x).toLinearEquiv.toLinearMap =
            a.splitting.stable.toDistribution x)
    (hUnstable : ∃ (r : ℕ) (P : (x : X) → Submodule ℂ (TangentSpace (complexModel d) x)),
      IsHolomorphicTangentSubbundle r P ∧ ∀ x : X,
        ((P x).restrictScalars ℝ).map
          (complexTangentToReal d x).toLinearEquiv.toLinearMap =
            a.splitting.unstable.toDistribution x)
    (hT : ∃ n : ℕ, Nonempty (X ≃ₜ UnitAddTorus (Fin n))),
    ∃ (L : FullComplexLattice d) (A : LatticeLinearEquiv L)
      (h : Biholomorph d d X (ComplexTorus L)),
      Function.Semiconj (fun x ↦ h x) (fun x ↦ f x)
        (fun t ↦ quotientLinearEquiv A t)

/-- Exact Theorem 1.3 interface, with equality to the original invariant distributions. -/
def Statement13 : Prop :=
  ∀ {d : ℕ} {X : Type u}
    [TopologicalSpace X] [ChartedSpace (ComplexModel d) X]
    [IsCompactComplexManifold d X]
    (f : Biholomorph d d X X) (a : AnosovDatum f)
    (hstable : HasComplexRankOne a.splitting.stable.toDistribution)
    (HS : HomotopyTorusRigidity.{u}),
    ∃ S U : (x : X) → Submodule ℂ (TangentSpace (complexModel d) x),
      (∀ x, ((S x).restrictScalars ℝ).map
        (complexTangentToReal d x).toLinearEquiv.toLinearMap =
          a.splitting.stable.toDistribution x) ∧
      (∀ x, ((U x).restrictScalars ℝ).map
        (complexTangentToReal d x).toLinearEquiv.toLinearMap =
          a.splitting.unstable.toDistribution x) ∧
      IsHolomorphicTangentSubbundle 1 S ∧ IsHolomorphicTangentSubbundle (d - 1) U

-- The four independently named targets must have the specified mathematical types.
theorem target_A_matches : StatementA.{u} :=
  @HolomorphicAnosov.theorem_A

theorem target_11_matches : Statement11.{u} :=
  @HolomorphicAnosov.theorem_1_1

theorem target_12_matches : Statement12.{u} :=
  @HolomorphicAnosov.theorem_1_2

theorem target_13_matches : Statement13.{u} :=
  @HolomorphicAnosov.theorem_1_3

-- The four public comparator wrappers must have those same complete types.
theorem wrapper_A_matches : StatementA.{u} :=
  @HolomorphicAnosov.zhang_theorem_A

theorem wrapper_11_matches : Statement11.{u} :=
  @HolomorphicAnosov.zhang_theorem_1_1

theorem wrapper_12_matches : Statement12.{u} :=
  @HolomorphicAnosov.zhang_theorem_1_2

theorem wrapper_13_matches : Statement13.{u} :=
  @HolomorphicAnosov.zhang_theorem_1_3

end HolomorphicAnosovAudit

set_option pp.universes true
set_option pp.fullNames true
set_option pp.proofs false
set_option pp.width 120

-- Human-readable complete signatures and wrapper applications.
#check @HolomorphicAnosov.theorem_A
#check @HolomorphicAnosov.theorem_1_1
#check @HolomorphicAnosov.theorem_1_2
#check @HolomorphicAnosov.theorem_1_3
#check @HolomorphicAnosov.zhang_theorem_A
#check @HolomorphicAnosov.zhang_theorem_1_1
#check @HolomorphicAnosov.zhang_theorem_1_2
#check @HolomorphicAnosov.zhang_theorem_1_3
#print HolomorphicAnosovAudit.StatementA
#print HolomorphicAnosovAudit.Statement11
#print HolomorphicAnosovAudit.Statement12
#print HolomorphicAnosovAudit.Statement13
#print HolomorphicAnosov.zhang_theorem_A
#print HolomorphicAnosov.zhang_theorem_1_1
#print HolomorphicAnosov.zhang_theorem_1_2
#print HolomorphicAnosov.zhang_theorem_1_3

-- Inspect the transitive axiom closure of EACH actual target and EACH public wrapper.
-- HS is an explicit parameter, so it will NOT appear in this list as an axiom.
#print axioms HolomorphicAnosov.theorem_A
#print axioms HolomorphicAnosov.theorem_1_1
#print axioms HolomorphicAnosov.theorem_1_2
#print axioms HolomorphicAnosov.theorem_1_3
#print axioms HolomorphicAnosov.zhang_theorem_A
#print axioms HolomorphicAnosov.zhang_theorem_1_1
#print axioms HolomorphicAnosov.zhang_theorem_1_2
#print axioms HolomorphicAnosov.zhang_theorem_1_3

-- The eight audit bindings should introduce no further axioms.
#print axioms HolomorphicAnosovAudit.target_A_matches
#print axioms HolomorphicAnosovAudit.target_11_matches
#print axioms HolomorphicAnosovAudit.target_12_matches
#print axioms HolomorphicAnosovAudit.target_13_matches
#print axioms HolomorphicAnosovAudit.wrapper_A_matches
#print axioms HolomorphicAnosovAudit.wrapper_11_matches
#print axioms HolomorphicAnosovAudit.wrapper_12_matches
#print axioms HolomorphicAnosovAudit.wrapper_13_matches
