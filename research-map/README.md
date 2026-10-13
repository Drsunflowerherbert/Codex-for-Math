# Research map — first edition, 13 October 2026

Use this map to find problem families, distinguish headline claims from checked scope, and choose bounded future study. It is metadata-complete for the pinned corpus and partial as a mathematical evidence audit. **No famous problem is labelled solved in this edition.**

The research baseline is [`e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f`](https://github.com/Drsunflowerherbert/Codex-for-Math/commit/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f). Its recorded official upstream is [`openai/math`](https://github.com/openai/math). The [dated source audit](SOURCES.md) identifies the latest observed upstream commit and its changes from the historical October8 snapshot. Manuscript source links and historical versions remain pinned; a branch name alone is not a reproducible source.

- [Field → subfield → problem family → manuscript map](FIELD-MAP.md)
- [Major-problem claim index and reliability tiers](MAJOR-CLAIMS.md)
- [Our scoped reusable libraries and ordinary studies](SCOPED-RESULTS.md)
- [Searchable self-contained catalog](index.html): download and open locally; GitHub's file view shows source, not a hosted app.
- [Machine-readable catalog](catalog.json), [CSV export](catalog.csv), and [actual coverage](coverage.json)
- [Schema and evidence rubric](SCHEMA.md), [provisional taxonomy](TAXONOMY.md), [version history](version-history.json), and [independent catalog review](REVIEW.md)

## Immediate findings

The three withdrawn family032 Hodge-related manuscripts have explicit proof-error notices. The surviving CM Hodge claim and conditional Kuga–Satake work require their own statement and dependency review. Three withdrawals do not mean that only three manuscripts have issues: the inventory also records 14 correction/repair/hypothesis-related directory changes and 13 citation-only revisions.

A quasi-Riemann zero-free half-plane is different in scope from the Riemann hypothesis. Low-Selmer-corank BSD is restricted by that hypothesis. General Hilbert16 claims cannot be certified by a formalization of a particular two-cycle quintic system. Pi/tangent libraries retain a Diophantine premise; mixed-moment, positive-block, convex and radial libraries cover their identified supporting statements. They do not certify Catalan irrationality, Crouzeix, Tingley or other manuscript headline claims.

The author title and abstract disagree for family134's generalized star-height bound (three versus thirteen). This map preserves both source descriptions and flags the conflict instead of choosing a bound.

Review coverage uses separate units: the major index has 29 entries across 16 families, with 25 statement/scope/notice inspections and four catalog-only entries. All 719 active manuscript rows retain metadata-only status; no complete upstream proof was independently validated here. All 21 local scoped-result groups have source/contract checks; eight received a new independent catalog spot review and 13 did not. Their earlier review/build receipts retain their original dates and scope.

## How to continue study

Start with the explicit contracts in the scoped-result index: radial geometry, exact-length Egyptian rewriting and positive-block identities have concrete prerequisites. Then study conditional tangent block estimates and finite-field Fourier mixing. Treat mixed-moment exchanges of integration and asymptotics as a separate analytic obligation. The existing [techniques guide](../learning-guide/verified-techniques.md) and its dated finalization updates give more detailed learning sequences.

For each major claim, next extract the complete theorem and every hypothesis, resolve repaired versions and internal dependencies, inspect the actual configured formal statement where available, and obtain independent mathematical review. Record any successful Lean run with its precise type, imports, axiom audit, toolchain and correspondence assessment. Only then assess whether the result covers the original famous problem. This edition organizes that work; it does not begin new open-problem proofs.

## Reproduce and verify

From the repository root, run `python3 research-map/build.py` to rebuild catalog, CSV, coverage, field map and HTML from the pinned inventory and reviewed overlays. Run `python3 research-map/verify.py` for structural, cross-reference, source-link and consistency checks. These commands do not run Lean or validate mathematical proofs. The catalog is usable offline; it makes no external network requests while searching.

## Attribution and modification notice

Derived source metadata is attributed to OpenAI/math and the exact commits in [SOURCES.md](SOURCES.md). The source snapshot's Apache2 license is retained at [publication/upstream/OpenAI-math-LICENSE.txt](../publication/upstream/OpenAI-math-LICENSE.txt); existing attribution is in [THIRD-PARTY.md](../THIRD-PARTY.md). This map reorganizes titles and short author metadata, preserves source/version links, adds editorial subfields and evidence annotations, and cites supporting source passages. It does not reproduce whole papers or redistribute upstream proof/dependency trees. No overall license, novelty or priority claim is introduced for our new annotations or libraries.
