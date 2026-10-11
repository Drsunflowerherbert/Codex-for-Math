# Hypotheses and carefully qualified counterexamples

All constants and arrays use the conventions in `study.md`. In particular, no linear independence of \(1,G,\zeta(2)\) is assumed. A nonzero formal coordinate and a nonmembership assertion about an evaluated real number are different claims.

## 1 Omitting Taylor contact

Take \(P=0\), \(D=1\), and \(j=0\). Then

\[
 M(P,0)-\frac32Z(D,0)=-\frac32\zeta(2).
\]

The defect is \(-1\), so the designated \(\zeta(2)\)-coordinate is nonzero. This is an exact counterexample to automatic coefficient cancellation without contact.

It is **not** an established unconditional counterexample to membership in \(\mathbb Q+\mathbb QG\). Claiming it were would require ruling out a rational affine relation between \(G\) and \(\zeta(2)\), which this study does not do. Under the additional hypothesis \(G\in\mathbb Q\), the target becomes \(\mathbb Q\), and the displayed value is irrational by the classical irrationality of \(\zeta(2)=\pi^2/6\). That last irrationality fact is not a premise needed for the cancellation theorem and is not reproved here.

More generally, taking the zero polynomial \(P\) and \(D=t^j\) gives

\[
 M(P,j)-\frac32Z(D,j)
 =\frac32H_j^{(2)}-\frac32\zeta(2).
\]

## 2 Replacing j less than L by j at most L

Take \(P=1\), \(D=0\), \(L=1\). The contact condition holds because \(t/f(t)=O(t)\). At the excluded endpoint \(j=L=1\),

\[
 M(P,1)-\frac32Z(D,1)=M(i=0,j=1)=\frac32\zeta(2).
\]

The formal cancellation conclusion fails. A less notationally terse example is \(P=1\), \(D=t\), \(L=3\). Its first three entries are

\[
 4G-\frac32,\quad \frac32,\quad \frac54,
\]

but at \(j=3\) the entry is

\[
 \frac34\zeta(2)-\frac18.
\]

For every \(L\ge1\), the choice \(P=t^{L-1}\), \(D=0\) has contact of exact order \(L\) and a nonzero formal coordinate \(3/2\) at \(j=L\). Thus the strict range is sharp for the uniform coefficient-cancellation claim. The same nonmembership caution as in Section 1 applies.

## 3 Omitting the initial factor t in the contact condition

The wrong condition \(P/f-D=O(t^L)\) would be satisfied by \(P=D=1\), \(L=2\), since \(1/f-1=O(t^2)\). Nevertheless, at \(j=0\),

\[
 M(P,0)-\frac32Z(D,0)=4G-\frac32\zeta(2).
\]

The \(\zeta(2)\)-coordinate does not vanish. The factor \(t\) in the correct contact condition comes from the index \(j-i-1\) and cannot be dropped.

## 4 Changing the multiplier three halves

Take \(P=1\), \(D=t\), \(L=3\), and \(j=1\). Replacing \(3/2\) by any rational \(\lambda\) gives

\[
 M(P,1)-\lambda Z(D,1)
 =\lambda+(3/2-\lambda)\zeta(2).
\]

Thus \(3/2\) is the unique multiplier that cancels the designated coordinate for all matching polynomial pairs. For example, multiplier one leaves \(1+\zeta(2)/2\).

## 5 Dropping nonnegative integrability restrictions

Nonnegative integer indices are sufficient conditions, and not all are individually necessary for integrability. But they cannot simply be removed.

- For \(Z(-1,0)\), on \(0<t<1/2\), \(0<s<1/2\), the integrand is at least \(1/t\). The integral diverges.
- For the putative \(M(-2,0)\), on the same region the absolute integrand is at least \(1/t\). The integral diverges.
- Let \(P=t\), \(D=0\), \(L=2\), and try \(j=-1\). The contact condition holds, and \(-1<L\), but on \(1/2<t<3/4\), \(0<s<1/2\), the positive integrand is bounded below by a positive constant times \(1/s\). Thus the integral diverges. The missing lower bound \(j\ge0\) cannot be ignored.

There is a useful nuance: the \(M\)-integral at index \(i=-1\) does converge absolutely for \(j\ge0\). Near zero the factor \(|t|t^{-1}\) is bounded. Moreover

\[
 \frac{t^{-1}s^j}{1-ts}=t^{-1}s^j+\frac{s^{j+1}}{1-ts}
\]

and the first term integrates to zero in \(t\) after including \(|t|/f(t)\). Therefore this separately defined extension satisfies

\[
 M(-1,j)=M(0,j+1).
\]

This observation is consistent with, but not required by, the source's algebraic convention for \(M^0(-1,j)\). It would be incorrect to claim that every negative \(i\) makes \(M\) diverge.

## 6 Local analyticity alone does not replace the polynomial hypothesis

Allow the rational function

\[
 P(t)=\frac1{1-t^2},\qquad D(t)=t.
\]

It is analytic on \((-1,1)\), has rational Taylor coefficients at zero, and satisfies

\[
 tP(t)/f(t)-D(t)=t(1-t^2)^{-3/2}-t=O(t^3).
\]

However, for \(t\in(1/2,1)\), \(s\in(0,1/2)\), the positive \(M(P,0)\)-integrand is at least a positive constant times \((1-t)^{-3/2}\). Its integral diverges. Local contact says nothing by itself about endpoint integrability.

Boundedness or an appropriate integrable majorant would repair this analytic issue, but would not automatically recover the finite rational decomposition used in the theorem.

## 7 Keeping the rational target with arbitrary real coefficients

There is an unconditional, explicit two-input obstruction to extending the theorem to all real-coefficient polynomials while retaining the target \(\mathbb Q+\mathbb QG\).

Use the two choices

\[
 (P_2,D,L,j)=(\sqrt2\,t,0,2,0),\qquad
 (P_3,D,L,j)=(\sqrt3\,t,0,2,0).
\]

Both have the required contact. Since \(M(t,0)=2\), their entries are \(2\sqrt2\) and \(2\sqrt3\).

The three numbers \(1,\sqrt2,\sqrt3\) are rationally linearly independent. Indeed, squaring a hypothetical relation \(a+b\sqrt2+c\sqrt3=0\) with \(bc\ne0\) would make \(\sqrt6\) rational, and the cases \(bc=0\) reduce to the irrationality of \(\sqrt2\) or \(\sqrt3\). But \(\mathbb Q+\mathbb QG\) has rational dimension at most two. Hence these two entries cannot both belong to it.

Thus **at least one of these two explicit inputs is a counterexample** to the universal real-coefficient extension. No unsupported claim is made about which individual input fails. The correct extension changes the target to \(K+KG\) for coefficients in a specified subfield \(K\subseteq\mathbb R\).

## 8 Assuming symmetry of M

The kernel \(1/(1-ts)\) alone is symmetric, but the domain and weight defining \(M\) are not. In fact,

\[
 M(1,0)=2,\qquad M(0,1)=\frac32\zeta(2)>2.
\]

For the strict inequality one needs no irrationality fact: \(\zeta(2)>1+1/4+1/9=49/36\), so \((3/2)\zeta(2)>49/24>2\). By contrast, \(Z(i,j)=Z(j,i)\) really is symmetric.

## 9 Omitting the zero-extension convention

If \(c_z\) is evaluated by a gamma-function interpolation when \(z\) is negative or half-integral, rather than set to zero as specified, the decomposition becomes a different and generally false assertion. For example, \(M(1,0)=2\) has zero displayed \(G\)-coordinate because \(c_{1/2}\) is zero under the required convention. The convention does not claim that a gamma interpolation of \(4^{-z}\binom{2z}{z}\) vanishes there.

In a future implementation, define the kernel directly on integer differences using sign and parity tests. Do not encode it as a partially defined quotient at arbitrary real indices.

## 10 What is and is not necessary

- Vanishing of a single defect coefficient is necessary and sufficient for cancellation of that coordinate in the specified decomposition.
- Contact through order \(L\) is equivalent to simultaneous vanishing of the first \(L\) defect coefficients.
- Neither statement proves necessity for the evaluated number to belong to \(\mathbb Q+\mathbb QG\), because evaluation could have a nontrivial kernel.
- Nonnegative indices and polynomiality are convenient sufficient analytic hypotheses. The examples above identify failed broader statements without claiming that every relaxation fails.
