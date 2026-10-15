# A small atlas of failed exchanges

This is a retrieval map to complete proofs, not a replacement for them. It gives
outcomes; use [PROBLEMS.md](PROBLEMS.md) for the problem-first route.

| Exchange or tempting inference | Example and failure mechanism | Positive sufficient condition |
|---|---|---|
| Integrate every section of a Lebesgue-measurable set | E03: a nonmeasurable set can sit in one exceptional section of a planar null set. | Borel measurability gives Borel sections everywhere; completed Lebesgue measurability gives measurable sections almost everywhere. |
| Swap signed iterated integrals | E04: both signed parts have infinite integral near the origin. E05: the signed matrix has infinite absolute sum. | Joint measurability and finite integral of the absolute value give Fubini; nonnegativity gives Tonelli with extended values. |
| Pass an almost-everywhere limit through an integral | E14: mass concentrates at a shrinking interval; its height grows. | DCT with one integrable majorant; on a finite measure space, convergence in measure plus uniform integrability gives convergence in $L^1$. |
| Treat bounded integral mass as sufficient on an infinite space | E14: a unit bump moves to infinity. Value-tail uniform integrability alone permits this. | Add spatial tightness to value-tail uniform integrability, together with convergence in measure on bounded sets (and an integrable limit). Precise versions are stated in E14. |
| Differentiate a parameter integral at an endpoint | E15: difference-quotient mass concentrates near zero; pointwise derivatives miss that mass. | Measurability, pointwise differentiability almost everywhere, one integrable local bound on the parameter derivative, and one integrable parameter slice. See the exact interval and endpoint conditions in E15. |
| Differentiate a uniform limit of differentiable functions | E15 related example: $\sin(nx)/n$ tends uniformly to zero while its derivative is $1$ at zero for every $n$. | On a compact interval, uniform convergence of the derivatives and convergence of the function values at one point imply a differentiable limit with the expected derivative. The mean value theorem proves this for differentiable functions; for $C^1$ functions one can also use the fundamental theorem of calculus. |
| Replace geometric area by parameter area | E08/E11: repeated or folded parametrizations count the image more than once. | Injectivity outside sets whose contributions are zero, or explicit multiplicity in the area formula. |
| Divide by a coarea Jacobian everywhere | E12: the gradient vanishes at the origin. | Restrict division to the positive-Jacobian set, then prove the zero set contributes zero or account for its contribution separately. |
| Use the area formula for a merely continuous monotone map | E13: the Cantor staircase has derivative zero almost everywhere but maps onto an interval. | Lipschitz maps satisfy the area formula; in one dimension absolute continuity gives the fundamental theorem and the relevant change-of-variable identities. |

Concentration is also a tool: E16 uses an approximate identity. There the
integration variable is rescaled and a fixed integrable majorant becomes
available. The conclusion is a boundary evaluation, with all its hypotheses
stated, rather than an exchange based solely on pointwise convergence in the
original variable.
