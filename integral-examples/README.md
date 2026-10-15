# Concrete Lebesgue and Hausdorff integral applications

A first collection of **16 fully worked examples**, written for an analysis
student. Start with the [problem index](PROBLEMS.md), then open the separate
solution that you want. The examples favor explicit computations, stated
hypotheses, and direct arguments explaining why the integration theorem applies.

- [Measures and theorem conventions](CONVENTIONS.md): normalized Hausdorff
  measure, completed-product sections, signed integrability, area and coarea.
- [Problem index](PROBLEMS.md): no computed answers.
- [Counterexample atlas](COUNTEREXAMPLES.md): precise failures and sufficient
  conditions for exchanging sums, limits, derivatives, and integrals.
- [Full worked collection, PDF](pdf/integral-examples.pdf) and
  [editable LaTeX](pdf/integral-examples.tex).
- [Compact guide, PDF](pdf/guide.pdf) and [LaTeX](pdf/guide.tex).
- [Source references](SOURCES.md), [source snapshot hashes](checks/source-references.json),
  and [verification ledger](VERIFICATION.md).
- [Machine-readable index](index.json) without results, and
  [full metadata](metadata.json) with hypotheses, results, and review status.

## Find a technique again

From the repository root, using Python 3 with its standard library:

```bash
python3 integral-examples/find_examples.py --topic coarea
python3 integral-examples/find_examples.py --technique multiplicity
python3 integral-examples/find_examples.py --prerequisite dominated
python3 integral-examples/find_examples.py --text concentration
python3 integral-examples/find_examples.py --list-tags
```

Filters are case-insensitive substring matches and combine with AND. They print
titles, tags, and paths relative to `integral-examples/`. The `--text` filter
searches IDs, titles, paths, topics, prerequisites, and techniques; it does not
search solution prose or recorded hypotheses/results. Add `--solutions` to
print the recorded result.
The files remain ordinary Markdown and JSON; retrieval needs no hosted service.

## How to study with the collection

For each problem, identify the function, its domain, the measure, and the
integrability question before computing. In a region problem, write the
indicator and determine its sections. For signed integrals, examine the absolute
value or the positive and negative parts. For a parametrization, compute the
Jacobian and count preimages before identifying the answer with an integral over
the image. For a parameter limit, write the proposed majorant explicitly.

E01–E06 cover Lebesgue integration and iterated integrals; E07–E13 cover curves,
surfaces, area, coarea, and singular maps; E14–E16 cover limit and derivative
exchanges and approximate identities. Cross-links in the atlas make failure
cases easy to retrieve alongside their positive criteria.

## Reproduce the checks and PDFs

```bash
python3 integral-examples/checks/check_examples.py
python3 integral-examples/checks/check_collection.py
python3 integral-examples/build.py
```

The concrete identity checker uses SymPy and mpmath. The collection checker and
retrieval command use only the Python standard library. The build uses Pandoc
and pdfLaTeX. See [checks/requirements.txt](checks/requirements.txt) for the
versions actually used. The checked-in PDF and LaTeX need no build tools to read.

Independent model reviewers audited every example; the ledger records the
scope, findings, and revisions. Symbolic and numerical checks supplement those
reviews and are **not proofs of analytic hypotheses**. No Lean verification or
human peer review is claimed. General measure-theoretic theorems are cited
prerequisites; this collection does not reprove all of measure theory.

All collection changes are confined to `integral-examples/` on branch
`codex/integral-examples-2026-10-15`, based on the integrated research commit
`e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f`. Other research branches are independent.
The earlier paper was not used or reconstructed. No third-party problem
collection or source PDF is reproduced, and no license is assigned here to the
cited sources or to unrelated repository work.
