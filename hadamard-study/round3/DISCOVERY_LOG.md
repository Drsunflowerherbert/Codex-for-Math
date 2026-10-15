# Discovery log: structure, weak pruning, and shared phases

This records the order of the third-round investigation and preserves approaches
that were weak, unsafe, or not implemented. Counts below are exploratory
enumeration observations supplied during development. Final timing, memory,
speedup and benchmark conclusions are reserved for the formal benchmark.

The domain throughout is odd-order **normalized symmetric circulant Williamson
quadruples**, reported as sorted row-mask multisets. These are not counts of all
Hadamard matrices or of every literature equivalence class.

## 1. Ask where an exclusion acts

The disk-covering comparison motivated seeking conditions that remove whole
classes or partial branches before constructing every complete object. We read
the actual public reports and the linked public n=20 partial-graph argument;
the unpublished n=25 exclusion formulas were not reconstructed from timings or
hashes. [Documented lessons](DISK_LESSONS.md), [pinned sources](SOURCES.md).

An early audit also corrected an attractive but redundant proposal from round
two: appending the product-theorem XOR mask to a join that already matches
**every** exact PAF coordinate cannot remove another valid full-profile match.
Full PAF cancellation already implies that product theorem. The XOR identity is
valuable earlier, when it determines or constrains missing rows; it is not an
additional mathematical exclusion after the full equations have been satisfied.
[Exact scope of the redundancy](../round2/PROOFS.md#adding-the-product-mask-to-a-full-profile-key).

## 2. Keep partial-sequence energy cancellation-safe

We considered generating individual rows recursively with attainable row sums
and integer-vector energy lower bounds. This became the separate
[partial-single comparator](scripts/partial_singles.py), rather than the main
structural-color search. It uses the same complete-row eligibility conditions
as round two, with safe bounds applied before completion.

The tempting shortcut was to fill unknown signs with zero, calculate the
resulting energy and reject if it was too large. This is unsound: unknown terms
can cancel the fixed contribution. At `m=9`, fixing position zero and the pairs
`+/-2,+/-3,+/-4` positive gives a zero-filled row sum seven, hence DC power
`49 > 4m=36`. Setting the remaining pair negative gives row sum five and power
25. This is mask 1 in the valid tuple `(1,9,9,14)`.
[Explicit counterexample and safe bound](PROOFS.md#why-unknown-entries-cannot-be-filled-with-zero-for-rejection).

The implemented bound instead encloses every remaining component contribution
and sums squared distances of those intervals from zero. A stronger
cardinality-aware completing-square certificate was derived, but its derivation
is not evidence that the comparator implements or benefits from it.
[Implemented and optional bounds](PROOFS.md#10-independent-alternative-single-sequence-partial-assignments).

## 3. Compression is an obstruction, not a lifting certificate

Compression suggested excluding entire residue-count classes before generating
signs. Its exact quotient equations retain energy `4m`, not `4d` for quotient
length `d`. A coupled quotient-diagonal count criterion was derived as an
additional option. It is not part of the main color benchmark unless explicitly
reported as implemented. [Derivation](PROOFS.md#11-additional-quotient-obstruction-before-full-sequences).

Two different counterexamples establish the limit of that idea:

- At `m=9`, masks `(2,10,10,13)` pass the row-square condition, product XOR and
  all proper cyclic quotient equations, yet their original shift-one PAF sum is
  `-8`. This disproves acceptance of **that particular lift**. It is not a
  no-lift example: the valid tuple `(1,9,9,14)` has the same compressed rows.
- The independent review found a stronger compressed type with rows
  `(-1,-1,-1), (-1,1,1), (-1,3,3), (3,-1,-1)`. Its combined compressed PAF is
  `(36,0,0)`. Each row individually has an original lift, but the recorded
  exhaustive check of all 16 original normalized rows and 3,876 four-row
  multisets finds no Williamson quadruple lifting the whole compressed type.

[Chosen-lift calculation](PROOFS.md#every-proper-quotient-can-pass-while-the-full-problem-fails),
[independent no-lift evidence](reviews/prefix-independent.json).
Thus compressed feasibility may preserve a necessary branch without certifying
that a valid full solution exists underneath it.

## 4. Replace four independent rows by coupled colors

Williamson's odd product theorem permits eight nonzero column states. Writing
them as `epsilon_i*(1-2e_color)` yields four orthogonal colors and a sign. Folding
each lag by reflection gives an exact edge equation. Its parity forces every
sign from the complete coloring. This removes the independent sign search
before individual rows or pair tables are generated.

Restricted-growth color words quotient precisely the already allowed row
permutations. The unpruned canonical domain has 43,947 colorings at `m=21` and
175,275 at `m=23`. Reconstructed columns still have to pass the full lag
equations. This is a derived exact representation, not a claim that every
coloring works or that the representation is novel. The classical quaternion
connection was reviewed separately. [Proof](PROOFS.md#3-shift-graphs-and-signs-forced-by-colors),
[prior art](SOURCES.md#quaternion-representation-and-the-separate-colorsign-investigation),
[independent representation check](reviews/structure-independent.json).

## 5. First prefix tests were sound but barely acted early

The first implementation propagated individually forced signs, coupled row
counts and per-lag capacity sets. Unknown edge terms were enclosed separately.
Every completion remained in those sets, so the exclusions were sound, but
shared dependencies between unknown signs were lost.

At `m=21`, the natural-order combined test entered **58,700 nodes** and
**43,877 complete colorings** out of 43,947. It skipped only **70** complete
colorings, all charged to rejections at depth nine. It retained the same
**34 solution multisets**. The pilot observation was slower than checking
complete colorings alone: this was not yet an effective early exclusion.
[Initial implementation](scripts/structure.py),
[prefix soundness and false positives](PROOFS.md#7-safe-lag-capacity-at-a-prefix),
[independent prefix review](reviews/prefix-independent.json).

This failure guided the next question: a sign may be individually unknown while
its relation to another unknown sign is already fixed.

## 6. Retain shared quadratic phases before relaxing them

Encoding each color with two Boolean bits expresses its sign exponent as a
quadratic algebraic-normal-form polynomial. After substituting a color prefix,
write `epsilon_i = eta_i * xi_(p_i)`, where `eta_i` is the known constant sign
and `p_i` is the residual polynomial with no constant term.

If two residual polynomials agree, their unknown phase is shared. Opposite
integer coefficients on that phase cancel exactly even if neither individual
sign is fixed. The independent review records an `m=15` example in which
vertices 2 and 6 have opposite constant signs and the same residual phase, so
their sum is identically zero. Treating those signs independently misses this.
[Phase proof](PROOFS.md#9-stronger-prefix-reasoning-through-shared-boolean-phases),
[checked example](reviews/anf-independent.json).

The exact expanded lag identity also retains unknown-color indicators as
quadratic phases. Exponents simplify over `F2`; their coefficients combine over
the integers. Only after equal phases have been collected do we relax distinct
phases to independent signs. Those distinct phases can still be dependent, so
passing the sumset test remains necessary rather than sufficient. Neither the
expanded identity nor the mixed unknown-edge enclosure was assumed to dominate
the other without measurement.

With the expanded identity and natural coordinate order at `m=21`, the working
run entered **49,291 nodes**, reached **34,468 complete colorings**, and skipped
**9,479**. Most exclusions still occurred at depth nine. It preserved the same
34 solutions. [Implementation](scripts/phases.py),
[independent ANF identities and solution-prefix checks](reviews/anf-independent.json).

The stronger predicates still have false positives. At `m=11`, the fixed
zero-based color prefix `(0,0,0,1)` passes both grouped row feasibility and the
expanded grouped lag test with one coordinate unassigned. Checking all four
unrestricted final colors, with signs reconstructed from the parity rule, finds
that every completion fails the full correlation equations. Individually
possible relaxed contributions need not come from one common completion.
[Recorded fixture and scope](PROOFS.md#12-traversal-memoization-and-a-bounded-diagnostic).

## 7. Choose an assignment order from structure, not solution data

The next change was a fixed collision heuristic computed only from quadratic
monomial supports. It greedily prefers coordinates whose assignment makes more
quadratic supports coincide; it uses deterministic tie-breaks and never consults
solutions. Its preparation is part of the charged preprocessing, not free work.
Canonical labels are introduced in visit order while all lag algebra retains
the original coordinate positions.

At `m=21`, it chose the one-based order
`[1,2,3,4,5,6,8,9,10,7]`. The exploratory run entered **20,239 nodes**, reached
**5,454 complete colorings**, and skipped **38,493**, preserving 34 solutions.
Of those skipped complete colorings, **141** were charged to depth-eight
rejections and **38,352** to depth-nine rejections. These are counts of
descendant leaves excluded, not counts of rejected prefix nodes.

At prime length 23 the heuristic returned natural order. That run reached
**127,102 of 175,275 complete colorings** and retained **11 solutions**. The
order therefore has no universal improvement guarantee, and the pruning remains
late at these bounds. [Ordering and traversal](scripts/phase_search.py),
[preserved round-two comparison at 23](reviews/m23-preserved-comparison.json).

## 8. Cache equivalent decisions without relabeling them as pruning

Finally, feasibility decisions were cached by canonical signatures after
irrelevant phase names were discarded. This reuses an answer to the same
necessary-condition subproblem. It changes evaluation cost, not the mathematical
predicate or the generation counts. Caches are cleared per run; their setup and
use belong in the benchmark's measurement scope.
[Decision caches](scripts/phases.py).

## 9. Diagnose why this particular equality test remains late

A bounded diagnostic then examined the quadratic supports of phase differences.
To make two residual phase polynomials equal under freely varying remaining
color bits, every quadratic monomial of their difference must first disappear.
Assigned physical vertices must cover those monomial supports; assigning one
endpoint removes a cross-vertex quadratic term, while a same-vertex term requires
that vertex. The diagnostic enumerates all assigned vertex subsets for each
pair, rather than guessing a minimum cover.

It includes the zero phase and the `h` sign phases, giving `C(h+1,2)` pairs.
At `m=21`, 40 pairs require at least six assigned vertices to remove all
quadratic terms, and 15 require at least seven. At `m=23`, the corresponding
counts are 11 and 55. Even after all quadratic terms disappear, remaining linear
terms can prevent phase equality.
[Diagnostic script](scripts/quadratic_diagnostic.py),
[exact bounded output](evidence/quadratic-obstruction.json).

This is a necessary condition for this free-color residual-phase equality
detection mechanism. It is not a lower bound on all pruning algorithms, on
reasoning restricted to canonical color completions, or on the global Hadamard
problem. It helps explain a limitation of the chosen relaxation without turning
a late-pruning observation into a general impossibility claim.
[Proof and caveats](PROOFS.md#12-traversal-memoization-and-a-bounded-diagnostic).

The recorded small-order checks, valid-solution-prefix preservation and exact
tuple comparisons support the tested implementation. They complement the
necessity and completeness proofs; they do not replace them.
[Subject audit](reviews/subject-audit.json),
[validated solution and matrix checks](data/validated-solutions.json).
No speedup over round two is claimed here. The formal benchmark must separately
measure preprocessing and traversal on its frozen sources, and compare the
complete output tuple lists. Exact matrix validation is a separate run. None
of these finite-family results proves the general Hadamard
conjecture or settles an unreported order.
