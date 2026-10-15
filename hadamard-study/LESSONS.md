# Lessons from the bounded Hadamard study

**Checkpoint: 2026-10-15. The full conjecture remains open.**

1. **A finite witness is much easier to verify than to discover.** We checked
   every row pair of externally supplied matrices at orders 668 and 2060 using
   independently authored exact arithmetic. This certifies those matrices. It
   does not reproduce the process that found their seeds or transfer credit for
   their construction to Codex.

2. **The source's date matters even for an old conjecture.** The “668 unknown”
   sentence on Epoch conflicts with its solution update. An August repository's
   “2060 next” claim is superseded by Schneider's explicit construction, current
   Sage source, and our finite verification. We leave the smallest unresolved
   order uncertified rather than infer a new frontier from incomplete coverage.

3. **Classical structure turns a matrix problem into a smaller exact problem.**
   Paley's prime construction follows from a short quadratic-character identity.
   Four symmetric circulants reduce Williamson orthogonality to complementary
   integer autocorrelation profiles. Their proofs and our implementations were
   independently checked. They are classical results, not new discoveries.

4. **A necessary filter can look stronger than it is.** Every feasible absolute
   row-sum pattern occurs among Williamson solutions for odd core orders through
   15. Nevertheless, a particular quadruple with the correct square sum may fail
   autocorrelation already at core order 5. Pattern feasibility and tuple
   validity are different questions.

5. **Small completeness is useful when its domain is explicit.** We enumerated
   every four-element multiset of first-entry-positive symmetric sign sequences
   at odd core orders 1 through 15. Counts are `1,1,1,4,7,5,15,14`; they are not
   equivalence-class counts. An independent brute-force enumeration agrees.
   This supplies reusable fixtures and correctness checks, not evidence of
   universal existence sufficient for a proof.

6. **The obstruction to continuing this approach is fundamental.** At core
   order 167 there are `2^83` normalized symmetric sequences. Pair buckets do
   not remove that exponential candidate-generation problem. Moreover, cited
   literature has failures of this restricted family at other orders. A failed
   family search can never establish global Hadamard nonexistence. We stopped
   instead of initiating an unbounded search or a speculative universal proof.
   One concrete comparison is the published Williamson failure at core 35:
   our checked Paley prime 139 instance still gives a Hadamard matrix of order 140.

The durable deliverables are [proofs](PROOFS.md), [exact small data](data/williamson-odd-through-15.json),
[independent reviews](reviews/independent-review.md), and
[source/hash replay instructions](PROVENANCE.md). No Lean result is claimed.
The 668 sources had no explicit redistribution license, so their full artifacts
are not republished. All downloaded code remained inert data or inspected text.

Useful future questions, each needing a separate bounded project:

- Can the published 668 compact seed and bordered array be reconstructed from
  primary data with a fully documented proof and clear discovery provenance?
- Which additional invariants distinguish small Williamson solutions that share
  row sums, and how do our multisets collapse under explicitly defined
  equivalences? This is classification work, not a route already known to solve
  all orders.
- Can a selected compression or SAT reduction preserve every solution in a
  declared family, with independently replayable certificates? First validate
  it against this complete small dataset and known family failures.
- What is the current verified construction frontier after reconciling dated
  databases with new explicit witnesses? This study verifies two large cases,
  not a census of all remaining gaps.
