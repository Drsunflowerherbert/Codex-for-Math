# Independently checked examples and adversarial cases

These examples test classification of a **real polynomial** at its stationary
point \((0,0)\), with a Hessian of rank one. They were derived independently of
the classifier. The expanded coefficients in [examples.json](examples.json)
are exact rational numbers encoded as strings; no decimal tolerance is used.
Every listed polynomial has vanishing gradient and Hessian rank one at the
origin. These hypotheses were also checked independently using SymPy 1.14.0.

## Reading the machine-readable data

The top-level object has `schema_version: 1` and an `examples` array. Each term
`[i,j,"a/b"]` denotes \((a/b)x^i y^j\). The human-readable `expression` field is
explanatory text; the term list is the executable representation.

Expected residual coefficients refer to this fixed normalization. Write
\(b=f_{xy}(0)\), \(c=f_{yy}(0)\). If \(c\ne0\), substitute
\[
x=X,\qquad y=Y-(b/c)X.
\]
If \(c=0\), swap coordinates \(x=Y,y=X\), and use the resulting nonzero
\(Y\)-second derivative as \(c\). In either case put
\[
P(X,Y)=\operatorname{sign}(c)\bigl(f(x,y)-f(0,0)\bigr).
\]
Thus \(P_{YY}(0)>0\). The residual is \(g(X)=P(X,\phi(X))\), where
\(P_Y(X,\phi(X))=0\) and \(\phi(0)=0\). Reported classifications always concern
the **original** polynomial \(f\). In particular, a positive normalized residual
can produce a maximum when the original nonzero Hessian eigenvalue is negative.

`residual_order: null` and `normalized_leading_coefficient: null` mean
\(g\equiv0\). Here `non_strict_local_minimum` means a local minimum which is
not strict, and similarly for a maximum. The coefficient is the actual leading
power-series coefficient, without factorial rescaling.

## The degree-four stress test

For \(s\in\{1,-1\}\), let
\[
f_s(x,y)=(y-x^2)^2+s y^4.
\]
Its Hessian is \(\operatorname{diag}(0,2)\), so no coordinate or sign change is
needed. The critical equation and its local analytic solution are
\[
\phi+2s\phi^3=x^2,\qquad
\phi=x^2-2s x^6+12x^{10}-96s x^{14}+880x^{18}+O(x^{22}).
\]
On this branch \(\phi-x^2=-2s\phi^3\), giving the exact identity
\[
g=s\phi^4+4\phi^6
  =s x^8-4x^{12}+24s x^{16}+O(x^{20}).
\]
The coefficients through degree 18 were checked by independent truncated
integer polynomial arithmetic. Substitution into the critical equation gives
zero through degree 18. Consequently both polynomials have residual order
eight, although their total degree is only four.

There are also direct checks which use no implicit series. For \(s=1\), the
polynomial is a sum of two nonnegative quantities and their common zero is only
the origin, so the minimum is strict. For \(s=-1\),
\[
f_{-1}(x,x^2)=-x^8<0\quad(x\ne0),\qquad
f_{-1}(0,y)=y^2-y^4>0\quad(0<|y|<1).
\]
Thus it is a saddle. Their negatives test the negative-Hessian case: negating
the first gives a strict maximum, and negating the second remains a saddle.

## Zero residuals and non-strict extrema

For \((y-x^2)^2\), the critical branch is the parabola \(y=x^2\), and the
residual is identically zero. Every point of that parabola is a critical point
with the same value. The origin is a non-strict minimum; negation gives a
non-strict maximum. The quadratic-only example \(y^2\) similarly has a full
line of critical points and equality.

A more demanding example is
\[
f(x,y)=(y+y^2-x^2)^2.
\]
Near the origin, the factor \(1+2y\) in
\(f_y=2(y+y^2-x^2)(1+2y)\) is nonzero. Therefore
\[
\phi=\frac{\sqrt{1+4x^2}-1}{2}
     =x^2-x^4+2x^6-5x^8+14x^{10}-\cdots,
\qquad g\equiv0.
\]
The series \(\phi\) is infinite. A zero-residual certificate must allow such
algebraic analytic branches instead of requiring a polynomial branch. The
displayed square proves the non-strict minimum directly, and its negative
gives a non-strict maximum.

## Coordinate, sign, and arithmetic checks

| Polynomial | Normalized residual | Classification of the original polynomial |
|---|---|---|
| \((2x+3y)^2+x^6\) | \(X^6\) | Strict minimum |
| \(-(2x+3y)^2-x^6\) | \(X^6\) | Strict maximum |
| \(-(2x+3y)^2+x^6\) | \(-X^6\) | Saddle |
| \(x^2+y^4\) | \(X^4\), after swapping coordinates | Strict minimum |
| \(-x^2-y^4\) | \(X^4\), after swapping and sign normalization | Strict maximum |
| \(y^2+x^3\) | \(X^3\) | Saddle |
| \(y^2+2x^2y\) | \(-X^4\) | Saddle |
| \((y-x^2/3)^2+x^6/7\) | \(X^6/7\) | Strict minimum |
| \(y^2-x^4/10^{100}\) | \(-X^4/10^{100}\) | Saddle |

The first Hessian is
\(\begin{pmatrix}8&12\\12&18\end{pmatrix}\), and the prescribed rational shear
is \(y=Y-2X/3\). It gives \(9Y^2+X^6\) exactly. Its sign-reversed variants
check that normalization is correctly translated back to the original
classification. For the mixed saddle, the original polynomial is positive on
\(2x+3y=0\) and negative on \(x=0\).

For the cubic example \(y^2+2x^2y\), the critical branch is \(\phi=-X^2\).
Thus \(g=-X^4\), even though the restriction \(f(x,0)\) vanishes identically.
Directly, \(f(x,-x^2)=-x^4\) and \(f(0,y)=y^2\). Substituting the kernel line
for the actual critical branch would misclassify this example.

The tiny rational coefficient is deliberately nonzero and negative. An
arbitrary numerical zero threshold would lose its mathematical meaning.
The shifted example \(7+(y-x^2)^2+y^4\) checks that residual computations
subtract the critical value; its normalized residual still begins with
\(X^8\).

## A family with delayed residuals

For integers \(m\ge2\), \(n\ge3\), and \(s\in\{1,-1\}\), consider
\[
f(x,y)=(y-x^m)^2+s y^n.
\]
It has degree \(\max(2m,n)\), while its critical branch satisfies
\[
\phi+\frac{s n}{2}\phi^{n-1}=X^m,
\qquad \phi=X^m+\text{higher-order terms}.
\]
The residual identity
\[
g=s\phi^n+\frac{n^2}{4}\phi^{2n-2}
\]
proves that its leading term is \(sX^{mn}\), because \(2n-2>n\). Thus residual
orders can grow quadratically with the polynomial degree.

The data include two further degree-six instances. The polynomial
\((y-x^3)^2+y^4\) has order 12 and is a strict minimum, as its sum-of-squares
form also proves. The polynomial \((y-x^3)^2+y^3\) has order 9 and is a saddle:
on \(y=x^3\) its values are \(x^9\), which have both signs arbitrarily near
the origin. These examples test both even and odd delayed residuals.

## Local isolation despite a distant critical curve

The degree-five polynomial
\[
f(x,y)=(1+x)^2(y^2+x^3)
\]
has Hessian \(\operatorname{diag}(0,2)\) at the origin, so its normalization
does nothing. Since \(f_y=2(1+x)^2y\), its local critical branch is
\(\phi=0\), and
\[
g=x^3+2x^4+x^5.
\]
The leading coefficient is 1 and the order is 3. Independently,
\(f(x,0)=x^3(1+x)^2\) has both signs arbitrarily near zero, proving the saddle
classification directly.

The two gradients are
\[
f_x=(1+x)(2y^2+3x^2+5x^3),\qquad f_y=2(1+x)^2y.
\]
Both have the common factor \(1+x\), and the entire distant line \(x=-1\)
is critical. Nevertheless, at the origin the factors \(1+x\) and \(3+5x\)
are units in the local analytic ring. Its gradient ideal is therefore
\((y,x^2)\), and its local complex Milnor number is 2. This verifies
\(\mu=\operatorname{ord}(g)-1\) while distinguishing isolation at the origin
from global isolation. A finite local stopping bound must allow global common
gradient factors which are units at the origin.

## Scope of these checks

The 22 cases cover every classification, both signs of the nonzero Hessian
eigenvalue, coordinate swapping, a nonzero mixed quadratic coefficient,
nonzero critical value, exact nonintegral coefficients, finite and identically
zero residuals, residual orders exceeding total degree, and local isolation
despite a distant critical curve. Their ordinary
proofs and independent exact computations support the expected answers. This
is a regression collection, not a proof that an implementation is correct on
all inputs. It does not provide a certified neighborhood radius or a Lean
formalization. Smooth flat functions lie outside this polynomial/analytic
representation: their zero Taylor series alone cannot certify a zero residual.
