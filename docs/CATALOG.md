# Project catalog

[Repository home](../README.md) · [Branch roles and snapshots](BRANCHES.md)

Recommended research editions, audited on 20 October 2026. Research links below
are pinned to full commits so the deliverables and their evidence remain
retrievable after navigation edits. The branch map links to moving branch tips.
Each substantive project is listed once; inherited directories on other branches
do not represent extra results.

**Evidence vocabulary.** “Formal” means the documented, scoped Lean statements
have saved build/audit evidence; this cleanup did not rerun Lean. “Conditional”
retains the stated mathematical premise. “Ordinary” means written proof/review,
not kernel verification. “Exact computation” checks stated finite inputs with a
trusted implementation. “Paused” records an explicit stopping point.
“Reference” catalogs sources without certifying their mathematical claims.

## Analysis and integration

| Project and recommended entry | Reading / evidence | Scope and status |
| --- | --- | --- |
| [Original tangent limit](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/d00a89dd9ce6c8ef782234d28c93e69cb712c947/tangent-limit/README.md) | [Project files](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/d00a89dd9ce6c8ef782234d28c93e69cb712c947/tangent-limit) | **Conditional formal:** cubic limit and absolute summability assume `PiDiophantine`; no proof of that hypothesis. |
| [Sharp tangent threshold](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/tangent-sharp/README.md) | [Proof notes](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/tangent-sharp/docs/sharp-threshold-proof.md) | **Conditional formal** absolute summability iff real exponent > 1; absolute nonsummability for exponents ≤ 1 is unconditional. No claim about conditional convergence of the signed series. |
| [Radial contact](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/radial-contact/README.md) | [Assumptions](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/radial-contact/ASSUMPTIONS.md) | **Scoped formal:** radial sphere contact in real normed spaces, with explicit hypotheses and saved build/type/axiom checks. |
| [Positive-block matrix inequalities](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/positive-blocks/README.md) | [Source review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/positive-blocks/reviews/final-source-review.md) | **Scoped formal:** matrix inequalities and equality cases; not the complete Crouzeix theorem. |
| [Convex approximation](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/convex-approximation/README.md) | [Sources and evidence](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/convex-approximation) | **Scoped formal:** smooth quantitative core and certified nested sequence; analytic charts and sphere/Jordan parametrizations remain deferred. |
| [Mixed-moment cancellation](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/mixed-moment/README.md) | [Sources and evidence](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/mixed-moment) | **Conditional formal scope:** actual-integral cancellation for rational polynomials under explicit analytic contact. Broader analytic clauses and exceptional tail endpoint remain deferred. |
| [Transport exponent obstruction](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/README.md) | [Ordinary derivation](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/docs/derivation.md) · [Target-cost bridge](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/docs/followup-measure-bridge.md) | **Scoped formal + ordinary proof:** finite/scalar obstructions and actual 2D Borel target-coupling cost. Cube-source maps and actual L2 map-norm identification remain deferred. |
| [Lebesgue and Hausdorff examples](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/dafa2d2c35b425ca510def9aae3bb17839e67aa5/integral-examples/README.md) | [Problems](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/dafa2d2c35b425ca510def9aae3bb17839e67aa5/integral-examples/PROBLEMS.md) · [Review ledger](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/dafa2d2c35b425ca510def9aae3bb17839e67aa5/integral-examples/VERIFICATION.md) | **Reviewed ordinary / learning:** 16 worked examples, conventions, counterexamples, full collection and guide PDFs. No Lean claim. |

## Optimisation

| Project and recommended entry | Reading / evidence | Scope and status |
| --- | --- | --- |
| [Rational LP certificate toolkit](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-certificates/README.md) | [Mathematics](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-certificates/notes/mathematics.md) · [Bridge limits](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-certificates/notes/checked-bridge.md) | **Scoped formal + exact checker:** original-real certificate soundness and per-input rechecking. Finder incomplete; parser/cache boundaries explicit. Prefer this integrated edition with later executable binding over the earlier sibling checkpoint. |
| [Sparse LP support study](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-sparse-discovery/README.md) | [Proofs](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-sparse-discovery/study.md) · [Finite experiments](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-sparse-discovery/benchmark/README.md) | **Reviewed ordinary + exact finite computation:** support bounds after equality elimination. No Lean verification or general solver implementation; fixture counts are not general performance results. |
| [Linear Programming by Sparse Certificates](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/16075fc88d1cec51dc3c8f137bca3fe70c6f9520/lp-paper/README.md) | [Paper PDF](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/16075fc88d1cec51dc3c8f137bca3fe70c6f9520/lp-paper/sparse-lp-certificates.pdf) · [Review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/16075fc88d1cec51dc3c8f137bca3fe70c6f9520/lp-paper/REVIEW.md) | **Reviewed exposition:** separate paper deliverable synthesizing the two preceding projects, not a new solver or theorem package. |
| [Rank-one critical-point classifier](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/40ebeb0f4583659a195d77ced27a91d4084ae75f/critical-points/README.md) | [Study](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/40ebeb0f4583659a195d77ced27a91d4084ae75f/critical-points/STUDY.md) · [Examples](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/40ebeb0f4583659a195d77ced27a91d4084ae75f/critical-points/EXAMPLES.md) | **Reviewed ordinary + exact computation:** local bivariate rational-polynomial stationary points at the origin with Hessian rank one. No Lean or global-extremum claim; coefficient budgets may return unresolved. |

## Discrete mathematics

| Project and recommended entry | Reading / evidence | Scope and status |
| --- | --- | --- |
| [Exact-length Egyptian fractions](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/egyptian-exact/README.md) | [Sources and evidence](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/egyptian-exact) | **Scoped formal:** exact-length cleanup, finite-state termination and marker-preserving padding. Separate ordinary optional bounds do not inherit formal status. |
| [Finite-field product mixing](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/finite-field-product-mixing/README.md) | [Formal scope](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/finite-field-product-mixing/evidence/formal-scope.json) | **Scoped formal, supplied evidence:** four-product covering and local divisor lift. Publication inspected completed evidence; it did not rerun Lean. No global Egyptian-fraction constant or distinctness claim. |
| [Hadamard / Williamson, latest round](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2834fea31fb4ca7203531ca220e55a2fb7640119/hadamard-study/round3/README.md) | [Round 1](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2834fea31fb4ca7203531ca220e55a2fb7640119/hadamard-study/README.md) · [Round 2](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2834fea31fb4ca7203531ca220e55a2fb7640119/hadamard-study/round2/README.md) · [Stopping point](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2834fea31fb4ca7203531ca220e55a2fb7640119/hadamard-study/round3/LESSONS.md) | **Paused ordinary / exact experiments:** three rounds of finite constructions and bounded search. No Lean proof, new general construction theorem or proof of the Hadamard conjecture. |

## Dynamical systems and paper reviews

| Project and recommended entry | Reading / evidence | Scope and status |
| --- | --- | --- |
| [Holomorphic Anosov review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2d6f543fcfe182c3df7d5316c0fba0279eebfe4f/holomorphic-anosov-review/README.md) | [Expanded report](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2d6f543fcfe182c3df7d5316c0fba0279eebfe4f/holomorphic-anosov-review/updated-review.md) · [Compiled checks and limits](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2d6f543fcfe182c3df7d5316c0fba0279eebfe4f/holomorphic-anosov-review/evidence/compiled-verification/deliverables/verification-method.md) | **Paper review with recorded formal audit:** build, types/axioms and same-kernel replay passed; official comparator has no verdict. A, 1.1 and 1.3 retain the homotopy-torus rigidity premise. Initial limited review is superseded. |

## Formal verification and tooling

| Project and recommended entry | Reading / evidence | Scope and status |
| --- | --- | --- |
| [Math evidence toolkit](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/math-evidence/README.md) | [Evidence and trust limits](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/math-evidence/VERIFICATION.md) | **Tooling:** structured source/assumption/dependency records, safe intake and separate fixed live gate. Imported records and saved receipts grant no fresh Lean pass. |
| [Evidence hardening companion](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/evidence-hardening/README.md) | [Migration](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/evidence-hardening/MIGRATION.md) · [Verification](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/evidence-hardening/VERIFICATION.md) | **Tooling:** stricter saved-receipt integrity, unreplaced Git-tree byte checks and fixed fixtures. Same-kernel replay is not an independent kernel implementation. |
| [Exact root certificate toolkit](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/5da47dc49651af44faf96ecc8604c180600bdc72/certified-roots/README.md) | [Study](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/5da47dc49651af44faf96ecc8604c180600bdc72/certified-roots/STUDY.md) · [Trust limits](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/5da47dc49651af44faf96ecc8604c180600bdc72/certified-roots/VERIFICATION.md) | **Reviewed ordinary + exact rational checker:** contraction certifies a unique root in the stated closed box and an error bound. No Lean; failed sufficient criterion does not prove no root exists. |

## Research maps and learning materials

| Project and recommended entry | Reading / evidence | Scope and status |
| --- | --- | --- |
| [Research corpus and reviewed studies](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/README.md) | [Reviewed supplement](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/README.md) | **Reference + ordinary:** revision-pinned corpus snapshot, seven reviewed studies and 81 core records. Starter affine/Egyptian copies are historical; use corrected links in the research README. Metadata and finite checks do not certify upstream manuscripts. |
| [Verified techniques guide](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/learning-guide/verified-techniques.md) | [Finalization update](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/learning-guide/STATUS-FINALIZATION-2026-10-11.md) | **Learning reference:** reusable proof methods drawn from scoped libraries; consult each exact theorem's assumptions and the dated updates. |
| [Competition practice library](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/ef8032ed20f05fb100e95fc287eefb5d3e431543/contest-library/README.md) | [Spoiler-free problems](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/ef8032ed20f05fb100e95fc287eefb5d3e431543/contest-library/PROBLEMS.md) · [Coverage](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/ef8032ed20f05fb100e95fc287eefb5d3e431543/contest-library/COVERAGE.md) | **Bounded learning collection:** 236 indexed entries, 12 provisional; three reviewed ordinary analysis solutions, no Lean claim. |
| [OpenAI mathematics research map](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/34e3e11e4c37109bfc06f4f195a62a2cf992c5b0/research-map/README.md) | [Field map](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/34e3e11e4c37109bfc06f4f195a62a2cf992c5b0/research-map/FIELD-MAP.md) · [Claim scope](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/34e3e11e4c37109bfc06f4f195a62a2cf992c5b0/research-map/MAJOR-CLAIMS.md) | **Reference / partial audit:** 719 active manuscript rows remain metadata-only; upstream proofs were not independently validated. The local browser catalog is downloadable HTML, not a hosted GitHub page. |

## Reading evidence correctly

The integrated projects above use research commit `e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f` unless another
commit is linked. Each project README identifies actual theorem statements,
mathematical hypotheses, toolchain pins and its own reproduction instructions.
No blanket “verified repository” status is assigned. In particular, compilation
does not discharge an explicit hypothesis, exact finite tests do not prove a
universal theorem, and a saved receipt is not a fresh run.

The [publication record](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/publication/README.md) and
[13 October report](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/publication/ROUND-2026-10-13.md) describe the
integrated edition. Whole-tree integrity checks apply to the source/baseline snapshots they
inventory, not every descendant carrying an inherited copy. Navigation changes
intentionally leave those historical manifests
untouched. See [branch roles and snapshots](BRANCHES.md) before reproducing a
historical receipt. Attribution and licenses remain project-specific.
