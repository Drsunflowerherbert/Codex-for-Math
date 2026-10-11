# Proof and normalization

For a prime `p`, the library uses `ZMod p` and the standard additive character
`ZMod.stdAddChar`. The Fourier convention is

\[
\widehat f(r)=\sum_x f(x)\chi(rx),\qquad
pf(z)=\sum_r\widehat f(r)\chi(-rz).
\]

The reusable inversion and convolution lemmas also accept an arbitrary
primitive complex additive character. Primitivity is discharged internally in
the principal mixing theorems.

For finite `A,B`, `bilinearSum χ A B r` is the sum over all ordered pairs.
`normalizedProductCoeff` divides by `|A||B|`. The theorem
`normalizedProductCoeff_eq_uniform_expect` identifies this value with the
uniform average over the Cartesian sample space `A × B`; the product values
retain their actual multiplicities. For nonzero `r`, orthogonality gives

\[
\sum_{x\in\mathbb F_p}\left|\sum_{b\in B}\chi(rxb)\right|^2=p|B|.
\]

Prime-field cancellation makes every off-diagonal frequency `r(b-c)`
nonzero. Cauchy–Schwarz on `A`, followed by extending the nonnegative energy
sum to the whole field, yields `|S|² ≤ |A|p|B|`. The normalized theorem is

\[
|\widehat\mu_{XY}(r)|\le\sqrt{p/(|A||B|)}.
\]

For the diagonal sampling set `H`, `productCount H z` counts pairs in
`H × H` whose product is `z`. Natural convolution counts the sums of
independent pairs. `convolutionCount_eq_tupleCount` proves that the recurrence
equals the event cardinality in the actual tuple sample space
`Fin k → ↥(H.product H)`. Its total size is proved to be `|H|^(2*k)`.
Consequently

\[
\operatorname{productSumProbability}(H,k,z)
=\frac{\#\{\omega:\sum_i\omega_{i,1}\omega_{i,2}=z\}}{|H|^{2k}}.
\]

This is uniform sampling on the Cartesian product, so all coordinates are
independent and uniform on `H`. It permits repeated samples and zero. The
library proves nonnegativity, total mass one for nonempty `H`, and equivalence
between positive probability and an actual product-sum witness.

Complex convolution of the normalized product density agrees exactly with
this count ratio. Its Fourier coefficients are powers of the one-product
coefficient. The zero coefficient is one and every nonzero coefficient has
modulus at most `(sqrt p / |H|)^k`. Separating the zero term in inversion
leaves exactly `p-1` frequencies. The triangle inequality yields

\[
\Pr(\textstyle\sum_{i=1}^kX_iY_i=z)
\ge\frac{1-(p-1)(\sqrt p/|H|)^k}{p}.
\]

This estimate is proved with no spectral estimate as an input hypothesis.
The strict inequality `(p-1)(sqrt p / |H|)^k < 1` gives covering. Under the
natural threshold `p³ ≤ |H|⁴`,

\[
(\sqrt p/|H|)^4=p^2/|H|^4\le1/p,
\quad
\Pr(\textstyle\sum_{i=1}^4X_iY_i=z)\ge1/p^2>0.
\]

The density threshold itself implies `H.Nonempty`; the four-product theorem
therefore needs only prime `p` and that threshold. Its conclusion uses
functions `a,b : Fin 4 → ZMod p` with every coordinate in `H` and
`∑ i, a i * b i = z`. There are no distinctness requirements.

The `k=0` definitions use the single empty tuple and its sum zero. The
probability lower-bound theorem remains valid for this additional case;
positive-covering criteria cannot be met at `k=0` for a prime modulus.

# Formal scope and evidence

The principal rectangular Fourier bound, diagonal `k`-product probability
bound, strict covering criterion, fourth-power probability bound, and
four-product witness theorem are Lean results. Generic finite Fourier,
complex convolution, natural counting, cast/normalization, and scalar
threshold lemmas are reusable independently.

The supplied study's broader heterogeneous-set/coefficient/shift results and
radical-free criterion equivalences are ordinary mathematical results in the
[already published study](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/finite-field-mixing/study.md);
the present main library does not claim their complete formalization.

The optional `DivisorLift.lean` applies four-product covering at residue zero
to the image modulo `p` of a finite natural-number set `D`. It lifts each
factor through the image map, so residue collisions cause no issue. If every
element of `D` is positive and divides a positive integer `Q`, the four
lifted products divide `Q²` and have positive sum. Their sum is divisible by
`p`, hence equals `p*m` for a positive natural multiplier `m`. The rational
identity is then `p = ∑ i, (a i*b i)/m`. This is a local lifting result with
repetitions permitted; it supplies no distinct unit fractions or global
denominator-length bound. The general-`k` lift remains ordinary-only.

`scripts/TheoremInventory.lean` prints every exported declaration's exact
type and axiom dependencies. The supplied final audit records a fresh build
of the project sources with the pinned compiler and mathlib revision. It
records that the source audit rejected proof placeholders and new axiom
declarations, and that only the standard Lean foundations `propext`,
`Classical.choice`, and `Quot.sound` appeared in the declaration audit.

Independent exact small-prime computations were recorded alongside the original
snapshot. They supplement the universal Lean proofs and do not establish the
universal statements themselves. The saved formal audit distinguishes ordinary
records from formal results. Publication review checked the receipt and source
hashes without rerunning the builds or computations. The original finite-test
checker, input archive, and some environment-specific receipts are omitted
from this public subset; historical references in the retained audit identify
the original run. See the project README and batch source map for the exact
publication boundary. No global Egyptian-fraction improvement or novelty is
asserted.

Publication note: source-location and evidence-packaging prose was edited for
public distribution. The mathematical argument above and all Lean library
sources are unchanged from the supplied completed snapshot.
