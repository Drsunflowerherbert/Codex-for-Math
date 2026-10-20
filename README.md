# Codex for Math — integrated research collection

Branch: `codex/research-2026-10-11`. This is the shared integrated research baseline,
including the reviewed 11 October projects and 13 October LP, transport and
evidence continuations. Its name records its start date, not its final scope.

Use the [repository project catalog](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/codex/tangent-limit/docs/CATALOG.md) to find later standalone
deliverables, and the [branch map](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/codex/tangent-limit/docs/BRANCHES.md) to distinguish those additions
from inherited copies of this collection.

## Read by topic

| Topic | Local entry points | Scope and evidence |
| --- | --- | --- |
| Analysis and integration | [Tangent limit](tangent-limit/README.md), [sharp tangent series](tangent-sharp/README.md) | Conditional absolute summability results retain `PiDiophantine`; the sharp extension separately proves absolute nonsummability for real exponents at most one without it. |
| Analysis and integration | [Radial contact](radial-contact/README.md), [positive blocks](positive-blocks/README.md), [convex approximation](convex-approximation/README.md), [mixed moments](mixed-moment/README.md) | Published scoped Lean libraries with saved build/audit evidence. Mixed moments retains explicit analytic contact; deferred clauses remain deferred. |
| Analysis and integration | [Transport continuation](transport-sharpness/README.md) | Finite/scalar obstructions and actual Borel target-cost bridge; source-map and L2 map-norm formalization remain deferred. |
| Optimisation | [Rational LP toolkit](lp-certificates/README.md), [sparse discovery study](lp-sparse-discovery/README.md) | Toolkit has selected Lean soundness results and an incomplete finder; support study and fixture comparisons are ordinary mathematics, not a formalized general solver. |
| Discrete mathematics | [Egyptian fractions](egyptian-exact/README.md), [finite-field product mixing](finite-field-product-mixing/README.md) | Scoped formal libraries. Finite-field publication inspected supplied completed evidence rather than rerunning Lean. |
| Formal verification and tooling | [Math evidence](math-evidence/README.md), [evidence hardening](evidence-hardening/README.md) | Saved evidence is distinct from a fresh live pass; fixed gates have explicit trust limits. |
| Research maps and learning | [Research data](research/README.md), [reviewed supplement](research/supplement/README.md), [techniques guide](learning-guide/verified-techniques.md) | Ordinary studies and source-pinned metadata are distinct from Lean projects; use the guide's [finalization update](learning-guide/STATUS-FINALIZATION-2026-10-11.md). |

## Publication records

- [Publication overview](publication/README.md) and [13 October round report](publication/ROUND-2026-10-13.md).
- [Third-party attribution](THIRD-PARTY.md).
- [Exact integrated research snapshot before navigation changes](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/README.md) (`e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f`).

The later integral examples, critical-point classifier, root toolkit, LP paper,
Hadamard rounds, competition library and research map live on separate branches.
They are indexed in the catalog; they are not merged into this tree. The
holomorphic Anosov review is a separate branch from the original tangent baseline.

## Snapshot and evidence boundary

This root README is a navigation update. Project sources, PDFs, datasets,
toolchain pins and substantive project documentation are preserved. Saved build,
review and experiment records describe the pinned research snapshot linked
above; this cleanup did not rerun Lean, project scripts or experiments.
Where a historical manifest inventories a complete tree, its checks apply to
its own recorded source/baseline, which may predate this branch's addition. An
inherited manifest does not automatically cover every descendant that carries
it. This root edit adds a further documented navigation difference.
