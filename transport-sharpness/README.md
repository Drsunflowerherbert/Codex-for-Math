# Transport exponent obstruction: exact finite core

This scoped continuation audits the prior three-atom example and supplies
pinned Lean proofs and exact rational regression data. The original
Euclidean definitions support the necessary finite-p exponent ceiling
`p/[2(p+1)]`, including `1/3` for W2. Shrinking central atom mass is essential
to that family. Fixing positive atom masses gives the separate `1/2` ceiling.
Neither calculation proves a positive global upper estimate, endpoint
optimality, or mathematical novelty.

For uniform probability `rho=2^-d 1_[-1,1]^d dx`, `d>=2`, and
`0<b<a`, `a+b<1`, the unique quadratic optimal maps from the affine potentials
`max(-x1,a,x1)` and `max(-x1,a+b*x2,x1)` satisfy

\[
\mu=\frac{1-a}{2}(\delta_{-e_1}+\delta_{e_1})+a\delta_0,\quad
\nu=\frac{1-a}{2}(\delta_{-e_1}+\delta_{e_1})+a\delta_{be_2},
\quad W_p^p=ab^p,\quad \|T_\mu-T_\nu\|_2^2=b/2+ab^2.
\]

The source density bounds on the cube are both exactly `2^-d`, uniformly in
the parameters. The targets are atomic and have no Lebesgue densities.

| Family | Central mass and displacement | Necessary L2 exponent ceiling |
|---|---|---|
| Shrinking mass | `a -> 0`, `b=a/2` | `p/[2(p+1)]`; W2 `1/3`, W1 `1/4` |
| Fixed mass | `a=a0 in (0,1)`, `b -> 0` | `1/2` for every finite `p>=1` |

The [full derivation](docs/derivation.md) and
[independent proof review](reviews/proof-review.md) give the precise
hypotheses, probability calculations, quadratic duality/uniqueness proof,
and quantified failure of every uniform constant. [Sources and licenses](docs/SOURCES.md)
record the baseline, upstream comparison, toolkit and toolchain pins.

## What is machine checked

[Finite.lean](TransportSharpness/Finite.lean) proves finite probability
normalization, coupling validity, primal/dual optimal costs for quadratic and
every real positive p-cost, and the candidate common-source matrix's exact
cost. [Obstruction.lean](TransportSharpness/Obstruction.lean) proves real-power
identities and that every proposed real constant is exceeded for exponents
above each family's ceiling. These statements use explicit finite arrays
and scalar formulas. Their interpretation as actual Brenier-map quantities
uses the separately reviewed ordinary Euclidean measure proof.

The measure-theoretic map construction, pushforward identification,
Lebesgue integration, null ties, and higher-dimensional product extension
are deferred Lean obligations. They are not disguised as assumptions proving
an entire transport theorem. The sources contain no proof placeholders,
added axioms or unsafe proof shortcuts. A separate review checks complete
expected declaration types, definition bodies, transitive allowed axioms,
and local declaration replay using the published evidence helper and the
same pinned Lean kernel; see [Lean review](reviews/lean-review.md).

## Exact examples and regression data

The [standard-library checker](scripts/check_exact.py) derives all cell
halfplanes from the actual affine pieces and computes rational polygon
intersection areas. Matching primal/dual certificates establish each
finite optimal value; independent vertex enumeration adds a cross-check.

- [13 named cases and seven rejected inputs](data/exact-cases.json), including
  near-clipping boundaries and explicit counterexamples to formulas used
  outside their hypothesis range.
- [100 admissible rational-grid cases](data/regression-grid.json).
- [48 exact proposed-constant violations and endpoint regressions](data/exponent-regressions.json).
- [Regression tests](tests/test_exact.py) include independent slice integration,
  deliberate broken certificates and hypothesis guards. All 16 pass, also
  with Python optimization enabled.

| `a` | `b` | W2 squared | Map L2 squared |
|---|---|---|---|
| `1/4` | `1/8` | `1/256` | `17/256` |
| `1/100` | `1/200` | `1/4000000` | `10001/4000000` |
| `1/4` | `1/32` | `1/4096` | `65/4096` |

The last row has fixed atom masses `(3/8,1/4,3/8)`. All arithmetic is exact;
no decimal root calculations establish a proof. The rational-power witnesses
raise the ratio to a positive integer power that clears exponent denominators.
Finite experiments do not establish all-parameter limits or Lean acceptance.

```sh
python3 -B scripts/check_exact.py --verify
python3 -B -O -m unittest discover -s tests -v
python3 -B scripts/check_exact.py --case 1/100 1/200
```

Lean/mathlib pins are in [lean-toolchain](lean-toolchain),
[lakefile.toml](lakefile.toml) and [lake-manifest.json](lake-manifest.json).
The saved environment's official Lean is reused without changing shell
profiles or credentials. See [verification instructions](docs/verification.md)
for fresh compilation, full-type/body checks, replay and trust limits.

The task branch is `codex/transport-sharpness-2026-10-13`, rooted at
`b1d6c20e2f02b484d09c5285e67d842b369f9df0`. Only this directory is published;
previous work and shared manifests are preserved. Publication evidence and
remaining obligations are in [STATUS.json](STATUS.json).
