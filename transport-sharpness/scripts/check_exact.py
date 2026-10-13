#!/usr/bin/env python3
"""Exact finite transport certificates, affine-cell geometry, and regressions.

Changed and expanded from the prior transport-stability/check_exact_cases.py:
all cell comparisons now come from slopes/intercepts; parameters are independent;
finite primal/dual certificates replace LP enumeration as the primary optimality
check; and rational-power counterexample witnesses avoid floating-point roots.

Only Python's standard library is used. Geometric and certificate calculations
use fractions.Fraction, never floating point. This is executable arithmetic
evidence, not a Lean proof or a parameter-uniform real-analysis theorem.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
import json
from math import lcm
from pathlib import Path
from typing import Iterable, Sequence


Point = tuple[F, F]
Plane = tuple[F, F, F]
Matrix = list[list[F]]
SQUARE: list[Point] = [(F(-1), F(-1)), (F(1), F(-1)),
                       (F(1), F(1)), (F(-1), F(1))]
DENSITY = F(1, 4)
BASELINE = "b1d6c20e2f02b484d09c5285e67d842b369f9df0"


def require(condition: bool, message: str) -> None:
    """Retain every check even when Python is invoked with -O."""
    if not condition:
        raise ValueError(message)


def as_fraction(value: F | int | str) -> F:
    require(not isinstance(value, float), "floating-point input is forbidden")
    return F(value)


def validate_parameters(a: F | int | str, b: F | int | str) -> tuple[F, F]:
    a, b = as_fraction(a), as_fraction(b)
    require(F(0) < b < a and a + b < 1,
            "the unclipped family requires 0 < b < a and a + b < 1")
    return a, b


@dataclass(frozen=True)
class Affine:
    slope: Point
    intercept: F

    def comparison(self, other: Affine) -> Plane:
        """Coefficients of self(x,t) - other(x,t) >= 0."""
        return (self.slope[0] - other.slope[0],
                self.slope[1] - other.slope[1],
                self.intercept - other.intercept)


def potentials(a: F, b: F) -> tuple[list[Affine], list[Affine]]:
    """Order slopes as minus, central, plus; tie order has zero-area effect."""
    u = [Affine((F(-1), F(0)), F(0)),
         Affine((F(0), F(0)), a),
         Affine((F(1), F(0)), F(0))]
    v = [Affine((F(-1), F(0)), F(0)),
         Affine((F(0), b), a),
         Affine((F(1), F(0)), F(0))]
    return u, v


def derive_cells(pieces: Sequence[Affine]) -> list[list[Plane]]:
    require(bool(pieces), "an affine maximum must be nonempty")
    require(len({piece.slope for piece in pieces}) == len(pieces),
            "distinct slopes are required for zero-area tie boundaries")
    return [[piece.comparison(other) for j, other in enumerate(pieces) if i != j]
            for i, piece in enumerate(pieces)]


def plane_value(plane: Plane, point: Point) -> F:
    return plane[0] * point[0] + plane[1] * point[1] + plane[2]


def clip_polygon(polygon: Sequence[Point], plane: Plane) -> list[Point]:
    """Sutherland-Hodgman intersection with a closed rational half-plane."""
    polygon = list(polygon)
    if not polygon:
        return []
    result: list[Point] = []
    for start, end in zip(polygon, polygon[1:] + polygon[:1]):
        vs, ve = plane_value(plane, start), plane_value(plane, end)
        if vs >= 0:
            result.append(start)
        if (vs < 0 < ve) or (ve < 0 < vs):
            weight = vs / (vs - ve)
            intersection = (start[0] + weight * (end[0] - start[0]),
                            start[1] + weight * (end[1] - start[1]))
            require(plane_value(plane, intersection) == 0,
                    "computed edge intersection is off the clipping line")
            result.append(intersection)
    # Consecutive duplicates add no area, but removing them makes certificates
    # easier to inspect and handles vertices already on a clipping line.
    deduplicated: list[Point] = []
    for point in result:
        if not deduplicated or point != deduplicated[-1]:
            deduplicated.append(point)
    if len(deduplicated) > 1 and deduplicated[0] == deduplicated[-1]:
        deduplicated.pop()
    return deduplicated


def intersect_polygon(planes: Iterable[Plane]) -> list[Point]:
    planes = list(planes)
    polygon = list(SQUARE)
    for plane in planes:
        polygon = clip_polygon(polygon, plane)
    require(all(plane_value(plane, point) >= 0
                for plane in planes for point in polygon),
            "intersection vertex violates an affine cell comparison")
    return polygon


def polygon_area(polygon: Sequence[Point]) -> F:
    polygon = list(polygon)
    if len(polygon) < 3:
        return F(0)
    doubled = sum((start[0] * end[1] - end[0] * start[1]
                   for start, end in zip(polygon, polygon[1:] + polygon[:1])), F(0))
    return abs(doubled) / 2


def common_source_geometry(a: F, b: F) -> dict:
    """Compute geometry without requiring the unclipped closed-form regime.

    This lower-level entry point is intentionally also used on clipped inputs:
    it computes the actual affine maxima, not the advertised formulas.
    """
    a, b = as_fraction(a), as_fraction(b)
    u, v = potentials(a, b)
    u_cells, v_cells = derive_cells(u), derive_cells(v)
    polygons = [[intersect_polygon(left + right) for right in v_cells]
                for left in u_cells]
    joint = [[DENSITY * polygon_area(polygon) for polygon in row]
             for row in polygons]
    require(DENSITY * polygon_area(SQUARE) == 1,
            "source density must normalize the square to probability one")
    require(sum((sum(row, F(0)) for row in joint), F(0)) == 1,
            "affine intersections do not partition the probability source")
    return {"u_affine_pieces": u, "v_affine_pieces": v,
            "u_cell_halfplanes": u_cells, "v_cell_halfplanes": v_cells,
            "intersection_polygons": polygons,
            "common_source_joint_mass_matrix": joint,
            "u_masses": [sum(row, F(0)) for row in joint],
            "v_masses": [sum(row[j] for row in joint) for j in range(3)]}


def squared_costs(source: Sequence[Point], target: Sequence[Point]) -> Matrix:
    return [[sum(((x - y) ** 2 for x, y in zip(left, right)), F(0))
             for right in target] for left in source]


def verify_coupling(matrix: Sequence[Sequence[F]],
                    row_masses: Sequence[F], column_masses: Sequence[F]) -> None:
    require(len(matrix) == len(row_masses)
            and all(len(row) == len(column_masses) for row in matrix),
            "coupling shape disagrees with its marginals")
    require(all(entry >= 0 for row in matrix for entry in row),
            "coupling has negative mass")
    require([sum(row, F(0)) for row in matrix] == list(row_masses),
            "coupling row marginal is incorrect")
    require([sum(row[j] for row in matrix) for j in range(len(column_masses))]
            == list(column_masses), "coupling column marginal is incorrect")
    require(sum(row_masses, F(0)) == sum(column_masses, F(0)) == 1,
            "transport marginals must both be probability laws")


def matrix_objective(matrix: Sequence[Sequence[F]], costs: Matrix) -> F:
    return sum((matrix[i][j] * costs[i][j]
                for i in range(len(matrix)) for j in range(len(matrix[i]))), F(0))


def verify_primal_dual(costs: Matrix, masses: Sequence[F], primal: Matrix,
                       row_dual: Sequence[F], column_dual: Sequence[F]) -> dict:
    verify_coupling(primal, masses, masses)
    require(len(row_dual) == len(costs)
            and len(column_dual) == len(costs[0]), "dual shape is incorrect")
    slack = [[costs[i][j] - row_dual[i] - column_dual[j]
              for j in range(len(column_dual))] for i in range(len(row_dual))]
    require(all(entry >= 0 for row in slack for entry in row),
            "dual certificate violates a cost inequality")
    primal_value = matrix_objective(primal, costs)
    dual_value = sum((mass * value for mass, value in zip(masses, row_dual)), F(0))
    dual_value += sum((mass * value for mass, value in zip(masses, column_dual)), F(0))
    require(primal_value == dual_value, "primal and dual objectives do not match")
    require(all(primal[i][j] * slack[i][j] == 0
                for i in range(len(primal)) for j in range(len(primal[i]))),
            "primal and dual certificates lack complementary slackness")
    return {"row_dual": list(row_dual), "column_dual": list(column_dual),
            "dual_slack_matrix": slack, "matching_primal": primal,
            "primal_objective": primal_value, "dual_objective": dual_value}


def solve_square(matrix: Sequence[Sequence[F]], rhs: Sequence[F]) -> list[F] | None:
    n = len(rhs)
    rows = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = next((i for i in range(column, n) if rows[i][column]), None)
        if pivot is None:
            return None
        rows[column], rows[pivot] = rows[pivot], rows[column]
        divisor = rows[column][column]
        rows[column] = [value / divisor for value in rows[column]]
        for i in range(n):
            if i != column:
                factor = rows[i][column]
                rows[i] = [value - factor * pivot_value
                           for value, pivot_value in zip(rows[i], rows[column])]
    return [row[-1] for row in rows]


def transport_vertices(masses: Sequence[F]) -> list[tuple[F, ...]]:
    """Extra finite cross-check; optimality does not depend on enumeration."""
    require(len(masses) == 3, "vertex enumeration is scoped to three atoms")
    columns = [tuple(F(i == r) for r in range(3))
               + tuple(F(j == c) for c in range(2))
               for i in range(3) for j in range(3)]
    vertices = set()
    for support in combinations(range(9), 5):
        matrix = [[columns[index][row] for index in support] for row in range(5)]
        solution = solve_square(matrix, list(masses) + list(masses[:2]))
        if solution is None or any(entry < 0 for entry in solution):
            continue
        entries = [F(0)] * 9
        for index, value in zip(support, solution):
            entries[index] = value
        verify_coupling([entries[3*i:3*i+3] for i in range(3)], masses, masses)
        vertices.add(tuple(entries))
    require(bool(vertices), "no feasible transport vertex was enumerated")
    return sorted(vertices)


def check_even_p(a: F, b: F, p: int, costs2: Matrix, masses: list[F],
                 vertices: Sequence[tuple[F, ...]] | None = None) -> dict:
    require(isinstance(p, int) and p >= 2 and p % 2 == 0,
            "exact Euclidean cost matrices require an even integer p >= 2")
    costs = [[entry ** (p // 2) for entry in row] for row in costs2]
    primal = [[masses[i] if i == j else F(0) for j in range(3)] for i in range(3)]
    certificate = verify_primal_dual(costs, masses, primal,
                                     [F(0)] * 3, [F(0), b**p, F(0)])
    require(certificate["primal_objective"] == a * b**p,
            "matching objective disagrees with a b^p")
    slacks = certificate["dual_slack_matrix"]
    require(all((slacks[i][j] == 0) == (i == j)
                for i in range(3) for j in range(3)),
            "dual zero-slack support is not exactly the diagonal")
    certificate.update({"p": p, "cost_matrix": costs,
                        "Wp_to_the_p": a * b**p,
                        "unique_by_positive_off_diagonal_slack": True})
    if vertices is not None:
        objectives = [sum((entry * cost for entry, cost in zip(vertex, sum(costs, []))), F(0))
                      for vertex in vertices]
        minimum = min(objectives)
        minimizers = [vertex for vertex, objective in zip(vertices, objectives)
                      if objective == minimum]
        require(minimum == certificate["primal_objective"],
                "independent vertex minimum disagrees with the certificate")
        require(minimizers == [tuple(sum(primal, []))],
                "vertex enumeration has a different or additional optimizer")
        certificate["vertex_enumeration_minimum"] = minimum
        certificate["minimizing_vertices"] = len(minimizers)
    return certificate


def check_case(a: F | int | str, b: F | int | str,
               even_ps: Sequence[int] = (2, 4, 6, 8),
               enumerate_vertices: bool = True) -> dict:
    a, b = validate_parameters(a, b)
    geometry = common_source_geometry(a, b)
    masses = [(1-a)/2, a, (1-a)/2]
    require(all(mass > 0 for mass in masses), "three atoms must have positive mass")
    require(geometry["u_masses"] == geometry["v_masses"] == masses,
            "computed target laws disagree with m, a, m")
    joint = geometry["common_source_joint_mass_matrix"]
    verify_coupling(joint, masses, masses)
    expected = [[masses[0]-b/8, b/8, F(0)],
                [b/8, a-b/4, b/8], [F(0), b/8, masses[2]-b/8]]
    require(joint == expected, "geometric joint matrix disagrees with the closed form")
    u, v = geometry["u_affine_pieces"], geometry["v_affine_pieces"]
    source, target = [piece.slope for piece in u], [piece.slope for piece in v]
    require(all(abs(coordinate) <= 1 for point in source + target for coordinate in point),
            "target atom is outside the fixed cube")
    for support in (source, target):
        require(all(sum((x-y)**2 for x, y in zip(left, right)) >= 1
                    for left, right in combinations(support, 2)),
                "within-target atom separation fell below one")
    costs2 = squared_costs(source, target)
    map_cost = matrix_objective(joint, costs2)
    require(map_cost == b/2 + a*b*b, "exact map L2 squared formula failed")
    vertices = transport_vertices(masses) if enumerate_vertices else None
    certificates = [check_even_p(a, b, p, costs2, masses, vertices) for p in even_ps]
    # For p=1, arbitrary Euclidean costs can be irrational. This exact check
    # verifies the coordinate lower bound via squared rational distances and
    # checks the diagonal cost ab; its monotonicity interpretation is written
    # ordinary mathematics rather than a rational full-cost LP calculation.
    coordinate_costs = [[abs(left[1]-right[1]) for right in target] for left in source]
    require(all(costs2[i][j] >= coordinate_costs[i][j]**2
                for i in range(3) for j in range(3)),
            "coordinate projection is not a lower bound on Euclidean distance")
    require(coordinate_costs == [[F(0), b, F(0)]] * 3,
            "coordinate lower bound must depend only on the destination")
    require(sum((masses[j] * coordinate_costs[0][j] for j in range(3)), F(0)) == a*b,
            "coordinate W1 lower-bound objective failed")
    return {"a": a, "b": b, "density_on_square": DENSITY,
            "density_lower_bound_on_square": DENSITY,
            "density_upper_bound_globally": DENSITY,
            "central_half_width_range": [a-b, a+b],
            "atom_masses": masses, "source_target_support_mu": source,
            "source_target_support_nu": target, **geometry,
            "quadratic_cost_matrix": costs2,
            "L2_map_difference_squared": map_cost,
            "W1_coordinate_certificate_value": a*b,
            "W2_squared": a*b*b,
            "same_source_cost_over_W2_squared": map_cost/(a*b*b),
            "even_p_certificates": certificates,
            "distinct_vertices_enumerated": len(vertices) if vertices is not None else None,
            "checks_passed": True}


def exponent_power(p: F | int | str, alpha: F | int | str) -> tuple[F, F, int, int, int]:
    p, alpha = as_fraction(p), as_fraction(alpha)
    require(p >= 1 and alpha > 0, "rational exponent check requires p >= 1 and alpha > 0")
    L = lcm((2*alpha/p).denominator, (2*alpha).denominator)
    a_power, b_power = 2*L*alpha/p, 2*L*alpha
    require(a_power.denominator == b_power.denominator == 1,
            "integer clearing power is incorrect")
    return p, alpha, L, int(a_power), int(b_power)


def exact_ratio_power(a: F, b: F, p: F | int | str, alpha: F | int | str) -> dict:
    """Return R^(2L), where R=D/Wp^alpha, without roots or real powers.

    The real Wp identity is an ordinary proof. This routine certifies exact
    rational consequences of that identity, even for nonintegral rational p.
    """
    a, b = validate_parameters(a, b)
    p, alpha, L, a_power, b_power = exponent_power(p, alpha)
    d_squared = b/2 + a*b*b
    numerator, denominator = d_squared**L, a**a_power * b**b_power
    return {"a": a, "b": b, "p": p, "alpha": alpha, "L": L,
            "ratio_power": 2*L, "a_denominator_power": a_power,
            "b_denominator_power": b_power, "numerator": numerator,
            "denominator": denominator, "ratio_to_integer_power": numerator/denominator}


def counterexample_witness(p: F | int | str, alpha: F | int | str,
                           constant: F | int | str, family: str) -> dict:
    """Find an exact dyadic violating D <= C Wp^alpha above its ceiling."""
    p, alpha, L, a_power, b_power = exponent_power(p, alpha)
    constant = as_fraction(constant)
    require(constant > 0, "candidate Holder constant must be positive")
    require(family in ("shrinking_mass", "fixed_mass"), "unknown parameter family")
    ceiling = p/(2*(p+1)) if family == "shrinking_mass" else F(1, 2)
    require(alpha > ceiling, "this family only certifies exponents strictly above its ceiling")
    growth = a_power + b_power - L if family == "shrinking_mass" else b_power - L
    require(growth > 0, "integer-powered asymptotic growth must be positive")
    k = 2 if family == "shrinking_mass" else 3
    while True:
        a = F(1, 2**k) if family == "shrinking_mass" else F(1, 4)
        b = a/2 if family == "shrinking_mass" else F(1, 2**k)
        # D² >= b/2. Clearing the positive integer power keeps order exact.
        lower_bound = (b/2)**L / (a**a_power * b**b_power)
        if lower_bound > constant**(2*L):
            break
        k += 1
    record = exact_ratio_power(a, b, p, alpha)
    require(record["ratio_to_integer_power"] >= lower_bound > constant**(2*L),
            "powered exact counterexample does not exceed the candidate constant")
    # Recompute the geometry even for a witness with very small atom mass.
    geometric = check_case(a, b, even_ps=(2,), enumerate_vertices=False)
    require(geometric["L2_map_difference_squared"] == b/2+a*b*b,
            "counterexample witness failed its actual affine-cell geometry")
    return {"family": family, "ceiling": ceiling, "candidate_constant": constant,
            "dyadic_k": k, "integer_growth_exponent": growth,
            "powered_lower_bound": lower_bound,
            "candidate_constant_powered": constant**(2*L),
            "strict_violation_verified": True, **record}


def negative_regressions() -> list[dict]:
    cases = [("zero_b", F(1,4), F(0)),
             ("negative_b", F(1,4), F(-1,8)),
             ("negative_a", F(-1,4), F(1,8)),
             ("b_equals_a", F(1,4), F(1,4)),
             ("lower_width_clipped", F(1,4), F(1,2)),
             ("upper_width_boundary", F(3,4), F(1,4)),
             ("upper_width_clipped", F(3,4), F(1,2))]
    output = []
    for label, a, b in cases:
        try:
            validate_parameters(a, b)
        except ValueError as error:
            record = {"label": label, "a": a, "b": b,
                      "rejected_as_unclipped_family": True, "reason": str(error)}
        else:
            raise ValueError(f"inadmissible input {label} was accepted")
        if label in ("lower_width_clipped", "upper_width_clipped"):
            geometry = common_source_geometry(a, b)
            record["actual_v_masses_from_clipping"] = geometry["v_masses"]
            record["advertised_unclipped_v_masses"] = [(1-a)/2, a, (1-a)/2]
            require(geometry["v_masses"] != record["advertised_unclipped_v_masses"],
                    "clipped negative regression unexpectedly obeys unclipped law")
            record["unclipped_mass_formula_fails"] = True
        output.append(record)
    return output


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, Affine):
        return {"slope": encode(value.slope), "intercept": encode(value.intercept)}
    if isinstance(value, (list, tuple)):
        return [encode(entry) for entry in value]
    if isinstance(value, dict):
        return {key: encode(entry) for key, entry in value.items()}
    return value


def json_bytes(value) -> bytes:
    return (json.dumps(encode(value), indent=2, sort_keys=True) + "\n").encode("utf-8")


def generate_reports() -> dict[str, dict]:
    fixture_parameters = [
        ("shrinking_2_5", F(2,5), F(1,5)),
        ("shrinking_1_4", F(1,4), F(1,8)),
        ("shrinking_1_10", F(1,10), F(1,20)),
        ("shrinking_1_100", F(1,100), F(1,200)),
        ("shrinking_1_1000", F(1,1000), F(1,2000)),
        ("fixed_1_32", F(1,4), F(1,32)),
        ("fixed_1_128", F(1,4), F(1,128)),
        ("fixed_1_1024", F(1,4), F(1,1024)),
        ("equal_masses", F(1,3), F(1,6)),
        ("lower_width_near_zero", F(1,4), F(249,1000)),
        ("upper_width_near_one", F(3,5), F(399,1000)),
        ("both_boundaries_near", F(1,2), F(499,1000)),
        ("small_mass_near_lower_boundary", F(1,10000), F(9999,100000000)),
    ]
    fixtures = [{"label": label, **check_case(a, b)}
                for label, a, b in fixture_parameters]
    rational_grid = sorted({F(n,d) for d in range(2,9) for n in range(1,d)})
    grid = []
    for a in rational_grid:
        for b in rational_grid:
            if 0 < b < a and a+b < 1:
                result = check_case(a, b, even_ps=(2,4,6))
                grid.append({"a": a, "b": b, "atom_masses": result["atom_masses"],
                             "joint_matrix": result["common_source_joint_mass_matrix"],
                             "W2_squared": result["W2_squared"],
                             "L2_map_difference_squared": result["L2_map_difference_squared"],
                             "vertices_enumerated": result["distinct_vertices_enumerated"],
                             "even_p_values_certified": [2,4,6], "checks_passed": True})
    exponent_records, scaling = [], []
    for p in (F(1), F(3,2), F(2), F(3), F(4), F(7,2)):
        ceiling = p/(2*(p+1))
        for family, threshold in (("shrinking_mass", ceiling), ("fixed_mass", F(1,2))):
            # Keep the regression witnesses readable: 1/2 is strictly above
            # every finite-p shrinking-mass ceiling, and 3/5 is above the
            # fixed-mass ceiling. Arbitrary rational alpha is supported by
            # the reusable witness API, without imposing this fixture choice.
            alpha = F(1,2) if family == "shrinking_mass" else F(3,5)
            for constant in (F(1), F(2), F(10), F(100)):
                exponent_records.append(counterexample_witness(p, alpha, constant, family))
            for label, exponent in (("below_ceiling", threshold/2),
                                    ("at_ceiling", threshold),
                                    ("above_ceiling", alpha)):
                values = []
                for k in (3,5,8,12):
                    a = F(1,2**k) if family == "shrinking_mass" else F(1,4)
                    b = a/2 if family == "shrinking_mass" else F(1,2**k)
                    values.append(exact_ratio_power(a,b,p,exponent))
                scaling.append({"family": family, "p": p, "ceiling": threshold,
                                "position": label, "values": values,
                                "interpretation": "finite exact powered ratios; the limit requires the ordinary proof"})
    common = {"schema": "transport-sharpness-exact-arithmetic-v1",
              "verified_starting_commit": BASELINE,
              "arithmetic": "fractions.Fraction; standard library; no floating-point roots",
              "dimension_executed": 2,
              "source": "uniform probability on [-1,1]^2; density 1/4 on the square and 0 outside",
              "limitations": "Finite executable checks and explicit LP certificates. No Lean acceptance, all-real-parameter proof, real-p LP arithmetic, or higher-dimensional execution is claimed."}
    return {"exact-cases.json": {**common, "cases": fixtures,
                                 "negative_regressions": negative_regressions()},
            "regression-grid.json": {**common, "grid_definition": "distinct n/d, 2<=d<=8, 1<=n<d; all admissible ordered a,b",
                                     "case_count": len(grid), "cases": grid},
            "exponent-regressions.json": {**common,
                                          "powered_ratio_identity": "R^(2L)=(b/2+a*b^2)^L/(a^(2L*alpha/p)*b^(2L*alpha))",
                                          "candidate_constant_witnesses": exponent_records,
                                          "scaling_cases": scaling}}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", nargs=2, metavar=("A", "B"),
                        help="check any rational admissible a,b; print its certificate")
    parser.add_argument("--output-dir", type=Path,
                        default=Path(__file__).resolve().parents[1]/"data",
                        help="write deterministic default reports to this directory")
    parser.add_argument("--verify", action="store_true",
                        help="recompute and require byte-identical existing reports without writing")
    args = parser.parse_args()
    if args.case:
        print(json_bytes(check_case(*args.case)).decode("utf-8"), end="")
        return
    reports = generate_reports()
    if not args.verify:
        args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, report in reports.items():
        path, payload = args.output_dir/name, json_bytes(report)
        if args.verify:
            require(path.read_bytes() == payload, f"regenerated bytes differ: {path}")
        else:
            path.write_bytes(payload)
        print(f"{'Verified' if args.verify else 'Wrote'} {path.name}: sha256={sha256(payload).hexdigest()}")
    print(f"Passed {len(reports['exact-cases.json']['cases'])} named fixtures, "
          f"{reports['regression-grid.json']['case_count']} rational-grid cases, "
          f"{len(reports['exact-cases.json']['negative_regressions'])} rejected inputs, and "
          f"{len(reports['exponent-regressions.json']['candidate_constant_witnesses'])} "
          "exact Holder-constant violations.")


if __name__ == "__main__":
    main()
