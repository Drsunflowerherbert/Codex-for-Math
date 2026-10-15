# Lessons from trying to move the generation barrier

**2026-10-15. Bounded symmetric Williamson research; no solution of the
Hadamard conjecture is claimed.**

The useful change was to search a coupled structure before constructing
individual rows. Classical product parity reduces each nonzero four-entry
column to a signed color. Reflection of the correlation equations then forces
every sign from the colors. We proved this reduction and its exact
block-permutation quotient, and independent complete enumerations reproduce
all 135 reported tuples. Every resulting array passes the exact matrix check:
689,008 entries and 339,854 unordered row pairs.

The disk-covering lesson that transferred was **where an exclusion acts**.
Already forced structure should imply a condition that every descendant must
satisfy; its failure removes a whole branch. The public n=25 report motivates
this, and the public n=20 difference-constraint argument supplies an inspectable
example. We did not obtain the unpublished n=25 formulas or replay its private
global proof. Geometry-specific exclusions did not become Hadamard lemmas by
analogy. The [source note](DISK_LESSONS.md) distinguishes the evidence.

The first direct attempt was disappointing. Independent unresolved-sign
domains, row-count distance bounds, and correlation intervals skipped just
70 of 43,947 canonical colorings at core 21. They added work while leaving
almost all completed structures to be generated. Adding more complete-row
filters would not fix this particular bottleneck.

The more useful insight was that **unknown quantities can have known
relations**. Two quadratic Boolean sign phases can have the same unresolved
part with opposite constants. Their sum then cancels for every completion.
Keeping this relation is stronger than giving each sign a separate interval.
Grouping exact residual phases made sound earlier exclusions possible. A fixed
order chosen from quadratic supports reduced completed colorings at core 21
to 5,454; 38,493 were skipped before completion. The order retained every
original coordinate and every output tuple.

That improvement has precise limits:

- Most skipped work still lies below prefixes of length nine out of ten.
  Only 141 leaves are accounted for at depth eight. At prime core 23, the
  order heuristic returns the natural order and enters 127,102 of 175,275
  complete colorings. There is no uniform early-generation breakthrough.
- The new structural code is slower than the previous filtered pair method
  in the measured cases. It uses no pair table, but bookkeeping and caches
  also consume memory. A smaller count in a different search space is not
  automatically less work. [The experiment log](EXPERIMENT_LOG.md) reports
  all preparation, elapsed time, memory, and count definitions.
- Equal quadratic parts merely make a shared phase possible. Linear parts
  can still differ. The implementation compares full residual polynomials.
  A bounded vertex-cover diagnostic explains one obstruction to constant-phase
  detection, not a lower bound for arbitrary algorithms.
- Distinct residual phases satisfy additional algebraic relations. Treating
  them as independent signs is a safe relaxation and can admit impossible
  combinations. A core-11 prefix passes the grouped tests yet none of its
  four unrestricted completions works. The doubled character expansion is
  another exact identity followed by a relaxation; it is not asserted to
  dominate every other enclosure.

Two failures are especially reusable as adversarial fixtures. Filling unknown
signs with zero can overestimate the energy of an actual valid completion:
the remaining signs can cancel the partial sum. Our alternative single-row
branch search uses a proved cancellation-safe lower bound and matches all
33 mask-list comparisons through core 21, but its proper-prefix energy gain
is modest. Separately, compressed rows can each have valid sign lifts and
jointly pass compressed correlations while the entire multiset has no
Williamson lift. Neither a projected witness nor compatible row sums supplies
the missing common completion.

Exact representation, exact rejection, and complete coverage are separate
obligations. We checked the RGS quotient against all color names, retained
original sequence masks rather than filtered ranks, counted complete leaves
before leaf rejection, and compared actual tuples against independently
authored unpruned searches. Every full-color lag test is already a correlation
check; the small count of later explicit acceptance calls is not the number
of candidate correlations performed. The review caught this reporting hazard
before publication.

We stopped after the representation, relation, ordering, and cancellation-safe
single-row alternatives had been proved and compared. The remaining domain
grows approximately as `4^h/24`, and the measured exclusions mostly act late.
Larger runs with these same rules would demonstrate that growth without
explaining universal existence. Moreover, the symmetric Williamson family
itself has known failures at other orders. Its bounded successes cannot settle
the general Hadamard conjecture.

Worthwhile next questions have concrete gates:

1. Can a small exact dependency system between residual phases reject the
   core-11 false positive cheaply? Validate every proposed rule against all
   stored valid prefixes and the complete small baselines before benchmarking.
2. Can quotient counts be coupled to support-generation choices early enough
   to survive their lifting counterexamples? The derived count criteria in
   [the proofs](PROOFS.md) are options, not completed implementations or assumed
   improvements.
3. Can variable order be chosen using more than quadratic collision potential
   while retaining the same output domain? A useful result must improve total
   time or another stated resource on independently held-out bounded cases,
   with ordering and preparation charged.

No new universal construction, new missing order, inequivalence classification,
global nonexistence result, priority claim, SAT completeness certificate, or
Lean verification follows from this work. The durable result is a reviewed
structural reduction, reproducible bounded evidence, and concrete reasons
that several tempting shortcuts fail.
