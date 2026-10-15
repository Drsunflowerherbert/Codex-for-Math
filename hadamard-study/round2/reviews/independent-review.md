# Independent adversarial review: round two

**2026-10-15 UTC. Disposition: accept the stated bounded reduction results.**
No mathematical, false-negative, numerical-reporting, or reproducibility blocker
was found in the final reviewed files. This is an acceptance of classical
criteria, their implemented finite searches, and the reported measurements.
It is not a novelty claim, an equivalence classification, a full Fourier PSD
oracle, or progress to a proof of universal Hadamard existence.

The review covers the final `README.md`, `PROOFS.md`, `SOURCES.md`, `LESSONS.md`,
`EXPERIMENT_LOG.md`, four primary scripts, new tests, complete solution data,
and benchmark records. [reviewed-file-sha256.json](reviewed-file-sha256.json)
binds the files present at acceptance. Subsequent publication/package metadata
is outside this review. No primary implementation file was edited by this
reviewer, and no commit was made.

## Proof and implementation audit

The cyclic-ring product proof is correct, including division by four over
integer coefficients before reduction modulo two. The XOR is taken over the
original sequence masks, with target `M=(1<<h)-1`; filtered-list ranks are never
substituted. Both the complementary product key and the product-forced fourth
mask have the stated coverage and uniqueness arguments.

An independent proof of the same product constraint uses scalar correlations.
Write `x_j=1-2e_j`, let `w_x=sum e_j`, and let
`N_x(s)=sum_j e_j e_(j+s)`. For nonzero `s`,
`PAF_x(s)=m-4w_x+4N_x(s)`. The involution `j -> -j-s` pairs the terms of
`N_x(s)` except the unique fixed point `j=-s/2`, so
`N_x(s)=e_(s/2) mod 2`. Williamson cancellation gives
`sum_x N_x(s)=sum_x w_x-m`, which is odd because every normalized symmetric
negative support has even size. Thus an odd number of the four signs is
negative at every nonzero coordinate. Oddness, symmetry, and normalization
are essential to this derivation.

The row-square sets are exact global necessary conditions, allow repetitions,
and safely truncate sums above `4m`. They do not require positive signed row
sums, an additional row-magnitude ordering, or a selected row-sum pattern.
The implementation retains the original mask ordering and uses inclusive
repetition throughout.

The energy inequality follows by removing nonnegative whole-sequence squared
norms from the Williamson identity. The profile evaluation equals direct
matrix-vector energy. The triangular vectors are fixed integer vectors;
there is no floating-point acceptance/rejection decision. All comparisons
correctly reject only strict violations. The order-three residue formula has
the right target `4m`, not the compressed length's target.

The report's claim that the triangular bank already contains the order-three
test also checks out. At `f=m/3`, its centered vector is
`(4m²/9)*(2,-1,-1,...)`, so its inequality is exactly the same scalar bound.
Putting the residue calculation first saves work and does not add final
strength to the full bank.

The explicit core-7 partial tuple `(1,2,4)` has Gram sum `20I+J`, hence residual
`8I-J` with positive eigenvalues 1 and 8. Its forced fourth mask is zero,
whose row square is 49, while the required remainder is 1. This correctly
shows that even full residual PSD feasibility for a proper partial tuple need
not imply completion. The proofs correctly distinguish this from exactly four
complete sequences, where a full PSD residual would have trace zero.

Both searches finish with the full correlation condition. Filtering therefore
preserves completeness without turning the necessary conditions into an
unproved acceptance rule. No unknown-entry zero filling or additional symmetry
ansatz is implemented.

## Independent finite checks and adversarial controls

[independent_reductions.py](independent_reductions.py) independently decodes all
small candidates and computes full-lag correlations and direct convolution
energies. It verifies:

- Exact tuple-set equality with all **48** first-edition solutions at every odd
  core order through 15 for all four methods and all three filter ablations.
- All **1,538** candidate/probe energy identities against explicit matrix-vector
  multiplication, and every actual two-position subset of each true tuple
  against the pair filters.
- **415** unit-index-multiplier closure checks on the complete small solution
  sets. No quotient by these transformations is used in any reported count.
- `m=1`, empty profiles/probe banks, repeated blocks, negative normalized row
  sums, and zero energies.

The valid core-9 tuple `(7,11,13,14)` has order-three energies `(0,36,0,0)`.
Mask 11 also reaches equality in the frequency-label-3 integer probe. Both the
single and pair threshold equalities survive. A `>=` rejection would lose this
solution. Explicit negative controls also show how a zero XOR target, filtered
rank XOR, square sums without repetition, positive signed rows only, or imposing
row-magnitude order as well as mask order would reject valid small cases.

[independent_moderate.py](independent_moderate.py) completes both moderate
unfiltered searches before importing the subject implementation. It uses
negative-support cyclic overlaps to compute PAFs, full nonzero-lag byte keys,
and every original unordered pair with repetition. It confirms exact solution
sets of **42 at core 19** and **34 at core 21**. Both filtered MITM variants
match these sets and their pre-order join counts. The independent run's elapsed
time is explicitly not a comparative benchmark.

[audit_certificates.py](audit_certificates.py) reconstructs every retained
Williamson array without importing the study modules and checks explicit
integer row dots: **124 arrays, 293,808 distinct row pairs**. It also independently
reconstructs all **33 recorded rejection examples**, using direct convolution,
residue sums, and arithmetic membership. These are checked sample certificates;
the soundness proof and complete-baseline comparisons support the full filters.

The original nine tests and the new nine tests passed on reviewer replay.
Evidence: [criteria](reductions-independent.json),
[moderate baseline](moderate-independent.json), and
[certificates and matrices](certificates-audit.json).

## Benchmark and report audit

[audit_benchmark.py](audit_benchmark.py) checked all **72 raw worker runs**:
four core orders, six configurations, three repetitions. Every recorded tuple
digest agrees with an independent complete baseline. Candidate counts, stage
monotonicity, tuple/triple combinatorial counts, and all reported minima,
medians, and maxima agree with the raw data. Preprocessing plus search equals
the in-process total. External wall includes startup/imports/output. Measured
source hashes before and after agree with each other and with the final source,
including the imported first-edition dependencies.

The headline core-21 arithmetic is correct:

| Quantity | Unfiltered MITM | Filtered MITM | Baseline / filtered |
| --- | ---: | ---: | ---: |
| Stored pairs | 524,800 | 24,985 | 21.0046 |
| Median preprocessing + search, seconds | 1.5016 | 0.2042 | 7.3528 |
| Median external wall, seconds | 1.5319 | 0.2370 | 6.4642 |
| Median observed worker peak RSS, KiB | 220,376 | 21,868 | 10.0776 |

The report correctly rounds these ratios to 21.00, 7.35, 6.46, and 10.08.
Its staged core-21 counts, ablation tables, preprocessing medians, raw
four-multiset count, and product-triple counters also match the data. The two
full-profile/product-key wall ranges overlap. Product triples are **28.34 times
slower on the in-process total** than filtered pair matching at core 21.

The main limitations are stated accurately:

- A full-profile match is already a valid Williamson tuple, so adding the
  product key cannot remove an exact match. All MITM configurations have the
  same pre-order join counts: 2, 76, 234, and 192 at cores 3, 15, 19, and 21.
  The product key's observed timing difference is not new mathematical pruning.
- Core 19 has no order-three frequency. The corresponding two ablations have
  identical counts. At core 3, PSD adds no pruning beyond row arithmetic, its
  in-process overhead is visible, and startup dominates external wall.
- RSS is the Linux worker high-water mark sampled after search, including the
  interpreter and preparation/search allocations. It is not incremental memory
  and does not measure a later serialization peak. Zero stored pairs does not
  mean zero memory for the product-triple method.
- The baseline shares the documented small preparation work, and its main loop
  has no filter calls or per-pair filter-counter overhead. Results compare these
  implementations, with no claim about the best possible implementation.
- Workers were sequential and reviewer numerical searches did not overlap the
  formal benchmark. Three rotated repetitions do not supply portable guarantees
  or a strong statistical claim about small timing differences.

Evidence: [benchmark audit](benchmark-audit.json) and the
[full primary record](../evidence/benchmark.json).

## Scope, preservation, and reproducibility

The final prose distinguishes the eight small validation orders from the two
moderate complete demonstrations. It expressly leaves 17 and 23 unsearched in
this round. Counts remain raw sorted multisets of normalized symmetric
sequences, with repetitions, rather than equivalence-class counts. The
executable's supported bound is not reported as completed coverage. The finite
PSD bank is not promoted to a complete spectral oracle, and the exponential
single-sequence generation barrier at core 167 remains explicit.

The updated lessons are separately saved in `round2/LESSONS.md`. Independent
Git-object comparison confirms all **33 first-edition files** remain byte
identical to `b947c2f9c6ee0da0728c93d9ba74b66345d73d60`; see
[preservation evidence](first-edition-preservation.json).
All executable imports are standard-library modules or local authored modules.
This review did not independently re-browse every bibliographic source or
formalize the human proofs in a proof assistant.

From the repository root, after the primary data/benchmark files are present:

```bash
python hadamard-study/round2/reviews/independent_reductions.py \
  --output /tmp/round2-reductions.json
python hadamard-study/round2/reviews/independent_moderate.py \
  --output /tmp/round2-moderate.json
python hadamard-study/round2/reviews/audit_certificates.py \
  --data hadamard-study/round2/data/validated-solutions.json \
  --output /tmp/round2-certificates.json
python hadamard-study/round2/reviews/audit_benchmark.py \
  --benchmark hadamard-study/round2/evidence/benchmark.json \
  --output /tmp/round2-benchmark-audit.json
```

Timing/path metadata can differ on replay. Exact solution tuples, hashes,
arithmetic certificates, and matrix identities must agree. No remaining blocker
prevents publication of this bounded checkpoint.
