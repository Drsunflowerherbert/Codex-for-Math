# Mathematics research data

The [reviewed supplement](supplement/README.md) contains seven supporting-lemma
studies and 81 core theorem/identity records. These are ordinary mathematical
proofs, separate reviews, and reproducible finite computations. They have not
been compiled or kernel checked in Lean. No novelty, external peer review,
native MRS admission, or whole-manuscript verification is asserted.

| Current study | Records | Final entry point |
| --- | ---: | --- |
| Affine avoidance | 5 | [Reviewed notes](supplement/reviews/affine/research-notes.reviewed.txt) |
| Egyptian fractions | 6 | [Corrected study](supplement/reviews/egyptian/corrected/study.md) |
| Transport stability | 10 | [Proof](supplement/transport-stability/proof.md) |
| Positive blocks | 10 | [Study](supplement/positive-blocks/study.md) |
| Mixed moments | 21 | [Study](supplement/mixed-moments/study.md) |
| Convex approximation | 19 | [Study](supplement/convex-approximation/study.md) |
| Finite-field mixing | 10 | [Study](supplement/finite-field-mixing/study.md) |

The [starter](starter/README.txt) preserves the earlier corpus inventory,
conditional pi/tangent proofs, ordinary radial study, and initial inputs.
Its affine and Egyptian copies are historical; use the corrected entry points
above. Optional ordinary Egyptian coarse/iterated bounds remain separately
unreviewed and unformalized. The separate Lean Egyptian library proves its own
one-step bound under its own explicit contract.

The corpus inventory is a snapshot attributed to OpenAI/math revision
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`: 719 active manuscripts, 372 families,
three withdrawn manuscripts, and 27 version-directory changes. These counts
are different units; upstream formalization claims are not certified here.

Run the public snapshot integrity check from the repository root:

```sh
python3 publication/verify.py
```

To reproduce the ordinary studies' computations in a temporary copy:

```sh
cd research/supplement
python3 reproduce_checks.py --full --output /tmp/research-reproduction.json
```

The checker exercises finite arithmetic and numerical illustrations. It does
not establish universal mathematical truths or perform Lean verification.
Publication changes and original/public hashes are in
[publication](../publication/README.md). Third-party source coverage and change
notices are in [THIRD-PARTY.md](../THIRD-PARTY.md).
