# Round-three source ledger and derived criteria

Checked **2026-10-15 (UTC)**. Earlier editions are preserved. External documents
and code were inspected as text only; no external program was executed.

## Pinned disk-covering sources

Benchmark revision:
[`pikaaa345/disk-covering-benchmark@122ba78c748303f4d590d20c7df16630dba51fd2`](https://github.com/pikaaa345/disk-covering-benchmark/tree/122ba78c748303f4d590d20c7df16630dba51fd2),
committer date **2026-10-05 17:47:50 UTC**, MIT license. Hashes below were
computed on the retrieved raw bytes, preserving line endings. They identify the
documents reviewed; they do not verify the mathematics described in them.

| Public path at that revision | Bytes | SHA-256 |
| --- | ---: | --- |
| `docs/record-n25-astra-20261002.en.md` | 16575 | `dba69e76221bcad935bc9d64952b84a383b1c4fa700ca9eb6360050d8d05582f` |
| `docs/record-n25-sol-20261002.en.md` | 9288 | `666e0d7f7d766ac05e8b7253bfe8b17f4a7754f99d945fec4c3a25bd2e758e9f` |
| `docs/record-n11-algorithm-run-20261001.en.md` | 5349 | `e701eeba2cc6bbeb86850d9c2db5812a78f34d26e2ed10c3b747bbfea398c2f1` |
| `docs/records.json` | 25074 | `92eaffcc7cd6dc2b6ef08e39544b754b73de779b5072cfbf5c7cf5a3c54a6bac` |
| `results/n12.json` | 14289 | `7d04531c60efc3853c48029bf30d4f798c26c4f1b29f4a500e31ec350ae7d4d0` |
| `results/n25.json` | 7876 | `97903ef80a9aa38c25942d4a3316ed5bc8f47aa65ead47fbd5f788d4d45a1267` |
| `docs/record-n12-deepseek-v4-pro-max-20261002.en.md` | 15029 | `830a0f32027de1e0e64ad2c22a1b91888a7a84b47d5520315a2d93345fcf8720` |
| `docs/record-n26-algorithm-run-20261001.en.md` | 5837 | `86daa26efadc34daba8a066cc5e74d882e610543ee37b6b15847e6c24351eb7e` |
| `docs/record-n26-algorithm-run-20261001.json` | 5559 | `87dac2b4b349f94fe4e1b9fa4ffb88e8025bb125e7c02d1068535b22a32e956c` |

At this revision, `docs/records.json` is an n=11 record collection, not an index
covering all cases. `results/n26.json` returns 404; use the named n=26 case files.
The older `results/n25.json` retains `candidate_upper_bound` in its Astra
fingerprint record, whereas the later public narrative records a corrected
reference label and the separate Sol acceptance. Preserve the versioned scope:
the Astra run's missing global proof is unaffected by the reference correction.

The benchmark's linked public mathematical antecedents are pinned to
[`VonEquinox/DiskCoveringSolve@089584973f41e6374ce110f6e5b5ee456df19352`](https://github.com/VonEquinox/DiskCoveringSolve/tree/089584973f41e6374ce110f6e5b5ee456df19352):

| Document | Bytes | SHA-256 |
| --- | ---: | --- |
| [n=20 proof, especially Section 5](https://github.com/VonEquinox/DiskCoveringSolve/blob/089584973f41e6374ce110f6e5b5ee456df19352/cover20/docs/r20_proof_zh.md) | 42483 | `ec4225ed1673e442f6b5d0557ea8a1d346c1aba684e5a34d05a636fe85f27139` |
| [n=12 proof](https://github.com/VonEquinox/DiskCoveringSolve/blob/089584973f41e6374ce110f6e5b5ee456df19352/cover12/docs/cover12_proof_zh.md) | 20865 | `3d84f69cc639a7f8fce9dcd95370bdcd44cd7f6ce29d060e2eb4665befa17d5a` |
| [general exact-algorithm theory, Sections 8–9](https://github.com/VonEquinox/DiskCoveringSolve/blob/089584973f41e6374ce110f6e5b5ee456df19352/theory/single_exponential_exact_algorithm_zh.md) | 30784 | `e90a5bb590921719263891276ecb4aa2f96d1d4ba1de944a46fdfd6dbb9807be` |

The documented lessons, limits, and the proposed Hadamard analogy are separated
in [DISK_LESSONS.md](DISK_LESSONS.md).

## Primary Williamson identities

[Bright, Kotsireas and Ganesh, *Applying Computer Algebra Systems with SAT
Solvers to the Williamson Conjecture*, arXiv:1804.01172v2](https://arxiv.org/html/1804.01172v2),
**2019-05-14**, CC BY 4.0: Corollary 13 supplies the row-sum identity; Theorem
14 credits Williamson's odd product theorem; Section 4.7 explicitly uses
initial-sign normalization and product constraints. The original odd product
result is attributed to [Williamson (1944)](https://doi.org/10.1215/S0012-7094-44-01108-7).

[Đoković and Kotsireas, *Compression of Periodic Complementary Sequences and
Applications*, arXiv:1302.0571v1](https://arxiv.org/html/1302.0571v1),
**2013-02-04**, journal version 2015: Theorems 2–3 establish Fourier and
compression preservation. The paper does not state the support-generation
filters below in this form. They are explicitly derived here without a novelty
claim.

## Before-generation support criteria derived from those identities

Write `m=2h+1` and normalize all four initial signs to `+1`. A target row sum
`r_X` fixes the number `k_X=(m-r_X)/4` of negatives in its `h` independent
positions. Each nonzero independent column has one or three negatives.

For two supports of sizes `k,l` on `g` positions, their possible Hamming
distances form the exact set

\[
T_g(k,l)=\{|k-l|,|k-l|+2,\ldots,\min(k+l,2g-k-l)\}.
\]

Four target counts on that group admit an odd-parity column table if and only if

\[
T_g(k_A,k_B)\cap\{g-t:t\in T_g(k_C,k_D)\}\ne\varnothing.
\]

Indeed, the mismatch sets of `A,B` and `C,D` must be complements. The distance
criterion is sufficient for this count-plus-product subproblem because supports
of fixed sizes can realize every distance in `T_g`, and a coordinate permutation
can place their mismatch set on any prescribed set of that size. It is only a
necessary condition for the full Williamson equations.

After full `A,B` are fixed, put `t=|{i:a_i!=b_i}|`. Product parity forces `D=C`
on those `t` positions and `D=-C` on the other `g-t`. The required numbers of
negative entries of `C` on the two parts are therefore

\[
p=(k_C+k_D-g+t)/2,\qquad q=(k_C-k_D+g-t)/2.
\]

Reject before generating `C` unless these are integers satisfying
`0<=p<=t`, `0<=q<=g-t`. Otherwise generate exactly those fixed-cardinality
supports and derive `D`. Apply this independently within every group whose
support counts have been fixed. This is a completion-preserving construction
rule, not a multiplier or symmetry restriction.

For general partially fixed cells, a reachability dynamic program over the eight
odd-weight four-bit columns and the four remaining row counts is exact for the
product-plus-count subproblem. Propagating the fourth sign once the other three
are fixed is its simplest local consequence.

## Coupling compression with support counts before signs are generated

At `m=21`, split the ten independent indices into `G0={3,6,9}` and the other
seven positions. Let each row have negative counts `k0,k1`, with `k=k0+k1`.
The residue sums modulo three are

\[
u_0=7-4k_0,\qquad u_1=u_2=7-2k_1.
\]

The exact frequency-seven Fourier equation becomes

\[
\widehat X(7)=2(k-3k_0),\qquad
\sum_X(k_X-3k_{0,X})^2=21.
\]

Thus enumerate group-count classes first, respecting
`max(0,k-7)<=k0<=min(3,k)`, the displayed equation, and the exact distance
intersection separately on groups of sizes three and seven. These conditions
can exclude whole classes before a single sign row is constructed. Retain all
surviving classes and check full PAF conditions on completed rows.

## Safe lower bounds during a sign assignment

For a fixed integer vector `v`, define
`w[j,i]=v[j-i]+v[j+i]`, with indices modulo `m`. Then

\[
(C_X^Tv)_j=v_j+\sum_{i=1}^h x_iw[j,i].
\]

Suppose an unfinished row must select exactly `t` further negatives from its
unknown index set `U`. Count unknown signs positively to form `b_j`; every
completion has component `b_j-2*sum_(i in M) w[j,i]`, where `|M|=t`.
The sums of the `t` smallest and `t` largest unknown weights bound that component
by an exact interval. Its squared distance from zero is a valid lower bound.
Alternatively use the exact cardinality-constrained subset-sum set and minimize
the squared component over it. Sum these bounds over coordinates and rows.
Reject only if the sum exceeds `4m*||v||^2`.

Taking separate minima for different coordinates relaxes their shared choices,
so the bound cannot remove a real completion. Fixing separate negative counts
in compression or product-parity strata can tighten it. Merely replacing
unknown signs by zero remains unsound. These bounds are our direct consequences
of the defining Gram identity, not newly located published theorems.

## Quaternion representation and the separate color/sign investigation

[Barrera Acevedo and Dietrich, *New infinite families of Williamson Hadamard
matrices*, Australasian Journal of Combinatorics 73(1), 207–219 (2019)](https://ajc.maths.uq.edu.au/pdf/73/ajc_v73_p207.pdf)
and [Bright, Kotsireas and Ganesh, *New Infinite Families of Perfect Quaternion
Sequences and Williamson Sequences*, arXiv:1905.00267v1](https://arxiv.org/html/1905.00267v1)
are primary background on the established connection. The former's Theorem 2.4
and Table 1 give the column/quaternion bijection, restated explicitly in the
latter's Section II-D, Theorem 1. The former's Proposition 3.2 and discussion on
page 212 describe the odd symmetric one-exceptional-coset form as quaternionic
Turyn sequences. These are classical representations relevant to this study.

The more recent [Bennett, Bright, Colinot and Nayak, *Quaternionic Perfect
Sequences and Hadamard Matrices*, arXiv:2601.22337v1](https://arxiv.org/html/2601.22337v1),
**2026-01-29**, gives a quaternion-perfect/Williamson-type correspondence in
Section 2.3, Theorem 4, over `Q_+=Q8 union qQ8`, with
`q=(1+i+j+k)/2`, and an enumeration algorithm. Its appendix includes symmetric
Williamson cases through length 21. The broader quaternion-type family must not
be identified with the symmetric family without checking the hypotheses.

The January 2026 paper's Section 3.2, Algorithm 1 enumerates sequence pairs and
matches correlation vectors. The four-color sign-reconstruction formula below
was not located there or in the two 2019 references during this bounded review.
That negative search result does not establish that the formula is unpublished.

## Four colors determine signs necessarily: separately checked derivation

Let the column at zero be `v0=(1,1,1,1)`. Product parity lets each other column
be written uniquely as `v_i=epsilon_i*w_(c_i)`, where
`w_c=(1,1,1,1)-2e_c`; extend colors and signs by reflection to all nonzero
indices. These four vectors satisfy `w_c dot w_d=4[c=d]` and
`v0 dot w_c=2`.

At lag `t!=0`, pair the terms of `sum_j v_j dot v_(j+t)` under
`j -> -j-t mod m`. Because `m` is odd, there is one fixed term contributing
four. The orbit incident with zero contributes `4*epsilon_t`. Each of the other
`h-1` orbits contributes eight times its signed same-color indicator. Therefore

\[
\frac{\sum_X\operatorname{PAF}_X(t)}4
=1+\varepsilon_t+
2\sum_{(u,v)\in E_t}\varepsilon_u\varepsilon_v[c_u=c_v].
\]

Here `E_t` is a **multiset of the remaining edge orbits**, after folding nonzero
indices by reflection. Keep an edge list so integer contributions and parity
reductions are not confused. The actual odd cyclic quotient has a path and
disjoint cycles of odd length, hence no parallel edges; composite lengths can
give cycles rather than a single path. Synthetic repeated-edge tests exercise
the more general list-based arithmetic without asserting such repeats occur
in these cyclic quotients.
For a solution the left side vanishes. Reduction modulo four gives the necessary
reconstruction

\[
\varepsilon_t=-(-1)^{\#\{(u,v)\in E_t:c_u=c_v\}}.
\]

Thus one may enumerate colors alone and reconstruct all signs. The formula is
necessary; reconstructed columns must still satisfy every full correlation
equation. Canonical restricted-growth color words quotient the four row
permutations, with exact count `sum_(k=1)^4 S(h,k)` for `h>0`, where `S` denotes
a Stirling number of the second kind. This is asymptotic to `4^h/24`; sequences
using fewer colors prevent treating that quotient as an exact count.

This algebra was independently checked within the team. It is presented as a
proved derivation in this study, with no claim of novelty or new classification.
The classical quaternion representation supplies context rather than a substitute
for the reflection-pairing proof.
