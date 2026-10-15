# Independent adversarial review of round three

**2026-10-15 UTC. Verdict: the stated finite checkpoint is supported.** No
blocking mathematical, coverage, arithmetic, or benchmark-record defect remains
in the reviewed version. The structural reduction acts before individual-row
generation, but the measured implementation does **not** improve elapsed time
over the preserved filtered pair search. It proves no general Hadamard claim.

The reviewer authored the independent scripts in this directory, did not edit
the subject implementations, and made no commits. The review binds the files
listed in `reviewed-files.sha256`; later publication metadata is outside that
binding. All checks use Python's standard library.

## Sources and scope

Before proposing exclusions, I independently read the two requested public
n=25 Astra and Sol disk-covering reports at revision
`122ba78c748303f4d590d20c7df16630dba51fd2`. They support the methodological
lesson about cheap exclusions removing classes or partial branches. They do
not disclose the complete new exclusion formulas and global proof archive.
The study properly separates those reports, its source author's additional
public antecedent review, and the Hadamard criteria derived here. I have not
independently replayed the disk-covering proofs or the unpublished n=25 work.

The exact target is sorted four-multisets of original normalized symmetric
sequence masks, with repetitions. Only block permutations are quotiented.
No multiplier, coordinate, shift, or Hadamard-equivalence quotient is silently
added. Structural quadruple validation covers odd cores 1 through 15 and
19, 21, 23; it does not include 17. The separate single-row study does include
17. Parameter acceptance through 25 is not a record of running every input.

## Mathematical and coverage checks

I independently reconstructed the reflection orbits of physical cyclic edges.
The zero-incident orbit and unique reflection-fixed edge give the constant
and single-sign terms. Every remaining orbit gives the stated same-color
contribution. Reduction of the exact integer equation modulo four forces
every sign from the complete coloring. Composite lags can yield cycles, so a
universal path assumption would be wrong. The actual remaining cyclic quotient
graphs are simple; synthetic repeated edges nevertheless correctly exercise
integer multiplicity versus cancellation modulo two.

The restricted-growth encoding is a bijection with the already specified
sorted block multisets, including unused colors, repeated rows, and the empty
core-one coloring. A fixed physical coordinate permutation changes traversal
only. I recanonicalized each true coloring in both visit orders and kept
physical positions in its reconstructed masks.

The prefix rules preserve every completion: attainable row-count sets and
edge Minkowski sums are supersets of actual possibilities; quadratic Boolean
phase substitution is exact; equal residual phases share one sign with their
constant factors retained. Distinct phases are then relaxed independently,
which can create false positives but cannot create false negatives. The
expanded character equation is an exact identity before that relaxation.
Neither expanded nor mixed-domain enclosure is assumed to dominate the other.
The coordinate score uses quadratic parts only as a heuristic; acceptance
uses the full residual polynomials. Cache keys retain the fixed constants,
coefficient multiplicities, domain orientations, and cross-color vector signs
up to one whole-vector negation. They cache equivalent relaxed decisions,
not complete mathematical states.

The cancellation-safe partial-single energy bound follows component by
component from the triangle inequality. Strict rejection above the energy
limit preserves equality. Optional stronger dual and quotient-diagonal
criteria have sound derivations but are identified as options, rather than
implemented benchmark improvements. Compressed feasibility does not imply
a compatible full lift.

## Independent exact evidence

`independent_structure.py` imports no study module and uses an independently
written physical-edge quotient and unpruned canonical-color enumeration:

| Core | Unpruned colorings | Exact normalized multisets |
| ---: | ---: | ---: |
| 1 | 1 | 1 |
| 3 | 1 | 1 |
| 5 | 2 | 1 |
| 7 | 5 | 4 |
| 9 | 15 | 7 |
| 11 | 51 | 5 |
| 13 | 187 | 15 |
| 15 | 715 | 14 |
| 19 | 11,051 | 42 |
| 21 | 43,947 | 34 |
| 23 | 175,275 | 11 |

All 124 previously checked tuples agree with the preserved independent
original-mask baselines. At 23 the new eleven tuples also agree with the
preserved round-two filtered original-mask search; this is distinct from an
unfiltered two-million-pair baseline. The new unpruned color enumeration is
complete in its proved bijective domain.

`independent_prefix.py` checks all 1,354 small unpruned prefix states, 8,919
full-color sign-domain components, and 1,230 valid-solution prefixes.
`independent_anf.py` uses square-free monomial sets rather than the subject's
packed polynomial representation and checks 49,798 exact identities.
`audit_subject.py` compares the subject with these independently established
objects: 30,383 residual ANFs, 4,062 basic predicates, both coordinate orders,
and 2,460 recanonicalized valid prefixes. Small cores exercise all phase modes;
the expanded mode in both orders matches every exact moderate tuple set.
Generation and skipped-subtree accounting are checked separately from outputs.

`independent_diagnostic.py` independently verifies all 194 phase-pair support
graphs and exact minimum-cover records at cores 15, 19, 21, 23. At 21 the
minimum assigned-vertex histogram is six:40, seven:15; at 23 it is six:11,
seven:55. This is an obstruction for formal free-color residual-phase
equality, not a lower bound for other pruning mechanisms or canonical domains.

Finally, `audit_final.py` rebuilds all 135 arrays without study imports and
checks **689,008 entries and 339,854 unordered row pairs** using explicit
integer dot products. Every reported matrix hash agrees. It also independently
enumerates all eligible single-row masks through 23 using direct integer
convolutions and checks all 33 stored validation lists and all benchmark
single-mask digests. All **30 unit tests** were replayed and passed: nine
first-edition tests, nine second-edition tests, and twelve new tests.
All **59** files tracked under `hadamard-study/` at preserved commit
`913b328b74712409a036cd49c954cd8a7dcd18b1` remain byte-identical.

## Adversarial fixtures retained

- A genuine core-nine Williamson row has zero-filled partial DC power above
  the permitted limit while a remaining negative pair cancels it. Zero-filling
  unknown signs would therefore create a false negative.
- At core seven, an unknown degree-two vertex with differently colored known
  neighbors cannot use the same cancellation rule as equal-colored neighbors.
- At core fifteen, vertices with a shared residual phase and opposite constant
  factors cancel exactly. Forgetting the constants changes the feasible set.
- At core eleven, prefix `(0,0,0,1)` passes the grouped row and expanded lag
  relaxations although all four unrestricted final colors fail. Only three
  are canonical extensions; the fourth is color-renaming equivalent.
- A core-nine compressed multiset has PAF `(36,0,0)` and individually liftable
  rows, yet checking all 16 original rows and 3,876 row multisets finds no
  Williamson lift of that entire compressed multiset. This is stronger than
  merely exhibiting one invalid choice of lifts.
- Core one, repeated blocks, equality at the rejection threshold, arbitrary
  assigned coordinate sets, repeated synthetic edges, one-sided lag domains,
  and unsafe coordinatewise sign normalization are explicitly checked.

## Resource and generation claims

The benchmark driver uses fresh sequential Linux subprocesses with three
repetitions per case. External wall includes imports, preparation, search, and
JSON output. Its in-process components charge their documented setup; RSS is
sampled through the search and excludes a later serialization peak. Row-profile
preparation performs more work than returning eligible single masks, so that
separate comparator is correctly not presented as equal-work quadruple timing.

I audited all **45 quadruple and 27 single-generation worker records**, matched
their tuple or mask digests with independent exact lists, recomputed all
**102** summary min/median/max triples, and verified the before/after measured
source hashes against current files. This audits the recorded experiment;
it does not independently reproduce those historical timings or certify an
otherwise idle host.

At core 21, the final traversal enters 20,239 nodes and 5,454 complete colorings
out of 43,947. Its 38,493 skipped leaves are mostly late: 141 are charged to
depth eight and 38,352 to depth nine of ten. Its median external wall is
1.132563 seconds versus 0.246415 for the earlier filtered pair method; observed
RSS is 19,712 versus 24,552 KiB. At 23, final phase traversal takes 8.674294
seconds versus 0.609887, with RSS 22,272 versus 39,680 KiB. These are resource
tradeoffs, not a speedup. Individual-sequence and color-leaf counts measure
different search domains.

The complete-coloring counter is incremented before leaf predicates. At a leaf
the grouped lag test already checks the full correlation equations; its later
explicit correlation call is redundant. The latter's smaller count must not
be reported as the number of completed candidates generated or correlations
evaluated. Final prose now makes this distinction.

## Reproduction and limits

The independent scripts expose `--output PATH`; run them from the repository
root. `audit_subject.py` compares subject code only after independently
constructed baselines, while the independent algebra, prefix, structural,
diagnostic, and final arithmetic scripts import no study modules. JSON files
next to them preserve their checked results. `audit_final.py` audits the saved
benchmark without rerunning a timing experiment.

The written soundness arguments and exhaustive bounded comparisons support
this implementation's declared finite coverage. They do not establish a
universal construction, new missing order, matrix-equivalence classification,
new priority claim, Lean verification, or completeness outside the stated
Williamson family. No downloaded third-party executable was run. Continuing
these mostly late exclusions at much larger bounds would need a new resource
case and new validation, rather than extrapolation from the present counts.
