# Independent mathematical review — E01–E04

Reviewer: geometry author, separate from the author of E01–E04. Review date: 2026-10-15. Scope: the four example Markdown files, their stated hypotheses, computations, pitfalls, and cited source locations. This is a human-readable mathematical audit assisted by exact symbolic checks; it is not formal proof verification.

## Disposition

All four examples pass after one minor domain clarification in E04. No open mathematical blocker remains in these four examples. The E04 author explicitly approved the correction on 2026-10-15. The primary-source references were checked against Hunter's online PDF on the review date.

## E01 — Measurable triangular region

- The two section descriptions are equivalent: for fixed $y$ the section is $(0,y)$, and for fixed $x$ it is $(x,1)$.
- Openness establishes Borel measurability, and the bound by $e\mathbf1_{(0,1)^2}$ establishes absolute integrability before Fubini is used. Both coordinate measure spaces are sigma-finite. Nonnegativity independently permits Tonelli.
- The useful section length is $y$, giving $\int_0^1y e^{y^2}\,dy=(e-1)/2$. The displayed series reindexing is correct: $2(k+1)k!=2(k+1)!$.
- Both uniform convergence on the compact interval and monotone convergence of nonnegative partial sums justify the optional sum calculation. The distinction between function and value is explicit.

Status: **pass**.

## E02 — Positive-measure boundary

- The recurrence is correct: $\ell_0=1$ and $(\ell_{n-1}-4^{-n})/2=2^{-n-1}+2^{-2n-1}>0$. Thus every stated removal fits strictly inside its parent. The recurrence produces exactly $2^n$ separated components at stage $n$.
- The removed lengths sum to $\frac12(1-2^{-n})$ through stage $n$. Continuity from above is legitimate because the initial measure is finite, giving $\mathcal L^1(C)=1/2$.
- Any nondegenerate interval in $C$ would lie in a single component of every $C_n$, contradicting $\ell_n\to0$. Thus $C$ is closed with empty interior, and its complement is dense.
- The product $E$ is closed with empty interior, hence equals its boundary in the ambient plane. The product formula gives boundary area $1/2$. This is a genuine positive-boundary-measure example; it does not use a hidden null-boundary assumption.
- The bounded Borel zero extension has integral $1/2$. All lower Darboux sums vanish because every positive-width interval meets the complement of $C$; upper sums dominate the Lebesgue integral. This directly proves failure of Riemann integrability.

Status: **pass**.

## E03 — Exceptional nonmeasurable section

- The Vitali representative argument is valid under the stated axiom of choice: distinct rational translates are disjoint, their countable union covers $[0,1]$, and that union lies in $[-1,2]$. Translation invariance gives the contradiction under either possible measurable value of $\mathcal L^1(V)$.
- The set $\{0\}\times V$ lies in a Borel planar null set. Completeness therefore proves joint Lebesgue measurability and nullity while leaving its section at $x=0$ nonmeasurable.
- The horizontal section sets are measurable even though their identities depend on membership in $V$; their section measures are identically zero. This distinction is correct.
- The general Borel representative $B$ and Borel null envelope $N$ exist for arbitrary Lebesgue-measurable $A$, including unbounded sets. Each Borel section is Borel, and Fubini applies to $\mathbf1_N\in L^1$. The resulting nonnegative section measure is zero almost everywhere. Completeness of the section measure transfers measurability from $B_x$ to $A_x$ only outside the resulting null parameter set.
- The example correctly distinguishes the uncompleted product sigma-algebra from its completion and never assigns an integral to the nonmeasurable exceptional section.

Status: **pass**.

## E04 — Finite iterated values without a joint signed integral

- Both primitive derivatives equal the stated integrand. Fixed positive coordinate sections extend continuously to the other coordinate's closed unit interval, so each section is absolutely integrable.
- The iterated values are respectively $\pi/4$ and $-\pi/4$.
- On $0<y<x/2$ the lower bound $f\geq12/(25x^2)>0$ is correct. Each $R_n$ lies in that cone and in $Q$, the rectangles are disjoint, their area is $2^{-2n-3}$, and their lower mass is $3/50$. The finite partial sum $3N/50$ proves divergence without exchanging a signed integral.
- Antisymmetry and coordinate transposition give the same divergence for the negative part. Therefore both sign parts are infinite, and the signed Lebesgue integral is undefined. Tonelli applies only separately to the nonnegative parts.
- The symmetric truncation calculation is correct. **Applied clarification:** changed $[\varepsilon,1]^2$ to $(\varepsilon,1)^2\subset Q$ in Step 4, so every use of $f$ remains inside its defined domain. This preserves boundedness, symmetry, and the zero integral, and the truncations exhaust $Q$ as $\varepsilon\downarrow0$.

Status: **pass after the stated minor clarification**.

## Source and computational evidence

Primary source: John K. Hunter, [*Measure Theory*](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf). Checked locations: Proposition 1.12 (continuity of measure), Theorems 2.27–2.28 (Borel approximation and completion), Theorem 4.6 (monotone convergence), Definition 4.8 (signed integral), Theorem 5.14 (product measure), Theorem 5.18 (Fubini; printed p. 61), and Example 5.20/Theorem 5.21 (completion and exceptional sections; printed p. 62). These support the background statements cited in the examples; the examples include their own direct computations and constructions.

Independent exact checks were run with SymPy: the E01 substitution result, E02 interval recurrence and removed-length sum, both E04 primitive derivatives, E04 antisymmetry, and the $3/50$ rectangle lower mass all simplified exactly to the claimed identities. These checks verify algebra, not measurability, completeness, theorem hypotheses, or infinite-divergence arguments; those were reviewed above.

## Reviewed input hashes

These SHA-256 hashes identify the exact Markdown inputs reviewed after the approved E04 correction. A later content change requires checking the affected review conclusions again.

| File | SHA-256 |
| --- | --- |
| `examples/E01-triangular-region.md` | `8eed24ce89582d0de378801ce5fdbecdc46941edd3a35911d730ca2e51554beb` |
| `examples/E02-positive-measure-boundary.md` | `436c35e79a6dcae2cb1d5a5e3cf266f18c410addeb6ad16690e7cd31b34b2eae` |
| `examples/E03-exceptional-sections.md` | `dfd1ccec2c3cbd4047d70629d401140b1bf6d5830a3b6408181e89002e561ed0` |
| `examples/E04-signed-fubini-trap.md` | `13492b6f8dcaf22028d8a31f96221e553b22d277ed3633850f0f54a40e6291f2` |
