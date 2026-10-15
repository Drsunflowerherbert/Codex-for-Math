# Independent mathematical review: E11–E13

Review date: 2026-10-15. Reviewer: the Lebesgue-example author agent, who did not author E11–E13. The area/coarea author confirmed completion before this reviewer edited the drafts. This is an independent mathematical audit by another agent, not proof-assistant verification or an external human referee report.

## Scope and method

The reviewer read every step of each example, independently recomputed the identities, checked the stated domains and measures, and opened the cited primary author-hosted PDFs. The source checks used Simon's 2018 NTU draft, not the differently numbered older course draft:

- [Simon, *Introduction to Geometric Measure Theory*](https://math.stanford.edu/~lms/ntu-gmt-text.pdf): Chapter 1, Definitions 2.1–2.2 and Theorem 2.6; Chapter 2, Theorem 3.3 and Remark 3.4(2); Theorem 7.3 and Remark 7.4(1).
- [Hunter, *Measure Theory*](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf): Examples 2.14 and 2.37, and the opening of Chapter 6.

These source statements support normalized Hausdorff measure, the area formula with all preimages counted, locally Lipschitz coarea, Cantor-set nullity, and the absolute-continuity distinction. The derivations below were also checked directly; a source citation was not treated as a substitute for checking applicability.

## E11 — pass

File: [E11-fold-area-multiplicity.md](../examples/E11-fold-area-multiplicity.md).

- The map extends smoothly to an open neighborhood, is Lipschitz on the compact source rectangle, and all weights used are nonnegative Borel functions. No unsupported signed subtraction is used.
- Independent differentiation gives $DF=\operatorname{diag}(2u,1)$ and $J_2F=2|u|$. The signed determinant $2u$ cannot replace the area Jacobian.
- Every fiber was checked: two preimages for $x>0$ in the image, one on its left edge, zero outside. The exceptional edge is planar null, so multiplicity is two almost everywhere on the image.
- The image area is $1$, the parameter area integral is $2$, the weighted parameter integral is $2$, and the image integral of $x+y$ counted once is $1$. An independent SymPy calculation of the positive sheet gave $\int_0^1\int_0^1 2u(u^2+v)\,dv\,du=1$; doubling gives $2$.
- The injective positive sheet remains eligible for the Lipschitz area formula despite its zero Jacobian on one edge. The example does not assume the inverse square-root branch is Lipschitz.
- Normalization and orientation are handled correctly: $\mathcal H^2=\mathcal L^2$ on the target plane; scalar area counts both sheets positively, while determinant signs record a different oriented quantity.

Findings requiring correction: none. The author aligned the final Simon citation to the 2018 theorem numbering before this review concluded.

## E12 — pass

File: [E12-radial-coarea-critical-value.md](../examples/E12-radial-coarea-critical-value.md).

- The source disk is Borel and $g(x,y)=x^2+y^2$ is locally Lipschitz. Simon's locally Lipschitz coarea theorem applies. The supplied global truncation $G(z)=\min(|z|^2,4)$ is also a valid alternative: it is $4$-Lipschitz and equals $g$ near the disk.
- Independent differentiation gives $J_1g=|\nabla g|=2|z|$. The critical point is exactly $0$, and its critical value is exactly $0$.
- For $0<t\leq1$, the level circle has normalized length $2\pi\sqrt t$. The level at zero is a singleton and has $\mathcal H^1$-measure zero. The half-open angle interval used to compute length is injective; it does not count a repeated endpoint.
- The compensating weight is Borel, is defined as zero at the critical point and outside the disk, and divides by the Jacobian only where it is positive. It recovers $\phi\circ g$ almost everywhere, including the allowed case $\phi(0)=+\infty$.
- The level integral is $\pi\phi(t)$ for $0<t\leq1$. The arbitrary endpoint values do not change the outer Lebesgue integral. This proves the extended nonnegative identity without requiring boundedness of $\phi$.
- Independent polar arithmetic verifies $\int_D2|z|\,dz=4\pi/3$ and $\int_D|z|^{2a}\,dz=\pi/(a+1)$ for $a>-1$. The exponent threshold $a=-1$ is correct; the integral diverges for $a\leq-1$. Symbolic checks also covered $a=-1/2,0,1,3/2$.
- The signed extension first establishes absolute integrability from the nonnegative formula, as required. The pushforward probability statement follows after dividing the planar measure by $\pi$.

Findings requiring correction: none. No use of Sard's theorem is needed for this explicitly computed critical value.

## E13 — pass after two small expository clarifications

File: [E13-cantor-singular-map.md](../examples/E13-cantor-singular-map.md).

- The nested Cantor sets have measures $(2/3)^n$, so continuity from above proves nullity. Each approximant is piecewise linear, nondecreasing, continuous, and absolutely continuous.
- The endpoint increments $2^{-n}$ on all basic stage-$n$ intervals justify the uniform Cauchy bound for later approximants. The uniform limit is continuous, monotone, and onto $[0,1]$ by its endpoint values.
- Every point outside the Cantor set lies in an open deleted gap, where the limiting function is locally constant. This proves the derivative is zero almost everywhere without asserting differentiability on the Cantor set.
- The multiplicity proof is correct: repeated preimages force a constant interval, which contains part of a gap. Thus multiplicity is one off the countable plateau-value set, infinite on that set, and zero outside $[0,1]$. Its target integral is $1$, while the integral of the almost-everywhere derivative is $0$.
- The unbounded quotients $(3/2)^n$ rule out a Lipschitz constant. The disjoint-interval sum with total length $(2/3)^n$ and total variation $1$ directly disproves absolute continuity. The proof that the Cantor set maps onto the whole interval correctly includes plateau values via gap endpoints.
- The derivative representatives $q_n=(3/2)^n\mathbf1_{K_n}$ have integral $1$ and converge to zero almost everywhere. The domination contradiction and failure of uniform integrability follow from the same shrinking-set calculation; no escape to infinity occurs.
- The stated positive replacement for absolutely continuous $F_n$ follows from their integral representation and dominated convergence of derivatives. Its uniform bound uses the $L^1$ difference, so the asserted absolutely continuous limit is justified.
- Independent exact rational checks of stages $0$ through $7$ verified interval counts and lengths, endpoint increments, the leftmost difference quotients, and the stated uniform bound for later stages $n+1$ and $n+2$. These finite checks corroborate arithmetic only; the limit and regularity claims are established by the written arguments.

Reviewer edits: added the one-sentence implication “nullity implies empty interior,” which is used in the fiber proof; replaced “shrinking neighborhoods $K_n$” with “shrinking sets $K_n$,” since the closed basic sets need not be topological neighborhoods of their endpoints. These edits do not change any result or proof strategy.

Author signoff: the area/coarea author explicitly accepted both clarifications on 2026-10-15 and confirmed that no further author changes were planned before these hashes were finalized. There were no substantive mathematical revisions requiring additional signoff.

## Limits of this review

No Lean or other proof assistant was run. The symbolic and finite-stage checks do not verify measurability, theorem hypotheses, infinite limiting arguments, or source correctness. Those were inspected in the independent mathematical review above. No unresolved mathematical issue was found in E11–E13 as reviewed.

## Exact reviewed inputs

These SHA256 hashes identify the final Markdown inputs inspected after the reviewer edits. A later change requires checking whether this review still applies.

| Example file | SHA256 |
|---|---|
| `examples/E11-fold-area-multiplicity.md` | `c0c22aece66be1e8361fc5dc5d5265a4e03ae85c4e82cc85953c3a844c90ea0d` |
| `examples/E12-radial-coarea-critical-value.md` | `618495ccec0c97691557e2aafd0b25e561d84e59e8df59abf7682de62063319d` |
| `examples/E13-cantor-singular-map.md` | `fc9c5677672449baa0ca88e3f90935238486bda657f13c23fc5b3e2a325da783` |
