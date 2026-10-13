# Scoped reusable results — 13 October 2026

This catalog covers 21 local library/study groups: 11 with saved formal build/audit evidence and 10 ordinary study groups. The seven reviewed supplement studies contain 81 core theorem/identity records. These are different counting units. No corpus headline solution is certified here; no Lean build was executed for this map.

All local source links are pinned to integrated baseline e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f. Motivating upstream links refer to the historical fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb snapshot. Latest upstream review belongs to the main research map. The [machine-readable companion](scoped-results.json) includes source hashes, separate status axes, exact scope gaps and evidence links.

An independent read-only catalog review spot-checked eight high-impact groups: cubic tangent, mixed moments, convex approximation, positive blocks, finite-field mixing, both transport layers and LP certificates. It reported no blocking discrepancy; two precision improvements were applied. Thirteen groups did not receive a new independent catalog spot review. All 21 retain links to their earlier scoped review evidence. This review is a source/scope comparison, not a new mathematical proof audit or Lean run.

“Full” below describes the explicitly stated supporting result. It never upgrades the original manuscript headline. Reading a successful saved compiler receipt establishes no fresh check; a successful kernel check does not by itself establish correspondence to an informal famous problem. Independent local review is separate from external peer review and established mathematical acceptance.

| Result group | Field → subfield | Kind | Evidence | Learning priority |
| --- | --- | --- | --- | --- |
| [Conditional cubic tangent decay and absolute summability](#scope-tangent-cubic) | Number theory → Diophantine approximation and series | conditional | Saved formal receipt + local review | medium |
| [Sharp absolute tangent-series threshold](#scope-tangent-sharp) | Number theory → Diophantine approximation and series | conditional | Saved formal receipt + local review | medium |
| [Radial contact and sphere homeomorphism](#scope-radial-lean) | Functional analysis → Normed-space geometry | full | Saved formal receipt + local review | high |
| [Exact-length duplicate removal and marker padding](#scope-egyptian-lean) | Number theory → Egyptian fractions | full | Saved formal receipt + local review | high |
| [Positive-block inequalities, exact gaps and full equality classification](#scope-positive-blocks-lean) | Linear algebra and operator theory → Positive semidefinite block matrices | full | Saved formal receipt + local review | high |
| [Smooth quantitative convex outer approximation and actual nesting](#scope-convex-lean) | Geometry and analysis → Finite-dimensional convex approximation | full | Saved formal receipt + local review | medium |
| [Actual-integral Taylor-contact cancellation](#scope-mixed-moment-lean) | Number theory and analysis → Mixed moments and special constants | full | Saved formal receipt + local review | advanced |
| [Finite-field Fourier mixing, four products and local divisor lift](#scope-finite-field-lean) | Number theory → Additive combinatorics over finite fields | full | Saved formal receipt + local review | medium |
| [Original-real rational LP certificate soundness and checked exports](#scope-lp-certificates) | Optimization → Linear programming certificates | technique | Saved formal receipt + local review | high |
| [Finite/scalar transport exponent obstructions](#scope-transport-finite) | Analysis → Optimal transport stability | counterexample | Saved formal receipt + local review | medium |
| [All-Borel-coupling atomic target-cost bridge](#scope-transport-measures) | Analysis → Optimal transport stability | full | Saved formal receipt + local review | advanced |
| [Sparse exact LP certificate discovery study](#scope-lp-sparse) | Optimization → Linear programming certificate discovery | technique | Ordinary local review; no Lean | high |
| [Periodic-to-global affine avoidance reduction](#scope-ordinary-affine) | Real analysis → Measure and affine avoidance | conditional | Ordinary local review; no Lean | medium |
| [Corrected ordinary Egyptian fraction core](#scope-ordinary-egyptian) | Number theory → Egyptian fractions | full | Ordinary local review; no Lean | high |
| [Ordinary uniform-cube optimal-map obstruction](#scope-ordinary-transport) | Analysis → Optimal transport stability | counterexample | Ordinary local review; no Lean | medium |
| [Ordinary positive-block Gram study](#scope-ordinary-blocks) | Linear algebra and operator theory → Positive semidefinite block matrices | full | Ordinary local review; no Lean | high |
| [Ordinary mixed-moment foundations and cancellation](#scope-ordinary-moments) | Number theory and analysis → Mixed moments and special constants | full | Ordinary local review; no Lean | advanced |
| [Ordinary analytic convex approximation study](#scope-ordinary-convex) | Geometry and analysis → Finite-dimensional convex approximation | full | Ordinary local review; no Lean | advanced |
| [Ordinary finite-field mixing and local lifts](#scope-ordinary-finite-field) | Number theory → Additive combinatorics over finite fields | full | Ordinary local review; no Lean | medium |
| [Ordinary radial contact geometry](#scope-ordinary-radial) | Functional analysis → Normed-space geometry | full | Ordinary local review; no Lean | high |
| [Ordinary Diophantine-to-tangent bridge](#scope-ordinary-pi-bridge) | Number theory → Diophantine approximation and series | conditional | Ordinary local review; no Lean | medium |

## Statement and evidence ledger

<a id="scope-tangent-cubic"></a>
### Conditional cubic tangent decay and absolute summability

**Hierarchy:** Number theory → Diophantine approximation and series → The irrationality exponent of π is 2. → Conditional cubic tangent decay and absolute summability at baseline e4f337c.

Under PiDiophantine, tan(n)/n^3 tends to zero along positive integers and sum(n>=1) abs(tan n)/n^3 is summable. Integer angles are in radians; nonpoles use mathlib pi irrationality.

**Hypotheses:** For every real nu>2, for all sufficiently large positive integers q and every integer p, abs(pi-p/q)>=q^(-nu). This PiDiophantine hypothesis is assumed, not proved here.

**Evidence:** [saved Lean build](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/tangent-limit/logs/final-build.log); [saved statement and axiom audit](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/tangent-limit/logs/final-theorem-inventory.log); [independent local review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/tangent-limit/docs/independent-review.md). All are saved records, not reruns by this map.

**Excluded headline:** The irrationality exponent of pi is 2. Unconditional Flint-Hills convergence.

**Gaps:** No proof of PiDiophantine; no upstream proof imported or validated.

**Study prerequisites:** Real limits and summability, Trigonometry, Rational approximation. **Priority:** medium.

**Statement sources:** [tangent-limit/README.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/tangent-limit/README.md), [tangent-limit/TangentLimit/Hypothesis.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/tangent-limit/TangentLimit/Hypothesis.lean), [tangent-limit/docs/theorem-statements.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/tangent-limit/docs/theorem-statements.md).

<a id="scope-tangent-sharp"></a>
### Sharp absolute tangent-series threshold

**Hierarchy:** Number theory → Diophantine approximation and series → The irrationality exponent of π is 2. → Sharp absolute tangent-series threshold at baseline e4f337c.

For every real s, under PiDiophantine, sum(n>=1) abs(tan n)/n^s is summable iff s>1. The separate nonsummability theorem for s<=1 is unconditional and uses standard pi irrationality.

**Hypotheses:** For every real nu>2, for all sufficiently large positive integers q and every integer p, abs(pi-p/q)>=q^(-nu). This PiDiophantine hypothesis is assumed, not proved here. s is real; necessity s<=1 uses no PiDiophantine premise.

**Evidence:** [independent local review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/tangent-sharp/docs/sharp-independent-review.md); [saved statement and axiom audit](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/tangent-sharp/logs/final-theorem-inventory.log). All are saved records, not reruns by this map.

**Excluded headline:** Proof of the pi-exponent headline. Conditional convergence of the signed tangent series.

**Gaps:** Sufficiency retains unproved PiDiophantine.

**Study prerequisites:** Cubic tangent bridge, Finite harmonic packing, Dyadic summability. **Priority:** medium.

**Statement sources:** [tangent-sharp/README.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/tangent-sharp/README.md), [tangent-sharp/TangentLimit/SharpSummability.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/tangent-sharp/TangentLimit/SharpSummability.lean), [tangent-sharp/TangentLimit/Divergence.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/tangent-sharp/TangentLimit/Divergence.lean).

<a id="scope-radial-lean"></a>
### Radial contact and sphere homeomorphism

**Hierarchy:** Functional analysis → Normed-space geometry → Tingley’s sphere-isometry problem. → Radial contact and sphere homeomorphism at baseline e4f337c.

For an interior center c and unit direction v, there is a unique positive radius r with norm(c+r*v)=1, and 1-norm(c)<=r<=1+norm(c). Radius and contact have Lipschitz constants (1+norm(c))^2/(1-norm(c)) and 2*(1+norm(c))/(1-norm(c)); normalized direction is the inverse sphere homeomorphism.

**Hypotheses:** E is a real normed space (NormedAddCommGroup and NormedSpace real). norm(c)<1; norm(v)=1. No completeness, dimension, smoothness or strict-convexity premise; empty sphere is allowed.

**Evidence:** [saved Lean build and audit](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/radial-contact/evidence/validation.json); [independent local review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/radial-contact/evidence/formal-review.md). All are saved records, not reruns by this map.

**Excluded headline:** Tingley's sphere-isometry extension theorem.

**Gaps:** Ordinary sharpness examples are not Lean theorems. Original formalizers lacked starter bytes and independently reconstructed the specification; later retrieval does not certify historical source access or entire-study equivalence.

**Study prerequisites:** Normed spaces, Intermediate value theorem, Convex combinations, Lipschitz maps. **Priority:** high.

**Statement sources:** [radial-contact/README.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/radial-contact/README.md), [radial-contact/ASSUMPTIONS.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/radial-contact/ASSUMPTIONS.md), [radial-contact/RadialContact/Basic.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/radial-contact/RadialContact/Basic.lean), [radial-contact/RadialContact/Inverse.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/radial-contact/RadialContact/Inverse.lean).

<a id="scope-egyptian-lean"></a>
### Exact-length duplicate removal and marker padding

**Hierarchy:** Number theory → Egyptian fractions → Short Egyptian fractions. → Exact-length duplicate removal and marker padding at baseline e4f337c.

A list of positive natural denominators with reciprocal sum strictly between 0 and 1 has a distinct positive-denominator list with the same length and sum. Positive sorted fixed-length representations of every real value form a finite set. A distinct expansion of 1 of length at least 3 can gain one term while preserving one chosen denominator; input bound B yields output bound B*(B+1).

**Hypotheses:** Cleanup: positive natural denominators and 0<reciprocalSum<1. Padding: positive distinct list, sum=1, length>=3, chosen marker belongs to input; bounded padding assumes every input denominator<=B.

**Evidence:** [independent local statement review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/egyptian-exact/review/AllStatementsAudit.md); [independent local marker review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/egyptian-exact/review/MarkerPaddingAudit.md); [saved publication Lean checks](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/publication/evidence/CURRENT-CHECKS.json). All are saved records, not reruns by this map.

**Excluded headline:** Global O(log log b) short-expansion theorem and optimal asymptotic constants.

**Gaps:** Companion Python algorithm has no formal extraction/refinement theorem. Cleanup does not preserve a marker or prove a sharp denominator bound. Starter access history is distinct from later validated archival retrieval.

**Study prerequisites:** Positive rational reciprocals, Finite-state termination, Well-founded relations. **Priority:** high.

**Statement sources:** [egyptian-exact/README.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/egyptian-exact/README.md), [egyptian-exact/Egyptian/Cleanup.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/egyptian-exact/Egyptian/Cleanup.lean), [egyptian-exact/Egyptian/Padding.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/egyptian-exact/Egyptian/Padding.lean).

<a id="scope-positive-blocks-lean"></a>
### Positive-block inequalities, exact gaps and full equality classification

**Hierarchy:** Linear algebra and operator theory → Positive semidefinite block matrices → The complete Crouzeix conjecture. → Positive-block inequalities, exact gaps and full equality classification at baseline e4f337c.

For a finite complex PSD block matrix [A B; B* C], the unnormalized Hilbert-Schmidt norms satisfy normHS(B)^2<=normHS(A)*normHS(C). For common-row Gram factors with A=X^H*X, B=X^H*Y, C=Y^H*Y, the sum deficit normHS(A)^2+normHS(C)^2-2*normHS(B)^2 equals normHS(X*X^H-Y*Y^H)^2. Product equality occurs iff a diagonal block is zero or a common positive-support normal form exists; existence and converse are proved.

**Hypotheses:** Finite complex matrix index types; rectangular B permitted. Full block matrix is positive semidefinite. Normalized nonzero equality criterion requires positive diagonal norms; zero cases have separate branches.

**Evidence:** [independent local final review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/positive-blocks/reviews/final-source-review.md); [saved publication Lean checks](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/publication/evidence/POSITIVE-BLOCK-CHECKS.json). All are saved records, not reruns by this map.

**Excluded headline:** Complete Crouzeix conjecture or constant-two numerical-range theorem.

**Gaps:** Optional ordinary corollaries outside exported source are not formally covered.

**Study prerequisites:** Complex matrices, Gram factorizations, Hilbert-Schmidt norm, Cauchy-Schwarz. **Priority:** high.

**Statement sources:** [positive-blocks/README.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/positive-blocks/README.md), [positive-blocks/PositiveBlocks/Blocks.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/positive-blocks/PositiveBlocks/Blocks.lean), [positive-blocks/PositiveBlocks/Classification.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/positive-blocks/PositiveBlocks/Classification.lean).

**History:** Historical supplied checkpoint had unfinished written verdict; separate final source review completed it without a core proof correction.

<a id="scope-convex-lean"></a>
### Smooth quantitative convex outer approximation and actual nesting

**Hierarchy:** Geometry and analysis → Finite-dimensional convex approximation → The complete Crouzeix conjecture. → Smooth quantitative convex outer approximation and actual nesting at baseline e4f337c.

For nonempty compact convex K, a finite unit-direction delta-net gives a smooth exponential support barrier with strictly convex compact outer sublevels. Outer distance and Hausdorff error are <=(epsilon+delta*sqrt(1-delta^2/4)*diam(K))/(1-delta^2/2); there is a recursively selected compactly nested sequence with vanishing Hausdorff error and intersection K. Smoothness is of the barrier; analytic boundary charts remain deferred.

**Hypotheses:** Finite-dimensional nontrivial real inner-product space; K nonempty compact convex. 0<=delta<sqrt(2); epsilon>0; t>0; N*exp(-t*epsilon)<1. No ambient interior assumption on K; singleton and lower-dimensional examples are included.

**Evidence:** [independent local review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/convex-approximation/notes/independent-review.md); [saved publication Lean checks](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/publication/evidence/CONVEX-APPROX-CHECKS.json). All are saved records, not reruns by this map.

**Excluded headline:** Complete Crouzeix conjecture. Full analytic boundary charts and sphere/Jordan parametrizations.

**Gaps:** Analytic boundary charts and sphere/Jordan parametrizations deferred. No globally uniform strong-convexity modulus, curvature bound or optimal net size.

**Study prerequisites:** Support functions, Finite nets, Multivariable differentiation, Compact convex sets. **Priority:** medium.

**Statement sources:** [convex-approximation/README.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/convex-approximation/README.md), [convex-approximation/ConvexApprox/Approximation.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/convex-approximation/ConvexApprox/Approximation.lean), [convex-approximation/ConvexApprox/Nesting.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/convex-approximation/ConvexApprox/Nesting.lean).

**History:** Earlier failed printer audit remains failed; corrected historical and fresh checks are separate.

<a id="scope-mixed-moment-lean"></a>
### Actual-integral Taylor-contact cancellation

**Hierarchy:** Number theory and analysis → Mixed moments and special constants → Irrationality of Catalan’s constant. → Actual-integral Taylor-contact cancellation at baseline e4f337c.

For rational polynomials P,D, natural L,j with j<L, one-sided or two-sided contact x*P(x)/sqrt(1-x^2)-D(x)=O(x^L) at zero implies Analysis.polynomialColumn(P,j)-(3/2)*Zeta.polynomialColumn(D,j)=a+b*G with explicit rational witnesses a,b. The first column is the integral of abs(t)*P(t)*s^j/(sqrt(1-t^2)*(1-t*s)) over (-1,1)x(0,1); the second is the integral of D(t)*s^j/(1-t*s) over (0,1)^2. Integrability, moment recurrences and boundary evaluations are proved.

**Hypotheses:** P,D in Q[t]; L,j natural; j<L. Contact at zero in the right-sided or two-sided neighborhood filter. Integrals are the defined actual Lebesgue product-measure columns, not merely formal coordinates.

**Evidence:** [independent local statement review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/mixed-moment/docs/final-statement-review.md); [independent local publication review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/mixed-moment/docs/publication-review.md); [saved publication Lean checks](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/publication/evidence/MIXED-MOMENT-CHECKS.json). All are saved records, not reruns by this map.

**Excluded headline:** Catalan's constant is irrational. Arithmetic independence or nonmembership in Q+QG from a nonzero formal zeta coefficient.

**Gaps:** Evaluation of formal coordinates into reals is not assumed injective. Tail theorem only for 2<=i+N, excluding i=0,N=1. Broader analytic clauses and optional pi/Basel evaluation deferred.

**Study prerequisites:** Measure theory, Dominated or nonnegative exchanges, Rational recurrences, Polynomial Taylor contact. **Priority:** advanced.

**Statement sources:** [mixed-moment/README.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/mixed-moment/README.md), [mixed-moment/docs/final-proof-scope.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/mixed-moment/docs/final-proof-scope.md), [mixed-moment/MixedMoments/Applications.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/mixed-moment/MixedMoments/Applications.lean).

**History:** Failed/interrupted historical printer and supplement attempts stay failed; 111-theorem audit is a subset, not complete coverage. Earlier archive transfer failure is historical; later direct verified intake does not change the ordinary-study Lean status.

<a id="scope-finite-field-lean"></a>
### Finite-field Fourier mixing, four products and local divisor lift

**Hierarchy:** Number theory → Additive combinatorics over finite fields → Short Egyptian fractions. → Finite-field Fourier mixing, four products and local divisor lift at baseline e4f337c.

For prime p and nonempty A,B in F_p, the normalized nonzero Fourier coefficient of independent uniform XY is bounded by sqrt(p/(|A|*|B|)). If |H|^4>=p^3, each residue has four-product probability at least 1/p^2 and is a sum of four products of H elements. A local positive-divisor rational four-summand lift is also compiled.

**Hypotheses:** p prime; independent uniform samples. A,B nonempty; four-product density condition implies H nonempty. Ordered tuples with multiplicities; repetitions and zero elements allowed.

**Evidence:** [supplied saved Lean build and audit](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/finite-field-product-mixing/evidence/final-independent-audit.json); [saved statement inventory](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/finite-field-product-mixing/evidence/final-theorem-inventory.log). All are saved records, not reruns by this map.

**Excluded headline:** Global short-Egyptian-fraction constant or full headline asymptotic theorem. Distinct-sample or optimal product-count theorem.

**Gaps:** Publication inspected unchanged source hashes and names; it did not rerun Lean or finite computations. Heterogeneous set/coefficient/shift theorem, radical-free equivalences and arbitrary-k lift remain ordinary-only.

**Study prerequisites:** Finite fields, Finite Fourier inversion, Character orthogonality, Cauchy-Schwarz. **Priority:** medium.

**Statement sources:** [finite-field-product-mixing/README.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/finite-field-product-mixing/README.md), [finite-field-product-mixing/evidence/formal-scope.json](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/finite-field-product-mixing/evidence/formal-scope.json), [finite-field-product-mixing/FiniteFieldMixing/Mixing.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/finite-field-product-mixing/FiniteFieldMixing/Mixing.lean), [finite-field-product-mixing/FiniteFieldMixing/DivisorLift.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/finite-field-product-mixing/FiniteFieldMixing/DivisorLift.lean).

<a id="scope-lp-certificates"></a>
### Original-real rational LP certificate soundness and checked exports

**Hierarchy:** Optimization → Linear programming certificates → Local reusable optimization technique → Original-real rational LP certificate soundness and checked exports at baseline e4f337c.

Rational Boolean acceptance of optimal, infeasible or unbounded certificates implies the corresponding result for all real feasible points. The typed original-input layer proves mixed-row and objective normalization sound. Per-input checked export regenerates trusted numeric Lean statements and requires fresh kernel acceptance; the deterministic witness finder is incomplete.

**Hypotheses:** Finite rational coefficients and witnesses; variables are unrestricted reals. Nonstrict inequalities; equality multipliers are free signed rationals. Acceptance hypotheses are explicit; input/output resource budgets apply to the external bridge.

**Evidence:** [independent local math review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-certificates/evidence/math-review.md); [independent local followup formal review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-certificates/evidence/followup-formal-review.md); [saved followup checks](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-certificates/evidence/followup-summary.md). All are saved records, not reruns by this map.

**Excluded headline:** Complete LP solver, certificate discovery completeness or strong duality.

**Gaps:** Python/JSON parsing and literal generation have no formal refinement theorem. Cached dependency OLeans and host runtime remain trusted; local replay uses the same kernel. Git-status dependency check can miss index-hidden changes. Coherently rehashed saved intake can admit malformed process metadata; saved intake is not a fresh Lean pass.

**Study prerequisites:** Finite exact linear algebra, Weak duality, Rational arithmetic, Typed certificate interfaces. **Priority:** high.

**Statement sources:** [lp-certificates/README.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-certificates/README.md), [lp-certificates/LPCertificates/Rational.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-certificates/LPCertificates/Rational.lean), [lp-certificates/LPCertificates/Input.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-certificates/LPCertificates/Input.lean).

**History:** Follow-up fixed large-integer formatting crash using budgets and fail-closed formatting; corrected weighted-slack interface note.

<a id="scope-transport-finite"></a>
### Finite/scalar transport exponent obstructions

**Hierarchy:** Analysis → Optimal transport stability → Sharp one-third stability of Brenier maps. → Finite/scalar transport exponent obstructions at baseline e4f337c.

Finite arrays and scalar formulas certify target cost a*b^p and mapSize^2=b/2+a*b^2. Along b=a/2 shrinking a, every proposed constant is exceeded above exponent p/(2*(p+1)); fixed positive central mass gives the separate 1/2 ceiling. Interpretation as actual Brenier-map L2 quantities uses a separately reviewed ordinary measure proof.

**Hypotheses:** Ordinary cube model: d>=2, 0<b<a, a+b<1, uniform cube source. Finite/scalar parameter hypotheses are explicit in each exported theorem; p>=1 for the ordinary probability transport reading. Shrinking central mass is essential to the first ceiling.

**Evidence:** [independent local ordinary review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/reviews/proof-review.md); [independent local Lean review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/reviews/lean-review.md); [saved core status](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/STATUS.json). All are saved records, not reruns by this map.

**Excluded headline:** Positive global upper stability theorem or endpoint optimality.

**Gaps:** Actual uniform-source maps, null ties, source integration and actual L2 norm identification remain deferred Lean obligations.

**Study prerequisites:** Pushforward laws versus maps, Wasserstein coupling definition, Exact finite transport, Real powers. **Priority:** medium.

**Statement sources:** [transport-sharpness/README.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/README.md), [transport-sharpness/TransportSharpness/Finite.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/TransportSharpness/Finite.lean), [transport-sharpness/TransportSharpness/Obstruction.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/TransportSharpness/Obstruction.lean).

<a id="scope-transport-measures"></a>
### All-Borel-coupling atomic target-cost bridge

**Hierarchy:** Analysis → Optimal transport stability → Sharp one-third stability of Brenier maps. → All-Borel-coupling atomic target-cost bridge at baseline e4f337c.

In dimension two, actual target probabilities with masses ((1-a)/2,a,(1-a)/2) at (-1,0),(0,0),(1,0) and (-1,0),(0,b),(1,0) have attained infimal Euclidean p-cost a*b^p over all Borel couplings; its 1/p root is a^(1/p)*b. Cost is an explicit coordinate Euclidean formula.

**Hypotheses:** Probability specialization: 0<=a<=1, b>=0, p>=1. More general equal-mass finite-measure cost identities assume a>=0,b>=0,p>0; a>1 must not be described as probability transport. No atomic-form premise is imposed on the coupling domain.

**Evidence:** [independent local followup math review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/reviews/followup-proof-review.md); [independent local followup Lean review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/reviews/followup-lean-review.md); [saved followup status](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/FOLLOWUP-STATUS.json). All are saved records, not reruns by this map.

**Excluded headline:** Original cube-source optimal-map stability headline. Abstract Wasserstein metric axioms or broad optimal transport library.

**Gaps:** No actual uniform-source map or L2-map identification. Higher-dimensional actual-measure extension and target optimizer uniqueness deferred.

**Study prerequisites:** Borel measures, Weighted Dirac integration, Map marginals, Nonnegative integral infima. **Priority:** advanced.

**Statement sources:** [transport-sharpness/docs/followup-measure-bridge.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/docs/followup-measure-bridge.md), [transport-sharpness/TransportSharpness/Measures.lean](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/transport-sharpness/TransportSharpness/Measures.lean).

<a id="scope-lp-sparse"></a>
### Sparse exact LP certificate discovery study

**Hierarchy:** Optimization → Linear programming certificate discovery → Local reusable optimization technique → Sparse exact LP certificate discovery study at baseline e4f337c.

After exact consistency checking and elimination of E*x=f with im(N)=ker(E), let k=rank(A*N)=rank([A;E])-rank(E). A valid bound over a nonempty feasible set has a nonnegative inequality certificate supported on at most k rows; infeasibility may require k+1. Exhaustive appropriate independent-support enumeration is complete under the stated model; implemented code is a fixture experiment.

**Hypotheses:** Finite nonstrict linear inequalities and equalities; exact rational arithmetic for executable search. Bound-certificate k-row reduction assumes a nonempty feasible set. Equality inconsistency is checked separately; infeasibility uses lifted supports.

**Evidence:** [independent local math review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-sparse-discovery/reviews/mathematical-review.md); [independent local computational review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-sparse-discovery/reviews/computational-review.md). All are saved records, not reruns by this map.

**Excluded headline:** Lean verification, general solver implementation or general performance advantage.

**Gaps:** No general LP input interface or checked Lean bridge. Truncated search exhaustion remains inconclusive; fixture subset counts are not timing comparisons.

**Study prerequisites:** Gaussian elimination, Conic dependence reduction, Farkas certificates, Exact arithmetic. **Priority:** high.

**Statement sources:** [lp-sparse-discovery/README.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-sparse-discovery/README.md), [lp-sparse-discovery/study.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-sparse-discovery/study.md).

<a id="scope-ordinary-affine"></a>
### Periodic-to-global affine avoidance reduction

**Hierarchy:** Real analysis → Measure and affine avoidance → The geometric case of the Erdős similarity conjecture. → Periodic-to-global affine avoidance reduction at baseline e4f337c.

Assuming small open 1-periodic sets hit every translated copy at normalized scale t in [1,2), a summably budgeted union over both signs and dyadic scales has small measure; its compact complement in [0,1] excludes every entire nonzero affine copy of the sequence.

**Hypotheses:** For every p in (0,1), one open periodic H_p works for all y and normalized t, with density<=C*p and a hit y+t*a_n. 0<eta<1; both signs of dilation included.

**Evidence:** [independent local ordinary review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/reviews/affine/independent-review.txt); [saved study status](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json). All are saved records, not reruns by this map.

**Excluded headline:** Original upstream manuscript headline.

**Gaps:** No construction of normalized hitting sets; not a proof of the source geometric-progression headline. No Lean compilation or kernel checking of these ordinary study records; related standalone libraries have separate, narrower contracts.

**Study prerequisites:** Lebesgue measure, Periodic sets, Summable budgets. **Priority:** medium.

**Statement sources:** [research/supplement/reviews/affine/research-notes.reviewed.txt](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/reviews/affine/research-notes.reviewed.txt), [research/supplement/STUDY-INDEX.json](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json).

**History:** Corrected limitation requires infinitely many distinct values, not pairwise distinct sequence terms.

<a id="scope-ordinary-egyptian"></a>
### Corrected ordinary Egyptian fraction core

**Hierarchy:** Number theory → Egyptian fractions → Short Egyptian fractions. → Corrected ordinary Egyptian fraction core at baseline e4f337c.

Six reviewed ordinary records give fixed-length duplicate removal, finite-state termination and marker-preserving padding. Corrected prose keeps runtime, denominator-size and evidence claims within the proof scope.

**Hypotheses:** Positive denominator invariant; cleanup sum strictly between zero and one. Padding a distinct expansion of one requires at least three terms and one specified marker.

**Evidence:** [independent local ordinary review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/reviews/egyptian/review.md); [saved study status](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json). All are saved records, not reruns by this map.

**Excluded headline:** Original upstream manuscript headline.

**Gaps:** Two optional coarse/iterated bound corollaries have no additional independent review. No global short-expansion asymptotic theorem. No Lean compilation or kernel checking of these ordinary study records; related standalone libraries have separate, narrower contracts.

**Study prerequisites:** Finite-state termination, Rational arithmetic. **Priority:** high.

**Statement sources:** [research/supplement/reviews/egyptian/corrected/study.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/reviews/egyptian/corrected/study.md), [research/supplement/STUDY-INDEX.json](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json).

**History:** Corrected scope/runtime/evidence/denominator-size wording; six statement IDs/hypotheses/conclusions retained.

<a id="scope-ordinary-transport"></a>
### Ordinary uniform-cube optimal-map obstruction

**Hierarchy:** Analysis → Optimal transport stability → Sharp one-third stability of Brenier maps. → Ordinary uniform-cube optimal-map obstruction at baseline e4f337c.

For uniform probability on [-1,1]^d with d>=2, 0<b<a and a+b<1, the quadratic optimal maps from max(-x1,a,x1) and max(-x1,a+b*x2,x1) yield W2^2=a*b^2 and map L2^2=b/2+a*b^2. The shrinking-mass path b=a/2 rules out uniform exponents above 1/3.

**Hypotheses:** d>=2; 0<b<a; a+b<1; uniform cube probability. Quadratic optimal-map identification uses the ordinary measure proof, not finite arithmetic alone.

**Evidence:** [independent local ordinary review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/reviews/transport/audit-report.md); [saved study status](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json). All are saved records, not reruns by this map.

**Excluded headline:** Original upstream manuscript headline.

**Gaps:** No positive global upper estimate or endpoint proof. No Lean compilation or kernel checking of these ordinary study records; related standalone libraries have separate, narrower contracts.

**Study prerequisites:** Convex affine maxima, Pushforward measures, Quadratic duality. **Priority:** medium.

**Statement sources:** [research/supplement/transport-stability/proof.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/transport-stability/proof.md), [research/supplement/STUDY-INDEX.json](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json).

<a id="scope-ordinary-blocks"></a>
### Ordinary positive-block Gram study

**Hierarchy:** Linear algebra and operator theory → Positive semidefinite block matrices → The complete Crouzeix conjecture. → Ordinary positive-block Gram study at baseline e4f337c.

Ten reviewed theorem/identity records derive Hilbert-Schmidt block comparisons from Gram factorization, exact sum/product deficits and equality conditions, including singular and zero cases.

**Hypotheses:** Finite complex PSD full block matrix; Hilbert-Schmidt normalization is unnormalized. Positive diagonal norms required for normalized equality conditions.

**Evidence:** [independent local ordinary review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/reviews/positive-blocks/parent-independent-review.md); [saved study status](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json). All are saved records, not reruns by this map.

**Excluded headline:** Original upstream manuscript headline.

**Gaps:** Five background nodes are additional; the complete Crouzeix theorem is excluded. No Lean compilation or kernel checking of these ordinary study records; related standalone libraries have separate, narrower contracts.

**Study prerequisites:** Gram matrices, Trace identities, Cauchy-Schwarz. **Priority:** high.

**Statement sources:** [research/supplement/positive-blocks/study.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/positive-blocks/study.md), [research/supplement/STUDY-INDEX.json](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json).

<a id="scope-ordinary-moments"></a>
### Ordinary mixed-moment foundations and cancellation

**Hierarchy:** Number theory and analysis → Mixed moments and special constants → Irrationality of Catalan’s constant. → Ordinary mixed-moment foundations and cancellation at baseline e4f337c.

Twenty-one reviewed records separate analytic integrability and exchanges from rational recurrence decompositions. Taylor contact of order L removes the displayed zeta2 coordinate for j<L, leaving rational-plus-rational-Catalan expressions.

**Hypotheses:** Rational polynomials and declared contact/order conventions. Integrability and exchange proofs are separate from finite rational recurrence checks.

**Evidence:** [independent local ordinary review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/mixed-moments/audit.md); [saved study status](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json). All are saved records, not reruns by this map.

**Excluded headline:** Original upstream manuscript headline.

**Gaps:** No Catalan irrationality, independence or arithmetic nonmembership theorem. Broader ordinary clauses are not all in the separate Lean core. No Lean compilation or kernel checking of these ordinary study records; related standalone libraries have separate, narrower contracts.

**Study prerequisites:** Lebesgue integration, Power series, Rational recurrences. **Priority:** advanced.

**Statement sources:** [research/supplement/mixed-moments/study.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/mixed-moments/study.md), [research/supplement/STUDY-INDEX.json](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json).

<a id="scope-ordinary-convex"></a>
### Ordinary analytic convex approximation study

**Hierarchy:** Geometry and analysis → Finite-dimensional convex approximation → The complete Crouzeix conjecture. → Ordinary analytic convex approximation study at baseline e4f337c.

Nineteen reviewed ordinary records use finite support directions and exponential barriers for analytic convex outer approximation, quantitative bounds and nesting. The ordinary scope extends beyond the separate smooth Lean core.

**Hypotheses:** Finite-dimensional inner-product ambient space; nonempty compact convex set. Positive direction-net, slack and exponential-scale conditions are retained per theorem.

**Evidence:** [independent local ordinary review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/convex-approximation/audit.md); [saved study status](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json). All are saved records, not reruns by this map.

**Excluded headline:** Original upstream manuscript headline.

**Gaps:** Rational checks and floating-point illustrations do not prove analytic conclusions. No source headline theorem validation; no automatic Lean status transfer. No Lean compilation or kernel checking of these ordinary study records; related standalone libraries have separate, narrower contracts.

**Study prerequisites:** Support functions, Analytic implicit function theorem, Convex geometry. **Priority:** advanced.

**Statement sources:** [research/supplement/convex-approximation/study.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/convex-approximation/study.md), [research/supplement/STUDY-INDEX.json](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json).

<a id="scope-ordinary-finite-field"></a>
### Ordinary finite-field mixing and local lifts

**Hierarchy:** Number theory → Additive combinatorics over finite fields → Short Egyptian fractions. → Ordinary finite-field mixing and local lifts at baseline e4f337c.

Ten reviewed records cover normalized Fourier mixing, sufficient four-product coverage and local positive-divisor lifting, including broader heterogeneous formulations outside the exported Lean core.

**Hypotheses:** Prime-field hypotheses, uniform independence and nonempty sampling sets where stated. Ordered tuples and multiplicities are retained.

**Evidence:** [independent local ordinary review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/reviews/finite-field-mixing/independent-review.md); [saved study status](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json). All are saved records, not reruns by this map.

**Excluded headline:** Original upstream manuscript headline.

**Gaps:** No optimal product count, distinctness theorem or global Egyptian-fraction constant. No Lean compilation or kernel checking of these ordinary study records; related standalone libraries have separate, narrower contracts.

**Study prerequisites:** Finite Fourier inversion, Character orthogonality. **Priority:** medium.

**Statement sources:** [research/supplement/finite-field-mixing/study.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/finite-field-mixing/study.md), [research/supplement/STUDY-INDEX.json](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/supplement/STUDY-INDEX.json).

<a id="scope-ordinary-radial"></a>
### Ordinary radial contact geometry

**Hierarchy:** Functional analysis → Normed-space geometry → Tingley’s sphere-isometry problem. → Ordinary radial contact geometry at baseline e4f337c.

The reviewed ordinary study proves positive unique sphere contact from an interior center, quantitative radius/contact/inverse estimates, and parameter perturbation bounds. It contains additional examples and estimates beyond the formal core.

**Hypotheses:** Real normed space, norm(c)<1; unit direction for unit-direction bounds. No completeness or finite-dimension requirement for contact existence.

**Evidence:** [independent local ordinary review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/starter/reviews/radial-review.json). All are saved records, not reruns by this map.

**Excluded headline:** Tingley's sphere-isometry theorem.

**Gaps:** Not every extra prose estimate or sharpness example is formalized. Ordinary study itself has no Lean verification.

**Study prerequisites:** Normed spaces, Scalar intermediate value theorem, Lipschitz estimates. **Priority:** high.

**Statement sources:** [research/starter/radial-maps/study.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/starter/radial-maps/study.md), [research/starter/radial-maps/provenance.json](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/starter/radial-maps/provenance.json).

<a id="scope-ordinary-pi-bridge"></a>
### Ordinary Diophantine-to-tangent bridge

**Hierarchy:** Number theory → Diophantine approximation and series → The irrationality exponent of π is 2. → Ordinary Diophantine-to-tangent bridge at baseline e4f337c.

A nearest odd-pole rational approximation and sine chord estimate convert PiDiophantine into eventual polynomial tangent growth, implying the cubic limit and absolute cubic series convergence.

**Hypotheses:** For every real nu>2, for all sufficiently large positive integers q and every integer p, abs(pi-p/q)>=q^(-nu). This PiDiophantine hypothesis is assumed, not proved here.

**Evidence:** [independent local ordinary review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/starter/reviews/pi-review.md). All are saved records, not reruns by this map.

**Excluded headline:** Proof of the irrationality exponent of pi. Upstream comparator configuration as evidence of a successful compiler run.

**Gaps:** Full source manuscript not reviewed. Ordinary bridge records have no Lean status; standalone tangent projects provide separate scoped evidence.

**Study prerequisites:** Trigonometry, Nearest poles, Rational approximation, p-series. **Priority:** medium.

**Statement sources:** [research/starter/pi-bridge/study.md](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/starter/pi-bridge/study.md), [research/starter/pi-bridge/sources.json](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/research/starter/pi-bridge/sources.json).

## Suggested learning route

Start with radial contact, exact-length Egyptian cleanup, positive-block Gram identities and rational LP certificate soundness. Their inputs and boundary cases are concrete. Continue to the conditional tangent bridge and harmonic packing, then finite-field Fourier mixing. Study convex barriers and actual atomic target-cost measures after their analysis prerequisites; mixed-moment cancellation needs a separate ledger for analytic exchanges and rational identities.

These priorities concern accessibility and reuse, following the [verified techniques guide](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/learning-guide/verified-techniques.md) and its [finalization update](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/learning-guide/STATUS-FINALIZATION-2026-10-11.md). They are not a ranking of the source manuscripts or evidence of novelty. No new open-problem proof is attempted.
