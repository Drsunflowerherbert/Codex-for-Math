# Exact certificates for approximate roots

A reusable first toolkit for proving that an exact real zero exists, is unique
in a specified **closed box**, and lies within a computable distance of a
rational approximate center. The method is classical fixed-preconditioner
contraction certification with exact rational interval arithmetic.

Start with [the study](STUDY.md), then follow the full calculations in
[the examples](EXAMPLES.md). The [input contract](SCHEMA.md) and
[JSON schema](certificate.schema.json) explain how to certify a new rational
polynomial system. [Verification and review](VERIFICATION.md) state what was
checked and what remains trusted.

## Run

Python 3.10 or later, standard library only. From the repository root:

```bash
python3 -B certified-roots/verify.py certified-roots/examples/circle-line.json
python3 -B certified-roots/verify.py certified-roots/examples/circle-parabola.json
python3 -B -m unittest discover -s certified-roots/tests -v
```

The verifier returns JSON and exits `0` for certification, `1` for a valid
candidate that fails this sufficient criterion, and `2` for invalid input.
Rational numbers are strings such as `"7/10"`. It recomputes all bounds from
the polynomial coefficients; an input cannot supply its own claimed Jacobian
or success flag.

| Example | Result | Exact information |
| --- | --- | --- |
| [Circle and line](examples/circle-line.json) | Certified | `q = 1/70`; each coordinate error at most `1/138`. |
| [Circle and parabola](examples/circle-parabola.json) | Certified | `q = 3/22`; each coordinate error at most `2/95`. |
| [Tiny residual, two roots](examples/tiny-residual-two-roots.json) | Not certified | Two roots are in the box, by separate algebra. |
| [Tiny residual, no root](examples/tiny-residual-no-root.json) | Not certified | No real root exists, by a separate positivity argument. |

## What acceptance means

For `T(x) = x - Y F(x)`, acceptance checks both:

1. An exact componentwise bound which ensures `T` maps the closed box into
   itself.
2. A strict weighted contraction bound `q < 1` throughout that box.

The study proves existence, uniqueness throughout that closed box, and the
residual/contraction error bound from these hypotheses. It carefully
distinguishes a map from its value, self-inclusion from contraction, and
uniqueness in a box from global uniqueness.

A small residual by itself is not a root certificate. Failed certification is
not nonexistence. This edition does not certify singular roots, enumerate all
roots, accept nonpolynomial functions, or run Lean. Exact arithmetic and
independent review are provided; the Python source and runtime remain trusted.

## Contents and provenance

- `verify.py`: exact checker and command-line entry point.
- `tests/test_verify.py`: adversarial, arithmetic, boundary and command-line tests.
- `evidence/`: reproducible output reports, test transcript and source manifest.
- `reviews/`: independent mathematics and implementation reviews with reviewed
  file hashes.
- `STUDY.pdf`: optional reading copy of the study and worked examples; Markdown
  and executable inputs remain the canonical sources.

The sources and historical comparison are linked in the study, including
[Rump's verification survey](https://www.tuhh.de/ti3/paper/rump/Ru10.pdf) and
[Hauenstein–Sottile on alpha theory](https://arxiv.org/abs/1011.1091v2). No novelty
claim or overall repository license is introduced.

This directory is an isolated addition based on integrated research commit
`e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f`, on branch
`codex/certified-roots-2026-10-15`. All prior repository files are preserved.
