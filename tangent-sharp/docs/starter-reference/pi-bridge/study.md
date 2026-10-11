# Rational approximation bounds and tangent at integer arguments

## Result and scope

For positive integers \(n\), an eventual all-numerator estimate

\[
  \left|\pi-\frac pq\right|\ge c q^{-\alpha}
  \quad(p\in\mathbb Z,\ q\in\mathbb Z,\ q\ge Q),
  \qquad c>0,\quad \alpha\ge2,
\]

implies

\[
 |\tan n|=O(n^{\alpha-1}),\qquad
 \frac{\tan n}{n^s}\longrightarrow0\quad(s>\alpha-1),\qquad
 \sum_{n=1}^{\infty}\frac{|\tan n|}{n^s}<\infty\quad(s>\alpha).
\]

The last inequality is a **sufficient threshold obtained by pointwise comparison**. This study does not claim it is necessary or sharp. It does not study improved aggregate estimates for the series.

The published PiExponent statement supplies the hypothesis with \(c=1\) for each separately chosen \(\alpha>2\). Consequently, this bridge gives \(|\tan n|=O_\varepsilon(n^{1+\varepsilon})\) for every \(\varepsilon>0\), a zero scaled limit for every \(s>1\), and absolute convergence for every \(s>2\). In particular,

\[
 \boxed{\lim_{n\to\infty}\frac{\tan n}{n^3}=0},\qquad
 \boxed{\sum_{n=1}^{\infty}\frac{|\tan n|}{n^3}<\infty}.
\]

These conclusions are ordinary mathematical deductions from the displayed approximation premise. They do not constitute a new proof of the premise or a new Lean verification.

## Evidence and verification status

Source inspection date: **11 October 2026 UTC**. The initial inspection used the mutable `main` branch. The central solution statement was subsequently checked at [commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/PiExponent/Main.lean); its exact source file has Git blob hash `486ed39ba52e5a10de7893cf0f302edb873801f2`. The source ledger also records content hashes for the scope note, definitions, comparator target, and comparator configuration. This is source provenance, not Lean verification.

The [family 017 scope note](https://github.com/openai/math/blob/main/lean/docs/017.md) describes an eventual lower bound for all integer numerators at every exponent strictly above two, together with an exact supremum characterization. The [official Main.lean](https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/PiExponent/Main.lean) contains the named declarations `pi_eventual_lower_bound`, `pi_integer_eventual_lower_bound`, `pi_irrationalityExponent_eq_two`, and `main`. Its first conjunct is precisely the all-integer eventual estimate used here, with \(c=1\), \(\alpha>2\), and an integer \(Q\ge2\).

The [statement definitions](https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/PiExponent/Statement.lean) distinguish natural and integer denominators. Its irrationality-exponent definition uses infinitely many **distinct reduced rationals**, excludes denominator one, and requires strictly positive approximation error. We use the explicit eventual-bound conjunct, avoiding any ambiguity about interpreting a bare supremum in a formal system.

The [comparator challenge](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PiExponent.lean) is a target statement ending in a placeholder. It is not the supplied proof. Its [configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PiExponent.json) selects `OAI.PiExponent.main` from the official solution module and permits `propext`, `Quot.sound`, and `Classical.choice`. Reading that configuration does not establish that a comparator run succeeded.

The source Main.lean additionally declares `flint_hills_summable`. The scope note says that consequence is outside the selected comparator statement. Both observations can hold simultaneously: source presence and selected comparator coverage are different facts. No Flint–Hills proof is used below.

**Verification performed here:** read the official sources through web tools; developed and checked the ordinary proofs below; validated the accompanying JSON's structure and dependency references. **Verification not performed here:** no Lean compilation, kernel checking, comparator run, axiom audit, dependency audit, downloaded-code execution, or software installation. A previously reported local verification is not adopted as a verification performed by this study.

## Conventions and reusable hypothesis

All angles are in **radians**. Powers of positive real numbers have their usual real-exponent meaning. Limits are along positive integers. A series starts at \(n=1\), so no convention about \(0^s\) or a zero denominator is needed.

Write \(D(c,\alpha,Q)\) for the following hypothesis:

* \(c\in\mathbb R\), \(c>0\);
* \(\alpha\in\mathbb R\), \(\alpha\ge2\);
* \(Q\in\mathbb Z\), \(Q\ge1\);
* for every \(p\in\mathbb Z\) and every integer \(q\ge Q\),
  \( |\pi-p/q|\ge c q^{-\alpha}\).

No coprimality condition is imposed. In particular, the hypothesis applies to \(p=2n\), even when \(2n\) and the denominator share a factor. If a given threshold is not positive, increase it to \(\max(Q,1)\).

We use the classical irrationality of \(\pi\) to ensure that every trigonometric term is defined and that the finite-denominator patch below has a positive constant. Alternatively, \(D(c,\alpha,Q)\) itself rules out rationality: if \(\pi=a/b\) with positive integer \(b\), apply it to \(p=ka,q=kb\ge Q\), obtaining \(0\ge c(kb)^{-\alpha}>0\).

## Lemma 1 A positive nearest odd denominator

**Statement.** For every integer \(n\ge1\), put

\[
 k_n=\left\lfloor\frac n\pi\right\rfloor,
 \qquad q_n=2k_n+1,
 \qquad \delta_n=\left|n-\frac{\pi q_n}{2}\right|,
 \qquad A=1+\frac2\pi.
\]

Then \(q_n\) is a positive odd integer and is the nearest odd integer to \(2n/\pi\). Moreover,

\[
 \left|q_n-\frac{2n}{\pi}\right|<1,
 \qquad 0<\delta_n<\frac\pi2,
 \qquad \frac{2n}{\pi}-1\le q_n\le\frac{2n}{\pi}+1\le An,
\]

and

\[
 \delta_n=\frac{q_n}{2}\left|\pi-\frac{2n}{q_n}\right|.
\]

If \(n\ge N_Q:=\lceil\pi(Q+1)/2\rceil\), then \(q_n\ge Q\).

**Proof.** Since \(n/\pi>0\), \(k_n\ge0\), and hence \(q_n\ge1\). Irrationality of \(\pi\) implies \(n/\pi\notin\mathbb Z\), so

\[
 2k_n<\frac{2n}{\pi}<2k_n+2.
\]

The midpoint of this interval is the odd integer \(2k_n+1\). It is within distance strictly less than one; every other odd integer is at distance strictly greater than one. Multiplication by \(\pi/2\) gives \(\delta_n<\pi/2\). If \(\delta_n=0\), then \(\pi=2n/q_n\), contradicting irrationality. The two-sided denominator estimate follows from the distance bound. Finally \(1\le n\) gives \(2n/\pi+1\le An\), and \(n\ge\pi(Q+1)/2\) gives \(q_n\ge2n/\pi-1\ge Q\). Factoring the positive quantity \(q_n/2\) proves the exact identity. ∎

The floor formula also works without a uniqueness argument. The weaker inequalities with non-strict distance at most one would suffice for every estimate below.

## Lemma 2 Distance from a tangent pole

**Statement.** For \(0<t\le\pi/2\),

\[
 0\le\cot t\le\frac1t.
\]

For the \(q_n,\delta_n\) of Lemma 1,

\[
 |\tan n|=\cot\delta_n\le\frac1{\delta_n}.
\]

**Proof.** On \(0\le t\le\pi/2\), define \(f(t)=\sin t-t\cos t\). Then \(f(0)=0\) and \(f'(t)=t\sin t\ge0\); hence \(t\cos t\le\sin t\). For \(t>0\), divide by \(t\sin t>0\). Nonnegativity follows from \(\cos t\ge0\).

Write \(n=\pi q_n/2+u\), where \(|u|=\delta_n\). Since \(q_n=2k_n+1\), the angle addition formulas give \(|\sin n|=|\cos u|=\cos\delta_n\) and \(|\cos n|=|\sin u|=\sin\delta_n>0\). Thus \(|\tan n|=\cos\delta_n/\sin\delta_n=\cot\delta_n\), and the first inequality applies. ∎

This is why odd denominators occur: the tangent poles are the odd multiples of \(\pi/2\), rather than all integer multiples of \(\pi/2\).

## Theorem 3 Explicit eventual tangent growth

**Statement.** Assume \(D(c,\alpha,Q)\). Define

\[
 N=\left\lceil\frac{\pi(Q+1)}2\right\rceil,
 \qquad C(c,\alpha)=\frac2c\left(1+\frac2\pi\right)^{\alpha-1}.
\]

Then, for every integer \(n\ge N\),

\[
  |\tan n|\le C(c,\alpha)n^{\alpha-1}.
\]

In particular, \(|\tan n|=O(n^{\alpha-1})\) as \(n\to\infty\).

**Proof.** Lemma 1 gives \(q_n\ge Q\), so \(D(c,\alpha,Q)\), with \(p=2n\), implies

\[
 \delta_n=\frac{q_n}{2}\left|\pi-\frac{2n}{q_n}\right|
 \ge\frac c2 q_n^{1-\alpha}>0.
\]

Lemma 2 and reciprocal monotonicity yield

\[
 |\tan n|\le\delta_n^{-1}
 \le\frac2c q_n^{\alpha-1}
 \le\frac2c(An)^{\alpha-1}
 =C(c,\alpha)n^{\alpha-1}.
\]

The penultimate inequality uses \(\alpha-1\ge0\), so \(t\mapsto t^{\alpha-1}\) is nondecreasing on positive reals. ∎

The assumption \(\alpha\ge2\) is convenient for the requested application. This particular growth proof only needs \(\alpha\ge1\), once the same Diophantine hypothesis is given. We retain the requested range in the theorem records.

## Lemma 4 Small denominators and a global constant

**Statement.** Under \(D(c,\alpha,Q)\), there exists a positive \(c_*\) for which

\[
 |\pi-p/q|\ge c_*q^{-\alpha}
 \quad\text{for every }p\in\mathbb Z,\ q\in\mathbb Z,\ q\ge1.
\]

An explicit finite formula is

\[
 c_* =\min\left(\{c\}\cup
 \{q^{\alpha-1}\,\|q\pi\|_{\mathbb Z}:1\le q<Q\}\right),
 \quad
 \|x\|_{\mathbb Z}=\min_{m\in\mathbb Z}|x-m|.
\]

Consequently, the global estimate

\[
 |\tan n|\le \frac2{c_*}A^{\alpha-1}n^{\alpha-1}
 \quad(n\ge1)
\]

holds.

**Proof.** For each integer \(1\le q<Q\), irrationality of \(\pi\) makes \(q\pi\) a noninteger. Writing \(q\pi=m+u\), \(m\in\mathbb Z\), \(0<u<1\), its distance to \(\mathbb Z\) is \(\min(u,1-u)>0\). Thus all entries in the finite set defining \(c_*\) are positive, including \(c\), so the minimum exists and is positive. For any integer \(p\) and \(1\le q<Q\),

\[
 |\pi-p/q|=q^{-1}|q\pi-p|
 \ge q^{-1}\|q\pi\|_{\mathbb Z}
 \ge c_*q^{-\alpha}.
\]

For \(q\ge Q\), use \(c_*\le c\) and the original hypothesis. Apply the proof of Theorem 3 to each \(n\ge1\): the denominator is always positive, so no eventual threshold is needed for this global bound. ∎

The infinitely many possible numerators at each small denominator do **not** require an infinite minimum: their errors have the positive minimum just computed. If \(Q=1\), the second set is empty and \(c_*=c\). Alternatively, for Big-O notation alone, finitely many initial tangent values can be absorbed into the growth constant. For convergence, it is enough that each initial term is finite.

## Corollary 5 Scaled tangent limits

**Statement.** Assume \(D(c,\alpha,Q)\), and let \(s>\alpha-1\). Then

\[
 \lim_{n\to\infty}\frac{|\tan n|}{n^s}=0,
 \qquad
 \lim_{n\to\infty}\frac{\tan n}{n^s}=0.
\]

More precisely, for \(n\ge N\),

\[
 \left|\frac{\tan n}{n^s}\right|
 \le C(c,\alpha)n^{-\beta},\qquad \beta=s-\alpha+1>0.
\]

**Proof.** Divide the estimate in Theorem 3 by the positive number \(n^s\). Since \(\beta>0\), \(n^{-\beta}\to0\); the squeeze theorem proves both conclusions. For a completely explicit tolerance statement, given \(\eta>0\), every integer

\[
 n\ge\max\!\left(N,\left\lfloor(C(c,\alpha)/\eta)^{1/\beta}\right\rfloor+1\right)
\]

satisfies \(|\tan n|/n^s<\eta\). ∎

At \(s=\alpha-1\), this argument only establishes boundedness, not convergence to zero.

## Corollary 6 Absolute convergence by pointwise comparison

**Statement.** Assume \(D(c,\alpha,Q)\), and let \(s>\alpha\). Then

\[
 \sum_{n=1}^{\infty}\frac{|\tan n|}{n^s}<\infty.
\]

Thus the signed series \(sum_{n=1}^{\infty}\tan n/n^s\) is absolutely convergent. For every integer \(M\ge N\), its absolute tail obeys

\[
 \sum_{n=M+1}^{\infty}\frac{|\tan n|}{n^s}
 \le\frac{C(c,\alpha)}{s-\alpha}M^{-(s-\alpha)}.
\]

**Proof.** Let \(r=s-\alpha+1>1\). By Theorem 3, the \(n\)-th summand is at most \(C(c,\alpha)n^{-r}\) for \(n\ge N\). The positive function \(x^{-r}\) is decreasing. Therefore, for each \(n\ge M+1\),

\[
 n^{-r}\le\int_{n-1}^{n}x^{-r}\,dx.
\]

Sum finite intervals and then let the upper endpoint tend to infinity. The integral is finite and equals

\[
 \int_M^{\infty}x^{-r}\,dx=\frac{M^{1-r}}{r-1}
 =\frac{M^{-(s-\alpha)}}{s-\alpha}.
\]

This proves the tail bound and convergence of the tail. There are only finitely many earlier terms, and each is finite because \(\cos n\ne0\). Adding them completes the proof. ∎

At \(s=\alpha\), the majorant becomes \(C/n\). Its divergence does not imply divergence of the smaller tangent series. This proof is simply inconclusive there, and likewise provides no necessity assertion below that endpoint.

## Specialization to the published PiExponent statement

Let **P** denote the first conjunct of the published `OAI.PiExponent.main`:

\[
 \forall\alpha>2\ \exists Q_\alpha\in\mathbb Z,\ Q_\alpha\ge2:
 \quad\forall p,q\in\mathbb Z,\ q\ge Q_\alpha\Longrightarrow
 |\pi-p/q|\ge q^{-\alpha}.
\]

The following are ordinary corollaries **conditional on P**. The reference to the public theorem identifies the proposed source of P, rather than an independently repeated verification of it.

### Growth for every positive epsilon

For any \(\varepsilon>0\), apply Theorem 3 with \(\alpha=2+\varepsilon\) and \(c=1\). There is a threshold \(N_\varepsilon\) such that

\[
 |\tan n|\le2A^{1+\varepsilon}n^{1+\varepsilon}
 \quad(n\ge N_\varepsilon).
\]

The threshold may depend on \(\varepsilon\). The global constant obtained by Lemma 4 may depend on it too. This is the meaning of \(O_\varepsilon(n^{1+\varepsilon})\).

### Scaled limits for every exponent above one

Given \(s>1\), choose \(\alpha=(s+3)/2\). Then \(2<\alpha<s+1\), so Corollary 5 applies. Thus

\[
 \frac{|\tan n|}{n^s}\longrightarrow0,
 \qquad \frac{\tan n}{n^s}\longrightarrow0.
\]

The displayed bound in this choice is \(2A^{(s+1)/2}n^{-(s-1)/2}\) for sufficiently large \(n\).

### A sufficient absolute convergence range

Given \(s>2\), choose \(\alpha=(s+2)/2\). Then \(2<\alpha<s\), so Corollary 6 applies. In this choice, for sufficiently large integer \(M\),

\[
 \sum_{n=M+1}^{\infty}\frac{|\tan n|}{n^s}
 \le\frac{2A^{s/2}}{s/2-1}M^{-(s/2-1)}.
\]

This proves convergence for \(s>2\) but does not identify the exact convergence range.

### Cubic scaling and the cubic absolute series

Choose a single exponent \(\alpha=5/2\), with \(c=1\). Let \(Q_{5/2}\) be supplied by P, put \(N=\lceil\pi(Q_{5/2}+1)/2\rceil\), and set

\[
 C=2A^{3/2}=2\left(1+\frac2\pi\right)^{3/2}.
\]

For all integers \(n\ge N\),

\[
 |\tan n|\le Cn^{3/2},\qquad
 \frac{|\tan n|}{n^3}\le Cn^{-3/2}.
\]

The second inequality tends to zero and is summable. Hence the two boxed conclusions at the beginning hold. For \(M\ge N\),

\[
 \sum_{n=M+1}^{\infty}\frac{|\tan n|}{n^3}
 \le2C M^{-1/2}=4A^{3/2}M^{-1/2}.
\]

The formula for the bound is explicit, but this source inspection does not yield a numerical value of \(Q_{5/2}\) or a numerical certified onset \(N\). It does not provide a numerical value of the infinite series.

## Quantifier and endpoint audit

1. **Do not set \(\alpha=2\) in P.** It quantifies over exponents strictly larger than two. The existence of thresholds separately for all \(\alpha>2\) does not furnish a single positive constant in a \(c/q^2\) bound. This study establishes neither such a bound for \(\pi\) nor its negation.
2. **A stronger extra hypothesis would have stronger consequences.** If \(D(c,2,Q)\) were separately given, our proof would establish \(O(n)\), scaled zero limits for \(s>1\), and absolute convergence for \(s>2\). It would still not settle the limit at \(s=1\) or convergence at \(s=2\) by the displayed pointwise comparison.
3. **At fixed \(\alpha\), the strict thresholds are used.** A zero-limit rate needs \(s-\alpha+1>0\); integrability of the majorant needs \(s-\alpha>0\). These are sufficient conditions for these arguments, not proofs of optimality.
4. **The useful parity class is narrower than all rationals.** The forward proof only invokes positive odd denominators and even numerators \(2n\). In a reduced representation of \(2n/q_n\), its common divisor with \(q_n\) is odd, so the reduced numerator remains even and the reduced denominator remains odd. No coprimality is needed in P. The reverse implication from tangent growth to a lower bound for every numerator and denominator is not claimed.
5. **A reduced-denominator theorem needs an extra step.** One cannot blindly apply a hypothesis requiring a large reduced denominator to an unreduced \(2n/q_n\). The published all-integer formulation avoids that problem. The next paragraph explains a safe general repair when needed.
6. **Finite denominators do not spoil asymptotics.** The threshold in Lemma 1 makes the original hypothesis applicable; alternatively Lemma 4 supplies a global positive constant. Poles cannot occur at positive integer \(n\), by irrationality of \(\pi\).
7. **The denominator is positive.** \(q_n\ge1\), which is essential for reciprocals, real powers, and monotonicity. The hypothesis need not cover zero or negative denominators.
8. **Units and indexing matter.** Integer inputs are radians. A degree interpretation gives a different problem. The series and limits exclude \(n=0\).
9. **No converse or sharp endpoint assertion is imported.** In particular, the pointwise proof does not decide \(\tan n/n\to0\), \(|\tan n|=O(n)\), or convergence/divergence of the \(s=2\) absolute series under P.

### Optional repair when only reduced rational approximations are given

Suppose, for a fixed \(\alpha>0\), that all but finitely many reduced rationals \(r=a/d\), \(d\ge2\), satisfy \(|\pi-r|\ge d^{-\alpha}\). Let \(E\) consist of the finitely many exceptional rationals and those integers \(r\) with \(|\pi-r|<1\). There are only finitely many such integers, because they lie in the bounded interval \((\pi-1,\pi+1)\). Irrationality makes every error for \(r\in E\) positive. Set \(\eta=\min(\{1\}\cup\{|\pi-r|:r\in E\})>0\), and choose a positive integer \(Q\ge\eta^{-1/\alpha}\).

For any integers \(p,q\) with \(q\ge Q\), reduce \(p/q\) to \(a/d\), where \(1\le d\le q\). If \(a/d\in E\), its error is at least \(\eta\ge q^{-\alpha}\). If \(d\ge2\) and it is not in \(E\), its error is at least \(d^{-\alpha}\ge q^{-\alpha}\). If \(d=1\) and it is not in \(E\), its error is at least \(1\ge q^{-\alpha}\). This yields an eventual all-integer estimate without assuming that unreduced denominators become large after reduction.

With the usual irrationality-exponent definition, \(\mu(\pi)=2\) means that for each fixed \(\alpha>2\) there are only finitely many reduced rationals with \(0<|\pi-r|<d^{-\alpha}\); the repair applies separately to each such \(\alpha\). Nothing in this argument supplies a uniform endpoint estimate at \(\alpha=2\).

## Suggested formalization boundary

The accompanying JSON records distinguish source premises from proved ordinary lemmas. Their identifiers and dependencies are suitable for a later adapter to an MRS; no external MRS schema or ingestion endpoint was supplied or tested.

An eventual Lean development could first prove the nearest-odd and pole-distance lemmas, then the fixed-\(\alpha\) growth theorem, limits, and summability. Only at the final specialization would it import `OAI.PiExponent.pi_integer_eventual_lower_bound` or the first projection of `OAI.PiExponent.main`. The parity-restricted formulation is a useful optional intermediate abstraction. Every generated theorem in this study is currently marked **not newly Lean-verified**; names in the JSON are stable study identifiers, not claims that declarations already exist in a Lean library.

## Sources

* Family scope: https://github.com/openai/math/blob/main/lean/docs/017.md
* Official solution entry point at the inspected commit: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/PiExponent/Main.lean
* Definitions: https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/PiExponent/Statement.lean
* Integer/natural denominator equivalence and exponent lemmas: https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/PiExponent/Approximation/Exponent.lean
* Comparator target: https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PiExponent.lean
* Comparator configuration: https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PiExponent.json
* Named manuscript, linked by the scope note; its full proof was not reviewed in this study: https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf

The bridge proofs above are newly written ordinary derivations. Only the stated source facts and imported Diophantine premise are attributed to the repository.
