# Experiment and decision log

Date: 2026-10-15 UTC. No claim of mathematical novelty is made.

| Step | Exact scope and result | Decision / limitation |
| --- | --- | --- |
| Repository audit | Remote integrated branch still `e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f`; no `AGENTS.md` or local skill files found. Existing baseline README and third-party notice read. | Start requested new branch; write only `hadamard-study/`. Snapshot remote heads for preservation check. |
| Current-source audit | Epoch solution update and MO verification identify 668 as finite solved case. Direct X returned HTTP 403; official oEmbed supplied announcement metadata. | Do not use stale background “smallest unknown 668”; do not claim full primary payload reconstruction. |
| Scope selection | Prime Paley proof/instances; all normalized symmetric circulant Williamson multisets at odd `m<=15`; exact public-matrix verification. | No unrestricted Hadamard search or universal proof attempt. |
| 668 public data | Pinned nreff signs and separately linked Motwani CSV fetched into `/tmp`; exact byte hashes recorded. All 222,778 row pairs zero. | Primary bit verifier and independent direct dot verifier agree. Independently parsed CSV matches sign data entry for entry. No artifact redistribution without explicit permission/license. |
| Paley | All 24 primes `p<=199`, `p=3 mod 4`; exact matrices of order `p+1`; all 147,240 row pairs checked. | Independent construction uses Euler criterion instead of enumerated square set, reproducing all canonical hashes and direct dots. |
| Williamson enumeration | All odd `m=1,3,...,15`. Sequence count `2^((m-1)/2)`, independent signs normalized at coordinate 0; block multiset sorted with repetition. Counts 1,1,1,4,7,5,15,14. | Exact complementary half-lag profile buckets; proof of completeness and no duplicate tuples. No further equivalence quotient asserted. |
| Independent search | Directly enumerates every four-multiset and tests full nonzero-lag conditions; 11716640 candidates at `m=15`. | Counts and row-sum pattern sets match. This tests a genuinely different search route. |
| Witness check | One stored witness for each of 13 absolute row-sum types across eight core orders; construct `4m` array and check exact Gram identity. | All 13 independently reconstructed and dot-checked. Not every counted tuple stored as a matrix. |
| Row-sum shortcut | All arithmetically feasible absolute patterns realized through 15. A concrete `m=5` tuple passes square sum and fails shift-one PAF. | Reject row-sum sufficiency for individual quadruples. No false claim that a feasible pattern must always have a realization at larger orders. |
| Frontier shortcut rejected | August nreff note suggests 2060 next. Later primary Schneider data and current Sage support 2060. | Audit exact matrix as data, not new search; do not infer a new smallest gap. |
| 2060 finite audit | Pinned published `H2060.py` is 14,882,482 bytes. Strict numeric-row parser, no import/execution; all 2,120,770 row pairs zero, entries all signs. | Exact evidence retained; independent verifier uses positive-support intersections. Large artifact not bundled. |
| Scaling / stopping | `m=167` has `2^83` normalized symmetric sequences. No candidate generation attempted. Published Williamson family failures at larger orders cited only. | Fundamental computational and conceptual barriers reached. Stop this line, preserve lessons. Increasing bounds would change the finite table, not supply universal coverage. |

## Failed or rejected lines, precisely

- **Stale status as a research target:** both 668 and 2060 were found labeled
  unresolved in dated/background sources. Fresh sources and exact finite
  checks supersede those labels. We did not claim to solve either order.
- **Row-sum-only validation:** rejected by the explicit core 5 counterexample.
  A nonzero-lag correlation check is essential.
- **Extrapolation from complete small success:** no missing pattern occurred in
  the eight tested core orders. That supplies no completeness beyond 15.
- **Direct scale-up to core 167:** not run. Candidate count alone makes the
  naive method unsuitable; failure to run is not a nonexistence result.
- **Universal closure argument:** Paley primes and tensor products supply
  infinite families without covering every admissible order by any argument
  given here. No universal proof was attempted past this coverage obstacle.

## Verification record

The nine unit tests cover literal-data rejection, malformed inputs, one-entry
corruption, exhaustive two-by-two verifier cross-checks, direct Paley Gram and
character sums, symmetry/normalization, full tiny Williamson searches, and
constructor input constraints. Their output is in [evidence/tests.log](evidence/tests.log).
The deterministic experiment run is in [evidence/experiments.log](evidence/experiments.log).
Separate reviewer evidence is in [reviews/](reviews/).

The study contains no Lean files, no downloaded implementation dependencies,
no external search solver, and no assertion that the whole reported <=2000
collection has been verified here. Full sources and fetch limitations are in
[SOURCES.md](SOURCES.md) and [PROVENANCE.md](PROVENANCE.md).
