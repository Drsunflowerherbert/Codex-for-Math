# Independent review: E05, E06, E14, E15, E16

Reviewer: `author_area_coarea`, independent of `author_parameters`, the author of these five examples. Review date: 2026-10-15. This is a mathematical text review with supporting computational checks; it is not formal proof verification.

## Scope and method

Read all five completed source files, reconstructed the computations and the theorem-hypothesis arguments, and inspected Hunter's *Measure Theory* (Theorems 4.24, 5.18; Example 5.19; Chapter 4 convergence examples) and Conrad's *Differentiating under the integral sign*. The stated differentiation results are proved by difference quotients in the examples rather than attributed to a stronger measurable theorem in the classical source.

| ID | Outcome | Independent mathematical checks |
|---|---|---|
| E05 | Pass | Every row has entries $1,-1$, the first column sums to $1$, and each later column sums to zero. The positive and negative double integrals are both infinite. Recounting a finite rectangle gives $\min(N,M)-\min(N,M-1)$, so square and next-column exhaustions differ. No undefined signed product integral is used. |
| E06 | Pass | The sign and logarithm agree: for $a\leq b$, the integrand is $\int_a^b e^{-tx}\,dt$. Tonelli uses a nonnegative Borel kernel on sigma-finite spaces before finiteness; the resulting integral is $\log(b/a)$. The $b$ derivative is positive. For $b$ near a fixed $b_0>0$, the mean value theorem provides the common majorant $e^{-b_0x/2}$ for the actual difference quotients. The $a>b$ and $a=b$ cases are covered. |
| E14 | Pass | Concentration, translation, and dilution all have integral one and the stated almost-everywhere limits. The exact large-value-tail definition is distinguished from spatial tightness on an infinite measure space. The finite-space truncation argument is valid, including Fatou for the limiting tail. On the line, local convergence in measure permits an almost-everywhere convergent diagonal subsequence, so Fatou transfers the spatial-tail bound to the limit; finite-interval $L^1$ convergence plus two tail bounds proves global $L^1$ convergence. |
| E15 | Pass | The integral is $t\arctan(1/t)$ for $t>0$, so its right derivative at zero is $\pi/2$, whereas each section's right derivative is zero. Quotient mass on $(0,t)$ is exactly $\pi/4$. For the parameter derivative the change $x=tu$ gives the same strictly positive mass on $(t,2t)$ for a countable sequence of parameters, ruling out an $L^1$ bound even when initial null exceptional sets depend on the parameter. The positive rule imposes a common full-measure set and controls the difference quotients; its endpoint version has the needed one-sided continuity through right differentiability. |
| E16 | Pass | The rescaling gives a fixed integrable kernel $e^{-u}$ and correct limit $g(0)$. The direct split gives $\varepsilon+2Me^{-n\delta}$. The first moment of the exponential probability kernel is $1/n$, giving the global Lipschitz error $L/n$, and the stated local variant adds the correct exponential tail. Original-variable concentration is demonstrated without inferring domination from pointwise density convergence. |

## Supporting exact calculations

A separate Python/SymPy 1.14.0 invocation reconstructed these expressions:

- $\int_0^\infty e^{-tx}\,dx=1/t$ for $t>0$.
- $\int_0^1 t^2/(x^2+t^2)\,dx=t\arctan(1/t)$ and $\lim_{t\downarrow0}\arctan(1/t)=\pi/2$.
- A primitive of $2u^2/(1+u^2)^2$ is $\arctan u-u/(1+u^2)$, confirming the derivative-band mass is $\arctan2-\pi/4+1/10>0$.
- $\int_0^\infty te^{-tx}\,dx=1$ and $\int_0^\infty te^{-tx}x\,dx=1/t$ for $t>0$.
- Exhaustive integer checks for $1\leq N,M\leq8$ agreed with the E05 finite-rectangle formula. The displayed counting argument supplies the general proof.

These calculations check algebra and elementary identities only. They do not establish measurability, sigma-finiteness, almost-everywhere statements, domination, uniform integrability, or validity of an exchange; those were checked in the prose arguments above.

## Corrections and remaining limits

No mathematical error requiring correction was found. The author signed off on and applied the three suggested E14 clarity/source improvements: explicitly naming real measurable functions in the sufficient conditions, making the diagonal subsequence in the infinite-space tail argument visible, and identifying Hunter Examples 4.18–4.20 as the source of the standard three families. The reviewer re-read that revised argument and confirmed the summable error-set construction and Fatou tail estimate. These are clarification/source-precision improvements, not repairs to incorrect assertions. All five final inputs below pass this independent review.

No Lean or other proof-assistant verification was performed. The UI criterion is stated for sequences and Lebesgue measure on $\mathbb R$ in its infinite-space version; the text does not claim a general topological-space tightness theorem.

## Exact reviewed inputs

SHA256 hashes, computed after the E14 author revisions were re-read:

| File | SHA256 |
|---|---|
| `examples/E05-signed-fubini-counting.md` | `6ec3c9aca8ae42e84506f3b809e2af3735d4dc513b6d8a28fd8469ce27471973` |
| `examples/E06-frullani-parameter-integral.md` | `eab2e9eb88fba447a7876cc9e7980ce2e00cdcb436e578f945dbfdfdf1ff05c7` |
| `examples/E14-concentration-escape-atlas.md` | `5241b8901c9b047292714af5f8c8c8bb95728409336d6be63d50168a90c9f024` |
| `examples/E15-differentiation-concentration.md` | `f41194163d0b97b3fb2c8a57def496c205cec72d534509fe08ebda51fed12718` |
| `examples/E16-exponential-approximate-identity.md` | `ec42b351eb40b2486ac89578ac40b2e231a2147aa65b511d1ea154c41afb4d37` |
