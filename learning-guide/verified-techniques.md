# Verified techniques from selected OpenAI mathematics

A learning and research guide for an undergraduate mathematics major

Status snapshot: 11 October 2026, 03:32 UTC

## What to learn first

Start with radial geometry, finite-state termination, and positive-block matrix inequalities. Their hypotheses are concrete, their proofs expose useful structures, and small examples reveal exactly why the assumptions matter. Then study the two tangent arguments together: the improvement from a pointwise bound to a block estimate is more instructive than the final convergence statement alone. Finite Fourier analysis is the next bridge into algebra. Mixed moments are the most demanding analysis project here because the algebraic cancellation and the analytic justification must both be completed.

The common habit is to look for a certificate that can survive reuse: a positive margin, an exact squared deficit, a finite state space, a separation scale, or an integrable majorant. Each method below includes a trigger, proof skeleton, failure mode, and a bounded next question. These questions are proposed exercises or investigations, not claims that the literature lacks answers.

This guide extracts supporting arguments from particular source passages. It does not validate their manuscripts' headline claims, establish novelty, or estimate how many people are studying the collection. The revision-pinned [inventory](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/starter/catalog/inventory.md) records 719 active manuscripts in 372 families, three withdrawals, and other revisions. Three recorded withdrawals do not mean that only three manuscripts have problems. Counts of manuscripts, families, source declarations, and verified theorems answer different questions.

## What the verification labels mean

1. **Ordinary proof review:** a complete written argument has been checked, with its hypotheses and dependencies. This is mathematical evidence, not a proof-assistant certificate.
2. **Exact finite checks:** integer, rational, or symbolic computations verify specified examples and regression cases. They can catch mistakes in formulas and implementations. They do not prove a statement quantified over all inputs or justify an exchange of infinite operations.
3. **Lean compilation and scope checking:** particular formal statements have compiled in a specified project. Their types, hypotheses, imports, axiom dependencies, and build evidence determine what was checked. A declaration count alone does not identify that scope; compiling a conditional theorem does not prove its hypothesis. A comparator target containing a placeholder is not a proof certificate.

The [published build record](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/publication/evidence/CURRENT-CHECKS.json) reports fresh project-source builds on Lean 4.24.0 with pinned mathlib dependencies:

- [Radial geometry](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/radial-contact/README.md): **47 declarations**, covering existence, uniqueness, radius and contact estimates, the inverse map, the sphere homeomorphism, and selected derived refinements. Sharpness examples are not formalized; no blanket claim is made for every additional estimate in the prose study.
- [Egyptian fractions](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/egyptian-exact/README.md): **42 theorems**, including fixed-length cleanup, finite-state termination, the boundary counterexample, marker-preserving one-step padding, and its coarse one-step bound. The iterated bound in the ordinary supplement is a separate induction corollary, not a reported compiled theorem.
- [Sharp conditional tangent threshold](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/tangent-sharp/README.md): **78 declarations**, comprising 76 public and 2 private declarations. Sufficiency assumes `PiDiophantine`; divergence for exponents at most one is unconditional.

The tangent project does not prove the underlying Diophantine bound for pi. These counts concern the formal projects' actual declarations, not entire source manuscripts or all prose records. The published checks report no `sorryAx` or added axioms and retain types and axiom inventories. They freshly build the project sources using provisioned pinned dependencies, rather than rebuilding all of mathlib from scratch. The Egyptian receipt preserves an aggregate successful shell result and inspected build, theorem-inventory, and exact-check markers; individual command exit codes were not separately retained. The pinned publication commit is `e8b12891144385544976c0db277a64144837383d`.

Finite-field mixing, positive-block inequalities, and mixed-moment Lean projects are **in progress at this snapshot**. Their ordinary proofs and exact checks must not be relabeled as completed Lean results. Affine avoidance, transport stability, and convex approximation have the review scopes recorded in their accompanying studies, with no new Lean completion claimed here.

## 1 Convert a singularity into a rational approximation problem

**Trigger.** A sequence samples a function with poles, and the size of a term is governed by how close the sample lies to a pole. Examples include tangent, cotangent, and reciprocals of trigonometric functions.

**Prerequisites.** Trigonometric identities, rational approximation, negative powers, and comparison tests for series.

For one fixed exponent $\alpha>2$, suppose there is a constant $c>0$ such that

$$
\left|\pi-\frac pq\right|\ge c q^{-\alpha}
\qquad(p\in\mathbb Z,\ q\in\mathbb Z_{\ge1}).
\tag{1}
$$

The source input used by the studies is stronger in its range of exponents but initially only eventual:

$$
\forall\alpha>2\ \exists Q\ge2\ \forall p\in\mathbb Z\ \forall q\in\mathbb Z,
\quad q\ge Q\Longrightarrow
\left|\pi-\frac pq\right|\ge q^{-\alpha}.
\tag{H}
$$

Here $Q$ may depend on $\alpha$, but not on $p,q$. Fractions need not be reduced. This is a **hypothesis in the new tangent work**, not a conclusion established there. The [pinned source statement](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/PiExponent/Main.lean#L17-L27) identifies the proposed input; inspection of that declaration is separate from verifying its imported proof.

To pass from H to (1), absorb the finitely many small denominators into $c$. For $1\le q<Q$, irrationality gives $m_q=\operatorname{dist}(q\pi,\mathbb Z)>0$. One can take

$$
c=\min\left(1,\min_{1\le q<Q}q^{\alpha-1}m_q\right)>0.
$$

This finite minimum is an important reusable repair: an eventual estimate often becomes a global estimate after changing its constant.

**Proof skeleton.** For an integer $n\ge1$, let $q_n$ be a positive odd integer indexing a nearest tangent pole, and set

$$
d_n=\left|n-\frac{q_n\pi}{2}\right|,
\qquad 0<d_n\le\frac\pi2,
\qquad q_n\le An,
\quad A=1+\frac2\pi.
$$

The exact interface between geometry and arithmetic is

$$
d_n=\frac{q_n}{2}\left|\pi-\frac{2n}{q_n}\right|
\ge\frac c2 q_n^{1-\alpha}
\ge\frac c2(An)^{1-\alpha}.
$$

Because $|\tan n|=\cot d_n\le1/d_n$, this gives

$$
|\tan n|\le\frac2c A^{\alpha-1}n^{\alpha-1}.
\tag{2}
$$

The comparison involving $q_n\le An$ reverses direction after raising to $1-\alpha<0$. Write that step explicitly.

**Worked consequence.** Under H, choose $\alpha=5/2$. Then $|\tan n|\le Cn^{3/2}$, so

$$
\frac{\tan n}{n^3}\longrightarrow0,
\qquad
\sum_{n=1}^{\infty}\frac{|\tan n|}{n^3}
\le C\sum_{n=1}^{\infty}n^{-3/2}<\infty.
$$

For a fixed $\alpha$, (2) proves the scaled limit when $s>\alpha-1$, but absolute convergence by this comparison only when $s>\alpha$. Under H this gives limits for all $s>1$, yet only the nonsharp series result for $s>2$.

**Failure modes.** Losing the factor $q_n/2$; using the estimate below its denominator threshold; assuming unreduced denominators remain large after reduction; silently setting $\alpha=2$; inferring divergence because a chosen majorant diverges. The pointwise argument only uses even numerators and odd denominators. The next method needs more.

**Next question.** For a periodic function with a pole of order $\gamma>0$, replace $1/d_n$ by $d_n^{-\gamma}$. Derive both a pointwise bound and a block bound, explicitly recording the Diophantine assumptions each needs.

Further proof and review: [pointwise bridge](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/starter/pi-bridge/study.md), [independent tangent review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/starter/reviews/pi-review.md).

## 2 Replace a worst case bound by separation and harmonic packing

**Trigger.** A pointwise estimate is too expensive when summed over a large block. Ask whether many terms can all be close to their worst case simultaneously.

**Prerequisites.** Method 1, distance on a circle, harmonic sums, and dyadic decomposition.

Retain (1), with $0<c\le1$, and fix an integer $N\ge1$. Put

$$
\delta_N=\frac c2(3N)^{1-\alpha}.
$$

Every integer $1\le n\le2N$ is at least $\delta_N$ from the nearest pole. There is also a **different estimate**, concerning two distinct sample points:

$$
\rho(n,m)=\min_{r\in\mathbb Z}|n-m-r\pi|\ge\delta_N.
\tag{3}
$$

To prove it, let $h=|n-m|$ and choose a nearest nonnegative integer $r\le3N$ to $h/\pi$. If $r=0$, the distance is $h\ge1$. If $r\ge1$, apply (1) to $h/r$. This is why the pole-only parity class is insufficient: pair spacing uses general integer numerators and positive denominators.

**Packing lemma.** Let $\delta>0$. Suppose positive distances satisfy

$$
a_1\ge\delta,\qquad a_{j+1}-a_j\ge\delta.
$$

Induction gives $a_j\ge j\delta$, and therefore

$$
\sum_{j=1}^{M}\frac1{a_j}\le\frac1\delta
\sum_{j=1}^{M}\frac1j=\frac{H_M}{\delta}.
$$

For the tangent block, represent residues by signed distances from a pole and sort the positive and negative sides separately. Equation (3) supplies the spacing on each side. The block $N\le n<2N$ contains exactly $N$ integers, so

$$
\sum_{N\le n<2N}|\tan n|
\le 2\delta_N^{-1}H_N
\le\frac{4\,3^{\alpha-1}}c
N^{\alpha-1}(1+\log N).
\tag{4}
$$

Summing the pointwise bound over $N$ terms would instead cost order $N^\alpha$. Separation avoids charging every point the smallest possible distance.

**Worked consequence.** Given $s>1$, choose $2<\alpha<s+1$ in H. On the block $[2^j,2^{j+1})$, (4) gives

$$
\sum_{2^j\le n<2^{j+1}}\frac{|\tan n|}{n^s}
\le C_\alpha(1+j\log2)2^{-j(s-\alpha+1)}.
$$

The exponent is positive, so summing over $j\ge0$ proves absolute convergence. Divergence for $s\le1$ has a separate elementary proof:

$$
|\tan n|+|\tan(n+1)|\ge\sin1.
$$

Pairing $2m-1,2m$ yields a contribution at least $\sin1/(2m)$ at $s=1$; comparison handles smaller $s$. Thus H implies the exact absolute-convergence threshold $s>1$. This says nothing about conditional convergence of the signed series at $s\le1$.

**Failure modes.** Confusing distance to the pole with pair spacing; omitting the $r=0$ case; assuming equidistribution; replacing a family of $\alpha>2$ estimates by one uniform exponent-two constant. No $O(N\log N)$ bound follows from this argument alone.

**Next question.** Prove the abstract packing bound $\sum a_j^{-\gamma}\le\delta^{-\gamma}\sum j^{-\gamma}$ and identify the different behaviors for $\gamma<1$, $\gamma=1$, and $\gamma>1$. This isolates the reusable lemma from tangent arithmetic.

Further proof: [sharp series study](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/starter/pi-series/tangent-series-proof.md).

## 3 Prove termination with a finite state space and a monotone statistic

**Trigger.** A rewrite rule preserves an object but may create new defects elsewhere. Directly counting defects need not decrease. Look instead for finitely many possible states and a statistic that strictly changes at every step.

**Prerequisites.** Induction, positive rational sums, and elementary divisibility.

Fix $k\ge1$ and $x>0$. There are only finitely many sorted positive-integer lists $n_1\le\cdots\le n_k$ with

$$
x=\sum_{i=1}^{k}\frac1{n_i}.
$$

Indeed, $x\le k/n_1$, so $n_1\le\lfloor k/x\rfloor$. After each choice, apply induction to the positive remainder and the remaining $k-1$ terms. Positivity of the remainder must be checked when terms remain.

For duplicate removal, strengthen the hypothesis to $0<x<1$. A repeated denominator cannot be 1 or 2. Replace equal pairs using

$$
\frac2{2p}=\frac1{p+1}+\frac1{p(p+1)}\quad(p\ge2),
$$

$$
\frac2{2p+1}=\frac1{p+1}+\frac1{(p+1)(2p+1)}\quad(p\ge1).
$$

Both rules preserve the total and list length. They increase the sum of denominators by $(p-1)^2>0$ and $2p^2>0$, respectively. After sorting, the state remains in the same finite set. Strict increase prevents repetition of a state, so every sequence of valid rewrites terminates. A terminal state has no repeated denominators.

**Worked example.** The list $[6,6,6]$ represents $1/2$. Replacing one equal pair gives $[4,6,12]$, since

$$
\frac16+\frac16=\frac14+\frac1{12}.
$$

The length stays three and the denominator sum increases from 18 to 22. In general the new denominators can collide with retained ones; the termination proof deliberately permits that.

A related construction pads a *distinct expansion of one* with at least three terms while preserving a specified denominator. Those hypotheses differ from cleanup. For example, preserving 6 in $[2,3,6]$, split $1/3=1/4+1/12$, obtaining $[2,4,6,12]$. The full padding proof handles exceptional collisions separately. Let $M_j$ be the largest denominator after $j$ padding steps. Its construction gives the coarse bound

$$
M_{j+1}\le M_j(M_j+1),\qquad
M_t\le(M_0+1)^{2^t}-1.
$$

This is a size bound, though not an economical one. The iterated formula follows by applying $M_{j+1}+1\le(M_j+1)^2$ inductively. Its supplemental write-up has not received a separate independent review or reported Lean formalization.

**Failure modes.** Strict increase alone does not prove termination on an infinite state space. Finiteness alone does not prevent cycles. A fixed runtime guard is not a universal complexity theorem. Cleanup at $x=1$ fails: $[2,2]$ cannot become a distinct two-term expansion of one. Preserving one marked denominator does not mean preserving every original denominator.

**Next question.** For fixed rational $x$ and length $k$, use the finite enumeration tree to derive a computable upper bound on the number of cleanup steps. Then compare it with observed traces. Keep an existence bound, a practical algorithm, and an optimal complexity bound separate.

Source: [removing repetitions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/elementary.tex), [marker padding](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/prescribed.tex). Use the [corrected study](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/reviews/egyptian/corrected/study.md) and [independent review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/reviews/egyptian/review.md).

## 4 Normalize Fourier analysis before using convolution mixing

**Trigger.** Prove that every value can be represented by a sum of several independently sampled algebraic expressions. Fourier coefficients quantify the departure from uniformity.

**Prerequisites.** Finite fields, complex numbers, finite probability, and Cauchy–Schwarz. No infinite Fourier series is needed.

Let $p$ be prime, let $A,B\subseteq\mathbb F_p$ be nonempty, and let $X,Y$ be independent uniform samples from them. Write $a=|A|$, $b=|B|$, and

$$
e_p(z)=\exp(2\pi i\widetilde z/p),\qquad
\widehat\mu_Z(r)=\mathbb E e_p(rZ).
$$

The value is independent of the integer representative $\widetilde z$. With this normalization $\widehat\mu_Z(0)=1$, and inversion is

$$
\Pr(Z=t)=\frac1p\sum_{r\in\mathbb F_p}e_p(-rt)\widehat\mu_Z(r).
$$

**Proof skeleton.** For $r\ne0$, put $T_x=\sum_{y\in B}e_p(rxy)$. Cauchy–Schwarz, extension of a nonnegative sum, and character orthogonality give

$$
\left|\sum_{x\in A}T_x\right|^2
\le a\sum_{x\in\mathbb F_p}|T_x|^2
=a\sum_{y,y'\in B}\sum_{x\in\mathbb F_p}e_p(rx(y-y'))
=pab.
$$

Only the $b$ diagonal pairs survive. Dividing by $(ab)^2$ and taking square roots yields

$$
|\widehat\mu_{XY}(r)|\le\sqrt{p/(ab)}.
$$

For independent products $U_1,\ldots,U_k$, their sum has Fourier coefficient $\prod_{i=1}^k\widehat\mu_{U_i}(r)$. If each nonzero-frequency bound is $\beta$, then

$$
\left|\Pr\left(\sum_{i=1}^kU_i=t\right)-\frac1p\right|
\le\frac{p-1}{p}\beta^k.
\tag{5}
$$

Keep the exact number $p-1$ of nonzero frequencies: a small saved factor can decide strict positivity.

**Worked consequence.** For $A=B=H$, write $h=|H|$. If $h^4\ge p^3$, then four products satisfy $\beta^4=p^2/h^4\le1/p$. Thus

$$
\Pr\left(\sum_{i=1}^4X_iY_i=t\right)
\ge\frac{1-(p-1)/p}{p}=\frac1{p^2}>0.
$$

Every residue therefore has a representation, allowing repetitions. At $p=7$, any five-element $H$ meets $5^4\ge7^3$.

The general sufficient criterion is $(p-1)(\sqrt p/h)^k<1$, equivalently $h^{2k}>(p-1)^2p^k$. The integer form is preferable for exact boundary checks. This local four-product deduction improves the source passage's five-product step; it does not establish a global Egyptian-fraction constant or an optimal product count.

**Failure modes.** Sampling $XY$ is not uniform sampling from its set of possible values. Uniform marginals do not imply independence: in $\mathbb F_5^*$, taking $Y=X^{-1}$ makes every product 1. Composite rings have zero divisors, so the off-diagonal orthogonality argument can fail. A zero lower bound does not imply a positive probability.

**Next question.** Derive the weighted version using collision probabilities $\sum_x\Pr(X=x)^2$ and $\sum_y\Pr(Y=y)^2$ in place of reciprocal set sizes. State exactly which independence assumptions remain necessary.

Source: [product mixing passage](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/prescribed.tex#L326-L366). Further details: [study](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/finite-field-mixing/study.md), [independent review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/reviews/finite-field-mixing/independent-review.md).

## 5 Turn positivity into a Gram identity and an equality certificate

**Trigger.** A positive block matrix controls an off-diagonal block. Factor the entire positive matrix before trying entrywise bounds or inverses.

**Prerequisites.** Complex matrices, adjoints, trace, positive semidefiniteness, and the finite-dimensional spectral theorem.

Suppose

$$
\Delta=\begin{pmatrix}A&B\\B^*&C\end{pmatrix}\succeq0,
\quad A\in\mathbb C^{p\times p},\ B\in\mathbb C^{p\times q},\ C\in\mathbb C^{q\times q},\quad p,q\ge1.
$$

Use the unnormalized Hilbert–Schmidt norm $\|T\|_{\rm HS}^2=\sum_{i,j}|T_{ij}|^2$. Choose a Gram factorization

$$
\Delta=[X\ Y]^*[X\ Y],
\qquad A=X^*X,\ B=X^*Y,\ C=Y^*Y.
$$

Although $A,C$ may have different sizes, $P=XX^*$ and $Q=YY^*$ have the same size. Put $a=\|A\|_{\rm HS}$, $c=\|C\|_{\rm HS}$, $\beta=\|B\|_{\rm HS}^2$. Trace cyclicity gives

$$
a^2+c^2-2\beta=\|P-Q\|_{\rm HS}^2\ge0.
\tag{6}
$$

This identity proves $2\beta\le a^2+c^2$ and identifies sum equality as $P=Q$.

If $a,c>0$, either Cauchy–Schwarz on $P,Q$ or the scaling $sP,s^{-1}Q$, with $s=\sqrt{c/a}$, gives $\beta\le ac$. Better still,

$$
ac-\beta=\frac{ac}{2}
\left\|\frac Pa-\frac Qc\right\|_{\rm HS}^2.
\tag{7}
$$

Equality therefore means proportional auxiliary Gram matrices, $Q=(c/a)P$. If $a=0$ or $c=0$, positivity forces $B=0$; handle this before division. Product equality then holds, while sum equality requires all three blocks to vanish.

**Worked example.** Take $X=[1]$, $Y=[2i]$. Then $A=[1]$, $B=[2i]$, $C=[4]$, so $(a,c,\beta)=(1,4,4)$. Product equality holds, but the sum gap is $1+16-8=9$. This distinguishes two equality conditions often conflated.

Equation (7) is also a stability certificate: if $\beta\ge(1-\varepsilon)ac$, then $\|P/a-Q/c\|_{\rm HS}\le\sqrt{2\varepsilon}$. It certifies closeness of the normalized auxiliary matrices; a conclusion about particular factors or original blocks requires additional work.

**Failure modes.** Positivity of $A,C$ alone is insufficient: scalar blocks $A=C=1,B=2$ violate the inequality. Do not invert singular diagonal blocks. A trace inequality does not automatically become a matrix inequality in the positive semidefinite order. Equality need not mean rank one.

**Next question.** Starting from (7), determine which additional hypotheses turn closeness of normalized Gram matrices into closeness of factors after a unitary change of coordinates. First test rank-deficient examples to see why a lower singular-value bound may matter.

Source: [positive block comparison](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/build/main.tex#L434-L445). Further details: [study](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/positive-blocks/study.md), [independent review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/reviews/positive-blocks/parent-independent-review.md).

## 6 Make geometric existence stable under changing parameters

**Trigger.** A construction is defined implicitly by first contact with a boundary. Existence and uniqueness are useful, but a reusable construction also needs quantitative dependence on its parameters.

**Prerequisites.** Normed spaces, the intermediate value theorem, convex combinations, and Lipschitz continuity.

Let $X$ be a real normed space and $\|c\|=r<1$. Write $a=1-r>0$, $U=1+r$, and $S_X=\{v:\|v\|=1\}$. Define the scalar-valued radius function and the sphere-valued contact map separately:

$$
\rho_c:S_X\to(0,\infty),\qquad
P_c:S_X\to S_X,\quad P_c(v)=c+\rho_c(v)v.
$$

For fixed $v$, let $h_v(t)=\|c+tv\|$. It is continuous, $h_v(0)<1$, and $h_v(U)\ge1$, so a positive contact exists. If $0<s<t$ both had norm one, then

$$
c+sv=(1-s/t)c+(s/t)(c+tv)
$$

would have norm strictly below one. Thus contact is unique, even for a norm with flat faces. Triangle inequalities give $a\le\rho_c(v)\le U$.

**Quantitative step.** Put $R=\rho_c(v)$. Convex combinations before and after contact give

$$
|h_v(t)-1|\ge\frac aR|t-R|\qquad(t\ge0).
\tag{8}
$$

For $S=\rho_c(w)$, norm continuity gives $|h_v(S)-1|\le S\|v-w\|$. Combining it with (8),

$$
|R-S|\le\frac{RS}{a}\|v-w\|,
\qquad
\left|\frac1R-\frac1S\right|\le\frac1a\|v-w\|.
$$

Consequently $\rho_c$ is Lipschitz with constant $U^2/a$, and $P_c$ has the valid Lipschitz bound $2U/a$. For centers $\|c\|,\|d\|\le q<1$, the uniform parameter estimate is

$$
|\rho_c(v)-\rho_d(w)|
\le\frac{1+q}{1-q}\|c-d\|
+\frac{(1+q)^2}{1-q}\|v-w\|.
\tag{9}
$$

The margin $1-q$ makes the construction stable; constants can deteriorate as the center approaches the boundary.

**Worked example and computation certificate.** In $\mathbb R$, $c=1/2$ and nonunit direction $u=2$ give $|1/2+2t|=1$ at $t=1/4$. Unit-direction bounds cannot be applied unchanged: the correct parameter is $\rho_c(u/\|u\|)/\|u\|$. For unit $v$ and trial parameter $t\ge0$, (8) also gives a posterior error certificate

$$
|t-\rho_c(v)|\le\frac Ua\left|\|c+tv\|-1\right|.
$$

If a norm evaluation has certified error $\varepsilon$, add $\varepsilon$ inside the final parentheses. An uncertainty interval containing 1 cannot determine a bisection side.

**Failure modes.** The function $h_v$ need not be monotone before contact. Strict convexity and ambient compactness are unnecessary. At a boundary center, contact may be absent or nonunique. A scalar root parameter and the point it selects are different objects.

**Next question.** Extend the crossing argument to a convex sublevel set $\{F\le1\}$ with an interior point and a uniform interior margin. Identify what supplies bounded contact radii and a quantitative perturbation bound for $F$.

Source: [radial lemma](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/build/main.tex#L135-L143). Further details: [study](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/starter/radial-maps/study.md), [review scope](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/starter/reviews/radial-review.json).

## 7 Separate algebraic cancellation from analytic interchange

**Trigger.** A family of integrals has a recurrence and takes values in the span of a few constants. Seek an exact coordinate formula, then impose polynomial conditions that cancel an unwanted coordinate.

**Prerequisites.** Improper or Lebesgue integration, dominated convergence, Tonelli and Fubini, power series, and rational polynomial arithmetic. This is the largest prerequisite step in the guide.

For $f(t)=\sqrt{1-t^2}$ on $(-1,1)$ and integers $i,j\ge0$, define

$$
M(i,j)=\int_{-1}^{1}\int_0^1
\frac{|t|t^is^j}{f(t)(1-ts)}\,ds\,dt,
\qquad
Z(i,j)=\int_0^1\int_0^1\frac{t^is^j}{1-ts}\,ds\,dt.
$$

Let $G=\sum_{r=0}^{\infty}(-1)^r/(2r+1)^2$, $\zeta_2=\sum_{n=1}^{\infty}n^{-2}$, and $c_r=4^{-r}\binom{2r}{r}$ for integers $r\ge0$. Expressions $c_{a/2}$ are defined to be zero when the integer $a$ is negative or odd.

**Analytic obligation first.** On either half of the $t$-interval, the integrated sum of absolute values of the geometric-series terms is controlled by

$$
\frac{-\log(1-u)}{\sqrt{1-u^2}},\qquad 0<u<1.
$$

Near 1 this is at most $(1-u)^{-1/2}|\log(1-u)|$, which is integrable. Near 0 it is $O(u)$. This justifies the series–integral interchange even on the negative half, where signs alternate. Bounded polynomial factors preserve the bound. Pointwise convergence of the geometric series would not suffice.

**Algebraic skeleton.** The one-variable moments

$$
m_i=\int_{-1}^{1}\frac{|t|t^i}{f(t)}\,dt
$$

are rational: odd moments vanish, $m_0=2$, and $(i+1)m_i=i m_{i-2}$ for $i\ge1$, with the explicit convention $m_{-1}=0$. One obtains

$$
M(i,j)=\sum_{u=0}^{\infty}\frac{m_{i+u}}{j+u+1},
\qquad
M(i,j)-M(i+1,j+1)=\frac{m_i}{j+1}.
$$

Finite diagonal reductions and boundary recurrences give rational arrays $M^0,Z^0$ such that

$$
M(i,j)=M^0(i,j)+4G c_{(i-j)/2}
+\frac32\zeta_2 c_{(j-i-1)/2},
$$

$$
Z(i,j)=Z^0(i,j)+[i=j]\zeta_2.
$$

For $P(t)=\sum_i p_it^i$ and $D(t)=\sum_i d_it^i$ in $\mathbb Q[t]$, extend $M,Z$ by finite linearity. The resulting expression has the exact form

$$
M(P,j)-\frac32Z(D,j)=A_j+B_jG+\frac32E_j\zeta_2,
$$

where $A_j,B_j,E_j\in\mathbb Q$, and

$$
E_j=\sum_i p_i c_{(j-i-1)/2}-d_j
=[t^j]\left(\frac{tP(t)}{\sqrt{1-t^2}}-D(t)\right).
\tag{10}
$$

Thus Taylor contact of order $L$, meaning $tP(t)/\sqrt{1-t^2}-D(t)=O(t^L)$, kills the displayed $\zeta_2$-coordinate for every $0\le j<L$. The value then belongs to $\mathbb Q+\mathbb QG$.

**Worked example.** Take $P=1,D=t,L=3$. Since $t/\sqrt{1-t^2}-t=\tfrac12t^3+O(t^5)$, the first three values are

$$
j=0:\ 4G-\frac32,\qquad
j=1:\ \frac32,\qquad
j=2:\ \frac54.
$$

At $j=3$, the value is $\tfrac34\zeta_2-\tfrac18$, so its specified $\zeta_2$-coordinate survives.

**Failure modes.** A coordinate in a specified formal decomposition is not an intrinsic coordinate of a real number unless independence is proved. The evaluation map

$$
\mathbb Q^3\longrightarrow\mathbb R,
\qquad(a,b,c)\longmapsto a+bG+c\zeta_2
$$

is not assumed injective. A nonzero displayed $\zeta_2$-coordinate therefore does not establish nonmembership in $\mathbb Q+\mathbb QG$. The column condition is $j<L$, not $j\le L$. Exact rational checks of the recurrences do not prove the analytic exchanges, and none of this proves irrationality of $G$.

**Next question.** Build the matching polynomial $D$ as the Taylor truncation of $tP/\sqrt{1-t^2}$, then determine all rational test polynomials $Q(s)=\sum_jq_js^j$ satisfying the weaker single condition $\sum_jq_jE_j=0$. This is finite rational linear algebra after the analytic theorem is established.

Source: [moment foundations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/foundations.tex). Further details: [study](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/mixed-moments/study.md), [audit](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/mixed-moments/audit.md).

## 8 Normalize all scales and pay for the union with a summable budget

**Trigger.** A local or normalized construction works on a compact range of scales. To handle arbitrary scales, normalize each one and ensure the costs of all rescaled constructions remain summable.

**Prerequisites.** Lebesgue measure, periodic sets, geometric series, and quantifier order.

Let $(a_n)_{n\ge1}$ be any real sequence. Assume there is a constant $C>0$ such that, for every $p\in(0,1)$, an open 1-periodic set $H_p$ exists with

$$
m(H_p\cap[0,1))\le Cp,
\qquad
\forall y\in\mathbb R\ \forall t\in[1,2)\ \exists n\ge1:
\quad y+ta_n\in H_p.
\tag{11}
$$

The order is $\forall p\ \exists H_p\ \forall y\ \forall t\ \exists n$. Choosing a different set for every $(y,t)$ is not enough.

**Proof skeleton.** Fix $0<\eta<1$, put $B=\max(1,C)$, and allocate

$$
p_k=\frac{\eta}{16B}4^{-|k|}\quad(k\in\mathbb Z),
\qquad
U=\bigcup_{k\in\mathbb Z}\left(2^kH_{p_k}\cup-2^kH_{p_k}\right).
$$

If a 1-periodic set has density $d$, then

$$
m((\pm2^kH)\cap[0,1])\le\max(1,2^k)d.
$$

The larger-scale cost cannot be replaced by density alone. Therefore

$$
m(U\cap[0,1])
\le\frac{2C\eta}{16B}
\sum_{k\in\mathbb Z}4^{-|k|}\max(1,2^k)
=\frac{7C\eta}{24B}\le\frac{7\eta}{24}.
$$

The sum is explicit: negative indices contribute $1/3$, zero contributes 1, and positive indices contribute 1.

For any dilation $s\ne0$, write $s=\sigma2^kt$ with $\sigma\in\{-1,1\}$, $1\le t<2$, and set $y=\sigma2^{-k}x$. A hit from (11) gives

$$
x+sa_n=\sigma2^k(y+ta_n)\in U.
$$

Hence the compact set $E=[0,1]\setminus U$ has measure greater than $1-\eta$ and contains no entire nonzero affine copy $\{x+sa_n:n\ge1\}$.

**Worked budget check.** Replacing $4^{-|k|}$ by $r^{-|k|}$ gives total weight $1/(r-1)+1+2/(r-2)$, finite for $r>2$. At $r=2$ the positive-index terms are all 1, so this proof's budget fails.

**Failure modes.** This argument assumes the normalized hitting sets; it does not construct them. A divergent upper-bound series does not prove the union is large. Both dilation signs matter. Multiplication by a dyadic scale changes the affine parameters, not the sequence index. Convergence of $a_n$ to zero is unused in this deduction.

**Next question.** Repeat the normalization with a base $b>1$ and normalized interval $[1,b)$. Derive the budget condition before choosing weights, and compare constants without changing the hitting hypothesis silently.

Source: [periodic reduction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/build/sections/02-periodic.tex). Further details: [reviewed derivation](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/reviews/affine/research-notes.reviewed.txt).

## 9 Test stability claims by separating maps from their output laws

**Trigger.** A proposed continuity estimate compares a map with the probability distribution it generates. A small change in the distribution can conceal substantial reassignment of source points.

**Prerequisites.** Integration on a square, convex piecewise-affine functions, pushforward measures, and the definition of Wasserstein distance.

For a map $T$, its pushforward $T_\#\rho$ is the measure defined by $T_\#\rho(E)=\rho(T^{-1}(E))$. The norm $\|T-S\|_{L^2(\rho)}$ compares values at the same source point. By contrast, $W_2(\mu,\nu)^2$ minimizes quadratic transportation cost over all couplings of the two output laws. The common-source coupling is only one candidate.

Take uniform probability $\rho$ on $[-1,1]^2$, parameters $0<b<a$ and $a+b<1$, and convex functions

$$
u(x)=\max\{-x_1,x_1,a\},
\qquad v(x)=\max\{-x_1,x_1,a+bx_2\}.
$$

Define $T=\nabla u$ and $S=\nabla v$ outside their null tie lines. These are maps, while $\mu=T_\#\rho$ and $\nu=S_\#\rho$ are measures. A finite-affine maximum supplies a direct optimality certificate: if $u(x)=\max_i(x\cdot y_i+c_i)$, then

$$
u(x)-x\cdot y_i-c_i\ge0,
$$

with equality at a winning slope. Integrating this nonnegative slack proves quadratic optimality; null tie sets give uniqueness. No numerical optimization is needed.

**Exact calculation.** Writing $m=(1-a)/2$, the output laws are

$$
\mu=m\delta_{-e_1}+a\delta_0+m\delta_{e_1},
\qquad
\nu=m\delta_{-e_1}+a\delta_{be_2}+m\delta_{e_1}.
$$

Matching corresponding atoms gives $W_2^2\le ab^2$. The second coordinate of every atom of $\mu$ is zero, so every coupling pays at least the second-coordinate cost $ab^2$. Hence equality holds.

The central source cells are $A=\{|x_1|<a\}$ and $B=\{|x_1|<a+bx_2\}$. Slicing at $x_2=t$, their symmetric difference has probability $b|t|$; averaging gives $\rho(A\mathbin\triangle B)=b/2$. Thus

$$
W_2(\mu,\nu)^2=ab^2,
\qquad
\|T-S\|_{L^2(\rho)}^2=\frac b2+ab^2.
\tag{12}
$$

**Worked obstruction.** Set $b=a/2$, $a\downarrow0$. Then $W_2=\tfrac12a^{3/2}$, whereas $\|T-S\|_2=\tfrac12\sqrt{a+a^3}$. A uniform estimate $\|T-S\|_2\le C W_2^\alpha$ would have ratio proportional to $a^{1/2-3\alpha/2}$. This diverges whenever $\alpha>1/3$.

**Failure modes.** An obstruction to larger exponents does not prove the endpoint upper bound. Here a target mass tends to zero, so the example does not refute estimates assuming uniformly positive atom masses. The construction requires a transverse coordinate; on the line, the common quantile coupling behaves differently. The distances between distinct atoms within each target law stay at least one, so atom collision is not the mechanism.

**Next question.** Keep the central mass bounded below and vary only the tilt. Determine which powers the same computation rules out, and which part of the original obstruction disappears. This is a controlled test of a new hypothesis, not a proof of a global stability theorem.

Source: [sharpness section](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/build/source/sections/sharpness.tex). Further details: [proof](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/transport-stability/proof.md), [independent audit](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/reviews/transport/audit-report.md).

## A modest study plan

The ordering below reflects accessibility, broad reuse, and verified foundations. It is not a ranking of the original manuscripts or of research novelty. A session means roughly one focused study period; completing a proof is more important than fitting a clock.

1. **Radial geometry, two sessions.** Reconstruct existence, uniqueness, and (8) without looking at the proof. Derive (9), then test a flat-faced norm and a boundary center. Deliverable: a one-page theorem with every parameter and constant stated. Compare its exact statement with the completed radial formalization.
2. **Finite-state termination, two sessions.** Prove fixed-length finiteness and the two rewrite identities. Explain why termination survives arbitrary choices of duplicate pairs. Deliverable: a small exact trace plus a universal proof; record the distinction. Compare with the completed Egyptian formalization.
3. **PSD Gram deficits, two sessions.** Prove (6) and (7), including zero blocks and rectangular dimensions. Deliverable: one equality example, one strict example, and one counterexample after dropping full positivity. The ordinary proof is reviewed; Lean completion remains pending at this snapshot.
4. **Tangent bridge and packing, three sessions.** First recover the nonsharp pointwise threshold. Then isolate the pair-spacing input and prove the harmonic-packing improvement. Deliverable: a dependency diagram with H visibly at its root and divergence visibly independent of H. Compare with the completed conditional tangent statements, not merely the declaration count.
5. **Finite Fourier mixing, two or three sessions.** Derive inversion from the indicator identity and prove (5) with the exact normalization. Deliverable: a four-product proof and two failed-hypothesis examples. The ordinary argument is reviewed; the formal project is still running at the snapshot.
6. **Mixed moments, three or four sessions after the measure-theory prerequisites.** Maintain two parallel pages: an analytic exchange ledger and a rational-coordinate calculation. Deliverable: a proof of (10), the example $P=1,D=t$, and a precise explanation of why evaluation need not be injective. The formal project is still running at the snapshot.
7. **Choose one extension.** Study the affine scale budget if interested in measure and combinatorics, or the transport example if interested in analysis and geometry. Each has a concrete ordinary proof and a bounded next question above.

An optional geometry continuation is the [analytic convex approximation study](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/convex-approximation/study.md), based on the [pinned approximation lemma](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/build/main.tex#L457-L511). It replaces support half-spaces by a finite sum of exponentials, uses a positive-spanning direction net for coercivity and a positive-definite Hessian, and uses a strict interior margin for regular analytic boundary contact. This connects Methods 5 and 6. The next prerequisites are multivariable differentiation, support functions, and the analytic implicit function theorem. Do not treat pointwise positive Hessian as a global uniform convexity constant, or silently pass from finite-dimensional compactness to an infinite-dimensional setting.

## A reusable research checklist

For each new supporting lemma, save a short record with these fields:

- **Statement:** exact domains, quantifiers, normalization, and strict inequalities
- **Input:** what is proved here, what is imported, and what remains conditional
- **Interface:** the map or construction, its output type, and the receiving theorem's assumptions
- **Certificate:** an identity, positive gap, majorant, finite state space, or separation estimate
- **Boundary tests:** zero cases, equality cases, dimension changes, lost positivity, failed independence, and parameter limits
- **Evidence:** ordinary proof review, exact finite checks, and formal compilation listed separately
- **Provenance:** source revision, exact passage, formal statement when applicable, and the version of the reviewed artifact
- **Next question:** one bounded extension, the evidence that would settle it, and a stopping condition

A useful first research outcome is often a smaller theorem with a complete proof and a clear interface. It can guide later work even when the source manuscript's much larger conclusion has not been established.
