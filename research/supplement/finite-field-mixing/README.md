# Finite-field Fourier and product-sum mixing

The local five-product step in family025 can use **four products**.
For a prime p and H contained in F_p with h = |H| and h^4 >= p^3,
every residue is a sum of four products from H, and independent uniform
sampling gives each residue probability at least 1/p^2.

The general sufficient criterion is

    (p - 1) (sqrt(p) / h)^k < 1.

For different nonempty sets A and B, replace sqrt(p)/h by
sqrt(p/(|A||B|)). For different pairs A_i,B_i, the exact integer condition
is product_i(|A_i||B_i|) > (p - 1)^2 p^k. Nonzero coefficients and an
additive shift are allowed.

## Files

- `study.md`: self-contained orthogonality, Cauchy–Schwarz, Fourier,
  probability, count, and positive-divisor lifting proofs
- `theorems.json`: ten portable theorem records, FF001–FF010
- `counterexamples.md`: explicit hypothesis failures and scope boundaries
- `verify.py`: original exact-arithmetic checks, using only Python's
  standard library
- `certificates.json`: reproducible full-run evidence and exact examples
- `exact-tests.md`: readable exact small-prime tables and test scope
- `audit.md`: source, proof-interface, and verification audit
- `MANIFEST-SHA256.json`: hashes of the study artifacts

## Exact checks

Run `python verify.py` from this directory, or call it by absolute path.
The full suite checks all 141,477 nonempty diagonal sets for primes
2, 3, 5, 7, 11, 13, 17 and all 17,148 ordered rectangular set pairs for
primes 2, 3, 5, 7, at k = 1,...,6. It also checks 120,050 heterogeneous
pair sequences, 3,951 exact cyclotomic sum-of-squares identities,
coefficient/shift examples, counterexamples, and direct enumeration.
No floating-point Fourier calculation is used.

## Source and limits

The motivating source is [family025, prescribed.tex, lines 326–366](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/prescribed.tex#L326-L366),
pinned to revision fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb.
The bilinear estimate is classical and is recorded as Proposition 1.1
by [Glibichuk and Konyagin](https://arxiv.org/pdf/math/0702729).
No novelty or optimality claim is made.

Only the local rational-divisor lift changes: **four rational summands
instead of five per lifted prime**. No improved global
short-Egyptian-fraction constant is claimed. Repeated factors and
summands are allowed. These records are not Lean-verified or native MRS
objects, and finite checks are evidence rather than universal proofs.

An independent mathematical and computational review is saved separately
under `../reviews/finite-field-mixing/` when finalized.
