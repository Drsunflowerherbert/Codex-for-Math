# Analytic strictly convex outer approximation in finite dimensions

## Result and scope

Every nonempty compact convex subset of a Euclidean space of dimension \(d\geq1\) has arbitrarily close bounded, strictly convex open neighborhoods with regular real-analytic boundary. Their boundaries are real-analytically diffeomorphic to the unit sphere. The neighborhoods can be chosen compactly nested. This includes singletons and convex sets with empty interior in the ambient space.

This study checks only Lemma `lem:approx`, lines 457–511, of the pinned source listed in `source-provenance.json`. It reconstructs that planar lemma and develops its finite-dimensional extension. It does not assess the source's headline theorem or other arguments. All proofs here are ordinary mathematical proofs; no Lean verification or novelty is claimed.

The useful quantitative refinement separates angular resolution from geometric slack. Let

- \(d\geq1\), and let \(K\subset\mathbb R^d\) be nonempty, compact, and convex;
- \(L=\operatorname{diam}K\);
- \(0<\delta<\sqrt2\), and let \(D\subset S^{d-1}\) be a finite Euclidean \(\delta\)-net;
- \(N=|D|\), \(\varepsilon>0\), and \(t>\log N/\varepsilon\);
- \(h_K(u)=\max_{v\in K}\langle u,v\rangle\).

Define

\[
\Phi(x)=\sum_{u\in D}\exp\bigl(t(\langle u,x\rangle-h_K(u)-\varepsilon)\bigr),
\quad \Omega=\{\Phi<1\},\quad C=\{\Phi\leq1\}.
\]

Set

\[
c=1-\delta^2/2>0,\qquad
s=\delta\sqrt{1-\delta^2/4},\qquad
\eta=\varepsilon-\frac{\log N}{t}>0.
\]

Then

\[
K+B(0,\eta)\subset\Omega,\qquad
\overline\Omega=C,\qquad \partial\Omega=\{\Phi=1\},
\]

and the following nested error bounds hold:

\[
d_H(C,K)=\sup_{x\in C}\operatorname{dist}(x,K)
\leq \frac{\varepsilon+sL}{c}
\leq \frac{\varepsilon+\delta L}{1-\delta^2/2}.
\tag{1}
\]

Here \(B(0,\eta)\) is the open Euclidean ball and \(d_H\) is the Hausdorff distance between nonempty compact sets. Because \(K\subset C\), only the displayed one-sided excess contributes to that distance.

## 1. Direction nets and the exact denominator

Compactness of \(S^{d-1}\) gives a finite \(\delta\)-net for every \(\delta>0\). We use chordal Euclidean distance, not angular distance. For unit vectors \(u,v\),

\[
\langle u,v\rangle=1-\tfrac12\|u-v\|^2.
\tag{2}
\]

Consequently every unit vector \(v\) has a member \(u\in D\) with \(\langle u,v\rangle\geq c>0\). This is the reason the denominator is \(1-\delta^2/2\), rather than the weaker \(1-\delta\) used in the source.

In particular, \(D\) spans \(\mathbb R^d\). If a nonzero vector were orthogonal to every member of \(D\), apply the preceding positive inner-product statement to its normalization. There are at least two members of \(D\): a singleton direction cannot have positive inner product with its own negative. Including the coordinate directions \(\pm e_i\) is convenient but unnecessary at this resolution.

An elementary size bound is available if desired. A maximal set of sphere points with pairwise distances greater than \(\delta\) is a \(\delta\)-net. The open ambient balls of radius \(\delta/2\) about its points are disjoint and lie in the ball of radius \(1+\delta/2\). Comparing \(d\)-dimensional volumes gives

\[
N\leq(1+2/\delta)^d.
\tag{3}
\]

A finite maximal set exists by this same packing bound, or by total boundedness and a finite greedy selection. Equation (3) is a convenient bound, not an optimal sphere-covering estimate.

## 2. Enclosure, an explicit inner tube, and coercivity

For \(x\in K\), every support deficit satisfies \(\langle u,x\rangle-h_K(u)\leq0\). Hence

\[
\Phi(x)\leq N e^{-t\varepsilon}<1.
\tag{4}
\]

More generally, compactness supplies a nearest point \(w\in K\) to an arbitrary \(x\). For each unit \(u\),

\[
\langle u,x\rangle-h_K(u)
\leq\langle u,x-w\rangle\leq\|x-w\|.
\]

Thus

\[
\Phi(x)\leq N e^{t(\operatorname{dist}(x,K)-\varepsilon)}.
\tag{5}
\]

In particular, \(\operatorname{dist}(x,K)<\eta\) implies \(x\in\Omega\), proving the inner-tube inclusion. This argument does not require \(K\) to contain an ambient ball.

To prove full coercivity, fix \(p\in K\) and write \(R_p=\max_{v\in K}\|v-p\|\leq L\). For \(x\ne p\), choose \(u\in D\) with \(\langle u,(x-p)/\|x-p\|\rangle\geq c\). Since \(h_K(u)-\langle u,p\rangle\leq R_p\), a single summand gives

\[
\Phi(x)\geq\exp\bigl(t(c\|x-p\|-R_p-\varepsilon)\bigr).
\tag{6}
\]

Therefore \(\Phi(x)\to\infty\) as \(\|x\|\to\infty\), and all closed sublevels are bounded. Continuity makes \(C\) closed, so \(C\) is compact. A rough explicit radius is

\[
C\subset\overline B\left(p,\frac{R_p+\varepsilon}{c}\right).
\tag{7}
\]

The sharper error estimate (1) will be proved separately; coercivity does not presuppose it.

## 3. Analyticity, strict convexity, and boundary identification

A finite sum of exponentials of affine functions is real analytic. Its Hessian is

\[
D^2\Phi(x)=t^2\sum_{u\in D}
e^{t(\langle u,x\rangle-h_K(u)-\varepsilon)}\,uu^{\mathsf T}.
\]

For any nonzero \(v\),

\[
D^2\Phi(x)[v,v]
=t^2\sum_{u\in D}e^{t(\langle u,x\rangle-h_K(u)-\varepsilon)}
\langle u,v\rangle^2>0,
\tag{8}
\]

because \(D\) spans and all weights are positive. Restriction to a nonconstant line segment has strictly positive second derivative. Thus \(\Phi\) is strictly convex.

The set \(\Omega\) is open by continuity, nonempty by (4), and convex by convexity of \(\Phi\). Consequently it is connected and is a domain. It is bounded by (6). In fact, the stronger geometric strict-convexity property holds: for distinct \(x,y\in C\) and \(0<\lambda<1\),

\[
\Phi((1-\lambda)x+\lambda y)
<(1-\lambda)\Phi(x)+\lambda\Phi(y)\leq1.
\tag{9}
\]

Hence every open chord of \(C\) lies in \(\Omega\).

It is important to identify the boundary before using it. Continuity first gives \(\overline\Omega\subset C\). Fix \(p\in K\subset\Omega\). For every \(x\in C\) and \(0<r\leq1\), convexity gives

\[
\Phi((1-r)x+rp)\leq(1-r)\Phi(x)+r\Phi(p)<1.
\]

Letting \(r\downarrow0\) shows \(x\in\overline\Omega\). Thus \(C=\overline\Omega\). Since \(\Omega\) is open,

\[
\partial\Omega=\overline\Omega\setminus\Omega=\{\Phi=1\}.
\tag{10}
\]

No appeal to an unproved assertion that an entire level set is the boundary is needed.

## 4. Regularity and radial sphere parametrization

For a differentiable convex function, the supporting-gradient inequality is

\[
\Phi(p)\geq\Phi(x)+\langle\nabla\Phi(x),p-x\rangle.
\]

At \(x\in\partial\Omega\), it yields

\[
\langle\nabla\Phi(x),x-p\rangle\geq1-\Phi(p)>0.
\tag{11}
\]

In particular \(\nabla\Phi(x)\ne0\) on the level set. The real-analytic implicit function theorem applies locally: at least one partial derivative is nonzero, so \(\Phi=1\) is locally the graph of a real-analytic function of (d-1) coordinates. This proves that the boundary is a regular real-analytic embedded hypersurface.

For completeness, topology and global parametrization can be proved directly. Fix \(\theta\in S^{d-1}\) and put \(g_\theta(r)=\Phi(p+r\theta)\), \(r\geq0\). We have \(g_\theta(0)<1\) and \(g_\theta(r)\to\infty\) by coercivity. Continuity gives a positive radius \(\rho(\theta)\) at which \(g_\theta=1\).

There cannot be two such positive radii \(0<r_1<r_2\): convexity between (0) and \(r_2\) would imply

\[
g_\theta(r_1)\leq(1-r_1/r_2)g_\theta(0)+(r_1/r_2)g_\theta(r_2)<1.
\]

The same argument gives \(g_\theta(r)<1\) for \(r<\rho(\theta)\) and \(g_\theta(r)>1\) for \(r>\rho(\theta)\). Equation (11) now says

\[
\partial_r\Phi(p+r\theta)\big|_{r=\rho(\theta)}
\geq\frac{1-\Phi(p)}{\rho(\theta)}>0.
\tag{12}
\]

Apply the real-analytic implicit function theorem to \(F(r,u)=\Phi(p+ru)-1\) near \((\rho(\theta),\theta)\), with \(u\) temporarily allowed to vary in an ambient open subset of \(\mathbb R^d\). The nonzero derivative (12) makes the root locally real analytic in \(u\). Restricted to the sphere, these local root functions agree by uniqueness. Therefore \(\rho:S^{d-1}\to(0,\infty)\) is real analytic.

The map

\[
\Psi(\theta)=p+\rho(\theta)\theta
\tag{13}
\]

is a bijection onto \(\partial\Omega\), with inverse

\[
\pi(x)=\frac{x-p}{\|x-p\|}.
\]

The inverse is analytic away from \(p\), and \(p\notin\partial\Omega\). For a tangent vector \(v\perp\theta\),

\[
D\Psi(\theta)v=D\rho(\theta)v\,\theta+\rho(\theta)v.
\]

The two summands are orthogonal, so this derivative cannot vanish when \(v\ne0\). Thus \(\Psi\) is a real-analytic diffeomorphism and an embedded parametrization, not just a continuous bijection.

For \(d=2\), compose (13) with \(\theta(a)=(\cos a,\sin a)\). The resulting periodic curve \(\gamma\) is injective modulo \(2\pi\), and

\[
\|\gamma'(a)\|^2=|\rho'(a)|^2+\rho(a)^2>0.
\]

It is a regular real-analytic Jordan parametrization. This explicit argument supplies both the Jordan property and regularity.

For \(d=1\), \(S^0=\{-1,1\}\) is a zero-dimensional analytic manifold. The same argument gives two boundary points and a bounded open interval. Neither “Jordan curve” nor positive hypersurface curvature should be used in this dimension.

For \(d\geq2\), an optional strengthening follows from (8). With outward unit normal \(n=\nabla\Phi/\|\nabla\Phi\|\), the second fundamental form in the convention \(\mathrm{II}(v,v)=\langle D_vn,v\rangle\) is

\[
\mathrm{II}_x(v,v)=\frac{D^2\Phi(x)[v,v]}{\|\nabla\Phi(x)\|}>0
\]

for every nonzero tangent vector. Thus every approximating boundary has positive principal curvatures in that convention. No uniform lower curvature bound along an approximating sequence is asserted.

## 5. Quantitative Hausdorff error

For \(x\in C\), each positive summand of \(\Phi(x)\leq1\) is at most one. Therefore

\[
\langle u,x\rangle\leq h_K(u)+\varepsilon\qquad(u\in D).
\tag{14}
\]

If \(x\notin K\), compactness supplies a nearest point \(w\in K\). Write \(r=\|x-w\|>0\) and \(\nu=(x-w)/r\). For each \(v\in K\), convexity puts \(w+a(v-w)\) in \(K\) for \(0\leq a\leq1\). Minimality gives

\[
0\leq\|x-w-a(v-w)\|^2-\|x-w\|^2
=-2ar\langle\nu,v-w\rangle+a^2\|v-w\|^2.
\]

Divide by \(a>0\) and let \(a\downarrow0\) to obtain

\[
\langle\nu,v-w\rangle\leq0\quad(v\in K).
\tag{15}
\]

Nearest-point uniqueness is not needed for this argument.

Choose \(u\in D\) with \(\|u-\nu\|\leq\delta\), and choose \(v\in K\) attaining \(h_K(u)\). Put \(a=\langle u,\nu\rangle\geq c\). Equations (14) and (15) first give the requested simple refinement:

\[
cr\leq ar=\langle u,x-w\rangle
\leq\langle u,v-w\rangle+\varepsilon
\leq\delta L+\varepsilon.
\tag{16}
\]

Indeed, \(\langle u,v-w\rangle=\langle\nu,v-w\rangle+\langle u-\nu,v-w\rangle\leq\delta L\). This proves the denominator improvement without altering the source's numerator estimate.

A further elementary sharpening uses the tangential component. Decompose \(u=a\nu+b\), where \(b\perp\nu\). Because \(a\geq c>0\), (15) implies

\[
\langle u,v-w\rangle
\leq\langle b,v-w\rangle
\leq\sqrt{1-a^2}\,L\leq\sqrt{1-c^2}\,L=sL.
\tag{17}
\]

Together with (14), this proves \(r\leq(\varepsilon+sL)/c\). Points of \(K\) have distance zero, so taking the supremum proves (1). The positivity of \(a\) matters in (17); it is not valid to discard a nonpositive normal component after multiplying by a negative coefficient.

In angular language, a chordal radius \(\delta=2\sin(\alpha/2)\), \(0<\alpha<\pi/2\), gives

\[
d_H(C,K)\leq \varepsilon\sec\alpha+L\tan\alpha.
\tag{18}
\]

The estimate is a verified upper bound; no optimality of its numerical constant is claimed.

## 6. Recovery of the source lemma

Identify \(\mathbb C\) with \(\mathbb R^2\), set \(\varepsilon=\delta\), take \(0<\delta<1\), and include the four coordinate directions in \(D\), as in the source. Any \(t\) with \(Ne^{-t\delta}<1\) satisfies the hypotheses. The coordinate inequalities reproduce the source's common bounding rectangle. Equations (8)–(13) rigorously supply strict convexity and a regular real-analytic Jordan boundary, including for line segments and singletons.

The source's distance estimate

\[
\sup_{x\in C}\operatorname{dist}(x,K)
\leq\frac{\delta(1+L)}{1-\delta}
\]

is valid: replace the exact lower bound \(c=1-\delta^2/2\) in (16) by the weaker \(1-\delta\). The stronger bounds are

\[
\sup_{x\in C}\operatorname{dist}(x,K)
\leq\frac{\delta+\delta\sqrt{1-\delta^2/4}\,L}{1-\delta^2/2}
\leq\frac{\delta(1+L)}{1-\delta^2/2}.
\]

Taking \(\delta_j=1/(j+1)\) for \(j\geq1\) gives the lemma as stated. This choice need not make the neighborhoods nested; nesting requires an additional selection argument.

## 7. Compactly nested analytic neighborhoods

There are two useful forms of the selection argument.

### Arbitrary prescribed accuracy

Let \(a_j>0\) tend to zero. First choose any approximating neighborhood \(\Omega_1\) with error \(<a_1\). Suppose \(\Omega_j\) is chosen. The continuous distance function to the closed set \(\Omega_j^c\) is positive on the compact set \(K\), so

\[
m_j=\operatorname{dist}(K,\Omega_j^c)>0.
\tag{19}
\]

The complement is nonempty because \(\Omega_j\) is bounded and \(d\geq1\). Positivity is a consequence of compactness and containment; \(K\) itself need not have interior.

Choose the next barrier so that its error bound is less than \(\min\{a_{j+1},m_j/2\}\). This is possible by letting \(\delta,\varepsilon\downarrow0\). For \(x\in\overline\Omega_{j+1}\), a nearest point \(w\in K\) has \(\|x-w\|<m_j/2\). If \(x\in\Omega_j^c\), the definition of \(m_j\) would give \(\|x-w\|\geq m_j\), a contradiction. Hence

\[
\overline\Omega_{j+1}\subset\Omega_j.
\tag{20}
\]

Moreover,

\[
\operatorname{dist}(\overline\Omega_{j+1},\Omega_j^c)
\geq m_j-d_H(\overline\Omega_{j+1},K)>m_j/2.
\tag{21}
\]

All neighborhoods are bounded, strictly convex, and real analytic by the previous proof. Both intersections equal \(K\):

\[
\bigcap_j\Omega_j=\bigcap_j\overline\Omega_j=K.
\tag{22}
\]

The reverse inclusion follows because a point outside the closed set \(K\) has positive distance from it, eventually exceeding the approximation error.

### Explicit certified nesting

For the \(j\)-th barrier, (5) gives \(m_j\geq\eta_j\). Thus it is enough to require the next explicit error bound to be \(<\eta_j/2\); no computation of the exact distance (19) is necessary.

A particularly simple source-style schedule is available after fixing Euclidean units. Take

\[
\delta_1=\tfrac12,\quad
\delta_{j+1}=\frac{\delta_j}{8(1+L)},\quad
\varepsilon_j=\delta_j,\quad
t_j=\frac{2\log N_j}{\delta_j}.
\tag{23}
\]

Here \(N_j\geq2\), so the strict parameter condition holds, and \(\eta_j=\delta_j/2\). Since \(\delta_j\leq1\), the simple error bound is at most \(2(1+L)\delta_j\). Thus

\[
E_{j+1}\leq\delta_j/4<\eta_j,
\qquad
\operatorname{dist}(\overline\Omega_{j+1},\Omega_j^c)\geq\delta_j/4.
\]

This proves compact nesting directly. The use of the numerical quantity (1+L) in (23) reflects the normalization \(\varepsilon=\delta\); the two-parameter theorem is the scale-covariant formulation.

## 8. Examples and sharpness of the angular order

### A segment or singleton in dimension one

For \(K=[a,b]\subset\mathbb R\), let \(m=(a+b)/2\), \(L=b-a\), and \(D=\{-1,1\}\). Then

\[
\Phi(x)=2e^{-t(L/2+\varepsilon)}\cosh(t(x-m)).
\]

The domain is \((m-\rho,m+\rho)\), where

\[
\rho=\frac1t\operatorname{arcosh}\left(\frac{e^{t(L/2+\varepsilon)}}2\right).
\tag{24}
\]

The assumed \(t\varepsilon>\log2\) ensures \(L/2<\rho<L/2+\varepsilon\), so the exact Hausdorff error is \(\rho-L/2\in(0,\varepsilon)\). Taking \(a=b\) gives the singleton case with no exceptional argument. Although a general positive \(\delta\) can be assigned to this net, its actual covering error is zero, so the bound \(\varepsilon\) is the relevant one-dimensional estimate.

### A singleton in any dimension

Take \(K=\{p\}\) and \(D=\{\pm e_i:1\leq i\leq d\}\). This net has \(c=1/\sqrt d\), equivalently \(\delta^2=2-2/\sqrt d\) (zero if \(d=1\)). The barrier is

\[
\Phi(x)=2e^{-t\varepsilon}\sum_{i=1}^d\cosh(t(x_i-p_i)).
\]

Its exact maximal radius, hence its exact Hausdorff distance from the singleton, is

\[
\frac{\sqrt d}{t}\operatorname{arcosh}\left(\frac{e^{t\varepsilon}}{2d}\right).
\tag{25}
\]

To prove this, fix \(\sum_i(x_i-p_i)^2=r^2\). The function \(z\mapsto\cosh(t\sqrt z)=\sum_{k\geq0}t^{2k}z^k/(2k)!\) is convex for \(z\geq0\), as follows by its nonnegative second derivative (or convexity of each power and convergence). Jensen's inequality shows that the sum is minimized when all squared coordinates equal \(r^2/d\). Thus the largest admissible radius occurs on a diagonal and is given by (25). This exact example verifies enclosure of lower-dimensional \(K\) without any ambient-interior hypothesis.

### Balls have a better angular estimate

If \(K=\overline B(p,R)\), then \(h_K(u)=\langle u,p\rangle+R\). Equation (14) in a direction with inner product at least \(c\) gives \(c\|x-p\|\leq R+\varepsilon\). Therefore

\[
d_H(C,K)\leq\frac{\varepsilon+R\delta^2/2}{1-\delta^2/2}.
\tag{26}
\]

The angular contribution is quadratic for balls. This does not extend uniformly to all compact convex sets.

### Flat sets can force linear angular error

For \(K=[-a,a]\times\{0\}\), \(a>0\), let \(n\geq4\) be divisible by four and choose normals at angles \((2k+1)\pi/n\), \(0\leq k<n\). Their angular covering radius is \(\theta=\pi/n\), and their chordal covering radius is \(\delta_n=2\sin(\pi/(2n))\). The vertical direction lies halfway between two adjacent normals.

Let

\[
P_0=\{x:\langle u,x\rangle\leq h_K(u)\text{ for every }u\in D\}.
\]

For every admissible barrier, \(P_0\subset\Omega\), because each summand is at most \(e^{-t\varepsilon}\) there. The point

\[
z=(0,a\tan\theta)
\]

belongs to \(P_0\). For a normal of positive vertical component, its angular distance from the upward vertical is at least \(\theta\), so \(a\tan\theta\,u_2\leq a|u_1|=h_K(u)\); normals with nonpositive vertical component satisfy the inequality automatically. Hence

\[
d_H(C,K)\geq a\tan\theta
=\frac{L}{2}\frac{\delta_n\sqrt{1-\delta_n^2/4}}{1-\delta_n^2/2}.
\tag{27}
\]

Even arbitrarily small support slack and arbitrarily large \(t\) cannot remove this finite-direction error. Thus a universal quadratic-in-\(\delta\) angular bound fails for this construction on arbitrary compact convex \(K\). Equation (27) proves necessity of linear angular order, not optimality of the coefficient in (1).

An exact rational example uses the eight directions \((\pm3/5,\pm4/5)\) and \((\pm4/5,\pm3/5)\), with independent signs. Their covering constant is \(c=4/5\), so \(\delta^2=2/5\), and \((0,3a/4)\in P_0\). To verify the covering constant, write \(A=\max(|v_1|,|v_2|)\) and \(B=\min(|v_1|,|v_2|)\) for a unit vector \(v\). The maximum inner product with the eight normals is \((4A+3B)/5\), and

\[
(4A+3B)^2-16(A^2+B^2)=B(24A-7B)\geq0.
\]

Thus that maximum is at least \(4/5\), with equality on coordinate axes. The accompanying exact-arithmetic computation checks all eight support inequalities for the displayed point.

## 9. Useful consequences and limitations

### Stable maxima of continuous functions

Suppose \(C_j=\overline\Omega_j\) and \(E_j=d_H(C_j,K)\to0\). They all lie in one fixed compact set after discarding finitely many terms, and adding those finitely many compact sets preserves compactness. For any continuous real-valued \(f\) on a common compact neighborhood, let \(\omega_f\) be a modulus of continuity there. Containment and nearest points imply

\[
0\leq\max_{C_j}f-\max_K f\leq\omega_f(E_j)\longrightarrow0.
\tag{28}
\]

For an \(M\)-Lipschitz function the error is at most \(ME_j\). This is a reusable consequence of outer Hausdorff approximation and does not rely on any specific operator-theoretic theorem.

### Scale and translation

Translation of (K,x) by the same vector leaves the barrier values unchanged. Under a positive dilation by \(\lambda\), transform \(\varepsilon\) to \(\lambda\varepsilon\) and \(t\) to \(t/\lambda\), while keeping the angular net fixed. The domains and all distance bounds scale by \(\lambda\). Orthogonal coordinate changes are compatible when the direction net is rotated with the set.

### Essential assumptions and nonconclusions

1. **Convexity is essential.** The support function of a compact nonconvex set equals that of its closed convex hull; these barriers cannot resolve the missing points. For \(K=\{-1,1\}\subset\mathbb R\), every convex neighborhood contains (0), whose distance from \(K\) is one.
2. **Nonemptiness and compactness have real roles.** Nonemptiness defines an interior anchor and support values; compactness gives finite supports, support maximizers, nearest points, and a positive distance to a prior complement. Bounded neighborhoods cannot contain an unbounded set.
3. **The net threshold cannot simply be dropped.** At \(\delta=\sqrt2\), the set \(D=\{\pm e_1\}\subset S^1\) is a \(\delta\)-net but produces a strip independent of the second coordinate. Coercivity and positive Hessian fail. Additional spanning/positive-spanning assumptions may repair some properties, but not the displayed positive-denominator argument at that threshold.
4. **Spanning alone does not ensure coercivity.** In \(\mathbb R^2\), \(D=\{e_1,e_2\}\) gives a positive-definite Hessian for a sum of two exponentials but an unbounded sublevel toward the southwest. Our net condition gives both directional positivity and spanning.
5. **Strict parameter margin is sufficient and important.** If one uses only \(t\varepsilon=\log N\), a singleton \(K=\{p\}\) has \(\Phi(p)=1\), so it is not in the open neighborhood. This is an exact failure, not just a weakness in the proof.
6. **Finite-dimensionality is part of this construction.** In an infinite-dimensional inner-product space a finite set of directions has a nontrivial common orthogonal complement, along which the barrier is constant. Such a finite-direction sublevel cannot be bounded.
7. **No automatic nesting.** Decreasing \(\delta\) while changing nets and \(t\) does not itself prove inclusion of consecutive domains. Section 7 supplies the needed argument.
8. **No convergence of derivatives or uniform curvature is implied.** The limit may be a polytope, segment, or point; smooth boundaries can degenerate. The main theorem asserts Hausdorff convergence of sets.
9. **The dimension-zero convention is excluded.** In \(\mathbb R^0\), the only nonempty compact convex set is the whole one-point space and its boundary is empty; the sphere language would require a separate convention for \(S^{-1}\).
10. **Formalization and novelty remain separate.** The theorem records and roadmap are import candidates and proof guidance, not executed Lean results or claims that these approximation facts are new.

Positive definiteness of the Hessian at every point is also weaker than global uniform strong convexity. For the three normals \((1,0),(-1/2,\sqrt3/2),(-1/2,-\sqrt3/2)\), with singleton \(K=\{0\}\), the Hessian on the vertical unit vector at ((r,0)) is \((3/2)t^2e^{-t\varepsilon-tr/2}\), which tends to zero. Uniform positivity does hold on each individual compact sublevel by continuity and compactness.

### Exact finite-direction criterion

For any nonempty finite direction set, put

\[
c_D=\min_{v\in S^{d-1}}\max_{u\in D}\langle u,v\rangle.
\]

This minimum exists because a finite maximum of continuous functions is continuous. A finite positive weighted sum of exponentials with slopes (t u), \(t>0\), is coercive if and only if \(c_D>0\). Sufficiency follows by the argument of (6), with the finitely many fixed coefficients absorbed into a constant. If \(c_D\leq0\), a minimizing unit vector \(v\) satisfies \(\langle u,v\rangle\leq0\) for every \(u\in D\); the sum stays bounded along (x+rv), \(r\geq0\), so it is not coercive. If its strict sublevel is nonempty, that sublevel is unbounded along the same ray. The Hessian, by contrast, is positive definite everywhere if and only if \(D\) spans the space, directly from (8). These separate criteria explain the distinction in limitation 4.

For a singleton \(K=\{p\}\), fixed \(D\) with \(c_D>0\), fixed \(\varepsilon>0\), and varying \(t>\log N/\varepsilon\), the exact limiting Hausdorff error is \(\varepsilon/c_D\). Indeed, at direction \(v\), with \(m(v)=\max_u\langle u,v\rangle>0\), the radial boundary equation and maximum-versus-sum estimates give

\[
\frac{\varepsilon-\log N/t}{m(v)}\leq\rho_t(v)\leq\frac{\varepsilon}{m(v)}.
\]

Taking the maximum over \(v\) sandwiches the outer radius between \((\varepsilon-\log N/t)/c_D\) and \(\varepsilon/c_D\). If \(\delta\) is the exact chordal covering radius of \(D\), identity (2) gives \(c_D=1-\delta^2/2\). Thus the denominator in the singleton bound is asymptotically attained for a fixed finite net; the geometric diameter term has a separate origin.

## Dependency summary

The finite-dimensional theorem needs only finite sphere nets, compactness and elementary Euclidean geometry, differentiation of exponentials, convexity, the intermediate value theorem, and the real-analytic implicit function theorem. The quantitative error depends on nearest-point geometry and the exact unit-vector identity. Compact nesting depends on the error estimate and positive distance from a compact set to the complement of an open neighborhood. The source's headline theorem is not a dependency of any result in this study.
