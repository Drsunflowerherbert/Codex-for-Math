# Mixed moments and Taylor contact cancellation

A complete ordinary-proof study of the Family005 supporting moment identities, extracted from OpenAI/math revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

## Main result

For rational polynomials P and D, if

\[
 tP(t)/\sqrt{1-t^2}-D(t)=O(t^L),
\]

then, for every integer \(0\le j<L\),

\[
 M(P,j)-(3/2)Z(D,j)\in\mathbb Q+\mathbb QG.
\]

Here M and Z are the absolutely convergent mixed moments specified in the source, and G remains symbolic. The study verifies the source's scoped identities and gives an exact defect formula without assuming contact:

\[
 M(P,j)-(3/2)Z(D,j)=A_j+B_jG
       +(3/2)\zeta(2)[t^j](tP/\sqrt{1-t^2}-D),
\]

with explicit rational A and B. No error was found in the scoped moment and cancellation claims.

## Contents

- `study.md`: full proofs, analytic exchange ledger, rational formulas, small exact examples, and reusable extensions
- `theorems.json`: 21 theorem records, explicit hypotheses, and a validated 39-edge dependency graph
- `counterexamples.md`: omitted-condition tests, actual divergence examples, and careful distinctions between formal noncancellation and real-number nonmembership
- `lean-roadmap.md`: a future formalization plan with explicit completion gates
- `certificates.py`: original standard-library Python exact-arithmetic program
- `certificates.json`: its 17,805 passing checks, symbolic moment tables, contact examples, and rational series-tail bounds
- `build_theorem_index.py`: original metadata writer and dependency-DAG validator
- `audit.md`: independent mathematical audit of the scoped source
- `verification.json`: provenance, file hashes, and final bundle checks

## What is new in the extraction

The source's particular polynomial rows are replaced by arbitrary rational polynomials satisfying the stated contact condition. The study also provides:

- an exact single-column defect identity, and a polynomial-test-function version
- an explicit rational contact-truncation algorithm
- a direct nonnegative-integral proof of \(M(0,1)=(3/2)\zeta(2)\)
- a rational, convergent error bound for finite M-series truncations
- a clear separation between formal coordinates and the evaluated real constants

The optional source identities involving pi and its Abel-series exchange are checked separately. They are not prerequisites for the cancellation theorem.

## Reproduction

From this directory, run:

    python certificates.py
    python build_theorem_index.py

Both programs use only the Python standard library and original code authored for this study. They do not execute repository code, access the network, install packages, invoke Lean, or substitute numerical approximations for G or zeta(2). The saved source snapshot must remain at its recorded catalog location for provenance checks.

## Limits

The arithmetic checks are finite certificates, not proofs of the infinite analytic identities. Those proofs are in `study.md`. No Lean verification has been performed.

This work does not establish Catalan irrationality, independence of G and zeta(2), or any later determinant, valuation, or nonvanishing claim. In particular, a surviving displayed zeta(2) coordinate is not by itself a proof that an evaluated number lies outside \(\mathbb Q+\mathbb QG\).

## Source

[Revision-pinned foundations.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/foundations.tex)

Source SHA-256: `3929650dfb36859d8f88281795d348043f903c41a70b0bf3598c21586a633852`.
