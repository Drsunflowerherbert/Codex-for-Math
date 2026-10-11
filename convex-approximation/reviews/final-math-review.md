# Independent final mathematical review: ConvexApprox verified core

Independent finalization review. Date: 2026-10-11 UTC.

**Verdict: accepted within the nine-module verified core; no mathematical proof gap or blocking source/type/axiom discrepancy found.** The sources prove the exact quantitative outer estimate, actual finite exponential barriers and their derivatives, pointwise positive Hessians, compact and strictly convex closed sublevels, nonzero level derivatives, arbitrary positive accuracy, and an actual compactly nested sequence recovering K. They accommodate singletons and convex sets with empty ambient interior.

The public source count is **146 explicitly named declarations: 124 theorems/lemmas, 20 definitions, one structure, and one abbreviation**. The supplied audit covers 145 of these, omitting only `ConvexApprox.Examples.Plane`. This is an inventory qualification, not a mathematical gap. The publication session’s separate fresh abbreviation audit has passed, completing fresh coverage of all 146 explicit names. Generated structure fields, constructors, and recursors are outside these explicit source counts.

Analytic boundary charts, analytic embedded hypersurface conclusions, and analytic sphere/Jordan parametrizations remain deferred from the formal core. Acceptance here does not complete the manuscript's analytic approximation lemma as a Lean theorem, validate other results in the source manuscript, or certify the headline Crouzeix claim.

## Review boundary and evidence hierarchy

The reviewed immutable root is:

the supplied `convex-approx-verified-core-2026-10-11.zip`, independently hash-verified

All nine production modules and the umbrella were read in full. Their definitions, visible hypotheses, proofs, and exported conclusions were compared with the supplied theorem inventory and final type/axiom records. All other `.lean` files were inspected: eight archived audit companions and four recovered original draft/umbrella files. Relevant project notes, handoff, original continuation/status, ordinary-proof study and audit, portable theorem records, source excerpt, build/environment/source receipts, and packaging scripts were reviewed as evidence. No supplied script, Lean source, or nested archive program was executed. No repository or recovered source was edited, and no commit or push was performed. This review did not change any production source.

There are three distinct statuses:

1. `project/` contains the completed verified core and successful archived build/type/axiom receipts.
2. `recovered/convex-approx-checkpoint-2026-10-11/` retains the earlier interrupted checkpoint. Its quantitative and barrier drafts had no successful saved compiler receipts; its umbrella imported only Mathlib. Its `CONTINUATION.md` and `RECOVERY-STATUS.json` are truthful historical records, not current blockers for the later verified project.
3. `recovered/.../reviewed-study/` and the nested supplement contain an independently reviewed ordinary mathematical proof and finite computations. Their `lean_status: not_run` describes that earlier ordinary study. Their 19 portable records do not become 19 fully formalized theorems merely because the later core builds.

Fresh pinned compilation and axiom auditing are separate publication-session evidence. This review independently checks the frozen source and the consistency and content hashes of its supplied and publication-session receipts; it does not represent an additional compiler invocation by this reviewer.

## Integrity and pins

The root manifest has 131 file entries. Every recorded byte count and SHA256 matches the actual file; the only additional file is the manifest itself, giving 132 files. No recorded file is missing. All ten production source hashes agree with both `project/evidence/source-pin-hashes.json` and the corrected independent audit receipt. The three project pin files also agree with that independent receipt.

The recovered input ZIP is 558341 bytes, SHA256 `c3c64e17ae69ef244c5355dd41a526b5ac810059f1b0e9353e7101591ea07aa3`. Its 29 file entries match the recovered copies byte for byte. Every entry in the 27-entry recovered manifest matches. The two files outside that manifest are its own `MANIFEST-SHA256.json` and the copied `source-evidence/MANIFEST-SHA256.json`; the different counts are consistent.

The nested ordinary-study supplement is 523782 bytes, SHA256 `9e03b1ce33dc5d5fa62ab9478b06998bcb0eb32635fc11bccac065223e892a74`, with 107 files and no Lean files. Its eleven `convex-approximation/` files match the recovered ordinary study exactly. Both ZIPs were inspected in memory without extraction or execution; no absolute/traversing entry path or symbolic link was found. Both copies of the nested supplement have the same bytes.

The pinned toolchain is Lean 4.24.0, compiler commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`; mathlib is `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. All nine dependency revisions in `lake-manifest.json` agree with the supplied clean-checkout receipt. This review checks the pin files and archived environment output; the publication session separately checks actual current dependency checkouts.

The manuscript excerpt is the local file of 35175 bytes with SHA256 `164f56cc3f5ecbfb65ddba0d0438cacf44f325919ef7dfb742d073c948fddabd`. Its supplied revision is `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, scoped to `lem:approx`, lines 457–511. The stored provenance explicitly relies on the supplied revision attribution and local cached-source manifest, rather than a fresh authenticated remote checkout. This review preserves that qualification.

## Declaration and axiom accounting

| Production module | Explicit names | Theorems/lemmas | Definitions | Other |
| --- | ---: | ---: | ---: | --- |
| Approximation | 24 | 23 | 1 | — |
| Barrier | 24 | 21 | 3 | — |
| Construction | 1 | 1 | 0 | — |
| Examples | 24 | 19 | 4 | 1 abbreviation |
| Geometry | 15 | 13 | 2 | — |
| Nesting | 20 | 13 | 6 | 1 structure |
| OuterApprox | 9 | 8 | 1 | — |
| Quantitative | 13 | 11 | 2 | — |
| Sublevels | 16 | 15 | 1 | — |
| Total | 146 | 124 | 20 | 2 |

There are 121 `theorem` declarations and three `lemma` declarations. No explicitly named private helper declaration is present. The umbrella has nine imports and no declaration. Both complete archived audits have exactly 145 distinct named type/axiom pairs, in exactly the inventory order, with no omitted inventoried name or duplicate. For every pair the reported transitive axioms are exactly `[propext, Classical.choice, Quot.sound]`. Neither final audit contains an error, warning, `sorryAx`, or unexpected project axiom. A separate source scan after removing comments finds no `sorry`, `admit`, axiom declaration, `opaque`, `unsafe`, `implemented_by`, or `native_decide` in production modules.

The explicit-parameter/universe type transcripts contain ordinary pretty-printer `⋯` elisions in proof arguments of instantiated library structures and numerals. They are not source proof holes or diagnostic truncation. The independent coverage artifact retains each printed type exactly, including these elisions, and pairs it with its declaration and axiom record. The source statements are retained separately so the mathematical assumptions and conclusions remain directly inspectable.

The first independent audit attempt exited 1 solely because it requested unsupported formatting options `pp.depth` and `pp.width`; its failed attempt is preserved. The corrected audit removes those options and exits 0 without changing the implementation source. The final fresh archived project build rebuilds all nine modules and the umbrella and exits 0. The final source audit and environment receipt also exit 0. Earlier development failures do not replace these final receipts, and are not silently discarded.

The publication session separately produced `../../publication/evidence/CONVEX-APPROX-CHECKS.json`, `fresh-project-build.log`, `fresh-type-axiom-audit.log`, `fresh-source-audit.log`, and `fresh-supplemental-audit.log` as separately recorded evidence. I read those receipts and independently verified all four log byte counts/hashes and all thirteen source/pin hashes against the frozen project. I also compared those thirteen files in the published source copies with the frozen project; all match. The fresh build rebuilds the nine modules and umbrella successfully. The fresh inventoried audit has 145 names in the exact historical inventory order, and the separate Plane audit adds the one omitted abbreviation. Each of the combined 146 axiom records is exactly the same standard three-axiom list; no final diagnostic, `sorryAx`, or project placeholder is present. All four reported exits are zero. The fresh receipt hash is `09530e120daef87849d5be47c17087ee7be57150d4fac191cc9440748bcf33f6`.

The publication session’s fresh build uses clean exact pinned cached dependency OLeans; it rebuilds project sources, rather than rebuilding all dependencies from source. The type audit prints elaborated types and checks transitive axiom closures. It is not a separately programmed expected-type-equality gate; the mathematical comparison with intended statements is the source review reported here. These limits are explicit in the fresh receipt. A preliminary invocation outside the project failed to select a default toolchain; it is preserved as a failure and is not counted as a successful build.

## Geometric and quantitative core

The common geometric ambient assumptions are a normed additive commutative group E with a real inner-product-space structure. Conditional projection/support/error statements do not require finite dimensionality. Finite dimensionality supplies net existence; nontriviality is added for the positive cardinal lower bound and the existential approximation/nested-family construction. The latter therefore covers dimension at least one without introducing a dimension-zero sphere convention.

`IsChordalNet D δ` says every member of the finite set D is a unit vector and every ambient unit vector has a member within norm distance δ. `supportValue K u` is the actual supremum of the inner products over K. Under compactness and nonemptiness, support attainment is proved and a member of K attaining the supremum is supplied. `nearest_point_normal` supplies an actual nearest point w and the supporting-normal inequality under convexity. These results make no interior, positive-diameter, or full-affine-dimension assumption on K.

Finite nets can contain any prescribed finite unit family. Existence uses compactness of the ambient unit sphere and strictly positive resolution; it does not assert finite zero-nets in higher dimensions. Fine-net statements use `δ² < 2`, giving the positive direction constant. Positive covering, separation of points, orthogonality implying zero, cardinality at least two in a nontrivial space, and full linear span in finite dimensions are separately exported.

Set

`c = 1 - δ²/2`, `s = δ * sqrt(1 - δ²/4)`, and `L = Metric.diam K`.

The exact quantitative error is

`E(K,δ,ε) = (ε + s * L) / c`.

`0 ≤ δ < sqrt 2` implies `δ² < 2` and `c > 0`. The unit-vector identity gives `inner u ν ≥ c`. The tangential estimate uses `inner u ν > 0` before multiplying the nearest-point normal inequality; hence dropping that normal contribution has the correct sign. The norm of the tangential component is bounded by s, and the diameter bound is applied to two actual points of the compact set K. The zero-residual case is treated separately. There is no division by a vanishing displacement or nonpositive denominator.

The exact point-distance and generic Hausdorff theorems require compact nonempty convex K, a chordal net, the fine-net interval, nonnegative ε, and the directional support inequalities. The generic Hausdorff result also explicitly requires `K ⊆ C`; an empty-set or infinite-distance convention is not substituted for that inclusion. The weaker numerator `ε + δ*L` is a separately proved bound. For a singleton the diameter term vanishes and the point-radius bound is `ε/c`.

## Exponential barrier, sublevels, and regular levels

The generic barrier is the actual finite sum

`Φ(x) = ∑ i, exp(Lᵢ(x) - bᵢ)`,

where each Lᵢ is a continuous real linear map. It needs no finite-dimensional or nonempty-index hypothesis. Empty finite sums are correctly allowed in that generic API. The actual Fréchet derivatives are identified with

`DΦ(x)[y] = ∑ i, exp(Lᵢ(x)-bᵢ) * Lᵢ(y)`,

`D²Φ(x)[y,z] = ∑ i, exp(Lᵢ(x)-bᵢ) * Lᵢ(y) * Lᵢ(z)`.

The second formula is connected to the iterated `fderiv`, not merely a separately defined bilinear expression. All-order `ContDiff` is exported for `n : WithTop ℕ∞`; the integrated certificate uses the C∞ specialization. Symmetry, nonnegative Hessian, convexity, and a supporting tangent inequality are proved. Detecting every nonzero vector by some Lᵢ yields pointwise positive Hessian and strict convexity. It does not yield coercivity or a globally uniform strong-convexity modulus.

For an arbitrary real level a, a strict anchor `Φ(p) < a` implies `DΦ(x)[x-p] > 0` whenever `Φ(x)=a`, and therefore the actual derivative is nonzero at that level. The same explicit anchor yields `closure {Φ<a} = {Φ≤a}` and `frontier {Φ<a} = {Φ=a}`. Separation of slopes is not needed for these anchor implications; the proof uses differentiability, convexity, and continuity. In the support-barrier application, a point of K and the strict cardinal margin provide the anchor. Nonempty K alone is not silently treated as a strict anchor.

The directional barrier specializes to the sum of `exp(t*(inner uᵢ x - hᵢ - ε))`. Positive summands and `t>0` give each directional halfspace inequality from `Φ≤1`. Unit directions give the tube estimate. Generic nonempty-index requirements for strict sum estimates and logarithmic cardinal identities are visible.

Coercivity uses positive directional covering, a positive cover constant, and `t>0`; it is not inferred from separation alone. A single positive summand gives an exponential lower bound in `c*norm(x-p) - R - ε`. The resulting theorem is an actual cobounded-to-atTop limit. Every real closed sublevel is compact in the proper-space API, with an explicit radius using `log(max A 1)` to handle arbitrary real sublevel values. Finite-dimensional support barriers instantiate this API. Negative or empty sublevels do not invalidate that compactness statement.

For a nonempty direction index and positive t, the strict cardinal condition

`N * exp(-t*ε) < 1`

is equivalent to `log N < t*ε`. It gives the positive inner margin

`η = ε - log N/t > 0`.

Every point with `infDist(x,K) < η` lies in the open sublevel. The actual tube theorem allows its numerical expression without separately assuming positivity; the applications supply the positive margin. No inclusion is inferred from a non-strict cardinal inequality.

## Integrated approximation and strict convexity as a set

`supportBarrier` uses the finite subtype `{u // u ∈ D}`, so each direction contributes exactly once. It is proved equal both to the directional sum and to the continuous-linear-map generic barrier.

`supportBarrier_outer_approximation` requires:

- A finite-dimensional nontrivial real inner-product ambient space.
- Compactness, nonemptiness, and convexity of K.
- A finite chordal net D at `0 ≤ δ < sqrt 2`.
- Positive support slack ε, positive scale t, and the strict cardinal margin.

It concludes C∞ regularity of the barrier, strict convexity of the function, openness of Ω, `K ⊆ Ω`, compactness of C, `closure Ω = C`, `frontier Ω = {Φ=1}`, nonzero actual derivative on level one, and the exact Hausdorff bound. C is consequently nonempty, bounded, and an actual compact outer approximation.

Separate named results prove convexity of Ω, every open chord between distinct points of C lies in Ω, and strict convexity of C as a set. The Hessian-positive theorem is also separately named. These facts are present in the module; they are not all conjuncts of the one bundled certificate. The set strict-convexity proof places the chord in the open sublevel and then in the interior of C, as required by the set notion.

## Positive accuracy and actual nesting

`exists_outer_parameters_containing` selects parameters below any target `ρ>0`, while retaining any prescribed finite unit family. One explicit selection is `δ = min(1/2, ρ/[8*(1+diam K)])`, `ε=ρ/8`, followed by sufficiently large positive t. Nonnegativity of `Metric.diam K` supplies the numerical inequalities; the theorem needs no compactness or convexity because its conclusion concerns valid net/parameter data and the numerical error only. It is not an approximation assertion for an arbitrary nonconvex or unbounded K.

`BarrierData K` stores all net, positivity, fine-resolution, scale, and strict-cardinal hypotheses. `chosenBarrierData` chooses actual data with error below a positive target. The actual recursive definition is

- P₀ has error < 1.
- Pₙ₊₁ has error below `min(Pₙ.tubeMargin/2, 1/(n+2))`.

Each preceding tube margin is proved positive, so the recursive target is positive. The next outer error is strictly below the preceding margin. `supportBarrier_certified_nesting` combines the next distance bound with the preceding tube inclusion to prove `Cₙ₊₁ ⊆ Ωₙ`. Nesting is therefore certified by the actual geometry, not inferred from parameter decay.

For compact nonempty convex K, each Cₙ is compact and is the closure of Ωₙ; each Ωₙ contains K. Errors satisfy `Eₙ < 1/(n+1)` and tend to zero. Both intersections of the actual open and closed families equal K. The reverse inclusion uses positive distance from a point outside the closed K, contradicted by the vanishing error bound. Actual Hausdorff distances also tend to zero by squeezing between zero and the error. Applying the integrated certificate to each Pₙ gives all its smoothness, strict convexity, and regular-level conclusions for that member.

`exists_smooth_outer_approximation` combines selected data with the geometric assumptions to produce an actual compact outer approximation with Hausdorff error < ρ. The delivered recursive family has its concrete reciprocal accuracy schedule. A theorem for an arbitrary prescribed accuracy sequence, the ordinary study's different closed numerical nesting schedule, and a quantitative distance from Cₙ₊₁ to Ωₙ's complement are not exported. Direction sets need not themselves be nested; the relevant sublevel-set inclusion is proved.

## Degenerate examples

The examples use the public abbreviation `Plane = EuclideanSpace ℝ (Fin 2)`. Horizontal and vertical vectors are unit vectors; nets may contain both signs of both axes. The segment from zero to the horizontal unit vector is proved nonempty, compact, convex, the image of `[0,1]`, and of diameter one. Every point has zero vertical coordinate. A nonzero vertical perturbation inside any sufficiently small ambient ball proves its ambient interior is empty.

The segment's actual support barrier has compact closed sublevels, strict enclosure under the cardinal margin, and the exact Hausdorff estimate. The planar singleton's actual support barrier has radius at most `ε/c`, with no residual diameter term. Thus lower-dimensional applicability is instantiated with actual defined objects; it does not rest only on an assertion that interior was unused.

These examples do not formalize the ordinary study's exact arcosh radius formulas, singleton sharpness limit, ball-specific quadratic error, or shifted polygonal angular obstruction. The singleton bound does not claim the sublevel is a centered ball or centrally symmetric.

## Original source and ordinary-study coverage

The local manuscript's finite exponential construction, support inequalities, positive Hessian, strict-anchor regularity reasoning, and nearest-point distance argument are mathematically consistent in the scoped approximation lemma. Its coarser planar bound is valid; the delivered core supplies the stronger chordal bound. The source-style choice `δⱼ=1/(j+1)` should be indexed from j≥1 when requiring δ<1, as the recovered study explicitly does. The formal nested family uses its own positive-data recursion and has no such endpoint ambiguity.

The ordinary analytic implicit-function/radial argument explains how to obtain analytic charts and a sphere parametrization, and in dimension two a regular analytic Jordan curve. That ordinary argument is preserved as proof guidance, not claimed as a completed formal manifold theorem. Dimension one gives two endpoints rather than a Jordan curve.

| Ordinary portable record | Status against the delivered formal core |
| --- | --- |
| ACOA-001 positive cover/net | Cover, span, cardinal lower bound, and net existence exported; packing-size upper bound not exported. |
| ACOA-002 inner tube | Positive η and infDist tube exported; Minkowski notation and explicit set-to-complement distance bound not exported. |
| ACOA-003 coercivity | Full coercivity and all compact sublevels exported; support API uses diameter rather than a named minimal radius Rₚ. |
| ACOA-004 Hessian/strict convexity | Actual derivative/Hessian positivity and open chords exported; no analytic boundary consequence bundled. |
| ACOA-005 closure/boundary | Exact closure/frontier and open convex enclosure exported. |
| ACOA-006 analytic sphere/Jordan/curvature | Nonzero level derivative exported; charts, parametrization, and curvature deferred. |
| ACOA-007 denominator improvement | Exact-bound theorem plus weaker-numerator corollary exported; no named supremum equality theorem. |
| ACOA-008 tangential improvement | Exact numerator and Hausdorff bound exported. |
| ACOA-009 full planar analytic source lemma | Quantitative smooth approximation core exported; full analytic/Jordan conclusion deferred. |
| ACOA-010 arbitrary scheduled analytic nesting | Actual smooth recursive family, nesting, intersections, and convergence exported; arbitrary prescribed schedule and analytic conclusion not exported. |
| ACOA-011 alternative explicit schedule | Not that particular schedule or its metric margin; a different actual certified recursion is exported. |
| ACOA-012 interval formula | Not exported. |
| ACOA-013 coordinate singleton exact radius | Not exported; singleton upper bound is exported. |
| ACOA-014 quadratic ball error | Not exported. |
| ACOA-015 angular lower obstruction | Not exported. |
| ACOA-016 convergence of maxima | Not exported. |
| ACOA-017 exact iff criteria | Sufficient separation/positive-cover implications exported; full converses/iff criteria not exported. |
| ACOA-018 singleton sharpness limit | Not exported. |
| ACOA-019 full analytic finite-dimensional approximation | Smooth compact strictly convex approximation and actual nesting exported; manifold/sphere conclusion deferred. |

Finite numerical checks and rational fixtures in the recovered study remain illustrations and consistency checks, not universal analytic proofs. No new status is assigned to unrelated supplement studies or to any whole-paper theorem.

## Final disposition and artifacts

No source proof hole, hidden mathematical assumption, unexpected axiom, or mismatch invalidating the compiled core was found. The only declaration-accounting correction is to distinguish the historical 145 inventoried declarations from 146 explicit source names including `Examples.Plane`; it does not require a proof-source change.

`final-source-coverage.json` records all 132 frozen-file hashes, the nine-module declaration breakdown, every explicit source statement, all 145 archived independent printed types and axiom records, all other Lean companions, ZIP entry hashes, and source/pin comparisons. `final-math-review.json` carries the machine-readable verdict and scope boundaries. `REVIEW-HASHES.json` binds these review artifacts to their reviewed source/pin identities.

The mathematical source review is finished, and the publication-session fresh build, 145-name audit, source/pin check, and separate abbreviation audit have passed and were read independently. No review blocker remains within the accepted core. Deferred analytic manifold work remains clearly outside that formal scope and is not treated as completed by this review.

Publication note: internal reviewer/task identity and private storage paths were omitted; artifact locators were updated. Mathematical verdict, source hashes, assumptions, independence and historical/fresh evidence distinctions are preserved. Original review hashes and current report hashes are separately recorded.

The fresh log basenames above are published in `../../publication/evidence/convex-approximation/`; the fresh receipt is `../../publication/evidence/CONVEX-APPROX-CHECKS.json`.
