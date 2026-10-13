# Inspected primary sources and source-use limits

## Mathematical background

**Stephen Boyd and Lieven Vandenberghe, _Convex Optimization_, Cambridge
University Press, 2004.** The PDF is distributed from the authors' official
Stanford book page:

- [Official book page](https://web.stanford.edu/~boyd/cvxbook/)
- [Official book PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)

Inspected passages, using **printed book page numbers**:

| Passage | Location | Use in these notes |
| --- | --- | --- |
| General LP with inequalities and equalities, and standard-form conversion | §4.3, pp. 146–148, equations (4.27)–(4.29) | Context for keeping free original variables and explicit rows. |
| Inequality and equality multipliers; lower-bound argument | §§5.1.1 and 5.1.3, pp. 215–216 | Context for sign restrictions and weak-duality reasoning. |
| Inequality-form LP dual and weak duality | §§5.2.1–5.2.2, p. 225, equations (5.21)–(5.23) | Compare signs after converting this toolkit's maximization objective to the book's minimization convention. |
| Complementary slackness | §5.5.2, pp. 242–243, equation (5.48) | Context for the zero weighted-slack condition. |
| Weak and strong alternatives and Farkas' homogeneous alternative | §5.8, pp. 259–263; the Farkas statement is in §5.8.3, p. 263, equations (5.87)–(5.90) | Background only; no completeness theorem is imported into the Lean result. |

The retrieved PDF has 714 physical pages; printed page `r` in these passages is
PDF page `r+14` (one-based). This was checked at printed pp. 146 and 263, so
links using `#page=...` refer to PDF pages rather than printed labels.

The author page states that Cambridge University Press holds copyright and
permits the authors to make the book available online. No PDF or substantial
excerpt is redistributed here. Proofs and examples in `mathematics.md` are
independently written; citations supply context, not kernel evidence.

Retrieval on 2026-10-13 UTC:

```
curl --fail --location --silent --show-error \
  https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf \
  -o /tmp/lp-bv-cvxbook.pdf
pdftotext -layout /tmp/lp-bv-cvxbook.pdf /tmp/lp-bv-cvxbook.txt
sha256sum /tmp/lp-bv-cvxbook.pdf
```

All commands exited `0`. Observed PDF SHA-256:

```
40d976c83c18cce1900eff8c41bd5ad408c102b813af39d05ff85678ccf8d76e
```

The hash identifies the retrieved bytes; the live author URL is not a revision
pin or an assertion that future downloads must have the same bytes.
The web-reader PDF retrieval timed out twice; the direct HTTPS download and
local text inspection succeeded. The author landing page was read successfully.

**Official authored lecture slides.** Stephen Boyd, Lieven Vandenberghe, and
Parth Nobel, revised _Convex Optimization_ slides, linked from the same official
book page:

- [Official slide PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf)

Inspected through the PDF web reader: slide 5.12 (weak and strong duality;
physical PDF page 166), slide 5.19 (complementary slackness; physical page 173),
and slide 5.35 (Farkas' lemma; physical page 189). These confirm the book
references; they are not separate machine-checked evidence.

**J. Farkas, “Theorie der einfachen Ungleichungen.”** _Journal für die reine und
angewandte Mathematik_ 124 (1902), pp. 1–27.
[Publisher DOI](https://doi.org/10.1515/crll.1902.124.1).
The authors' book bibliography, entry `[Far02]` (printed p. 688), gives these
bibliographic details, and the publisher search result agrees. Direct publisher
and EuDML article views were blocked (`405` and `403`, respectively). The full
original article was **not inspected**, so no exact theorem or proof from it is
claimed as a checked source. It is retained only as a primary historical
reference, not as support for a new completeness claim.

## Project evidence protocol

The existing repository's `math-evidence/README.md`, `RUNBOOK.md`,
`VERIFICATION.md`, and `LEAN-RECEIPTS.md` were inspected before writing the review.
Their stated fixed plans concern pinned tangent/sample targets. The LP work
must supply its own fresh compiler output and declaration checks; stored
receipts, source hashes, hand calculations, and exact Python tests do not grant
a Lean pass. The protocol also explicitly excludes claims of an independent
kernel implementation or validated native Mac/installed MRS integration.

No `AGENTS.md` or `.agents/skills/*/SKILL.md` was found under `/workspace` by
the reviewer's independent filesystem search. No third-party text, dependency
tree, executable, or license is copied into these notes, and no new license is
assigned by the reviewer.
