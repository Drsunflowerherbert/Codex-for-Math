# Reproduction and verification boundaries

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

The saved Linux environment supplies the official Lean 4.24.0 compiler at
`${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux`
and the nine pinned dependency checkouts under the saved tangent project's
`.lake/packages`. Its original checkout and tracked files were preserved.
No tool update, shell-profile modification, credential operation or package
purchase is part of this workflow.

From this task's `transport-sharpness/` directory, reuse those already installed
packages through a local, ignored symlink if needed:

```sh
mkdir -p .lake
ln -s ${PINNED_REPOSITORY}/tangent-limit/.lake/packages .lake/packages
```

If the symlink already exists, retain it and inspect its resolved location.
On another machine use the pinned official compiler and lockfile packages;
the existing [tangent setup instructions](../../tangent-limit/README.md)
describe the official pinned installer. Do not substitute a floating toolchain
or `lake update`. Dependencies and compiler caches are excluded from publication.

A normal development build uses:

```sh
export ELAN_HOME=${PINNED_REPOSITORY}/tangent-limit/.elan
export PATH="$ELAN_HOME/bin:$PATH"
lake build
```

The recorded final development build completed successfully with no warnings
([log](../evidence/development-build.log)). A build by itself is weaker than
the fresh audit below and does not assert the measure-theoretic bridge.

## Fresh full-type, body, axiom and replay audit

The independently written driver is
[`verify.py`](../evidence/lean-review/verify.py). Each execution uses a new
attempt directory, copies the inspected inputs into a private ignored cache,
and excludes all old project OLeans from the import path. Its helper is the
unchanged published [EvidenceHarness.lean](../../math-evidence/lean/EvidenceHarness.lean),
whose SHA-256 is fixed in the driver.

```sh
python3 -B evidence/lean-review/verify.py \
  --lean ${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lean \
  --lake ${PINNED_REPOSITORY}/tangent-limit/.elan/bin/lake \
  --elan-home ${PINNED_REPOSITORY}/tangent-limit/.elan \
  --toolkit ${PROJECT_REPOSITORY}/math-evidence
```

The driver records exact argv, cwd, selected environment, timestamps,
stdout/stderr bytes and SHA-256, exit codes, source identities and outcomes.
The review checks all 48 closed public declaration types against separately
written expected terms, all 19 transparent definition bodies, and transitive
axioms against `{propext, Classical.choice, Quot.sound}`. A separate replay
checks the local declaration closure against `[Mathlib,EvidenceHarness]`
using the same Lean kernel. The 75 replayed declarations include generated
local auxiliaries. The review harness does not specialize target binders or
read a target's type to manufacture the expected type.

Preflight checks compiler/runtime bytes, Lean version and compiler Git hash,
all nine package HEAD/origin pins and clean tracked sources. Postflight checks
sources, configuration, helper, driver, compiler/runtime and recorded outputs.
The initial successful driver's assertion-based checks were replaced by
explicit exceptions before final acceptance so Python `-O` does not erase
its verification guards. The initial attempt and its exact driver bytes remain
archived as historical evidence; final hardened runs are identified by the
[Lean review](../reviews/lean-review.md) and [STATUS.json](../STATUS.json).

The published [toolchain byte audit](../evidence/compiler-audit.json) separately
compares five installed compiler/runtime members with the existing verified
release archive. The archive digest matches the previously published official
installer pin. This is a byte comparison, not a release-signature audit.

## Exact arithmetic and independent geometry

```sh
python3 -B scripts/check_exact.py --verify
python3 -B -O -m unittest discover -s tests -v
python3 -B reviews/independent_slice_check.py
```

The first command recomputes three deterministic JSON reports and requires
byte equality without overwriting them. It checks 13 named examples, 100
admissible rational pairs, seven rejected inputs and 48 exact counterexamples
to proposed positive constants. The 16 tests include independently integrated
clipped slices, faulty primal/dual certificates, full plane comparisons and
endpoint/subcritical hypothesis guards. Optimization leaves all checker guards
active. The last command belongs to the independent reviewer and checks all
nine common-source joint masses through interval-slice integration, separately
from polygon clipping or the advertised joint-matrix formula.

For even integer p the entire finite Euclidean p-cost matrix is rational.
For W1 the exact checker verifies the projected lower bound and the matching
upper bound; it does not approximate irrational off-diagonal costs. Rational
nonintegral-p ratio regressions clear exponents with a positive integer power;
they are consequences of the ordinarily proved real-p formula, rather than a
rational optimization of an irrational cost matrix.

## Remaining obligations and trust

The finite/scalar core has local Lean acceptance under the inspected pinned
cached environment. Ordinary proofs still establish source normalization,
null ties and Borel maps, integration of source-to-target duality, pushforward
identification with the finite array, exact slice areas, higher-dimensional
product reduction, and the representation of every Borel target coupling by
its finite mass array. These are substantive deferred formalization tasks.
Finite target optimizer uniqueness is ordinary mathematics here, with explicit
finite even-p certificate checks; there is no kernel theorem claiming it.

Cached dependency OLeans and host runtime are trusted; dependency proof bodies
were not rebuilt or replayed. Local replay uses the same kernel implementation,
not a second independent proof checker. This custom audit is not an accepted
fixed plan of the toolkit's `live.cjs`, not a `math-live-receipt/v1` receipt,
and not a native Mac MRS integration. Source hashes, ordinary reviews,
regression execution and stored receipt inspection never grant a new Lean pass.
Only the fresh complete Lean phases establish the scoped local acceptance.
