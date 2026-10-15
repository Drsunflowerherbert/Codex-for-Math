# Hadamard study: checked finite constructions and the limits of a small search

**Research checkpoint: 2026-10-15 UTC. The general Hadamard conjecture remains
open. This study does not propose a proof of it.**

A Hadamard matrix is a square matrix of signs with
`H H^T = n I_n`. The conjecture asks for one at every order `n=4k`, for every
positive integer `k`. Orthogonality forces the order to be 1, 2, or divisible
by four; the difficult part is sufficiency.

This reusable study supplies human proofs, small complete search data, two
independently written checking implementations, and a record of where we
stopped. The work was conducted by Codex with requested `gpt-6.1-sol`, `ultra`
author/reviewer agents. Existing large matrices are attributed to their external
sources; their existence is not a discovery or capability demonstration by this
study.

## What was achieved

- Reproved the necessary order condition, tensor closure/Sylvester doubling,
  the prime Paley construction, and the symmetric circulant Williamson array.
  See [PROOFS.md](PROOFS.md), including every sign convention and the proof of
  completeness of the bounded enumeration.
- Constructed and exactly verified all **24 Paley matrices** for primes
  `p <= 199`, `p = 3 mod 4`, of orders `p+1`; **147,240** distinct row pairs.
  An independent Euler-criterion implementation reproduced their hashes and
  checked their row dot products.
- Completely enumerated normalized symmetric Williamson quadruples at every
  odd core order `m <= 15`. An independent direct search over every four-element
  multiset reproduced the counts below. This is complete within the stated
  family and bounds.
- Independently verified public matrices of orders **668 and 2060** as data.
  The 668 sign fixture also matches every entry of the CSV linked by David
  Speyer. These finite checks correct two stale status claims encountered in
  the audit.

These are replications and bounded observations. No new construction theorem,
inequivalence classification, global nonexistence result, or Lean proof is
claimed. Every tested small order already had known constructions.

## Status audit: both 668 and 2060 have finite witnesses

[Epoch's solution update](https://epoch.ai/frontiermath/open-problems/hadamard)
reports order 668 solved through human/Claude-assisted work and constructions
for the previously missing admissible orders through 2000. Its older background
paragraph still describes 668 as unknown. The public attribution names Levent
Alpöge, Philippe Voinov, Saul Reynolds-Haertle, and Claude, with discovery details
not settled by this audit. Our check establishes the supplied matrix identity,
not who contributed which mathematical idea.

The August `nreff/hadamard-search` note's next-gap claim of 2060 is also stale.
[Loïc Schneider's published construction](https://github.com/schneiderlo/hadamard-2060/tree/ad794186b6788328a2de6e6f6d68f7c493464735)
provides explicit data, and
[pinned Sage source](https://github.com/sagemath/sage/blob/0835358cba62dc19fccdff54f32e52fded9f22b0/src/sage/combinat/matrices/hadamard_matrix.py#L1207)
supports the construction. We verified that supplied matrix independently.
We do **not** certify a new smallest unresolved order. Nor did we independently
verify the full reported collection through 2000. The dated evidence, primary
sources, access limitations, attribution, and licenses are in [SOURCES.md](SOURCES.md).

| Supplied matrix | Entries checked | Distinct row pairs checked | Result |
| --- | ---: | ---: | --- |
| 668, nreff sign fixture | 446,224 | 222,778 | Every dot product zero; all row norms 668 |
| 668, Motwani CSV | 446,224 | 222,778 | Same matrix entry for entry |
| 2060, Schneider literal data | 4,243,600 | 2,120,770 | Every dot product zero; all row norms 2060 |

The primary verifier uses exact integer XOR/Hamming distance. The independent
668 verifier uses direct integer multiplication and summation. The independent
2060 verifier uses positive-support intersections. No floating point tolerance
or sampled pair checking is used. See [PROVENANCE.md](PROVENANCE.md) for exact
file hashes and safe fetch/replay commands. Downloaded Python files were parsed
using a strict numeric-data grammar; none were executed or imported.

## The restricted research question

For `m=2h+1`, choose four sign sequences satisfying `x[j]=x[-j mod m]`.
Each defines a symmetric circulant matrix. The Williamson array is Hadamard
exactly when the four periodic autocorrelations sum to zero at every nonzero
shift. Normalize each sequence to `x[0]=+1` and sort their four sequence indices.
This leaves `2^h` possible individual sequences and removes independent sign
choices and block order from the enumeration.

We asked: **which normalized four-sequence multisets work for odd `m <= 15`,
and which feasible absolute row-sum patterns occur?**

| Core `m` | Matrix order `4m` | Individual sequences | Solving normalized multisets | Realized absolute row-sum patterns |
| ---: | ---: | ---: | ---: | --- |
| 1 | 4 | 1 | 1 | (1,1,1,1) |
| 3 | 12 | 2 | 1 | (1,1,1,3) |
| 5 | 20 | 4 | 1 | (1,1,3,3) |
| 7 | 28 | 8 | 4 | (1,1,1,5); (1,3,3,3) |
| 9 | 36 | 16 | 7 | (1,1,3,5); (3,3,3,3) |
| 11 | 44 | 32 | 5 | (1,3,3,5) |
| 13 | 52 | 64 | 15 | (1,1,1,7); (1,1,5,5); (3,3,3,5) |
| 15 | 60 | 128 | 14 | (1,1,3,7); (1,3,5,5) |

These counts are **not equivalence-class counts**. Index multipliers, shifts,
and further matrix equivalences are not quotiented. Repeated blocks are allowed.
The exact candidate indices, one verified witness per row-sum pattern, and
verification records are in
[the generated JSON](data/williamson-odd-through-15.json).
All 13 stored witness arrays were also independently reconstructed and checked.

The necessary row-sum equation is `r_a^2+r_b^2+r_c^2+r_d^2=4m`.
Every feasible absolute pattern occurred within these bounds. This does not
make the row-sum equation sufficient for a given tuple: the explicit `m=5`
counterexample in [PROOFS.md, Section 6](PROOFS.md#6-row-sum-identity-and-its-limits)
passes the row-sum equation and fails the shift-one correlation condition.

At `m=15`, a direct enumeration has `C(131,4)=11,716,640` candidate multisets.
The primary search groups the `8,256` unordered sequence pairs by their exact
correlation-sum vectors and matches complementary vectors. The independent
reviewer instead checks the four-element multisets directly. Agreement between
the two approaches provides a check of the optimized search's completeness.

## Why we stopped

The small search revealed no missing row-sum pattern. Extending it by a few more
orders would not address the general conjecture. At `m=167`, even normalized
symmetric sequences number `2^83`, before pair matching. We did not attempt to
enumerate them, launch a heuristic campaign, or extrapolate small-order success
to a theorem. Published nonexistence results within the Williamson family at
some larger core orders also show that this particular family cannot settle
all Hadamard orders by itself; those results are cited, not re-proved here.
For a concrete example, the cited exhaustive literature reports no Williamson
quadruple at `m=35`, whereas our Paley instance `p=139` directly constructs and
checks a Hadamard matrix of order 140. A failure in that restricted family would
therefore be compatible with a valid Hadamard matrix at the same order.

The conceptual difficulty is finding constructions or structural arguments that
cover every admissible order. Exact verification makes a proposed matrix easy
to trust; it does not supply its seed or explain universal existence. The large
external witnesses establish finite identities, with their discovery methods
outside this study. [LESSONS.md](LESSONS.md) records the useful takeaways,
nonclaims, and worthwhile next questions.

## Reproduce and inspect

Python **3.12.14** was used, with only the standard library and no installation.
From the repository root:

```bash
python -m unittest discover -s hadamard-study/tests -v
python hadamard-study/scripts/run_experiments.py
python hadamard-study/reviews/independent_williamson_check.py --output /tmp/williamson-independent.json
```

The first command runs nine tests, including malformed/corrupted matrices,
literal-only data parsing, direct Gram checks, and a tiny full-search cross-check.
The second regenerates our Paley evidence and Williamson data deterministically.
The third independently repeats the complete small-family enumeration.
[PROVENANCE.md](PROVENANCE.md) covers downloading external data and replaying
both finite-matrix checks. A fetch can fail if its host changes access; the
hash pins which bytes were actually verified.

Evidence and independent reviews are in [evidence/](evidence/) and
[reviews/](reviews/). [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md) records choices,
failed shortcuts, bounds, and stopping decisions. Publication adds only
`hadamard-study/`, based on integrated commit
`e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f`; other research branches are preserved.
