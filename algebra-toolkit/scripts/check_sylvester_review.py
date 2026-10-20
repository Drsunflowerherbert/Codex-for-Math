#!/usr/bin/env python3
"""Independent finite-field adversarial checks; pure Python, no imports of the author checker."""
from itertools import permutations, product
import json


def matrices(rows, cols, p):
    return list(product(range(p), repeat=rows * cols))


def mul(a, b, rows, inner, cols, p):
    return tuple(
        sum(a[i * inner + k] * b[k * cols + j] for k in range(inner)) % p
        for i in range(rows) for j in range(cols)
    )


def add(a, b, p):
    return tuple((x + y) % p for x, y in zip(a, b))


def scale(c, a, p):
    return tuple(c * x % p for x in a)


def delta(a, b, h, m, n, p):
    return add(mul(a, h, m, m, n, p), scale(-1, mul(h, b, m, n, n, p), p), p)


def trace_pair(g, c, m, n, p):
    return sum(g[j * m + i] * c[i * n + j] for i in range(m) for j in range(n)) % p


def det(a, n, p):
    total = 0
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = (-1) ** inversions
        for i in range(n):
            term *= a[i * n + perm[i]]
        total += term
    return total % p


def charpoly(a, n, p):
    # Descending coefficient order. Tests use dimensions at most two.
    if n == 1:
        return [1, -a[0] % p]
    return [1, -(a[0] + a[3]) % p, det(a, 2, p)]


def resultant(f, g, p):
    m, n = len(f) - 1, len(g) - 1
    rows = []
    for shift in range(n):
        rows.append([0] * shift + f + [0] * (n - shift - 1))
    for shift in range(m):
        rows.append([0] * shift + g + [0] * (m - shift - 1))
    return det(tuple(x for row in rows for x in row), m + n, p)


counts = {"endpoint_pairs": 0, "extension_blocks": 0, "resultant_identities": 0}
for p in (2, 3):
    for m, n in product((1, 2), repeat=2):
        if p == 3 and m * n > 2:
            continue
        hs = matrices(m, n, p)
        gs = matrices(n, m, p)
        for a in matrices(m, m, p):
            for b in matrices(n, n, p):
                values = [delta(a, b, h, m, n, p) for h in hs]
                image = set(values)
                reverse = [
                    g for g in gs
                    if mul(g, a, n, m, m, p) == mul(b, g, n, n, m, p)
                ]
                kernel_size = values.count((0,) * (m * n))
                assert len(image) * len(reverse) == p ** (m * n)
                assert kernel_size == len(reverse)
                columns = [
                    delta(a, b, tuple(int(i == j) for i in range(m * n)), m, n, p)
                    for j in range(m * n)
                ]
                linear_matrix = tuple(
                    columns[j][i] for i in range(m * n) for j in range(m * n)
                )
                assert det(linear_matrix, m * n, p) == resultant(
                    charpoly(a, m, p), charpoly(b, n, p), p
                )
                counts["resultant_identities"] += 1
                for c in hs:
                    trace_vanishing = all(trace_pair(g, c, m, n, p) == 0 for g in reverse)
                    assert (c in image) == trace_vanishing
                    number_of_graphs = values.count(scale(-1, c, p))
                    assert number_of_graphs == (kernel_size if trace_vanishing else 0)
                    counts["extension_blocks"] += 1
                counts["endpoint_pairs"] += 1


bezout_cases = 0
for p in (2, 3, 5):
    zeros = (0, 0, 0, 0)
    identity = (1, 0, 0, 1)
    nilpotents = [n for n in matrices(2, 2, p) if mul(n, n, 2, 2, 2, p) == zeros]
    basis = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    for n in nilpotents:
        for m in nilpotents:
            b = add(identity, m, p)

            def inverse(d):
                nd = mul(n, d, 2, 2, 2, p)
                dm = mul(d, m, 2, 2, 2, p)
                ndm = mul(nd, m, 2, 2, 2, p)
                return add(add(scale(-1, d, p), scale(-1, nd, p), p),
                           add(dm, scale(2, ndm, p), p), p)

            for d in basis:
                assert delta(n, b, inverse(d), 2, 2, p) == d
                assert inverse(delta(n, b, d, 2, 2, p)) == d
                bezout_cases += 1

counts["square_zero_bezout_basis_cases"] = bezout_cases
counts["status"] = "pass"
print(json.dumps(counts, indent=2))
