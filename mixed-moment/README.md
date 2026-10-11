# Mixed-moment integral cancellation

This project proves Taylor-contact cancellation for actual mixed-moment
Lebesgue integrals of rational polynomials. For `P,D : Polynomial ℚ`, natural
`L,j` with `j < L`, and one-sided or two-sided contact
`x*P(x)/sqrt(1-x²)-D(x)=O(x^L)` at zero, the corrected column integral equals
`rationalWitness P D j + catalanWitness P j * catalan`, with rational witnesses.
Integrability, the integral recurrences and boundary evaluations are proved.

The entry points are [MixedMoments.lean](MixedMoments.lean) and
[Applications.lean](MixedMoments/Applications.lean). The
[proof scope](docs/final-proof-scope.md) and
[21-record statement review](docs/final-statement-review.md) give the actual
definitions, assumptions and deferred clauses. This is a compiled scoped core;
the broader ordinary study is not claimed fully formalized.

The supplied completed build covers 17 modules and 77 rational examples. Its
public audit covers 513 named declarations, including 429 theorems; the full
project-origin inventory covers 835 constants, including private/generated
declarations. Ordinary axiom inspection permits only `propext`,
`Classical.choice` and `Quot.sound`. Five compiler-generated partial runtime
helpers are explicitly inventoried; their safe source parents are distinct.
The publication review separately checks recursor rule dependencies as well.
See [fresh publication evidence](evidence/publication/README.md) and the
[independent publication review](docs/publication-review.md) for current results.

Lean is pinned to 4.24.0 (commit
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`), and mathlib to
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. All nine exact dependency revisions
are in [lake-manifest.json](lake-manifest.json). Install this compiler, obtain
the pinned packages and their mathlib cache, then run from this directory:

```sh
lake build
python3 -B scripts/audit_lean.py
python3 -B scripts/audit_environment.py
lake env lean scripts/inductive_kernel_metadata.lean
python3 -B scripts/independent_checks.py --output logs/public-independent.json
```

`scripts/with-lean.sh` uses PATH, or the optional `MIXED_MOMENTS_LEAN_BIN`
compiler-bin directory. Fresh publication builds compile project sources from
an empty project build directory while reusing clean pinned dependency OLeans;
neither Lean nor mathlib is rebuilt from source here.

The standalone independent checker reads the existing public ordinary-study
certificate and performs 20,072 exact rational checks. The supplied full
certificate/provenance checker additionally needs the original 523,782-byte
source ZIP and its complete unchanged extraction, which are not redistributed:

```sh
python3 -B scripts/check_certificates.py --archive /path/to/input.zip \
  --source /path/to/complete-extraction --output logs/certificates-verification.json
```

It authenticates the fixed ZIP hash and all 107 extracted files before running
17,805 supplied checks, 20,072 independent checks and 993 provenance checks.
These finite checks do not prove analytic integrals or infinite sums. The
ordinary study's `lean_verification: not_performed` status stays unchanged.

Formal coordinates are in the free space `Fin 3 → ℚ`; evaluation into real
numbers is not assumed injective. A nonzero formal zeta coefficient proves
no arithmetic nonmembership in `ℚ+ℚG`. Catalan irrationality, arithmetic
independence and the optional pi/Basel evaluation are outside this scope.
The tail theorem retains the explicit range `2 ≤ i+N`, excluding `i=0,N=1`.

[Supplied evidence](evidence/supplied/logs/) remains historical, including
failed and interrupted attempts. Normalized paths and hashes never convert
a subset audit or failed command into a full-project pass. The whole-repository
[publication manifest](../publication/FILES.json) binds current public bytes;
[source dispositions](../publication/SOURCE-MAP.json) bind original and public
hashes for every archive candidate. Archives, private handoffs, dependencies,
binaries and build caches are excluded. Existing third-party attribution and
license are retained in [THIRD-PARTY.md](../THIRD-PARTY.md); no overall license
or novelty claim is added.
