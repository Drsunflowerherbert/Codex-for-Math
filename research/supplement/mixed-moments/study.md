# Mixed moments and Taylor contact cancellation

## Conclusion and scope

The mixed-moment identities in the specified source are correct under their stated nonnegative-index conventions. They give a reusable, unconditional cancellation theorem for rational polynomials. This study proves that theorem independently, including the analytic convergence arguments, the exact rational recurrences, both boundary constants, and the coefficient calculation responsible for cancellation.

The result does **not** prove that Catalan's constant is irrational. It assumes neither irrationality of Catalan's constant nor linear independence of the constants occurring below. Determinants, valuations, nonvanishing, and the source's later arguments are outside the study. No Lean compilation or formal verification has been performed.

Source provenance: OpenAI/math revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, `preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/foundations.tex`, especially lines 54–71 and 93–262 of the saved text. The source's SHA-256 is `3929650dfb36859d8f88281795d348043f903c41a70b0bf3598c21586a633852`.

[Revision-pinned source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/foundations.tex)

## 1 Definitions and the main theorem

Put

\[
 f(t)=\sqrt{1-t^2}\quad(-1<t<1),\qquad
 G=\sum_{r=0}^{\infty}\frac{(-1)^r}{(2r+1)^2},\qquad
 \zeta_2=\sum_{n=1}^{\infty}\frac1{n^2}.
\]

The square root is positive. Both constant series converge absolutely. For nonnegative integers \(i,j\), define

\[
 M(i,j)=\int_{-1}^1\int_0^1
       \frac{|t|t^i s^j}{f(t)(1-ts)}\,ds\,dt,
 \qquad
 Z(i,j)=\int_0^1\int_0^1\frac{t^i s^j}{1-ts}\,ds\,dt.
\]

These are Lebesgue integrals, equivalently the absolutely convergent improper integrals established below. Values assigned on the null boundary sets do not matter. For polynomials \(P,Q,D\), write

\[
 M(P,Q)=\int_{-1}^1\int_0^1
       \frac{|t|P(t)Q(s)}{f(t)(1-ts)}\,ds\,dt,
 \qquad
 Z(D,Q)=\int_0^1\int_0^1\frac{D(t)Q(s)}{1-ts}\,ds\,dt,
\]

and abbreviate \(M(P,s^j)\) to \(M(P,j)\), and similarly for \(Z\).

**Main theorem.** Let \(P,D\in\mathbb Q[t]\), let \(L\ge1\) be an integer, and suppose that, as real \(t\to0\),

\[
 \frac{tP(t)}{\sqrt{1-t^2}}-D(t)=O(t^L).
\]

Then for every integer \(0\le j<L\),

\[
 M(P,j)-\frac32 Z(D,j)\in\mathbb Q+\mathbb QG.
\]

One-sided contact as \(t\downarrow0\) also suffices, because the function whose contact is being tested is analytic near zero. There is no requirement on the degrees beyond finiteness. \(L=0\) could be allowed, but would give an empty range of columns.

The proof will give explicit rational numbers \(A_j,B_j\) such that the expression is \(A_j+B_jG\).

## 2 Absolute convergence and the basic exchanges

For \(0<u<1\),

\[
 \int_0^1\frac{ds}{1-us}=\frac{-\log(1-u)}u,
 \qquad
 \int_0^1\frac{ds}{1+us}=\frac{\log(1+u)}u.
\]

The integrals of the absolute value of the base \(M\)-kernel over its positive and negative halves are therefore respectively

\[
 \int_0^1\frac{-\log(1-u)}{\sqrt{1-u^2}}\,du,
 \qquad
 \int_0^1\frac{\log(1+u)}{\sqrt{1-u^2}}\,du.
\]

The second is at most the first, since \(\log(1+u)\le-\log(1-u)\). The first is finite: on \((0,1/2]\), use \(-\log(1-u)\le2u\) and \(\sqrt{1-u^2}\ge\sqrt3/2\); near one use

\[
 \frac{-\log(1-u)}{\sqrt{1-u^2}}
 \le \frac{-\log(1-u)}{\sqrt{1-u}},
\]

whose integral is finite by \(v=\sqrt{1-u}\). For \(Z\), the corresponding integral is

\[
 \int_0^1\frac{-\log(1-u)}u\,du<\infty;
\]

the apparent singularity at zero is removable, and the logarithmic singularity at one is integrable.

Every polynomial is bounded on the relevant compact interval, so multiplying by \(P(t)Q(s)\) preserves absolute integrability. Consequently:

1. Fubini applies to these integrands, in either integration order.
2. Finite polynomial expansions can be integrated term by term.
3. All changes of variables below are valid first on compact subintervals and then by absolute convergence, or by monotone convergence when the integrand is nonnegative.

There is a separate detail for the geometric series on the negative half of the \(M\)-domain. For \(|t|<1\),

\[
 \frac1{1-ts}=\sum_{u=0}^{\infty}t^us^u.
\]

The series of **absolute values** after including the weight is bounded by

\[
 \frac{|t|}{f(t)}\sum_{u\ge0}|t|^us^u
 =\frac{|t|}{f(t)(1-|t|s)}.
\]

Its integral is exactly twice the first finite integral above. Thus absolute-integrability Fubini justifies interchanging this possibly alternating geometric series with both integrals. Pointwise convergence alone would not suffice. For the \(Z\)-series every term is nonnegative, so Tonelli also applies directly.

## 3 The central binomial coefficients and the Taylor kernel

For \(r\ge0\), set

\[
 c_r=4^{-r}\binom{2r}{r}.
\]

Then \(c_0=1\), \(c_r>0\), and

\[
 c_{r+1}=\frac{2r+1}{2r+2}c_r.
\]

Whenever \(c_{a/2}\) is written with integral \(a\), it means zero if \(a<0\) or \(a\) is odd. This zero-extension is essential.

For completeness, the generating function follows without invoking a generalized binomial theorem. The series \(C(t)=\sum_{r\ge0}c_rt^{2r}\) and its derivatives converge uniformly on every compact subinterval of \((-1,1)\), since \(0<c_r\le1\). The coefficient recurrence gives

\[
 (1-t^2)C'(t)=tC(t),\qquad C(0)=1.
\]

Hence the derivative of \(\sqrt{1-t^2}C(t)\) is zero, so

\[
 \frac1{\sqrt{1-t^2}}=\sum_{r\ge0}c_rt^{2r}\qquad(|t|<1).
\]

In particular, every Taylor coefficient of \(tP(t)/f(t)\) is rational when \(P\) has rational coefficients.

## 4 The one-variable moments

Define

\[
 m_i=\int_{-1}^1\frac{|t|t^i}{f(t)}\,dt\quad(i\ge0),
 \qquad m_{-1}:=0.
\]

The negative index here is an explicit convention. Symmetry gives \(m_i=0\) for odd \(i\). Also

\[
 m_0=2\int_0^1\frac{t}{\sqrt{1-t^2}}\,dt=2.
\]

For \(r\ge1\), integrate the derivative of \(t^{2r}\sqrt{1-t^2}\) over \((0,1)\). The boundary terms vanish, and all derivative terms are integrable. Writing \(\sqrt{1-t^2}=(1-t^2)/\sqrt{1-t^2}\) gives

\[
 (2r+1)m_{2r}=2r\,m_{2r-2}.
\]

The same recurrence is zero on both sides for odd indices, including \(i=1\) with the specified \(m_{-1}\). Thus

\[
 (i+1)m_i=i m_{i-2}\quad(i\ge1),
 \qquad
 m_i=\begin{cases}
 \displaystyle\frac2{(i+1)c_{i/2}},&i\text{ even},\\
 0,&i\text{ odd}.
 \end{cases}
\]

The explicit formula follows by induction from the recurrence for \(c_r\). In particular every \(m_i\) is rational.

Finally \(m_i\to0\) as \(i\to\infty\): the integrands tend to zero almost everywhere and their absolute values are bounded by the integrable weight \(|t|/f(t)\). This is a direct application of dominated convergence. The limit is needed in the telescoping arguments; it is not inferred merely from rationality.

## 5 Evaluation of Z

Tonelli and the geometric series give

\[
 Z(i,j)=\sum_{u=0}^{\infty}
          \frac1{(i+u+1)(j+u+1)}.
\]

Write \(H_n=\sum_{k=1}^n1/k\), \(H_n^{(2)}=\sum_{k=1}^n1/k^2\), with empty sums zero.

If \(i=j\), shifting the absolutely convergent series gives

\[
 Z(i,i)=\zeta_2-H_i^{(2)}.
\]

If \(i\ne j\), partial fractions give

\[
 \frac1{(i+u+1)(j+u+1)}
 =\frac1{j-i}\left(\frac1{i+u+1}-\frac1{j+u+1}\right).
\]

For example, when \(i<j\), a finite sum up to \(u=N-1\) is

\[
 \frac1{j-i}\left(H_j-H_i-
       \sum_{k=i+N+1}^{j+N}\frac1k\right).
\]

The last sum has the fixed number \(j-i\) of terms and tends to zero. This yields

\[
 Z(i,j)=\frac{H_i-H_j}{i-j}\quad(i\ne j).
\]

Define the rational array

\[
 Z^0(i,j)=\begin{cases}
 -H_i^{(2)},&i=j,\\
 (H_i-H_j)/(i-j),&i\ne j.
 \end{cases}
\]

Then \(Z(i,j)=Z^0(i,j)+[i=j]\zeta_2\). The sign in the off-diagonal quotient is worth checking: \(Z(0,1)=1\), not \(-1\). The array \(Z\) is symmetric.

## 6 The M series and its diagonal recurrence

The absolute series argument in Section 2 gives

\[
 M(i,j)=\sum_{u=0}^{\infty}\frac{m_{i+u}}{j+u+1}.
\]

Although the original integrand can have either sign, every term in this series is nonnegative. Reindexing an absolutely convergent series gives

\[
 M(i,j)-M(i+1,j+1)=\frac{m_i}{j+1}.
\]

Iterating this identity is a finite operation. If \(i\ge j\),

\[
 M(i,j)=M(i-j,0)-\sum_{k=1}^j\frac{m_{i-j+k-1}}k.
\]

If \(i<j\), writing \(d=j-i\) gives

\[
 M(i,j)=M(0,d)-\sum_{k=d+1}^j\frac{m_{k-d-1}}k.
\]

The cases \(i=0\), \(j=0\), and \(i=j\) are covered by empty sums without a separate limiting convention.

### An exact rational tail bound

This is a useful additional consequence for reproducible checks. For \(N\ge1\), put \(n_0=i+N\) and

\[
 T_N=M(i,j)-\sum_{u=0}^{N-1}\frac{m_{i+u}}{j+u+1}.
\]

The moment recurrence says

\[
 \frac{m_n}{n}=m_{n-2}-m_n\quad(n\ge1).
\]

For \(n\ge n_0\), with \(d=j-i+1\), the positive ratio \(n/(n+d)\) is at most

\[
 C=\max\left(1,\frac{i+N}{j+N+1}\right).
\]

Consequently, using \(m_n\ge0\) and telescoping,

\[
 0\le T_N\le C\bigl(m_{i+N-2}+m_{i+N-1}\bigr).
\]

All quantities on the right are rational and the bound tends to zero. If \(j=i-1\), the ratio is identically one and the full series itself telescopes, giving the exact extra identity

\[
 M(i,i-1)=m_{i-2}+m_{i-1}\quad(i\ge1).
\]

## 7 The two boundary recurrences

Set \(K_d^-=M(d,0)\) and \(K_d^+=M(0,d)\).

For \(d\ge2\), the moment recurrence implies, term by term,

\[
 \frac{d m_{d+u}-(d-1)m_{d+u-2}}{u+1}
 =m_{d+u-2}-m_{d+u}.
\]

The finite sum for \(0\le u\le N\) on the right is

\[
 m_{d-2}+m_{d-1}-m_{d+N-1}-m_{d+N}.
\]

Since the last two moments tend to zero, and the series on the left are absolutely convergent,

\[
 dK_d^-=(d-1)K_{d-2}^-+m_{d-2}+m_{d-1}\quad(d\ge2).
\]

For \(d=1\), omit the term multiplied by \(d-1\). The same finite telescoping works with \(m_{-1}=0\) and gives

\[
 K_1^-=m_{-1}+m_0=2.
\]

For the plus recurrence, first reindex the \(K_d^+\)-series by two. For \(u\ge2\),

\[
 \frac{(d-1)m_{u-2}-(d-2)m_u}{d+u-1}
 =m_{u-2}-m_u.
\]

Its sum is \(m_0+m_1=2\). The omitted \(u=0,1\) terms from the other series contribute

\[
 -(d-2)\left(\frac{m_0}{d-1}+\frac{m_1}d\right)
 =-\frac{2(d-2)}{d-1}.
\]

Therefore

\[
 (d-1)K_d^+=(d-2)K_{d-2}^++\frac2{d-1}\quad(d\ge2).
\]

At \(d=2\) the old start \(K_0^+\) has coefficient zero. Thus even positive plus indices do not inherit the \(G\)-term in \(K_0^+\). This is an important endpoint detail.

## 8 The two independent boundary constants

### The Catalan start

Splitting the \(t\)-integral into its positive and negative halves gives

\[
 K_0^-=K_0^+
 =\int_0^1\frac{\log((1+t)/(1-t))}{\sqrt{1-t^2}}\,dt.
\]

With \(t=\sin\theta\), the half-angle identity

\[
 \frac{1+\sin\theta}{1-\sin\theta}
 =\tan^2(\pi/4+\theta/2)
\]

and then reflection around \(\pi/4\) give

\[
 K_0^-= -4\int_0^{\pi/4}\log\tan v\,dv
       =4\int_0^1\frac{-\log x}{1+x^2}\,dx.
\]

The final substitution is \(x=\tan v\). To justify expansion at the endpoint, note that

\[
 \sum_{r\ge0}\int_0^1x^{2r}(-\log x)\,dx
 =\sum_{r\ge0}\frac1{(2r+1)^2}<\infty.
\]

The elementary integral follows by integration by parts, or by differentiating the integral of \(x^a\) on a compact parameter interval. Absolute-integrability Fubini now permits the alternating geometric series, proving

\[
 K_0^-=K_0^+=4G.
\]

### The zeta start by a direct nonnegative integral

Pair \(t=u\) with \(t=-u\) in \(M(0,1)\), then integrate in \(s\):

\[
 K_1^+
 =2\int_0^1\frac{u}{\sqrt{1-u^2}}
          \int_0^1\frac{s}{1-u^2s^2}\,ds\,du
 =\int_0^1\frac{-\log(1-u^2)}{u\sqrt{1-u^2}}\,du.
\]

The substitution \(x=\sqrt{1-u^2}\) gives

\[
 K_1^+=2\int_0^1\frac{-\log x}{1-x^2}\,dx
       =2\sum_{r\ge0}\frac1{(2r+1)^2}
       =\frac32\zeta_2.
\]

Here the series terms are nonnegative, so Tonelli applies directly. The last equality separates the even terms of \(\zeta_2\). This proof supplies exactly the constant required for cancellation without using the Basel evaluation.

### Verification of the source's pi notation

The source also writes \(K_1^+=\pi^2/4\). The following independent argument confirms that equality without assuming a previously evaluated zeta series.

The moment series and the ratio for \(c_r\) give

\[
 K_1^+=\sum_{k\ge1}\frac1{2k^2c_k}.
\]

The central binomial coefficient is the largest of the \(2k+1\) coefficients in \((1+1)^{2k}\), so \(c_k\ge1/(2k+1)\). Hence the power series

\[
 y(x)=\sum_{k\ge1}\frac{x^{2k}}{2k^2c_k}
\]

and its first two derivatives converge uniformly on every \(|x|\le r<1\). Direct coefficient comparison gives

\[
 (1-x^2)y''-xy'=2,\qquad y(0)=y'(0)=0.
\]

The same equations hold for \((\arcsin x)^2\). If their difference is \(h\), then

\[
 \bigl(\sqrt{1-x^2}\,h'(x)\bigr)'=0;
\]

the initial values imply \(h=0\) throughout \((-1,1)\). Finally, the coefficients of \(y\) are nonnegative, so monotone convergence as \(x\uparrow1\) gives

\[
 \sum_{k\ge1}\frac1{2k^2c_k}
 =\lim_{x\uparrow1}(\arcsin x)^2=\frac{\pi^2}4.
\]

Combined with the direct integral evaluation, this also proves \(\zeta_2=\pi^2/6\). The proof of cancellation itself does not need this last reformulation.

### The source's Abel exchange

The source alternatively relates the odd reciprocal-square sum to pi by an Abel parameter. That exchange is valid as well. For fixed \(0<\rho<1\), the series

\[
 \sum_{k\ge1}\frac{\rho^k\sin(kx)}k
 =\operatorname{Im}(-\log(1-\rho e^{ix}))
\]

converges absolutely and uniformly for \(0\le x\le\pi\), because its absolute values are bounded by \(\sum_k\rho^k/k<\infty\). It can therefore be integrated term by term, giving \(2\sum_{k\text{ odd}}\rho^k/k^2\). On \(0<x<\pi\), the number \(1-\rho e^{ix}\) has positive real part and negative imaginary part. Thus the imaginary part of its negative principal logarithm lies between zero and \(\pi/2\), uniformly in \(\rho\). As \(\rho\uparrow1\), it tends to \((\pi-x)/2\), since

\[
 1-e^{ix}=2\sin(x/2)e^{i(x/2-\pi/2)}.
\]

Dominated convergence on the integral side and monotone convergence on the nonnegative odd-series side now give

\[
 2\sum_{k\text{ odd}}\frac1{k^2}
 =\int_0^\pi\frac{\pi-x}2\,dx=\frac{\pi^2}4.
\]

This verifies the source's particular exchange separately from the direct proof used above.

## 9 Rational boundary arrays and their explicit solutions

Define rational sequences with starts

\[
 k_0^-=k_0^+=k_1^+=0,\qquad k_1^-=2,
\]

and recurrences

\[
 dk_d^-=(d-1)k_{d-2}^-+m_{d-2}+m_{d-1},
 \qquad
 (d-1)k_d^+=(d-2)k_{d-2}^++\frac2{d-1}
\]

for \(d\ge2\). All denominators are nonzero; induction proves existence, uniqueness, and rationality.

For \(z\ge0\), set

\[
 H_z^*=\begin{cases}
 c_{z/2},&z\text{ even},\\
 \displaystyle\frac1{z c_{(z-1)/2}},&z\text{ odd}.
 \end{cases}
\]

These are positive rational numbers and satisfy

\[
 H_{z+2}^*/H_z^*=(z+1)/(z+2).
\]

Dividing the minus recurrence by \(zH_z^*\) yields the increment

\[
 \frac{k_z^-}{H_z^*}-\frac{k_{z-2}^-}{H_{z-2}^*}
 =\begin{cases}
 2/(z^2(H_z^*)^2),&z\text{ even},\\
 2/z,&z\text{ odd},
 \end{cases}
\]

where the even case begins at \(z=2\), the odd recurrence at \(z=3\), and the odd initial value is \(k_1^-/H_1^*=2\). Thus

\[
 k_u^-=\begin{cases}
 \displaystyle H_u^*\sum_{\substack{1\le z\le u\\z\text{ even}}}
            \frac2{z^2(H_z^*)^2},&u\text{ even},\\[4pt]
 \displaystyle H_u^*\sum_{\substack{1\le z\le u\\z\text{ odd}}}
            \frac2z,&u\text{ odd}.
 \end{cases}
\]

For the plus recurrence, put \(d=u+1\). Dividing by \(uH_u^*\) gives increment \(2/(u^2H_u^*)\), with starts \(k_1^+=0\) and \(k_2^+=2\). Therefore

\[
 k_{u+1}^+=H_u^*
       \sum_{\substack{1\le z\le u\\z\equiv u\pmod2}}
          \frac2{z^2H_z^*}\quad(u\ge0).
\]

The case \(u=0\) is an empty sum, not a term with denominator zero. This verifies all the source's explicit rational-boundary formulas.

## 10 The universal decomposition

Define

\[
 M^0(i,j)=\begin{cases}
 \displaystyle k_{i-j}^- -\sum_{k=1}^j\frac{m_{i-j+k-1}}k,&i\ge j,\\[5pt]
 \displaystyle k_{j-i}^+ -\sum_{k=j-i+1}^j
            \frac{m_{k-(j-i)-1}}k,&i<j.
 \end{cases}
\]

This is an unambiguous rational array. The boundary recurrences, their starts, and the recurrence for \(c_r\) prove by induction that

\[
 K_d^-=k_d^-+4G c_{d/2}\quad(d\ge0),
\]

and

\[
 K_d^+=k_d^++4G[d=0]+\frac32\zeta_2 c_{(d-1)/2}\quad(d\ge0).
\]

For the second formula, check \(d=0,1,2\) explicitly: the zero multiplier at \(d=2\) eliminates the old \(G\)-start. Subsequent homogeneous recurrences propagate the odd-index \(\zeta_2\)-start by \(c_r\).

The finite diagonal reductions preserve \(i-j\), and all their correction terms are rational. Consequently

\[
 \boxed{M(i,j)=M^0(i,j)+4G c_{(i-j)/2}
                  +\frac32\zeta_2 c_{(j-i-1)/2}}
\]

and

\[
 \boxed{Z(i,j)=Z^0(i,j)+[i=j]\zeta_2}.
\]

For any individual \(M(i,j)\), at most one of its displayed \(G\)- and \(\zeta_2\)-kernels is nonzero. This follows directly from their index inequalities, not from independence of constants.

### Meaning of a coefficient of a constant

The displayed formulas provide a specified representation in the span of \(1,G,\zeta_2\). No uniqueness as a real-number representation is asserted. More formally, compute first in the free rational vector space with basis \(e_0,e_G,e_\zeta\), and then apply the evaluation map

\[
 a e_0+b e_G+c e_\zeta\longmapsto a+bG+c\zeta_2.
\]

That evaluation map is not assumed injective. In this study, a “\(\zeta_2\)-coefficient” always means the explicitly constructed coordinate in this free space. This distinction is crucial when discussing failed cancellation.

## 11 The exact defect identity and the main theorem

Write \(P(t)=\sum_i p_it^i\) and \(D(t)=\sum_i d_it^i\), padding coefficient lists by zeros. Finite linearity and the universal decompositions give, for every \(j\ge0\),

\[
 M(P,j)-\frac32 Z(D,j)
 =A_j+B_jG+\frac32 E_j\zeta_2,
\]

where all three quantities below are rational:

\[
 A_j=\sum_i p_iM^0(i,j)-\frac32\sum_i d_iZ^0(i,j),
\]

\[
 B_j=4\sum_{r\ge0}p_{j+2r}c_r,
 \qquad
 E_j=\sum_i p_i c_{(j-i-1)/2}-d_j.
\]

The sum defining \(B_j\) is finite because \(P\) is a polynomial. By Section 3,

\[
 E_j=[t^j]\left(\frac{tP(t)}{f(t)}-D(t)\right).
\]

This is the exact defect identity. It is valid whether or not contact holds.

Let \(F(t)=tP(t)/f(t)-D(t)\). It is analytic near zero. For an analytic function, \(F(t)=O(t^L)\) is equivalent to vanishing of its Taylor coefficients in degrees \(0,\ldots,L-1\). Here is the needed argument: if the first nonzero coefficient had index \(k<L\), then \(F(t)/t^k\) would approach that nonzero coefficient, whereas the big-O bound would force its absolute value to approach zero. Conversely, if those coefficients vanish, then \(F(t)=t^LH(t)\) for an analytic, locally bounded \(H\), proving the big-O estimate.

Thus contact implies \(E_j=0\) whenever \(0\le j<L\). The defect identity reduces to \(A_j+B_jG\), which proves the main theorem.

## 12 Reusable extensions

### A single coefficient condition is enough

For one fixed \(j\), it is enough to assume \(E_j=0\); full contact of order \(j+1\) is stronger than necessary. In the specified free-space decomposition, vanishing of \(E_j\) is both necessary and sufficient for cancellation of that coordinate. It is not claimed to be necessary for membership of the evaluated real number in \(\mathbb Q+\mathbb QG\).

### Polynomial test functions

Let \(Q(s)=\sum_jq_js^j\in\mathbb Q[s]\). Then

\[
 M(P,Q)-\frac32Z(D,Q)
 =\sum_jq_jA_j+G\sum_jq_jB_j
        +\frac32\zeta_2\sum_jq_jE_j.
\]

Consequently contact to order \(L\), together with \(\deg Q<L\), implies membership in \(\mathbb Q+\mathbb QG\). More generally, only the exact pairing condition \(\sum_jq_jE_j=0\) is needed. This handles cancellation across several columns without requiring every coordinate separately to vanish.

### Computing a matching polynomial

For any \(P\in\mathbb Q[t]\) and \(L\ge1\), the unique \(D\) of degree less than \(L\) with the required contact is

\[
 D(t)=\sum_{j=0}^{L-1}\left(\sum_i p_i c_{(j-i-1)/2}\right)t^j.
\]

Any other polynomial with the same contact differs from this one by a multiple of \(t^L\). Such a change cannot affect the formal \(\zeta_2\)-coefficient in columns \(j<L\), though it can change their rational parts.

### Other coefficient fields

For any subfield \(K\subseteq\mathbb R\), the same proof gives the corresponding conclusion \(K+KG\) for coefficients in \(K\): retain \(0\le j<L\) for a monomial test, or \(\deg Q<L\) for a polynomial test, under contact of order \(L\). The more general exact defect-pairing condition also suffices. Keeping the target \(\mathbb Q+\mathbb QG\) while allowing arbitrary real coefficients is an invalid universal generalization; see `counterexamples.md`.

### The source's rows

The source has already constructed polynomials \(P_r,D_r\) with

\[
 tP_r/f-D_r=tR_r/f,
 \qquad R_r=(1-t)^h t^{C-1}w^{r-g},
 \qquad w=t/(1+f).
\]

Since \(w=(t/2)(1+O(t^2))\) and \(C-g=L\), their defect has the leading term

\[
 tR_r/f=2^{g-r}t^{L+r}(1+O(t)).
\]

Thus their actual contact order is \(L+r\), and the universal theorem covers all source columns \(j<L\), as well as the additional columns \(L\le j<L+r\) for that row. At \(j=L+r\), the first nonzero displayed \(\zeta_2\)-coordinate is \((3/2)2^{g-r}\). This is a coefficient statement, not a new nonmembership claim. No determinant or valuation conclusion is being drawn here.

## 13 Exact small examples

The following values are exact:

\[
\begin{array}{c|ccc}
 M(i,j)&j=0&j=1&j=2\\\hline
 i=0&4G&\tfrac32\zeta_2&2\\
 i=1&2&4G-2&\tfrac32\zeta_2-1\\
 i=2&2G+1&2&4G-2
\end{array}
\]

Also

\[
 M(0,3)=\frac12+\frac34\zeta_2,\quad
 M(3,0)=\frac{16}9,\quad
 M(0,4)=\frac{14}9,\quad
 M(4,0)=\frac{13}{12}+\frac32G.
\]

For \(Z\),

\[
 Z(0,0)=\zeta_2,\quad Z(0,1)=1,\quad Z(0,2)=\frac34,
 \quad Z(1,1)=\zeta_2-1,\quad Z(1,2)=\frac12.
\]

Take \(P=1\), \(D=t\). Since

\[
 t/f-t=\frac12t^3+\frac38t^5+\cdots,
\]

contact holds with \(L=3\). The resulting entries are

\[
 j=0:\quad4G-\frac32,\qquad
 j=1:\quad\frac32,\qquad
 j=2:\quad\frac54.
\]

At the first excluded column,

\[
 j=3:\quad \frac34\zeta_2-\frac18.
\]

This checks the strict inequality in the coefficient-cancellation mechanism. It does not prove that the last value lies outside \(\mathbb Q+\mathbb QG\).

## 14 Analytic exchange ledger

Every infinite exchange used in the proof has a specified justification:

- The original two-dimensional \(M\) and \(Z\) integrals: absolute integrability from Section 2, then Fubini.
- The \(M\) geometric series on either sign of \(t\): summable integrated absolute values, using \(1/(1-|t|s)\).
- The \(Z\) geometric series: Tonelli for nonnegative terms.
- The limit \(m_i\to0\): dominated convergence by \(|t|/f(t)\).
- Boundary recurrence sums: finite telescoping first, then the established zero moment tails and convergence of the original series.
- The Catalan integral series: \(\sum_r\int_0^1x^{2r}(-\log x)\,dx<\infty\), so absolute Fubini.
- The direct \(K_1^+\) series: Tonelli for nonnegative terms.
- Differentiating the Taylor series of \(1/f\) and of \((\arcsin x)^2\): uniform convergence of each derivative series on every compact subset of \((-1,1)\).
- The limit of the latter power series at one: monotone convergence for nonnegative coefficients.
- The source's optional Abel-series argument: uniform absolute convergence for fixed parameter, a uniform argument bound for dominated convergence, and monotone convergence of the positive odd terms.
- Polynomial contraction: finite sums only, so no further infinite interchange is introduced.

No argument substitutes an endpoint directly into a power series before proving an appropriate convergence theorem.

## 15 Source audit and proof status

The audit found no false assertion in the scoped convergence paragraph, moment evaluations, rational recurrences, rational decompositions, explicit boundary arrays, or cancellation proposition. The presentation above expands the source's abbreviated analytic arguments and replaces one optional boundary-constant detour with a direct positive integral.

Important qualifications are:

1. \(m_{-1}=0\) and the zero-extension of \(c\) are conventions that must be explicit in arithmetic and in a future formalization.
2. The source's \(M^0(-1,j)=k^+_{j+1}\) is an algebraic convention and was not needed for the theorem proved here.
3. “Coefficient of \(\zeta_2\)” refers to the designated decomposition; no independence of \(1,G,\zeta_2\) is assumed.
4. Missing contact and the excluded endpoint yield genuine nonzero formal coordinates. They do not supply unconditional nonmembership counterexamples in \(\mathbb Q+\mathbb QG\).
5. The original exact-arithmetic program checks finite identities and examples. It does not certify the analytic arguments, Catalan irrationality, or any Lean declaration.

The proof is a complete ordinary mathematical proof of the extracted theorem. The separate `lean-roadmap.md` is a future implementation plan, not a formal verification report.
