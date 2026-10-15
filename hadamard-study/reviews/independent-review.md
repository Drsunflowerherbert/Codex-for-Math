# Independent review of the bounded Hadamard checkpoint

Reviewed **2026-10-15 UTC** by a separate reviewer agent. **Disposition: accept
the stated finite checkpoint. No mathematical or computational blocker remains.**
This review does not approve a solution of the general Hadamard conjecture,
mathematical novelty, a classification up to equivalence, or a certified current
smallest unresolved order. None of these is claimed by the reviewed documents.

The reviewed scope comprises `README.md`, `PROOFS.md`, `SOURCES.md`,
`PROVENANCE.md`, `LESSONS.md`, `EXPERIMENT_LOG.md`, the three study scripts,
the nine-test suite, and the generated finite data and verification records.
The final reviewed file identities are recorded in
[reviewed-file-sha256.json](reviewed-file-sha256.json). Subsequent publication
metadata is outside this mathematical review.

## Independent finite checks

| Check | Independent method | Result |
| --- | --- | --- |
| Order 668 | Explicit Python integer multiplication and summation for every row pair; no study-code import | All 446,224 entries are signs; 668 norms and 222,778 distinct row pairs pass |
| Second order-668 encoding | ASCII comma splitting with literal-token validation, then canonical sign serialization | Motwani CSV and nreff sign file are exactly the same ordered matrix |
| Order 2060 | Strict numeric-row parsing; positive-support intersection formula for every row pair | All 4,243,600 entries are signs; all 2,120,770 distinct row pairs pass |
| Prime Paley examples | Independently construct characters using Euler's criterion; explicit integer dots | All 24 primes through 199, 147,240 row pairs, and every canonical matrix digest agree |
| Williamson enumeration | Directly visit every four-element multiset; test every nonzero correlation lag | Exact solution tuple sets agree at every odd core order through 15 |
| Stored Williamson witnesses | Independently reconstruct each block array and compute integer row dots | All 13 witnesses pass; their indices and row-sum labels also agree |

The order-668 sign file has 446,892 bytes and SHA-256
`bdeb5059d77e2703211082627b60441b8c888c928a55cc6f295e011941a387b0`.
The CSV has 1,115,894 bytes and SHA-256
`5eaef5f4c814469a1f0815756876b83e8c4944ff7ccf4f023ee479de5e8f9a8b`.
Independent serialization of the CSV gives exactly the former sign bytes.

The order-2060 literal-data file has 14,882,482 bytes and SHA-256
`8c81090db76e2b503561ba82598b514e0c2e39940a3703783c5b1b2c6b80a37a`.
Its canonical sign digest is
`c7a145d86210740dd3f8ea21ca896a54d6916007a042638f17c8c47f097200f7`,
matching the primary verifier. The independent calculation uses
`n - 2|P_i| - 2|P_j| + 4|P_i intersection P_j|`, where `P_i` is the set of
positive positions in row `i`. It uses AND/intersection counts rather than the
primary verifier's XOR/Hamming-distance calculation. Row norms follow from the
validated sign entries. The downloaded assignment file was never executed,
imported, or passed to an expression evaluator.

Both independent matrix checkers reject a single-sign corruption in their
negative controls. Their parser checks also reject malformed or nonliteral
input. The primary nine-test suite passed on reviewer replay after the
literal-data parser was added.

Evidence: [668](order-668-independent.json),
[2060](order-2060-independent.json),
[encoding comparison](source-data-comparison-independent.json),
[Paley](paley-independent.json), and
[stored witnesses](williamson-witnesses-independent.json).

## Search completeness and count interpretation

The independent search imports no study code and does not use complementary
pair buckets. It directly tested **12,539,727** candidate four-multisets across
the eight core orders, including 11,716,640 at `m=15`. It tested full nonzero-lag
correlations, rather than relying on the primary search's half-lag reduction.

| Core order | Normalized sequences | Candidate four-multisets | Solving multisets |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 1 |
| 3 | 2 | 5 | 1 |
| 5 | 4 | 35 | 1 |
| 7 | 8 | 330 | 4 |
| 9 | 16 | 3,876 | 7 |
| 11 | 32 | 52,360 | 5 |
| 13 | 64 | 766,480 | 15 |
| 15 | 128 | 11,716,640 | 14 |

The complete sets of 48 solving tuples, converted to the documented
little-endian sequence-index convention, agree exactly with the primary
enumerator. This is stronger than agreement of counts alone. The independently
computed feasible, realized, and unrealized absolute row-sum type sets also
agree. No feasible absolute row-sum type is absent within these bounds.

The completeness argument in `PROOFS.md` is valid: sign normalization preserves
every correlation; the `2^((m-1)/2)` independent sign choices are enumerated
bijectively; and each sorted tuple has one first pair, one last pair, and one
complementary bucket match. Repeated indices, zero keys, and `m=1` are covered.
These counts identify normalized sequence multisets. They do not quotient
shifts, index multipliers, Williamson equivalence, or general Hadamard
equivalence, and must not be compared directly with published equivalence-class
counts. No inference to a larger core order follows from the completed table.

Evidence: [direct enumeration](williamson-independent.json) and
[complete solution-set comparison](williamson-solution-set-comparison.json).

## Proof review

The necessary order argument and Kronecker-product proof are correct. The Paley
proof establishes the required character facts and character-sum identity and
uses the implemented signs `Q[i,j]=chi(j-i)`, `C=Q+I`, with a negative first
column below the corner. Those signs correctly cancel the border products.
The claim is expressly restricted to primes congruent to 3 modulo 4.

For the Williamson proof, the circulant convention, symmetry, commutation,
Gram-to-correlation identity, and all six displayed off-diagonal block
products check out. The row-sum equation is a valid necessary condition.
The possible normalized absolute row sums are precisely the positive odd
integers through `m`. The `m=5` counterexample has the stated row sums and
shift-one correlation, so it correctly refutes sufficiency for an individual
tuple even though every feasible type is realized in the finite table.

These are human proofs of classical results. No formal proof assistant was
run, and no Lean result is asserted.

## Status, provenance, and remaining limits

The final prose correctly replaces stale unknown-order language for both 668
and 2060 with checked finite witnesses. It separates the source report about
all missing orders through 2000 from the two large cases actually checked here.
It does not infer a new smallest unresolved order or transfer construction
credit to this study. This review checked local witness data and the internal
consistency of the source ledger; it did not independently re-browse every
historical source or settle the discovery attribution.

The pinned revisions and byte hashes in `PROVENANCE.md` agree with the checked
local inputs. The lack of an immutable Drive revision is disclosed. Keeping
the external 668 artifacts outside the repository is consistent with the
recorded absence of an explicit redistribution license. The order-2060 MIT
source is attributed, and no third-party implementation is incorporated.
Replay requires the external hosts to remain accessible. This is a documented
retrieval limitation, not a failure of a completed arithmetic check.

All reviewed Python imports are standard-library modules or local modules
authored for this study. No third-party solver, downloaded implementation, or
software installation is needed. The large files remained inert input data.

## Reviewer replay

After the fetch and hash checks in [PROVENANCE.md](../PROVENANCE.md), run from
the repository root:

```bash
python -m unittest discover -s hadamard-study/tests -v
python hadamard-study/reviews/independent_check.py /tmp/hadamard-668.txt \
  --expected-order 668 --output /tmp/review-order-668.json
python hadamard-study/reviews/independent_2060_check.py /tmp/hadamard-2060-data.py \
  --expected-sha256 8c81090db76e2b503561ba82598b514e0c2e39940a3703783c5b1b2c6b80a37a \
  --output /tmp/review-order-2060.json
python hadamard-study/reviews/independent_williamson_check.py \
  --output /tmp/review-williamson.json
python hadamard-study/reviews/supplemental_review.py \
  --matrix-signs /tmp/hadamard-668.txt \
  --matrix-csv /tmp/hadamard-668-primary.csv \
  --independent-williamson /tmp/review-williamson.json \
  --output-dir /tmp/review-supplemental
```

The supplemental replay produced byte-identical copies of all four recorded
supplemental JSON results. Runtime and input-path metadata in timed checks may
vary on replay; the matrices, hashes, counts, and tuple sets must agree.
