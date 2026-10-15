# Updated lessons after the search-reduction round

**2026-10-15.** This update preserves the [first edition](../LESSONS.md) and
adds what the second round established. The full Hadamard conjecture remains
open; none of these finite searches was a new matrix discovery.

1. **Mathematical criteria did move the practical barrier.** At core 21, exact
   row-square and integer energy tests reduce stored pairs from 524,800 to 24,985
   while preserving the exact 34-solution set. Three-process medians improve
   external wall time by 6.46 times and observed peak RSS by 10.08 times. This is
   a comparison against an already efficient full-profile MITM baseline,
   with preprocessing included.

2. **The most attractive identity was not automatically the fastest algorithm.**
   Williamson's classical odd product theorem forces the fourth sequence from
   the other three. The resulting triple search stores no pair table but is
   much slower than filtered pair matching at 21. Adding product bits to an
   exact full-correlation key eliminates no matches at all: the correlation
   equations already imply the product theorem. Redundancy is a useful finding.

3. **Exactness is possible without floating spectral thresholds.** For any
   integer vector, the selected circulants' squared output norms must sum to
   at most `4m` times its squared norm. A finite bank of integer vectors gives
   sound rejection certificates. It need not catch every Fourier PSD failure.
   The cheap order-three residue test is one exact direction already contained
   in the bank, so its early placement saves work without adding final strength.

4. **A safe filter is a necessary condition, not a completion theorem.** At
   core 7, even a three-sequence tuple with a positive-definite residual has no
   Williamson completion. Row sums, product parity, and energy bounds must be
   combined, and every accepted quadruple still receives exact correlation
   checks. This family is only one way to build a Hadamard matrix.

5. **False-negative controls are indispensable.** A valid core 9 tuple attains
   the PSD threshold exactly, so a `>=` rejection would be wrong. Negative
   normalized row sums and repeated blocks must survive. Filtered list ranks
   cannot replace original bitmasks. Independent checking preserved every one
   of 48 first-edition solutions and matched independent unfiltered moderate
   baselines at 19 and 21.

6. **A factor improvement is not an asymptotic breakthrough.** The implementation
   still enumerates all `2^((m-1)/2)` complete single sequences. At core 167,
   `2^83` remains prohibitive for this method. Measured pruning fractions at 21
   cannot be extrapolated to that order. We stopped at the complete moderate
   demonstration and documented the remaining exponential barrier.

Worthwhile next projects would be: a sound partial-assignment energy bound that
allows cancellation by unknown signs; compressed enumeration with every lift
accounted for; or a larger, explicitly defined family with a constructive
existence argument. Each needs its own proof and complete small-domain audit.
Merely increasing the brute-force bound would not answer the structural problem.

See the [report](README.md), [proofs](PROOFS.md), [validated data](data/validated-solutions.json),
and [independent review](reviews/independent-review.md). No global nonexistence,
new universal construction, complete Fourier oracle, or Lean result is claimed.
