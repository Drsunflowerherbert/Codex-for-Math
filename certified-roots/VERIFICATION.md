# Verification, review, and trust limits

First-edition verification date: 15 October 2026. The checked environment used
Python 3.12.14. No third-party Python packages, floating-point root solver,
network lookup, or credentials are needed to check the certificates.

## Reproduce the checks

From the repository root:

```bash
python3 -B -m unittest discover -s certified-roots/tests -v
python3 -B certified-roots/reviews/independent_check.py
python3 -B certified-roots/verify.py certified-roots/examples/circle-line.json
python3 -B certified-roots/verify.py certified-roots/examples/circle-parabola.json
python3 -B certified-roots/verify.py certified-roots/examples/tiny-residual-two-roots.json
python3 -B certified-roots/verify.py certified-roots/examples/tiny-residual-no-root.json
```

The two final commands intentionally exit `1`: the candidates are well formed
but fail this sufficient test. The two successful examples exit `0`; malformed
input exits `2`. Each command produces an exact JSON report. Fresh saved
reports, exit codes, environment information and hashes are in
[`evidence/verification.json`](evidence/verification.json), with complete
reports in [`evidence/example-results.json`](evidence/example-results.json).

## Results

The main suite passed **45 tests**. Its full output is in
[`evidence/test-results.txt`](evidence/test-results.txt). It covers:

- Polynomial tampering and rejected forged residual/Jacobian/result fields.
- Boundary self-inclusion, strict contraction at and below one, contraction
  without self-inclusion, zero residual at a singular root, and different
  coordinates attaining the worst residual and derivative bounds.
- Unequal radii, asymmetric signed preconditioners and exact pivot swaps.
- Exact interval arithmetic and derivative enclosures checked at independent
  rational sample points, including even powers crossing zero.
- Duplicate JSON keys, floats, nonfinite constants, boolean exponents,
  dimensions, singular matrices, invalid rationals, and resource boundaries.
- CLI exit codes and exact serialization of intermediate results larger than
  Python's default decimal-integer conversion limit.

The separately authored executable audit passed **2,237 cases**, with these
reported counts:

| Audit | Cases | Independent comparison |
| --- | ---: | --- |
| Matrix rank | 681 | Exact cofactor determinant versus checker elimination. |
| Affine systems | 604 | Point matrix arithmetic versus interval outputs, weighted norms, self-map conditions and errors. |
| Integer power ranges | 924 | Exact endpoint and zero extrema through degree 32. |
| Parser, resource and CLI boundaries | 18 | Explicit adversarial input and status expectations. |
| Large exact outputs | 6 | Separately chunked rational parsing and exact identities, including CLI output. |
| Worked systems | 4 | Hand-derived exact expectations. |

Its transcript is [`evidence/independent-results.txt`](evidence/independent-results.txt).
The audit uses fixed seeds for finite matrix samples. Case counts are not
claims of exhaustive correctness for all inputs.

## Independent review

Two separate review agents examined material written by other agents:

- [Mathematics review](reviews/mathematics-review.md): hypotheses, full proof,
  interval enclosure reasoning, uniqueness region, error formula, all displayed
  example arithmetic, source comparisons and theorem-to-code assumptions.
  Eight additional exact mathematical expectation checks passed.
- [Checker review](reviews/checker-review.md): parser and input contract,
  interval operations, differentiation, exact elimination, signed matrix
  products, weighted bounds, result semantics and adversarial tests. It also
  supplies the independent audit above.

Both reviews approve the bounded first edition with no unresolved blocking
finding. They identify reviewed file bytes using SHA-256 hashes. This is
independent agent review, not external peer review or machine-checked formal
verification. The final source/evidence snapshot is indexed by
[`evidence/manifest.json`](evidence/manifest.json); the manifest deliberately
excludes itself.

Review prompted three concrete improvements: an explicit alpha-theory norm
convention, clarification that the raw weighted error output can be capped by
box membership, and exact chunked serialization for arbitrarily long
intermediate integers. Regression tests cover the implementation changes.

## PDF

[`STUDY.pdf`](STUDY.pdf) is a ten-page reading copy of the reviewed Markdown
study and examples. It was built using Pandoc and XeLaTeX; representative
theorem and example pages were visually inspected, and text extraction
completed. It is not an additional mathematical source or an executable
certificate. To rebuild it, with those optional tools installed:

```bash
pandoc certified-roots/STUDY.md certified-roots/EXAMPLES.md \
  --from=markdown+tex_math_single_backslash --standalone --toc \
  --pdf-engine=xelatex -V geometry:margin=1in -V fontsize=11pt \
  -V colorlinks=true --metadata title='Exact Root Certificates' \
  --metadata date='15 October 2026' -o certified-roots/STUDY.pdf
```

PDF metadata can make independently built bytes differ. The supplied PDF's
hash is recorded; the Markdown and JSON inputs are canonical.

## Remaining assumptions and limitations

The mathematical proof establishes the theorem from its stated hypotheses.
The program's claim additionally trusts its reviewed source, Python's
integer/Fraction arithmetic and JSON implementation, the runtime and
hardware, and faithful input transcription. Tests and agent review do not
prove these components correct. No Lean development or Lean verification was
performed for this toolkit.

The certificate proves a statement about the exact rational polynomial system
in its input, not about an unspecified physical model or rounded source
coefficients. Natural interval dependency loss can make valid approximations
fail the sufficient test. Operational input limits do not give a worst-case
runtime or memory guarantee; the checker is a local research tool, not a
hardened service for hostile workloads.

The implemented criterion cannot certify a singular root and does not handle
complex roots, non-square systems, nonpolynomial functions or uncertain
coefficients. It does not search for certificates or enumerate all roots.
Uniqueness is confined to the stated closed box. A failed certificate proves
neither nonexistence nor multiplicity. A small residual alone proves neither
existence nor an error bound.

## Repository scope

The branch starts from integrated baseline
`e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f`. Only `certified-roots/` is added.
The initial checkout's older tangent reference and every existing project are
preserved. The publication uses the requested new branch without force push,
pull request or merge. Remote commit and file-byte verification is performed
after publication and reported with commit-pinned links; a local test record
alone is not evidence that remote content was checked.
