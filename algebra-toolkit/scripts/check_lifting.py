#!/usr/bin/env python3
"""Bounded exact regressions for the compression/common-lift chapter."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
from math import comb
from pathlib import Path
import argparse
import json


def convolution(a, b):
    n = len(a)
    return tuple(sum(a[k] * b[(j-k) % n] for k in range(n))
                 for j in range(n))


def correlation(a):
    return convolution(a, (a[0],) + tuple(reversed(a[1:])))


def compress(x, d):
    return tuple(sum(x[j] for j in range(s, len(x), d)) for s in range(d))


def symmetric_rows(n):
    for half in product((-1, 1), repeat=(n-1)//2):
        yield (1,) + half + tuple(reversed(half))


def lift_count(y, r):
    d = len(y)
    if any(y[s] != y[-s] for s in range(d)):
        return 0
    if (r-y[0]) % 4 or not 0 <= (r-y[0])//4 <= (r-1)//2:
        return 0
    count = comb((r-1)//2, (r-y[0])//4)
    for s in range(1, (d+1)//2):
        if abs(y[s]) > r or (r-y[s]) % 2:
            return 0
        count *= comb(r, (r-y[s])//2)
    return count


def main(output=None):
    checks = []
    # Enumerate single rows at fixed small orders, never four-row searches.
    fibers_checked = 0
    for n in (1, 3, 5, 9, 15):
        for d in range(1, n+1):
            if n % d:
                continue
            counts = Counter(compress(x, d) for x in symmetric_rows(n))
            for y, number in counts.items():
                assert lift_count(y, n//d) == number
                fibers_checked += 1
            assert sum(counts.values()) == 2**((n-1)//2)
    assert lift_count((-5,), 5) == 0
    assert lift_count((-3,), 5) == 1
    assert lift_count((1,), 5) == 2
    assert lift_count((1, 1, -1), 1) == 0
    checks.append({"name": "individual_lift_counts", "compressed_rows": fibers_checked,
                   "orders": [1, 3, 5, 9, 15]})

    # Rational arithmetic also checks even sizes: the real-algebra split
    # itself has no oddness hypothesis.
    projector_cases = 0
    for m, d in ((1, 1), (4, 1), (4, 2), (9, 3), (15, 5), (5, 5)):
        r = m//d
        e = tuple(Fraction(1, r) if j % d == 0 else Fraction(0)
                  for j in range(m))
        assert convolution(e, e) == e
        assert compress(e, d) == (1,) + (0,)*(d-1)
        x = tuple((3*j*j + 2*j + 1) % 11 - 5 for j in range(m))
        y = compress(x, d)
        low = convolution(e, x)
        high = tuple(xj-lj for xj, lj in zip(x, low))
        assert low == tuple(Fraction(y[j % d], r) for j in range(m))
        assert compress(high, d) == (0,)*d
        assert convolution(low, high) == (0,)*m
        assert sum(a*b for a, b in zip(low, high)) == 0
        assert sum(a*a for a in low) == Fraction(sum(a*a for a in y), r)
        assert sum(a*a for a in x) == sum(a*a for a in low+high)
        projector_cases += 1
    checks.append({"name": "rational_orthogonal_projector",
                   "cases": projector_cases})

    target = ((-1, -1, -1), (-1, 1, 1), (-1, 3, 3), (3, -1, -1))
    rows = list(symmetric_rows(9))
    lifts = [[x for x in rows if compress(x, 3) == y] for y in target]
    assert list(map(len, lifts)) == [3, 3, 1, 3]
    assert tuple(sum(correlation(y)[j] for y in target)
                 for j in range(3)) == (36, 0, 0)
    survived = []
    all_count = 0
    for quad in product(*lifts):
        all_count += 1
        gram = tuple(sum(correlation(x)[j] for x in quad) for j in range(9))
        assert gram != (36,) + (0,)*8
        colprod = [quad[0][j]*quad[1][j]*quad[2][j]*quad[3][j]
                   for j in range(1, 9)]
        if colprod != [-1]*8:
            continue
        a, b, c, d = quad
        p = next(j for j in (1, 2, 4) if a[j] == 1)
        q = next(j for j in (1, 2, 4) if d[j] == 1)
        k = next(j for j in (1, 2, 4) if b[j] == -1)
        assert {p, q, k} == {1, 2, 4}
        expected = tuple(36 if j == 0 else
                         8 if j in (p, 9-p) else
                         -8 if j in (k, 9-k) else 0 for j in range(9))
        assert gram == expected
        defect = (gram[0]-36,) + gram[1:]
        assert compress(defect, 3) == (0, 0, 0)
        survived.append({"p": p, "q": q, "k": k, "gram": gram})
    assert all_count == 27 and len(survived) == 6
    assert {(v["p"], v["q"], v["k"]) for v in survived} == set(permutations((1,2,4)))
    checks.append({"name": "fixed_core_nine_residual", "labelled_lifts": 27,
                   "product_survivors": 6, "full_solutions": 0,
                   "surviving_defects": survived})

    # Real Gram lift in a case where 2 sqrt(m) is rational.
    # m=9, so no approximate arithmetic or numerical tolerance is used.
    e = tuple(Fraction(1, 3) if j % 3 == 0 else Fraction(0) for j in range(9))
    one_minus_e = tuple((1 if j == 0 else 0)-e[j] for j in range(9))
    low = [tuple(Fraction(y[j % 3], 3) for j in range(9)) for y in target]
    real = [tuple(l[j] + (6*one_minus_e[j] if i == 0 else 0)
                  for j in range(9)) for i, l in enumerate(low)]
    assert [compress(x, 3) for x in real] == list(target)
    assert tuple(sum(correlation(x)[j] for x in real)
                 for j in range(9)) == (36,) + (0,)*8
    assert any(v not in (-1, 1) for x in real for v in x)
    checks.append({"name": "unrestricted_real_lift", "order": 9,
                   "preserves_compression_and_full_gram": True,
                   "is_sign_lift": False})

    result = {"status": "pass", "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "scope": "Fixed exact regressions, not formal verification or an existence search.",
              "checks": checks}
    if output:
        output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    main(parser.parse_args().output)
