import Comparator.Solution

/-!
Private definitional-semantic audit for commit 65f2b33a7309de661a8500e4642e5609a537a8ff.
Read together with VerifyStatements.lean and the source-level correspondence report.

The `rfl` checks below require the actual imported predicates to unfold to the specified
mathematical content. Structure definitions and their fields are additionally printed.
No axiom or admitted proof is introduced.
-/

open scoped ContDiff Bundle
open HolomorphicAnosov

universe u v

namespace HolomorphicAnosovDefinitionAudit

attribute [local instance] HolomorphicAnosov.complex_isManifold_real

example (d : ℕ) : ComplexModel d = (Fin d → ℂ) := rfl

example {d e : ℕ} {X : Type u} {Y : Type v}
    [TopologicalSpace X] [ChartedSpace (ComplexModel d) X]
    [TopologicalSpace Y] [ChartedSpace (ComplexModel e) Y] :
    Biholomorph d e X Y = Diffeomorph (complexModel d) (complexModel e) X Y ∞ := rfl

-- Complex rank one means a genuine complex line whose realification is the given fibre.
example {d : ℕ} {X : Type u}
    [TopologicalSpace X] [ChartedSpace (ComplexModel d) X]
    (S : RealTangentDistribution (realModel d) X) :
    HasComplexRankOne S ↔
      ∀ x : X, ∃ K : Submodule ℂ (TangentSpace (complexModel d) x),
        Module.finrank ℂ K = 1 ∧
          (K.restrictScalars ℝ).map
            (complexTangentToReal d x).toLinearEquiv.toLinearMap = S x := Iff.rfl

-- Holomorphicity means a local independent holomorphic frame spanning the actual fibres.
example {d : ℕ} {X : Type u}
    [TopologicalSpace X] [ChartedSpace (ComplexModel d) X]
    [IsManifold (complexModel d) ∞ X]
    (r : ℕ) (P : (x : X) → Submodule ℂ (TangentSpace (complexModel d) x)) :
    IsHolomorphicTangentSubbundle r P ↔
      ∀ x : X, ∃ (U : Set X) (s : Fin r → (y : X) → TangentSpace (complexModel d) y),
        x ∈ U ∧ IsHolomorphicTangentFrame U s ∧
          ∀ y ∈ U, Submodule.span ℂ (Set.range (fun i ↦ s i y)) = P y := Iff.rfl

example {d r : ℕ} {X : Type u}
    [TopologicalSpace X] [ChartedSpace (ComplexModel d) X]
    [IsManifold (complexModel d) ∞ X]
    (U : Set X) (s : Fin r → (y : X) → TangentSpace (complexModel d) y) :
    IsHolomorphicTangentFrame U s ↔
      IsOpen U ∧
        (∀ i, ContMDiffOn (complexModel d) (complexModel d).tangent ∞
          (fun y ↦ (⟨y, s i y⟩ : TangentBundle (complexModel d) X)) U) ∧
        ∀ y ∈ U, LinearIndependent ℂ (fun i ↦ s i y) := Iff.rfl

-- The datum requires one common positive iterate and the actual complementary splitting.
example {d : ℕ} {X : Type u}
    [TopologicalSpace X] [ChartedSpace (ComplexModel d) X]
    [IsManifold (complexModel d) ∞ X]
    (f : Biholomorph d d X X) (a : AnosovDatum f) : 1 ≤ a.k := a.one_le_k

example {d : ℕ} {X : Type u}
    [TopologicalSpace X] [ChartedSpace (ComplexModel d) X]
    [IsManifold (complexModel d) ∞ X]
    (f : Biholomorph d d X X) (a : AnosovDatum f) (x : X) :
    IsCompl (a.splitting.stable.toDistribution x)
      (a.splitting.unstable.toDistribution x) := a.splitting.isCompl x

example {d : ℕ} {X : Type u}
    [TopologicalSpace X] [ChartedSpace (ComplexModel d) X]
    [IsManifold (complexModel d) ∞ X]
    (f : Biholomorph d d X X) (a : AnosovDatum f) :
    letI : Bundle.RiemannianBundle (fun x : X ↦ TangentSpace (realModel d) x) :=
      ⟨a.metric.toRiemannianMetric⟩
    ∀ x, ‖(restrictedIterateDerivative f.toReal a.splitting.stable.toDistribution
      a.splitting.stable_map a.k x).toContinuousLinearMap‖ < 1 := a.stable_contracting

example {d : ℕ} {X : Type u}
    [TopologicalSpace X] [ChartedSpace (ComplexModel d) X]
    [IsManifold (complexModel d) ∞ X]
    (f : Biholomorph d d X X) (a : AnosovDatum f) :
    letI : Bundle.RiemannianBundle (fun x : X ↦ TangentSpace (realModel d) x) :=
      ⟨a.metric.toRiemannianMetric⟩
    ∀ x, ‖(restrictedIterateDerivative f.toReal a.splitting.unstable.toDistribution
      a.splitting.unstable_map a.k x).symm.toContinuousLinearMap‖ < 1 := a.unstable_contracting

-- The final complex model includes an invertible complex lattice automorphism,
-- a biholomorphism, the true eigenvalue condition, and the pointwise conjugacy equation.
example {d : ℕ} {X : Type u}
    [TopologicalSpace X] [ChartedSpace (ComplexModel d) X] (f : X → X) :
    HasHyperbolicComplexTorusModel (d := d) f ↔
      ∃ (L : FullComplexLattice d) (A : LatticeLinearEquiv L)
        (h : Biholomorph d d X (ComplexTorus L)),
        (∀ μ : ℂ, Module.End.HasEigenvalue A.linear.toLinearMap μ → ‖μ‖ ≠ 1) ∧
          ∀ x : X, h (f x) = quotientLinearEquiv A (h x) := Iff.rfl

example (n : ℕ) (X : Type u) [TopologicalSpace X] (f : X → X) :
    HyperbolicRealToralConjugacy n X f ↔
      ∃ (A : Matrix.GeneralLinearGroup (Fin n) ℤ)
        (h : X ≃ₜ UnitAddTorus (Fin n)),
        (∀ μ : ℂ,
          Module.End.HasEigenvalue
            (Matrix.mulVecLin (fun i j : Fin n ↦ (A i j : ℂ))) μ → ‖μ‖ ≠ 1) ∧
        ∀ x : X, h (f x) = integralToralMap A (h x) := Iff.rfl

-- This checks the exact extra topological premise; it does NOT prove that premise.
example : HomotopyTorusRigidity.{u} ↔
    ∀ (n : ℕ),
      5 ≤ n →
        ∀ (M : Type u) [TopologicalSpace M]
          [ChartedSpace (EuclideanSpace ℝ (Fin n)) M],
          ClosedSmoothRealManifold n M →
            Nonempty (ContinuousMap.HomotopyEquiv M (UnitAddTorus (Fin n))) →
              Nonempty (Homeomorph M (UnitAddTorus (Fin n))) := Iff.rfl

end HolomorphicAnosovDefinitionAudit

set_option pp.universes true
set_option pp.fullNames true
set_option pp.proofs false

-- Inspect the actual imported declarations, not README descriptions.
#print HolomorphicAnosov.ComplexModel
#print HolomorphicAnosov.complexModel
#print HolomorphicAnosov.realModel
#print HolomorphicAnosov.IsCompactComplexManifold
#print HolomorphicAnosov.Biholomorph
#print HolomorphicAnosov.ContinuousRealTangentSubbundle
#print HolomorphicAnosov.InvariantRealTangentSplitting
#print HolomorphicAnosov.restrictedIterateDerivative
#print HolomorphicAnosov.AnosovDatum
#print HolomorphicAnosov.complexTangentToReal
#print HolomorphicAnosov.HasComplexRankOne
#print HolomorphicAnosov.IsHolomorphicTangentFrame
#print HolomorphicAnosov.IsHolomorphicTangentSubbundle
#print HolomorphicAnosov.FullComplexLattice
#print HolomorphicAnosov.ComplexTorus
#print HolomorphicAnosov.complexTorusChartedSpace
#print HolomorphicAnosov.LatticeLinearEquiv
#print HolomorphicAnosov.quotientLinearEquiv
#print HolomorphicAnosov.ComplexLinearHyperbolic
#print HolomorphicAnosov.integralToralMap
#print HolomorphicAnosov.HyperbolicRealToralConjugacy
#print HolomorphicAnosov.HasHyperbolicComplexTorusModel
#print HolomorphicAnosov.ClosedSmoothRealManifold
#print HolomorphicAnosov.HomotopyTorusRigidity

-- These Mathlib interfaces rule out weakened meanings of lattice, norm, homotopy,
-- and the misleading inference that a semiconjugacy witness h need not be invertible.
#print IsZLattice
#print Bundle.RiemannianMetric
#print Bundle.RiemannianBundle
#print ContinuousMap.HomotopyEquiv
#print Diffeomorph
#print Function.Semiconj
#print Module.End.HasEigenvalue
