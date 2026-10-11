# Independent ordinary mathematical review

Date: 2026-10-11. Scope: radial contact with the unit sphere in an arbitrary real normed space. This review was conducted independently of the source archive and does not assert that any result below has been formalized in Lean. Formalization and compilation evidence belong to the implementation environment's separate build records.

## Provenance and limitations

At the time of this review, the source archive
`OpenAI-math-research-starter-2026-10-11.zip`, version 0, expected SHA256
`b87f7e32f3ccbef1bcbbb819b05dafdc1481260925f22689563474467d2555da`, was
unavailable after two supported transfer attempts. Its designated records were
`radial-maps/study.md` and `reviews/radial-review.json`.

This reviewer did not read that archive, verify its bytes, or inspect either designated record. Accordingly, “requested source-specification results” below means results explicitly requested in the task, not results checked against the unavailable archive. The mathematical arguments below were derived independently from that specification.

No assumptions of completeness, finite dimension, smoothness, strict convexity, or a nonempty unit sphere are used.

## Setup

Let `E` be a real normed space, let `c : E` satisfy `a = ‖c‖ < 1`, and put

\[
m=1-a>0,\qquad M=1+a>0.
\]

Let

\[
S=\{v\in E:\|v\|=1\}.
\]

For a positive contact radius `r` in direction `v ∈ S`, the contact equation is

\[
\|c+rv\|=1.
\]

The scalar products below denote real scalar multiplication in `E`.

## Requested source-specification results

### Existence and radius bounds

For a unit vector `v`, define the real-valued function

\[
f(t)=\|c+tv\|.
\]

This function is continuous. At the endpoints of `[0,M]`,

\[
f(0)=a<1,\qquad
f(M)\ge\|Mv\|-\|c\|=M-a=1.
\]

The intermediate value theorem therefore supplies `r ∈ [0,M]` with `f(r)=1`. Triangle inequalities give

\[
1=\|c+rv\|\le a+r,
\]

so `m ≤ r`; in particular, `r > 0`. Also,

\[
r=\|rv\|=\|(c+rv)-c\|\le1+a=M.
\]

Thus every positive contact radius satisfies

\[
1-\|c\|\le r\le1+\|c\|.
\]

The only intermediate value theorem needed is for a continuous real-valued function on a real interval. The target normed space need not be complete.

### A module identity for uniqueness and the quantitative bound

Suppose `v,w ∈ S`, `r,s > 0`, and

\[
x=c+rv,\quad y=c+sw,\quad\|x\|=\|y\|=1.
\]

Assume first that `r ≤ s`. The exact algebraic identity

\[
sx=ry+(s-r)c+rs(v-w)
\tag{1}
\]

uses only the real module laws. Taking norms, all scalar coefficients on the right are nonnegative, so

\[
s\le r+(s-r)a+rs\|v-w\|.
\]

Equivalently,

\[
(s-r)m\le rs\|v-w\|.
\tag{2}
\]

Identity (1) and inequality (2) avoid divisions until the final numerical estimate, making them convenient reusable intermediate lemmas for formalization.

For uniqueness, take `v=w`. Then (2) yields `(s-r)m ≤ 0`; since `s-r ≥ 0` and `m > 0`, it follows that `r=s`. If the radii were ordered the other way, interchange them first. Thus each unit direction has exactly one positive contact radius, denoted `ρ(v)`.

An alternative ordinary proof of uniqueness uses convexity: if `0<r<s` and `‖c+sv‖=1`, then

\[
c+rv=(1-r/s)c+(r/s)(c+sv),
\]

and hence

\[
\|c+rv\|\le(1-r/s)a+r/s<1.
\]

The strict inequality comes from the center being inside the ball; it does not require strict convexity of the norm.

### Radius Lipschitz estimate

Apply (2) to the contact radii and reverse their order if necessary. Using `r,s ≤ M` gives

\[
|\rho(v)-\rho(w)|
\le\frac{\rho(v)\rho(w)}m\|v-w\|
\le\frac{M^2}m\|v-w\|.
\]

The requested constant is therefore

\[
K=\frac{(1+\|c\|)^2}{1-\|c\|}.
\]

### Contact-map Lipschitz estimate

Define

\[
F(v)=c+\rho(v)v.
\]

For positive `r,s` and unit `v,w`, the triangle inequality, choosing the smaller radius as the coefficient of `v-w`, gives

\[
\|rv-sw\|\le|r-s|+\min(r,s)\|v-w\|.
\]

Consequently,

\[
\|F(v)-F(w)\|
\le\left(\frac{M^2}m+M\right)\|v-w\|
=\frac{2M}m\|v-w\|,
\]

because `m+M=2`. The requested constant is

\[
L=\frac{2(1+\|c\|)}{1-\|c\|}.
\]

### Normalized inverse on the unit sphere

For `x ∈ S`, put

\[
n_x=\|x-c\|,\qquad U(x)=n_x^{-1}(x-c).
\]

The reverse triangle inequality and the triangle inequality give

\[
m\le n_x\le M.
\]

Thus `n_x > 0`, and `‖U(x)‖=1`. The equation

\[
c+n_xU(x)=x
\]

shows that `n_x` is a positive contact radius in direction `U(x)`. Uniqueness therefore gives

\[
\rho(U(x))=n_x,\qquad F(U(x))=x.
\]

Conversely, positivity of `ρ(v)` and `‖v‖=1` imply

\[
\|F(v)-c\|=\|\rho(v)v\|=\rho(v),
\]

so scalar cancellation gives

\[
U(F(v))=v.
\]

Thus `F` and `U` are mutually inverse maps of `S`. The contact estimate above and the inverse estimate below make them continuous, yielding a homeomorphism.

### Empty sphere and zero center

If `S` is empty, the direction-indexed assertions are vacuous, and `F` and `U` are the unique maps from the empty subtype to itself. No choice of a unit vector should be required merely to define the maps. The zero vector space is included.

If `c=0` and `v ∈ S`, then `‖1v‖=1`, so uniqueness gives `ρ(v)=1`. Accordingly,

\[
F(v)=v,\qquad U(v)=v.
\]

The exact radius map is constant, and its optimal Lipschitz constant is `0`; the contact and inverse maps are identities and admit Lipschitz constant `1`. The general requested constants are still valid at zero center but are loose there. In an empty sphere, statements about optimal constants should be avoided or explicitly qualified.

## Additional derived results

These results were independently derived during review. They should be kept separate from any later account of the unavailable source archive.

### Reciprocal-radius estimate

Dividing the first radius estimate by the positive product `ρ(v)ρ(w)` gives

\[
\left|\frac1{\rho(v)}-\frac1{\rho(w)}\right|
\le\frac1m\|v-w\|.
\]

This is a stronger intermediate description than first replacing both radii by `M`.

### Inverse Lipschitz estimate

For nonzero vectors `u,z`, set `n=‖u‖`, `p=‖z‖`, and `d=‖u-z‖`. Suppose `n ≥ p`. The identity

\[
u/n-z/p=(u-z)/n+(1/n-1/p)z
\]

and `n-p ≤ d` give

\[
\|u/n-z/p\|\le\frac{d+n-p}{n}\le\frac{2d}{n}.
\]

Interchanging `u,z` if necessary yields the pointwise bound

\[
\|u/\|u\|-z/\|z\|\|
\le\frac{2\|u-z\|}{\max(\|u\|,\|z\|)}.
\]

Apply this with `u=x-c` and `z=y-c`; their norms are at least `m`, while `‖u-z‖=‖x-y‖`. Therefore

\[
\|U(x)-U(y)\|\le\frac2m\|x-y\|.
\]

### Sharpness of the radius and contact constants: ordinary proof only

The following finite-dimensional examples establish sharpness across the class of arbitrary real normed spaces for every fixed `0<a<1`. They are ordinary mathematical proofs, not claims of Lean formalization.

Use `E=ℝ³` with its maximum norm. Put `t=m/M`, and choose

\[
c=(-a,a,a),\qquad v=(1,-1,t),\qquad
w_\varepsilon=(1,-1+\varepsilon,t+\varepsilon),
\]

where `0<ε<1-t`. Then `‖c‖=a`, both directions have norm `1`, and

\[
\|v-w_\varepsilon\|=\varepsilon.
\]

The contacts have radii

\[
r=M,\qquad s=\frac m{t+\varepsilon}.
\]

Indeed, the first contact is `(1,-1,1)`. The second contact is

\[
(-a+s,\;a-s+s\varepsilon,\;1).
\]

Since `0<s<M` and `0<ε<1`, its first two coordinates lie in `[-1,1]`, while its third is exactly `1`. Thus it also has norm `1`.

The radius quotient is

\[
\frac{r-s}{\varepsilon}=\frac M{t+\varepsilon}
\longrightarrow\frac{M^2}m
\quad(\varepsilon\downarrow0).
\]

The difference between the contacts has maximum norm

\[
M-s+s\varepsilon=\frac{2\varepsilon}{t+\varepsilon}.
\]

Thus its Lipschitz quotient tends to

\[
\frac2t=\frac{2M}m.
\]

No smaller uniform radius or contact constant, depending only on `a`, works for all real normed spaces when `a>0`. The exact behavior at `a=0` is different, as stated above.

### Sharpness of the inverse constant: ordinary proof only

Again use the maximum norm on `ℝ³`, and fix `0<a<1`. Choose

\[
c=(a,0,0),\quad x=(1,m,-m),\quad
y_\varepsilon=(1,m+\varepsilon,-m+\varepsilon),
\]

where `0<ε<a`. Both `x,yε` are on the unit sphere, and `‖x-yε‖=ε`. Also,

\[
\|x-c\|=m,\qquad\|y_\varepsilon-c\|=m+\varepsilon.
\]

Their normalized inverse images are

\[
U(x)=(1,1,-1),\qquad
U(y_\varepsilon)=
\left(\frac m{m+\varepsilon},1,
\frac{-m+\varepsilon}{m+\varepsilon}\right).
\]

Therefore

\[
\frac{\|U(x)-U(y_\varepsilon)\|}{\|x-y_\varepsilon\|}
=\frac2{m+\varepsilon}
\longrightarrow\frac2m.
\]

So the inverse constant `2/(1-a)` is also optimal in this uniform sense for every `a>0`.

## Review conclusion

The requested existence, uniqueness, radius bounds, radius and contact Lipschitz estimates, and normalized inverse are mathematically valid with precisely the stated generality. The algebraic comparison identity (1) is a particularly useful reusable core. The empty-sphere and zero-center cases must be retained explicitly in definitions and theorem statements. This file is ordinary-proof evidence; it contains no Lean build or axiom-dependency certification.
