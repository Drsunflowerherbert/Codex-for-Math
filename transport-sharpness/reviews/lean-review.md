# Independent Lean statement and kernel review

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

Reviewed on 2026-10-13 by the independent Lean-review agent. The complete
public declaration types and defining bodies of `TransportSharpness/Finite.lean`
and `TransportSharpness/Obstruction.lean` were read independently before
authoring `scripts/ReviewHarness.lean`. No theorem assumes its own conclusion,
and the natural finite marginal, positivity, and exponent hypotheses support
the conclusions stated. No mathematical scope defect was identified.

The final reviewed mathematical source hashes are:

| File | SHA-256 |
| --- | --- |
| `TransportSharpness/Finite.lean` | `2ca131e39877bb4ec3d0803de4b9bdfa21d7d2e2935f9777db0408aa3cadf18a` |
| `TransportSharpness/Obstruction.lean` | `ebb8d5361a6dce5ebc7e436d59750a58581030ca1d351e420f9280dcf83df0e1` |
| `scripts/ReviewHarness.lean` | `6ebc84014b1cd2b08dfc1817e996efe769adddd5a824343252a4b313c1bc52ad` |
| `scripts/Replay.lean` | `9971da32d70cf9b9ae6efaa19ca216d9b96d1253039d91315fbe603946d3c93f` |

## Formalized scope and hypotheses

`Atom` is exactly `Fin 3`; `Plan` is a real-valued three-by-three matrix.
`IsCoupling` requires nonnegative entries and the specified equal row and
column marginals. Its definition is independently body matched, so a
conclusion is not hidden inside that predicate. `mass_sum` proves total mass
one for the explicit mass list; `mass_positive` requires `0<a<1`.
`matching_coupling` admits the boundary cases `a=0` and `a=1`, which are not
three-positive-atom examples.

`sqCost` uses the sum of squared coordinate differences between the displayed
two-dimensional atoms. It does not use Lean's default product norm. Its
definition and those of `sourcePoint`, `targetPoint`, and `pCost` are body
matched. Finite weak duality, the projected dual certificate, and the matching
plan prove an attained optimum `a*b^p` for every real `p>0`, with `0<=a<=1`
and `b>=0`. The usual Wasserstein interpretation requires `p>=1`; the core
does not introduce an abstract Wasserstein-distance definition.

`commonSource` is the displayed matrix with diagonal entries
`((1-a)/2-b/8, a-b/4, (1-a)/2-b/8)` and four central off-diagonal entries
`b/8`. `Admissible` is independently matched to exactly
`0<b`, `b<a`, and `a+b<1`. Under these hypotheses the matrix is a coupling.
Its quadratic cost is exactly `b/2+a*b^2`. The strict cost-comparison theorem
assumes only `b>0` because it states an algebraic inequality; interpreting both
matrices as probability couplings additionally uses their coupling theorems.

`mapSize` is defined to be `sqrt(b/2+a*b^2)` and `targetDistance` to be
`a^(1/p)*b`. These are scalar definitions. Their names alone do not identify
them with a map norm or a Wasserstein distance. The independently reviewed
ordinary proof supplies that identification; it is not encoded in this core.

For `b=a/2`, the formalized lower bound has exponent
`1/2-alpha*(1+1/p)`. `shrinking_exceeds_constant` kernel checks the quantifiers:
for every real proposed constant `C`, every real `p>=1`, and every exponent
`alpha>p/[2(p+1)]`, an admissible `a in (0,1/2)` strictly violates the scalar
estimate. `W2_exceeds_constant` specializes that threshold to `1/3`. The
proof uses real-power divergence, not numerical extrapolation.

The separate fixed-mass theorem fixes any `a in (0,1)` and finds an admissible
shrinking `b` for every `alpha>1/2` and every real `C`. Its scalar type permits
all real `p`, including Lean's totalized `1/p` at zero. Its restriction to
`p>=1` has the intended Wasserstein interpretation. No `1/3` obstruction is
claimed from fixed positive mass.

## Fresh checker evidence

The independent harness manually specifies all 48 closed whole declaration
types: 19 definitions/abbreviations and 29 theorems. It separately specifies
all 19 defining bodies. Expected theorem types do not programmatically read
the target types, and no target is specialized to a convenient instance.
Dependencies among expected expressions refer only to separately body-matched
definitions. The unchanged published helper is
`math-evidence/lean/EvidenceHarness.lean`, SHA-256
`bb71282fcb088498a9c40b0460694f1663e8f3a145fc15469050b8ade2f390dc`.
Its `LEAN-RECEIPTS.md` protocol was read before constructing this harness.

An initial fresh execution ran from `01:54:38` to `01:56:33` UTC on
2026-10-13. It passed compilation, all 48 whole-type matches, all 19 body
matches, and same-kernel replay of 75 local declarations against the imported
`[Mathlib, EvidenceHarness]` baseline. The union of the actual transitive
axiom closures was exactly `propext`, `Classical.choice`, and `Quot.sound`.
No `sorryAx` or custom axiom occurred. Its complete phase evidence is
`evidence/lean-review/20261013T015438415836Z/report.json`.

The exact initial command, from the scoped directory, was:

```sh
python3 evidence/lean-review/verify.py --lean ${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lean --lake ${PINNED_REPOSITORY}/tangent-limit/.elan/bin/lake --elan-home ${PINNED_REPOSITORY}/tangent-limit/.elan --toolkit ${PROJECT_REPOSITORY}/math-evidence
```

The original driver used Python `assert` guards, active in that ordinary
execution. Its exact bytes are retained as that attempt's
`driver-before-hardening.py`, matching the originally captured driver
SHA-256 `abcd4b417ee6183244b327dda21ac8c8572c7c462bfb04628440f8aa8ecb81ef`.
The driver was subsequently hardened to explicit `require` failures, so
optimization cannot strip its checks. The old evidence remains an observation
of the original execution, rather than a claim that hardened code ran then.

The hardened driver also checks for forbidden Lean proof escape tokens outside
comments and string literals, hashes configuration/helper/runner before and
after, preserves the exact runner in each new attempt, and checks all products
and captured stdout/stderr files before declaring success. An independently
executed `python3 -O` smoke test confirmed that a false `require` fails and
that nested comment, line comment, string-literal, and forbidden-token cases
behave as intended. Two final fresh executions of the hardened driver passed:

| Run | UTC start–finish on 2026-10-13 | Report |
| --- | --- | --- |
| Ordinary Python | `02:00:02`–`02:01:33` | `evidence/lean-review/20261013T020002583180Z/report.json` |
| Optimized Python (`-O`) | `02:01:48`–`02:03:49` | `evidence/lean-review/20261013T020148426067Z/report.json` |

Both accepted 48 full closed declaration types and 19 defining bodies and
replayed 75 local declarations. All listed preflight and postflight checks
passed. Both used the hardened driver with SHA-256
`cd90ddc83f0b78b8ded197166f2b699200d713def91d7366d5d10c1795f0603a`.
The optimized report records optimization level one and the
`explicit_require_not_assert` guard contract. Every retained phase exited zero;
the core module compilation stderr streams were empty. The proof sources and
harness hashes are the final hashes listed above, identical across all three
fresh executions.

The ordinary final command was exactly the initial command displayed above.
The optimized final command was:

```sh
python3 -O evidence/lean-review/verify.py --lean ${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lean --lake ${PINNED_REPOSITORY}/tangent-limit/.elan/bin/lake --elan-home ${PINNED_REPOSITORY}/tangent-limit/.elan --toolkit ${PROJECT_REPOSITORY}/math-evidence
```

Every fresh execution compiles the unchanged helper, `Finite`, `Obstruction`,
the root import module, `ReviewHarness`, and `Replay` to a new private cache.
Existing project oleans are excluded. All nine package Git HEADs, origins, and
clean tracked-source states are checked against the pinned Lake manifest,
before and after. The Lean loader and four runtime libraries match the fixed
Linux release-member byte pins from the published evidence toolkit. The
compiler reports Lean `4.24.0`, commit
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`; mathlib HEAD is
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.

Each report contains the exact subprocess argv, cwd, relevant `ELAN_HOME` and
`LEAN_PATH`, start/finish times, exit codes, source/product hashes, and separate
stdout/stderr byte counts and hashes. Raw outputs are retained beside it. The
compiled binaries and private caches are ignored and are not publication
artifacts.

## Boundaries and deferred obligations

These are custom scoped review reports using the published helper. They are
not the tangent-only `live.cjs` runner's `math-live-receipt/v1` receipts. A
stored report describes an observed execution; its hashes do not authenticate
past process events. This review does not claim native Mac MRS integration.

Replay uses the same pinned Lean kernel implementation and rechecks the local
declaration closure, including generated proof auxiliaries. It does not
independently implement the kernel, rebuild or replay imported Mathlib proof
bodies, authenticate host runtime libraries, or rederive the cached dependency
oleans. Those cached dependency artifacts and the host remain explicit trusted
inputs. Dependency HEAD/origin/clean-source checks and selected compiler-member
byte checks do not eliminate that trust boundary.

The remaining formalization obligations are the Lebesgue cube probability
measure and its density bounds, measurability and null tie boundaries, affine
cell integration, source-map pushforwards, quadratic source-map optimality and
uniqueness, and the identification of the finite same-source matrix with the
map norm. Finite optimizer uniqueness also remains an ordinary equality-case
argument. The independent proof review establishes these bridges by ordinary
mathematics; this Lean review does not label them kernel checked.

No global upper estimate, endpoint optimality, positive target-density result,
or novelty claim follows from the accepted finite/scalar declarations. The
atomic targets have no Lebesgue densities; fixed density bounds apply to the
source on its cube, not to the targets or globally as a positive lower bound.
