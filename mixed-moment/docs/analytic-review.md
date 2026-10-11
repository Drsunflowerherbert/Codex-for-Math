> Historical source review: mathematical statements and verdicts are retained. Quoted hashes identify the original supplied files, which may differ from privacy-normalized public receipts. Original/public hashes are recorded in `publication/SOURCE-MAP.json`; fresh publication checks are separate.

# Independent analytic review

## Review status

This review distinguishes the ordinary mathematical argument in the supplied
study from claims established by the Lean development. The source review below
is complete. The declaration and dependency review will be updated after the
implementation has stabilized; no statement in this initial version certifies
an uninspected Lean declaration.

Reviewed sources are `study.md`, `audit.md`, and `lean-roadmap.md` in
`research/supplement/mixed-moments/`.
The study identifies its extracted original source by SHA-256
`3929650dfb36859d8f88281795d348043f903c41a70b0bf3598c21586a633852`.

## Mathematical findings

The scoped mixed-moment identities and the sufficient Taylor-contact
cancellation theorem are correct. Independent derivation reproduces the
following boundary values and recurrences, with natural-number indices:

\[
 M(0,0)=4G,\quad M(1,0)=2,\quad
 M(0,1)=\tfrac32\zeta(2),\quad M(0,2)=2,
\]

\[
 M(i,j)-M(i+1,j+1)=\frac{m_i}{j+1},
 \qquad
 m_i=\int_{-1}^1\frac{|t|t^i}{\sqrt{1-t^2}}\,dt.
\]

Here odd moments vanish, \(m_0=2\), and
\((k+3)m_{k+2}=(k+2)m_k\). In particular the moments are rational.
The boundary recurrences are

\[
 dM(d,0)=(d-1)M(d-2,0)+m_{d-2}+m_{d-1}\quad(d\ge2),
\]

\[
 (d-1)M(0,d)=(d-2)M(0,d-2)+\frac2{d-1}\quad(d\ge2).
\]

At \(d=2\), the second recurrence deliberately has zero coefficient on
\(M(0,0)\). Thus its positive even branch is rational; it does not retain
the Catalan boundary contribution.

The series for the unweighted moment is

\[
 Z(i,j)=\sum_{n\ge0}\frac1{(n+i+1)(n+j+1)}.
\]

Its diagonal is \(\zeta(2)-H_i^{(2)}\), and its off-diagonal is
\((H_i-H_j)/(i-j)\). In particular \(Z(0,1)=1\); this checks the
partial-fraction sign.

Writing \(c_r=4^{-r}\binom{2r}{r}\), the designated zeta coordinate of
\(M(i,j)\) is zero except when \(j-i=2r+1>0\), when it is
\(\tfrac32c_r\). The designated Catalan coordinate is zero except when
\(i-j=2r\ge0\), when it is \(4c_r\). The remaining coordinate is
rational. These are specified coordinates, not a uniqueness statement about
representations of real numbers.

For rational polynomials \(P=\sum p_i t^i\), \(D=\sum d_i t^i\), the
zeta coordinate of \(M(P,j)-\tfrac32Z(D,j)\) is

\[
 \frac32\left(\sum_i p_i c_{(j-i-1)/2}-d_j\right).
\]

The kernel \(c_{a/2}\) means zero for a negative or odd integer \(a\).
It must not be implemented by unguarded truncated natural subtraction.
The parenthesized expression is the degree-\(j\) Taylor coefficient of
\(tP(t)/\sqrt{1-t^2}-D(t)\). Analyticity near zero makes the stated
big-O contact of order \(L\) imply its vanishing for \(j<L\), including
for one-sided contact with the filter stated explicitly.

## Integrability and interchange obligations

The singular corner \((1,1)\) is integrable in two dimensions. However,
the unweighted section at exactly \(t=1\) is not integrable in \(s\).
Fubini therefore supplies integrability of sections almost everywhere, not
at every outer variable. Assigning arbitrary values on the endpoint lines
does not affect the product integral or the justified iterated integral.

In Lean, inverse and real square root are totalized. Their values at singular
endpoints do not eliminate the need for an integrability proof. Pointwise
identities involving positive square roots and geometric expansions should
be established on the open rectangle and transferred almost everywhere.

The study's logarithmic majorant proves absolute integrability correctly.
There is also an alternative product majorant convenient for formalization.
For \(0\le u<1\), \(0\le s<1\), put
\(a=1-u\), \(b=1-s\), \(d=1-us\). Then \(a,b,d>0\),
\(a\le d\), and \(b\le d\). Monotonicity of negative real powers gives

\[
 d^{-1}=d^{-1/4}d^{-3/4}\le a^{-1/4}b^{-3/4}.
\]

Also \(u/\sqrt{1-u^2}\le a^{-1/2}\), so

\[
 \frac{u}{\sqrt{1-u^2}(1-us)}
 \le (1-u)^{-3/4}(1-s)^{-3/4}.
\]

Both factors are integrable at their endpoints. Reflection in \(t\)
extends this estimate to \(u=|t|\). All monomial factors have absolute
value at most one on their integration domains. Boundedness of polynomial
factors extends the domination to polynomial moments. For \(Z\), the
simpler majorant \((1-t)^{-1/2}(1-s)^{-1/2}\) suffices.

This proof requires no weighted arithmetic-geometric-mean theorem.
In mathlib v4.24.0 the relevant inspected declarations include
`Real.rpow_le_rpow_of_nonpos`, `Real.rpow_add`,
`intervalIntegral.intervalIntegrable_rpow'`,
`intervalIntegral.integrableOn_Ioo_rpow_iff`,
`MeasureTheory.Integrable.mul_prod`, and `Integrable.mono'`.

The same majorant controls the sum of absolute geometric-series terms for
\(M\). Pointwise convergence alone does not justify exchanging this signed
series with an integral on the negative half of the domain. For \(Z\),
Tonelli applies because all geometric-series terms are nonnegative.
Inspected exchange APIs include `MeasureTheory.integral_tsum` and
`MeasureTheory.integral_tsum_of_summable_integral_norm`, with their actual
integrability/summability premises retained.

Finite telescoping identities for boundary recurrences must retain their
tail terms until \(m_n\to0\) is proved. The study correctly supplies that
limit by dominated convergence. Rationality of the moments alone would not
imply the limit.

## Arithmetic scope and regression obligations

No step needs irrationality of Catalan's constant or linear independence of
\(1,G,\zeta(2)\). A nonzero designated zeta coordinate proves failure of
that formal cancellation; it does not prove that the evaluated real number
lies outside \(\mathbb Q+\mathbb QG\).

For \(P=1\), \(D=t\), and \(L=3\), the contact hypothesis holds and the
first three corrected entries are
\(4G-3/2\), \(3/2\), and \(5/4\). At the excluded endpoint \(j=3\),
the entry is \(3\zeta(2)/4-1/8\), with nonzero designated zeta coordinate.
This checks the strict bound \(j<L\), not unconditional nonmembership.

## Lean acceptance checks pending implementation

The final review must inspect theorem types and transitive dependencies,
not only names and successful compilation. In particular:

1. Actual Lebesgue integrals must be linked to the rational arrays before an
   unconditional theorem about the integrals is reported.
2. A theorem assuming integral decomposition, boundary evaluations, or
   integrability remains conditional on those hypotheses unless they are
   separately discharged.
3. A coefficient-contact interface is a valid algebraic result, but is not
   by itself a proof of the source's analytic big-O interface.
4. All denominators and natural/integer index transitions need their stated
   range conditions, particularly the two exceptional plus-boundary starts.
5. The inspected target declarations should have no admitted proofs or
   extra mathematical axioms. The usual Lean logical axioms must be
   distinguished from unproved assumptions added by the project.
