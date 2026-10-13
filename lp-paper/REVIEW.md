# Paper review and rendering evidence

Date: 13 October 2026 UTC.

## Reviewed artifacts

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `sparse-lp-certificates.tex` | 47,384 | `aba7614746e49fd27a777427897b0e3cb6a4d0365fbe4e554ee06ea76ea72b5c` |
| `sparse-lp-certificates.pdf` | 322,200 | `7ca7e666e0aae2780c39f9af609d330eae77ca2a39ab7df10ec3c70897442e72` |

The PDF has 14 US Letter pages. These checks bind this source and this PDF;
they do not grant new Lean acceptance or formal algorithm verification.

## Draft transfer and bounded finalization

Both transferred source checkpoints were verified against their supplied
byte counts and SHA-256 values after decoding the transport's HTML entities:

- Initial checkpoint: 46,640 bytes,
  `2e70e5d9b68ea2a21ba314af4dbb64d914f19598976871927b5edc61571767d2`.
- Final checkpoint: 46,682 bytes,
  `c8ffe446bc76e7cadbdddc7302e79e8c5562c21183c610b3386fc1063f61603b`.

The manuscript was finalized from the last checkpoint. Bounded clarifications
made the objective-vector domain and strict/integer exclusions explicit,
qualified the equality-row recovery count by consistency, specified the
contradiction search's deterministic ordering and empty support, described the
exact finite toy domain and assertion-enabled Python mode, and stated the
same-kernel replay and absence of a simplex runtime comparison. No research
proof, implementation, dependency pin, or existing manifest was changed.

## Independent mathematical and source review

Two independent reviews of the actual manuscript found no remaining blocker.
They checked the final source hash and bounded diff. Review covered:

- Nonnegative inequality and signed equality weights; full-coordinate
  coefficient identities, feasible attainment, contradiction signs, and ray bases.
- Consistent equality elimination, original-row multiplier recovery and cost
  identity, and the intrinsic projected rank.
- Full proofs of conic dependence reduction, finite-cone closure and separation,
  the unrestricted-variable contradiction alternative, and bound existence with
  its nonemptiness hypothesis.
- The normal-rank support bound for valid bounds, active-row restriction at a
  feasible optimizer, lifted-rank contradiction support, and sharp examples.
- Rational witnesses, independent exact solves, exhaustive finite-search
  completeness and termination under the stated assumptions, minimum positive
  support for direct cardinality-first search, and worst-case subset counts.
- Normalization, degeneracy, nonuniqueness, zero cases, vacuous bounds, and
  incomplete or prematurely stopped implementation searches.
- Worked optima 9 and 17/18, zero-normal contradiction, no-vertex optimum, and
  the augmented first-success counterexample. Nine original-coordinate identities
  were also checked independently with exact Fraction arithmetic.
- Reported fixture and finite-audit counts, selected Lean scope, parser/cache
  trust, same-kernel replay, and absence of general strong-duality or finder
  completeness claims in the formal package.

The primary references were opened and relevant page statements checked:
Border's Theorems 3–5 and Proposition 35; Bertsekas's MIT Lectures 3 and 10;
and Boyd–Vandenberghe's equality-elimination slides 4.35 and 10.4 (PDF pages
122 and 331). The Stanford PDF required direct author-site downloading after
the browser retrieval failed; no source PDF is included in this directory.

## Computational source checks

Fresh finalization QA reproduced the unchanged research experiment:
14 regression tests passed and the benchmark output matched the recorded
`results.json` byte for byte (SHA-256
`c314baf34cb68412b97727e0dbfa75806cc9de3f2b71ba6bce7cc345c619b107`).
The independent determinant-minor/Cramer oracle reproduced 44 fixture runs,
5,040 toy inputs and 10,080 searches, 13 additional zero-dimensional searches,
two first-success counterexample searches, six original-coordinate identities,
and two affine parametrizations. These are separate finite counters, not
timings, general performance evidence, or formal proofs. No Lean batch was
rerun for this paper.

## Rendering and visual QA

The final source compiled with `latexmk -pdf` and pdfTeX 1.40.26. The final
LaTeX log contained no warnings, undefined references, missing characters,
overfull boxes, or underfull boxes. All 37 labels were unique, all 30 explicit
cross-references resolved, and the PDF contained nine external bibliography
links. All 18 listed fonts were embedded, subsetted, and supplied Unicode maps.

All 14 pages were rendered to separate 140-dpi PNGs and opened individually.
The finalizing agent inspected every page, and two separate visual reviewers
independently covered pages 1–7 and 8–14 at original image resolution. All pages
passed: no clipping, overlap, missing glyphs, equation or table collisions,
broken references, or unreadable typography. Proof and algorithm continuations
across pages were readable; the evidence table and bibliography fit cleanly.
Text extraction additionally found no replacement glyphs or text blocks outside
the page rectangles. No final visual repair was required.

## Publication checks

The deliverables contain mathematical exposition and scoped evidence only.
Bibliographic attribution is retained; no third-party PDF or extended quoted
passage, private input archive, credential, dependency tree, or compiler binary
is redistributed. Existing notices and research files are preserved. Publication
adds only files under `lp-paper/` on a separate paper branch, by normal push,
with no PR, merge, force push, or credentials change.
