#!/usr/bin/env python3
"""Fixture-only exact-rational sparse-certificate experiment.

This is independent research code, not an LP solver, input parser, or export
bridge. It uses no code from lp-certificates and makes no general LP status
classification. Run this file to reproduce results.json on standard output.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations
import json
from typing import Iterable, Sequence


Vector = tuple[Q, ...]


def vector(values: Iterable[int | str | Q]) -> Vector:
    return tuple(Q(value) for value in values)


def dot(left: Sequence[Q], right: Sequence[Q]) -> Q:
    if len(left) != len(right):
        raise ValueError("dimension mismatch")
    return sum((a * b for a, b in zip(left, right)), Q(0))


def rref(matrix: Sequence[Sequence[Q]], coefficient_columns: int):
    """Eliminate only coefficient columns; return rows and pivot columns."""
    rows = [list(map(Q, row)) for row in matrix]
    if any(len(row) < coefficient_columns for row in rows):
        raise ValueError("short matrix row")
    if rows and any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("ragged matrix")
    pivots: list[int] = []
    for column in range(coefficient_columns):
        next_row = len(pivots)
        pivot_row = next((i for i in range(next_row, len(rows))
                          if rows[i][column]), None)
        if pivot_row is None:
            continue
        rows[next_row], rows[pivot_row] = rows[pivot_row], rows[next_row]
        divisor = rows[next_row][column]
        rows[next_row] = [entry / divisor for entry in rows[next_row]]
        for i, row in enumerate(rows):
            if i != next_row and row[column]:
                multiple = row[column]
                rows[i] = [entry - multiple * pivot
                           for entry, pivot in zip(row, rows[next_row])]
        pivots.append(column)
    return rows, pivots


def column_rank(columns: Sequence[Vector], dimension: int) -> int:
    if any(len(column) != dimension for column in columns):
        raise ValueError("column dimension mismatch")
    rows = [[column[i] for column in columns] for i in range(dimension)]
    return len(rref(rows, len(columns))[1])


def independent_solution(columns: Sequence[Vector], target: Vector) -> Vector | None:
    """Unique solution for independent columns, or None if inconsistent.

    Dependent columns raise ValueError. No arbitrary free-zero solution is used.
    The caller separately counts rank tests and independent solves.
    """
    if any(len(column) != len(target) for column in columns):
        raise ValueError("column dimension mismatch")
    rows = [[column[i] for column in columns] + [target[i]]
            for i in range(len(target))]
    reduced, pivots = rref(rows, len(columns))
    if len(pivots) != len(columns):
        raise ValueError("columns are dependent")
    if any(all(entry == 0 for entry in row[:-1]) and row[-1] != 0
           for row in reduced):
        return None
    # Every variable is a pivot variable: this is a unique solution.
    return tuple(reduced[i][-1] for i in range(len(columns)))


@dataclass(frozen=True)
class OriginalSpace:
    """Supplied exact affine parametrization, independently checked below."""
    x0: Vector
    null_columns: tuple[Vector, ...]
    equality_rows: tuple[Vector, ...]
    equality_rhs: Vector
    inequality_rows: tuple[Vector, ...]
    inequality_rhs: Vector
    objective: Vector | None = None
    bound: Q | None = None


@dataclass(frozen=True)
class Fixture:
    name: str
    kind: str
    normals: tuple[Vector, ...]
    budgets: Vector
    objective: Vector | None = None
    bound: Q | None = None
    feasible_witness: Vector | None = None
    original: OriginalSpace | None = None
    note: str = ""
    expected_min_support: int | None = None

    @property
    def dimension(self) -> int:
        return len(self.normals[0]) if self.normals else len(self.objective or ())


def bound_fixture(name, normals, budgets, objective, bound, witness, **kwargs):
    return Fixture(name, "bound", tuple(map(vector, normals)), vector(budgets),
                   vector(objective), Q(bound), vector(witness), **kwargs)


def contradiction_fixture(name, normals, budgets, **kwargs):
    return Fixture(name, "contradiction", tuple(map(vector, normals)),
                   vector(budgets), **kwargs)


def reduced_fixture(name: str, original: OriginalSpace, kind: str,
                    witness: Vector | None = None, **kwargs) -> Fixture:
    normals = tuple(tuple(dot(row, column) for column in original.null_columns)
                    for row in original.inequality_rows)
    budgets = tuple(rhs - dot(row, original.x0)
                    for row, rhs in zip(original.inequality_rows,
                                        original.inequality_rhs))
    objective = None if original.objective is None else tuple(
        dot(original.objective, column) for column in original.null_columns)
    bound = None if original.bound is None else (
        original.bound - dot(original.objective, original.x0))
    return Fixture(name, kind, normals, budgets, objective, bound, witness,
                   original, **kwargs)


def fixtures() -> tuple[Fixture, ...]:
    identity3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    late_rows = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0],
                 [0, 0, 1], [0, 0, -1], [1, 1, 1]]
    late_rhs = [1, 1, 1, 1, 1, 1, 3]
    equality_bound = OriginalSpace(
        vector([1, 0, 2]), (vector([-1, 1, 0]),),
        (vector([1, 1, 0]), vector([0, 0, 1])), vector([1, 2]),
        (vector([1, 0, 0]), vector([0, -1, 0]), vector([0, 1, 0]),
         vector([2, -1, 0])), vector(["4/3", "1/2", "2/3", 3]),
        vector([1, 2, 1]), Q("11/3"))
    equality_contradiction = OriginalSpace(
        vector([1, 0]), (vector([0, 1]),),
        (vector([1, 0]),), vector([1]),
        (vector([1, 0]),), vector([0]))
    return (
        bound_fixture("sharp-normal-support-k", identity3, [1, 1, 1],
                      [1, 1, 1], 3, [0, 0, 0], expected_min_support=3,
                      note="All three normal coordinates require a positive weight."),
        bound_fixture("loose-budget-vertical", [[1, 0], [0, 1]], [1, 1],
                      [1, 1], 3, [0, 0], expected_min_support=2,
                      note="Augmented equality needs the vertical residual of 1."),
        bound_fixture("duplicates-dependent-normals",
                      [[1, 0], [2, 0], [0, 1], [1, 1], [1, 0]],
                      [2, 4, 3, 5, 2], [1, 1], 5, [0, 0],
                      expected_min_support=1,
                      note="Duplicates and a dependent combined row remain in the input."),
        bound_fixture("cheaper-redundant-row", [[1, 0], [2, 0], [0, 1]],
                      [10, 2, 3], [1, 0], 1, [0, 0],
                      expected_min_support=1,
                      note="The first normal is sufficient for representation but too costly."),
        reduced_fixture("rational-equality-reduction", equality_bound, "bound",
                        vector([0]), expected_min_support=1,
                        note="Ambient dimension 3 reduces to affine dimension 1."),
        bound_fixture("zero-objective-positive-budget", [[1], [-1]], [2, 2],
                      [0], 1, [0], expected_min_support=0,
                      note="The empty direct support certifies 0 <= 1."),
        bound_fixture("zero-objective-zero-budget", [[1], [-1]], [2, 2],
                      [0], 0, [0], expected_min_support=0,
                      note="The empty support solves both target formulations."),
        bound_fixture("late-singleton-row-order", late_rows, late_rhs,
                      [1, 1, 1], 3, [0, 0, 0], expected_min_support=1,
                      note="The useful singleton appears last."),
        bound_fixture("early-singleton-row-order", list(reversed(late_rows)),
                      list(reversed(late_rhs)), [1, 1, 1], 3, [0, 0, 0],
                      expected_min_support=1,
                      note="The same rows reordered put the useful singleton first."),
        contradiction_fixture("sharp-contradiction-support-k-plus-one",
                              identity3 + [[-1, -1, -1]], [0, 0, 0, -1],
                              expected_min_support=4,
                              note="The four-row positive circuit cannot omit any row."),
        reduced_fixture("zero-projected-row-contradiction", equality_contradiction,
                        "contradiction", expected_min_support=1,
                        note="The equality makes x1 <= 0 project to 0 <= -1."),
        contradiction_fixture("rational-contradiction", [["2/3"], ["-3/5"]],
                              ["1/2", -1], expected_min_support=2,
                              note="Unique normalized weights are 18/11 and 20/11."),
        contradiction_fixture("duplicate-contradiction", [[1], [2], [-1]],
                              [1, 2, -2], expected_min_support=2,
                              note="The scaled duplicate creates a rank rejection."),
    )


def validate_fixture(fixture: Fixture) -> None:
    k = fixture.dimension
    assert len(fixture.normals) == len(fixture.budgets)
    assert all(len(row) == k for row in fixture.normals)
    if fixture.kind == "bound":
        assert fixture.objective is not None and len(fixture.objective) == k
        assert fixture.bound is not None
        assert fixture.feasible_witness is not None
        assert len(fixture.feasible_witness) == k
        assert all(dot(row, fixture.feasible_witness) <= rhs
                   for row, rhs in zip(fixture.normals, fixture.budgets))
    else:
        assert fixture.kind == "contradiction"
    original = fixture.original
    if original is None:
        return
    n = len(original.x0)
    assert all(len(row) == n for row in original.equality_rows)
    assert all(len(row) == n for row in original.inequality_rows)
    assert len(original.equality_rows) == len(original.equality_rhs)
    assert len(original.inequality_rows) == len(original.inequality_rhs)
    assert all(dot(row, original.x0) == rhs
               for row, rhs in zip(original.equality_rows, original.equality_rhs))
    assert all(dot(row, column) == 0 for row in original.equality_rows
               for column in original.null_columns)
    assert column_rank(original.null_columns, n) == k
    equality_rank = column_rank(original.equality_rows, n)
    assert equality_rank + k == n  # N spans the full nullspace.
    assert equality_rank == len(original.equality_rows)
    if fixture.kind == "bound":
        point = tuple(original.x0[j] + sum(
            (column[j] * weight for column, weight in
             zip(original.null_columns, fixture.feasible_witness)), Q(0))
                      for j in range(n))
        assert all(dot(row, point) <= rhs
                   for row, rhs in zip(original.inequality_rows, original.inequality_rhs))


def verify_weights(fixture: Fixture, weights: Vector) -> bool:
    if len(weights) != len(fixture.normals) or any(weight < 0 for weight in weights):
        return False
    combined = tuple(sum((weight * row[j] for weight, row in
                          zip(weights, fixture.normals)), Q(0))
                     for j in range(fixture.dimension))
    cost = dot(weights, fixture.budgets)
    if fixture.kind == "bound":
        return combined == fixture.objective and cost <= fixture.bound
    return combined == (Q(0),) * fixture.dimension and cost == -1


def original_identity(fixture: Fixture, weights: Vector):
    """Check and reconstruct equality weights only for the supplied examples."""
    original = fixture.original
    if original is None:
        return None
    combined = tuple(sum((weight * row[j] for weight, row in
                          zip(weights, original.inequality_rows)), Q(0))
                     for j in range(len(original.x0)))
    target = original.objective if fixture.kind == "bound" else (Q(0),) * len(combined)
    residual = tuple(a - b for a, b in zip(target, combined))
    equality_weights = independent_solution(original.equality_rows, residual)
    assert equality_weights is not None
    cost = dot(weights, original.inequality_rhs) + dot(
        equality_weights, original.equality_rhs)
    if fixture.kind == "bound":
        assert cost <= original.bound
    else:
        assert cost == -1
    return {"equality_weights": list(map(str, equality_weights)),
            "original_combination_rhs": str(cost), "identity_checked": True}


def search(fixture: Fixture, strategy: str, stop_at_first: bool):
    """Enumerate supplied fixture supports by size, then input index order."""
    validate_fixture(fixture)
    m, k = len(fixture.normals), fixture.dimension
    if strategy == "direct":
        if fixture.kind != "bound":
            raise ValueError("direct strategy is only used for feasible bound fixtures")
        columns = fixture.normals
        target = fixture.objective
    elif strategy == "augmented":
        columns = tuple(row + (rhs,) for row, rhs in
                        zip(fixture.normals, fixture.budgets))
        if fixture.kind == "bound":
            columns += ((Q(0),) * k + (Q(1),),)
            target = fixture.objective + (fixture.bound,)
        else:
            target = (Q(0),) * k + (Q(-1),)
    else:
        raise ValueError("unknown transparent search choice")
    maximum_support = column_rank(columns, len(target))
    counts = {"subsets_attempted": 0, "rank_tests": 0,
              "dependent_subsets_rejected": 0, "independent_solves": 0,
              "inconsistent_independent_systems": 0,
              "negative_solutions_rejected": 0, "budget_rejections": 0,
              "certificates_checked": 0}
    first = None
    minimum_support = None
    for size in range(maximum_support + 1):
        for support in combinations(range(len(columns)), size):
            counts["subsets_attempted"] += 1
            selected = tuple(columns[i] for i in support)
            counts["rank_tests"] += 1
            if column_rank(selected, len(target)) != size:
                counts["dependent_subsets_rejected"] += 1
                continue
            counts["independent_solves"] += 1
            solution = independent_solution(selected, target)
            if solution is None:
                counts["inconsistent_independent_systems"] += 1
                continue
            if any(weight < 0 for weight in solution):
                counts["negative_solutions_rejected"] += 1
                continue
            weights = [Q(0)] * m
            vertical = Q(0)
            for index, weight in zip(support, solution):
                if index < m:
                    weights[index] = weight
                else:
                    vertical = weight
            weights = tuple(weights)
            if strategy == "direct" and dot(weights, fixture.budgets) > fixture.bound:
                counts["budget_rejections"] += 1
                continue
            assert verify_weights(fixture, weights)
            if strategy == "augmented" and fixture.kind == "bound":
                assert dot(weights, fixture.budgets) + vertical == fixture.bound
            counts["certificates_checked"] += 1
            actual_support = sum(weight > 0 for weight in weights)
            if minimum_support is None or actual_support < minimum_support:
                minimum_support = actual_support
            if first is None:
                first = {
                    "enumerated_indices": list(support),
                    "inequality_weights": list(map(str, weights)),
                    "positive_inequality_support": actual_support,
                    "vertical_residual_weight": str(vertical),
                    "combination_rhs": str(dot(weights, fixture.budgets)),
                    "first_success_subsets_attempted": counts["subsets_attempted"],
                    "first_success_independent_solves": counts["independent_solves"],
                    "original_identity": original_identity(fixture, weights),
                }
            if stop_at_first:
                break
        if first is not None and stop_at_first:
            break
    return {
        "strategy": strategy,
        "mode": "first_success" if stop_at_first else "exhaustive",
        "column_count": len(columns), "column_rank": maximum_support,
        "maximum_enumerated_support": maximum_support,
        "candidate_found": first is not None,
        "minimum_positive_inequality_support_observed": minimum_support,
        "first_certificate": first, "counts": counts,
    }


def fixture_data(fixture: Fixture):
    data = {"name": fixture.name, "kind": fixture.kind,
            "dimension": fixture.dimension,
            "normals": [list(map(str, row)) for row in fixture.normals],
            "budgets": list(map(str, fixture.budgets)), "note": fixture.note,
            "expected_minimum_inequality_support": fixture.expected_min_support}
    if fixture.kind == "bound":
        data.update(objective=list(map(str, fixture.objective)), bound=str(fixture.bound),
                    feasible_witness=list(map(str, fixture.feasible_witness)),
                    feasible_witness_checked=True)
    if fixture.original is not None:
        original = fixture.original
        data["original_space"] = {
            "x0": list(map(str, original.x0)),
            "null_columns": [list(map(str, row)) for row in original.null_columns],
            "equality_rows": [list(map(str, row)) for row in original.equality_rows],
            "equality_rhs": list(map(str, original.equality_rhs)),
            "inequality_rows": [list(map(str, row)) for row in original.inequality_rows],
            "inequality_rhs": list(map(str, original.inequality_rhs)),
            "objective": None if original.objective is None else list(map(str, original.objective)),
            "bound": None if original.bound is None else str(original.bound),
            "affine_parametrization_checked": True,
        }
    return data


def report():
    entries = []
    for fixture in fixtures():
        strategies = ("direct", "augmented") if fixture.kind == "bound" else ("augmented",)
        runs = [search(fixture, strategy, stop_at_first)
                for strategy in strategies for stop_at_first in (True, False)]
        assert all(run["candidate_found"] for run in runs)
        for run in runs:
            if run["mode"] == "exhaustive":
                assert run["minimum_positive_inequality_support_observed"] == fixture.expected_min_support
        entries.append({"fixture": fixture_data(fixture), "runs": runs})
    return {
        "schema": "lp-sparse-discovery-fixture-benchmark-v1",
        "arithmetic": "Python standard-library fractions.Fraction; no floating point",
        "scope": "Built-in fixtures only; no general LP status classification or formal verification",
        "enumeration_order": "increasing support size, then lexicographic input indices",
        "counts_definition": {
            "subsets_attempted": "includes empty and dependent supports",
            "rank_tests": "one exact rank test per attempted support",
            "independent_solves": "support-search unique-solution RREF calls after full-column-rank check; excludes original equality reconstruction",
            "certificates_checked": "accepted independent-support candidates, including duplicate representations",
        },
        "fixtures": entries,
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
