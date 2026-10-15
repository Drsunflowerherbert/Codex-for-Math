"""Adversarial tests for the exact rank-one classifier.

Run from this directory with ``python -m unittest -v test_classifier``.
No numerical tolerances or third-party packages are used.  The polynomial
substitution helpers below are independent of classifier.py.
"""

from fractions import Fraction
from math import comb
from pathlib import Path
import json
import random
import subprocess
import sys
import tempfile
import unittest

from classifier import classify, critical_series


def terms(poly):
    """Serialize a sparse rational polynomial in the public input format."""
    return [[i, j, str(c)] for (i, j), c in sorted(poly.items()) if c]


def polynomial(rows):
    out = {}
    for i, j, c in rows:
        out[i, j] = out.get((i, j), Fraction(0)) + Fraction(c)
    return {k: c for k, c in out.items() if c}


def multiply(left, right):
    out = {}
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            out[i + k, j + l] = out.get((i + k, j + l), Fraction(0)) + a * b
    return {k: c for k, c in out.items() if c}


def linear_power(a, b, n):
    return {(k, n - k): Fraction(comb(n, k)) * a**k * b**(n - k)
            for k in range(n + 1) if a**k * b**(n - k)}


def substitute(poly, matrix):
    """Return f(a*x+b*y,c*x+d*y), without classifier helpers."""
    (a, b), (c, d) = [[Fraction(v) for v in row] for row in matrix]
    out = {}
    for (i, j), coefficient in poly.items():
        monomial = multiply(linear_power(a, b, i), linear_power(c, d, j))
        for key, value in monomial.items():
            out[key] = out.get(key, Fraction(0)) + coefficient * value
    return {k: c for k, c in out.items() if c}


def scale(poly, coefficient):
    return {key: Fraction(coefficient) * value for key, value in poly.items()
            if coefficient * value}


STRESS = {
    1: {(0, 2): Fraction(1), (2, 1): Fraction(-2),
        (4, 0): Fraction(1), (0, 4): Fraction(1)},
    -1: {(0, 2): Fraction(1), (2, 1): Fraction(-2),
         (4, 0): Fraction(1), (0, 4): Fraction(-1)},
}


class ClassificationTests(unittest.TestCase):
    def check_result(self, poly, classification, order=None, sigma=None, **options):
        result = classify(terms(poly), **options)
        self.assertEqual(result["classification"], classification)
        self.assertEqual(result["residual_order"], order)
        if sigma is not None:
            self.assertEqual(result["sigma"], sigma)
        if order is not None:
            self.assertFalse(result["residual_identically_zero"])
            self.assertNotEqual(Fraction(result["normalized_leading_coefficient"]), 0)
        return result

    def test_all_sign_parity_and_flat_cases(self):
        for sigma in (-1, 1):
            for power in (3, 4, 5, 6, 8, 12):
                for coefficient in (Fraction(-7, 3), Fraction(5, 11)):
                    with self.subTest(sigma=sigma, power=power, coefficient=coefficient):
                        poly = {(0, 2): Fraction(sigma),
                                (power, 0): sigma * coefficient}
                        if power % 2 or coefficient < 0:
                            expected = "saddle"
                        else:
                            expected = ("strict_local_minimum" if sigma > 0
                                        else "strict_local_maximum")
                        result = self.check_result(poly, expected, power, sigma)
                        self.assertEqual(Fraction(result["normalized_leading_coefficient"]),
                                         coefficient)
            expected = ("non_strict_local_minimum" if sigma > 0
                        else "non_strict_local_maximum")
            result = self.check_result({(0, 2): Fraction(3 * sigma, 7)},
                                       expected, sigma=sigma)
            self.assertTrue(result["residual_identically_zero"])
            self.assertIsNone(result["normalized_leading_coefficient"])

    def test_degree_four_stress_has_order_eight(self):
        for sign, poly in STRESS.items():
            with self.subTest(sign=sign):
                expected = "strict_local_minimum" if sign > 0 else "saddle"
                result = self.check_result(poly, expected, 8, 1)
                self.assertEqual(Fraction(result["normalized_leading_coefficient"]), sign)
                self.assertEqual(result["bound_order"], 10)
                reflected = self.check_result(scale(poly, -1),
                    "strict_local_maximum" if sign > 0 else "saddle", 8, -1)
                self.assertEqual(Fraction(reflected["normalized_leading_coefficient"]), sign)

    def test_stress_formal_series_to_order_eighteen(self):
        # Independently obtained by y - x^2 + 2*s*y^3 = 0.  In particular,
        # degree four does not justify inspecting only four Taylor terms.
        for sign, poly in STRESS.items():
            with self.subTest(sign=sign):
                phi, residual = critical_series(terms(poly), 18)
                self.assertEqual(len(phi), 19)
                self.assertEqual(len(residual), 19)
                expected_phi = {2: 1, 6: -2 * sign, 10: 12,
                                14: -96 * sign, 18: 880}
                expected_residual = {8: sign, 12: -4, 16: 24 * sign}
                self.assertEqual(phi, [Fraction(expected_phi.get(k, 0))
                                       for k in range(19)])
                self.assertEqual(residual, [Fraction(expected_residual.get(k, 0))
                                            for k in range(19)])
                self.assertTrue(all(isinstance(c, Fraction) for c in phi + residual))

    def test_cap_before_and_at_first_nonzero_term(self):
        for sign, poly in STRESS.items():
            with self.subTest(sign=sign):
                unresolved = self.check_result(poly, "unresolved", max_order=7)
                self.assertEqual(unresolved["computed_order"], 7)
                self.assertIsNone(unresolved["residual_identically_zero"])
                expected = "strict_local_minimum" if sign > 0 else "saddle"
                self.check_result(poly, expected, 8, max_order=8)
                sharp = self.check_result(poly, expected, 8, bound="ploski")
                self.assertEqual(sharp["bound_order"], 8)

    def test_partial_zero_jet_does_not_claim_an_extremum(self):
        for poly in ({(0, 2): Fraction(1)},
                     {(0, 2): Fraction(1), (18, 0): Fraction(-1)}):
            result = self.check_result(poly, "unresolved", max_order=1)
            self.assertIsNone(result["residual_identically_zero"])
        self.check_result({(0, 2): Fraction(1), (18, 0): Fraction(-1)},
                          "saddle", 18, max_order=18)

    def test_repeated_factor_is_non_strict(self):
        # Critical locus is the analytic curve y=x^2; it is not isolated.
        poly = {(0, 2): Fraction(1), (2, 1): Fraction(-2),
                (4, 0): Fraction(1)}
        for sigma in (-1, 1):
            expected = ("non_strict_local_minimum" if sigma > 0
                        else "non_strict_local_maximum")
            result = self.check_result(scale(poly, sigma), expected, sigma=sigma)
            self.assertTrue(result["residual_identically_zero"])

    def test_curved_valley_with_nonconstant_unit(self):
        # (y-x^2)^2*(1+x+2*y) has a positive analytic unit at the origin.
        square = {(0, 2): Fraction(1), (2, 1): Fraction(-2),
                  (4, 0): Fraction(1)}
        poly = multiply(square, {(0, 0): Fraction(1), (1, 0): Fraction(1),
                                 (0, 1): Fraction(2)})
        result = self.check_result(poly, "non_strict_local_minimum", sigma=1)
        self.assertTrue(result["residual_identically_zero"])

    def test_global_critical_component_does_not_prevent_local_isolation(self):
        # f=(1+x)^2*(y^2+x^3) has a whole critical line at x=-1,
        # while the origin is an isolated complex critical point.
        poly = multiply({(0, 0): Fraction(1), (1, 0): Fraction(2),
                         (2, 0): Fraction(1)},
                        {(0, 2): Fraction(1), (3, 0): Fraction(1)})
        result = self.check_result(poly, "saddle", 3)
        self.assertEqual(result["milnor_number"], 2)
        self.assertTrue(result["isolated_complex_critical_point"])

    def test_order_zero_series_is_an_exact_zero_jet(self):
        phi, residual = critical_series(terms(STRESS[1]), 0)
        self.assertEqual(phi, [Fraction(0)])
        self.assertEqual(residual, [Fraction(0)])

    def test_rational_linear_changes_and_sign_flips(self):
        matrices = [
            [[1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 1], [1, -1]],
            [[Fraction(1, 2), Fraction(2, 3)], [Fraction(-3, 5), Fraction(7, 4)]],
            [[1, 0], [Fraction(19, 7), -2]],
        ]
        cases = [({(0, 2): Fraction(1), (4, 0): Fraction(1)},
                  "strict_local_minimum", "strict_local_maximum", 4),
                 ({(0, 2): Fraction(1), (4, 0): Fraction(-1)},
                  "saddle", "saddle", 4),
                 ({(0, 2): Fraction(1), (5, 0): Fraction(1)},
                  "saddle", "saddle", 5),
                 ({(0, 2): Fraction(1)},
                  "non_strict_local_minimum", "non_strict_local_maximum", None)]
        generator = random.Random(20261015)
        while len(matrices) < 17:
            matrix = [[Fraction(generator.randint(-5, 5), generator.randint(1, 5))
                       for _ in range(2)] for _ in range(2)]
            if matrix[0][0] * matrix[1][1] != matrix[0][1] * matrix[1][0]:
                matrices.append(matrix)
        for matrix in matrices:
            for base, positive, negative, order in cases:
                for sigma, expected in ((1, positive), (-1, negative)):
                    with self.subTest(matrix=matrix, expected=expected, order=order):
                        poly = scale(substitute(base, matrix), sigma)
                        poly[0, 0] = Fraction(17, 13)
                        result = self.check_result(poly, expected, order, sigma)
                        # Matrix convention: original variables = A * normalized variables.
                        transformed = scale(substitute(poly, result["transform_matrix"]), sigma)
                        transformed.pop((0, 0), None)
                        self.assertEqual(polynomial(result["normalized_terms"]), transformed)
                        self.assertNotIn((2, 0), transformed)
                        self.assertNotIn((1, 1), transformed)
                        self.assertGreater(transformed[0, 2], 0)

    def test_duplicate_terms_and_exact_cancellation(self):
        result = classify([[0, 2, "1/3"], [0, 2, "2/3"], [4, 0, "9/7"],
                           [4, 0, "-9/7"], [0, 0, "-1000000000000000001/3"]])
        self.assertEqual(result["classification"], "non_strict_local_minimum")
        self.assertTrue(result["residual_identically_zero"])

    def test_example_catalog(self):
        path = Path(__file__).with_name("examples.json")
        data = json.loads(path.read_text())
        examples = data["examples"] if isinstance(data, dict) else data
        for example in examples:
            with self.subTest(example=example.get("id", example.get("name"))):
                result = classify(example["terms"])
                expected = example["expected"]
                self.assertEqual(result["classification"], expected["classification"])
                self.assertEqual(result["residual_order"], expected["residual_order"])
                if expected.get("normalized_leading_coefficient") is not None:
                    self.assertEqual(Fraction(result["normalized_leading_coefficient"]),
                                     Fraction(expected["normalized_leading_coefficient"]))
                sharp = classify(example["terms"], bound="ploski")
                for key in ("classification", "residual_order",
                            "normalized_leading_coefficient", "residual_identically_zero"):
                    self.assertEqual(sharp[key], result[key])

    def test_very_small_exact_coefficient_is_not_rounded_away(self):
        tiny = Fraction(-1, 10**300)
        result = self.check_result({(0, 2): Fraction(1), (4, 0): tiny}, "saddle", 4)
        self.assertEqual(Fraction(result["normalized_leading_coefficient"]), tiny)


class RejectedInputTests(unittest.TestCase):
    def test_stationarity_and_hessian_rank_are_required(self):
        bad = [[], [[0, 0, "1"]], [[1, 0, "1"], [0, 2, "1"]],
               [[0, 1, "1"], [0, 2, "1"]], [[4, 0, "1"]],
               [[2, 0, "1"], [0, 2, "1"]],
               [[2, 0, "1"], [0, 2, "-1"]]]
        for rows in bad:
            with self.subTest(rows=rows), self.assertRaises((ValueError, TypeError)):
                classify(rows)

    def test_float_and_invalid_exponents_are_rejected(self):
        for row in ([0, 2, 1.0], [-1, 2, "1"], [0.5, 2, "1"],
                    [0, -2, "1"], [0, "2", "1"], [True, 2, "1"],
                    [0, 2, True], [0, 2, "1/0"]):
            with self.subTest(row=row), self.assertRaises((ValueError, TypeError)):
                classify([[0, 2, "1"], row])

    def test_unknown_bound_and_invalid_cap_are_rejected(self):
        rows = [[0, 2, "1"]]
        for options in ({"bound": "degree"}, {"max_order": -1},
                        {"max_order": 3.5}):
            with self.subTest(options=options), self.assertRaises((ValueError, TypeError)):
                classify(rows, **options)

    def test_series_requires_normalized_terms_and_integer_order(self):
        for rows in ([[0, 2, "-1"]], [[2, 0, "1"]],
                     [[0, 2, "1"], [1, 1, "1"]],
                     [[0, 2, "1"], [0, 0, "1"]]):
            with self.subTest(rows=rows), self.assertRaises((ValueError, TypeError)):
                critical_series(rows, 8)
        for order in (-1, 1.5):
            with self.subTest(order=order), self.assertRaises((ValueError, TypeError)):
                critical_series([[0, 2, "1"]], order)


class CommandLineTests(unittest.TestCase):
    def test_exact_json_success_and_inexact_json_failure(self):
        script = Path(__file__).with_name("classifier.py")
        with tempfile.TemporaryDirectory(prefix="critical-points-cli-") as directory:
            path = Path(directory) / "polynomial.json"
            path.write_text(json.dumps({"terms": [[0, 2, "1"], [4, 0, "1/7"]]}))
            success = subprocess.run([sys.executable, str(script), str(path)],
                                     capture_output=True, text=True, check=False)
            self.assertEqual(success.returncode, 0, success.stderr)
            self.assertEqual(json.loads(success.stdout)["classification"], "strict_local_minimum")
            self.assertEqual(success.stderr, "")

            path.write_text(json.dumps({"terms": [[0, 2, 1.0]]}))
            failure = subprocess.run([sys.executable, str(script), str(path)],
                                     capture_output=True, text=True, check=False)
            self.assertEqual(failure.returncode, 2)
            self.assertEqual(failure.stdout, "")
            self.assertIn("floats are rejected", failure.stderr)
            self.assertNotIn("Traceback", failure.stderr)


if __name__ == "__main__":
    unittest.main()
