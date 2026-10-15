# Formal experiment record

Run date: **2026-10-15 UTC**. Configuration and exact raw observations are in
[benchmark.json](evidence/benchmark.json). Pilot results that guided the search
are preserved separately in [DISCOVERY_LOG.md](DISCOVERY_LOG.md).

## Protocol and validity checks

The formal run used Python **3.12.14**, Linux x86-64, an AMD EPYC 9V74 80-Core
Processor, and the standard library only. There were **45 quadruple-search
workers**: five configurations, three core orders, three repetitions. A further
**27 workers** compared eligible single-row generation. Workers ran sequentially
in fresh processes, with deterministically rotated case order. Independent
review and validation processes had finished before timing began.

Every measured implementation and imported first-/second-edition dependency was
SHA-256 hashed before and after the whole run. All hashes stayed identical.
Each quadruple worker returned the **actual full sorted tuple list** from the
independent unpruned structural enumeration. Every list matched. Single-row
workers likewise agreed on their full original-mask lists. Hashes of those
lists are additional identifiers, not substitutes for the equality comparisons.

Preparation includes graphs, targets, phase algebra, coordinate ordering,
probe construction, sequence profiles where applicable, and cache reset.
Reported internal total is preparation plus search. External wall also includes
Python startup, imports, worker-wrapper work, and JSON serialization. The Linux
`ru_maxrss` observation is taken immediately after search: it includes the
interpreter, preparation, and decision caches, but excludes any larger later
serialization peak. It measures an entire worker process, not incremental
algorithm allocation. There is no subtraction of a common interpreter cost.

Exact matrix construction and all-row-pair verification were separate untimed
validation runs. Source hashes bind a fixed implementation, not the soundness
of an exclusion; that comes from the proofs and independent checks.

## Same-domain structural ablation

The structural configurations all enumerate the same canonical four-color
domain and report the same normalized row-mask multiset outputs. Their counts
are directly comparable. `leaf` applies no proper-prefix rejection. `basic`
uses independent sign domains, row feasibility, and lag capacities. `phase`
retains shared residual phases and uses the expanded lag identity. Natural
and collision orders use the same predicates. Decision caches are cleared on
each phase search and bounded at 4096 entries per cache.

| Core | Configuration | Nodes entered | Complete colorings entered | Leaves skipped before completion | Solutions |
| ---: | --- | ---: | ---: | ---: | ---: |
| 15 | leaf | 977 | 715 | 0 | 14 |
| 15 | basic | 972 | 710 | 5 | 14 |
| 15 | phase, natural | 897 | 635 | 80 | 14 |
| 15 | phase, collision order | 478 | 216 | 499 | 14 |
| 21 | leaf | 58,770 | 43,947 | 0 | 34 |
| 21 | basic | 58,700 | 43,877 | 70 | 34 |
| 21 | phase, natural | 49,291 | 34,468 | 9,479 | 34 |
| 21 | phase, collision order | 20,239 | 5,454 | 38,493 | 34 |
| 23 | leaf | 234,045 | 175,275 | 0 | 11 |
| 23 | basic | 232,676 | 173,908 | 1,367 | 11 |
| 23 | phase, natural | 185,862 | 127,102 | 48,173 | 11 |
| 23 | phase, collision order | 185,862 | 127,102 | 48,173 | 11 |

Every node and complete coloring is counted **on entry, before its tests**.
Skipped-leaf totals use the exact restricted-growth subtree recurrence and
exclude depth-`h` rejection. For each run,
`complete_entered + proper_prefix_skipped = all_canonical_colorings`.
That accounting check supports the implementation; the mathematical proof is
still required to show each rejected subtree contains no solution.

At core 21 the fixed one-based order is `[1,2,3,4,5,6,8,9,10,7]`. Its 38,493
skipped leaves consist of **141** charged to rejections at depth eight and
**38,352** at depth nine, out of ten coordinates. At core 23 the order is
natural: **37** leaves are charged at depth nine and **48,136** at depth ten,
out of eleven. These are descendant-leaf counts, not rejected-node counts.
The depth-resolved rejected-node counts are retained in the JSON.

At a complete coloring, the grouped lag predicate is an exact correlation
check already. The later `full_correlation` function repeats it for acceptance.
Thus `full_correlation_checks_after_row_identity` is only that explicit-call
counter. It is **not** the total number of correlations considered and is not
used here as a generation metric.

## Time and memory, including preparation

The reference is the preserved round-two filtered full-profile pair method.
It generates all individual normalized rows before filtering. It stores 1,061,
24,985, and 58,982 pairs at cores 15, 21, and 23. Every structural method stores
zero pairs and generates no separate single-row pool; it still visits the
complete color assignments counted above. Pair counts and color-node counts
have different units and must not be divided to claim a work reduction.

All values below are **medians of three fresh workers**. Minimum and maximum
observations, including preparation/search components, are in the raw data.

| Core | Method | Preparation (s) | Internal total (s) | External wall (s) | Observed process peak RSS (KiB) |
| ---: | --- | ---: | ---: | ---: | ---: |
| 15 | round-two filtered pairs | 0.002118 | 0.007125 | 0.050696 | 14,336 |
| 15 | structural leaf | 0.000183 | 0.004040 | 0.047836 | 13,824 |
| 15 | structural basic | 0.000178 | 0.018955 | 0.065698 | 13,824 |
| 15 | phase, natural | 0.000354 | 0.032314 | 0.079597 | 14,336 |
| 15 | phase, collision order | 0.000486 | 0.019271 | 0.066370 | 14,080 |
| 21 | round-two filtered pairs | 0.025440 | 0.200095 | 0.246415 | 24,552 |
| 21 | structural leaf | 0.000344 | 0.326725 | 0.368957 | 13,952 |
| 21 | structural basic | 0.000327 | 1.602465 | 1.649883 | 13,952 |
| 21 | phase, natural | 0.000691 | 1.936337 | 2.009284 | 20,864 |
| 21 | phase, collision order | 0.000934 | 1.066556 | 1.132563 | 19,712 |
| 23 | round-two filtered pairs | 0.055751 | 0.567459 | 0.609887 | 39,680 |
| 23 | structural leaf | 0.000344 | 1.493585 | 1.538409 | 14,080 |
| 23 | structural basic | 0.000372 | 5.725581 | 5.773086 | 14,080 |
| 23 | phase, natural | 0.000874 | 8.605222 | 8.680591 | 22,268 |
| 23 | phase, collision order | 0.001060 | 8.618204 | 8.674294 | 22,272 |

The final structural method is slower than the filtered pair reference at all
three measured orders. It reduces process RSS at the moderate cores, with
phase bookkeeping/cache costs visible relative to the simple structural leaf
method. At core 23, natural and collision traversals are identical; their small
timing difference is run variation, not a pruning effect. Small core-15 wall
times are dominated by startup and should not be read as a scaling result.

This confirms a structural generation reduction at core 21 and a time/memory
tradeoff on this implementation. It does not establish a generally faster
algorithm, a hardware-independent speed ratio, or an asymptotic improvement.

## Alternative: generate eligible single rows by partial assignments

This experiment has a different output domain: eligible individual masks,
**without any quadruple join**. `prefix-row` tests exact attainable row-square
residuals at proper prefixes. `prefix-all` also uses cancellation-safe integer
energy lower bounds. Both use all round-two eligibility conditions at a leaf.
The reference round-two preparation additionally builds complete profiles for
its later pair search; the prefix comparators do not. Their times are therefore
reported as observed generation/preparation work, not equal-work quadruple
search runtimes.

| Core | Prefix method | Nodes visited | Complete assignments entered | Eligible masks | Proper-prefix energy rejections |
| ---: | --- | ---: | ---: | ---: | ---: |
| 15 | row | 251 | 124 | 81 | 0 |
| 15 | all | 241 | 116 | 81 | 3 |
| 21 | row | 2,003 | 984 | 560 | 0 |
| 21 | all | 1,871 | 868 | 560 | 50 |
| 23 | row | 3,937 | 1,914 | 968 | 0 |
| 23 | all | 3,579 | 1,612 | 968 | 123 |

Proper energy rejections exclude row arithmetic; at core 21 they comprise
eight order-three and 42 triangular-probe rejections. The unpruned binary
trees have 255, 2,047, and 4,095 nodes respectively. A complete assignment can
be rejected before constructing its full sequence object; it still counts as
entered and is not described as an avoided complete candidate.

| Core | Configuration | Median internal total (s) | Median external wall (s) | Observed peak RSS (KiB) |
| ---: | --- | ---: | ---: | ---: |
| 15 | round-two preparation | 0.002774 | 0.043637 | 13,952 |
| 15 | prefix row | 0.020158 | 0.067953 | 14,464 |
| 15 | prefix all | 0.029011 | 0.074692 | 14,976 |
| 21 | round-two preparation | 0.029331 | 0.080657 | 14,592 |
| 21 | prefix row | 0.293722 | 0.341810 | 14,720 |
| 21 | prefix all | 0.372430 | 0.420954 | 15,232 |
| 23 | round-two preparation | 0.056596 | 0.103098 | 15,488 |
| 23 | prefix row | 0.668506 | 0.711845 | 14,720 |
| 23 | prefix all | 0.698099 | 0.742300 | 15,360 |

The early energy exclusions are real but modest, and this implementation does
not overcome their cost. No integrated partial-row-plus-pair speedup is claimed.
[Full single-row validation](evidence/partial-single-validation.json) compares
all three configurations at every odd core through 21: **33 exact mask-list
comparisons**. Exhaustive completion audits through core 11 check **354 visited
nodes and 1,134 probe-bound comparisons**, retaining all cancellation cases.

## Review, matrix validation, and stopping decision

Independent reviewers implemented their own physical-edge quotient, unpruned
color enumeration, monomial-set phase algebra, step-two count sets, and integer
Minkowski sums. The [subject audit](reviews/subject-audit.json) checks both visit
orders, exact small and moderate outputs, and all recorded true prefixes.
The [diagnostic review](reviews/diagnostic-independent.json) independently checks
194 phase pairs and the core-11 relaxed false positive. The original small
baseline is exhaustive over all four-multisets; the moderate independent
structural baseline is unpruned. Core 23 also agrees with preserved round-two
filtered matching.

All **135 matrices**, at the eleven stated cores, pass **339,854** exact row-pair
checks. Their sign-byte hashes and full original-mask tuples are in
[validated-solutions.json](data/validated-solutions.json). These tests are
separate from comparative timing. Earlier-edition tests and the new bounded
regressions are recorded alongside the review.

We stopped after the weak rules, shared-phase rules, structural ordering,
single-row energy alternative, and a diagnostic obstruction were checked.
The surviving exponential domain and late exclusions are concrete blockers
for extending this line to large cores. They are not a proof that stronger
structural rules are impossible. More unguided enumeration with the same rules
would not address the general conjecture.
