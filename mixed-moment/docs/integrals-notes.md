> Historical source review: mathematical statements and verdicts are retained. Quoted hashes identify the original supplied files, which may differ from privacy-normalized public receipts. Original/public hashes are recorded in `publication/SOURCE-MAP.json`; fresh publication checks are separate.

# Actual M integrals and their convergence

`MixedMoments/Integrals.lean` defines the actual Lebesgue integrals in namespace
`MixedMoments.Analysis`. It does not define the integrals to equal the rational
arrays or their series.

The definitions are

\[
w(t)=\frac{|t|}{\sqrt{1-t^2}},\quad
m_i=\int_{-1}^{1} w(t)t^i\,dt,\quad
M(i,j)=\int_{-1}^{1}\int_0^1
   \frac{w(t)t^i s^j}{1-ts}\,ds\,dt.
\]

Lean's square root and division are total functions, so these expressions also
assign values at the endpoints. Endpoints have zero Lebesgue measure. The file
explicitly proves agreement of the iterated interval integral with the product
integral on the open rectangle, rather than silently interchanging integration
orders.

## Unconditional single-moment results

`intervalIntegrable_positive_weight` and `integral_positive_weight` show that
\(t/\sqrt{1-t^2}\) is integrable on \([0,1]\), with integral \(1\).
The proof applies automatic integrability of nonnegative derivatives to
\(-\sqrt{1-t^2}\), which is continuous through the endpoint singularity.

Reflection and multiplication by continuous bounded powers then prove:

- `intervalIntegrable_weight` and `intervalIntegrable_moment`;
- `moment_reflection` and `moment_odd`;
- `moment_zero`, `moment_one`, and `moment_two`;
- `moment_recurrence`:
  \((i+3)m_{i+2}=(i+2)m_i\);
- `moment_eq_rat`: the actual \(m_i\) equals the real cast of the independently
  defined rational `MixedMoments.moment i`;
- `moment_rational` and `moment_tendsto_zero`.

The recurrence follows from the derivative of
\(t^{i+2}\sqrt{1-t^2}\) on \((0,1)\). Its derivative is proved integrable using
the already established single-moment integrability. Its continuous primitive
vanishes at both endpoints, so the fundamental theorem of calculus applies.
The decay theorem follows from the rational sequence's proved square bound
after the integral-to-rational identification.

## Absolute convergence and the series exchange

The file also defines the absolute moments

\[
b_i=\int_{-1}^{1}w(t)|t|^i\,dt
    =2\int_0^1\frac{t^{i+1}}{\sqrt{1-t^2}}\,dt.
\]

`absoluteMoment_eq`, `absoluteMoment_nonneg`, and
`absoluteMoment_recurrence` prove this representation, nonnegativity, and the
same two-step recurrence as the signed moments. The generic theorem
`MixedMoments.Series.summable_momentSeries` then proves

\[
\sum_{u\ge0}\frac{b_{i+u}}{j+u+1}<\infty.
\]

`integrable_monomial` and `integral_norm_monomial` identify these terms as the
integrals of the norms of the geometric-series monomials on the product
rectangle. This is the needed absolute-series justification on the negative
half of the domain.

For clarity, an explicit nonnegative majorant is defined:

\[
\frac{w(t)|t|^i s^j}{1-|t|s}.
\]

`integrable_absoluteKernel` proves its integrability by its nonnegative
geometric expansion and the preceding summability result. The pointwise bound
`norm_productKernel_le_absoluteKernel` then proves
`integrable_productKernel`. This handles the corner singularity without a
conditional convergence claim.

The resulting unconditional identities are:

- `intervalIntegrable_outer_slice`: outer integrability for every natural
  pair of indices;
- `M_eq_productIntegral`: the iterated integral equals the product integral;
- `M_eq_swappedIntegral`: the two interval-integration orders agree;
- `M_eq_series`:
  \(M(i,j)=\sum_{u\ge0}m_{i+u}/(j+u+1)\);
- `M_eq_rationalMomentSeries`: the same series uses the real casts of the
  independently defined rational moments;
- `M_diagonal`:
  \(M(i,j)-M(i+1,j+1)=m_i/(j+1)\);
- `M_finite_diagonal`: the finite telescoping form of that recurrence;
- `M_minus_boundary_recurrence` and `M_plus_boundary_recurrence`;
- `M_one_zero`, `M_zero_two`, and `M_two_zero`:
  \(M(1,0)=2\), \(M(0,2)=2\), and
  \(M(2,0)=1+M(0,0)/2\).

`M_diagonal_of_intervalIntegrable` is retained as a more general intermediate
interface with explicit outer-integrability hypotheses. The stronger
`M_diagonal` discharges those hypotheses within this file.

## Boundary-evaluation interfaces

`pairedSlice01`, `M_zero_one_eq_paired`, and
`intervalIntegrable_pairedSlice01` expose the reflection pairing needed for the
zeta boundary:

\[
M(0,1)=\int_0^1\int_0^1
\frac{2(t/\sqrt{1-t^2})s}{1-t^2s^2}\,ds\,dt.
\]

The analogous `pairedSlice00` interfaces expose the Catalan boundary, and
`pairedSlice00_eq_log`, `intervalIntegrable_logMarginal00`, and
`M_zero_zero_eq_logIntegral` identify the integrable marginal as

\[
M(0,0)=\int_0^1
\frac{\log(1+t)-\log(1-t)}{\sqrt{1-t^2}}\,dt.
\]

The actual boundary evaluations \(M(0,0)=4G\) and
\(M(0,1)=\tfrac32\zeta_2\) are separate declarations owned by the boundary
modules. They are not assumptions of the convergence and recurrence results
listed above. This file also does not establish the conversion from an
analytic big-O Taylor-contact hypothesis to finite coefficient contact.

## Actual polynomial integrals

`polynomialColumn P j` is the product integral of
\(w(t)P(t)s^j/(1-ts)\), with rational coefficients evaluated by the canonical
cast into the reals. `integrable_columnKernel` proves absolute integrability;
`polynomialColumn_eq_sum` proves its finite expansion in actual \(M(i,j)\);
`polynomialColumn_eq_iterated` recovers the source's iterated notation.

The corresponding definitions and theorems `polynomialKernel`,
`polynomialIntegral`, `integrable_polynomialKernel`,
`polynomialIntegral_eq_sum`, and `polynomialIntegral_eq_iterated` allow genuine
polynomials in both variables. These extensions require no further
integrability or boundary-evaluation assumptions.

## Verification

The development uses Lean 4.24.0 and mathlib revision
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. Compile with

```sh
bash scripts/with-lean.sh lake env lean MixedMoments/Integrals.lean
```

No `sorry`, `admit`, new axiom, or `native_decide` is used. The moment and
integral results above are proved from the actual integrands and standard
measure-theoretic and calculus results in mathlib.

`lake build MixedMoments.Integrals` succeeds. Dependency inspection with
`#print axioms` for the moment identification, integrability, series identity,
diagonal recurrence, both rational low values, logarithmic marginal, and both
polynomial expansions reports only the standard Lean axioms `propext`,
`Classical.choice`, and `Quot.sound`.
