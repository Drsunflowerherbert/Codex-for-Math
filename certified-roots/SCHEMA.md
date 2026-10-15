# Certificate input and output contract, version 1

`verify.py` is the authoritative validator. The accompanying
[`certificate.schema.json`](certificate.schema.json) describes the structural
JSON shape; its comments identify additional checks performed by the program.
No third-party JSON Schema package is needed to run the verifier.

## Input

Every top-level key below is required, and other keys are rejected.

| Key | Meaning |
| --- | --- |
| `schema_version` | The JSON integer `1`; a boolean or floating number is invalid. |
| `name` | A descriptive string; not used in the mathematics. |
| `variables` | An ordered list of unique strings; its length is the dimension `n`. |
| `polynomials` | Exactly `n` polynomials, in equation order. |
| `center` | Exactly `n` rational strings describing `c`. |
| `radii` | Exactly `n` strictly positive rational strings describing `r`. |
| `preconditioner` | An `n` by `n` rational matrix `Y`, in row order. It must be nonsingular. |

A polynomial is an array of terms. A term has exactly two keys:
`{"coefficient":"3/2", "powers":[2,1]}` means \((3/2)x_1^2x_2\).
Each exponent vector has length `n` and consists of nonnegative JSON integers.
Duplicate monomials, zero coefficients and empty polynomials are allowed;
their exact sums define the polynomial. There is no expression evaluation or
executable input. Variable labels do not change the ordered exponent positions.

Rational strings must match the full ASCII regular expression
`-?[0-9]+(?:/[1-9][0-9]*)?`. Numerator and denominator each have at most
128 decimal digits, excluding the sign and slash. Thus `"-2/3"`, `"0"`,
`"001/2"` and `"2/4"` are permitted. `"0.5"`, `"1e-3"`, `"+1"`,
`"1/0"`, `"1/02"`, surrounding whitespace and JSON numeric coefficients are
invalid. Output fractions are normalized by `Fraction`.

Additional limits and validations are:

- Strict UTF-8 JSON input of at most 1,048,576 bytes through `load_certificate`.
- Dimension between 1 and 8, at most 256 terms across all equations, and
  total degree at most 32 **per term**.
- Exactly matched dimensions for every vector, matrix and exponent vector.
- Duplicate JSON object keys, floats, `NaN` and infinities rejected while
  reading. Boolean values rejected in integer positions.
- Positive radii and invertible `Y`, checked by exact rational elimination.
- Unknown or missing keys rejected both at the top level and inside terms.

The file-size limit applies to file loading. The Python `analyze(data)` API
receives an already constructed object, validates its mathematical shape and
arithmetic limits, and cannot check the original byte encoding or duplicate
keys that a caller may already have discarded. Use `load_certificate` for
external JSON. Input bounds are operational limits, not a guarantee of bounded
runtime or memory for all possible rational computations.

For example, this certifies the boundary root of \(F(x)=x-1\) in `[-1,1]`:

```json
{
  "schema_version": 1,
  "name": "boundary root",
  "variables": ["x"],
  "polynomials": [[
    {"coefficient": "1", "powers": [1]},
    {"coefficient": "-1", "powers": [0]}
  ]],
  "center": ["0"],
  "radii": ["1"],
  "preconditioner": [["1"]]
}
```

## Output and exit codes

Run `python3 certified-roots/verify.py PATH.json` from the repository root.
The program writes a JSON report. Exit code `0` means both sufficient tests
passed; `1` means the input is valid but the combined criterion failed; `2`
means invalid input or invocation. An ordinary invalid-input report has
`status: "invalid"`, `certified: false`, and an explanatory `error` string;
argument usage errors are handled by Python's argument parser.

For valid inputs, all mathematical scalar outputs are **exact rational
strings**, including integers. Intervals are `[lower, upper]` pairs of such
strings. JSON numbers are reserved for the report schema version. The report
contains:

| Field | Exact interpretation |
| --- | --- |
| `center`, `radii`, `box` | The specified center, radii, and closed uniqueness box. |
| `preconditioner_invertible` | True after the exact rank check. |
| `residual` | The vector `F(c)`. |
| `step` | The vector `Y F(c)`; `T(c) = c - step`. |
| `d` | The componentwise absolute value of `step`. |
| `J` | The recomputed interval enclosure of `DF` over the entire box. |
| `E` | The interval matrix `I - Y J`, called `A` in the study. |
| `M` | Entrywise maximum absolute endpoints of `E`. |
| `q`, `eta` | The weighted contraction and residual-step bounds in the theorem. |
| `selfmap_lhs`, `slack` | `d + M r` and `r - (d + M r)`. |
| `contraction`, `self_map` | Separate Boolean results for `q < 1` and nonnegative slack. |
| `certified`, `status` | Combined result; status is `certified` or `not_certified`. |
| `failure_reasons` | Reasons for a failed sufficient test, with zero-based coordinates. |
| `weighted_error_bound` | `eta/(1-q)` when certified; otherwise `null`. It can be capped by 1 using the box. |
| `coordinate_error_bounds` | `min(r_i, r_i*eta/(1-q))` when certified; otherwise `null`. |

Reports also retain the descriptive `name` and ordered `variables`.
A valid `not_certified` report can contain useful diagnostics, including a
successful self-map test, but the verifier issues no error-bound certificate
for it. It does not assert nonexistence. Saved reports are evidence of a run,
not trusted inputs: recompute them from the source certificate and reviewed
verifier when assurance is needed.
