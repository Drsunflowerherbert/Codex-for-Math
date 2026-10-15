# Round-two experiment log

Date: 2026-10-15 UTC. Parent checkpoint:
`b947c2f9c6ee0da0728c93d9ba74b66345d73d60`. All first-edition files are preserved
byte for byte; second-round files live under `hadamard-study/round2/`.

| Decision / experiment | Scope, outcome, and limitation |
| --- | --- |
| Primary-source review | Inspected author manuscripts for odd product theorem, row-square identity, spectral bounds, and compression. Full original 1944 article unavailable; modern primary sources expressly credit it. No external code run. |
| Criteria selected | Global attainable remaining row squares; exact order-three energy where applicable; deterministic integer triangular probes; product-forced fourth mask as a separate search route. No extra symmetry restrictions or selected row-sum ansatz. |
| Proofs | Complete human proofs of each rejection, the product theorem, and coverage/uniqueness of both algorithms. A finite integer bank is explicitly weaker than a full residual PSD check. |
| Small validation | All odd cores 1,...,15 against the preserved independent unpruned baseline. All 48 tuples retained by all four methods and filter-subset ablations. Original mask labels and multiplicities audited. |
| Preliminary core 21 check | Found 34 solutions with both unfiltered and filtered MITM. Recorded exploratory `/tmp` outputs only; these are not the final benchmark evidence. |
| Independent adversarial review | Direct convolution versus profile-score identities; original-rank/XOR hazards; signed rows; repeated blocks; exact-threshold equality; unit-multiplier closure; exact PSD-no-completion counterexample. No false-negative pruning found. |
| Moderate baseline | Independent full-lag byte-key unfiltered MITM, using negative-support overlaps for PAF, found 42 solutions at 19 and 34 at 21. Exact tuple sets, not just counts, match. |
| Formal measurements | Sequential fresh Linux workers, 3 repetitions, 6 configurations at 3,15,19,21; 72 final raw runs. Measured-source hashes before/after match. All preprocessing charged; independent audit recomputed summaries and tuple hashes. |
| Benchmark audit refinement | The first timing pass led to a protocol improvement: bind worker/driver/dependency hashes before and after, and describe order as rotated rather than balanced. Re-ran the full protocol with the final measured source. Only that final run is in evidence/benchmark.json. |
| Strongest bounded reduction | At 21, raw singles 1024→row 912→order-three 875→probes 560. After those single filters, 157080 pairs→row 112602→order-three 103649→probes 24985. Unfiltered storage 524800. Both have 192 exact joins and 34 outputs. |
| Ablations | Row-only storage 314853; row+order-three 274295; all filters 24985 at 21. These configurations have different single pools, so their pair counts are not mislabeled as one common stage pipeline. |
| Ineffective criteria | At 19, order-three test is unavailable; row and row+order-three have identical counts. At 3, energy filters prune nothing beyond row arithmetic and add setup cost. |
| Product-key negative result | It retains the same 192 full-profile joins at 21, by theorem. Small runtime variation is an implementation effect, not mathematical pruning. |
| Product-triple tradeoff | At 21, visits 29426320 triples; forces 4058702 ordered eligible fourth masks; 498704 pass full row square sum; 24904 reach full PAF; 34 solve. Lower peak memory, slower than filtered MITM. |
| Output construction check | All 124 solution tuples across ten measured/validated core orders yield Hadamard arrays by the proved block construction; 293808 distinct row pairs checked exactly. |
| Stopping decision | No run at 17 or 23 this round. No large search at 167; 2^83 single candidates still appear before filters. The practical pair-memory barrier moved by a large factor, but the exponential candidate-generation barrier did not. |

## What was rejected as an argument

- Keeping only nonnegative signed row sums after fixing `x[0]=1` loses cases.
- Treating compressed feasibility as an actual lift is unjustified. We only
  apply the order-three projection to complete original candidates.
- Zero-filling unknown signs gives no safe lower energy bound because omitted
  contributions can cancel. No such prefix pruning is implemented.
- Rejecting equality in a PSD bound loses a known valid core 9 tuple.
- The product identity and row-square identity are not sufficient by themselves.
  Even full PSD feasibility for a proper partial tuple need not give a completion.
- No speedup is claimed against an unrun raw quadruple scan or against a
  differently normalized/equivalence-quotiented search.

## Reproduction boundaries

The primary code has nine new tests. All nine original tests also pass. Review
scripts and evidence are in [reviews/](reviews/); mathematical proofs are in
[PROOFS.md](PROOFS.md). Timing replay requires Linux for KiB `ru_maxrss` units.
Only exact integers determine rejections; floating values appear in elapsed-time
measurement. Runtime/path/RSS fields may vary. Original-mask solution tuple
hashes, counts, and the constructed-matrix identities must agree.
