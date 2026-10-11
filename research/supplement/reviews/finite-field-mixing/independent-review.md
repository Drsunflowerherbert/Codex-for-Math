# Independent review: finite-field product-sum mixing

Review date: 2026-10-11 (UTC).

## Verdict

**The mathematics passes independent review.** For a prime `p`, a nonempty
subset `H` of the prime field, and eight mutually independent uniform samples
`X_1,Y_1,...,X_4,Y_4` from `H`, the hypothesis `|H|^4 >= p^3` implies

\[
\Pr\bigl(X_1Y_1+\cdots+X_4Y_4=t\bigr)\ge 1/p^2
\]

for every residue `t`. Consequently every residue is a sum of four products,
with repetitions allowed. The rectangular and heterogeneous versions stated in
the study also pass. The positive-divisor lifting argument is valid.

No mathematical correction was needed. Two control characters and inconsistent
inline-math delimiters were reported during review; the study author corrected
them, and the corrected draft was rechecked. Final-file integrity is recorded
separately in the review manifest.

This review establishes no global Egyptian-fraction theorem improvement, no
optimal product count, no novelty claim, and no Lean or proof-assistant result.
The exact computations are finite regression evidence supplementing the
ordinary proofs.

## Mathematical audit

### 1. Probability and Fourier normalization

The sample space is the Cartesian product of the factor sets with its uniform
probability measure. Thus the factors inside each pair are independent, and so
are the products across pairs. The induced product distribution is generally
not uniform on its set of values.

The convention is `mu_hat(r) = E e_p(rZ)`, not a separately normalized transform
of a counting function. In particular `mu_hat(0)=1`. The inverse formula is

\[
\Pr(Z=t)=p^{-1}\sum_{r\in\mathbb F_p} e_p(-rt)\widehat\mu_Z(r).
\]

Its sign and factor `1/p` agree with character orthogonality. Taking
expectations of the point-mass indicator identity proves the formula directly,
so no convention is imported implicitly.

### 2. Orthogonality and the field hypothesis

For `d=0`, the character sum over the field is `p`. For `d!=0`, it is the
geometric sum of all powers of a nontrivial `p`th root of unity and is zero.

In the bilinear estimate the off-diagonal term is `r(y-y')`. Its nonvanishing
uses that the modulus is prime and `r!=0`. Orthogonality on a composite cyclic
group alone does not justify this inference. The modulus-16 counterexample in
the study correctly distinguishes these statements.

### 3. Bilinear Cauchy–Schwarz estimate

For nonempty `A,B`, put `a=|A|`, `b=|B|` and
`T_x = sum_(y in B) e_p(rxy)`. Cauchy–Schwarz gives

\[
\left|\sum_{x\in A}T_x\right|^2
\le a\sum_{x\in A}|T_x|^2
\le a\sum_{x\in\mathbb F_p}|T_x|^2
= pab.
\]

The final equality has exactly `b` diagonal pairs, each contributing `p`.
Dividing the unnormalized sum by `ab` gives

\[
|\widehat\mu_{XY}(r)|\le\sqrt{p/(ab)}.
\]

For `A=B=H`, this is `sqrt(p)/|H|`. There is no missing factor of `p`, `a`,
or `b`. The optional minimum with 1 is valid but unnecessary for the stated
sufficient criterion.

The study's algebraic sum-of-squares identity has the correct coefficients:

\[
pab-|S|^2
=a\sum_{x\notin A}|T_x|^2+
  \sum_{x<x',\ x,x'\in A}|T_x-T_{x'}|^2.
\]

Its right side is nonnegative at the specified complex root of unity. The
independent checker also verifies all 3,951 stated small-prime identities by
sparse group-ring arithmetic, without importing the study's implementation.

### 4. Convolution and pointwise lower bound

Independence makes the characteristic function of a sum the product of the
individual characteristic functions. Separating frequency zero leaves exactly
`p-1` nonzero frequencies. If their individual moduli are at most `beta_i`, then

\[
\left|\Pr\left(\sum_iU_i=t\right)-1/p\right|
\le (p-1)p^{-1}\prod_i\beta_i.
\]

The triangle inequality applies to the entire complex remainder. No comparison
of a complex coefficient with a real number is used. A fixed shift changes
only a unit-modulus phase; multiplying a product by a nonzero coefficient
permutes its nonzero frequencies. Zero coefficients must be removed before
applying the effective-product threshold, as the study states.

### 5. Exact sufficient criterion

For `k>=1` independent products from fixed `A,B`, with `N=|A||B|`, the criterion

\[
(p-1)\bigl(\sqrt{p/N}\bigr)^k<1
\]

is exactly equivalent to `N^k > (p-1)^2 p^k`. For diagonal sets it is equivalent
to `|H|^(2k) > (p-1)^2 p^k`. These are exact reformulations of this sufficient
Fourier criterion, not necessary-and-sufficient conditions for actual coverage.
Strictness matters: the rectangular characteristic-two example attains a
zero lower bound while missing a residue.

For heterogeneous pairs, the total tuple count is
`M=product_i(|A_i||B_i|)`. The stated squared count bound

\[
(pC_t-M)^2\le(p-1)^2p^kM
\]

is obtained by multiplying the probability bound by `pM` and squaring
nonnegative quantities. The normalization and total `sum_t C_t=M` are correct.

### 6. Four products and the endpoint

For fixed `A,B`, four powers of the coefficient bound give `p^2/N^2`. If
`N^2>=p^3`, then

\[
\Pr\left(\sum_{i=1}^4X_iY_i=t\right)
\ge\frac{1-(p-1)p^2/N^2}{p}
\ge\frac{1-(p-1)/p}{p}=\frac1{p^2}.
\]

The positive gap comes from retaining `p-1` frequencies. Replacing that count
by the looser value `p` would conceal the endpoint margin. For `A=B=H`, the
hypothesis is `|H|^4>=p^3`. The strict Fourier criterion actually needs only
`|H|^4>(p-1)p^2` for four products.

The asserted non-strict density hypothesis is valid. Equality `h^4=p^3` has
no integer solution for prime `p`, so it adds no realizable set size beyond
the strict version. The proof works for `p=2` as well.

### 7. Positive-divisor lifting

Let `D` be a nonempty set of positive divisors of a positive integer `Q`, and
let `H` be its residue image. A zero-sum tuple of products from `H` can be
lifted one factor at a time to positive elements of `D`. Each lifted product
`e_i=a_i b_i` divides `Q^2`, since
`Q^2/e_i=(Q/a_i)(Q/b_i)` is a positive integer.

The congruence gives `p | sum_i e_i`. Positivity and `k>=1` ensure
`t=(sum_i e_i)/p` is a positive integer, and consequently
`p=sum_i e_i/t`. Residue collisions, zero residues, and repetitions cause no
problem. The lifting argument does not require the divisor map to be
injective or the divisor set to be squarefree. Uniform sampling is on the
residue image, so unequal numbers of divisor lifts per residue do not alter
the probabilistic premise.

This proves a local change from five to four rational summands per lifted
prime in the motivating passage. It does not verify the manuscript's separate
prime supply, prime grouping, even case, distinctness, padding, or later
unit-fraction conversion. No global asymptotic constant is certified here.

## Independent exact computations

`independent_check.py` is original standard-library Python. It neither imports
nor executes `finite-field-mixing/verify.py`. Its main counting method encodes
an ordinary product-count polynomial in a power-of-two base, raises the
encoded integer to the required power, extracts its carry-free coefficients,
and folds exponents modulo `p`. The base exceeds the total tuple count, so
ordinary polynomial coefficients cannot carry into adjacent positions. This
is computationally distinct from the study's cyclic-convolution recurrence.

The completed independent checks include:

- Every nonempty `H` for `p=2,3,5,7,11,13,17`: 141,477 sets, each for `k=1..6`.
- Every ordered nonempty pair `A,B` for `p=2,3,5,7`: 17,148 pairs, each for
  `k=1..6`.
- Every recorded guaranteed-set count, criterion-failure coverage count,
  four-product minimum and witness, dense minimum probability, and threshold.
- All ordered sequences of two and three rectangular pairs over the field
  with three elements: 120,050 sequences. The independent audit additionally
  applies alternating coefficients 1 and 2 and a shift of 1, testing the
  heterogeneous coefficient/shift extension explicitly.
- All 346 coefficient-vector/shift cases over the fields with 2, 3, and 5
  elements in the final expanded study certificate.
- All 3,951 small-prime sum-of-squares identities, with character
  orthogonality checked directly in their group-ring representation.
- Direct enumeration of the four selected tuple spaces, totaling 16,161
  tuples; all exact count arrays agree.
- The eight example and counterexample records, including the composite
  modulus, both independence failures, strict-boundary failure, sufficient
  criterion not necessary, small-set obstruction, nonuniform weights, and
  positive-divisor lift.
- Every row of the 13-prime threshold table, using only integer inequalities.
- The study verifier's hash against its certificate and the local motivating
  source against the catalog manifest.

The nonuniform example correctly yields a nonzero Fourier coefficient `79/80`,
which exceeds `1/sqrt(5)`. It refutes a uniform-cardinality quantitative bound,
not qualitative full-support coverage. The divisor example has `Q=30`, `p=7`,
products `1,1,2,10`, positive denominator 2, and sum exactly 7.

The independent checker can be rerun with:

```sh
python reviews/finite-field-mixing/independent_check.py
```

The complete machine-readable outcome is `independent-results.json`.

## Provenance and literature scope

The motivating local source is the proof passage in `build/prescribed.tex`,
lines 326–366, at pinned revision
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`:

[OpenAI/math pinned passage](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/prescribed.tex#L326-L366).

Its full local file SHA-256 is
`771d9da7e0181aad85eb620d4bacbb1726827db86249655850f0b63b20307432`,
matching the catalog and the study certificate. The passage explicitly uses
five independent products and positive divisor lifts.

I also independently read page 2 of the primary
[Glibichuk–Konyagin manuscript](https://arxiv.org/pdf/math/0702729). Proposition
1.1 supports the rectangular bilinear estimate. That page states a known
three-product covering result under `|H|>p^(3/4)+1`. The study correctly avoids
asserting that four is optimal. This review did not undertake a complete
literature novelty search.

## Corrections and remaining limitations

Applied editorial corrections: remove a NUL and a backspace character; repair
inline-math escaping; spell out the expectation modulus in the FF002 record
to avoid an ambiguous use of “the latter.” No theorem statement or proof correction was required.

The findings concern the named files and hashes in the review manifest.
Subsequent edits require rechecking the affected conclusions. Neither the
study nor this review is a native theorem-database import, a Lean build, or an
external peer-review certificate.

## Final packet check

The final frozen study consists of nine files: `README.md`, `audit.md`,
`certificates.json`, `counterexamples.md`, `exact-tests.md`, `study.md`,
`theorems.json`, `verify.py`, and `MANIFEST-SHA256.json`. The independent
checker was rerun successfully against this exact final certificate. All ten
records FF001–FF010 pass review; their dependency references exist and form
an acyclic graph. The study's eight-entry manifest matches every covered file,
and all nine study files contain no unexpected control characters.

`artifact-validation.json` records these packaging checks.
`REVIEW_MANIFEST.json` hashes all nine final study files and the five review
artifacts, excluding itself to avoid self-reference. Rerunning a checker may
rewrite its result file; regenerate the manifest if a new snapshot is wanted.
