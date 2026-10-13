"""Independent checks against raw rows and the original objective.

No verifier parser, normalization, dot-product or certificate helper is used as
an oracle.  This is bounded computational evidence, not Lean acceptance or a
proof that certificates can always be found.
"""

from copy import deepcopy
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import verifier  # noqa: E402


def inner(a, b):
    assert len(a) == len(b)
    return sum((Q(x) * Q(y) for x, y in zip(a, b)), Q(0))


def original_feasible(problem, x, *, ray=False):
    for row in problem["constraints"]:
        lhs = inner(row["coefficients"], x)
        rhs = Q(0) if ray else Q(row["rhs"])
        relation = row["sense"]
        if relation == "<=" and lhs > rhs:
            return False
        if relation == ">=" and lhs < rhs:
            return False
        if relation == "=" and lhs != rhs:
            return False
    return True


def raw_certificate_accepts(document):
    """Mathematical predicate on already well-formed documents, in raw senses."""
    problem, cert = document["problem"], document["certificate"]
    c = problem["objective"]["coefficients"]
    maximize = problem["objective"]["sense"] == "max"
    if cert["kind"] == "unbounded":
        change = inner(c, cert["direction"])
        improves = change > 0 if maximize else change < 0
        return (original_feasible(problem, cert["base_point"])
                and original_feasible(problem, cert["direction"], ray=True)
                and improves)
    ys, zs = cert["inequality_multipliers"], cert["equality_multipliers"]
    if any(Q(y) < 0 for y in ys):
        return False
    signed_weights = []
    iy = iz = 0
    for row in problem["constraints"]:
        if row["sense"] == "=":
            signed_weights.append(Q(zs[iz]))
            iz += 1
        else:
            signed_weights.append(Q(ys[iy]) * (1 if row["sense"] == "<=" else -1))
            iy += 1
    rows = problem["constraints"]
    total = [sum((w * Q(row["coefficients"][j])
                  for row, w in zip(rows, signed_weights)), Q(0))
             for j in range(len(c))]
    bound = sum((w * Q(row["rhs"]) for row, w in zip(rows, signed_weights)), Q(0))
    if cert["kind"] == "infeasible":
        return all(a == 0 for a in total) and bound < 0
    polarity = 1 if maximize else -1
    return (original_feasible(problem, cert["point"])
            and total == [polarity * Q(a) for a in c]
            and bound == polarity * inner(c, cert["point"]))


def document(rows, c=(1,), sense="max", **cert):
    return {"version": 1,
            "problem": {"objective": {"sense": sense, "coefficients": list(c)},
                        "constraints": deepcopy(list(rows))},
            "certificate": cert}


def row(a, sense, b):
    return {"coefficients": list(a), "sense": sense, "rhs": b}


class IndependentReview(unittest.TestCase):
    def assert_raw_agreement(self, doc):
        expected = raw_certificate_accepts(doc)
        result = verifier.verify(doc)
        self.assertNotEqual(result["status"], "invalid", doc)
        self.assertEqual(result["accepted"], expected, doc)
        return expected

    def assert_sampled_soundness(self, doc, samples):
        problem, cert = doc["problem"], doc["certificate"]
        c = problem["objective"]["coefficients"]
        maximize = problem["objective"]["sense"] == "max"
        if cert["kind"] == "optimal":
            optimum = inner(c, cert["point"])
            for x in samples:
                if original_feasible(problem, x):
                    value = inner(c, x)
                    self.assertTrue(value <= optimum if maximize else value >= optimum, doc)
        elif cert["kind"] == "infeasible":
            self.assertFalse(any(original_feasible(problem, x) for x in samples), doc)
        else:
            base = cert["base_point"]
            direction = cert["direction"]
            base_value = inner(c, base)
            for t in [Q(0), Q(1, 3), Q(1), Q(2), Q(100)]:
                x = [Q(a) + t * Q(d) for a, d in zip(base, direction)]
                self.assertTrue(original_feasible(problem, x), doc)
                if t > 0:
                    value = inner(c, x)
                    self.assertTrue(value > base_value if maximize else value < base_value, doc)

    def test_published_fixtures_against_raw_oracle(self):
        names = sorted((ROOT / "examples").glob("*.json"))
        self.assertEqual(len(names), 17)
        for path in names:
            with self.subTest(example=path.name):
                result = verifier.verify_json(path.read_text())
                expected_status = ("invalid" if path.name.startswith("invalid_") else
                                   "rejected" if path.name.startswith("rejected_") else "accepted")
                self.assertEqual(result["status"], expected_status)
                if expected_status != "invalid":
                    doc = json.loads(path.read_text())
                    self.assert_raw_agreement(doc)
                    if result["accepted"]:
                        dimension = len(doc["problem"]["objective"]["coefficients"])
                        samples = product([Q(-2), Q(-1), Q(0), Q(1, 3), Q(1), Q(2), Q(4)],
                                          repeat=dimension)
                        self.assert_sampled_soundness(doc, samples)

    def test_exact_values_recalculated_by_hand(self):
        mixed = json.loads((ROOT / "examples/optimal_mixed_redundant.json").read_text())
        # 1(1,1) + (3/4)(2,2) + (1/2)(1,-1) = (3,2).
        self.assertEqual(Q(1) + Q(3, 4) * 2 + Q(1, 2), Q(3))
        self.assertEqual(Q(1) + Q(3, 4) * 2 - Q(1, 2), Q(2))
        self.assertEqual(Q(4) + Q(3, 4) * 8, Q(10))
        self.assertEqual(verifier.verify(mixed)["certified_objective_value"], "10")
        fractional = json.loads((ROOT / "examples/optimal_min_fraction_equality.json").read_text())
        # Objective (3/2)(1/3)=1/2; the signed equality weight is -1/2.
        self.assertEqual(inner(["3/2"], ["1/3"]), Q(1, 2))
        self.assertEqual(verifier.verify(fractional)["certified_objective_value"], "1/2")
        infeasible = json.loads((ROOT / "examples/infeasible_equalities.json").read_text())
        self.assertEqual(2 * 0 - 1, -1)
        self.assert_raw_agreement(infeasible)
        ray = json.loads((ROOT / "examples/unbounded_min_lower_dimensional.json").read_text())
        self.assertEqual(inner([-2, 1], [1, 1]), -1)
        self.assert_raw_agreement(ray)

    def test_bounded_exhaustive_two_row_certificates(self):
        # 18 raw rows, every ordered pair, both objective senses.  72,900
        # well-formed certificate documents, independently calculated below.
        rows = [row([a], rel, b)
                for a, rel, b in product([-1, 1], ["<=", ">=", "="], [-1, 0, 1])]
        grid = [(Q(k, 2),) for k in range(-4, 5)]
        count = {"optimal": 0, "infeasible": 0, "unbounded": 0}
        accepted = {kind: 0 for kind in count}
        for raw_rows in product(rows, repeat=2):
            for weights in product([-1, 0, 1], repeat=2):
                ys = [w for r, w in zip(raw_rows, weights) if r["sense"] != "="]
                zs = [w for r, w in zip(raw_rows, weights) if r["sense"] == "="]
                doc = document(raw_rows, c=(0,), kind="infeasible",
                               inequality_multipliers=ys, equality_multipliers=zs)
                count["infeasible"] += 1
                if self.assert_raw_agreement(doc):
                    accepted["infeasible"] += 1
                    self.assert_sampled_soundness(doc, grid)
                for sense, c, p in product(["max", "min"], [-1, 0, 1], [-1, 0, 1]):
                    doc = document(raw_rows, c=(c,), sense=sense, kind="optimal", point=[p],
                                   inequality_multipliers=ys, equality_multipliers=zs)
                    count["optimal"] += 1
                    if self.assert_raw_agreement(doc):
                        accepted["optimal"] += 1
                        self.assert_sampled_soundness(doc, grid)
            for sense, c, p, d in product(["max", "min"], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1]):
                doc = document(raw_rows, c=(c,), sense=sense, kind="unbounded", base_point=[p], direction=[d])
                count["unbounded"] += 1
                if self.assert_raw_agreement(doc):
                    accepted["unbounded"] += 1
                    self.assert_sampled_soundness(doc, grid)
        self.assertEqual(count, {"optimal": 52488, "infeasible": 2916, "unbounded": 17496})
        self.assertEqual(accepted, {"optimal": 1752, "infeasible": 96, "unbounded": 224})
        # Exact counts make inadvertent weakening of this bounded experiment visible.
        print("Independent exhaustive counts:", count, "accepted:", accepted)

    def test_equality_negative_weights_and_interleaved_rows(self):
        doc = document([row([1, 0], "=", 2), row([0, 1], "<=", 3),
                        row([2, 0], "=", 4), row([0, 1], ">=", 0)],
                       c=(-1, 1), kind="optimal", point=[2, 3],
                       inequality_multipliers=[1, 0], equality_multipliers=[1, -1])
        self.assertTrue(self.assert_raw_agreement(doc))
        self.assertEqual(verifier.verify(doc)["certified_objective_value"], "1")
        self.assert_sampled_soundness(doc, product([Q(-1), Q(0), Q(2), Q(3)], repeat=2))
        doc["certificate"]["equality_multipliers"] = [-1, 1]
        self.assertFalse(self.assert_raw_agreement(doc))

    def test_zero_dimensions_empty_rows_and_zero_objectives(self):
        empty_opt = document([], c=(), kind="optimal", point=[], inequality_multipliers=[], equality_multipliers=[])
        self.assertTrue(self.assert_raw_agreement(empty_opt))
        for kind, cert in [("infeasible", {"inequality_multipliers": [], "equality_multipliers": []}),
                           ("unbounded", {"base_point": [], "direction": []})]:
            self.assertFalse(self.assert_raw_agreement(document([], c=(), kind=kind, **cert)))
        for c, d in [(0, 1), (1, 0), (0, 0)]:
            self.assertFalse(self.assert_raw_agreement(document([], c=(c,), kind="unbounded", base_point=[0], direction=[d])))
        impossible = document([row([], "=", 1)], c=(), kind="infeasible",
                              inequality_multipliers=[], equality_multipliers=[-1])
        self.assertTrue(self.assert_raw_agreement(impossible))
        false_opt = document([row([], "<=", -1)], c=(), kind="optimal", point=[],
                             inequality_multipliers=[0], equality_multipliers=[])
        self.assertFalse(self.assert_raw_agreement(false_opt))

    def test_positive_rational_row_rescaling_and_ray_rescaling(self):
        for name in ["optimal_mixed_redundant.json", "optimal_min_fraction_equality.json",
                     "infeasible_mixed.json", "infeasible_equalities.json"]:
            base = json.loads((ROOT / "examples" / name).read_text())
            for scale in [Q(1, 7), Q(13, 3), Q(10**40 + 1, 10**30 + 3)]:
                doc = deepcopy(base)
                iy = iz = 0
                for r in doc["problem"]["constraints"]:
                    r["coefficients"] = [str(scale * Q(a)) for a in r["coefficients"]]
                    r["rhs"] = str(scale * Q(r["rhs"]))
                    field = "equality_multipliers" if r["sense"] == "=" else "inequality_multipliers"
                    i = iz if r["sense"] == "=" else iy
                    doc["certificate"][field][i] = str(Q(doc["certificate"][field][i]) / scale)
                    if r["sense"] == "=":
                        iz += 1
                    else:
                        iy += 1
                self.assertTrue(self.assert_raw_agreement(doc), (name, scale))
        base = json.loads((ROOT / "examples/unbounded_min_lower_dimensional.json").read_text())
        for scale in [Q(1, 7), Q(13, 3), Q(1000001)]:
            doc = deepcopy(base)
            doc["certificate"]["direction"] = [str(scale * Q(d)) for d in doc["certificate"]["direction"]]
            self.assertTrue(self.assert_raw_agreement(doc))
        for scale in [Q(0), Q(-1)]:
            doc = deepcopy(base)
            doc["certificate"]["direction"] = [str(scale * Q(d)) for d in doc["certificate"]["direction"]]
            self.assertFalse(self.assert_raw_agreement(doc))

    def test_degeneracy_redundancy_and_nonunique_multiplier(self):
        doc = json.loads((ROOT / "examples/optimal_mixed_redundant.json").read_text())
        for weights in [["5/2", 0, 0, 0], [0, "5/4", 0, 0], [1, "3/4", 0, 0]]:
            doc["certificate"]["inequality_multipliers"] = weights
            self.assertTrue(self.assert_raw_agreement(doc))
        # An optimal point in a segment with zero objective: every feasible point is optimal.
        face = document([row([1, 0], "=", 0), row([0, 1], "<=", 1), row([0, 1], ">=", 0)],
                        c=(0, 0), kind="optimal", point=[0, "1/2"],
                        inequality_multipliers=[0, 0], equality_multipliers=[0])
        self.assertTrue(self.assert_raw_agreement(face))
        self.assert_sampled_soundness(face, product([Q(-1), Q(0), Q(1, 2), Q(1), Q(2)], repeat=2))

    def test_exact_strictness_at_arbitrarily_small_rational_scale(self):
        epsilon = Q(1, 10**120 + 39)
        for sense, c in [("max", epsilon), ("min", -epsilon)]:
            ray = document([], c=(str(c),), sense=sense,
                           kind="unbounded", base_point=[0], direction=[1])
            self.assertTrue(self.assert_raw_agreement(ray))
        contradiction = document([row([], "<=", str(-epsilon))], c=(), kind="infeasible",
                                 inequality_multipliers=[1], equality_multipliers=[])
        self.assertTrue(self.assert_raw_agreement(contradiction))
        near_miss = document([row([1], "<=", 1)], kind="optimal", point=[1],
                             inequality_multipliers=[str(1 + epsilon)], equality_multipliers=[])
        self.assertFalse(self.assert_raw_agreement(near_miss))

    def test_failed_sign_strictness_and_feasibility_obligations(self):
        cases = [
            document([row([1], ">=", 0)], kind="optimal", point=[0],
                     inequality_multipliers=[-1], equality_multipliers=[]),
            document([row([1], "<=", 0)], kind="unbounded", base_point=[0], direction=[1]),
            document([row([1], ">=", 0)], kind="unbounded", base_point=[-1], direction=[1]),
            document([row([1], "=", 0)], kind="unbounded", base_point=[0], direction=[1]),
            document([row([0], "<=", 0)], c=(0,), kind="infeasible",
                     inequality_multipliers=[1], equality_multipliers=[]),
            document([row([1], "<=", 1)], kind="optimal", point=[0],
                     inequality_multipliers=[1], equality_multipliers=[]),
        ]
        for doc in cases:
            self.assertFalse(self.assert_raw_agreement(doc))

    def test_malformed_rationals_types_fields_and_dimensions(self):
        base = document([row([1], "<=", 1)], kind="optimal", point=[1],
                        inequality_multipliers=[1], equality_multipliers=[])
        for value in [True, False, 0.1, None, [], {}, "1/0", "1/-2", "1.0", " 1", "1/02", "1e2"]:
            doc = deepcopy(base)
            doc["problem"]["objective"]["coefficients"] = [value]
            self.assertEqual(verifier.verify(doc)["status"], "invalid", value)
        mutations = [
            lambda d: d.update(version=True),
            lambda d: d.update(extra=0),
            lambda d: d.pop("version"),
            lambda d: d["problem"].update(constraints={}),
            lambda d: d["problem"]["constraints"][0].update(coefficients=[]),
            lambda d: d["certificate"].update(point=[]),
            lambda d: d["certificate"].update(inequality_multipliers=[]),
            lambda d: d["certificate"].update(equality_multipliers=[0]),
            lambda d: d["certificate"].update(kind="Optimal"),
            lambda d: d["certificate"].update(direction=[0]),
            lambda d: d["certificate"].update(point=(1,)),
            lambda d: d["problem"]["objective"].update(sense="MAX"),
            lambda d: d["problem"]["constraints"][0].update(sense="<"),
        ]
        for mutate in mutations:
            doc = deepcopy(base)
            mutate(doc)
            self.assertEqual(verifier.verify(doc)["status"], "invalid", doc)
        self.assertEqual(verifier.verify({0: "bad"})["status"], "invalid")
        ray = document([], kind="unbounded", base_point=[0], direction=[])
        self.assertEqual(verifier.verify(ray)["status"], "invalid")

    def test_json_duplicate_keys_constants_and_parse_errors(self):
        base = json.dumps(document([], kind="unbounded", base_point=[0], direction=[1]))
        malformed = ["", "{", "[]", "null", "true", base + " trailing",
                     '{"version": 1, "version": 1}',
                     base.replace('"kind": "unbounded"', '"kind": "optimal", "kind": "unbounded"'),
                     base.replace('"coefficients": [1]', '"coefficients": [NaN]'),
                     base.replace('"coefficients": [1]', '"coefficients": [Infinity]'),
                     base.replace('"coefficients": [1]', '"coefficients": [-Infinity]')]
        for text in malformed:
            self.assertEqual(verifier.verify_json(text)["status"], "invalid", text)

    def test_cli_stdin_exit_codes_and_invalid_input(self):
        cases = [("unbounded_max_no_rows.json", 0, "accepted"),
                 ("rejected_negative_multiplier.json", 1, "rejected"),
                 ("invalid_duplicate_key.json", 2, "invalid")]
        for name, exit_code, status in cases:
            text = (ROOT / "examples" / name).read_text()
            result = subprocess.run([sys.executable, str(ROOT / "verifier.py"), "-"],
                                    input=text, text=True, capture_output=True, check=False)
            self.assertEqual(result.returncode, exit_code)
            self.assertEqual(result.stderr, "")
            self.assertEqual(json.loads(result.stdout)["status"], status)
        for text in ["{", "[" * 11000 + "]" * 11000]:
            result = subprocess.run([sys.executable, str(ROOT / "verifier.py"), "-"],
                                    input=text, text=True, capture_output=True, check=False)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stderr, "")
            self.assertEqual(json.loads(result.stdout)["status"], "invalid")
        missing = subprocess.run([sys.executable, str(ROOT / "verifier.py"), str(ROOT / "examples/does-not-exist.json")],
                                 text=True, capture_output=True, check=False)
        self.assertEqual(missing.returncode, 2)
        self.assertEqual(json.loads(missing.stdout)["diagnostics"][0]["code"], "io")


if __name__ == "__main__":
    unittest.main()
