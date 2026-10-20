#!/usr/bin/env python3
"""Exact checks for notes/12-integral-spectral-gluing.md.

Requires SymPy. This is a fixed-example and finite identity checker, not a
Hadamard/Williamson search. It writes no files and uses no network.
"""

from itertools import product
from math import comb
import json

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

t = sp.Symbol("t")


def poly(expr):
    return sp.Poly(expr, t, domain=sp.QQ)


def coefficients(expr, length):
    p = poly(expr)
    return sp.Matrix([p.nth(j) for j in range(length)])


def expression(vector):
    return sum(c * t**j for j, c in enumerate(vector))


def remainder(expr, modulus):
    return poly(expr).rem(poly(modulus)).as_expr()


def multiplication_matrix(expr, modulus):
    degree = sp.degree(modulus, t)
    return sp.Matrix.hstack(
        *[coefficients(remainder(expr * t**j, modulus), degree)
          for j in range(degree)]
    )


def field_trace(expr, d):
    return sp.trace(multiplication_matrix(expr, sp.cyclotomic_poly(d, t)))


def evaluation_matrix(m):
    blocks = []
    for d in sp.divisors(m):
        phi = sp.cyclotomic_poly(d, t)
        blocks.append(sp.Matrix.hstack(
            *[coefficients(remainder(t**j, phi), sp.degree(phi, t))
              for j in range(m)]
        ))
    return sp.Matrix.vstack(*blocks)


def split_components(vector, m):
    offset = 0
    result = {}
    for d in sp.divisors(m):
        size = int(sp.totient(d))
        result[d] = expression(vector[offset:offset + size])
        offset += size
    assert offset == m
    return result


def trace_inverse(vector, m):
    components = split_components(vector, m)
    return sp.Matrix([
        sum(field_trace(b * t**((-j) % d), d)
            for d, b in components.items()) / m
        for j in range(m)
    ])


def integral(vector):
    return all(c.q == 1 for c in vector)


def even_components(vector):
    return all(c.q == 1 and c % 2 == 0 for c in vector)


def gram(row):
    m = len(row)
    return sp.Matrix([
        sum(row[j] * row[(j + s) % m] for j in range(m))
        for s in range(m)
    ])


def summed_gram(rows):
    return sum((gram(row) for row in rows), sp.zeros(len(rows[0]), 1))


def circulant(row):
    m = len(row)
    return sp.Matrix(m, m, lambda i, j: row[(j - i) % m])


def smith_diagonal(matrix):
    smith = smith_normal_form(matrix, domain=sp.ZZ)
    return [abs(int(smith[j, j])) for j in range(min(smith.shape))]


def test_resultants_and_defects():
    cases = [
        (t - 1, t + 1, 2),
        (t - 1, t**2 + t + 1, 3),
        (t**2 - 1, t**2 + 1, 4),
        ((t - 1)**2, t**2 + 1, 4),
        (t**2 + 1, t**3 - 2, 5),
    ]
    for f, g, expected in cases:
        multiplication = multiplication_matrix(g, f)
        result = sp.resultant(f, g, t)
        assert result == expected
        assert multiplication.det() == result
        r, s = sp.degree(f, t), sp.degree(g, t)
        sylvester = sp.Matrix.hstack(
            *[coefficients(f * t**j, r + s) for j in range(s)],
            *[coefficients(g * t**j, r + s) for j in range(r)],
        )
        assert abs(sylvester.det()) == abs(result)
    assert smith_diagonal(multiplication_matrix(t**2 + 1, t**2 - 1)) == [2, 2]
    assert remainder(2 * t * (t - 1), 2 * t) == 0
    assert remainder(2 * t * (t - 1), 2 * (t - 1)) == 0
    # Rational quotient 1/2 is not an integral polynomial.
    assert sp.cancel(2 * t * (t - 1) / (4 * t * (t - 1))) == sp.Rational(1, 2)
    return {"resultant_cases": len(cases), "noncyclic_defect": [2, 2]}


def test_prime_reconstruction():
    count = 0
    for p in [2, 3, 5, 7, 11]:
        phi = sp.cyclotomic_poly(p, t)
        representatives = [0, 1, -2, sum((-1)**j * (j + 1) * t**j
                                       for j in range(p - 1))]
        representatives += [t**j for j in range(p - 1)]
        for b in representatives:
            b_at_one = sp.expand(b).subs(t, 1) if hasattr(b, "subs") else b
            for shift in [-2, 0, 1]:
                a = b_at_one + p * shift
                reconstructed = sp.Matrix([
                    (a + field_trace(b * t**((-j) % p), p)) / p
                    for j in range(p)
                ])
                assert reconstructed == coefficients(b + shift * phi, p)
                assert integral(reconstructed)
                wrong_a = a + 1
                wrong = sp.Matrix([
                    (wrong_a + field_trace(b * t**((-j) % p), p)) / p
                    for j in range(p)
                ])
                assert not integral(wrong)
                count += 1
    return {"prime_reconstruction_cases": count, "primes": [2, 3, 5, 7, 11]}


def test_prime_parity():
    count = 0
    for p in [2, 3]:
        evaluation = evaluation_matrix(p)
        for values in product(range(-2, 3), repeat=p):
            row = sp.Matrix(values)
            data = evaluation * row
            expected = all(v % 2 == 1 for v in values)
            a = data[0]
            if p == 2:
                b = data[1]
                found = (a + b) % 4 == 2 and (a - b) % 4 == 2
            else:
                found = a % 2 == 1 and all(v % 2 == 0 for v in data[1:])
            assert found == expected
            count += 1
    assert evaluation_matrix(2).inv() * sp.Matrix([2, 2]) == sp.Matrix([2, 0])
    return {"bounded_coefficient_vectors": count, "p2_exception_verified": True}


def test_general_trace_and_indices():
    details = {}
    for m in [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]:
        evaluation = evaluation_matrix(m)
        inverse = evaluation.inv()
        factors = [sp.cyclotomic_poly(d, t) for d in sp.divisors(m)]
        predicted = sp.prod(
            abs(sp.resultant(factors[i], factors[j], t))
            for i in range(len(factors)) for j in range(i + 1, len(factors))
        )
        assert abs(evaluation.det()) == predicted
        for j in range(m):
            basis = sp.eye(m)[:, j]
            assert trace_inverse(basis, m) == inverse * basis
        assert integral(m * inverse)
        details[str(m)] = int(abs(evaluation.det()))
    for p, a in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2)]:
        m = p**a
        assert abs(evaluation_matrix(m).det()) == p**sum(p**j for j in range(a))
    return {"integral_indices": details, "all_component_basis_traces_checked": True}


def test_order_four():
    evaluation = evaluation_matrix(4)
    expected = sp.Matrix([[1, 1, 1, 1], [1, -1, 1, -1],
                          [1, 0, -1, 0], [0, 1, 0, -1]])
    assert evaluation == expected
    assert evaluation.det() == -8
    assert smith_diagonal(evaluation) == [1, 1, 2, 4]
    inverse = evaluation.inv()
    for a, c, u, v in product(range(-1, 2), repeat=4):
        conditions = (a + c - 2 * u) % 4 == 0 and (a - c - 2 * v) % 4 == 0
        assert integral(inverse * sp.Matrix([a, c, u, v])) == conditions
    assert inverse * sp.Matrix([0, 0, 1, 1]) == sp.Matrix([1, 1, -1, -1]) / 2
    assert inverse * sp.Matrix([2, 0, 0, 0]) == sp.ones(4, 1) / 2
    assert evaluation.extract([0, 2], [1, 2]).det() == -1
    assert evaluation.extract([0, 1, 2], [0, 1, 2]).det() == 4
    assert evaluation.extract([0, 2, 3], [0, 1, 2]).det() == 2
    return {"index": 8, "smith": [1, 1, 2, 4], "mod4_cases": 81}


def test_order_nine():
    evaluation = evaluation_matrix(9)
    assert abs(evaluation.det()) == 81
    invariants = smith_diagonal(evaluation)
    assert invariants == [1] * 6 + [3, 3, 9]
    phi1, phi3, phi9 = [sp.cyclotomic_poly(d, t) for d in [1, 3, 9]]
    assert [sp.resultant(phi1, phi3, t), sp.resultant(phi1, phi9, t),
            sp.resultant(phi3, phi9, t)] == [3, 3, 9]
    assert remainder(phi9, phi3) == 3
    assert smith_diagonal(3 * evaluation_matrix(3)) == [3, 3, 9]
    return {"index": 81, "smith": invariants}


def hasse_jet(expr, q, p):
    expanded = poly(expr)
    return [sum(comb(j, k) * expanded.nth(j)
                for j in range(k, max(0, expanded.degree()) + 1)) % p
            for k in range(q)]


def test_prime_power_jets():
    count = 0
    for p, a in [(2, 1), (2, 2), (2, 3), (3, 2), (5, 1)]:
        q, m = p**(a - 1), p**a
        f, g = t**q - 1, sp.cyclotomic_poly(m, t)
        assert remainder(g, f) == p
        assert sp.Poly(f - (t - 1)**q, t, modulus=p).is_zero
        assert sp.Poly(g - (t - 1)**((p - 1) * q), t, modulus=p).is_zero
        stage = sp.Matrix.vstack(
            sp.Matrix.hstack(*[coefficients(remainder(t**j, f), q)
                               for j in range(m)]),
            sp.Matrix.hstack(*[coefficients(remainder(t**j, g), m - q)
                               for j in range(m)]),
        )
        assert abs(stage.det()) == p**q
        probes = [sp.zeros(m, 1)] + [sp.eye(m)[:, j] for j in range(m)]
        probes += [p * v for v in probes[1:]]
        probes += [sp.Matrix([(-1)**j * (j + 1) for j in range(m)])]
        for target in probes:
            lower = expression(target[:q])
            upper = expression(target[q:])
            jets_match = hasse_jet(lower, q, p) == hasse_jet(upper, q, p)
            assert integral(stage.inv() * target) == jets_match
            count += 1
    assert hasse_jet((t - 1)**2, 3, 3) == [0, 0, 1]
    assert hasse_jet((t - 1)**2, 4, 2) == [0, 0, 1, 0]
    assert all(sp.diff((t - 1)**2, t, k).subs(t, 1) % 2 == 0 for k in range(5))
    return {"stage_probe_cases": count, "ordinary_derivative_failure": True}


def test_energy_example():
    row = sp.Matrix([1, 2, -1, 0, 0, 0, 0, 0, 0, -1, 2])
    assert sum(row) == 3
    assert (row.T * row)[0] == 11
    assert all(row[j] == row[-j % 11] for j in range(11))
    b = remainder(expression(row), sp.cyclotomic_poly(11, t))
    b_bar = remainder(sum(row[j] * t**((-j) % 11) for j in range(11)),
                      sp.cyclotomic_poly(11, t))
    assert b == b_bar
    assert 3 + field_trace(b, 11) == 11
    assert 9 + field_trace(b * b_bar, 11) == 121
    c = sp.Symbol("c")
    spectral = 3 + 4 * c - 4 * c**2
    assert [spectral.subs(c, x) for x in [-1, 1, sp.Rational(1, 2)]] == [-5, 3, 4]
    assert sp.diff(spectral, c, 2) == -8
    assert 25 < 44
    assert not all(x in [-1, 1] for x in row)
    return {"augmentation": 3, "energy": 11, "spectral_interval": [-5, 4]}


def test_gram_counterexamples():
    rows = [[1, -2, -2], [1, 0, 0], [1, 0, 0], [1, 0, 0]]
    assert summed_gram(rows) == sp.Matrix([12, 0, 0])
    assert [gram(r)[0] for r in rows] == [9, 1, 1, 1]
    assert [evaluation_matrix(3) * sp.Matrix(r) for r in rows] == [
        sp.Matrix([-3, 3, 0]), *[sp.Matrix([1, 1, 0]) for _ in range(3)]
    ]
    # Even-order component parity can miss affine-lattice membership.
    evaluation = evaluation_matrix(4)
    row = sp.Matrix([2, 0, 0, 0])
    b = evaluation * row
    J = evaluation * sp.ones(4, 1)
    assert even_components(b - J)
    assert summed_gram([list(row)] * 4) == sp.Matrix([16, 0, 0, 0])
    assert evaluation.inv() * ((b - J) / 2) == sp.Matrix([1, -1, -1, -1]) / 2
    assert not integral(evaluation.inv() * ((b - J) / 2))
    # Odd-order parity/norm data with no integral gluing.
    prime3_data = [sp.Matrix([3, 0, 0])] + [sp.Matrix([1, 2, 0])] * 3
    reconstructed = [evaluation_matrix(3).inv() * v for v in prime3_data]
    assert reconstructed == [sp.ones(3, 1)] + [sp.Matrix([5, -1, -1]) / 3] * 3
    assert [(r.T * r)[0] for r in reconstructed] == [3] * 4
    assert summed_gram(reconstructed) == sp.Matrix([12, 0, 0])
    return {"normalized_m3_integral_nonsign": True,
            "even_m4_affine_failure": True, "odd_m3_gluing_failure": True}


def test_nonsymmetric_array():
    a, b, c, d = map(circulant, [[1, 1, 1], [1, 1, -1],
                               [1, 1, -1], [1, -1, 1]])
    assert sum((x * x.T for x in [a, b, c, d]), sp.zeros(3)) == 12 * sp.eye(3)
    array = sp.Matrix.vstack(
        sp.Matrix.hstack(a, b, c, d),
        sp.Matrix.hstack(-b, a, -d, c),
        sp.Matrix.hstack(-c, d, a, -b),
        sp.Matrix.hstack(-d, -c, b, a),
    )
    block = (array * array.T)[:3, 3:6]
    assert block == sp.Matrix([[0, -4, 4], [4, 0, -4], [-4, 4, 0]])
    return {"nonzero_gram_block_12": [list(block.row(j)) for j in range(3)]}


def test_affine_certificate_examples():
    examples = {
        1: [[1]] * 4,
        2: [[1, 1], [1, 1], [1, -1], [1, -1]],
        3: [[1, 1, 1], [1, -1, -1], [1, -1, -1], [1, -1, -1]],
        4: [[1, 1, -1, 1]] * 4,
    }
    for m, rows in examples.items():
        evaluation = evaluation_matrix(m)
        J = evaluation * sp.ones(m, 1)
        assert summed_gram(rows) == sp.Matrix([4 * m] + [0] * (m - 1))
        for row in rows:
            b = evaluation * sp.Matrix(row)
            assert integral(evaluation.inv() * ((b - J) / 2))
            assert trace_inverse(b, m) == sp.Matrix(row)
            assert all(row[j] == row[(-j) % m] for j in range(m))
    return {"valid_symmetric_sign_examples": list(examples)}


def test_exercises_and_hypothesis_examples():
    e3 = evaluation_matrix(3)
    assert e3.inv() * sp.Matrix([1, 1, 1]) == sp.Matrix([2, 2, -1]) / 3
    row5 = sp.Matrix([1, -1, 1, 1, -1])
    data5 = evaluation_matrix(5) * row5
    assert data5[0] == 1
    b5 = expression(data5[1:])
    assert field_trace(b5, 5) == 4
    assert field_trace(b5**2, 5) == 24
    # Product condition alone at odd order.
    rows5 = [[1, -1, -1, -1, -1]] + [[1, 1, 1, 1, 1]] * 3
    assert all(sp.prod(row[j] for row in rows5) == -1 for j in range(1, 5))
    assert sum(sum(row)**2 for row in rows5) == 84
    # Oddness and normalization cannot be deleted from the product theorem.
    rows2 = [[1, 1], [1, 1], [1, -1], [1, -1]]
    assert summed_gram(rows2) == sp.Matrix([8, 0])
    assert sp.prod(row[1] for row in rows2) == 1
    rows3 = [[-1, -1, -1]] + [[1, -1, -1]] * 3
    assert summed_gram(rows3) == sp.Matrix([12, 0, 0])
    assert all(sp.prod(row[j] for row in rows3) == 1 for j in [1, 2])
    real_row = sp.Matrix([1, sp.sqrt(2), 0, 0, sp.sqrt(2)])
    assert (real_row.T * real_row)[0] == 5
    return {"exercise_and_hypothesis_examples": "passed"}


def main():
    groups = [
        test_resultants_and_defects,
        test_prime_reconstruction,
        test_prime_parity,
        test_general_trace_and_indices,
        test_order_four,
        test_order_nine,
        test_prime_power_jets,
        test_energy_example,
        test_gram_counterexamples,
        test_nonsymmetric_array,
        test_affine_certificate_examples,
        test_exercises_and_hypothesis_examples,
    ]
    results = {group.__name__: group() for group in groups}
    print(json.dumps({"status": "passed", "groups": len(groups),
                      "sympy_version": sp.__version__, "results": results},
                     indent=2, default=str))


if __name__ == "__main__":
    main()
