# Round 3: exclude structural branches before generating sequences

**Checked checkpoint, 2026-10-15 UTC. The Hadamard conjecture remains open.**

This round replaces the complete-sequence pool with a four-color structural
search, proves that every solution in the declared family survives, and checks
the exact output against independent complete baselines. At core order 21,
the final structural traversal enters **5,454 complete colorings out of
43,947**, preserving all **34** solutions. It builds no pool of individual
sequences and stores no sequence pairs. The exclusions remain mostly late,
and the structural implementation is slower than the earlier filtered pair
method. The evidence below keeps generation, elapsed time, and memory separate.

The first two editions remain byte-for-byte preserved at
[`913b328b74712409a036cd49c954cd8a7dcd18b1`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/913b328b74712409a036cd49c954cd8a7dcd18b1/hadamard-study).
The [first status audit](../README.md#status-audit-both-668-and-2060-have-finite-witnesses)
and its exact checks of external matrices at orders 668 and 2060 still apply.
This round adds no large external matrix claim and certifies no smallest open
order. Human/Claude-assisted construction reports are distinct from our Codex
replications and bounded search.

## What transferred from the disk-covering records

The specified public n=25 comparison credits cheap necessary exclusions of
whole topology classes and partial graph branches. Its two complete exclusion
formulas and proof archive are not public. We read the actual reports and their
public n=20 antecedent, whose already forced graph edges yield persistent exact
difference constraints. A contradiction can remove all descendants before
their completed graphs are built. [DISK_LESSONS.md](DISK_LESSONS.md) records the
sources, their publication limits, and the lessons from the other named cases.

Here the transferable requirement is to reject a partial structure only when
**every completion fails**. A geometric lemma or a local certificate does not
transfer automatically. In particular, one common Hadamard order does not
remove the many unknown signs, just as a common covering radius does not
remove the geometry's quantified variables.

## The exact restricted target

Let `m=2h+1`. Each of four sequences has `x[0]=+1`, `x[j]=x[-j]`, and entries
in `{−1,+1}`. We seek sorted four-multisets of their original negative-bit masks,
allowing repetitions. Their periodic autocorrelations must sum to zero at
every nonzero shift. The Williamson array then gives a Hadamard matrix of
order `4m`. We quotient block permutations only, exactly as in earlier editions;
we do not quotient coordinate multipliers, shifts, or matrix equivalence.

Complete validation covers **odd cores 1 through 15, then 19, 21, and 23**.
Core 17 was not included in the structural quadruple study. The separate
single-row comparator does include every odd core through 21. Bounds accepted
by an executable are not claims that every accepted input was run.

This family is narrower than general Hadamard matrices. Published Williamson
failures already preclude treating it as a universal construction family.
No absence of a solution here would prove global Hadamard nonexistence.

## The structural reduction

Williamson's classical odd product theorem forces each nonzero coordinate's
four signs to have product `−1`. Thus its column is uniquely

```text
epsilon_j * w_(color_j),     w_c = (1,1,1,1) − 2e_c,
epsilon_j in {−1,+1},        color_j in {0,1,2,3}.
```

The four `w_c` are orthogonal. Pairing correlation terms by reflection gives
an exact edge equation for each lag `t`. If `E_t` is its folded edge multiset,
then

```text
total_PAF(t)/4 = 1 + epsilon_t
                 + 2 sum_(u,v in E_t) epsilon_u epsilon_v [color_u=color_v].
```

Reduction modulo four forces **every sign from the colors alone**:

```text
epsilon_t = −(−1)^(number of monochromatic edges in E_t).
```

Full correlation equations still have to pass. Canonical restricted-growth
color words encode exactly one representative per sorted block multiset.
There are `sum_(k<=4) S(h,k)` such words for `h>0`, approximately `4^h/24`.
This remains exponential. The quaternion/column representation is classical;
our checked sign derivation and implementation carry no priority claim.

The first prefix tests treated unresolved signs independently. They were weak:
at core 21 they skipped only 70 complete colorings. Encoding colors by two bits
expresses every sign as a quadratic Boolean phase. Two signs may share the
same unresolved phase with opposite constant factors, so their sum is exactly
zero even while neither sign is individually known. The final rules preserve
these relations, group equal residual polynomials, and relax only the remaining
distinct phases to independent signs. An impossible exact integer sum then
rejects every descendant. [PROOFS.md](PROOFS.md) proves these steps and the
finite-domain coverage; it also proves the safe partial-energy comparator.

A fixed coordinate order chosen from quadratic supports exposes some relations
earlier at composite core 21. It uses no solution data. Actual decisions always
use full residual polynomials, including linear terms and constant factors.
Small bounded caches store equivalent feasibility questions, not guessed
answers or merged mathematical states. Their preparation and memory are charged.

## Exact results and resource comparison

All **135** output tuples were converted into Hadamard arrays. Exact checking
covered **689,008 entries and 339,854 unordered row pairs**, with every
off-diagonal dot product zero. The [stored tuples and matrix hashes](data/validated-solutions.json)
identify every array. Independent unpruned color enumeration agrees, as do the
preserved original-mask baselines. These are counts of normalized multisets,
not equivalence classes or newly discovered orders.

| Core | Matrix order | All canonical colorings | Final complete colorings entered | Solutions |
| ---: | ---: | ---: | ---: | ---: |
| 15 | 60 | 715 | 216 | 14 |
| 19 | 76 | 11,051 | 8,916 | 42 |
| 21 | 84 | 43,947 | 5,454 | 34 |
| 23 | 92 | 175,275 | 127,102 | 11 |

“Entered” counts a complete coloring **before any leaf filter**, including
ones immediately rejected. At a full coloring the grouped lag test itself is
already an exact correlation check. The later explicit acceptance call repeats
that check; its smaller counter must not be substituted for candidate generation.
Node counts, depth-resolved exclusions, stored pairs, timing, and peak process
RSS are recorded in [the formal experiment log](EXPERIMENT_LOG.md) and
[raw benchmark data](evidence/benchmark.json).

## Why this is a useful stopping point

The first simple transfer was too weak; shared-phase relations and structural
ordering improved it substantially at one moderate composite order. They did
not produce a uniformly early or faster method. At core 21, 141 skipped leaves
are accounted for at depth eight and 38,352 at depth nine of ten; most decisions
still wait for almost the whole structure. At prime core 23 the heuristic
selects the natural order. A bounded quadratic-support diagnostic explains
one obstacle to forcing phases early, while not claiming a lower bound for
other algorithms.

We also retain concrete failures of sufficiency. A core-11 prefix passes the
final relaxed row and lag tests but none of its four unrestricted color
completions works.
At core nine, compressed equations can pass for individually liftable rows
without any Williamson lift of the entire compressed multiset. Unknown signs
filled with zero can falsely reject an actual valid completion. The
[discovery log](DISCOVERY_LOG.md) preserves these examples and abandoned paths.

Continuing to larger orders with these same tests would mainly spend more
exponential work. A worthwhile next project would need stronger dependencies
between phase values or quotient-aware partial structures, first tested against
this exact dataset. No such improvement is assumed, and no general existence
argument follows from this checkpoint. [LESSONS.md](LESSONS.md) states the
achievements, nonclaims, and specific future questions.

## Reproduce

Python 3.12.14, standard library only; no installation or Library dependency.
From the repository root:

```bash
python -m unittest discover -s hadamard-study/round3/tests -v
python hadamard-study/round3/scripts/validate.py --output /tmp/hadamard-r3-validation.json
python hadamard-study/round3/scripts/partial_singles.py --validate-max-core 21 --output /tmp/hadamard-r3-singles.json
python hadamard-study/round3/scripts/quadratic_diagnostic.py --output /tmp/hadamard-r3-quadratic.json
python hadamard-study/round3/scripts/benchmark.py --cores 15 21 23 --repeats 3 --output /tmp/hadamard-r3-benchmark.json
```

The benchmark requires Linux for its KiB RSS interpretation. Its workers run
sequentially and verify actual tuple-list equality. Benchmark times are empirical
on this machine, not complexity bounds. [SOURCES.md](SOURCES.md) contains pinned
primary references and document hashes; [the independent review](reviews/REVIEW.md)
records the adversarial checks. No downloaded third-party solver was executed,
no third-party matrix is republished here, and no Lean result is claimed.
