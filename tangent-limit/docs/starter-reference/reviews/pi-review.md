# Independent review of the tangent limit and series studies

Review date: 11 October 2026 UTC.

## Verdict

The written pointwise bridge and dyadic series arguments are valid ordinary mathematical deductions from the explicitly stated Diophantine hypothesis. The divergence statement for the absolute series at every real exponent at most one is valid without that hypothesis. This is a review of the new mathematical arguments and their stated inputs. It is not a Lean formalization, a Lean execution, or a verification of the imported proof of the irrationality exponent of pi.

Final artifact inventory and fingerprints are recorded below after the authors' last cleanup and the reviewer's source-locator correction. The acceptance applies to those exact reviewed versions.

## Exact source input

Write H for the following proposition:

For every real alpha greater than 2, there is an integer Q at least 2 such that every pair of integers p and q with q at least Q satisfies

|pi - p/q| >= q^(-alpha).

The quantifiers matter: Q may depend on alpha, but it is uniform over both p and q. Numerators are unrestricted integers, denominators need not be reduced, and denominators used in the conclusion are positive. Alpha equals 2 is excluded.

The reviewer independently inspected the repository's family 017 scope note, comparator target, Main.lean, Statement.lean, and comparator configuration through read-only GitHub retrieval. Main.lean states exactly H in the first conjunct of OAI.PiExponent.main. Statement.lean distinguishes the integer-denominator formulation from the natural-denominator formulation. The supremum characterization of the irrationality exponent is not needed by either study.

Primary references: [Main.lean at the inspected commit](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/PiExponent/Main.lean#L17-L27) and the [family 017 scope note](https://github.com/openai/math/blob/main/lean/docs/017.md).

The comparator target contains a placeholder proof; that is a target statement and is not the submitted proof. The configuration points to the solution module and allowed axioms, but reading the configuration is not running its verification. The separate Flint–Hills declaration in Main.lean is outside the selected comparator statement according to the scope note and is unused here. A catalog omission does not by itself refute a theorem or a separately executed verification.

Source URLs, retrieved source bytes, and Git blob identifiers are retained in this review directory. Those identifiers pin the inspected file contents; this reviewer did not execute the sources or audit their imported dependencies. Both studies supply a commit-pinned Main.lean reference, independently cross-checked by this reviewer. Each of the five stored source files exactly reproduces its official Git blob hash.

## Accepted pointwise claims

The bridge study works with the more general fixed-exponent assumption D(c, alpha, Q): c is positive, alpha is at least 2, Q is a positive integer, and |pi-p/q| is at least c q^(-alpha) for every integer p and every integer q at least Q.

1. The nearest-pole construction is correct. For n at least 1, q_n = 2 floor(n/pi) + 1 is positive and odd. Its distance from 2n/pi is less than one, and the pole distance d_n = |n-pi q_n/2| lies strictly between zero and pi/2. With A = 1+2/pi, q_n is at most A n. The specified onset n at least ceil(pi(Q+1)/2) safely guarantees q_n at least Q.

2. The exact conversion d_n = (q_n/2)|pi-2n/q_n| and the bound |tan n| = cot(d_n) <= 1/d_n are correct. The proof of the cotangent bound includes the endpoint pi/2. There is no reversal of the negative-exponent comparison.

3. The explicit eventual bound |tan n| <= (2/c) A^(alpha-1) n^(alpha-1) follows. Thus the scaled tangent limit is zero for every real s greater than alpha-1. The explicit tolerance threshold and the special choices of alpha in the study are algebraically correct.

4. Pointwise comparison alone proves absolute convergence when s is greater than alpha and gives the stated tail bound (2/c) A^(alpha-1) M^(-(s-alpha))/(s-alpha). The study correctly labels this sufficient threshold as non-sharp. A divergent harmonic majorant at s=alpha gives no divergence conclusion for the smaller series.

5. Globalization over small denominators is valid. The finite positive minimum of c and q^(alpha-1) dist(q pi, Z), for 1 <= q < Q, works for every numerator. An infinite minimum over numerators is unnecessary. If Q=1, the additional set is empty and c is retained.

6. The parity audit and the optional reduced-rational repair are correct. The growth proof uses even numerators and odd denominators. An odd common divisor preserves that parity on reduction, but a large unreduced denominator need not yield a large reduced denominator. The optional repair handles finitely many exceptional reduced rationals and nearby integers before returning to all integer pairs.

Under H these claims give |tan n| = O_epsilon(n^(1+epsilon)) for every positive epsilon and tan(n)/n^s -> 0 for every s>1. They in particular give the cubic scaled limit and absolute cubic-series convergence. They do not give a uniform exponent-two Diophantine constant, an O(n) growth bound, or an endpoint limit at s=1.

## Accepted sharper series claims

The series study proves more than the pointwise comparison, by controlling the number of terms close to poles in a whole dyadic block.

1. Fix alpha>2 and globalize H to |pi-p/q| >= c q^(-alpha) for all positive q, with 0<c<=1. Put delta_N = (c/2)(3N)^(1-alpha) for integer N>=1. The chosen nearest pole for any 1<=n<=2N has positive odd denominator q<=3N, so its distance d_n from n is at least delta_N.

2. For distinct n,m in that range, put h=|n-m|. A nearest multiplier r to h/pi can be chosen nonnegative, with r<=3N. If r=0, the circular separation is h>=1>=delta_N. If r>=1, the all-integer approximation bound applied to h/r gives circular separation at least c(3N)^(1-alpha)=2 delta_N. The separate zero case is essential and is present.

3. The spacing step legitimately uses numerators and denominators beyond the pole parity class. The study explicitly warns that a pole-only even/odd approximation bound does not automatically supply this argument.

4. Splitting signed distances around the pole into the two half-intervals is valid. On either side the first distance is at least delta_N and consecutive ordinary distances differ by at least delta_N. The j-th distance is therefore at least j delta_N. There is no assumption of independence or equidistribution.

5. The resulting bound is

   sum_(N<=n<2N) |tan n| <= (4*3^(alpha-1)/c) N^(alpha-1) H_N
   <= (4*3^(alpha-1)/c) N^(alpha-1)(1+log N).

   The block contains exactly N integers, the factor two safely covers its two sides, and the use of 1+log N includes N=1. This yields the claimed O_epsilon(N^(1+epsilon) log N) asymptotic for N>=2, or the stated globally valid 1+log N version.

6. For each fixed s>1 choose 2<alpha<s+1. The absolute weighted sum over the block [2^j,2^(j+1)) is at most a constant times (1+j log 2)2^(-j(s-alpha+1)). The positive exponent makes the sum over j converge. It follows that the absolute series converges for every s>1 under H.

7. The elementary bound |tan n|+|tan(n+1)|>=sin(1)>0 is correct. It follows directly from the sine subtraction identity, the triangle inequality, and |sin x|<=|tan x| when cosine is nonzero. Positive integer arguments are not poles because pi is irrational. Pairing 2m-1 with 2m gives an absolute weighted contribution at least sin(1)/(2m) when s=1, proving divergence. For every real s<=1, n^(-s)>=n^(-1), so the divergence extends to the full claimed range.

Thus, conditional on H, sum_(n>=1) |tan n|/n^s converges if and only if s>1. The implication from s>1 to convergence uses H. Divergence for s<=1 does not. No conclusion about conditional convergence of the signed tangent series for s<=1 follows from this review.

## Corrections and remaining boundaries

The initial bridge draft contained damaged inline math escapes; these were repaired and the final files contain no disallowed control characters. The series opening was clarified from an ambiguous use of "forward" to an explicit statement that s>1 implies convergence conditionally on H. Source locators in both studies were corrected against the exact raw Main.lean: the main declaration occupies lines 17–27, its H conjunct lines 18–20, and the Flint–Hills declaration lines 29–32. These were presentation and provenance repairs, not changes to the valid proof strategy. A serialization-added terminal newline was removed from each saved source copy, and exact Git blob hashes were then verified.

No mathematical blocker was found in the final complete proofs and structured records. The outstanding boundary is evidentiary: the imported H is not proved or independently formal-checked by these studies or this review. Ordinary proof acceptance must not be relabeled as Lean verification. No external MRS schema or ingestion endpoint has been supplied or tested, so structured records remain portable study records rather than a claim of successful MRS ingestion.

## Final artifacts reviewed

All six files below were reviewed in their final form. The two full proof texts and both mathematical record files were read for mathematical content; the final formatting and provenance changes were checked against the exact source. The 13 bridge records agree with their proofs. JSON parses; record and source references resolve; the dependency graph is acyclic; source ledgers agree; math delimiters are balanced; and every flag for new Lean verification remains false. These structural checks supplement, rather than replace, the ordinary mathematical review.

- pi-bridge/study.md
  SHA-256: 8d24f900a83f41b8ec55e582531b814ccf755c7a7e90175cf1f81f0a160ec1d8

- pi-bridge/theorem_records.json
  SHA-256: 33920382a79939a307012972c0bd2981f63798f3d7721138c0fe8ed6b9cbcb7b

- pi-bridge/sources.json
  SHA-256: 6282c78bdb576ed3ebbf442b5fd0418877e76c34b7f4910dc5dc261d13629e9b

- pi-bridge/validation.json
  SHA-256: 853f2caabf57d1ef4c53c718ffcbfee94acb39359ea0abd231089890a9b332bd

- pi-series/tangent-series-proof.md
  SHA-256: 39d0bf6532bedbcd5fa4e74e61717ebb52c7b404d9e31dac0d78ccb5f214e5ee

- pi-series/tangent-series-assumptions.json
  SHA-256: a873a191d41f1e1ab06c09ba8def945708974f318829d78adcbe05899e6eb556

Machine-readable review status and these fingerprints are also saved in pi-review-validation.json. There are no pending author repairs or unresolved mathematical gaps in the reviewed conditional arguments.
