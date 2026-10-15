# Rank-one stationary points of bivariate polynomials

First reviewed edition, 15 October 2026. This is an implementation and study of
classical splitting-lemma and plane-singularity methods, with ordinary proofs
and exact computations. **There is no novelty claim and no Lean verification.**

For a real polynomial with a stationary point at the origin and Hessian of rank
exactly one, a linear change and a possible sign reversal reduce the problem to

\[
 P_{YY}(0)>0,\qquad P_Y(X,\phi(X))=0,\qquad g(X)=P(X,\phi(X)).
\]

The original polynomial has the same local type as
\(\sigma(g(X)+Z^2)\), up to adding its value at the origin. Here
\(\sigma\in\{1,-1\}\) records the sign of its nonzero Hessian eigenvalue.

| Normalized residual | Original local classification |
| --- | --- |
| First nonzero term has odd degree | Saddle |
| First nonzero term has even degree and negative coefficient | Saddle |
| First nonzero term has even degree and positive coefficient | Strict minimum if \(\sigma=1\); strict maximum if \(\sigma=-1\) |
| Identically zero as an analytic germ | Non-strict minimum if \(\sigma=1\); non-strict maximum if \(\sigma=-1\) |

“Non-strict” means an extremum that is **not** strict. “Saddle” means every
neighborhood contains values above and below the value at the origin.

Read [the study and proofs](STUDY.md), [worked examples](EXAMPLES.md), and
[review records](reviews/README.md). The machine-readable cases are in
[examples.json](examples.json); the executable is [classifier.py](classifier.py).

## Run

Python 3.10 or later; no third-party dependencies are needed. From the repository
root:

```bash
python critical-points/classifier.py critical-points/examples.json
python critical-points/classifier.py critical-points/examples.json --example quartic_plus --bound ploski
python -m unittest discover -s critical-points -p 'test_*.py' -v
```

The example ids are listed in `examples.json`. For your own polynomial, create
a JSON object with `terms`. A term `[i,j,c]` means \(c x^i y^j\); for example,
\((y-x^2)^2+y^4\) is:

```json
{"terms": [[0,2,"1"], [2,1,"-2"], [4,0,"1"], [0,4,"1"]]}
```

Coefficients must be rational strings or JSON integers. Strings such as `"1/3"`
and `"0.125"` denote exact rationals. JSON floating-point numbers are rejected.
Duplicate monomials are combined before checking the hypotheses and degree.
The origin must already be stationary; translating an arbitrary point is the
caller's responsibility. Hessians of rank zero or two are rejected.

The default `--bound bezout` proves termination by checking residual coefficients
through \(N=(d-1)^2+1\). The optional `--bound ploski` uses
\(N=(d-1)^2-\lfloor d/2\rfloor+1\) for \(d\ge3\), after the source hypotheses
checked in the study; degree two uses \(N=2\). The algorithm stops early as soon
as a nonzero residual coefficient is found. In particular, a quartic can require
order eight, exceeding its polynomial degree.

`--max-order K` sets a coefficient budget. If the budget ends before the bound
with no nonzero coefficient, the result is `unresolved`, and
`residual_identically_zero` is `null`. It never converts an insufficient zero
jet into a proof of a zero residual. Resource exhaustion is also possible for
large inputs; the implementation makes no practical polynomial-time claim.

## Inspect the output

The output records the exact original value and Hessian, the rational matrix
mapping normalized coordinates back to original coordinates, the sign `sigma`,
the normalized polynomial, the critical-branch jet, and the first nonzero
residual coefficient. All rational output coefficients are strings. If a
nonzero coefficient is found, `milnor_number` is its order minus one, for the
local **complex** singularity. A zero residual has a non-isolated critical
curve, so that field is `null`, not a finite Milnor number.

The reported jets end at `computed_order`; omitted coefficients through that
order are zero. The critical branch and residual generally continue as infinite
convergent series. Only `residual_identically_zero: true` asserts a full identity,
using the finite-bound proof. `critical_series(normalized_terms, order)` also
exposes longer exact jets for independent inspection.

## Scope and evidence

The mathematical classification covers all real polynomial inputs satisfying
the hypotheses. This executable handles their **rational-coefficient** subset.
Exact algebraic coefficients could be supported with an ordered algebraic field
implementation; arbitrary real coefficients require additional representation,
equality and sign information. Floating-point tolerances are not a replacement.

The analytic reduction also holds for real analytic functions, but a polynomial
degree bound does not apply to arbitrary analytic input. Smooth flat residuals
can have identical Taylor series and different local types. No explicit
neighborhood radius is computed or certified. This classifies a germ at the
origin, not global extrema or other critical points.

[Validation evidence](evidence/validation.json) records fresh checks for this
edition. The Python runtime, parser, arithmetic implementation, and reviewer
judgment remain part of the trust boundary. Tests are finite checks, separate
from the ordinary mathematical proofs. Review records identify the exact
reviewed files by SHA-256.

All tracked changes in this edition are under `critical-points/`, on branch
`codex/critical-points-2026-10-15`, based on
`e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f`. Existing branches are preserved;
publication does not merge this branch into any other branch.
