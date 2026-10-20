#!/usr/bin/env python3
"""Exact finite checks for the original averaging/separability chapter.

These checks exercise independent matrix representations and counterexamples.
They supplement the proofs; they are not formal verification.
"""

import argparse
import json
from pathlib import Path

import sympy as sp


t = sp.Symbol("t")


def reduce_matrix(matrix, prime):
    if prime is None:
        return matrix
    return matrix.applyfunc(
        lambda value: int(sp.numer(value))
        * pow(int(sp.denom(value)), -1, prime)
        % prime
    )


def rank_mod(matrix, prime):
    rows = [list(map(int, row)) for row in matrix.tolist()]
    nrows, ncols = matrix.shape
    rank = 0
    for col in range(ncols):
        pivot = next(
            (row for row in range(rank, nrows) if rows[row][col] % prime), None
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = pow(rows[rank][col] % prime, -1, prime)
        rows[rank] = [(scale * value) % prime for value in rows[rank]]
        for row in range(nrows):
            if row != rank:
                scale = rows[row][col] % prime
                rows[row] = [
                    (a - scale * b) % prime
                    for a, b in zip(rows[row], rows[rank])
                ]
        rank += 1
    return rank


def companion(poly):
    degree = sp.degree(poly, t)
    matrix = sp.zeros(degree)
    for j in range(degree - 1):
        matrix[j + 1, j] = 1
    for j in range(degree):
        matrix[j, degree - 1] = -sp.expand(poly).coeff(t, j)
    return matrix


def tensor_data(poly):
    matrix = companion(poly)
    degree = matrix.rows
    identity = sp.eye(degree)
    x = sp.kronecker_product(matrix, identity)
    y = sp.kronecker_product(identity, matrix)
    unit = sp.zeros(degree, 1)
    unit[0] = 1
    tensor_unit = sp.kronecker_product(unit, unit)
    multiplication = sp.Matrix.hstack(
        *((matrix ** (i + j)) * unit for i in range(degree) for j in range(degree))
    )
    return matrix, x, y, unit, tensor_unit, multiplication


def polynomial_tensor_case(poly, prime=None):
    matrix, x, y, unit, tensor_unit, multiplication = tensor_data(poly)
    degree = matrix.rows
    derivative = sp.diff(poly, t)
    if prime is None:
        inverse = sp.invert(derivative, poly, t)
    else:
        inverse = sp.invert(derivative, poly, t, modulus=prime)
    inverse_operator = sp.zeros(degree * degree)
    for j in range(degree):
        inverse_operator += sp.expand(inverse).coeff(t, j) * y**j
    difference = sp.zeros(degree * degree)
    for power in range(1, degree + 1):
        for j in range(power):
            difference += (
                sp.expand(poly).coeff(t, power) * x ** (power - 1 - j) * y**j
            )
    tensor_operator = difference * inverse_operator
    tensor = reduce_matrix(tensor_operator * tensor_unit, prime)
    assert reduce_matrix((x - y) * tensor, prime) == sp.zeros(degree * degree, 1)
    assert reduce_matrix(multiplication * tensor, prime) == unit
    assert reduce_matrix(tensor_operator * tensor - tensor, prime) == sp.zeros(
        degree * degree, 1
    )

    # Independent rectangular Hom-space action, using regular modules S and S^2.
    source = matrix
    target = sp.diag(matrix, matrix)
    arbitrary = sp.Matrix(
        2 * degree, degree, lambda i, j: ((i + 3) * (j + 5) + i * i) % 11 - 5
    )

    def average(linear_map):
        result = sp.zeros(2 * degree, degree)
        for i in range(degree):
            for j in range(degree):
                result += (
                    tensor[degree * i + j] * target**i * linear_map * source**j
                )
        return reduce_matrix(result, prime)

    repaired = average(arbitrary)
    assert reduce_matrix(target * repaired - repaired * source, prime) == sp.zeros(
        2 * degree, degree
    )
    assert average(repaired) == repaired
    inclusion = sp.Matrix.vstack(sp.eye(degree), sp.zeros(degree))
    assert average(inclusion) == inclusion
    return {
        "polynomial": str(poly),
        "field": "Q" if prime is None else f"F_{prime}",
        "tensor_coefficients": list(map(str, tensor)),
        "rectangular_hom_shape": [2 * degree, degree],
    }


def impossible_tensor_case(poly, prime=None):
    matrix, x, y, unit, tensor_unit, multiplication = tensor_data(poly)
    degree = matrix.rows
    constraints = (x - y).col_join(multiplication)
    rhs = sp.zeros(degree * degree, 1).col_join(unit)
    if prime is None:
        ranks = [constraints.rank(), constraints.row_join(rhs).rank()]
    else:
        ranks = [
            rank_mod(constraints, prime),
            rank_mod(constraints.row_join(rhs), prime),
        ]
    assert ranks[1] > ranks[0]
    return {
        "polynomial": str(poly),
        "field": "Q" if prime is None else f"F_{prime}",
        "constraint_rank": ranks[0],
        "augmented_rank": ranks[1],
    }


def matrix_unit(i, j, size):
    result = sp.zeros(size)
    result[i, j] = 1
    return result


def run_checks():
    polynomial_cases = [
        polynomial_tensor_case(t**2 - 1),
        polynomial_tensor_case(t**2 + 1),
        polynomial_tensor_case(t**3 - 2),
        polynomial_tensor_case(t**3 - t, 5),
        polynomial_tensor_case(t**2 + t + 1, 2),
    ]
    impossible_cases = [
        impossible_tensor_case(t**2),
        impossible_tensor_case((t - 1) ** 2 * (t + 2)),
        impossible_tensor_case(t**2 - 1, 2),
    ]

    involution = sp.Matrix([[1, 2], [0, -1]])
    projection = sp.Matrix([[1, 3], [0, 0]])
    repaired = (projection + involution * projection * involution) / 2
    assert repaired == sp.Matrix([[1, 1], [0, 0]])
    assert repaired**2 == repaired
    assert involution * repaired == repaired * involution
    section = sp.Matrix([0, 1])
    repaired_section = (section - involution * section) / 2
    assert repaired_section == sp.Matrix([-1, 1])

    diagonal = sp.diag(1, -1)
    average = lambda f: (f + diagonal * f * diagonal) / 2
    f, g = matrix_unit(0, 1, 2), matrix_unit(1, 0, 2)
    assert average(f) * average(g) == sp.zeros(2)
    assert average(f * g) == matrix_unit(0, 0, 2)
    q = sp.ones(2) / 2
    assert q**2 == q
    assert average(q) == sp.eye(2) / 2
    assert average(q) ** 2 != average(q)

    matrix_cases = []
    for size in (2, 3):
        units = [
            matrix_unit(i, j, size)
            for i in range(size)
            for j in range(size)
        ]
        terms = [
            (matrix_unit(i, 0, size), matrix_unit(0, i, size))
            for i in range(size)
        ]
        # Faithful A^e representation: a tensor b^op -> a tensor transpose(b).
        e = sum(
            (sp.kronecker_product(a, b.T) for a, b in terms),
            sp.zeros(size * size),
        )
        assert sum((a * b for a, b in terms), sp.zeros(size)) == sp.eye(size)
        assert e * e == e
        for c in units:
            assert sp.kronecker_product(c, sp.eye(size)) * e == (
                sp.kronecker_product(sp.eye(size), c.T) * e
            )
        # Integer identities also hold after reduction at the prime dividing size.
        assert reduce_matrix(e * e - e, size) == sp.zeros(size * size)
        matrix_cases.append({"matrix_size": size, "characteristic_checked": size})

    return {
        "description": "Exact finite checks supporting the averaging chapter",
        "scope": "Examples and counterexamples; not formal verification",
        "passed": True,
        "groups": 5,
        "polynomial_tensor_cases": polynomial_cases,
        "nonexistence_by_linear_rank": impossible_cases,
        "invariant_projection_and_section": {
            "projection": [[1, 1], [0, 0]],
            "section": [-1, 1],
        },
        "nonmultiplicativity_and_nonpreservation_of_idempotence": True,
        "matrix_algebra_cases": matrix_cases,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    evidence = run_checks()
    rendered = json.dumps(evidence, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end="")
