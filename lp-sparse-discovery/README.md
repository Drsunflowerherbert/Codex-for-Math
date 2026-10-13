# Sparse LP certificate discovery: a focused study

For hand-sized rational LPs, eliminate consistent equalities exactly, then
search for a sparse nonnegative combination of the remaining projected
inequalities. A bound certificate over a **nonempty** feasible set needs at
most k inequalities, where

```
k = rank(A N) = rank([A; E])-rank(E),  im(N)=ker(E).
```

An infeasibility certificate can require k+1 inequalities. A known feasible
optimizer permits a smaller active-row search. Equality multipliers are
recovered afterwards by exact linear algebra. No primal slack variables,
artificial variables, or splitting of equalities is needed.

- [Study and proofs](study.md): existence, support reduction, rationality,
  ideal finite-search completeness, practical ordering and safe pruning.
- [Worked examples](examples.md): signed equality recovery, exact fractions,
  sharp support bounds, duplicate rows, zero normals, no-vertex optima, and
  failures of unnecessary RHS normalization or coefficient grids.
- [Primary references](SOURCES.md): checked author-hosted sources and precise
  locations; no novelty claim.
- [Fixture benchmark](benchmark/README.md): exact reproducible comparisons of
  direct normal search against augmented search with a vertical residual
  generator, including first-success and exhaustive counts.
- [Independent mathematical review](reviews/mathematical-review.md) and
  [computational review](reviews/computational-review.md).

The benchmark's three-dimensional sharp bound needs 8 attempted subsets with
direct normal search, versus 12 to first success and 16 exhaustively with the
augmented choice. Reordering one seven-row fixture changes first success from
8 attempts to 2; exhaustive counts remain unchanged. These are counts on
specified fixtures, not speed measurements or a general solver comparison.

Reproduce with Python 3.12 and the standard library:

```sh
python3 lp-sparse-discovery/benchmark/benchmark.py > /tmp/lp-sparse-results.json
cmp /tmp/lp-sparse-results.json lp-sparse-discovery/benchmark/results.json
python3 -m unittest discover -s lp-sparse-discovery/benchmark -v
python3 lp-sparse-discovery/reviews/independent_check.py
```

The mathematical procedure is complete only when it exhausts the appropriate
independent supports with exact arithmetic and satisfies its stated assumptions.
Finite benchmark evidence and ordinary proofs are **not formal verification**.
The code is a fixture experiment; it provides no general LP input interface,
whole-solver status classifier or Lean bridge. Budget exhaustion or a failed
truncated search remains inconclusive.

This standalone directory was prepared on
`codex/lp-sparse-discovery-2026-10-13`, based on verified research baseline
`b1d6c20e2f02b484d09c5285e67d842b369f9df0`. The separate `lp-certificates/`
component was inspected at frozen commit
[`032db09354d41b58c2e9211ed7e69024a3e74010`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/032db09354d41b58c2e9211ed7e69024a3e74010/lp-certificates).
Its deliberately incomplete finder, certificate soundness proofs and checked
export bridge were neither copied nor changed. This branch adds only
`lp-sparse-discovery/`; it does not integrate that sibling component.

All new proofs, examples and code were authored for this study. Public files
include no source PDFs, dependency code, credentials, private datasets or
private archives. The repository's existing attribution is preserved, and no
new or overall license is assigned. See [PROVENANCE.json](PROVENANCE.json) and
[publication review](evidence/publication-review.md) for the scoped evidence.
