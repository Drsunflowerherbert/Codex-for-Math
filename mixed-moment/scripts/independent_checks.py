#!/usr/bin/env python3
"""Independent finite exact checks for the reviewed mixed-moment certificates.

Only the standard library is used.  This file never imports or executes the
reviewed implementation.  Triples are formal rational coordinates, not numbers
obtained by substituting values for G or zeta(2).  Finite checks are not proofs
of analytic identities, irrationality, independence, or Lean theorems.
"""
from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json
from math import comb, factorial
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = PROJECT.parent / "research/supplement"
ZERO = (Q(0), Q(0), Q(0))


class Audit:
    def __init__(self):
        self.counts = Counter()

    def check(self, category, condition, detail=""):
        if not condition:
            raise AssertionError(f"{category}: {detail}")
        self.counts[category] += 1

    def equal(self, category, actual, expected, detail=""):
        self.check(category, actual == expected,
                   f"{detail}: got {actual!r}, expected {expected!r}")


def encoded(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, (list, tuple)):
        return [encoded(x) for x in value]
    if isinstance(value, dict):
        return {str(k): encoded(v) for k, v in value.items()}
    return value


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(q, a):
    return tuple(Q(q) * x for x in a)


def sub(a, b):
    return add(a, scale(-1, b))


def natural(n, label):
    if type(n) is not int or n < 0:
        raise ValueError(f"{label} must be a nonnegative integer")


@lru_cache(None)
def moment(n):
    """Integrate 2*(1-u^2)^r as a polynomial; no binomial-denominator formula."""
    if n == -1:
        return Q(0)
    natural(n, "moment index (except the explicit -1 convention)")
    if n % 2:
        return Q(0)
    r = n // 2
    return 2 * sum((Q((-1)**k * comb(r, k), 2*k + 1)
                    for k in range(r + 1)), Q(0))


@lru_cache(None)
def kernel(n):
    """Solve (1-t^2)*C(t)^2=1, C(0)=1 coefficient by coefficient.

    The input is a SIGNED difference.  Negative indices must be zero; replacing
    them by natural-number truncated subtraction changes the mathematics.
    """
    if type(n) is not int:
        raise ValueError("kernel index must be an integer")
    if n < 0:
        return Q(0)
    if n == 0:
        return Q(1)
    previous_square = sum((kernel(k)*kernel(n-2-k)
                           for k in range(n-1)), Q(0))
    interior = sum((kernel(k)*kernel(n-k) for k in range(1, n)), Q(0))
    return (previous_square - interior)/2


@lru_cache(None)
def hstar(d):
    natural(d, "H-star index")
    result = Q(1)
    for n in range(2 if d % 2 == 0 else 3, d + 1, 2):
        result *= Q(n-1, n)
    return result


@lru_cache(None)
def minus_boundary(d):
    """Closed finite sums, independent of the source's recursive evaluator."""
    natural(d, "minus boundary index")
    if d % 2:
        rational = hstar(d)*sum((Q(2, k) for k in range(1, d+1, 2)), Q(0))
    else:
        rational = hstar(d)*sum((Q(2, k*k)/hstar(k)**2
                                 for k in range(2, d+1, 2)), Q(0))
    return (rational, 4*kernel(d), Q(0))


@lru_cache(None)
def plus_boundary(d):
    natural(d, "plus boundary index")
    if d == 0:
        return (Q(0), Q(4), Q(0))
    u = d-1
    rational = hstar(u)*sum((Q(2, k*k)/hstar(k)
                            for k in range(1, u+1) if (u-k) % 2 == 0), Q(0))
    return (rational, Q(0), Q(3, 2)*kernel(d-1))


@lru_cache(None)
def mixed(i, j):
    """Fill diagonals from boundaries; no source piecewise finite-sum code."""
    natural(i, "M first index")
    natural(j, "M second index")
    if j == 0:
        return minus_boundary(i)
    if i == 0:
        return plus_boundary(j)
    return sub(mixed(i-1, j-1), (moment(i-1)/j, Q(0), Q(0)))


@lru_cache(None)
def zed(i, j):
    """Cancel the common part of the harmonic sums before rational summation."""
    natural(i, "Z first index")
    natural(j, "Z second index")
    if i == j:
        return (-sum((Q(1, k*k) for k in range(1, i+1)), Q(0)), Q(0), Q(1))
    lo, hi = sorted((i, j))
    return (sum((Q(1, k*(hi-lo)) for k in range(lo+1, hi+1)), Q(0)), Q(0), Q(0))


def contact_product(polynomial, length):
    """Ordinary truncated polynomial multiplication t*P*C, not a defect call."""
    natural(length, "contact length")
    result = [Q(0)]*length
    for i, p in enumerate(polynomial):
        for k in range(max(0, length-i-1)):
            result[i+k+1] += Q(p)*kernel(k)
    return result


def entry(polynomial, correction, j, multiplier=Q(3, 2)):
    natural(j, "entry index")
    result = ZERO
    for i, p in enumerate(polynomial):
        result = add(result, scale(p, mixed(i, j)))
    for i, d in enumerate(correction):
        result = sub(result, scale(Q(multiplier)*Q(d), zed(i, j)))
    return result


def series_data(i, j, terms):
    natural(i, "series first index")
    natural(j, "series second index")
    if type(terms) is not int or terms < 1:
        raise ValueError("series term count must be positive")
    partial = sum((moment(i+u)/Q(j+u+1) for u in range(terms)), Q(0))
    start = i+terms
    multiplier = max(Q(1), Q(start, j+terms+1))
    return partial, multiplier*(moment(start-2)+moment(start-1))


def validate_saved(data, audit):
    """Check all numerical fields in the saved certificate, preserving shape."""
    audit.equal("saved_triple_order", data["triple_order"], ["rational", "G", "zeta(2)"])
    audit.equal("saved_moment_count", len(data["m_0_through_16"]), 17)
    for n, actual in enumerate(data["m_0_through_16"]):
        audit.equal("saved_moment", actual, str(moment(n)), f"m[{n}]")
    audit.equal("saved_boundary_count", len(data["rational_boundaries_0_through_16"]), 17)
    for d, actual in enumerate(data["rational_boundaries_0_through_16"]):
        expected = {"d": d, "k_minus": str(minus_boundary(d)[0]),
                    "k_plus": str(plus_boundary(d)[0])}
        audit.equal("saved_boundary", actual, expected, f"boundary[{d}]")
    for label, function in (("M", mixed), ("Z", zed)):
        table = data[f"{label}_0_through_6"]
        audit.equal("saved_table_shape", len(table), 7, label)
        for i, row in enumerate(table):
            audit.equal("saved_table_shape", len(row), 7, f"{label}[{i}]")
            for j, triple in enumerate(row):
                audit.equal(f"saved_{label}_triple", triple, encoded(function(i, j)), f"{i},{j}")
    audit.equal("saved_example_count", len(data["contact_examples"]), 6)
    for index, example in enumerate(data["contact_examples"]):
        polynomial = list(map(Q, example["P_coefficients_low_to_high"]))
        correction = list(map(Q, example["D_coefficients_low_to_high"]))
        length = example["L"]
        audit.equal("saved_contact_polynomial", correction, contact_product(polynomial, length), str(index))
        audit.equal("saved_contact_row_count", len(example["entries"]), length+2)
        product_coefficients = contact_product(polynomial, length+2)
        for j, row in enumerate(example["entries"]):
            defect = product_coefficients[j] - (correction[j] if j < len(correction) else Q(0))
            expected = {"j": j, "entry_coefficients_1_G_zeta2": encoded(entry(polynomial, correction, j)),
                        "Taylor_defect_coefficient": str(defect)}
            audit.equal("saved_contact_entry", row, expected, f"example {index}, j={j}")
    audit.equal("saved_formal_failure_count", len(data["formal_non_cancellation_examples"]), 3)
    for example in data["formal_non_cancellation_examples"]:
        expected = entry(list(map(Q, example["P"])), list(map(Q, example["D"])),
                         example["j"], Q(example.get("multiplier", "3/2")))
        audit.equal("saved_formal_failure", example["entry"], encoded(expected), example["name"])
    audit.equal("saved_series_count", len(data["exact_series_enclosures"]), 6)
    for example in data["exact_series_enclosures"]:
        partial, upper = series_data(example["i"], example["j"], example["terms"])
        audit.equal("saved_series_partial", example["partial_sum"], str(partial))
        audit.equal("saved_series_lower", example["tail_lower"], "0")
        audit.equal("saved_series_upper", example["tail_upper"], str(upper))


def run(source=DEFAULT_SOURCE):
    audit = Audit()
    data = json.loads((Path(source)/"mixed-moments/certificates.json").read_text())
    validate_saved(data, audit)

    # Distinct formulas are cross-checked without importing the supplied code.
    for n in range(201):
        closed_kernel = Q(factorial(n), 4**(n//2)*factorial(n//2)**2) if n % 2 == 0 else Q(0)
        audit.equal("formal_sqrt_vs_factorials", kernel(n), closed_kernel, str(n))
        if n >= 1:
            audit.equal("moment_recurrence", (n+1)*moment(n), n*moment(n-2), str(n))
        audit.check("moment_nonnegative", moment(n) >= 0, str(n))
    for n in range(-100, 0):
        audit.equal("signed_negative_kernel", kernel(n), Q(0), str(n))
    for d in range(2, 101):
        audit.equal("minus_boundary_recurrence", scale(d, minus_boundary(d)),
                    add(scale(d-1, minus_boundary(d-2)), (moment(d-2)+moment(d-1), Q(0), Q(0))), str(d))
        audit.equal("plus_boundary_recurrence", scale(d-1, plus_boundary(d)),
                    add(scale(d-2, plus_boundary(d-2)), (Q(2, d-1), Q(0), Q(0))), str(d))
    for i in range(25):
        for j in range(25):
            audit.equal("M_signed_difference_coefficients", mixed(i, j)[1:],
                        (4*kernel(i-j), Q(3, 2)*kernel(j-i-1)), f"{i},{j}")
            audit.equal("Z_symmetry", zed(i, j), zed(j, i), f"{i},{j}")
            for terms in (1, 2, 5, 10):
                partial, upper = series_data(i, j, terms)
                audit.equal("M_finite_telescope", sub(mixed(i, j), mixed(i+terms, j+terms)),
                            (partial, Q(0), Q(0)), f"{i},{j},{terms}")
                finite_z = sum((Q(1, (i+u+1)*(j+u+1)) for u in range(terms)), Q(0))
                audit.equal("Z_finite_telescope", sub(zed(i, j), zed(i+terms, j+terms)),
                            (finite_z, Q(0), Q(0)), f"{i},{j},{terms}")
                # A finite block below a candidate bound is a finite check only.
                block = sum((moment(i+u)/Q(j+u+1) for u in range(terms, terms+32)), Q(0))
                audit.check("finite_tail_block_below_bound", Q(0) <= block <= upper, f"{i},{j},{terms}")
    for i in range(1, 101):
        audit.equal("adjacent_diagonal", mixed(i, i-1), (moment(i-2)+moment(i-1), Q(0), Q(0)), str(i))

    for polynomial in product((-1, 0, 1), repeat=4):
        coefficients = contact_product(polynomial, 10)
        for length in range(1, 9):
            correction = contact_product(polynomial, length)
            for j in range(10):
                defect = coefficients[j] - (correction[j] if j < length else Q(0))
                result = entry(polynomial, correction, j)
                audit.equal("bounded_polynomial_defect", result[2], Q(3, 2)*defect)
                if j < length:
                    audit.equal("bounded_strict_contact", result[2], Q(0))
            perturbed = correction.copy()
            perturbed[length-1] += 1
            audit.equal("bounded_contact_perturbation", entry(polynomial, perturbed, length-1)[2], Q(-3, 2))

    rational_polynomial = [Q(1), Q(2, 3), Q(0), Q(-5, 7)]
    rational_correction = contact_product(rational_polynomial, 9)
    examples = {
        "M_0_1": mixed(0, 1), "M_1_0": mixed(1, 0), "M_2_0": mixed(2, 0),
        "Z_0_1": zed(0, 1), "Z_2_2": zed(2, 2),
        "P_1_D_t_L_3_entries_j_0_through_3": [entry([1], [0, 1], j) for j in range(4)],
        "rational_polynomial": rational_polynomial,
        "rational_contact_polynomial_L_9": rational_correction,
        "rational_entries_j_0_through_10": [entry(rational_polynomial, rational_correction, j) for j in range(11)],
    }
    adversarial = []
    # Wrong natural subtraction creates a false constant-term contribution.
    for i, j, coordinate, coefficient, signed in ((0, 1, "G", Q(4), -1),
                                                 (1, 0, "zeta(2)", Q(3, 2), -2)):
        correct = coefficient*kernel(signed)
        broken = coefficient*kernel(max(0, signed))
        audit.check("adversarial_negative_difference", correct != broken)
        adversarial.append({"name": "negative_difference_"+coordinate, "i": i, "j": j,
                            "signed_difference": signed, "correct_coordinate": correct,
                            "truncated_subtraction_coordinate": broken})
    for length in range(1, 17):
        polynomial = [0]*(length-1)+[1]
        audit.equal("endpoint_contact_holds_below_L", contact_product(polynomial, length), [Q(0)]*length)
        audit.equal("endpoint_j_equals_L_fails", entry(polynomial, [], length)[2], Q(3, 2))
    adversarial.append({"name": "strict_range", "P": [1], "D": [], "L": 1,
                        "valid_j_0": entry([1], [], 0), "excluded_j_1": entry([1], [], 1)})
    audit.equal("missing_contact_failure", entry([0], [1], 0), (Q(0), Q(0), Q(-3, 2)))
    audit.equal("missing_initial_t_failure", entry([1], [1], 0), (Q(0), Q(4), Q(-3, 2)))
    audit.equal("wrong_multiplier_failure", entry([1], [0, 1], 1, Q(1)), (Q(1), Q(0), Q(1, 2)))
    adversarial.extend([
        {"name": "missing_contact", "formal_entry": entry([0], [1], 0)},
        {"name": "missing_initial_t", "formal_entry": entry([1], [1], 0)},
        {"name": "wrong_multiplier", "formal_entry": entry([1], [0, 1], 1, Q(1))},
    ])
    # Pure linear algebra: quotient identifies the formal labels zeta2 and G.
    # This is a countermodel to an inference rule, NOT a relation among real constants.
    formal = (Q(0), Q(0), Q(-3, 2))
    represented_without_third = (Q(0), Q(-3, 2), Q(0))
    quotient = lambda vector: (vector[0], vector[1]+vector[2])
    audit.check("nonzero_coordinate_not_nonmembership", formal[2] != 0 and
                quotient(formal) == quotient(represented_without_third))
    adversarial.append({"name": "formal_coordinate_is_not_nonmembership",
                        "nonzero_third_coordinate_vector": formal,
                        "same_class_vector_with_zero_third_coordinate": represented_without_third,
                        "quotient_map": "(a,b,c) -> (a,b+c)",
                        "scope": "Abstract quotient-space countermodel only; no relation among actual G and zeta(2) is asserted."})

    for function, args in ((moment, (-2,)), (mixed, (-1, 0)), (mixed, (0, -1)),
                           (zed, (-1, 0)), (hstar, (-1,)), (series_data, (0, 0, 0))):
        try:
            function(*args)
        except ValueError:
            audit.check("invalid_domain_rejected", True)
        else:
            raise AssertionError(f"invalid domain accepted: {function.__name__}{args}")

    # Verify that our saved-certificate validator actually rejects corrupted data.
    mutations = [
        ("negative_difference_G", lambda d: d["M_0_through_6"][0][1].__setitem__(1, "4")),
        ("negative_difference_zeta2", lambda d: d["M_0_through_6"][1][0].__setitem__(2, "3/2")),
        ("rational_sign", lambda d: d["Z_0_through_6"][0][1].__setitem__(0, "-1")),
        ("excluded_endpoint", lambda d: d["contact_examples"][0]["entries"][1]["entry_coefficients_1_G_zeta2"].__setitem__(2, "0")),
        ("wrong_tail_bound", lambda d: d["exact_series_enclosures"][0].__setitem__("tail_upper", "0")),
        ("changed_contact", lambda d: d["contact_examples"][0]["D_coefficients_low_to_high"].__setitem__(0, "1")),
        ("missing_table_row", lambda d: d["M_0_through_6"].pop()),
    ]
    mutation_results = []
    for name, mutate in mutations:
        changed = deepcopy(data)
        mutate(changed)
        try:
            validate_saved(changed, Audit())
        except AssertionError as exc:
            audit.check("corrupted_certificate_rejected", True)
            mutation_results.append({"mutation": name, "rejected": True, "reason": str(exc)})
        else:
            raise AssertionError(f"corrupted certificate accepted: {name}")

    return encoded({
        "schema_version": 1, "status": "passed", "arithmetic": "Python stdlib fractions.Fraction only",
        "source_implementation_imported_or_executed": False,
        "methods": {"moment": "finite polynomial integration after u=sqrt(1-t^2)",
                    "kernel": "solve (1-t^2)C^2=1 coefficientwise with C(0)=1",
                    "boundaries": "closed finite sums with product-defined H-star",
                    "M": "diagonal dynamic programming from boundary triples",
                    "Z": "finite interval sum after common harmonic terms cancel",
                    "contact": "truncated polynomial convolution t*P*C"},
        "bounds": {"moments": [0, 200], "kernel": [-100, 200], "boundary_recurrences": [2, 100],
                   "grid_i_j": [0, 24], "finite_telescope_lengths": [1, 2, 5, 10],
                   "tail_block_length": 32, "polynomial_coefficients": [-1, 0, 1],
                   "polynomial_coefficient_count": 4, "polynomial_contact_orders": [1, 8],
                   "polynomial_entry_indices": [0, 9], "sharp_endpoint_family_L": [1, 16]},
        "check_counts": dict(sorted(audit.counts.items())), "total_checks": sum(audit.counts.values()),
        "rational_examples": examples, "adversarial_examples": adversarial,
        "mutation_tests": mutation_results,
        "limits": ["Finite algebraic checks, not universal proofs.",
                   "Saved series bounds are recomputed and finite tail blocks checked; infinite-tail validity remains analytic.",
                   "No numerical substitutions for G or zeta(2).",
                   "No integral identities, irrationality, linear independence, nonmembership, or Lean verification are established here."]})


def lean_cases():
    """Exact expectations for a separate Lean checker; Python grants no Lean status."""
    return encoded({
        "schema_version": 1,
        "status": "Python exact expectations; Lean verification is a separate step",
        "triple_order": ["rational", "G", "zeta(2)"],
        "M": [{"i": i, "j": j, "triple": mixed(i, j)} for i in range(6) for j in range(6)],
        "Z": [{"i": i, "j": j, "triple": zed(i, j)} for i in range(6) for j in range(6)],
        "P_1_D_t": [{"j": j, "triple": entry([1], [0, 1], j)} for j in range(5)],
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=PROJECT/"logs/certificates-independent.json")
    parser.add_argument("--lean-cases", type=Path, help="Also write rational expectations for separate Lean checks")
    args = parser.parse_args()
    report = run(args.source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    if args.lean_cases:
        args.lean_cases.parent.mkdir(parents=True, exist_ok=True)
        args.lean_cases.write_text(json.dumps(lean_cases(), indent=2)+"\n")
    print(json.dumps({"status": report["status"], "total_checks": report["total_checks"],
                      "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
