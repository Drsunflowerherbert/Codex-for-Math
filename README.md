# Codex for Math

**Directory branch: `main`.** The repository default is still `codex/tangent-limit`:
GitHub rejected the integration's default-change request with HTTP 403.
Thirteen topic renames are complete; the original tangent branch's rename
remains pending. See [remaining actions](docs/MIGRATION.md#remaining-administration-actions).

A directory of mathematical studies, scoped Lean libraries, exact-computation
tools and learning materials. Research files live on the topic branches;
`main` contains this directory and its navigation documents.

**[Browse the project catalog](docs/CATALOG.md)** for recommended reading editions,
exact research links, evidence and limitations. Use the
**[branch map](docs/BRANCHES.md)** for current names and the complete rename table.

## Find work by topic

| Topic | Start here |
| --- | --- |
| Analysis and integration | [Tangent, radial contact, matrices, approximation, mixed moments, transport and integral examples](docs/CATALOG.md#analysis-and-integration) |
| Optimisation | [LP toolkit, sparse study, paper and critical-point classifier](docs/CATALOG.md#optimisation) |
| Discrete mathematics | [Egyptian fractions, finite-field mixing and paused Hadamard study](docs/CATALOG.md#discrete-mathematics) |
| Dynamical systems and paper reviews | [Holomorphic Anosov review and its explicit limits](docs/CATALOG.md#dynamical-systems-and-paper-reviews) |
| Formal verification and tooling | [Evidence tools, hardening and exact root certificates](docs/CATALOG.md#formal-verification-and-tooling) |
| Research maps and learning materials | [Corpus studies, techniques, competition practice and field map](docs/CATALOG.md#research-maps-and-learning-materials) |

## Choose an entry point

- [Integrated research collection](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/integrated): the shared baseline, with later LP, transport and evidence continuations.
- [Integral problems](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/research/integral-examples/integral-examples/PROBLEMS.md): start with the problem, then follow the collection's conventions and solutions.
- [LP paper](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/research/lp-paper/lp-paper/README.md): exposition before the support study and certificate toolkit.
- [Competition practice](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/research/contest-library/contest-library/PROBLEMS.md): spoiler-free problem retrieval.
- [Field map](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/research/research-map/research-map/FIELD-MAP.md): subject-based research retrieval.
- [Original tangent project](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/codex/tangent-limit/tangent-limit/README.md): conditional cubic limit and absolute summability.

## Branch conventions and evidence

- `main`: repository directory and catalog; default switch pending.
- `research/<topic>`: recommended project branches or integrated collection.
- `archive/<topic>-source`: earlier source checkpoints whose reviewed publication copies appear in `research/integrated`.

The tangent branch is the one pending naming exception. The new names are
stable and use lowercase words separated by hyphens; dates remain in
the project records and commit history. A `research/` name does not imply that
a project is active, unconditional or formally verified. The catalog preserves
the distinctions between scoped formal results, conditional proofs, ordinary
reviews, exact finite checks, paused experiments and reference metadata.

Research links in the catalog remain pinned to their original full commits.
Saved evidence is historical, and each project retains its own assumptions,
trust boundaries and attribution. This organization change adds no mathematical
result or verification claim.

If you used an old branch name, read [branch and clone migration](docs/MIGRATION.md).
