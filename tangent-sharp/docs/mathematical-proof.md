# Conditional decay and absolute convergence for integer tangents

## Hypothesis, kept explicit

Throughout, assume the following statement, denoted **H**:

> For every real number \(\nu>2\), there is an integer \(Q_\nu\ge 1\) such that, for every positive integer \(q\ge Q_\nu\) and every integer \(p\),
> \[
> \left|\pi-\frac pq\right|\ge q^{-\nu}.
> \tag{H}
> \]

All real powers in this document have positive bases. We do not prove H. Every conclusion below is conditional on H. Standard elementary properties of trigonometric functions, \(\pi>2\), and the standard irrationality theorem for \(\pi\) may be used. In particular, \(\cos n\ne0\) for every positive integer \(n\): otherwise the usual description of the zeros of cosine would give \(n=(k+1/2)\pi\) for an integer \(k\), contradicting the irrationality of \(\pi\). Thus the ordinary real tangent is defined at all the arguments in the series.

## A nearest odd integer and the distance to its pole

For a positive integer \(n\), put
\[
k_n=\left\lfloor\frac n\pi\right\rfloor,
\qquad q_n=2k_n+1,
\qquad t_n=n-\frac{\pi q_n}{2},
\qquad d_n=|t_n|.
\]
Since \(n/\pi\ge0\), we have \(k_n\ge0\), so \(q_n\) is a positive odd integer. The defining inequalities for the floor give
\[
2k_n\le\frac{2n}{\pi}<2k_n+2.
\]
Therefore
\[
\left|\frac{2n}{\pi}-q_n\right|\le1,
\qquad -\frac\pi2\le t_n<\frac\pi2,
\qquad 0\le d_n\le\frac\pi2.
\tag{1}
\]
The integer \(q_n\) is a nearest odd integer to \(2n/\pi\). Indeed, if another odd integer \(r\ne q_n\) is chosen, then \(|r-q_n|\ge2\). With \(a=|2n/\pi-q_n|\le1\), the reverse triangle inequality gives
\[
\left|\frac{2n}{\pi}-r\right|\ge2-a\ge a.
\]
Ties at an endpoint are allowed; our formula chooses the odd integer above the lower even endpoint. Consequently \(d_n\) is the distance from \(n\) to the closest tangent pole.

The same floor inequalities give the useful estimates
\[
\frac{2n}{\pi}-1<q_n\le\frac{2n}{\pi}+1\le2n.
\tag{2}
\]
For the last inequality, use \(\pi>2\) and \(n\ge1\), so \(2n/\pi\le n\) and \(n+1\le2n\). The lower bound shows that \(q_n\to\infty\).

## Converting H to a tangent bound

Fix any real \(\nu>2\), and take \(Q_\nu\) from H. Choose a positive integer \(N_\nu\) satisfying
\[
N_\nu\ge1,
\qquad \frac{2N_\nu}{\pi}-1\ge Q_\nu.
\tag{3}
\]
For example,
\[
N_\nu=\max\!\left(1,\left\lceil\frac\pi2(Q_\nu+1)\right\rceil\right)
\]
satisfies (3). If \(n\ge N_\nu\), then (2) implies \(q_n\ge Q_\nu\), so H applies with denominator \(q_n\) and integer numerator \(p=2n\). Hence
\[
d_n
=\left|n-\frac{\pi q_n}{2}\right|
=\frac{q_n}{2}\left|\pi-\frac{2n}{q_n}\right|
\ge\frac12q_n^{1-\nu}>0.
\tag{4}
\]

Since \(n=t_n+\pi k_n+\pi/2\), the addition and period formulas imply
\[
|\cos n|=|\sin t_n|=\sin d_n.
\tag{5}
\]
For \(0\le d\le\pi/2\), the standard chord bound for sine is
\[
\sin d\ge\frac{2d}{\pi}.
\tag{6}
\]
It follows, for example, from the concavity of sine on \([0,\pi/2]\) and its endpoint values \(0\) and \(1\). Equations (4)--(6) give
\[
|\cos n|\ge\frac{2d_n}{\pi}\ge\frac1\pi q_n^{1-\nu}>0.
\]
Using \(|\sin n|\le1\), we obtain
\[
|\tan n|
=\frac{|\sin n|}{|\cos n|}
\le\pi q_n^{\nu-1}
\le\pi(2n)^{\nu-1}.
\tag{7}
\]
Here the last step uses (2) and the monotonicity of positive real powers with exponent \(\nu-1>0\). Dividing by \(n^3>0\) yields the reusable eventual estimate
\[
\boxed{
\frac{|\tan n|}{n^3}
\le \pi\,2^{\nu-1}n^{\nu-4}
\qquad(n\ge N_\nu).
}
\tag{8}
\]

## The requested limit

Use H with \(\nu=3\). Equation (7) becomes
\[
|\tan n|\le\pi q_n^2\le4\pi n^2
\qquad(n\ge N_3),
\]
and consequently
\[
\left|\frac{\tan n}{n^3}\right|
\le\frac{4\pi}{n}.
\tag{9}
\]
Given any \(\varepsilon>0\), choose a positive integer \(M\ge N_3\) with \(M>4\pi/\varepsilon\). For every integer \(n\ge M\), (9) is strictly less than \(\varepsilon\). This proves
\[
\boxed{\displaystyle\lim_{n\to\infty,\ n\in\mathbb N_{>0}}
\frac{\tan n}{n^3}=0.}
\]

## Absolute convergence of the series

Now use H with \(\nu=5/2\). Equation (8) gives
\[
0\le\frac{|\tan n|}{n^3}
\le C\,n^{-3/2}
\qquad(n\ge N_{5/2}),
\qquad C=\pi\,2^{3/2}.
\tag{10}
\]
The positive series \(\sum_{n=1}^{\infty}n^{-3/2}\) converges by the usual \(p\)-series theorem. Equivalently, its tail is bounded by a finite first term and the integral
\[
\int_A^{\infty}x^{-3/2}\,dx=2A^{-1/2}
\qquad(A>0).
\]
Comparison using (10) therefore proves convergence of the tail of
\(\sum_{n=1}^{\infty}|\tan n|/n^3\). Its finitely many earlier terms are all finite, so
\[
\boxed{\displaystyle\sum_{n=1}^{\infty}\frac{|\tan n|}{n^3}<\infty.}
\]
In particular, \(\sum_{n=1}^{\infty}\tan n/n^3\) converges absolutely.

## Formalization conventions and dependency record

The Lean statements retain H as an explicit theorem argument; H is not declared as an axiom. The intended sequence can be indexed by \(\mathbb N\), using \(n+1\) for the positive-integer sequence. An alternative sequence indexed by \(n\) may include the harmless zero term: Lean's totalized real division gives \(\tan(0)/0^3=0\), and a finite prefix affects neither a limit nor summability.

The proof needs only the stated approximation hypothesis, the nearest odd construction from the floor, elementary integer/cast inequalities, the sine chord bound, standard trigonometric identities, and standard limit and \(p\)-series comparison theorems. No assertion about the validity of H is made. The estimate for the limit uses only its instance \(\nu=3\); the summability extension additionally uses its instance \(\nu=5/2\).
