# Independent adversarial semantic check of the Lean statements

> Historical source-review track. The later [compiled follow-up](../evidence/compiled-verification/deliverables/verification-method.md) built the pinned solution and checked full types, selected definitions and axiom lists. Statements below about no Lean execution describe this earlier track. The explicit HS qualification and original cited-source audit limits remain.

*Publication note: any `extension/evidence/`, `working-reference/`, or source-copy filenames in these notes identify excluded working references. Third-party PDFs, scans, OCR and raw article-response logs are not bundled. Included search/access metadata is under `../evidence/`; use the primary-source URLs for original texts.*


Inspected repository: `extension/formalisation/`, pinned commit **65f2b33a7309de661a8500e4642e5609a537a8ff**. Comparator manuscript: exact supplied arXiv:2609.37695v3, 13 October 2026, SHA-256 **3c8287bf41d153c7f0d0950b8a4b477546229333ee66ba7e9ae60e6a387920c6**.

This was a bounded independent source inspection, challenging the conclusions in `lean-semantic-correspondence.md`. I read the principal definitions, the target/wrapper signatures, selected actual derivative/metric/realification bridges, the holonomy receiving interface, and the application of the explicit topological premise. **No repository code, Lean process, build, installation, or repository-provided script was executed.** Shell commands only read and searched source files and wrote this private note.

## Result

I found **no additional semantic mismatch, vacuous hypothesis, or weakened conclusion** in the inspected interfaces. The main qualification in the first semantic report is real and independently confirmed: the advertised target theorems A, 1.1, and 1.3 require an explicit proof of `HomotopyTorusRigidity`; 1.2 does not. These targets therefore do not, by themselves, supply unconditional Lean statements of all four paper results.

This is an adversarial source-level conclusion, not a kernel verification. Neither this inspection nor the coordinating reviewer's lexical import-closure scan establishes compilation or the actual compiled declarations' `#print axioms` output.

## Attempts to find a semantic escape

### 1. A fake Anosov norm, or an arbitrary derivative equivalence

`Paper/Zhang/Anosov.lean:33–57` packages an actual smooth Riemannian metric, an invariant complementary real tangent splitting, one common `k ≥ 1`, and the two strict operator-norm bounds. Its stable operator is the forward derivative restricted to the stable fibre; its unstable operator is the inverse of the forward derivative restricted to the unstable fibre. The source and target fibres are correct.

`Dynamics/Anosov/RestrictedIterateDerivative.lean:32–39` constructs this equivalence by restricting `(realIterate I g n).mfderivToContinuousLinearEquiv` to the invariant submodules. It is not an arbitrary linear isomorphism whose norm could be chosen independently of the dynamics. The underlying map `g` is a genuine smooth diffeomorphism, so the derivative is not being obtained from a nondifferentiable-map fallback.

The local `RiemannianBundle` instance in the bounds installs the selected metric's actual tangent-fibre norms. The locked Mathlib source copied at `source-evidence/mathlib/Mathlib/Topology/VectorBundle/Riemannian.lean:370–378` requires a symmetric bilinear inner product and strict positivity on every nonzero vector. Lines 420–444 give the norm instance compatible with the existing fibre topology. This rules out a zero seminorm and an unrelated topology. `ContinuousRealTangentSubbundle.lean:22–30` likewise uses the topology induced by inclusion into the actual tangent bundle.

The pointwise fixed-iterate definition does not add an illicit uniformity assumption or omit ordinary uniform hyperbolicity. `Paper/Zhang/FixedBlockUniformAnosovEstimates.lean:70–120` proves local bounds for these exact operators, `:165–199` assembles a common compact bound below one, and `:301–316` states all-iterate exponential bounds in the original metric. I inspected this assembly, not every lower operator-norm lemma.

**Assessment:** faithful interface; no norm/derivative escape found.

### 2. An empty, disconnected, boundary, or noncomplex manifold

`Paper/Zhang/ComplexManifold.lean:16–19` requires the selected topology and atlas, Hausdorffness, second countability, compactness, connectedness, and `IsManifold (complexModel d) ∞`. Mathlib's `ConnectedSpace` includes nonemptiness. `Geometry/ComplexModel.lean:14–22` uses the entire finite-dimensional model `Fin d → ℂ`, with `modelWithCornersSelf`, rather than a boundary model. `Geometry/Biholomorph.lean:12–15` abbreviates `Diffeomorph` **over ℂ**, including complex smoothness of both directions. It is not ordinary real smoothness renamed holomorphicity.

The auxiliary real-recharting construction does not change the manifold's topology: `Targets/Theorem12Support/RealRechart/Recharted.lean:10–14` is a type copy with precisely the original topology; `identityDiffeomorph.lean:27–34` supplies a smooth identity under the linearly re-expressed atlas.

**Assessment:** ordinary compact connected complex manifolds and genuine biholomorphisms are used. The `d=0` branch in 1.2 is a harmless additional point-torus case.

### 3. Real rank one substituted for complex rank one

`Geometry/Manifold/VectorBundle/ComplexTangentRankOne.lean:15–21` requires, at every point, a complex submodule with `finrank ℂ = 1` whose canonical realification equals the actual selected real distribution. It gives real rank two, not real rank one. Theorem A uses a disjunction of stable and unstable rank-one predicates (`Targets/TheoremA.lean:30–33`), and 1.1 uses stable complex rank one (`Targets/Theorem11.lean:1725–1731`).

The realification is not freely selected. `Geometry/ComplexTangent.lean:39–47` compares the same preferred chart after scalar restriction; `:55–77` proves coordinate-change compatibility. `Geometry/BiholomorphToReal.lean:17–24` preserves the actual equivalence, and `:55–66` identifies the actual real and complex derivatives under this realification.

**Assessment:** correct complex codimension-one condition; no hidden holomorphicity assumption in 1.1's final signature.

### 4. Arbitrary convenient subbundles substituted for the stable/unstable bundles

`IsHolomorphicTangentSubbundle` (`Geometry/Manifold/VectorBundle/HolomorphicTangentSubbundle.lean:18–24`) asks for local independent holomorphic frames in the actual complex tangent bundle. Its frame predicate (`HolomorphicTangentLocalFrame.lean:19–26`) requires an open neighborhood, actual complex `ContMDiffOn` total-space sections, and pointwise complex linear independence. The syntactically global section variables only need regularity on this neighborhood; arbitrary extension outside it is allowed, as in an ordinary local-frame definition.

Crucially, both Theorem 1.2's hypotheses (`Targets/Theorem12.lean:78–87`) and Theorem 1.3's conclusion (`Targets/Theorem13.lean:469–475`) equate these complex subbundles' realifications with the **original datum's** stable and unstable distributions. They cannot be unrelated holomorphic subbundles selected to make the statement easy.

**Assessment:** faithful holomorphic-subbundle hypotheses/conclusion.

### 5. A manufactured torus structure, semiconjugacy alone, or omitted hyperbolicity

`FullComplexLattice.lean:10–13` requires a discrete integer submodule in the ordinary finite-dimensional complex vector space with full real span. Its discrete-topology field concerns the inherited subtype topology. `Quotient.lean:12–13` is the actual additive quotient by that subgroup. `Charts.lean:19–22` chooses local inverse charts of the natural quotient projection; its complex structure is not transported from the source manifold merely to manufacture a conclusion. `Charts.lean:94–154` explicitly derives locally translational transitions and complex smoothness.

`LatticeLinearEquiv.lean:12–15` is an actual complex-linear equivalence mapping the lattice onto itself. `LinearMap.lean:12–15` induces precisely its quotient automorphism. `Paper/Zhang/TorusModel.lean:19–24` requires a genuine biholomorphism to this torus and tests every complex eigenvalue for unit modulus. The `Function.Semiconj` equation is full conjugacy because the supplied biholomorphism is bijective.

The real target likewise uses an invertible integer matrix, a true homeomorphism, the actual toral matrix map, and absence of unit-modulus complexified eigenvalues (`HyperbolicRealToralConjugacy.lean:14–20`; `IntegralToralMap.lean:10–13`). The formal 1.2 omits hyperbolicity exactly as the printed 1.2 does; Theorem A separately derives it (`Targets/TheoremA.lean:42–45`).

**Assessment:** no weakened torus/conjugacy conclusion.

### 6. Hidden global holonomy, transitivity, or leaf complex structures as final inputs

The final theorem signatures take the original Anosov datum and the printed rank/holomorphicity/topology assumptions, plus the explicit topological premise where stated. They do not take transitivity, preexisting global holonomy, or a toral classification certificate as extra final-theorem hypotheses.

The internal holonomy interface deserves a nuance. `Geometry/OriginalAnosovGlobalUnstableHolonomy.lean:69–112` records entire biholomorphic transports agreeing with genuine local holonomy germs, with restriction/composition/reversal consistency. It does not separately state in a field that every transported point globally stays on its original transverse leaf. This is not, on its own, a defect in the final theorem: the Ghys developing-map argument can recover global product structure from germ-compatible entire biholomorphic extensions. The independently reconstructed common-pole argument in `lean-proof-bridges.md` explains why this weaker-looking intermediate packaging still suffices. Its native complex atlas is required to be compatible with the actual real leaf atlas and to make the actual inclusion a holomorphic immersion (`Geometry/NativeLeafComplexUpgrade.lean:23–41`).

`Paper/Zhang/GlobalUnstableHolonomy.lean:114–169` supplies the internal data as an output from original Anosov hypotheses, with partitions explicitly identified with the actual forward/backward asymptotic relations and leaf derivative ranges with the original invariant distributions. A separate proof-bridge reviewer is auditing this larger construction; this note does not certify its entire chain.

**Assessment:** no additional semantic escape found; the intermediate interface must be interpreted according to its stated role rather than equated word-for-word with the paper's informal phrase “global holonomy.”

## The explicit topological premise

`Topology/HomotopyTorusRigidity.lean:33–40` is precisely:

> For every `n ≥ 5`, a closed smooth real n-manifold with a genuine homotopy equivalence to the standard n-torus admits a homeomorphism to that torus.

The closed-manifold package fixes its topology and Euclidean atlas and includes compactness, Hausdorffness, second countability, and smoothness (`ClosedSmoothRealManifold.lean:34–41`). A separate connectedness field is unnecessary in this premise because the homotopy equivalence to a connected torus supplies path connectedness. Its use of a whole Euclidean model imposes the usual boundaryless convention.

This is a genuine general topological recognition principle of the kind Ghys invokes on printed p. 598, not the paper's dynamical conclusion renamed. It mentions **no** Anosov map, complex structure, invariant distribution, holomorphicity, or conjugacy. Its input is homotopy equivalence, not a disguised homeomorphism. `Topology/RealTorusHomeomorphOfAffineCover.lean:25–51` first derives the genuine homotopy equivalence from a contractible cover and a faithful translation representation, packages the same original smooth manifold, and only then applies `HS`. The target group `Multiplicative ℂ` at `:33` is the standard multiplicative notation for the **additive** complex group, as appropriate for translations; it is not the multiplicative group of nonzero complex scalars.

The premise has no supplied proof in the inspected interface. It is explicitly passed to A, 1.1, and 1.3 (`Targets/TheoremA.lean:33`; `Theorem11.lean:1730`; `Theorem13.lean:467`), and absent from 1.2 (`Theorem12.lean:74–92`). The comparator wrappers preserve this distinction (`Comparator/Solution.lean:23–86`). Therefore the conditionality is not a scanner artefact or an invisible axiom: it is visible in the mathematical statements themselves. The classical theorem may be used in an ordinary mathematical proof, but a Lean proof of this schema is still needed for an unconditional kernel-checked corollary of those targets.

## Nonvacuity sanity check

There is an ordinary mathematical model for the inspected geometric/dynamical hypotheses: on `C²/(Z[i])²`, the integer matrix `[[2,1],[1,1]]` preserves the full Gaussian-integer lattice. Its eigenvalues are `(3 ± sqrt(5))/2`, with complex one-dimensional stable and unstable eigenspaces. In a constant Hermitian/Riemannian metric with orthogonal eigenspaces, both required contractions are `(3-sqrt(5))/2 < 1`, already for `k=1`. The torus is compact connected and the map biholomorphic. Thus the intended hypotheses admit a concrete standard example; there is no evident semantic contradiction behind the conclusions. This is a mathematical sanity check, not an independently elaborated Lean example.

## Limits and reporting recommendation

Report the source signatures as faithful to the paper's geometric/dynamical meanings, **with the explicit HS qualification**. Report the absence of obvious lexical admissions separately from semantic correspondence. Do not call the repository formally verified on the evidence of either audit: no compiler/kernel run, compiled import inspection, or `#print axioms` check was performed. The 4,230-module solution closure is far beyond the bounded source inspection here. I found no reason to amend the first semantic report's substantive conclusion.

No external/public write, author contact, approval denial, or uncertain mutation occurred. The remaining limitations are verification scope and the explicit undischarged topological premise.
