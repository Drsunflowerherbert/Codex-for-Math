# Independent challenge of the proposed Schwarzian replacement proof

*Publication note: any `extension/evidence/`, `working-reference/`, or source-copy filenames in these notes identify excluded working references. Third-party PDFs, scans, OCR and raw article-response logs are not bundled. Included search/access metadata is under `../evidence/`; use the primary-source URLs for original texts.*


Repository commit: **65f2b33a7309de661a8500e4642e5609a537a8ff**. This is a bounded independent follow-up to `lean-ghys-schwarzian-followup.md`. It inspects the actual source-level mathematical argument, without running Lean, compiling the repository, installing dependencies, or executing repository scripts.

## Conclusion

I find **no demonstrated mathematical flaw or hidden transitivity/full-support premise in the inspected immediate replacement argument**. The finite inverse-Jacobian budget and disjoint stable-path packing provide a coherent alternative to the questionable inference and overstrong disk assertion in the printed Ghys proof. This conclusion is conditional on the lower geometric providers supplying the source cores, continuous Schwarzian family, affine iterate calculus, and uniform stable shrinking with their stated meanings; this inspection does not verify their entire dependency trees or kernel acceptance.

The source therefore supplies a proposed alternative proof of the needed conclusion. It does **not** retrospectively validate the particular acim-to-transitivity inference printed in Ghys, nor does a static source inspection automatically repair a paper that merely cites that printed argument.

## Exact pieces challenged

* `Paper/Ghys/Proposition41.lean:34–105`: the public wrapper derives the affine family and completeness from Proposition 3.1, then calls Schwarzian vanishing and the Schwarzian-zero/Möbius criterion. No transitivity or measure-support input is added in the wrapper.
* `Paper/Ghys/Proposition41SchwarzianVanishing.lean:29–70`: the intermediate statement takes ordinary Anosov data, the true intrinsic foliation presentation, and an invariant continuous family of complete affine unstable-leaf structures. The extra holomorphicity input concerns the actual local holonomy representative. The theorem does not assume its own desired Schwarzian-zero conclusion.
* `Ghys/AnosovIntrinsicFoliationPresentation.lean:28–88`: its leaf partitions agree with actual asymptotic classes and its leaf inclusions are the native inclusions. Its structures do not contain a dense-orbit or full-support field.
* `Ghys/AffineProjectiveStructure.lean:527–548`: continuity along stable holonomy asks for continuous transported affine ratios of fixed triples. It does not say those ratios are constant. `AnosovIntrinsicFoliationPresentation.lean:97–109` requires the **dynamics** to act affinely, not the stable holonomy.

## 1. The budget counts roots correctly

The mathematical identity used is

`integral_y sum_(x in K, g(x)=y) C/|g'(x)|² = C * area(K)`

for a compact source core `K`, holomorphic `g` near `K`, and nonzero derivative there. This is valid. A finite local injectivity cover exists by compactness. Partition the source core into disjoint measurable ownership pieces subordinate to that cover. The images of different pieces may overlap: their contributions must be **added**, because different source roots are distinct. The inspected code does precisely that (`Analysis/Complex/FiniteInverseBranchBudget.lean:60–92,104–122,153–221`). It never replaces the root sum by one chosen inverse image on the whole target.

On each ownership piece the real Jacobian is `|g'|²`; change of variables cancels that factor with its reciprocal. I inspected the specialization in `Analysis/Complex/HolomorphicInverseWeightedArea.lean:43–73`: it uses an actual left inverse on the source piece, derives injectivity, restricts the complex derivative to a real derivative, and explicitly identifies the real determinant. The nonzero derivative rules out division by zero on active pieces. The application weight is finite and nonnegative.

`NativeStablePlaqueProducts.lean:674–724` applies the budget to a **compact anchor restriction** inside the open holomorphic domain, not to an arbitrary open source with a falsely finite root set. The restriction is the fixed compact transverse core intersected with the closed preimage of the receiving compact buffer. The source coordinate is injective, so reindexing its roots loses none and duplicates none.

The resulting bound is allowed to depend on the fixed original source family and its chosen affine coordinates. It is independent of the iterate and of the later number of paths. The displayed budget is chosen at `Proposition41SchwarzianVanishing.lean:80–92`, before the receiving path-packing choices. Summing over overlapping different source cores only increases the budget; the finite sum remains finite.

**Challenge outcome:** no invalid cover-integral step found.

## 2. Root coverage does not require recurrence

The elementary root-cover argument is explicit in `Topology/CompactLocalInjectiveBranches.lean:140–201`. For an arbitrary receiving point `z`, it takes a source-core representation of `f^(-n)(z)` (`:194–201`). The image of that source plaque contains `z`. Uniform stable shrinking puts its anchor into a larger receiving compact set and keeps the whole small plaque in the outer box. The box's stable projection is constant on that plaque, giving the correct root.

There are two separate positive buffers: the inner receiving core to the anchor restriction, and the anchor restriction to the whole receiving box. These are present in the statement and application; they are not replaced by an unsupported assertion that a nearby anchor automatically remains in the chart. Root finiteness follows from a finite injectivity cover of a compact source restriction (`:26–59`); it does not infer finite roots merely from isolated roots on an open domain.

The geometric application in `Geometry/Holonomy/NativeStablePlaqueProducts.lean:837–928` supplies the finite source-core cover, stable shrinking, projection constancy, and local injectivity, then invokes that elementary theorem. The finite source-core cover itself is produced by taking one actual compact product core with interior around every point and extracting a finite subcover (`:780–834`). There is no requirement that one orbit or one leaf be dense.

**Challenge outcome:** the inspected coverage mechanism uses global invertibility, compactness, and uniform stable contraction, not transitivity or support of a measure.

## 3. The path-packing order of quantifiers is correct

A continuous nonzero variation gives a fixed positive endpoint gap on a fixed planar receiving disk of positive area. Only **after** that disk and gap are chosen does the proof choose an arbitrary finite number `L` of disjoint stable-parameter paths. This is explicit in `Topology/ParallelPathsConvexOpen.lean:110–157` and its application at `Proposition41SchwarzianVanishing.lean:470–537`.

The paths can be chosen by translating a segment in a direction independent of its endpoint difference. Their disjointness requires real stable parameter dimension at least two. Here that dimension is `2*d-2`; if nonzero variation is possible it is indeed at least two. The zero-dimensional case is separately dismissed because the scalar field then has no stable variation. For surfaces the required dimension is exactly two, which is sufficient.

For each chosen finite family, compactness gives a positive minimum separation uniformly over the fixed receiving disk. The iterate `n` may depend on `L` and that separation. Uniform stable shrinking then ensures that one iterated source plaque meets at most one path. No uniform separation for an infinite path family is asserted or needed (`:538–579`).

Finite closed plaque pieces cover each path. The weighted variation estimate uses a simple path in the finite intersection graph and the triangle inequality (`Topology/FiniteClosedCoverVariation.lean:46–75`). Its packing refinement sums these inequalities and counts a piece at most once because that piece meets at most one chosen path (`:88–129`). Pieces need not be disks or connected, so the false stronger collinear-disc assertion from the printed argument is irrelevant to this replacement.

It follows for every `z` in the fixed receiving disk that `L*eta <= B_n(z)`. Integrating gives `L*eta*area(T) <= fixed_budget`. The density and iterate can change with `L`; the fixed positive area, gap, and budget cannot. The contradiction theorem explicitly permits exactly this quantifier order (`FiniteInverseBranchBudget.lean:266–279`).

**Challenge outcome:** no hidden exchange of limits, dependence on `L` in the wrong constant, or invalid infinite packing was found.

## 4. The remaining substantive lower inputs

The source-to-receiving Schwarzian identity is implemented at `Proposition41SchwarzianVanishing.lean:153–349`, followed by its within-plaque variation bound at `:369–393`. Mathematically the cancellation is legitimate: source and target unstable expressions of `f^n` are affine, so the Schwarzian chain rule gives a common `Schwarzian(G_n)` term; subtracting two stable-parameter evaluations cancels that term, leaving the receiving variation multiplied by `G_n'^2`. Dividing its absolute value gives the inverse-Jacobian weight used in the budget.

I inspected the immediate providers constructing the continuous scalar field (`Analysis/Complex/AffineHolonomyFamilySchwarzian.lean:330–393`) and bounding its values on source compact cores (`NativeStablePlaqueProducts.lean:650–670,727–776`). The field is actual Schwarzian data and is only assumed continuous before this argument; it is not defined to be zero. Complete affine coordinates give one planar coordinate on the entire source unstable leaf. Compact source-parameter cores give a finite variation bound.

However, the lower constructions of the invariant affine family, holomorphic local holonomy, native plaque products, and derivative/coordinate continuity remain substantial dependencies. I have not independently reconstructed every one of those lower Lean proofs. An error there would be a different finding from a demonstrated failure of the finite-budget/path-packing argument itself.

## Reporting recommendation

The earlier follow-up's narrow claim withstands this independent challenge: **the immediate alternative proof is mathematically coherent on its stated hypotheses, and no hidden full-support/transitivity premise or erroneous integral counting was identified.** Describe it as a source-level proposed replacement with substantial lower dependencies still unchecked and no kernel run. Do not describe it as verification of Ghys's disputed printed inference or as an unconditional formal-verification result.

No action was denied, blocked, or left with uncertain execution status. No public write or author contact occurred.
