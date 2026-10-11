# Source and proof-interface audit

## Status

The local four-product replacement is valid. The general k-product
criterion, its rectangular and heterogeneous variants, exact count
form, and positive-divisor lift have self-contained ordinary proofs in
`study.md`. Exact finite tests passed before final packaging.

An independent reviewer separately checked the universal argument and
recomputed the exhaustive finite distributions using carry-free
polynomial integer encoding, rather than the author's convolution code.
Its final review and exact reviewed-file hashes are stored under
`../reviews/finite-field-mixing/` when finalized. No formal proof-assistant
verification is asserted.

## Provenance

- Family: 025, Short Egyptian fractions
- Revision: fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb
- Source: preprints/Short-Egyptian-fractions-September-25-2026/build/prescribed.tex
- Local source SHA-256:
  771d9da7e0181aad85eb620d4bacbb1726827db86249655850f0b63b20307432
- Manifest comparison: exact match
- Focus: lines 326–366 in the proof of lem:rational-divisor-supply
- Classical antecedent: Glibichuk–Konyagin, Proposition 1.1, checked in
  the primary manuscript at https://arxiv.org/pdf/math/0702729, page 2

The study preserves source attribution. The bilinear estimate is
classical, and this is a reusable proof study with a local tightening,
not a claim to a new theorem or an optimal covering bound.

## Mathematical checks

1. Character normalization: the transform is E[e_p(rZ)] and inversion
   includes exactly 1/p and the target phase e_p(-rt).
2. Bilinear estimate: Cauchy–Schwarz contributes |A|, orthogonality
   contributes p|B|, and uniform normalization divides by |A|^2|B|^2
   after squaring. The resulting modulus bound is sqrt(p/(|A||B|)).
3. Field cancellation: r != 0 and b != b' imply r(b-b') != 0. This is
   where the prime-field assumption matters.
4. Independence: both the uniform Cartesian-product law inside pairs
   and product independence across summands are stated explicitly.
5. Reality: the probability difference is bounded in complex modulus;
   no non-real Fourier coefficient is treated as an ordered real number.
6. Frequency count: exactly p-1 nonzero frequencies are retained.
7. Strict positivity: the general threshold is strict. At h^4 >= p^3,
   four products have error factor <= (p-1)/p < 1 and probability
   at least 1/p^2 at every residue.
8. Integer-only criterion: product_i(|A_i||B_i|) > (p-1)^2 p^k is exactly
   equivalent to the nonnegative radical criterion.
9. Set-theoretic interpretation: positive finite probability implies a
   witness; repetitions and zero residues are allowed.
10. Rectangular extension: neither A=B nor a subgroup property is used.
11. Coefficients and shifts: nonzero c_i preserve nonzero frequencies;
    an additive shift contributes only a modulus-one factor.
12. Probability versus existence: nonuniform positive full-support
    weights preserve possible sums but need not preserve the bounds.

## Local lifting audit

The source sets H to the residue image of a collection of positive
divisors. It then samples H uniformly and only afterward chooses positive
representatives. This order avoids a multiplicity-weighting ambiguity.

If a,b divide Q, their product divides Q^2 because
Q^2/(ab) = (Q/a)(Q/b) is a positive integer. A lifted zero-sum is a
positive integer multiple of p. Its multiplier t is unrestricted, and
p = sum_i e_i/t follows. Four products satisfy every one of these local
requirements. Zero residues and repeated products are harmless.

The quantified saving is one rational summand per lifted prime, from
five to four (20% locally), with eight factor slots rather than ten.

## Exclusions

This work does not audit or certify:

- The exceptional-prime estimate or its global use
- Quantitative three-prime asymptotics or uniform threshold management
- Grouping the remaining numerator
- Distinct unit-fraction cleanup or padding
- Any final Egyptian-fraction term bound or improved global constant
- Any source-wide Lean status, proof-assistant build, or comparator check
- Native MRS schema compatibility or admission

The source's independently mentioned three-product result at a stronger
threshold is context only; it is not used to establish the four-product
proof here. Four is not claimed optimal.

## Computation and records

`verify.py` is original code using the Python standard library only.
It does not download or execute repository code, install dependencies,
or use floating-point complex exponentials. It records the source hash
and its own program hash in `certificates.json`.

The full suite enumerates 141,477 nonempty diagonal sets and 17,148
ordered rectangular pairs, with k from 1 to 6, plus 120,050 heterogeneous
sequences and 3,951 exact cyclotomic sum-of-squares identities. It checks
the exact representation-count inequality, the strict criterion, and
the four-product lower bound where applicable. Independent direct
enumeration and coefficient/shift cases supplement those suites.

The ten theorem records use a provisional portable JSON format with
explicit hypotheses, dependencies, proof locations, source links, and
verification limits. They are not executable proof objects. Finite
computations remain checks; the universal claims rest on the written
proofs.
