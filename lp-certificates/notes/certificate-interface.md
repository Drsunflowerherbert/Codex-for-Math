# Exact certificate interface, version 1

`verifier.py` accepts one UTF-8 JSON document. Every object has exactly its
documented fields; unknown and missing fields are errors. Duplicate JSON keys,
floating-point values, booleans used as numbers, nonfinite constants, malformed
dimensions, and deeply nested JSON are invalid inputs. The dimension is the
length of the objective vector; zero variables and empty constraint lists are
supported.

Rationals are JSON integers or strings matching
`[+-]?[0-9]+(?:/[1-9][0-9]*)?`. Thus `"-2/3"`, `"+7"`, `0`, and `"0/5"` are
valid; `0.5`, `"0.5"`, `"1/0"`, and `true` are invalid. Denominators must be
positive; the standard-library `Fraction` type reduces values exactly.
There is no tolerance, implicit rounding, or approximate acceptance.

The Python verifier has explicit resource budgets: JSON text at most 1 MiB,
at most 32 variables and 128 rows, each reduced input numerator/denominator at
most 1024 bits, and total reduced input rational bit length at most 131072. Exact output
numerators/denominators are capped at 8192 bits; the runtime's integer-formatting
limit can impose a lower cap. An exceeded budget or formatting limit yields
`status: "invalid"`, `accepted: false`, and a `resource_limit` diagnostic.
It never implies an LP classification. Exactness applies to supported inputs;
large mathematically valid witnesses may require another verification setup.

```json
{
  "version": 1,
  "problem": {
    "objective": {"sense": "max", "coefficients": [3, 2]},
    "constraints": [
      {"coefficients": [1, 1], "sense": "<=", "rhs": 4},
      {"coefficients": [1, -1], "sense": "=", "rhs": 0}
    ]
  },
  "certificate": {
    "kind": "optimal",
    "point": [2, 2],
    "inequality_multipliers": ["5/2"],
    "equality_multipliers": ["1/2"]
  }
}
```

Variables range freely over the reals. Bounds such as `x_j >= 0` must be rows.
The objective sense is `"max"` or `"min"`; an additive objective constant is
not supported. Each constraint sense is `"<="`, `">="`, or `"="`. Every
coefficient vector and supplied point/direction has the exact objective length.
Only nonstrict linear inequalities and equalities are supported.

The checker negates **both** coefficients and right-hand side of each `>=` row,
and negates the objective coefficients for minimization. Inequality multipliers
are then nonnegative weights on normalized `<=` rows. Their array follows the
original order of all nonequality rows, including flipped `>=` rows. Equality
multipliers follow the original order of all equality rows and can have either
sign. The corresponding signed weight on an unflipped `>=` row is the negative
of the supplied nonnegative multiplier.

An `optimal` certificate contains exactly `kind`, `point`,
`inequality_multipliers`, and `equality_multipliers`. It checks feasibility,
nonnegative inequality weights, a complete coordinatewise identity with the
normalized objective, and equality of the combined bound and candidate value.
Its `checks` report the exact feasibility, multiplier-sign, coefficient-identity,
and attained-bound comparisons. Weighted slack products are explained in the
mathematical notes; they are not emitted as separate output fields.

An `infeasible` certificate contains exactly `kind`, `inequality_multipliers`,
and `equality_multipliers`. The same combination must have coefficient vector
zero and strictly negative right-hand side. No primal point is supplied.

An `unbounded` certificate contains exactly `kind`, `base_point`, and
`direction`. It checks base-point feasibility, nonpositive normalized inequality
direction products, zero equality direction products, and strictly positive
normalized objective gain. A base point cannot be omitted.

The Python API is `verify(document)` for a decoded object and
`verify_json(text)` for JSON text. Only the latter can detect duplicate keys;
the former cannot recover keys lost by another JSON parser. The command-line
interface reads JSON itself with duplicate detection:

```sh
python3 verifier.py examples/optimal_mixed_redundant.json
python3 verifier.py - < examples/infeasible_mixed.json
```

Results are deterministic JSON, with `status` equal to `accepted`, `rejected`,
or `invalid`, an `accepted` Boolean, and diagnostics. Well-formed documents
include exact individual `checks` with rational left/right values and a
`passed` Boolean. CLI exit codes are respectively `0`, `1`, and `2` (I/O errors
also return `2`). An original optimal objective value is certified only for an
accepted optimality certificate. Failed checks classify the **certificate**;
they do not classify the LP.

The Lean interface uses finite typed matrices in `Problem ℚ n m k`, already
normalized to `<=` rows and a maximization objective. `checkOptimal`,
`checkInfeasible`, and `checkUnbounded` compute Boolean decisions of the exact
arithmetic predicates. Their three `*_sound_real` theorems quantify over real
feasible points. The JSON parser, Python arithmetic runtime, and external
normalization-to-Lean correspondence have not been formally proved equivalent
to those definitions. Independent arithmetic tests and hand transcription
review are evidence about that boundary, not an extraction theorem.

All nine accepted JSON fixtures have matching normalized Lean examples:
`mixedRedundant`, `singletonMin`, `contradiction`, `equalityContradiction`,
`lineRayMin`, `zeroVariableFeasible`, `zeroVariableInfeasible`, `freeRay`, and
`constantNoRows`. Additional Lean rejection and alternate-weight examples are
independently stated and do not purport to mirror every rejection JSON fixture.

The follow-up `InputProblem` interface in `LPCertificates/Input.lean` preserves
the original rational rows, their source order and senses, and the original
objective sense. Its normalization and original-real soundness implications are
proved inside Lean. The checked export path generates literal instances of this
raw model and requires fresh kernel checking of each supplied witness; see
[checked bridge](checked-bridge.md). Parsing/literal-generation fidelity remains
an independently tested external boundary, not a proved parser refinement.
