# Algebra as a structural toolkit

A source-backed study for returning to algebra with a durable conceptual spine.
The intended reader has undergraduate analysis and some abstract algebra. The
question guiding the notes is: **which properties of a construction let us
reconstruct its other uses, even after the formulas have been forgotten?**

This expanded edition preserves the corrected baseline at commit
`a4a28796bdd63c5cbddbfba698c95d34728bd94c` and adds four chapters on
splitting obstructions and exact reconstruction, plus two proof-level book
comparisons. Start the continuation with the
[reconstructive map](RECONSTRUCTION-MAP.md). The
[continuation review](PHASE2-REVIEW.md) records checks, corrections, and limits;
the earlier six corrections remain documented in
[the baseline review](LOCAL-REVIEW.md).

Start with the [return guide](READING-GUIDE.md), then the
[architecture and prerequisite map](notes/00-architecture.md). The
[125-page PDF](algebra-structural-toolkit.pdf) and its
[generated LaTeX source](algebra-structural-toolkit.tex) collect the study,
comparison, reading guide, and verification record in reading order.

## The mathematical core

1. [Quotients, duality, direct sums, and splitting](notes/01-quotients-duality-splitting.md).
2. [An operator as a module; canonical forms and polynomial projections](notes/02-operators-as-modules.md).
3. [Hom and tensor products](notes/03-hom-and-tensor.md).
4. [Free algebras, exterior powers, determinants, and minors](notes/04-multilinear-and-determinants.md).
5. [Forms, adjoints, metric geometry, and the right equivalence relation](notes/05-forms-and-adjoints.md).
6. [Exact sequences, extensions, and a calibrated introduction to homology](notes/06-exactness-and-homology.md).
7. [Representations and semisimplicity](notes/07-representations.md).
8. [Bridges to arithmetic, geometry, and differential topology](notes/08-bridges.md).
9. [The concrete Hadamard/Williamson foundation bridge](notes/09-hadamard-williamson-bridge.md).
10. [Invariant complements, Sylvester equations, and extensions](notes/10-sylvester-extensions.md).
11. [Spectral projection, separability, and averaging](notes/11-averaging-separability.md).
12. [Integral spectral gluing and the affine-lattice sign certificate](notes/12-integral-spectral-gluing.md).
13. [Compression and an exact common-lift obstruction](notes/13-compression-and-common-lifts.md).

[Book comparison](COMPARISON.md) separates theorem, proof, construction, and
pedagogical coverage. [Source ledger](SOURCES.md) gives edition information,
printed/PDF page conventions, and the actual selected reading evidence.
The expanded comparisons inspect
[operator and multilinear proofs](PROOF-COMPARISON-OPERATORS.md) and
[arithmetic and representation proofs](PROOF-COMPARISON-ARITHMETIC.md),
with precise boundaries on what can be shortened.
[Verification](VERIFICATION.md) separates written proofs, cited theorems,
finite computational checks, source corrections, and unresolved comparisons.
[Progress](PROGRESS.md) records scope and remaining work honestly.

This is ordinary mathematical exposition with exact computational spot checks,
not a formally verified theorem library or a complete audit of eleven books.
The notes contain original synthesis and short references, not copies of the
source books. Source PDFs and rendered source pages stay outside the repository.

The confirmed research destination is the existing Hadamard/Williamson study.
The Hadamard chapters develop the relevant foundation and explain its prior
obstacles; it does not restart the search or claim a universal construction.

## Rebuild

From this directory, run `python3 scripts/check_examples.py` and
`python3 scripts/check_phase2.py`, then
`bash scripts/build.sh`, then `python3 scripts/audit_deliverable.py`.
The PDF build needs Pandoc, XeLaTeX, Graphviz, and the fonts named
in `scripts/header.tex`; the exact checks need Python and SymPy. Saved logs in
`evidence/` state what was actually run.
