#!/usr/bin/env python3
"""Incomplete, deterministic exact certificate search for hand-size rational LPs.

Search limits: at most three variables and eight constraint rows. Candidate
points are intersections of constraint and coordinate-zero hyperplanes;
multiplier candidates solve small-support rational systems; directions come
from the integer grid [-2, 2]^n. Unknown means only that this search found no
certificate. Every emitted certificate is accepted by verifier.py first.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path
import sys
from typing import Any, Sequence

import verifier


MAX_VARIABLES = 3
MAX_ROWS = 8
DIRECTION_INTEGER_BOUND = 2


def solve_linear_system(
    coefficients: Sequence[Sequence[Fraction]],
    rhs: Sequence[Fraction],
    variables: int,
) -> tuple[Fraction, ...] | None:
    """Rational RREF particular solution with free coordinates set to zero.

    Return None for an inconsistent system. This helper does not optimize,
    choose signs, or characterize all solutions of an underdetermined system.
    """
    if len(coefficients) != len(rhs) or any(len(row) != variables for row in coefficients):
        raise ValueError("Linear system dimension mismatch")
    rows = [[Fraction(value) for value in row] + [Fraction(value)]
            for row, value in zip(coefficients, rhs)]
    pivots: list[tuple[int, int]] = []
    next_row = 0
    for column in range(variables):
        pivot = next((index for index in range(next_row, len(rows)) if rows[index][column]), None)
        if pivot is None:
            continue
        rows[next_row], rows[pivot] = rows[pivot], rows[next_row]
        divisor = rows[next_row][column]
        rows[next_row] = [value / divisor for value in rows[next_row]]
        for index in range(len(rows)):
            if index != next_row and rows[index][column]:
                factor = rows[index][column]
                rows[index] = [value - factor * pivot_value
                               for value, pivot_value in zip(rows[index], rows[next_row])]
        pivots.append((next_row, column))
        next_row += 1
        if next_row == len(rows):
            break
    if any(all(value == 0 for value in row[:variables]) and row[-1] != 0 for row in rows):
        return None
    solution = [Fraction(0)] * variables
    for row_index, column in pivots:
        solution[column] = rows[row_index][-1]
    return tuple(solution)


def _parse_problem(document: Any) -> verifier.Problem:
    # Delegate rational, row-sense, dimension, and nested-field validation to
    # exactly the verifier's parser; the dummy witness is never accepted/emitted.
    root = verifier.object_fields(document, {"version", "problem"}, "$")
    raw_problem = root["problem"]
    raw_rows = raw_problem.get("constraints", []) if isinstance(raw_problem, dict) else []
    raw_rows = raw_rows if isinstance(raw_rows, list) else []
    inequalities = sum(isinstance(row, dict) and row.get("sense") in ("<=", ">=") for row in raw_rows)
    equalities = sum(isinstance(row, dict) and row.get("sense") == "=" for row in raw_rows)
    augmented = {"version": root["version"], "problem": raw_problem, "certificate": {
        "kind": "infeasible", "inequality_multipliers": [0] * inequalities,
        "equality_multipliers": [0] * equalities,
    }}
    return verifier.parse_document(augmented)[0]


def _is_feasible(problem: verifier.Problem, point: Sequence[Fraction]) -> bool:
    return (all(verifier.dot(row.coefficients, point) <= row.rhs for row in problem.inequalities)
            and all(verifier.dot(row.coefficients, point) == row.rhs for row in problem.equalities))


def _feasible_points(problem: verifier.Problem, counts: dict[str, int]) -> list[tuple[Fraction, ...]]:
    rows = list(problem.inequalities) + list(problem.equalities)
    equations = [(row.coefficients, row.rhs) for row in rows]
    equations += [(tuple(Fraction(int(index == column)) for index in range(problem.dimension)), Fraction(0))
                  for column in range(problem.dimension)]
    points: list[tuple[Fraction, ...]] = []
    seen: set[tuple[Fraction, ...]] = set()
    for chosen in combinations(equations, problem.dimension):
        counts["linear_systems"] += 1
        point = solve_linear_system([row for row, _ in chosen], [rhs for _, rhs in chosen], problem.dimension)
        if point is not None and point not in seen:
            seen.add(point)
            counts["point_candidates"] += 1
            if _is_feasible(problem, point):
                points.append(point)
    counts["feasible_points"] = len(points)
    # Highest normalized objective first; stable ordering resolves ties.
    points.sort(key=lambda point: verifier.dot(problem.objective, point), reverse=True)
    return points


def _multiplier_candidates(
    problem: verifier.Problem,
    target: tuple[Fraction, ...],
    counts: dict[str, int],
    point: tuple[Fraction, ...] | None = None,
):
    rows = list(problem.inequalities) + list(problem.equalities)
    inequality_count = len(problem.inequalities)
    eligible = [index for index, row in enumerate(rows)
                if point is None or index >= inequality_count
                or verifier.dot(row.coefficients, point) == row.rhs]
    for support_size in range(min(problem.dimension + 1, len(eligible)) + 1):
        for support in combinations(eligible, support_size):
            columns = [rows[index].coefficients + (rows[index].rhs,) for index in support]
            matrix = [[column[index] for column in columns] for index in range(problem.dimension + 1)]
            counts["linear_systems"] += 1
            solution = solve_linear_system(matrix, target, support_size)
            if solution is None or any(value < 0 for index, value in zip(support, solution)
                                       if index < inequality_count):
                continue
            all_multipliers = [Fraction(0)] * len(rows)
            for index, value in zip(support, solution):
                all_multipliers[index] = value
            yield (tuple(all_multipliers[:inequality_count]), tuple(all_multipliers[inequality_count:]))


def _strings(vector: Sequence[Fraction]) -> list[str]:
    return [verifier.fraction_string(value) for value in vector]


def _limits() -> dict[str, Any]:
    return {"max_variables": MAX_VARIABLES, "max_rows": MAX_ROWS,
            "direction_integer_bound": DIRECTION_INTEGER_BOUND,
            "multiplier_support_bound": "number of variables + 1",
            "point_search": "constraint/coordinate-zero hyperplane intersections"}


def _find(document: Any) -> dict[str, Any]:
    limits = _limits()
    common: dict[str, Any] = {"incomplete": True, "limits": limits}
    try:
        problem = _parse_problem(document)
    except verifier.SchemaError as exc:
        return {**common, "status": "invalid", "diagnostics": [exc.diagnostic()]}
    if problem.dimension > MAX_VARIABLES or len(problem.inequalities) + len(problem.equalities) > MAX_ROWS:
        return {**common, "status": "unknown", "reason": "search_limits_exceeded"}

    counts = {"linear_systems": 0, "point_candidates": 0, "feasible_points": 0,
              "direction_candidates": 0, "certificates_checked": 0}

    def accepted(certificate: dict[str, Any]) -> dict[str, Any] | None:
        full_document = {"version": 1, "problem": copy.deepcopy(document["problem"]),
                         "certificate": certificate}
        counts["certificates_checked"] += 1
        verification = verifier.verify(full_document)
        if not verification["accepted"]:
            return None
        return {**common, "status": "found", "certificate_kind": certificate["kind"],
                "certificate_document": full_document, "verification": verification, "search_counts": dict(counts)}

    contradiction_target = (Fraction(0),) * problem.dimension + (Fraction(-1),)
    for inequalities, equalities in _multiplier_candidates(problem, contradiction_target, counts):
        result = accepted({"kind": "infeasible", "inequality_multipliers": _strings(inequalities),
                           "equality_multipliers": _strings(equalities)})
        if result is not None:
            return result

    points = _feasible_points(problem, counts)
    for point in points:
        target = problem.objective + (verifier.dot(problem.objective, point),)
        for inequalities, equalities in _multiplier_candidates(problem, target, counts, point):
            result = accepted({"kind": "optimal", "point": _strings(point),
                               "inequality_multipliers": _strings(inequalities),
                               "equality_multipliers": _strings(equalities)})
            if result is not None:
                return result

    if points:
        values = range(-DIRECTION_INTEGER_BOUND, DIRECTION_INTEGER_BOUND + 1)
        for entries in product(values, repeat=problem.dimension):
            direction = tuple(Fraction(value) for value in entries)
            counts["direction_candidates"] += 1
            if (verifier.dot(problem.objective, direction) <= 0
                    or any(verifier.dot(row.coefficients, direction) > 0 for row in problem.inequalities)
                    or any(verifier.dot(row.coefficients, direction) != 0 for row in problem.equalities)):
                continue
            result = accepted({"kind": "unbounded", "base_point": _strings(points[0]),
                               "direction": _strings(direction)})
            if result is not None:
                return result
    return {**common, "status": "unknown", "reason": "no_certificate_in_bounded_search",
            "search_counts": counts}


def find(document: Any) -> dict[str, Any]:
    """Find one checked witness or return unknown; make no completeness claim."""
    try:
        return _find(document)
    except (verifier.SchemaError, ValueError, OverflowError):
        # Input schema errors were handled at the parsing boundary in _find.
        # Computed rational growth may exceed the verifier/host's output budget.
        # This is a search failure and must never become an LP status claim.
        return {"status": "unknown", "incomplete": True, "limits": _limits(),
                "reason": "search_arithmetic_limit", "diagnostics": [{
                    "code": "search_arithmetic_limit", "path": "search",
                    "message": "A computed rational exceeded the search's formatting or arithmetic budget."}]}


def find_json(text: str) -> dict[str, Any]:
    try:
        document = json.loads(text, object_pairs_hook=verifier._unique_object,
                              parse_constant=verifier._forbid_constant)
    except verifier.SchemaError as exc:
        return {"status": "invalid", "incomplete": True, "diagnostics": [exc.diagnostic()]}
    except (json.JSONDecodeError, ValueError, RecursionError) as exc:
        return {"status": "invalid", "incomplete": True,
                "diagnostics": [{"code": "json", "path": "$", "message": str(exc)}]}
    return find(document)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", help="problem-only v1 JSON document path, or - for standard input")
    args = parser.parse_args(argv)
    try:
        source = sys.stdin.read() if args.document == "-" else Path(args.document).read_text(encoding="utf-8")
        result = find_json(source)
    except (OSError, UnicodeError) as exc:
        result = {"status": "invalid", "incomplete": True,
                  "diagnostics": [{"code": "io", "path": args.document, "message": str(exc)}]}
    print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    return {"found": 0, "unknown": 1, "invalid": 2}[result["status"]]


if __name__ == "__main__":
    raise SystemExit(main())
