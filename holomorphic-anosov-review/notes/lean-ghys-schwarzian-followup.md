# Targeted follow-up: Ghys Proposition 4.1 / Lemma 4.3

*Publication note: any `extension/evidence/`, `working-reference/`, or source-copy filenames in these notes identify excluded working references. Third-party PDFs, scans, OCR and raw article-response logs are not bundled. Included search/access metadata is under `../evidence/`; use the primary-source URLs for original texts.*


Pinned source: `65f2b33a7309de661a8500e4642e5609a537a8ff` in `pinned HolomorphicAnosov source checkout`.

This is a bounded static source audit prompted by two questions about the proof printed in Ghys (1995), p. 596: its overstated collinear-disc Fact 1, and its inference from the Schwarzian-diameter absolutely continuous invariant measure to transitivity and everywhere-positive density. No build or kernel check was run.

## Finding

The actual Lean source **does not follow Ghys's Markov/Schwarzian-diameter-measure argument** for this result. It supplies an explicitly described alternative proof by a finite inverse-Jacobian integral budget and arbitrarily many disjoint stable-parameter paths. In the inspected theorem and immediate supporting providers there is no hypothesis, theorem application, or conclusion asserting that an acim of the expanding Markov quotient implies transitivity/full support. There is also no use of containing discs with collinear centers or of a no-triple-cover inference.

Thus the source is **not evidence that the questionable original acim-to-transitivity inference has been formalized or justified**. It is evidence of a different proposed proof of the needed Schwarzian-vanishing conclusion. I found no hidden transitivity/full-support assumption in its inputs or immediate helper records. Its high-level replacement argument is mathematically coherent on the inspected hypotheses. The full lower dependency tree and kernel acceptance remain unchecked.

## Exact theorem and inputs

`HolomorphicAnosov/Paper/Ghys/Proposition41SchwarzianVanishing.lean:29–72` states `proposition_4_1_schwarzian_vanishing`. It takes compact holomorphic Anosov data, complex rank-one unstable distribution, an intrinsic Anosov foliation presentation, and an affine unstable-leaf family satisfying:

- affine action of the original dynamics;
- continuity along stable holonomy;
- completeness of each affine leaf structure.

It concludes that the Schwarzian of every actual holomorphic stable holonomy representative vanishes near its marked point in the chosen affine coordinates. It does **not** take transitivity, a Markov coding, an invariant measure, positive density, or full support.

The intermediate inputs do not encode the desired projectivity:

- `Ghys/AnosovIntrinsicFoliationPresentation.lean:28–87` records literal stable/unstable partitions, their agreement with asymptotic classes, native immersed leaves and compatible intrinsic charts.
- `Ghys/AnosovIntrinsicFoliationPresentation.lean:97` onward defines `ActsAffinely` by affine germs of **the dynamics**, rather than affine or projective stable holonomy.
- `Ghys/AffineProjectiveStructure.lean:527–548` defines `ContinuousAlongStableHolonomy` by common local prefix representatives and continuity of transported affine ratios. It does not require those ratios to be constant or the Schwarzian to vanish.
- `Ghys/AffineProjectiveStructure.lean:117–118` defines completeness by a genuine whole-leaf affine biholomorphism to the complex plane, plus simple connectedness.

The public wrapper `Paper/Ghys/Proposition41.lean:34–105` obtains that affine family and its properties from `proposition_3_1` at `:76–79`, applies Schwarzian vanishing at `:94`, then applies the Schwarzian-zero/Möbius criterion. Thus the affine-family assumptions of the intermediate theorem are derived before the final Ghys Proposition 4.1 conclusion is used.

## Replacement proof map

Write `S(z,s)` for the scalar Schwarzian field in one receiving box, where `z` is the complex transverse coordinate and `s` the stable parameter. A nonzero value would imply a nonzero variation from the diagonal value `S(z,s0)=0`.

1. **Finite source cores and finite budget.** `Proposition41SchwarzianVanishing.lean:79–96` obtains finitely many genuine compact native stable source cores covering the manifold and sets a finite budget equal to the sum, over source cores, of a uniform source Schwarzian-variation bound times the planar area of the corresponding compact transverse coordinate image.

   The supporting existence proof is `Geometry/Holonomy/NativeStablePlaqueProducts.lean:780–834`: build a core around every point from actual native stable plaques and a compact transverse neighborhood, prove its image contains a neighborhood of the point, then take a finite subcover. The record itself at `:229–246` has actual plaques, a receiving box, anchor data, an interior stable radius, and a compact transverse core. No recurrence or transitivity field is present.

2. **Inverse-Jacobian root density.** `Proposition41SchwarzianVanishing.lean:99–141` constructs, for every iterate and receiving compact core, a nonnegative measurable density

   \[
   B_n(z)=\sum_{i,t\text{ a root at }z}
       \frac{b_i}{|G_{n,i}'(\chi_i(t))|^2},
   \qquad \int_{\mathbb C} B_n\le B<\infty,
   \]

   where `G_{n,i}` is the receiving projection of the iterated unstable source transversal, and `b_i` bounds the source Schwarzian variation. This is an area-change budget; `B_n` is not an invariant density and may depend on `n` and the selected receiving compact core.

   The exact analytic provider is `Analysis/Complex/FiniteInverseBranchBudget.lean:153–221`: compact local injectivity gives finitely many branches, finite Borel ownership avoids multiple counting, and the inverse-Jacobian integral is exactly the weight times the source area. `:227–257` transports this through the actual injective source coordinate. `Geometry/Holonomy/NativeStablePlaqueProducts.lean:674–724` applies it to literal compact native anchor roots. These are proof bodies, not acim/transitivity certificates.

3. **Finite root cover of each receiving stable fibre.** `Proposition41SchwarzianVanishing.lean:142–151` calls `native_source_cores_eventual_root_cover`; its body is `Geometry/Holonomy/NativeStablePlaqueProducts.lean:837–928`. Uniform stable shrinking makes the whole image of each relevant stable plaque stay in the receiving box. Surjectivity of `f^n` and the finite source-core cover ensure every point of the receiving core is covered by one such iterated plaque. Its anchor has the same stable-fibre projection. Local injectivity on a compact anchor restriction makes the root set finite.

   This is also explicit in the elementary provider `Topology/CompactLocalInjectiveBranches.lean:140–201`: the cover is proved by taking the source-core representative of `f^{-n}(z)` (`:194–201`). There is no assumption that one particular orbit or leaf is dense.

4. **Schwarzian chain rule bounds variation on each small plaque.** `Proposition41SchwarzianVanishing.lean:153–349` proves the actual chain-rule identity, then obtains the bound

   \[
   |S(z,s)-S(z,s')|\le b_i/|G_{n,i}'(\chi_i(t))|^2
   \]

   for two points covered by the same iterated source stable plaque. Nonzero derivatives are obtained from receiving projection calculus, not assumed as uniform expansion or positive invariant density. `:350–393` ensures the relevant whole plaques stay in the box and transfers the bound to the covered point sets.

5. **Arbitrarily many disjoint stable paths.** If `S(z0,s1)≠0`, continuity gives one fixed closed planar ball `T` of positive area and a fixed positive endpoint gap `eta`. Because stable real dimension is at least two whenever nonzero variation is possible, one can choose, for every integer `L`, `L` disjoint parallel stable-parameter paths, each retaining that gap for every `z∈T`. This is `Proposition41SchwarzianVanishing.lean:470–537`, using `Topology/ParallelPathsConvexOpen.lean:30–107` and `:110` onward.

   The argument handles a zero-dimensional stable parameter trivially (`:477–482`) and uses real stable dimension `2d−2≥2` otherwise. For surfaces (`d=2`) this dimension is exactly two, so the same construction applies.

6. **Packing forces a contradiction to the fixed integral budget.** Uniform shrinking ensures that, for large enough `n`, one small iterated source plaque can meet at most one of the selected disjoint paths (`Proposition41SchwarzianVanishing.lean:538–579`). Each path is covered by finitely many closed plaque pieces. Their weighted within-piece variation bounds imply a total weight at least `eta` per path, hence

   \[
   L\eta\le B_n(z)\quad(z\in T),\qquad
   L\eta\,\operatorname{area}(T)\le\int_T B_n\le B.
   \]

   Since `L` is arbitrary, this is impossible. The assembly is `:580–609`; the integral contradiction is the elementary theorem `Analysis/Complex/FiniteInverseBranchBudget.lean:266–279`.

   The finite-cover variation provider, `Topology/FiniteClosedCoverVariation.lean:46–72`, needs only a connected intersection chain and the triangle inequality. Its packing refinement at `:88–133` sums the variation bounds when each piece meets at most one selected path. The file explicitly labels this a replacement proof. It neither states nor proves the false strong collinear-disc clause from Ghys's Fact 1.

Finally `Proposition41SchwarzianVanishing.lean:610–742` transfers the zero scalar field to each local plaque transport and then to arbitrary finite plaque chains using the Schwarzian chain rule.

## Where the continuous Schwarzian field comes from

This is not assumed to vanish: `Analysis/Complex/AffineHolonomyFamilySchwarzian.lean:330–393` proves `one_box_complete_affine_schwarzian_family`. It chooses a whole-leaf affine source coordinate from completeness (`:373–377`), gets actual continuous one-box plaque transports (`:378–379`), and obtains their scalar Schwarzian family and compact bounds from local continuous affine coordinates and holomorphic dependence (`:380–392`). `Geometry/Holonomy/NativeStablePlaqueProducts.lean:727–776` specializes it to each compact native source core and supplies the finite bound used above.

I inspected these statements and proof bodies sufficiently to rule out an immediate hidden transitivity/full-support premise at these nodes. I did not re-audit the complete construction of invariant affine structures in Proposition 3.1 or every holomorphic-derivative-continuity lemma below this scalar-family theorem.

## Relation to the final targets

`Targets/GhysTheoremA.lean:47` onward calls `surface_projective_product` at `:85`; `Paper/Ghys/SurfaceProjectiveProduct.lean:85` onward builds that product from surface projective charts. The latter file imports Proposition 4.1, and its projective-chart providers use the Schwarzian-vanishing chain. The actual code therefore replaces, rather than blindly assumes, Ghys's projectivity result in the surface branch.

A dependency nuance: although the paper's new flat-connection argument permits an affine developing route in dimensions at least three, the **actual formal target's higher-dimensional path still uses the formal Ghys projective-development theorem**. The source route is `OriginalGlobalHolonomyEuclideanCover` → `CompleteGlobalHolonomyAffineCover` → `ProjectiveDeveloping` → `ProjectiveTransverseDevelopment` → `NativeAffineTransverseProjectiveAtlas` / `NativeAffineCarrierTransport` → the projective-holonomy provider invoking Schwarzian vanishing. This source dependency should not be described as absent merely because another mathematical proof route is available.

## Coverage limit and suggested report language

Suggested precise statement: “At the pinned commit, the source supplies a different, measure-budget and path-packing proof of Ghys's required Schwarzian-vanishing result. We found no transitivity or full-support assumption in that inspected chain. This does not verify the disputed inference printed in Ghys's original argument, and we did not run Lean or audit every lower dependency.”

No action was denied or blocked; no public write or contact occurred.
