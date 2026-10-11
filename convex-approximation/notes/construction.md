# Arbitrary-accuracy parameter selection

`Construction.lean` implements the reviewed arbitrary-accuracy step from section 7
using the existing finite-net theorem and quantitative bound. It preserves any
prescribed finite family A of unit directions.

For a requested error ρ > 0, write L = Metric.diam K and choose

    δ = min(1/2, ρ / (8(1 + L))),
    ε = ρ/8.

Both parameters are positive. The first choice gives δ ≤ 1/2 and
δ L ≤ ρ/8. Thus the numerator ε + chordalSin(δ)L is at most ρ/4,
while the cosine denominator is at least 1/2. The exact error is therefore
strictly less than ρ. The construction obtains a finite chordal net D containing A.

With N = D.card, choose

    t = max(1, log(N)/ε + 1).

Then t > 0 and log(N) < t ε. Geometry's explicit [Nontrivial E] hypothesis
makes D nonempty. Sublevels' compiled logarithmic equivalence gives the strict
cardinal margin N exp(-t ε) < 1.

`exists_outer_parameters_containing` requires a finite-dimensional nontrivial real
inner-product space and unit members of A. Compactness, convexity and nonemptiness
of K are not needed for this numerical selection theorem; those hypotheses are
required by Approximation's geometric theorems when the selected parameters are used
for an outer approximation. No ambient interior assumption is introduced.

This proves existence of parameters for each positive accuracy. It does not itself
construct an infinite nested sequence, prove analytic boundary charts, or establish
a sphere parametrization. The integrated Approximation module separately supplies the
compiled one-step nesting certificate under its explicit error-versus-margin condition.

Verification: `source scripts/environment.sh; lake build ConvexApprox.Construction`
passed without warnings (logs/construction-build-03.log). The exact type and axiom
audit passed (logs/construction-audit.log); its only dependencies are propext,
Classical.choice, and Quot.sound. The first attempted build recorded a dependency
parse error while the integrated Approximation source was being edited; the final module
imports the stable Sublevels and OuterApprox modules instead. No placeholder or new
axiom is present. The integrated build and independent statement review are separate.
