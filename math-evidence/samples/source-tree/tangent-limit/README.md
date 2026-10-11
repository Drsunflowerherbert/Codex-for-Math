# Conditional decay and absolute convergence of integer tangents

This standalone Lean 4 project proves, with an explicit hypothesis, that
`tan(n)/n³ → 0` along positive integers and that `Σ |tan(n)|/n³` converges.

The hypothesis is retained as the argument `h : TangentLimit.PiDiophantine`:

> For every real ν > 2, all sufficiently large positive integers q and every
> integer p satisfy |π − p/q| ≥ q^(−ν).

The project does not prove or supply this hypothesis. Its source contains no
placeholder proofs or added axioms. The compiled theorem inventory records
only Lean's standard foundational axioms: `propext`, `Classical.choice`, and
`Quot.sound`.

## Pinned versions and reproduction

- Lean **4.24.0**, compiler commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`.
- mathlib **v4.24.0**, exact commit `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.
- All transitive dependency commits are fixed in `lake-manifest.json`.

Prerequisites: Bash, Git, curl, Python 3, tar, and sha256sum. From the repository
root:

```bash
cd tangent-limit
./scripts/setup.sh
./scripts/verify.sh
```

Setup installs the pinned compiler, downloads the official alternate mathlib
cache, and preserves the supplied dependency manifest. Verification builds the
project, prints theorem statements and axiom dependencies, and scans source for
proof placeholders and added axiom declarations. An existing Elan installation
can be selected by setting `ELAN_HOME` before running the scripts.
Otherwise setup uses a project-local, ignored `.elan/` directory.

## Proof and source

The complete ordinary mathematical proof was saved **before** formalization in
`docs/mathematical-proof.md`. It chooses the nearest odd denominator
`q = 2 * floor(n / π) + 1`, controls distance to its tangent pole, and derives
`|tan(n)| ≤ π q^(ν−1)` eventually. Exponent 3 gives the limit; exponent 5/2
gives comparison with the summable sequence `π 2^(3/2) n^(−3/2)`.

| Source file | Result |
| --- | --- |
| `TangentLimit/Hypothesis.lean` | Visible, unproved hypothesis |
| `TangentLimit/NearestPole.lean` | Nearest odd construction and geometric bounds |
| `TangentLimit/Trigonometry.lean` | Cosine/offset identity and sine chord estimate |
| `TangentLimit/Diophantine.lean` | Approximation-error algebra and eventual growth |
| `TangentLimit/LimitComparison.lean` | Reusable quadratic-growth limit lemma |
| `TangentLimit/Limit.lean` | Requested conditional limit |
| `TangentLimit/NonPole.lean` | Cosine is nonzero at every integer argument |
| `TangentLimit/Summability.lean` | Requested absolute convergence and signed convergence |

Every principal result has a positive-integer version indexed by `n+1`.
Natural indexing also includes a harmless zero term. `NonPole.lean` uses the
standard mathlib irrationality theorem for π to certify ordinary tangent
values at all integer arguments.

## Verification and saved progress

- `logs/final-build.log`: complete project build.
- `logs/final-theorem-inventory.log`: compiler-generated statements and axioms.
- `logs/source-audit.log`: source placeholder/axiom-declaration scan.
- `docs/theorem-statements.md`: readable copy of the compiled inventory.
- `docs/independent-review.md`: independent proof and formalization review.
- `PROGRESS.md` and `milestones/`: milestone summaries, timestamped source/log
  records, and preserved status of each compiled result.
- `logs/`: final verification and selected successful milestone/module builds.

This repository contains a reviewed publication subset. Local dependency
caches, compiler binaries, temporary diagnostics, downloaded installer scripts,
and compressed working-session snapshots were not uploaded. The original local
project retains the earlier setup and compilation attempts.

The initial 4.19.0 cache attempt failed because the environment rejected its
official Azure host. The exact 4.24.0 release had a reachable official cache;
all 7335 cache files downloaded successfully. The final build uses 4.24.0.

The supplied research starter's relevant ordinary proofs and reviews are
preserved under `docs/starter-reference/`. All 38 packaged manifest hashes
matched. The relevant bridge proof and ordinary review are retained; see
`docs/SOURCES.md` and `docs/starter-assessment.md` for attribution and the
boundary between that evidence and the present compilation.

To save another inspectable snapshot:

```bash
./scripts/checkpoint.sh my-checkpoint
```

Dependency caches and compiler binaries are excluded from distributable source
archives; the pinned setup script retrieves them.
