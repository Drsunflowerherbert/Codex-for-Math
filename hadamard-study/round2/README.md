# Round 2: exact criteria that reduce Williamson search

**Checked checkpoint, 2026-10-15 UTC.** The new criteria preserve every solution
in the declared odd symmetric circulant Williamson family. They give a real
resource saving at core order 21, with **21.00 times fewer stored pairs**, a
**6.46 times lower median external process wall time**, and **10.08 times lower
observed worker peak RSS**, compared with unfiltered full-profile matching.
All 34 solutions are preserved. These are bounded replication results using
classical constraints; the general Hadamard conjecture remains open.

The first edition and its complete small baseline remain unchanged. Its
[published revision](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/b947c2f9c6ee0da0728c93d9ba74b66345d73d60/hadamard-study)
is preserved. This edition's updated conclusions are in [LESSONS.md](LESSONS.md).

## Family, normalization, and what counts

At odd core order `m=2h+1`, candidates are complete sign sequences with
`x[0]=+1` and `x[j]=x[m-j]`. A mask `a` in `0,...,2^h-1` specifies its negative
independent coordinates, exactly as in the first edition. We search sorted
four-multisets `a<=b<=c<=d`, allowing repetitions. **Filtered list ranks never
replace original masks.** No additional symmetry quotient is applied.

The acceptance condition is exact cancellation of all nonzero-lag periodic
autocorrelations. By the original [Williamson array proof](../PROOFS.md), this
is sufficient to construct a Hadamard matrix of order `4m`. It also supplies
a complete test within this family. Failure in this family says nothing about
global Hadamard nonexistence.

The small validation domain is every odd core order from 1 through 15. The
moderate complete demonstrations are **19 and 21**. We did not search 17 or 23
in this round, even though the executable accepts odd inputs through 23.

## Three proof-backed criteria

The self-contained proofs, including completeness of both implemented search
methods, are in [PROOFS.md](PROOFS.md). [SOURCES.md](SOURCES.md) records the
primary literature and attribution. No result below is claimed as a new theorem.

1. **Attainable remaining row squares.** Let
   `W={t²: t odd, 1<=t<=m}`. A single candidate with row sum `r` must have
   `4m-r²` in `W+W+W`; a pair must have `4m-r_a²-r_b²` in `W+W`.
   Sums allow repetition. Normalization permits negative signed row sums;
   imposing nonnegative row sums as well would lose solutions.

2. **Williamson's odd-order product theorem.** At every nonzero coordinate,
   the four signs multiply to −1. Thus original masks obey
   `a xor b xor c xor d = M`, where `M=2^h-1`, and the fourth mask is forced:
   `d=M xor a xor b xor c`. The proof uses the defining cyclic-ring identity
   modulo two after dividing its integer coefficients by four. This removes
   the fourth free choice from direct quadruple enumeration, but does not
   automatically improve an existing meet-in-the-middle algorithm.

3. **Exact positive-semidefinite energy bounds.** For complete sequences
   selected from a possible quadruple and any integer vector `v`,

   ```text
   sum_x ||C_x^T v||² <= 4m ||v||².
   ```

   Every omitted complete sequence contributes a nonnegative squared norm.
   One strict violation is therefore a sound rejection. We evaluate a fixed
   bank of centered integer triangular vectors, with all arithmetic in Python
   integers. For `3|m`, a cheap exact order-three frequency test uses residue
   sums: symmetry gives `c1=c2`, so the energy is `(c0-c1)²` and single/pair
   energies must sum to at most `4m`. Equality survives.

The triangular bank is a finite set of PSD probes, **not a complete Fourier PSD
oracle**. It contains the order-three test when applicable; putting that cheap
test first changes work performed, not the final pruning strength of the whole
bank. No floating point PSD comparison is used. No unknown signs are replaced
by zero. Compression is used only to compute a necessary energy of a complete
sequence; we do not equate compressed feasibility with the existence of a lift.

## Staged reduction at core order 21

The final filtered configuration uses the same original-mask domain as the
unfiltered algorithm. Its exact counts are:

| Stage | Candidates remaining |
| --- | ---: |
| All normalized symmetric single sequences | 1,024 |
| After single row-square feasibility | 912 |
| After single order-three energy | 875 |
| After single integer probes | 560 |
| Unordered pairs from those 560 sequences, repetition allowed | 157,080 |
| After pair row-square feasibility | 112,602 |
| After pair order-three energy | 103,649 |
| After pair integer probes / pairs stored | 24,985 |
| Exact full-profile complementary pair combinations before sorted-order test | 192 |
| Solving normalized four-multisets | 34 |

The unfiltered method stores **524,800** pairs and has the same 192 exact
complementary combinations and 34 outputs. The gain comes from discarding
uncompletable singles and pairs **before storage and matching**. It does not
shrink the already exact final solution set.

Separate full configurations, each retaining all 34 solutions, give an ablation:

| Configuration at 21 | Singles retained | Pairs stored | Median preprocessing + search (s) | Median external wall (s) | Observed worker peak RSS (KiB) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Unfiltered full-profile MITM | 1,024 | 524,800 | 1.5016 | 1.5319 | 220,376 |
| Row squares only | 912 | 314,853 | 1.0435 | 1.0754 | 143,016 |
| Row squares + order-three energy | 875 | 274,295 | 0.8718 | 0.9014 | 126,988 |
| Row squares + order-three + integer probes | 560 | 24,985 | 0.2042 | 0.2370 | 21,868 |
| Same filters + product bitmask in full-profile key | 560 | 24,985 | 0.1933 | 0.2214 | 22,548 |
| Same filters + product-forced triples | 560 | 0 | 5.7877 | 5.8168 | 13,696 |

The full filtered method is 7.35 times faster on the in-process total; the
6.46 factor uses the separately measured external wall time, including process
startup and output. The RSS ratio is 10.08, an absolute worker high-water mark
through the search, not an incremental allocation measurement. Preprocessing
costs are charged: median 0.02769 s with all filters versus 0.01553 s unfiltered.
The phase medians in the JSON need not sum to its total median, because each
median is computed separately.

## What helped less, or failed as a shortcut

- **The product bitmask adds no exact full-profile matches to reject.** Full
  correlation cancellation already implies the product theorem. Both keys
  have 192 pre-order matches at 21. The small observed timing difference has
  overlapping three-run ranges and is not an additional mathematical pruning
  gain; its larger key increases observed memory here.
- **Forcing the fourth sequence trades memory for time.** It stores no pair
  table, but visits 29,426,320 retained triples at 21. Of these 4,058,702 have an
  ordered eligible fourth mask; 498,704 pass the complete row-square sum;
  24,904 pass the selected pair bounds and receive a full PAF test; 34 work.
  It is 28.34 times slower than filtered pair matching on the in-process total.
  This is not a claimed speedup over the first edition.
- **The order-three test is unavailable at prime core 19.** Row-only and
  row-plus-order-three configurations then have identical counts. The general
  integer probes still reduce stored pairs from 131,328 to 6,798; all 42 solutions
  survive. Median external wall drops from 0.3397 s to 0.0775 s.
- **Some tiny cases gain no PSD pruning.** At 3 both single PSD stages retain
  both candidates and reject no pair surviving the row filter. Their setup
  adds overhead; process startup dominates the roughly 0.03 s wall times. Small
  fluctuations are not evidence of a speedup.
- **Even a full residual PSD condition is not sufficient for completion.** At 7
  the three masks `(1,2,4)` leave residual `8I-J`, which is positive definite.
  Yet the product theorem forces the wrong fourth row square. [The proof](PROOFS.md#5-why-safe-spectral-filters-remain-necessary-conditions)
  gives the exact calculation. Final autocorrelation checks remain essential.

No comparison divides an equivalence-class count by a raw candidate count.
There are 46,081,900,800 raw four-multisets at 21, but we did **not** brute-force
them or claim a timing speedup against that unrun algorithm. The reference is
the already efficient unfiltered full-profile pair method.

## Validation and reproducibility

Independent adversarial review checked the exact solution sets, rather than
only their cardinalities:

- All 48 original solutions at odd cores 1,...,15 survive every criterion and
  every implemented method, matching a direct exhaustive unpruned baseline.
- An independently authored unfiltered full-lag MITM, using support-overlap
  autocorrelations and byte keys, confirms 42 solutions at 19 and 34 at 21.
- All 124 tuples across these ten orders are retained in
  [validated-solutions.json](data/validated-solutions.json), with staged counts
  and sample exact rejection certificates. All 124 resulting Hadamard arrays
  pass exact checking, comprising 293,808 distinct row-pair checks.
- Nine new tests and the original nine tests pass. Adversarial checks include
  repeated blocks, empty masks at 1, negative row sums, original masks versus
  filtered ranks, and PSD equality at 9. Changing `>` to `>=` would reject a
  known valid tuple whose order-three energy is exactly 36.

The [independent review](reviews/independent-review.md),
[criterion evidence](reviews/reductions-independent.json),
[moderate baseline](reviews/moderate-independent.json), and
[benchmark audit](reviews/benchmark-audit.json) are separate from the primary code.

The formal protocol uses Python 3.12.14 on Linux, three sequential fresh worker
processes per case, with a deterministic rotation of method order. Four cores
`3,15,19,21` times six configurations times three repetitions give 72 raw runs.
Before/after hashes bind the measured worker, benchmark driver, and imported
first-edition sources. No concurrent timed workers or reviewer computations
were run. The in-process total charges all mathematical preprocessing; external
wall also charges imports, interpreter startup, and result serialization. RSS is
sampled after search and includes the interpreter and preprocessing/search
allocations, but excludes any later serialization peak. [benchmark.json](evidence/benchmark.json)
records the CPU, platform, all raw runs, phase timings, minima/medians/maxima,
and original-mask solution-set hashes. There are no performance guarantees for
other machines, lengths, or implementations.

The baseline shares candidate, PAF, row-square, and small square-set preparation
with the filtered methods. Its main pair loop has no filter calls or per-pair
stage-counter overhead. The comparison is between these measured implementations,
not a claim about the fastest possible implementation of either method.

From the repository root, with the standard library only:

```bash
python -m unittest discover -s hadamard-study/tests -v
python -m unittest discover -s hadamard-study/round2/tests -v
python hadamard-study/round2/scripts/benchmark.py --cores 3 15 19 21 --repeats 3 \
  --output hadamard-study/round2/evidence/benchmark.json
python hadamard-study/round2/scripts/validate.py
```

Run the benchmark without other heavy work. Replays replace local measurement
files and naturally differ in timing/RSS; exact tuple hashes and counts must
agree. [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md) records the sequence and stopping
decision. The independent scripts have replay commands in their review.

## What barrier moved

We substantially reduced pair storage and measured computation for a complete
moderate case. We did **not** remove the need to generate all `2^h` individual
sequences. At 167 that is still `2^83` candidates before filtering; no complete
search was attempted there. Product-forced triples do not improve the pair
method's asymptotic generation bound and were slower in this demonstration.
Further progress would need a proved method for pruning partial assignments,
an audited compression/lifting search, or a new construction idea. We stop at
this checked reduction rather than turn it into an unsupported large search.
