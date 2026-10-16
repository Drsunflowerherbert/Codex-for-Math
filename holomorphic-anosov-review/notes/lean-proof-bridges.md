# Static audit of Lean proof bridges

*Publication note: any `extension/evidence/`, `working-reference/`, or source-copy filenames in these notes identify excluded working references. Third-party PDFs, scans, OCR and raw article-response logs are not bundled. Included search/access metadata is under `../evidence/`; use the primary-source URLs for original texts.*


Repository inspected: `pinned HolomorphicAnosov source checkout`.

Pinned commit independently checked with `git rev-parse HEAD`:
`65f2b33a7309de661a8500e4642e5609a537a8ff`.

Scope: read-only inspection of actual Lean definitions, theorem hypotheses and proof bodies for the Anosov input, invariant quotient connection, curvature/regularity passages, complete leaf coordinates, global extension/developing-map bridge, Section 4 distributional regularity, and selected Ghys/Franks–Manning/Bochner–Montgomery bridges. No build, package setup, installation, or repository-supplied executable was run. This is a source audit, **not kernel verification**, and it does not establish the absence of issues throughout the several thousand file dependency tree.

## Assessment

Within the paths inspected, I found **no demonstrated conclusion-smuggling or admitted mathematical bridge**. The records and intermediate lemmas I inspected contain substantive geometric hypotheses and proof bodies. Several alarming comments and filenames are stale: in particular, a comment saying that a named provider retains a `sorry` is followed by a proof that calls a supplied curvature-sequence theorem, whose body constructs and estimates the sequence.

There is one important explicit limitation: the advertised main target is **conditional on `HomotopyTorusRigidity`**. This is visible in its theorem type, rather than hidden in an instance or the Anosov record. It is appropriate to describe that target as a formal derivation from a separately supplied topology theorem; an unconditional kernel verification of Theorem A has not been established by this inspection.

The formal global-holonomy interface asks for whole-leaf biholomorphic extensions of actual local holonomy germs with coherence laws. It does **not** assert that the extension sends every arbitrary point to its original stable leaf. This absence, by itself, is **not a demonstrated flaw in the classification proof**: the downstream code uses the germ-compatible entire extension to compare holomorphic projective developing maps, then obtains equality of their omitted poles by the identity theorem. This is a mathematically meaningful way to avoid needing arbitrary-point leaf tracking at that intermediate step.

## 1. Genuine Anosov input

`HolomorphicAnosov/Paper/Zhang/Anosov.lean:33–57` defines `AnosovDatum` by:

- a smooth Riemannian metric;
- an invariant continuous real tangent splitting;
- an iterate `k ≥ 1`;
- strict contraction of its stable restricted derivative and inverse unstable restricted derivative in that metric.

The splitting itself is in `HolomorphicAnosov/Dynamics/Anosov/InvariantRealTangentSplitting.lean:27–41`: two continuous real tangent subbundles, pointwise complementarity, and exact image equalities under the actual manifold derivative. No torus model, transitivity, global holonomy, or holomorphicity of the invariant distributions is a field of these records.

This matters because a plausible formalisation failure would be to place a later conclusion inside the meaning of “Anosov.” That particular failure is not present in the definitions inspected.

## 2. Main theorem and the explicit topology premise

`HolomorphicAnosov/Targets/TheoremA.lean:27–58` takes the compact complex manifold, biholomorphism, `AnosovDatum`, complex rank-one alternative, and an additional argument

```lean
(HS : HomotopyTorusRigidity.{u})
```

The stable-rank-one branch invokes Theorems 1.1, 1.3, then 1.2, and proves hyperbolicity of the final complex linear model; the unstable-rank-one branch applies the stable branch to the inverse map. Thus its chain is concrete rather than a direct projection of a model field.

`HolomorphicAnosov/Topology/HomotopyTorusRigidity.lean:33–41` defines `HomotopyTorusRigidity` as the schema that every closed smooth real `n`-manifold, `n ≥ 5`, genuinely homotopy equivalent to the standard real `n`-torus is homeomorphic to it. This file supplies a proposition definition, not a proof or axiom asserting it. The target docstrings explicitly say “assuming homotopy-torus rigidity.”

The same explicit argument occurs in `Targets/Theorem11.lean:1725–1761`, `Targets/Theorem13.lean:462` onward, and `Paper/Zhang/InvariantHolomorphicOneForm.lean:120` onward. Theorem 1.2's public statement, `Targets/Theorem12.lean:74–97`, instead has a torus-homeomorphism assumption corresponding to the paper's own hypothesis and does not take `HS`.

The topology premise is used at the appropriate point: `Paper/Zhang/OriginalGlobalHolonomyTorusHomeomorph.lean:22–47` first obtains an actual simply connected Euclidean universal cover and a faithful translation representation, then calls the torus-homeomorphism construction with `HS`. `Paper/Zhang/Proposition29.lean:28–59` obtains that homeomorphism before applying the Anosov real-toral conjugacy bridge. I did not find a circular use of a topological torus hypothesis in Theorem 1.1's holonomy construction.

## 3. Invariant connection and curvature

### Definitions are geometric

`Geometry/Manifold/VectorBundle/HolomorphicQuotientLineConnection.lean` uses the literal tangent quotient as the fibre (`:29–35`); local quotient sections with local holomorphic lifts (`:39–44`); normalized local holomorphic quotient frames (`:48–53`); and frame connection forms satisfying the standard gauge law (`:69–76`).

Continuity is continuity of coordinate connection forms (`:97–103`). Flatness explicitly requires real differentiability plus vanishing alternating derivative (`:119–127`). Compatibility is the type-(1,0) condition together with the quotient Bott bracket formula (`:149–165`). Invariance is the explicit frame pullback formula (`:197` onward). None defines flatness or compatibility by the theorem's eventual conclusion.

### Proof construction is present

`Paper/Zhang/InvariantConnection.lean:23–155` constructs smooth compatible pullback sequences using the connection-calculus seed and pullback constructions, obtains a continuous compatible invariant limit, and proves uniqueness by contraction. Its hypotheses include holomorphicity of the unstable bundle, but that is supplied by the separately proved rank-one Ghys bridge, rather than included in `AnosovDatum`.

`Paper/Zhang/ConnectionFlat/NativePullbackCurvatureSequence.lean:82` onward constructs a smooth compatible sequence `Ds`, defines the curvature evaluations as

```lean
fderiv ℝ (A n) z v w - fderiv ℝ (A n) z w v
```

and proves weak convergence using the actual C⁰ connection limit and integration by parts. Its final L² claim calls `native_smooth_pullback_curvature_l2_decay`.

That latter theorem is not merely a hypothesis package: `Paper/Zhang/ConnectionFlat/NativeSmoothPullbackCurvatureL2Decay.lean:55` onward has a `:= by` proof that obtains local foliation charts and connection curvature representatives, proves curvature annihilation on the unstable hyperplane, proves pullback naturality, and proceeds to the determinant/Jacobian bound. I read the statement and the chart/kernel/naturality portion; I did not independently audit every lower singular-value, volume or integration dependency.

`ConnectionNativeCurrentClosedFlat.lean:229–264` obtains the actual curvature sequence and uses uniqueness of limits to prove the closed-current identity. `:408–465` then derives holomorphic scalar coefficients from the type-(1,0) closed current, obtains smoothness, and derives classical flatness. It does not simply assume the invariant connection is differentiable or flat.

**Stale-comment trap:** `ConnectionNativeCurrentClosedFlat.lean:197–215` says the native-box/L² steps remain in “this named provider's `sorry`.” The actual provider at `:229` has the proof just described. Likewise a filename ending `CurvatureExistenceGluingGap.lean` contains a full displayed theorem proof: `exists_curvature_representative_gap` constructs its representative from selected charts and proves overlap independence. These names/comments are not evidence of an actual admission at this commit.

## 4. Complete coordinates and the global extension interface

`Paper/Zhang/CompleteStableCoordinates.lean:977` onward assumes the actual Anosov data, continuous complex stable subbundle, equality with the original real stable distribution, an actual continuous compatible invariant quotient connection, and native leaf data. The conclusion supplies whole-leaf complex diffeomorphisms to the stable tangent lines, normalization at the marked point, the local parallel-coordinate germ, iterate formulas, and continuous inverse evaluation. Its proof begins from uniform local coordinates and intrinsic leaf metric contraction rather than taking whole-leaf coordinates as a hypothesis.

`Paper/Zhang/GlobalUnstableHolonomy.lean:114` onward starts from ordinary `AnosovDatum` and stable real rank two. In the proof:

1. it obtains stable foliations from all-iterate Hermitian Anosov estimates;
2. derives holomorphicity of the complex unstable bundle;
3. constructs the invariant connection;
4. constructs local parallel coordinates and source-compatible product boxes;
5. obtains `complete_stable_coordinates`;
6. identifies these source-native leaves with intrinsic receiving leaves;
7. proves linearity of all local plaque transport germs;
8. invokes the complete-linear-coordinate extension theorem.

The extension theorem is `Geometry/Holonomy/CompleteLinearCoordinatesGlobalHolonomyG8.lean:1165` onward. Its hypotheses are complete leaf coordinates, their zero normalization, linearity of actual local plaque germs in those coordinates, and endpoint-fixed path homotopy on the transverse leaves. It constructs each entire map by conjugating the coefficient linear equivalence by the supplied complete coordinates and proves germ compatibility, homotopy independence, composition and reversal. Those complete coordinates and local linearity are supplied by the preceding construction, not added to the final target's hypotheses.

### Exact strength of `GlobalSHolonomyData`

`Geometry/GlobalHolonomy.lean:48–75` has fields for local continuation, a whole-leaf biholomorphism for each intrinsic path, equality of its marked germ with the actual local continuation, and restriction/concatenation/reversal laws. There is no field asserting stable-relatedness of arbitrary `z` and its transported point.

This difference from geometric whole-leaf path lifting needs care in any explanatory report. An analytic continuation of a transverse germ is not automatically a global leafwise holonomy lift. Nevertheless, the code does not need to infer that stronger property to get its next result.

## 5. How the downstream developing-map bridge uses the weaker interface

`Paper/Ghys/ProjectiveDeveloping.lean:52–156` takes ordinary compact holomorphic Anosov data with rank-one unstable bundle, and returns the complete unstable affine structures and projective developing data on genuine covering maps, including lifted-leaf ranges and omitted-pole charts. Its proof at `:157` onward obtains the native identification and transverse development. Thus this major Ghys implication is stated with a proof body; it is not an extra “Ghys certificate” argument to the target.

The crucial bridge can be read directly in `Geometry/CoveringGlobalHolonomyDevelopingGerm.lean`:

- `covering_global_holonomy_developing_germ`, `:212` onward, obtains an equality of germs for the developed maps on pointed transverse leaf lifts, using actual local plaque-chain holonomy and covering uniqueness.
- `covering_global_holonomy_poles_eq`, `:294–356`, then uses holomorphicity on the connected source leaf to extend that equality to an equality of entire developed maps. The key actual proof is `:337–355`: equality of germs; holomorphic identity theorem; surjectivity of the transported whole-leaf biholomorphism; equality of ranges; equality of complements of singleton poles.
- `covering_global_holonomy_common_pole`, `:361` onward, applies this along lifted stable paths, obtains constancy on both types of lifted box slices, and concludes local constancy of the pole function and then global constancy on the connected cover.

`Paper/Ghys/CompleteGlobalHolonomyAffineCover.lean:309` onward consumes that common-pole result, chooses an affine chart omitting the common pole, constructs the affine developing map, supplies global leaf coordinates and a product homeomorphism, and derives translation deck action.

The independent mathematical core is sound at this level: if `D_x` and `D_y` map their respective entire complex leaves onto the projective line minus one point and an entire biholomorphism `H_xy` intertwines them on an open germ, the identity theorem gives `D_x=D_y∘H_xy` everywhere, so their ranges and omitted points coincide. This needs germ-compatible entire biholomorphic extension, not a pre-existing proof of leafwise tracking for every point. The many lower statements supplying these hypotheses have not all been independently verified here.

## 6. Section 4 regularity and distributional passage

`Paper/Zhang/InvariantHolomorphicOneForm.lean:120` onward has `HS` explicit and derives the toral model using Theorem 1.1; it then constructs the scalar projection and descends its differential. It does not take the desired nowhere-vanishing eigenform as a final-theorem input.

The stand-alone intermediate theorem `Paper/Zhang/StableVectorHolomorphic.lean:41–77` does take that eigenform and a continuous normalized stable section, as is appropriate for the paper's Lemma 4.3. Its proof at `:88–136` obtains smooth normalized approximations and applies a distributional section criterion.

The substantive approximation theorem is `Paper/Zhang/StableVectorPublic/NormalizedPullbackTestSequence.lean:24` onward. Its input has the invariant form and genuine Anosov data; it does not take the desired approximation sequence or L² convergence as a hypothesis. The proof constructs

```lean
sn n x = μ ^ n • (mfderiv ... ((f : X → X)^[n]) x).inverse
  (e₀ ((f : X → X)^[n] x))
```

then establishes uniform coefficient error bounds and a Jacobian-dominated square bound before integrating on compact chart test supports. I inspected these construction and estimate steps; I did not recheck every lower determinant/volume lemma.

`Analysis/Distribution/HolomorphicSectionCriterion.lean:141–167` requires continuous target section, weak convergence of its coefficients, and weak vanishing of antiholomorphic derivatives, and concludes complex smoothness of the actual total-space section. The proof uses scalar current holomorphic regularity (`:195–197`), identifies the continuous coefficient with its holomorphic representative by integration against test functions (`:202` onward), and assembles local bundle regularity. It is not a definition equating distributional holomorphicity with the claimed smooth result.

## 7. Cited-result bridges: proof bodies versus assumptions

| Bridge | Actual source evidence | Audit result |
|---|---|---|
| Ghys Prop. 2.2, rank one implies complementary holomorphic foliation | `Paper/Zhang/RankOneStableHolomorphicUnstable.lean:43` onward derives local first integrals using Ghys flowbox/holonomy estimates; `Paper/Ghys/StableHolonomyHolomorphic.lean:66` onward has ordinary Anosov inputs and derives holomorphicity through comparison limits | A proof chain is supplied; not a target hypothesis or axiom in the inspected files. Lower comparison proofs not exhaustively audited. |
| Ghys complete/projective development | `Paper/Ghys/ProjectiveDeveloping.lean:52–162`; `Paper/Ghys/CompleteGlobalHolonomyAffineCover.lean:73` onward | Actual geometric hypotheses and proof bodies. Omitted-pole bridge independently reconstructed above. |
| Higher-dimensional homotopy torus rigidity | `Topology/HomotopyTorusRigidity.lean:33–41`; explicit `HS` in main targets | **Assumed explicitly**, not proved in this repository file. Material limit to an unconditional formalisation claim. |
| Franks–Manning | `Topology/FranksManning.lean:3868–3926` states classification on the original smooth manifold with actual invariant continuous subbundles, actual metric contraction estimates and a torus homeomorphism. Proof constructs lift data and proves surjectivity and conjugacy | A proof body and many named lower geometric/topological dependencies are supplied. Their sheer extent prevents full audit here. No extra Franks classification certificate parameter appears in this theorem. |
| Bochner–Montgomery regularity | `Paper/Zhang/FreeTransitiveVectorOrbitDiffeomorphism.lean:20–53` derives orbit diffeomorphism from continuous action, genuine biholomorphic slices, freeness, transitivity and dimension. `Paper/Zhang/VectorActionOrbitSmooth.lean:38` onward derives smooth orbit maps. `Geometry/Manifold/OneParameterSmoothGenerator.lean:73–181` constructs local averaged coordinates and a generator | A substantive proof chain is supplied. Smooth parameter dependence is not taken as an input to the public action theorem. Lower Montgomery derivative-continuity and averaging lemmas not exhaustively audited. |

## 8. Admitted proofs / unsafe code observations

A targeted textual scan of the inspected `Paper/Zhang`, `Geometry/Holonomy`, and connection-current files found no active `axiom`, `opaque`, `unsafe`, `sorry`, or `admit` declaration/token. Hits were ordinary English (“admits”) or the stale comment described above. This was a focused scan, not the coordinating reviewer's repository-wide declaration/import-closure audit; it cannot rule out admissions in uninspected imports or prebuilt artifacts.

No denial, approval blocker, uncertain external action, public write, or author contact occurred. The remaining limitations are verification scope: no Lean build/kernel run, no exhaustive audit of every dependency, and the explicit unproved `HS` premise.
