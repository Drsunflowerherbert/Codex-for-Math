#!/usr/bin/env python3
"""Check rational LP certificates using exact arithmetic and no third-party code.

Variables range freely over the reals; bounds must be explicit constraint rows.
Inequalities ``>=`` are negated and minimization objectives are negated before
checking. This checker verifies supplied witnesses; it never searches for one.
See notes/certificate-interface.md for the mathematical interpretation.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path
import re
import sys
from typing import Any, Mapping, Sequence


RATIONAL_PATTERN = re.compile(r"[+-]?[0-9]+(?:/[1-9][0-9]*)?\Z")


class SchemaError(ValueError):
    """An input that cannot be interpreted as a v1 certificate document."""

    def __init__(self, code: str, path: str, message: str) -> None:
        self.code, self.path, self.message = code, path, message
        super().__init__(message)

    def diagnostic(self) -> dict[str, str]:
        return {"code": self.code, "path": self.path, "message": self.message}


@dataclass(frozen=True)
class Row:
    coefficients: tuple[Fraction, ...]
    rhs: Fraction
    source_index: int


@dataclass(frozen=True)
class Problem:
    objective: tuple[Fraction, ...]
    original_objective: tuple[Fraction, ...]
    sense: str
    inequalities: tuple[Row, ...]
    equalities: tuple[Row, ...]

    @property
    def dimension(self) -> int:
        return len(self.objective)


@dataclass(frozen=True)
class Certificate:
    kind: str
    point: tuple[Fraction, ...] = ()
    direction: tuple[Fraction, ...] = ()
    inequality_multipliers: tuple[Fraction, ...] = ()
    equality_multipliers: tuple[Fraction, ...] = ()


def rational(value: Any, path: str) -> Fraction:
    """Accept only JSON integers or signed integer / positive denominator strings."""
    if type(value) is int:
        return Fraction(value)
    if type(value) is str and RATIONAL_PATTERN.fullmatch(value):
        try:
            if "/" in value:
                numerator, denominator = value.split("/")
                return Fraction(int(numerator), int(denominator))
            return Fraction(int(value))
        except ValueError as exc:
            raise SchemaError("rational", path, "Rational integer is too large to parse.") from exc
    raise SchemaError(
        "rational", path,
        "Expected an integer or exact string n/d with positive denominator; floats and booleans are forbidden.",
    )


def object_fields(value: Any, fields: set[str], path: str) -> Mapping[str, Any]:
    if not isinstance(value, dict):
        raise SchemaError("object", path, "Expected an object.")
    if any(type(key) is not str for key in value):
        raise SchemaError("field", path, "Object field names must be strings.")
    unknown = sorted(set(value) - fields)
    missing = sorted(fields - set(value))
    if unknown:
        raise SchemaError("unknown_field", path, "Unknown fields: " + ", ".join(unknown))
    if missing:
        raise SchemaError("missing_field", path, "Missing fields: " + ", ".join(missing))
    return value


def vector(value: Any, path: str, dimension: int | None = None) -> tuple[Fraction, ...]:
    if not isinstance(value, list):
        raise SchemaError("array", path, "Expected an array.")
    if dimension is not None and len(value) != dimension:
        raise SchemaError("dimension", path, f"Expected {dimension} entries; got {len(value)}.")
    return tuple(rational(entry, f"{path}[{index}]") for index, entry in enumerate(value))


def parse_document(document: Any) -> tuple[Problem, Certificate]:
    root = object_fields(document, {"version", "problem", "certificate"}, "$")
    if type(root["version"]) is not int or root["version"] != 1:
        raise SchemaError("version", "$.version", "Expected integer schema version 1.")
    raw_problem = object_fields(root["problem"], {"objective", "constraints"}, "$.problem")
    raw_objective = object_fields(
        raw_problem["objective"], {"sense", "coefficients"}, "$.problem.objective"
    )
    sense = raw_objective["sense"]
    if type(sense) is not str or sense not in ("max", "min"):
        raise SchemaError("sense", "$.problem.objective.sense", "Expected max or min.")
    original_objective = vector(raw_objective["coefficients"], "$.problem.objective.coefficients")
    objective = original_objective if sense == "max" else tuple(-v for v in original_objective)
    raw_rows = raw_problem["constraints"]
    if not isinstance(raw_rows, list):
        raise SchemaError("array", "$.problem.constraints", "Expected an array.")
    inequalities, equalities = [], []
    for index, raw_row in enumerate(raw_rows):
        path = f"$.problem.constraints[{index}]"
        raw_row = object_fields(raw_row, {"coefficients", "sense", "rhs"}, path)
        row_sense = raw_row["sense"]
        if type(row_sense) is not str or row_sense not in ("<=", ">=", "="):
            raise SchemaError("sense", path + ".sense", "Expected <=, >=, or =.")
        coefficients = vector(raw_row["coefficients"], path + ".coefficients", len(objective))
        rhs = rational(raw_row["rhs"], path + ".rhs")
        if row_sense == ">=":
            coefficients, rhs = tuple(-v for v in coefficients), -rhs
        row = Row(coefficients, rhs, index)
        (equalities if row_sense == "=" else inequalities).append(row)
    problem = Problem(objective, original_objective, sense, tuple(inequalities), tuple(equalities))

    raw_certificate = root["certificate"]
    if not isinstance(raw_certificate, dict):
        raise SchemaError("object", "$.certificate", "Expected an object.")
    kind = raw_certificate.get("kind")
    if type(kind) is not str or kind not in ("optimal", "infeasible", "unbounded"):
        raise SchemaError("kind", "$.certificate.kind", "Expected optimal, infeasible, or unbounded.")
    fields = {"kind"}
    if kind in ("optimal", "infeasible"):
        fields |= {"inequality_multipliers", "equality_multipliers"}
    if kind == "optimal":
        fields.add("point")
    if kind == "unbounded":
        fields |= {"base_point", "direction"}
    raw_certificate = object_fields(raw_certificate, fields, "$.certificate")
    point = direction = inequality_multipliers = equality_multipliers = ()
    if kind in ("optimal", "unbounded"):
        point_field = "point" if kind == "optimal" else "base_point"
        point = vector(raw_certificate[point_field], "$.certificate." + point_field, problem.dimension)
    if kind == "unbounded":
        direction = vector(raw_certificate["direction"], "$.certificate.direction", problem.dimension)
    else:
        inequality_multipliers = vector(
            raw_certificate["inequality_multipliers"], "$.certificate.inequality_multipliers",
            len(problem.inequalities),
        )
        equality_multipliers = vector(
            raw_certificate["equality_multipliers"], "$.certificate.equality_multipliers",
            len(problem.equalities),
        )
    return problem, Certificate(kind, point, direction, inequality_multipliers, equality_multipliers)


def dot(left: Sequence[Fraction], right: Sequence[Fraction]) -> Fraction:
    # Dimensions are checked at the parsing boundary; retain a guard for API use.
    if len(left) != len(right):
        raise ValueError("Internal dot product dimension mismatch")
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def fraction_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def verify(document: Any) -> dict[str, Any]:
    """Return accepted / rejected / invalid, with exact, deterministic check evidence."""
    try:
        problem, certificate = parse_document(document)
    except SchemaError as exc:
        return {"status": "invalid", "accepted": False, "diagnostics": [exc.diagnostic()]}
    checks: list[dict[str, Any]] = []

    def check(code: str, path: str, lhs: Fraction, relation: str, rhs: Fraction) -> None:
        passed = {"<=": lhs <= rhs, "=": lhs == rhs, ">=": lhs >= rhs,
                  "<": lhs < rhs, ">": lhs > rhs}[relation]
        checks.append({"code": code, "path": path, "lhs": fraction_string(lhs),
                       "relation": relation, "rhs": fraction_string(rhs), "passed": passed})

    if certificate.kind in ("optimal", "unbounded"):
        point_path = "$.certificate.point" if certificate.kind == "optimal" else "$.certificate.base_point"
        for row in problem.inequalities:
            check("point_feasibility", f"{point_path}/row[{row.source_index}]",
                  dot(row.coefficients, certificate.point), "<=", row.rhs)
        for row in problem.equalities:
            check("point_feasibility", f"{point_path}/row[{row.source_index}]",
                  dot(row.coefficients, certificate.point), "=", row.rhs)

    if certificate.kind in ("optimal", "infeasible"):
        for index, multiplier in enumerate(certificate.inequality_multipliers):
            check("multiplier_nonnegative", f"$.certificate.inequality_multipliers[{index}]",
                  multiplier, ">=", Fraction(0))
        weighted_rows = list(zip(certificate.inequality_multipliers, problem.inequalities))
        weighted_rows += list(zip(certificate.equality_multipliers, problem.equalities))
        combined_coefficients = tuple(
            sum((multiplier * row.coefficients[index] for multiplier, row in weighted_rows), Fraction(0))
            for index in range(problem.dimension)
        )
        combined_rhs = sum((multiplier * row.rhs for multiplier, row in weighted_rows), Fraction(0))
        target = problem.objective if certificate.kind == "optimal" else (Fraction(0),) * problem.dimension
        for index, coefficient in enumerate(combined_coefficients):
            check("coefficient_identity", f"combination.coefficients[{index}]", coefficient, "=", target[index])
        if certificate.kind == "optimal":
            check("bound_attained", "combination.rhs", combined_rhs, "=", dot(problem.objective, certificate.point))
        else:
            check("contradiction", "combination.rhs", combined_rhs, "<", Fraction(0))
    else:
        for row in problem.inequalities:
            check("recession_direction", f"$.certificate.direction/row[{row.source_index}]",
                  dot(row.coefficients, certificate.direction), "<=", Fraction(0))
        for row in problem.equalities:
            check("recession_direction", f"$.certificate.direction/row[{row.source_index}]",
                  dot(row.coefficients, certificate.direction), "=", Fraction(0))
        check("strict_improvement", "normalized_objective.direction",
              dot(problem.objective, certificate.direction), ">", Fraction(0))

    accepted = all(entry["passed"] for entry in checks)
    result: dict[str, Any] = {
        "status": "accepted" if accepted else "rejected", "accepted": accepted,
        "kind": certificate.kind, "dimension": problem.dimension,
        "objective_sense": problem.sense,
        "inequality_rows": len(problem.inequalities), "equality_rows": len(problem.equalities),
        "checks": checks,
        "diagnostics": [dict(entry) for entry in checks if not entry["passed"]],
    }
    if certificate.kind == "optimal" and accepted:
        result["certified_objective_value"] = fraction_string(dot(problem.original_objective, certificate.point))
    return result


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, entry in pairs:
        if key in value:
            raise SchemaError("duplicate_key", "$", "Duplicate JSON object key: " + key)
        value[key] = entry
    return value


def _forbid_constant(value: str) -> None:
    raise SchemaError("json_constant", "$", "Nonstandard JSON constant is forbidden: " + value)


def verify_json(text: str) -> dict[str, Any]:
    """Parse strict JSON, preserving integers and rejecting duplicate object keys."""
    try:
        document = json.loads(text, object_pairs_hook=_unique_object, parse_constant=_forbid_constant)
    except SchemaError as exc:
        return {"status": "invalid", "accepted": False, "diagnostics": [exc.diagnostic()]}
    except (json.JSONDecodeError, ValueError, RecursionError) as exc:
        return {"status": "invalid", "accepted": False,
                "diagnostics": [{"code": "json", "path": "$", "message": str(exc)}]}
    return verify(document)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", help="v1 JSON document path, or - for standard input")
    args = parser.parse_args(argv)
    try:
        source = sys.stdin.read() if args.document == "-" else Path(args.document).read_text(encoding="utf-8")
        result = verify_json(source)
    except (OSError, UnicodeError) as exc:
        result = {"status": "invalid", "accepted": False,
                  "diagnostics": [{"code": "io", "path": args.document, "message": str(exc)}]}
    print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    return {"accepted": 0, "rejected": 1, "invalid": 2}[result["status"]]


if __name__ == "__main__":
    raise SystemExit(main())
