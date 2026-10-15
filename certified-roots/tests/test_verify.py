"""Independent adversarial and arithmetic checks for the exact certificate verifier.

Run from the repository root:
    python3 -m unittest discover -s certified-roots/tests -v

These finite tests exercise implementation failure modes; the mathematical proof
in the study is the justification for the verifier's universal enclosure claims.
Only the standard library is used, including Fraction for all test arithmetic.
"""

from copy import deepcopy
from fractions import Fraction
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("certified_roots_verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = verify
SPEC.loader.exec_module(verify)


def term(coefficient, *powers):
    return {"coefficient": str(coefficient), "powers": list(powers)}


def certificate(polynomials=None, center=None, radii=None, preconditioner=None):
    """A boundary-root certificate F(x)=x-1 on [-1,1] by default."""
    center = ["0"] if center is None else center
    n = len(center)
    return {
        "schema_version": 1,
        "name": "test certificate",
        "variables": [f"x{i + 1}" for i in range(n)],
        "polynomials": [[term(1, 1), term(-1, 0)]] if polynomials is None else polynomials,
        "center": center,
        "radii": ["1"] * n if radii is None else radii,
        "preconditioner": (
            [["1" if i == j else "0" for j in range(n)] for i in range(n)]
            if preconditioner is None else preconditioner
        ),
    }


def as_fraction(value):
    # This parser is the independent standard-library rational implementation.
    return Fraction(value)


def parse_large_rational(value):
    """Independent decimal parser that avoids Python's int-string digit limit."""
    def parse_integer(digits):
        sign = -1 if digits.startswith("-") else 1
        digits = digits.lstrip("-")
        if not digits or not digits.isascii() or not digits.isdecimal():
            raise ValueError("not a decimal integer")
        result = 0
        for index in range(0, len(digits), 1000):
            chunk = digits[index:index + 1000]
            result = result * (10 ** len(chunk)) + int(chunk)
        return sign * result

    parts = value.split("/")
    if len(parts) == 1:
        return Fraction(parse_integer(parts[0]))
    if len(parts) != 2:
        raise ValueError("not a rational")
    return Fraction(parse_integer(parts[0]), parse_integer(parts[1]))


def inside(interval_json, value):
    return as_fraction(interval_json[0]) <= value <= as_fraction(interval_json[1])


class MathematicalPremisesTests(unittest.TestCase):
    def test_nonstrict_self_map_accepts_a_boundary_root(self):
        result = verify.analyze(certificate())
        self.assertTrue(result["certified"])
        self.assertTrue(result["self_map"])
        self.assertTrue(result["contraction"])
        self.assertEqual(as_fraction(result["q"]), 0)
        self.assertEqual([as_fraction(x) for x in result["selfmap_lhs"]], [1])
        self.assertEqual([as_fraction(x) for x in result["slack"]], [0])
        self.assertEqual(as_fraction(result["weighted_error_bound"]), 1)
        self.assertEqual([as_fraction(x) for x in result["coordinate_error_bounds"]], [1])

    def test_zero_lipschitz_constant_does_not_replace_self_map(self):
        data = certificate()
        data["polynomials"][0][1]["coefficient"] = "-2"
        result = verify.analyze(data)
        self.assertEqual(as_fraction(result["q"]), 0)
        self.assertTrue(result["contraction"])
        self.assertFalse(result["self_map"])
        self.assertFalse(result["certified"])
        self.assertIsNone(result["weighted_error_bound"])
        self.assertIsNone(result["coordinate_error_bounds"])

    def test_self_map_alone_does_not_certify_a_zero_polynomial(self):
        result = verify.analyze(certificate(polynomials=[[]]))
        self.assertTrue(result["self_map"])
        self.assertEqual(as_fraction(result["q"]), 1)
        self.assertFalse(result["contraction"])
        self.assertFalse(result["certified"])

    def test_q_equal_one_is_rejected_despite_a_unique_root(self):
        result = verify.analyze(certificate(polynomials=[[term(2, 1)]]))
        self.assertTrue(result["self_map"])
        self.assertEqual(as_fraction(result["q"]), 1)
        self.assertFalse(result["certified"])

    def test_q_just_below_one_uses_exact_rationals(self):
        denominator = 10 ** 60
        result = verify.analyze(certificate(polynomials=[[term(f"1/{denominator}", 1)]]))
        self.assertEqual(as_fraction(result["q"]), Fraction(denominator - 1, denominator))
        self.assertTrue(result["certified"])
        self.assertEqual(as_fraction(result["weighted_error_bound"]), 0)

    def test_zero_residual_at_singular_root_is_insufficient(self):
        result = verify.analyze(certificate(polynomials=[[term(1, 2)]]))
        self.assertEqual([as_fraction(x) for x in result["residual"]], [0])
        self.assertFalse(result["contraction"])
        self.assertFalse(result["certified"])

    def test_nonlinear_success_and_rigorous_error_bound(self):
        # F(x)=x^2-2, c=3/2, r=1/10, Y=1/3.
        # J(B)=[14/5,16/5], q=1/15, eta=5/6, bound=25/28.
        data = certificate(
            polynomials=[[term(1, 2), term(-2, 0)]],
            center=["3/2"], radii=["1/10"], preconditioner=[["1/3"]],
        )
        result = verify.analyze(data)
        self.assertTrue(result["certified"])
        self.assertEqual(as_fraction(result["q"]), Fraction(1, 15))
        self.assertEqual(as_fraction(result["eta"]), Fraction(5, 6))
        self.assertEqual(as_fraction(result["weighted_error_bound"]), Fraction(25, 28))
        self.assertEqual([as_fraction(x) for x in result["coordinate_error_bounds"]], [Fraction(5, 56)])
        # Exact endpoint signs locate sqrt(2), independently of interval code.
        self.assertLess(Fraction(7, 5) ** 2 - 2, 0)
        self.assertGreater(Fraction(8, 5) ** 2 - 2, 0)

    def test_weighted_unequal_radii_and_asymmetric_preconditioner(self):
        data = certificate(
            polynomials=[
                [term(2, 1, 0), term(1, 0, 1), term("-1/2", 0, 0)],
                [term(1, 0, 1), term("-1/2", 0, 0)],
            ],
            center=["0", "0"], radii=["2", "1"],
            preconditioner=[["1/2", "-1/4"], ["0", "1/2"]],
        )
        result = verify.analyze(data)
        self.assertTrue(result["certified"])
        self.assertEqual(as_fraction(result["q"]), Fraction(1, 2))
        self.assertEqual(as_fraction(result["eta"]), Fraction(1, 4))
        self.assertEqual([as_fraction(x) for x in result["selfmap_lhs"]], [Fraction(3, 8), Fraction(3, 4)])
        self.assertEqual([as_fraction(x) for x in result["coordinate_error_bounds"]], [1, Fraction(1, 2)])

    def test_componentwise_self_map_is_stronger_than_scalar_shortcut(self):
        data = certificate(
            polynomials=[[term(1, 1, 0), term(-1, 0, 0)],
                         [term("1/10", 0, 1)]],
            center=["0", "0"],
        )
        result = verify.analyze(data)
        self.assertTrue(result["certified"])
        self.assertEqual(as_fraction(result["q"]), Fraction(9, 10))
        self.assertEqual(as_fraction(result["eta"]), 1)
        self.assertGreater(as_fraction(result["eta"]) + as_fraction(result["q"]), 1)
        self.assertEqual([as_fraction(x) for x in result["selfmap_lhs"]], [1, Fraction(9, 10)])
        self.assertEqual(as_fraction(result["weighted_error_bound"]), 10)
        # The box itself also bounds each coordinate's distance from its center.
        self.assertEqual([as_fraction(x) for x in result["coordinate_error_bounds"]], [1, 1])

    def test_tampered_polynomial_cannot_reuse_an_old_claim(self):
        original = certificate()
        self.assertTrue(verify.analyze(original)["certified"])
        altered = deepcopy(original)
        altered["polynomials"][0][1]["coefficient"] = "-7/3"
        self.assertFalse(verify.analyze(altered)["certified"])
        # A claimed q is not part of the certificate schema.
        altered["q"] = "0"
        with self.assertRaises(verify.ValidationError):
            verify.analyze(altered)

    def test_row_swap_invertible_preconditioner_is_accepted(self):
        data = certificate(
            polynomials=[[term(1, 0, 1), term(-1, 0, 0)],
                         [term(1, 1, 0), term(-1, 0, 0)]],
            center=["0", "0"],
            preconditioner=[["0", "1"], ["1", "0"]],
        )
        result = verify.analyze(data)
        self.assertTrue(result["certified"])
        self.assertEqual(as_fraction(result["q"]), 0)

    def test_duplicate_monomials_and_zero_coefficients_are_valid(self):
        data = certificate(
            polynomials=[[term(1, 1), term(1, 1), term(-2, 0), term(0, 32)]],
            preconditioner=[["1/2"]],
        )
        result = verify.analyze(data)
        self.assertTrue(result["certified"])
        self.assertEqual(as_fraction(result["q"]), 0)

    def test_repository_examples_have_the_documented_status(self):
        expected = {
            "circle-line.json": True,
            "circle-parabola.json": True,
            "tiny-residual-two-roots.json": False,
            "tiny-residual-no-root.json": False,
        }
        for name, certified in expected.items():
            with self.subTest(example=name):
                result = verify.analyze(verify.load_certificate(ROOT / "examples" / name))
                self.assertEqual(result["certified"], certified)
                if not certified:
                    self.assertEqual(as_fraction(result["q"]), Fraction(501, 500))


class IntervalArithmeticTests(unittest.TestCase):
    def test_negative_and_zero_crossing_power_endpoints(self):
        cases = [
            ((-3, -1), 2, (1, 9)), ((-3, -1), 3, (-27, -1)),
            ((-2, 3), 2, (0, 9)), ((-2, 3), 3, (-8, 27)),
            ((-2, 0), 4, (0, 16)), ((0, 0), 0, (1, 1)),
            ((-5, 7), 0, (1, 1)), ((0, 3), 1, (0, 3)),
        ]
        for endpoints, exponent, expected in cases:
            with self.subTest(endpoints=endpoints, exponent=exponent):
                value = verify.Interval(*endpoints) ** exponent
                self.assertEqual((value.lo, value.hi), expected)

    def test_rational_multiplication_and_subtraction_with_mixed_signs(self):
        left = verify.Interval(Fraction(-2, 3), Fraction(1, 5))
        right = verify.Interval(Fraction(-7, 4), Fraction(3, 2))
        product = left * right
        difference = left - right
        self.assertEqual((product.lo, product.hi), (Fraction(-1), Fraction(7, 6)))
        self.assertEqual((difference.lo, difference.hi), (Fraction(-13, 6), Fraction(39, 20)))
        self.assertEqual(left.abs_max(), Fraction(2, 3))
        self.assertEqual(((-left).lo, (-left).hi), (Fraction(-1, 5), Fraction(2, 3)))

    def test_operations_enclose_independent_fraction_samples(self):
        points = [Fraction(-3, 2), Fraction(-1, 2), Fraction(0), Fraction(1, 3), Fraction(5, 4)]
        intervals = [(a, b) for a in points for b in points if a <= b]
        for (a, b), (c, d) in itertools.product(intervals, repeat=2):
            left, right = verify.Interval(a, b), verify.Interval(c, d)
            sums, differences, products = left + right, left - right, left * right
            for x, y in itertools.product([a, (a + b) / 2, b], [c, (c + d) / 2, d]):
                self.assertLessEqual(sums.lo, x + y)
                self.assertGreaterEqual(sums.hi, x + y)
                self.assertLessEqual(differences.lo, x - y)
                self.assertGreaterEqual(differences.hi, x - y)
                self.assertLessEqual(products.lo, x * y)
                self.assertGreaterEqual(products.hi, x * y)

    def test_powers_enclose_independent_fraction_samples(self):
        for a, b in itertools.combinations_with_replacement(
            [Fraction(-3), Fraction(-1, 2), Fraction(0), Fraction(1, 3), Fraction(2)], 2
        ):
            for power in range(9):
                interval = verify.Interval(a, b) ** power
                for numerator in range(17):
                    sample = a + (b - a) * Fraction(numerator, 16)
                    self.assertLessEqual(interval.lo, sample ** power)
                    self.assertGreaterEqual(interval.hi, sample ** power)

    def test_invalid_intervals_and_exponents_are_rejected(self):
        for endpoints in [(1, -1), (True, 1), (0.0, 1), (0, float("inf"))]:
            with self.subTest(endpoints=endpoints):
                with self.assertRaises((ValueError, TypeError)):
                    verify.Interval(*endpoints)
        for power in [-1, True, 0.5]:
            with self.subTest(power=power):
                with self.assertRaises((ValueError, TypeError)):
                    verify.Interval(-1, 2) ** power

    def test_computed_jacobian_and_defect_enclose_exact_derivatives(self):
        data = certificate(
            polynomials=[
                [term(1, 2, 1), term(-3, 1, 2), term(2, 0, 0)],
                [term(1, 3, 0), term(-1, 0, 3), term(1, 1, 1)],
            ],
            center=["1/4", "-1/3"], radii=["3/4", "2/3"],
            preconditioner=[["1/2", "-1/3"], ["2/5", "1/4"]],
        )
        result = verify.analyze(data)
        y_matrix = [[Fraction(1, 2), Fraction(-1, 3)], [Fraction(2, 5), Fraction(1, 4)]]
        for x, y in itertools.product(
            [Fraction(-1, 2), Fraction(0), Fraction(1, 4), Fraction(1)],
            [Fraction(-1), Fraction(-1, 3), Fraction(0), Fraction(1, 3)],
        ):
            # Hand differentiated formulas; no verifier derivative helpers used.
            derivative = [[2 * x * y - 3 * y * y, x * x - 6 * x * y],
                          [3 * x * x + y, -3 * y * y + x]]
            for i, j in itertools.product(range(2), repeat=2):
                self.assertTrue(inside(result["J"][i][j], derivative[i][j]))
                defect = int(i == j) - sum(y_matrix[i][k] * derivative[k][j] for k in range(2))
                self.assertTrue(inside(result["E"][i][j], defect))


class InputValidationTests(unittest.TestCase):
    def test_missing_top_level_keys(self):
        for key in certificate():
            data = certificate()
            del data[key]
            with self.subTest(key=key), self.assertRaises(verify.ValidationError):
                verify.analyze(data)

    def test_unknown_or_forged_derived_fields(self):
        for key, value in {"q": "0", "J": [[["1", "1"]]], "jacobian": [],
                           "certified": True, "error_bound": "0"}.items():
            data = certificate()
            data[key] = value
            with self.subTest(key=key), self.assertRaises(verify.ValidationError):
                verify.analyze(data)

    def test_schema_version_is_exact_integer_one(self):
        for version in [True, False, 1.0, "1", 0, 2, None]:
            data = certificate()
            data["schema_version"] = version
            with self.subTest(version=version), self.assertRaises(verify.ValidationError):
                verify.analyze(data)

    def test_name_and_variable_types_and_duplicates(self):
        bad = []
        data = certificate(); data["name"] = 1; bad.append(data)
        data = certificate(); data["variables"] = [1]; bad.append(data)
        data = certificate(center=["0", "0"]); data["variables"] = ["x", "x"]; bad.append(data)
        for index, data in enumerate(bad):
            with self.subTest(case=index), self.assertRaises(verify.ValidationError):
                verify.analyze(data)

    def test_dimension_mismatches(self):
        bad = []
        for key in ["variables", "polynomials", "radii", "preconditioner"]:
            data = certificate(); data[key] = []; bad.append(data)
        data = certificate(); data["preconditioner"] = [["1", "0"]]; bad.append(data)
        data = certificate(); data["polynomials"][0][0]["powers"] = [1, 0]; bad.append(data)
        data = certificate(); data["center"] = ["0", "0"]; bad.append(data)
        for index, data in enumerate(bad):
            with self.subTest(case=index), self.assertRaises(verify.ValidationError):
                verify.analyze(data)

    def test_zero_dimension_is_rejected(self):
        with self.assertRaises(verify.ValidationError):
            verify.analyze(certificate(polynomials=[], center=[], radii=[], preconditioner=[]))

    def test_nonpositive_radii_are_rejected(self):
        for radius in ["0", "-0", "-1", "-1/1000"]:
            data = certificate(radii=[radius])
            with self.subTest(radius=radius), self.assertRaises(verify.ValidationError):
                verify.analyze(data)

    def test_singular_preconditioners_are_invalid(self):
        data = certificate(preconditioner=[["0"]])
        with self.assertRaises(verify.ValidationError):
            verify.analyze(data)
        # Every entry is nonzero; exact row dependence still makes Y singular.
        data = certificate(
            polynomials=[[term(1, 1, 0)], [term(1, 0, 1)]],
            center=["0", "0"],
            preconditioner=[["1/2", "2/3"], ["3/4", "1"]],
        )
        with self.assertRaises(verify.ValidationError):
            verify.analyze(data)

    def test_rationals_must_be_strings_not_float_bool_or_int(self):
        for value in [0, 1, True, False, 0.0, 0.1, float("nan"), float("inf"), None]:
            for field in ["center", "radii", "preconditioner", "coefficient"]:
                data = certificate()
                if field == "preconditioner":
                    data[field][0][0] = value
                elif field == "coefficient":
                    data["polynomials"][0][0][field] = value
                else:
                    data[field][0] = value
                with self.subTest(value=repr(value), field=field), self.assertRaises(verify.ValidationError):
                    verify.analyze(data)

    def test_noncanonical_rational_syntax_is_rejected(self):
        for value in ["1.0", "1e2", " 1", "1 ", "+1", "1/0", "1/-2", "NaN", "inf", "2/02", "1//2", ""]:
            data = certificate(center=[value])
            with self.subTest(value=value), self.assertRaises(verify.ValidationError):
                verify.analyze(data)

    def test_allowed_leading_numerator_zeros_remain_exact(self):
        data = certificate(center=["-00"], radii=["01"])
        data["polynomials"][0][0]["coefficient"] = "001/1"
        self.assertTrue(verify.analyze(data)["certified"])

    def test_invalid_exponents(self):
        for exponent in [-1, True, False, 1.0, "1", None]:
            data = certificate()
            data["polynomials"][0][0]["powers"] = [exponent]
            with self.subTest(exponent=exponent), self.assertRaises(verify.ValidationError):
                verify.analyze(data)

    def test_term_schema_is_strict(self):
        for new_term in [None, [], {"coefficient": "1"}, {"powers": [1]},
                         {"coefficient": "1", "powers": [1], "derivative": "1"}]:
            data = certificate(polynomials=[[new_term]])
            with self.subTest(term=new_term), self.assertRaises(verify.ValidationError):
                verify.analyze(data)

    def test_resource_limits_before_expensive_arithmetic(self):
        bad = []
        data = certificate(); data["polynomials"][0][0]["powers"] = [33]; bad.append(data)
        data = certificate(); data["polynomials"][0][0]["powers"] = [10 ** 9]; bad.append(data)
        data = certificate(); data["center"] = ["1" * 129]; bad.append(data)
        data = certificate(); data["center"] = ["1/" + "1" * 129]; bad.append(data)
        data = certificate(polynomials=[[term(0, 0)] * 257]); bad.append(data)
        data = certificate(polynomials=[[]] * 9, center=["0"] * 9); bad.append(data)
        data = certificate(polynomials=[[term(1, 16, 17)], []], center=["0", "0"]); bad.append(data)
        for index, data in enumerate(bad):
            with self.subTest(case=index), self.assertRaises(verify.ValidationError):
                verify.analyze(data)

    def test_resource_limits_allow_their_exact_boundary(self):
        data = certificate(polynomials=[[term(1, 1), term(-1, 0)] + [term(0, 32)] * 254])
        self.assertTrue(verify.analyze(data)["certified"])
        for center in ["1" * 128, "1/" + "1" * 128]:
            data = certificate(polynomials=[[term(1, 1), term("-" + center, 0)]], center=[center])
            self.assertTrue(verify.analyze(data)["certified"])
        data = certificate(polynomials=[[]] * 8, center=["0"] * 8)
        self.assertFalse(verify.analyze(data)["certified"])

    def test_valid_input_can_serialize_rationals_beyond_python_digit_limit(self):
        first, second = 10 ** 127 + 1, 10 ** 127 + 3
        data = certificate(
            polynomials=[[term(1, 32)]], center=[f"1/{first}"], radii=[f"1/{second}"],
        )
        result = verify.analyze(data)
        self.assertEqual(result["status"], "not_certified")
        self.assertFalse(result["certified"])
        endpoints = result["J"][0][0]
        self.assertTrue(all(isinstance(value, str) for value in endpoints))
        self.assertGreater(max(map(len, endpoints)), 4300)
        lower, upper = Fraction(1, first) - Fraction(1, second), Fraction(1, first) + Fraction(1, second)
        self.assertEqual(parse_large_rational(endpoints[0]), 32 * lower ** 31)
        self.assertEqual(parse_large_rational(endpoints[1]), 32 * upper ** 31)
        # JSON sees only strings, so serialization must not need numeric rounding.
        self.assertEqual(json.loads(json.dumps(result))["J"], result["J"])

    def test_non_object_top_level_values(self):
        for data in [None, [], 1, True, "certificate"]:
            with self.subTest(data=data), self.assertRaises(verify.ValidationError):
                verify.analyze(data)


class FileAndCommandLineTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.directory = Path(self.temporary.name)

    def tearDown(self):
        self.temporary.cleanup()

    def write(self, text, name="certificate.json"):
        path = self.directory / name
        path.write_text(text, encoding="utf-8")
        return path

    def cli(self, path):
        return subprocess.run([sys.executable, str(ROOT / "verify.py"), str(path)],
                              capture_output=True, text=True, check=False)

    def test_load_round_trip(self):
        data = certificate()
        loaded = verify.load_certificate(self.write(json.dumps(data)))
        self.assertEqual(loaded, data)
        self.assertTrue(verify.analyze(loaded)["certified"])

    def test_duplicate_json_keys_at_multiple_depths_are_rejected(self):
        serialized = json.dumps(certificate())
        duplicates = [
            serialized.replace('"schema_version": 1', '"schema_version": 1, "schema_version": 1', 1),
            serialized.replace('"coefficient": "1"', '"coefficient": "1", "coefficient": "2"', 1),
            '{"schema_version": 1, "schema_version": 2}',
        ]
        for index, content in enumerate(duplicates):
            with self.subTest(case=index), self.assertRaises(verify.ValidationError):
                verify.load_certificate(self.write(content))

    def test_json_nonfinite_and_floating_literals_are_rejected(self):
        serialized = json.dumps(certificate())
        for literal in ["NaN", "Infinity", "-Infinity", "0.0", "1e0"]:
            content = serialized.replace('"center": ["0"]', f'"center": [{literal}]', 1)
            with self.subTest(literal=literal), self.assertRaises(verify.ValidationError):
                verify.load_certificate(self.write(content))

    def test_malformed_json_invalid_utf8_and_missing_file(self):
        for content in ["{", "", '{"schema_version": 1} trailing']:
            with self.subTest(content=content), self.assertRaises(verify.ValidationError):
                verify.load_certificate(self.write(content))
        path = self.directory / "invalid-utf8.json"
        path.write_bytes(b"\xff")
        with self.assertRaises(verify.ValidationError):
            verify.load_certificate(path)
        with self.assertRaises(verify.ValidationError):
            verify.load_certificate(self.directory / "missing.json")

    def test_oversized_file_is_rejected(self):
        path = self.directory / "too-large.json"
        path.write_bytes(b" " * (1048576 + 1))
        with self.assertRaises(verify.ValidationError):
            verify.load_certificate(path)

    def test_file_at_exact_size_limit_is_accepted(self):
        encoded = json.dumps(certificate()).encode("utf-8")
        path = self.directory / "at-limit.json"
        path.write_bytes(encoded + b" " * (1048576 - len(encoded)))
        self.assertTrue(verify.analyze(verify.load_certificate(path))["certified"])

    def test_cli_accepts_verified_boundary_certificate(self):
        completed = self.cli(self.write(json.dumps(certificate())))
        self.assertEqual(completed.returncode, 0, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertTrue(result["certified"])
        self.assertEqual(result["status"], "certified")

    def test_cli_reports_valid_but_uncertified(self):
        data = certificate(polynomials=[[term(1, 1), term(-2, 0)]])
        completed = self.cli(self.write(json.dumps(data)))
        self.assertEqual(completed.returncode, 1, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertFalse(result["certified"])
        self.assertEqual(result["status"], "not_certified")
        self.assertTrue(result["failure_reasons"])

    def test_cli_reports_invalid_input(self):
        data = certificate(); data["q"] = "0"
        completed = self.cli(self.write(json.dumps(data)))
        self.assertEqual(completed.returncode, 2, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertFalse(result["certified"])
        self.assertEqual(result["status"], "invalid")
        self.assertIsInstance(result["error"], str)


if __name__ == "__main__":
    unittest.main()
