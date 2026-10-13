# Codex for Math

Reviewed additions from 13 October 2026 are summarized in the
[round report](publication/ROUND-2026-10-13.md):

| Deliverable | Scope and evidence |
| --- | --- |
| [LP certificates](lp-certificates/README.md) | Exact rational certificates, original-real Lean soundness, bounded numeric export and fresh per-input rechecking; incomplete exact finder. Parser/cache trust and saved-process intake limits are explicit. |
| [Transport continuation](transport-sharpness/README.md) | Finite/scalar exponent obstructions and actual two-dimensional Borel target-coupling cost. Cube-source maps and actual L2 map-norm identification remain deferred. |
| [Evidence hardening](evidence-hardening/README.md) | Stricter saved-receipt integrity and unreplaced Git-tree byte checks, plus one accepted and nine rejected fixed Lean fixtures. Saved inspection grants no fresh Lean pass. |

Completed research and standalone Lean projects published from verified source
bundles on 11 October 2026:

| Deliverable | Scope and evidence |
| --- | --- |
| [Research data](research/README.md) | Revision-pinned corpus inventory, initial studies, seven reviewed ordinary studies and 81 core records; finite computations and numerical illustrations are distinct from Lean verification. |
| [Radial contact](radial-contact/README.md) | 47 audited Lean declarations in arbitrary real normed spaces; explicit assumptions, independent review, reproducibility checks and 27 regression tests. |
| [Exact-length Egyptian fractions](egyptian-exact/README.md) | 42 Lean theorems for exact-length cleanup, finite-state termination and marker-preserving padding, with reviews and exact checks. |
| [Sharp tangent series](tangent-sharp/README.md) | Conditional absolute summability iff real s > 1, and unconditional nonsummability for s ≤ 1; 78 declaration audits. PiDiophantine remains assumed. |
| [Finite-field product mixing](finite-field-product-mixing/README.md) | 85 audited declarations, including the four-product covering criterion and local divisor lift; supplied completed build evidence, with publication-only receipt inspection. |
| [Positive-block matrix inequalities](positive-blocks/README.md) | 142 public Lean declarations, full equality classification and common-support normal form; completed independent source review and fresh build/type/axiom checks. |
| [Convex approximation](convex-approximation/README.md) | Nine-module smooth quantitative approximation core and actual certified nested sequence; 145 inventoried declarations plus the Plane abbreviation, with independent review and fresh audits. Analytic charts and sphere/Jordan parametrizations remain deferred. |
| [Mixed-moment cancellation](mixed-moment/README.md) | Actual-integral cancellation for rational polynomials under explicit analytic contact; 17 modules, 513 public declarations and 835 project-origin constants. Broader analytic clauses and the exceptional tail endpoint remain deferred. |
| [Math evidence toolkit](math-evidence/README.md) | Source/assumption/dependency records, safe byte intake and separate fixed live gate; 283 fresh suite checks and eight extracted consumer commands, with explicit trust limits. |
| [Verified techniques guide](learning-guide/verified-techniques.md) | Nine reusable proof methods, examples and study plan; see the dated [initial addendum](learning-guide/STATUS-2026-10-11.md) and [finalization update](learning-guide/STATUS-FINALIZATION-2026-10-11.md). |

The mixed-moment final source/evidence archive has now been received and its
bytes verified directly. Its earlier transfer failure remains historical in
the [transfer record](publication/PENDING-TRANSFER.json). The separately
published ordinary study retains its original verification status.

All Lean projects pin Lean/mathlib 4.24.0. Mathematical scope, current versus
historical evidence, exclusions, privacy review and reproduction records are
documented in [publication/](publication/README.md). Retained upstream text is
covered by [third-party attribution](THIRD-PARTY.md); no overall license or
novelty claim is introduced. The original `tangent-limit/` project below is
unchanged.

The standalone project in [tangent-limit/](tangent-limit/README.md) proves that
`tan(n)/n³ → 0` over positive integers and that `Σ |tan(n)|/n³` converges,
conditional on an explicit π-approximation hypothesis. It does not prove or
assert that hypothesis.

The results compiled with pinned Lean/mathlib 4.24.0. Sources, mathematical
proof, theorem statements, axiom audits, build logs, source attribution, and
milestone records are included. There are no proof placeholders or added axioms.

```bash
cd tangent-limit
./scripts/setup.sh
./scripts/verify.sh
```

See the [project README](tangent-limit/README.md) for dependency pins,
reproduction requirements, verification evidence, and its scope.
