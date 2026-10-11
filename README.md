# Codex for Math

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
| [Verified techniques guide](learning-guide/verified-techniques.md) | Nine reusable proof methods, examples and study plan; see the dated [initial addendum](learning-guide/STATUS-2026-10-11.md) and [finalization update](learning-guide/STATUS-FINALIZATION-2026-10-11.md). |

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
