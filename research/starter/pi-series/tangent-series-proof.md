# Absolute convergence threshold for the tangent series

## Result and scope

Assume the following Diophantine approximation statement:

**H.** For every real \(\alpha>2\), there is an integer \(Q\ge2\) such that
\[
 \left|\pi-\frac pq\right|\ge q^{-\alpha}
 \qquad(p\in\mathbb Z,\ q\in\mathbb Z,\ q\ge Q).
\]

Then, for every real \(s\),
\[
 \sum_{n=1}^{\infty}\frac{|\tan n|}{n^s}<\infty
 \quad\Longleftrightarrow\quad s>1.
\]
Angles are in radians. The convergence direction (s > 1 implies convergence) is conditional on H. Divergence for \(s\le1\) is elementary and does not use H or equidistribution. Consequently, under H the signed series \(\sum \tan n/n^s\) is absolutely convergent for every \(s>1\). No conclusion about conditional convergence of the signed series for \(s\le1\) is asserted.

The proof gives the intermediate estimate, for every fixed \(\alpha>2\),
\[
 \sum_{N\le n<2N}|\tan n|
   =O_\alpha\bigl(N^{\alpha-1}(1+\log N)\bigr)
 \qquad(N\in\mathbb Z_{\ge1}).
\]
All constants may depend on the chosen exponent and its Diophantine bound, but not on \(N\). This is an aggregate estimate, stronger for summability purposes than summing a pointwise bound separately over every term.

## 1. Uniform treatment of small denominators

Fix \(\alpha>2\), and take \(Q\) from H. The hypothesis implies that \(\pi\) is irrational: a rational expression \(\pi=p_0/q_0\) with \(q_0>0\) would, after multiplication of numerator and denominator, contradict H at arbitrarily large denominators.

For each of the finitely many integers \(1\le q<Q\), set
\[
 m_q=\operatorname{dist}(q\pi,\mathbb Z)>0,
 \qquad
 c=\min\left(1,\min_{1\le q<Q}q^{\alpha-1}m_q\right)>0.
\]
Then \(0<c\le1\), and for every integer numerator \(p\) and every positive integer denominator \(q\),
\[
 \left|\pi-\frac pq\right|\ge c q^{-\alpha}. \tag{1}
\]
Indeed, for \(q<Q\), the left side is at least \(m_q/q\), which is at least \(c q^{-\alpha}\); for \(q\ge Q\), use H and \(c\le1\). Thus all later uses of (1), including small denominators, are justified. Fractions need not be in lowest terms.

## 2. Distance of each integer to the poles

Fix an integer \(N\ge1\). Define
\[
 \delta_N=\frac c2(3N)^{1-\alpha}. \tag{2}
\]
For each integer \(1\le n\le2N\), choose a nearest pole of tangent and write
\[
 d_n=\min_{k\in\mathbb Z}\left|n-(k+\tfrac12)\pi\right|
     =\left|n-\frac{q_n\pi}{2}\right|,
\]
where \(q_n\) is an odd integer. A nearest pole can be chosen positive: every negative pole is farther from a positive \(n\) than the positive pole \(\pi/2\). Thus \(q_n\ge1\). Also \(0<d_n\le\pi/2\), with positivity following from irrationality, and
\[
 q_n\le \frac{2n}{\pi}+1
       \le \frac{4N}{\pi}+1
       \le3N,
\]
where \(\pi>2\) and \(N\ge1\) suffice for the final inequality. Applying (1) with the **even numerator \(p=2n\)** and the **positive odd denominator \(q=q_n\)** gives
\[
 d_n=\frac{q_n}{2}\left|\pi-\frac{2n}{q_n}\right|
     \ge\frac c2q_n^{1-\alpha}
     \ge\delta_N. \tag{3}
\]
The last comparison has the displayed direction because \(1-\alpha<0\).

The elementary identity and inequality
\[
 |\tan n|=\cot d_n\le\frac1{d_n} \tag{4}
\]
hold for \(0<d_n\le\pi/2\). For \(0<d<\pi/2\), \(\tan d\ge d\), for example by integrating \((\tan d)'=\sec^2d\ge1\); at \(d=\pi/2\), \(\cot d=0\) also satisfies the inequality.

## 3. Pair spacing modulo pi

For distinct integers \(n,m\) in \([1,2N]\), let \(h=|n-m|\), and let
\[
 \rho(n,m)=\min_{r\in\mathbb Z}|h-r\pi|
\]
be their circular distance modulo \(\pi\). A minimizing integer \(r\) can be chosen nonnegative and satisfies
\[
 0\le r\le h/\pi+1/2\le2N/\pi+1/2\le3N.
\]
If \(r=0\), then \(\rho(n,m)=h\ge1\ge\delta_N\). If \(r\ge1\), apply (1) to the unrestricted integer numerator \(p=h\) and positive integer denominator \(q=r\):
\[
 \rho(n,m)=r\left|\pi-\frac hr\right|
       \ge c r^{1-\alpha}
       \ge c(3N)^{1-\alpha}
       =2\delta_N.
\]
In particular,
\[
 \rho(n,m)\ge\delta_N. \tag{5}
\]
This step uses the all-numerator, all-positive-denominator form of H. A hypothesis restricted only to the even-numerator/odd-denominator approximants used for tangent poles would not, by itself, supply (5).

## 4. Harmonic packing bound

Represent each residue \(n\pmod\pi\) by its signed distance \(y_n\) from the pole at \(\pi/2\), choosing \(y_n\in[-\pi/2,\pi/2)\). Then \(|y_n|=d_n\). There are no zero representatives because no positive integer is a pole.

Consider the \(N\) integers in the dyadic block \(N\le n<2N\), and separate their representatives into the positive and negative half-intervals. On either half-interval, list the distances from zero in increasing order:
\[
 0<a_1<a_2<\cdots<a_M\le\pi/2.
\]
Equation (3) gives \(a_1\ge\delta_N\). For consecutive points on the same side, their ordinary separation equals the difference of their distances and is at least their circular separation; (5) therefore gives \(a_{j+1}-a_j\ge\delta_N\). Consequently \(a_j\ge j\delta_N\), and
\[
 \sum_{j=1}^M\frac1{a_j}
    \le\delta_N^{-1}H_M,
 \qquad H_M=\sum_{j=1}^M\frac1j,
 \quad H_0=0.
\]
Applying this to both half-intervals and using \(M\le N\), equations (2) and (4) yield
\[
 \sum_{N\le n<2N}|\tan n|
   \le2\delta_N^{-1}H_N
   =\frac4c(3N)^{\alpha-1}H_N
   \le\frac{4\,3^{\alpha-1}}c
          N^{\alpha-1}(1+\log N). \tag{6}
\]
No equidistribution theorem or estimate for continued fractions is used.

## 5. Absolute convergence for every exponent above one

Fix \(s>1\), and choose \(\alpha\) with
\[
 2<\alpha<s+1.
\]
Since \(s>0\), equation (6) gives
\[
 \sum_{2^j\le n<2^{j+1}}\frac{|\tan n|}{n^s}
 \le C_\alpha(1+j\log2)\,2^{-j(s-\alpha+1)}.
\]
Here \(s-\alpha+1>0\). The series over \(j\ge0\) on the right converges, since it is a geometric series with a linear factor. These dyadic blocks partition the positive integers, proving absolute convergence.

Equivalently, for each \(\varepsilon>0\), taking \(\alpha=2+\varepsilon\) yields the block estimate \(O_\varepsilon(N^{1+\varepsilon}(1+\log N))\), and choosing \(0<\varepsilon<s-1\) proves convergence. This argument does not assert the stronger estimate \(O(N\log N)\), which would require a uniform exponent-two Diophantine constant or other additional input.

## 6. Divergence at and below one

This part uses only elementary trigonometry, \(\sin1>0\), and the fact that \(\cos n\ne0\) for integer \(n\), a consequence of the standard irrationality of \(\pi\). For every integer \(n\ge1\),
\[
 \begin{aligned}
  \sin1
   &=|\sin(n+1)\cos n-\cos(n+1)\sin n|\\
   &\le|\sin(n+1)|+|\sin n|\\
   &\le|\tan(n+1)|+|\tan n|.
 \end{aligned} \tag{7}
\]
Therefore, for each \(m\ge1\),
\[
 \frac{|\tan(2m-1)|}{2m-1}
 +\frac{|\tan(2m)|}{2m}
 \ge\frac{|\tan(2m-1)|+|\tan(2m)|}{2m}
 \ge\frac{\sin1}{2m}.
\]
Summing these disjoint pairs proves divergence to \(+\infty\) at \(s=1\). For every real \(s\le1\) and every integer \(n\ge1\), \(n^{-s}\ge n^{-1}\), so termwise comparison proves divergence for all \(s\le1\).

## Source and verification boundaries

- [OpenAI mathematics scope note 017](https://github.com/openai/math/blob/main/lean/docs/017.md), inspected on 2026-10-11, states the eventual all-rational bound used as H.
- [PiExponent comparator statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PiExponent.lean), inspected on 2026-10-11, states H as the first conjunct of `OAI.PiExponent.main`, together with a supremum characterization. The comparator file itself contains a placeholder proof; the comparator alone does not certify the theorem.
- [Main implementation at commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/PiExponent/Main.lean), inspected through its [raw source](https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/PiExponent/Main.lean) on 2026-10-11: lines 17–27 declare and assemble `OAI.PiExponent.main`; lines 18–20 give exactly H as its first conjunct. Lines 8–12 provide the named eventual-lower-bound declarations. This is a statement-level inspection of this file, not an audit of its imported proof dependencies.
- The mathematical argument above is a conditional consequence supplied in this audit. It is not a Lean theorem, does not prove H, and does not claim an executed Lean verification or a repository-wide proof audit. Only the eventual lower bound H is needed for convergence; the supremum characterization is unused.

