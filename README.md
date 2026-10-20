# Codex for Math

A topic-based guide to this repository's mathematical studies, scoped Lean
libraries, exact-computation tools and learning materials.

**Start with the [project catalog](docs/CATALOG.md).** It links to the recommended
research edition of each deliverable and states its evidence and limitations.
The [branch map](docs/BRANCHES.md) explains all 14 branches and their ancestry.

## Find work by topic

| Topic | Recommended entry points |
| --- | --- |
| Analysis and integration | [Tangent limit](tangent-limit/README.md), [formal analysis libraries](docs/CATALOG.md#analysis-and-integration), [integral examples](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/dafa2d2c35b425ca510def9aae3bb17839e67aa5/integral-examples/PROBLEMS.md) |
| Optimisation | [LP toolkit, sparse study, paper and critical-point classifier](docs/CATALOG.md#optimisation) |
| Discrete mathematics | [Egyptian fractions, finite-field mixing and paused Hadamard study](docs/CATALOG.md#discrete-mathematics) |
| Dynamical systems and paper reviews | [Holomorphic Anosov review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2d6f543fcfe182c3df7d5316c0fba0279eebfe4f/holomorphic-anosov-review/README.md) |
| Formal verification and tooling | [Evidence toolkit, hardening and exact root certificates](docs/CATALOG.md#formal-verification-and-tooling) |
| Research maps and learning materials | [Corpus studies, field map, techniques and competition practice](docs/CATALOG.md#research-maps-and-learning-materials) |

## Choose a reading path

- **Study analysis:** [integral problems](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/dafa2d2c35b425ca510def9aae3bb17839e67aa5/integral-examples/PROBLEMS.md) → [measure conventions](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/dafa2d2c35b425ca510def9aae3bb17839e67aa5/integral-examples/CONVENTIONS.md) → individual solutions from the collection.
- **Inspect a formal result:** [techniques guide](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/learning-guide/verified-techniques.md) and its [finalization update](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/learning-guide/STATUS-FINALIZATION-2026-10-11.md) → a project's README → exact statements, assumptions and saved evidence.
- **Read LP research:** [paper PDF](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/16075fc88d1cec51dc3c8f137bca3fe70c6f9520/lp-paper/sparse-lp-certificates.pdf) → [ordinary support study](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-sparse-discovery/README.md) → [certificate toolkit](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/lp-certificates/README.md).
- **Find a subject or practice problem:** [field map](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/34e3e11e4c37109bfc06f4f195a62a2cf992c5b0/research-map/FIELD-MAP.md) or [spoiler-free competition index](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/ef8032ed20f05fb100e95fc287eefb5d3e431543/contest-library/PROBLEMS.md).

## How the repository is organized

The existing default branch is `codex/tangent-limit`. Its root is now the repository
landing page; it still contains the original tangent project below. Most later
research files live on other branches. Follow the catalog links to their exact
research commits; a relative path on this branch cannot reach a sibling branch.

The integrated baseline is [`codex/research-2026-10-11`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/codex/research-2026-10-11). Several branches inherit
that collection unchanged and add one directory. Four earlier continuation
branches are source checkpoints whose reviewed copies were integrated later.
Those copies are not separate mathematical results. No branches were renamed,
deleted or merged by this documentation cleanup.

Status labels distinguish **scoped formal results**, **conditional formal
results**, **reviewed ordinary proofs**, **exact finite computations**,
**paused experiments** and **reference metadata**. Saved builds and reviews are
reported historical evidence, not fresh verification by this cleanup. Conditions
and deferred obligations remain part of each result's scope. See the catalog
for project-specific limits and the branch map for snapshot-integrity guidance.

## Original tangent-limit project

The standalone project in [tangent-limit/](tangent-limit/README.md) proves
`tan(n)/n³ → 0` over positive integers and convergence of `Σ |tan(n)|/n³`,
**conditional on an explicit π-approximation hypothesis**. It does not prove
that hypothesis. The published project records Lean/mathlib 4.24.0 build,
statement and axiom evidence; all project bytes and dependency pins are preserved.

```bash
cd tangent-limit
./scripts/setup.sh
./scripts/verify.sh
```

Read the [project README](tangent-limit/README.md) for reproduction requirements,
proof notes, exact assumptions and evidence. The [original repository snapshot](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/d00a89dd9ce6c8ef782234d28c93e69cb712c947/README.md)
remains available in Git history. The broader publication's
[attribution](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f/THIRD-PARTY.md) and each project's notices retain their own scope;
this index introduces no repository-wide license or novelty claim.
