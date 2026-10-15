# Problem index — without computed answers

Each entry links to a separate full solution. Read [CONVENTIONS.md](CONVENTIONS.md)
first for measure normalization and the exact role of almost-everywhere sections.
The JSON index and retrieval command described in [README.md](README.md) support
search by topic, prerequisite, and technique without printing answers by default.

| ID | Task | Main prerequisites | Technique to look for |
|---|---|---|---|
| [E01](examples/E01-triangular-region.md) | Integrate $e^{y^2}$ over $0<x<y<1$. | Measurability, Tonelli | Change order on a measurable region |
| [E02](examples/E02-positive-measure-boundary.md) | Construct a region whose boundary has positive area; integrate $2y$ over it. | Countable additivity, Tonelli | Explicit removed-interval sums |
| [E03](examples/E03-exceptional-sections.md) | Can every section of a Lebesgue-measurable null set be integrated? Prove the correct general statement. | Completion, Fubini | Borel representative and null envelope |
| [E04](examples/E04-signed-fubini-trap.md) | Compare the iterated integrals of $(x^2-y^2)/(x^2+y^2)^2$ on $(0,1)^2$. | Signed integrals, Fubini | Check positive and negative parts first |
| [E05](examples/E05-signed-fubini-counting.md) | Sum an explicit signed matrix by rows and by columns. | Counting measure, series | Detect infinite absolute mass |
| [E06](examples/E06-frullani-parameter-integral.md) | Evaluate and differentiate a Frullani parameter integral. | Tonelli, dominated convergence | Replace a quotient by a parameter integral |
| [E07](examples/E07-parabola.md) | Integrate the first coordinate along a parabola with respect to length. | Derivatives, area formula | Compute the speed and pull back the weight |
| [E08](examples/E08-circle-multiplicity.md) | Integrate a coordinate square on a twice-traversed circle. | Curve area formula | Count multiplicity; distinguish circulation |
| [E09](examples/E09-paraboloid-graph.md) | Integrate height on a paraboloid graph over the unit disk. | Gram determinant, polar coordinates | Derive the graph area factor |
| [E10](examples/E10-sphere-moment.md) | Integrate a coordinate square over a sphere of radius $R$. | Surface area formula | Handle chart seams and pole exceptions |
| [E11](examples/E11-fold-area-multiplicity.md) | Apply weighted area to a folded square parametrization. | Jacobian, area formula | Compare source integral and image multiplicity |
| [E12](examples/E12-radial-coarea-critical-value.md) | Turn an integral on a disk into integrals over circular level sets. | Gradient, coarea | Account for a critical point before division |
| [E13](examples/E13-cantor-singular-map.md) | Explain why the Cantor staircase violates a proposed derivative-area identity. | Cantor set, absolute continuity | Locate the failed Lipschitz hypothesis |
| [E14](examples/E14-concentration-escape-atlas.md) | Track mass in concentration and escape examples when taking limits under integrals. | Pointwise convergence, DCT | Uniform integrability and spatial tightness |
| [E15](examples/E15-differentiation-concentration.md) | Compare a parameter derivative with the integral of pointwise derivatives. | Difference quotients, DCT | Test local domination; distinguish derivative limits |
| [E16](examples/E16-exponential-approximate-identity.md) | Recover a boundary value from exponential averages. | Substitution, DCT | Approximate identity and an explicit tail estimate |

Suggested routes: E01–E06 for Lebesgue integration and iterated integrals;
E07–E13 for geometric integration; E14–E16 for exchanges of limits, derivatives,
and integrals. E03 and E04 are useful safeguards before generalizing a successful
calculation. The [counterexample atlas](COUNTEREXAMPLES.md) maps the safeguards
to precise sufficient conditions and contains some outcome spoilers.
