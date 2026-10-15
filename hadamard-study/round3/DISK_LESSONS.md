# What the disk-covering records actually teach

Review date: **2026-10-15 (UTC)**. The public benchmark was read at commit
[`122ba78c748303f4d590d20c7df16630dba51fd2`](https://github.com/pikaaa345/disk-covering-benchmark/tree/122ba78c748303f4d590d20c7df16630dba51fd2).
Only documents and JSON data were read. No downloaded solver or verifier was run.
The public reports describe mathematical reviews whose private evidence is not
available for independent replay here. This note separates those reports from
the mathematical pruning arguments that are publicly inspectable.

## The relevant n=25 comparison

The [specified Astra comparison](https://github.com/pikaaa345/disk-covering-benchmark/blob/122ba78c748303f4d590d20c7df16630dba51fd2/docs/record-n25-astra-20261002.en.md)
attributes Sol's advantage to finding cheap necessary conditions that exclude
whole topology classes and partial graph-generation branches. It records two
conditions incorporated around 1 h 53 min and 2 h 51 min; the reference-assisted
Astra repeat reached the first around 5 h 50 min and remained incomplete when
interrupted around 7 h 10 min. This supports a lesson about **where a criterion
acts**, rather than a general model ranking.

The [Sol report](https://github.com/pikaaa345/disk-covering-benchmark/blob/122ba78c748303f4d590d20c7df16630dba51fd2/docs/record-n25-sol-20261002.en.md)
names a necessary seven-spoke-wheel condition for the eight-interior-disk case.
It reports a completed catalogue and exact certificate replay. It withholds the
full proof, numerical answer and certificate archive. Neither report publishes
the formulas for both new cheap exclusions. We therefore cannot reproduce those
specific n=25 lemmas from these reports, and do not reconstruct them from timing
or hashes.

The original Astra run produced useful candidate coverage and local certificates,
but lacked global exclusion. The record does not say those local statements were
all false. Its matching answer fingerprint did not repair the missing proof.

## A public antecedent supplies the actual pruning mechanism

The comparison explicitly links
[VonEquinox's n=20 proof, Section 5](https://github.com/VonEquinox/DiskCoveringSolve/blob/089584973f41e6374ce110f6e5b5ee456df19352/cover20/docs/r20_proof_zh.md),
at commit `089584973f41e6374ce110f6e5b5ee456df19352`. It describes the following
necessary constraints and proves their safety for partial graphs:

- Boundary-angle gaps obey `0 <= g_i <= A` and `sum g_i = 1`.
- Already revealed center-edge paths bound distances between boundary anchors.
  Four- and six-rod paths yield angle alternatives `u <= C` or `u >= 1-C`.
- The long-arc alternative is removed only when a separate bound
  `k*A < 1-C` rules it out. Treating every oriented angle as a short arc would
  be unsound.
- The remaining inequalities have the form `u_j-u_i <= d_ij/10^7`.
  A negative directed cycle makes their sum read `0 < 0`, certifying
  infeasibility with integers.

Its decisive monotonicity argument is simple: every edge used in the partial
state is already forced to remain in every completed graph. Thus every derived
constraint remains necessary in every descendant. A contradiction removes the
entire branch before generating its completed graphs. This is an inspectable
antecedent, not a claim that these are precisely Sol's two unpublished n=25
improvements.

## A shared answer parameter does not remove search dimensions

The [public n=12 proof](https://github.com/VonEquinox/DiskCoveringSolve/blob/089584973f41e6374ce110f6e5b5ee456df19352/cover12/docs/cover12_proof_zh.md)
uses an algebraic candidate system with fourteen variables and separately handles
boundary-angle domains and competing topologies for its lower bound. An algebraic
radius, or a symmetric candidate construction, does not justify searching only a
one-dimensional family of possible covers.

Likewise, the [general exact-algorithm document, Sections 8–9](https://github.com/VonEquinox/DiskCoveringSolve/blob/089584973f41e6374ce110f6e5b5ee456df19352/theory/single_exponential_exact_algorithm_zh.md)
has one **free** radius parameter `t` but up to `19n+22` quantified variables.
Its complexity argument explicitly retains those eliminated variables. A common
parameter is a compatibility condition across the search, not a license to omit
geometric degrees of freedom.

## Failure and publication boundaries matter to the analogy

The [n=12 failed-submission review](https://github.com/pikaaa345/disk-covering-benchmark/blob/122ba78c748303f4d590d20c7df16630dba51fd2/docs/record-n12-deepseek-v4-pro-max-20261002.en.md)
reports an exact strictly better continuous cover, refuting the submitted optimum
without needing a proof of the true optimum. It also identifies a quantifier
error: a boundary-arc inequality involving `m` does not imply a stronger bound
obtained by substituting nine when `m >= 9`. A missing upper bound on the number
of boundary disks leaves branches unaccounted for. Finite allowed-center LP
calculations also require a justified reduction before becoming continuous-cover
obstructions.

The [n=11 algorithm-run report](https://github.com/pikaaa345/disk-covering-benchmark/blob/122ba78c748303f4d590d20c7df16630dba51fd2/docs/record-n11-algorithm-run-20261001.en.md)
describes fresh geometry feedback and two consumers binding to the same final
root source. It excludes algorithm development from measured runtime and inherits
source-admission and finite-classification trust. Those are useful workflow
requirements, not a publicly replayed global theorem here.

The [n=26 report](https://github.com/pikaaa345/disk-covering-benchmark/blob/122ba78c748303f4d590d20c7df16630dba51fd2/docs/record-n26-algorithm-run-20261001.en.md)
states that local review accepted the global-optimality proof while independent
review of the minimal-polynomial source remains pending. It is neither evidence
of a missed branch nor an independently completed full-contract audit. The
requested `results/n26.json` is absent at this pinned version; the cited case
report and its adjacent JSON are the available records.

## Proposed transfer to the Hadamard study

The transfer is mathematical organization, not a transplant of disk geometry.
For Hadamard matrices, a verified example settles one finite existence claim.
Failure of a symmetric circulant Williamson search excludes only that family;
we have no reduction of all Hadamard matrices to it.

Within this family, the useful analogue of a partial graph is a partial table of
four sign rows, with row-support counts and compressed residue counts fixed.
Published product and Fourier identities provide constraints that every
completion must retain. This motivates three genuinely earlier rejection points:

1. **Before any row is generated**, reject whole row-count/compression classes
   using exact product-parity reachability and compressed Fourier equations.
2. **After A and B but before C**, use their mismatch set to prescribe how many
   negative entries C must select in each stratum; generate only such supports
   and derive D from the product theorem.
3. **During a row assignment**, bound the minimum possible remaining quadratic
   energy using all allowed sign completions, rather than treating unknown signs
   as zero. A proven lower bound above the energy budget excludes every descendant.

For each proposed reduction the proof obligation is the same as for the public
disk antecedent: state an invariant shared by every descendant, prove the
contradiction using that invariant, and preserve every feasible class. Record
which classes or prefixes were eliminated and compare results with an independent
small-order enumeration. Regression agreement tests implementation; the written
necessity argument justifies the pruning.

The four-color representation supplies another structural reduction: a
reflection-pairing parity argument necessarily reconstructs the signs from the
colors. That argument and its exact row-permutation quotient are documented in
the companion source ledger. Reconstructed candidates still require the full
correlation equations. Established quaternion representations are relevant prior
art; neither a familiar representation nor a smaller measured search space
establishes novelty or exhaustive correctness.
