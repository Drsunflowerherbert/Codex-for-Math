# Hand-checkable examples

All numbers in these certificates are integers or rational numbers. Decimal
approximations are unnecessary. The inequalities below use ordinary rational
arithmetic and the interval rules in the study.

For a polynomial **map** \(F:\mathbb R^2\to\mathbb R^2\), the expression
\(F(c)\) is its vector **value** at the center. The derivative \(DF(z)\) is a
matrix depending on the point \(z\). The interval matrix \(J(X)\) encloses all
those derivative values on the closed box
\(X=\prod_i[c_i-r_i,c_i+r_i]\). It is not a single derivative value.

The verifier forms the fixed-point map \(T(z)=z-YF(z)\), encloses its
derivative by \(A=I-YJ(X)\), and sets

\[
 M_{ij}=\max(|\inf A_{ij}|,|\sup A_{ij}|),\quad
 d_i=|(YF(c))_i|,\quad
 q=\max_i\sum_j M_{ij}\frac{r_j}{r_i},\quad
 \eta=\max_i\frac{d_i}{r_i}.
\]

The self-map test is the coordinatewise inequality
\(d+Mr\le r\). The contraction test is the strict inequality \(q<1\).
With nonsingular \(Y\), the self-map test supplies existence by the fixed-point
argument in the study. The contraction test separately supplies uniqueness.
When both hold and \(Y\) is nonsingular, the theorem certifies one and only one
zero in the **closed box \(X\)**, with

\[
 |z_i^*-c_i|\le \frac{\eta r_i}{1-q}.
\]

Here \(\eta\) is a common maximum: substituting each individual \(d_i/r_i\)
into that bound is generally unjustified because the coordinates interact.
These are local claims. Global root counts stated below follow from separate
elementary algebra, not from the certificate.

## 1. A circle and a line

Certificate: [`examples/circle-line.json`](examples/circle-line.json).

Use

\[
 F(x,y)=\binom{x^2+y^2-1}{x-y},\quad
 c=\binom{7/10}{7/10},\quad r=\binom{1/100}{1/100},\quad
 X=[69/100,71/100]^2.
\]

Both coordinates are coupled in the first equation. Choose the exact inverse
of the center derivative as the preconditioner:

\[
 DF(c)=\begin{pmatrix}7/5&7/5\\1&-1\end{pmatrix},\quad
 Y=\begin{pmatrix}5/14&1/2\\5/14&-1/2\end{pmatrix},\quad
 \det Y=-5/14\ne0.
\]

The derivative enclosure and center value are

\[
 J(X)=\begin{pmatrix}[69/50,71/50]&[69/50,71/50]\\1&-1\end{pmatrix},
 \qquad F(c)=\binom{-1/50}{0},\qquad
 YF(c)=\binom{-1/140}{-1/140}.
\]

For example,
\((YJ)_{11}=(5/14)[69/50,71/50]+1/2
=[139/140,141/140]\). Every entry of \(I-YJ(X)\) is consequently
\([-1/140,1/140]\), so

\[
 M=\begin{pmatrix}1/140&1/140\\1/140&1/140\end{pmatrix},\qquad
 q=1/70,\quad \eta=5/7.
\]

The self-map upper bound in each coordinate is

\[
 \frac1{140}+\frac1{140}\frac1{100}
                  +\frac1{140}\frac1{100}
 =\frac{51}{7000}<\frac1{100},
\]

with margin \(19/7000\) in each coordinate. Thus the box contains a unique
zero, and the error bound is

\[
 |z_i^*-7/10|\le
 \frac{(5/7)(1/100)}{1-1/70}=\frac1{138}
 \quad(i=1,2).
\]

Separately, substitution \(x=y\) shows that the two real roots in the whole
plane are \((1/\sqrt2,1/\sqrt2)\) and
\((-1/\sqrt2,-1/\sqrt2)\). The negative root lies outside the certified box.
The certificate itself did not need these radical expressions.

## 2. A circle and a parabola

Certificate: [`examples/circle-parabola.json`](examples/circle-parabola.json).

Both equations are nonlinear:

\[
 F(x,y)=\binom{x^2+y^2-1}{x^2-y},\quad
 c=\binom{4/5}{3/5},\quad r=\binom{1/20}{1/20},\quad
 X=[3/4,17/20]\times[11/20,13/20].
\]

The exact center derivative and its inverse are

\[
 DF(c)=\begin{pmatrix}8/5&6/5\\8/5&-1\end{pmatrix},\quad
 Y=\begin{pmatrix}25/88&15/44\\5/11&-5/11\end{pmatrix},\quad
 \det Y=-25/88\ne0.
\]

The exact data needed by the checker are

\[
 J(X)=\begin{pmatrix}[3/2,17/10]&[11/10,13/10]\\{}[3/2,17/10]&-1\end{pmatrix}.
\]

\[
 F(c)=\binom0{1/25},\quad
 YF(c)=\binom{3/220}{-1/55},\quad
 d=\binom{3/220}{1/55}.
\]

The interval products are worth writing out, since the verifier does not
silently cancel dependent occurrences of the same interval:

\[
\begin{aligned}
 (YJ)_{11}
 &=\left(\frac{25}{88}+\frac{15}{44}\right)[3/2,17/10]
   =[15/16,17/16],\\
 (YJ)_{12}
 &=\frac{25}{88}[11/10,13/10]-\frac{15}{44}
   =[-5/176,5/176],\\
 (YJ)_{21}
 &=\frac5{11}[3/2,17/10]-\frac5{11}[3/2,17/10]
   =[-1/11,1/11],\\
 (YJ)_{22}
 &=\frac5{11}[11/10,13/10]+\frac5{11}
   =[21/22,23/22].
\end{aligned}
\]

In the actual derivative of \(T\), the \((2,1)\) entry is identically zero.
The interval matrix computation forgets this dependency and still gives a
valid, wider enclosure. Consequently

\[
 A=\begin{pmatrix}[-1/16,1/16]&[-5/176,5/176]\\{}
                  [-1/11,1/11]&[-1/22,1/22]\end{pmatrix},\quad
 M=\begin{pmatrix}1/16&5/176\\1/11&1/22\end{pmatrix}.
\]

The row sums are \(1/11\) and \(3/22\). Equal radii therefore give

\[
 q=3/22<1,\quad \eta=\max(3/11,4/11)=4/11,
\]

and the self-map test reads

\[
 d+Mr=
 \binom{3/220+(1/11)(1/20)}{1/55+(3/22)(1/20)}
 =\binom{1/55}{1/40}
 \le\binom{1/20}{1/20}.
\]

The margins are \(7/220\) and \(1/40\). The error bound is

\[
 |x^*-4/5|\le2/95,\qquad |y^*-3/5|\le2/95,
 \qquad \frac{(4/11)(1/20)}{1-3/22}=\frac2{95}.
\]

Separately, \(y=x^2\) gives \(t^2+t-1=0\), where \(t=x^2\ge0\).
Thus the two real roots in the whole plane are

\[
 \left(\mathord\pm\sqrt{\frac{\sqrt5-1}{2}},
              \frac{\sqrt5-1}{2}\right).
\]

The certificate locates the positive root and proves uniqueness in its box;
it does not assert global uniqueness.

## 3. Tiny residual, singular center, and two roots

Certificate: [`examples/tiny-residual-two-roots.json`](examples/tiny-residual-two-roots.json).

Consider

\[
 F_-(x,y)=\binom{x^2-10^{-12}}{y-x},\quad
 c=\binom00,\quad r=\binom{1/1000}{1/1000},\quad Y=I.
\]

Here \(10^{-12}\) means the exact rational
\(1/1000000000000\); it is not a floating-point datum. The residual is tiny:
\(F_-(c)=(-10^{-12},0)^T\). However,

\[
 DF_-(c)=\begin{pmatrix}0&0\\-1&1\end{pmatrix}
\]

is singular. The chosen \(Y=I\) is nonsingular, as required by the theorem,
but it cannot repair the lack of a contraction on this box. Indeed,

\[
 J(X)=\begin{pmatrix}[-1/500,1/500]&0\\-1&1\end{pmatrix},\quad
 A=\begin{pmatrix}[499/500,501/500]&0\\1&0\end{pmatrix},\quad
 M=\begin{pmatrix}501/500&0\\1&0\end{pmatrix}.
\]

Thus

\[
 q=501/500>1,\quad \eta=1/1000000000,\quad
 d+Mr=\binom{1002000001/1000000000000}{1/1000}.
\]

The first self-map margin is
\(-2000001/1000000000000\), so both the self-map and contraction tests fail.
The checker reports **not certified**, with no error certificate. There are
in fact two roots in the box:

\[
 (1/1000000,1/1000000),\qquad
 (-1/1000000,-1/1000000).
\]

The small residual alone gave neither existence nor uniqueness in the specified box.

## 4. The same tiny residual size, and no real root

Certificate: [`examples/tiny-residual-no-root.json`](examples/tiny-residual-no-root.json).

Replace the first equation above by \(x^2+10^{-12}\), giving

\[
 F_+(x,y)=\binom{x^2+10^{-12}}{y-x}.
\]

The same \(c,r,Y\) give exactly the same \(J(X),A,M,d,q,\eta\) and self-map
test as in Example 3: taking the absolute value of the center correction
erases the residual's sign. The checker again reports **not certified**.
Nevertheless \(x^2+10^{-12}>0\) for every real \(x\), so this system has no
real root at all. That nonexistence conclusion follows from this separate
inequality, not from a failed certificate.

Together Examples 3 and 4 demonstrate the distinction: a rejected candidate
certificate is compatible with two roots, no roots, and other possibilities.
It is not a decision procedure for root existence.
