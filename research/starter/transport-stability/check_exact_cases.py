#!/usr/bin/env python3
"""Exact, standard-library-only checks for the three-atom obstruction.

The cell masses are computed by rational half-plane clipping and shoelace
areas, not by substituting the closed-form mass formulas. The target W2
problem is independently checked by enumerating all basic feasible 3x3
transport matrices. This is an arithmetic check, not a formal proof.
"""

from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json


def clip(poly, coefficients):
    A, B, C = coefficients

    def value(point):
        x, t = point
        return A * x + B * t + C

    result = []
    if not poly:
        return result
    for start, end in zip(poly, poly[1:] + poly[:1]):
        vs, ve = value(start), value(end)
        if vs >= 0:
            result.append(start)
        if (vs < 0 < ve) or (ve < 0 < vs):
            weight = vs / (vs - ve)
            result.append(tuple(s + weight * (e - s) for s, e in zip(start, end)))
    return result


def polygon_mass(poly):
    if len(poly) < 3:
        return F(0)
    double_area = sum(x1 * t2 - x2 * t1
                      for (x1, t1), (x2, t2) in zip(poly, poly[1:] + poly[:1]))
    return abs(double_area) / 8  # area / area([-1,1]^2)


def solve_square(matrix, rhs):
    n = len(rhs)
    rows = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = next((i for i in range(column, n) if rows[i][column]), None)
        if pivot is None:
            return None
        rows[column], rows[pivot] = rows[pivot], rows[column]
        factor = rows[column][column]
        rows[column] = [entry / factor for entry in rows[column]]
        for i in range(n):
            if i != column:
                factor = rows[i][column]
                rows[i] = [entry - factor * pivot_entry
                           for entry, pivot_entry in zip(rows[i], rows[column])]
    return [row[-1] for row in rows]


def transport_vertices(masses):
    # Three row sums and two column sums form five independent constraints.
    columns = []
    for i in range(3):
        for j in range(3):
            columns.append(tuple(F(int(i == r)) for r in range(3)) +
                           tuple(F(int(j == c)) for c in range(2)))
    rhs = masses + masses[:2]
    vertices = set()
    for support in combinations(range(9), 5):
        matrix = [[columns[index][row] for index in support] for row in range(5)]
        solution = solve_square(matrix, rhs)
        if solution is None or any(x < 0 for x in solution):
            continue
        entries = [F(0)] * 9
        for index, value in zip(support, solution):
            entries[index] = value
        assert [sum(entries[3*i:3*i+3]) for i in range(3)] == masses
        assert [sum(entries[j::3]) for j in range(3)] == masses
        vertices.add(tuple(entries))
    return sorted(vertices)


def check_case(a):
    b = a / 2
    assert 0 < b < a and a + b < 1
    square = [(F(-1), F(-1)), (F(1), F(-1)),
              (F(1), F(1)), (F(-1), F(1))]
    u_cells = [[(-1, 0, -a)], [(1, 0, a), (-1, 0, a)], [(1, 0, -a)]]
    v_cells = [[(-1, -b, -a)], [(1, b, a), (-1, b, a)], [(1, -b, -a)]]
    joint = []
    for u_cell in u_cells:
        row = []
        for v_cell in v_cells:
            polygon = square
            for plane in u_cell + v_cell:
                polygon = clip(polygon, plane)
            row.append(polygon_mass(polygon))
        joint.append(row)
    masses = [(1-a)/2, a, (1-a)/2]
    assert [sum(row) for row in joint] == masses
    assert [sum(row[j] for row in joint) for j in range(3)] == masses
    expected = [[masses[0]-b/8, b/8, F(0)],
                [b/8, a-b/4, b/8],
                [F(0), b/8, masses[2]-b/8]]
    assert joint == expected
    source_points = [(-1, 0), (0, 0), (1, 0)]
    target_points = [(-1, 0), (0, b), (1, 0)]
    costs = [[sum((F(y)-F(z))**2 for y, z in zip(src, dst))
              for dst in target_points] for src in source_points]
    map_cost = sum(joint[i][j] * costs[i][j] for i in range(3) for j in range(3))
    assert map_cost == b/2 + a*b*b
    flat_cost = sum(costs, [])
    vertices = transport_vertices(masses)
    objective = [sum(x*c for x, c in zip(vertex, flat_cost)) for vertex in vertices]
    minimum = min(objective)
    minimizers = [vertex for vertex, cost in zip(vertices, objective) if cost == minimum]
    assert minimum == a*b*b
    assert len(minimizers) == 1
    expected_matching = (masses[0], F(0), F(0), F(0), a, F(0), F(0), F(0), masses[2])
    assert minimizers[0] == expected_matching
    # Rational certificate for |y-z| >= |y_2-z_2|, hence W1 >= a*b.
    coordinate_costs = [[abs(F(src[1])-F(dst[1])) for dst in target_points]
                        for src in source_points]
    assert all(costs[i][j] >= coordinate_costs[i][j]**2
               for i in range(3) for j in range(3))
    assert sum(masses[j] * coordinate_costs[0][j] for j in range(3)) == a*b
    return {
        "a": a, "b": b,
        "central_width_range": [a-b, a+b],
        "target_masses_order_minus_central_plus": masses,
        "common_source_joint_mass_matrix": joint,
        "quadratic_target_cost_matrix": costs,
        "central_intersection_mass": joint[1][1],
        "A_minus_B_mass": joint[1][0] + joint[1][2],
        "B_minus_A_mass": joint[0][1] + joint[2][1],
        "symmetric_difference_mass": joint[1][0] + joint[1][2] + joint[0][1] + joint[2][1],
        "W1": a*b,
        "W2_squared": minimum,
        "L2_map_difference_squared": map_cost,
        "common_source_cost_divided_by_optimal_target_cost": map_cost/minimum,
        "transport_polytope_distinct_vertices_enumerated": len(vertices),
        "quadratic_minimizer_vertices": len(minimizers),
        "checks_passed": True,
    }


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, list):
        return [encode(x) for x in value]
    if isinstance(value, dict):
        return {key: encode(val) for key, val in value.items()}
    return value


def main():
    result = {
        "schema": "portable-exact-arithmetic-cases-v1",
        "family_id": "374",
        "arithmetic": "fractions.Fraction; no floating point",
        "methods": ["rational half-plane polygon clipping and shoelace areas",
                    "enumeration of all invertible 5-column bases of the 3x3 transport polytope",
                    "coordinate-projection lower bound for W1"],
        "limitations": "Finite fixtures and arithmetic certificates; not Lean or a substitute for the parameter-uniform written proof.",
        "cases": [check_case(a) for a in [F(2, 5), F(1, 4), F(1, 10), F(1, 100)]],
    }
    output = Path(__file__).with_name("exact-cases.json")
    output.write_text(json.dumps(encode(result), indent=2) + "\n")
    print(f"Passed {len(result['cases'])} exact cases; wrote {output.name}")
    for case in result["cases"]:
        print(f"a={case['a']}: W1={case['W1']}, W2²={case['W2_squared']}, "
              f"L2²={case['L2_map_difference_squared']}, "
              f"LP vertices={case['transport_polytope_distinct_vertices_enumerated']}")


if __name__ == "__main__":
    main()
