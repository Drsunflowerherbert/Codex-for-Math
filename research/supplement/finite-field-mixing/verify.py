#!/usr/bin/env python3
"""Original standard-library exact checks for finite-field product-sum mixing.

No floating-point arithmetic, external package, downloaded program, or proof
assistant is used. The assertions check finite cases; study.md supplies proofs.
Run: python verify.py [--quick] [--output certificates.json]
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


def prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, int_sqrt(n) + 1))


def int_sqrt(n: int) -> int:
    # Integer-only binary search; no approximate root enters any threshold.
    lo, hi = 0, n + 1
    while hi - lo > 1:
        m = (lo + hi) // 2
        if m * m <= n:
            lo = m
        else:
            hi = m
    return lo


def subsets(p: int):
    for mask in range(1, 1 << p):
        yield tuple(x for x in range(p) if mask & (1 << x))


def product_counts(p: int, A, B):
    out = [0] * p
    for a in A:
        for b in B:
            out[(a * b) % p] += 1
    return out


def convolve(p: int, f, g):
    out = [0] * p
    for i, x in enumerate(f):
        if x:
            for j, y in enumerate(g):
                if y:
                    out[(i + j) % p] += x * y
    return out


def powers(p: int, f, max_k: int):
    out = [1] + [0] * (p - 1)
    for k in range(1, max_k + 1):
        out = convolve(p, out, f)
        yield k, out


def criterion(p: int, N: int, k: int) -> bool:
    """Equivalent to (p-1)*(sqrt(p/N))**k < 1, without radicals."""
    return N**k > (p - 1) ** 2 * p**k


def check_count_bound(p: int, counts, M: int, k: int):
    """M = product_i |A_i||B_i| is the total number of tuples."""
    assert sum(counts) == M
    rhs = (p - 1) ** 2 * p**k * M
    for c in counts:
        assert (p * c - M) ** 2 <= rhs
    if M > (p - 1) ** 2 * p**k:
        assert all(c > 0 for c in counts)


def diagonal_suite(primes, max_k):
    report = []
    for p in primes:
        assert prime(p)
        checked, guaranteed = 0, [0] * max_k
        covered_without_criterion = [0] * max_k
        dense_four_checked, dense_four_min = 0, None
        threshold_h = next(h for h in range(1, p + 1) if h**4 >= p**3)
        minima_by_size = {}
        for H in subsets(p):
            h = len(H)
            N = h * h
            f = product_counts(p, H, H)
            checked += 1
            for k, counts in powers(p, f, max_k):
                check_count_bound(p, counts, N**k, k)
                if criterion(p, N, k):
                    guaranteed[k - 1] += 1
                    assert min(counts) > 0
                elif min(counts) > 0:
                    covered_without_criterion[k - 1] += 1
                if k == 4:
                    if h**4 >= p**3:
                        dense_four_checked += 1
                        assert p * p * min(counts) >= N**4
                        value = Fraction(min(counts), N**4)
                        if dense_four_min is None or value < dense_four_min:
                            dense_four_min = value
                    row = minima_by_size.setdefault(str(h), {"minimum_count": None})
                    if row["minimum_count"] is None or min(counts) < row["minimum_count"]:
                        row.update(minimum_count=min(counts), witness_H=list(H),
                                   first_minimum_residue=counts.index(min(counts)))
        report.append({
            "p": p, "nonempty_H_checked": checked,
            "k_values": list(range(1, max_k + 1)),
            "guaranteed_sets_by_k": guaranteed,
            "covering_sets_failing_sufficient_criterion_by_k": covered_without_criterion,
            "minimum_h_with_h4_ge_p3": threshold_h,
            "dense_four_sets_checked": dense_four_checked,
            "dense_four_minimum_probability": str(dense_four_min),
            "four_product_minima_by_size": minima_by_size,
        })
    return report


def rectangular_suite(primes, max_k):
    report = []
    for p in primes:
        sets = list(subsets(p))
        checked, guaranteed = 0, [0] * max_k
        for A in sets:
            for B in sets:
                N = len(A) * len(B)
                f = product_counts(p, A, B)
                checked += 1
                for k, counts in powers(p, f, max_k):
                    check_count_bound(p, counts, N**k, k)
                    if criterion(p, N, k):
                        guaranteed[k - 1] += 1
                    if k == 4 and N * N >= p**3:
                        assert p * p * min(counts) >= N**4
        report.append({"p": p, "ordered_nonempty_set_pairs_checked": checked,
                       "k_values": list(range(1, max_k + 1)),
                       "guaranteed_pairs_by_k": guaranteed})
    return report


def add(f, g):
    return [x + y for x, y in zip(f, g)]


def sub(f, g):
    return [x - y for x, y in zip(f, g)]


def scale(c, f):
    return [c * x for x in f]


def abs_square(p: int, f):
    # Laurent conjugation z -> z^-1 in Z[z]/(z^p-1).
    out = [0] * p
    for i, x in enumerate(f):
        for j, y in enumerate(f):
            out[(i - j) % p] += x * y
    return out


def cyclotomic_reduce(f):
    # Phi_p(z)=1+...+z^(p-1), for prime p.
    return tuple(x - f[-1] for x in f[:-1])


def bilinear_sos_suite(primes):
    """Verify the proof's sum-of-Hermitian-squares identity exactly."""
    report = []
    for p in primes:
        checked = 0
        sets = list(subsets(p))
        for A in sets:
            for B in sets:
                for r in range(1, p):
                    T = []
                    for x in range(p):
                        row = [0] * p
                        for b in B:
                            row[(r * x * b) % p] += 1
                        T.append(row)
                    S = [0] * p
                    for a in A:
                        S = add(S, T[a])
                    lhs = scale(-1, abs_square(p, S))
                    lhs[0] += p * len(A) * len(B)
                    rhs = [0] * p
                    for x in range(p):
                        if x not in A:
                            rhs = add(rhs, scale(len(A), abs_square(p, T[x])))
                    for i, a in enumerate(A):
                        for b in A[i + 1:]:
                            rhs = add(rhs, abs_square(p, sub(T[a], T[b])))
                    assert cyclotomic_reduce(lhs) == cyclotomic_reduce(rhs)
                    checked += 1
        report.append({"p": p, "identities_checked": checked,
                       "ring": "Z[z]/(1+z+...+z^(p-1))"})
    return report


def heterogeneous_suite():
    # Every ordered two- and three-pair sequence over the nonempty sets of F_3.
    p = 3
    sets = list(subsets(p))
    pairs = [(A, B, product_counts(p, A, B), len(A) * len(B))
             for A in sets for B in sets]
    totals = []
    for k in (2, 3):
        checked, guaranteed = 0, 0
        for sequence in product(pairs, repeat=k):
            counts, M = [1, 0, 0], 1
            for _, _, f, N in sequence:
                counts = convolve(p, counts, f)
                M *= N
            check_count_bound(p, counts, M, k)
            guaranteed += M > (p - 1)**2 * p**k
            checked += 1
        totals.append({"p": p, "number_of_pairs": k, "sequences_checked": checked,
                       "guaranteed_sequences": guaranteed})
    return totals


def direct_enumeration_crosscheck():
    tests = []
    for p, A, B, k in [(2, (0, 1), (0, 1), 4),
                        (3, (0, 1), (1, 2), 3),
                        (5, (0, 1, 2), (1, 3), 3),
                        (7, (1, 2, 3, 5, 6), (1, 2, 3, 5, 6), 3)]:
        pairs = list(product(A, B))
        direct = [0] * p
        for sequence in product(pairs, repeat=k):
            direct[sum(a * b for a, b in sequence) % p] += 1
        recurrence = list(powers(p, product_counts(p, A, B), k))[-1][1]
        assert direct == recurrence
        tests.append({"p": p, "A": list(A), "B": list(B), "k": k,
                      "counts": direct, "tuples": len(pairs)**k})
    return tests


def coefficient_shift_suite():
    rows = []
    for p in (2, 3, 5):
        k = 3
        pairs = [(tuple(x for x in range(p) if x != i % p), tuple(range(p)))
                 for i in range(k)]
        M = 1
        bases = []
        for A, B in pairs:
            M *= len(A) * len(B)
            bases.append(product_counts(p, A, B))
        checked = 0
        for coefficients in product(range(1, p), repeat=k):
            counts = [1] + [0] * (p - 1)
            for coefficient, base in zip(coefficients, bases):
                scaled = [0] * p
                for x, n in enumerate(base):
                    scaled[coefficient*x % p] += n
                counts = convolve(p, counts, scaled)
            for shift in range(p):
                shifted = [counts[(t-shift) % p] for t in range(p)]
                check_count_bound(p, shifted, M, k)
                checked += 1
        rows.append({"p": p, "pairs": pairs, "k": k,
                     "all_nonzero_coefficient_vectors_and_shifts_checked": checked,
                     "total_tuples_per_case": M})
    return rows


def examples_and_failures():
    # Composite modulus: the field-only bilinear bound and conclusion fail.
    p = 16
    H = tuple(range(0, p, 2))
    composite_counts = list(powers(p, product_counts(p, H, H), 4))[-1][1]
    assert len(H)**4 == p**3
    assert criterion(p, len(H)**2, 4)
    assert [x for x, n in enumerate(composite_counts) if n] == [0, 4, 8, 12]
    assert all((4 * a * b) % 16 == 0 for a in H for b in H)

    # Independence inside pairs cannot be replaced by uniform marginals.
    p = 5
    H = tuple(range(1, p))
    inverse_pairs = [(a, next(b for b in H if a * b % p == 1)) for a in H]
    assert sorted(b for _, b in inverse_pairs) == list(H)
    assert len(H)**4 >= p**3
    assert {sum(a*b for a,b in seq) % p
            for seq in product(inverse_pairs, repeat=4)} == {4}

    # Four identical copies of the same valid product in characteristic two.
    assert {4 * a*b % 2 for a in range(2) for b in range(2)} == {0}

    # Equality in the general strict criterion gives no positive guarantee.
    eq_counts = list(powers(2, product_counts(2, (0,), (0, 1)), 4))[-1][1]
    assert 2**4 == (2 - 1)**2 * 2**4
    assert eq_counts == [16, 0]

    # The sufficient cardinality condition is not a necessary condition.
    unnecessary = list(powers(5, product_counts(5, (0, 1), (0, 1)), 4))[-1][1]
    assert not criterion(5, 4, 4) and all(unnecessary)
    missing = list(powers(7, product_counts(7, (0, 1), (0, 1)), 4))[-1][1]
    assert [x for x, n in enumerate(missing) if not n] == [5, 6]

    # Nonuniform distributions with full support: violated bound, not coverage.
    weights = [Fraction(9, 10)] + [Fraction(1, 40)] * 4
    weighted_products = [Fraction(0)] * 5
    for a in range(5):
        for b in range(5):
            weighted_products[a*b % 5] += weights[a] * weights[b]
    assert weighted_products == [Fraction(99, 100)] + [Fraction(1, 400)] * 4
    phi = weighted_products[0] - weighted_products[1]
    assert phi == Fraction(79, 80) and phi*phi > Fraction(1, 5)

    # A positive-divisor lift with a genuinely nontrivial multiplier.
    P, p = 30, 7
    divisors = [d for d in range(1, P + 1) if P % d == 0]
    image = sorted({d % p for d in divisors})
    pairs = [(1, 1), (1, 1), (1, 2), (2, 5)]
    numerators = [a*b for a, b in pairs]
    assert len(image)**4 >= p**3
    assert all(a in divisors and b in divisors for a, b in pairs)
    assert all(P*P % e == 0 for e in numerators)
    assert sum(numerators) % p == 0
    t = sum(numerators) // p
    assert t == 2 and sum(Fraction(e, t) for e in numerators) == p

    return {
        "composite_modulus": {"modulus": 16, "H": list(range(0, 16, 2)),
                              "k": 4, "counts": composite_counts,
                              "nonzero_frequency_with_character_identically_one": 4},
        "dependent_within_pairs": {"p": 5, "pairs": inverse_pairs,
                                   "k": 4, "support_of_sum": [4]},
        "dependent_between_pairs": {"p": 2, "construction": "U_i=AB for all four i",
                                    "support_of_sum": [0]},
        "strict_boundary_failure": {"p": 2, "A": [0], "B": [0, 1],
                                    "k": 4, "counts": eq_counts},
        "criterion_not_necessary": {"p": 5, "H": [0, 1], "k": 4,
                                    "counts": unnecessary},
        "small_set_can_fail": {"p": 7, "H": [0, 1], "k": 4, "counts": missing},
        "nonuniform_full_support": {"p": 5, "marginal_weights": list(map(str, weights)),
                                    "product_weights": list(map(str, weighted_products)),
                                    "nontrivial_character_expectation": str(phi)},
        "positive_divisor_lift": {"P": P, "p": p, "positive_divisors": divisors,
                                  "H": image, "factor_pairs": pairs,
                                  "numerators": numerators, "multiplier": t,
                                  "sum_of_rational_summands": str(p)},
    }


def threshold_table():
    rows = []
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 101, 1009]:
        assert prime(p)
        row = {"p": p, "minimum_h_at_density_three_quarters":
               next(h for h in range(1, p + 1) if h**4 >= p**3)}
        for k in range(1, 7):
            row[f"minimum_h_for_{k}_product_criterion"] = next(
                (h for h in range(1, p + 1) if criterion(p, h*h, k)), None)
        rows.append(row)
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--output", default="certificates.json")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    source = here.parent / "catalog/sources/preprints_Short-Egyptian-fractions-September-25-2026_build_prescribed.tex"
    manifest = json.loads((here.parent / "catalog/source_manifest.json").read_text())
    source_hash = sha256(source.read_bytes()).hexdigest()
    expected = next(row["sha256"] for row in manifest["files"] if row["file"] == source.name)
    assert source_hash == expected
    result = {
        "status": "All exact arithmetic assertions passed; finite evidence, not a formal proof.",
        "original_code": True, "arithmetic": "integers and fractions.Fraction only",
        "run_mode": "quick" if args.quick else "full",
        "source_revision": manifest["revision"], "source_sha256": source_hash,
        "source_matches_catalog_manifest": True,
        "program_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "diagonal_exhaustive": diagonal_suite([2, 3, 5, 7] if args.quick else [2, 3, 5, 7, 11, 13, 17], 6),
        "rectangular_exhaustive": rectangular_suite([2, 3, 5] if args.quick else [2, 3, 5, 7], 6),
        "bilinear_sum_of_squares": bilinear_sos_suite([2, 3, 5]),
        "heterogeneous_exhaustive": heterogeneous_suite(),
        "nonzero_coefficients_and_shifts": coefficient_shift_suite(),
        "independent_direct_enumeration": direct_enumeration_crosscheck(),
        "examples_and_counterexamples": examples_and_failures(),
        "exact_threshold_table": threshold_table(),
        "scope": {"ordinary_proof": "study.md", "lean_compilation": False,
                  "native_MRS_import": False, "global_Egyptian_fraction_constant_audited": False},
    }
    destination = Path(args.output)
    if not destination.is_absolute():
        destination = here / destination
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"output": str(destination), "status": result["status"],
                      "diagonal_sets": sum(r["nonempty_H_checked"] for r in result["diagonal_exhaustive"]),
                      "rectangular_pairs": sum(r["ordered_nonempty_set_pairs_checked"] for r in result["rectangular_exhaustive"]),
                      "heterogeneous_sequences": sum(r["sequences_checked"] for r in result["heterogeneous_exhaustive"]),
                      "SOS_identities": sum(r["identities_checked"] for r in result["bilinear_sum_of_squares"])}))


if __name__ == "__main__":
    main()
