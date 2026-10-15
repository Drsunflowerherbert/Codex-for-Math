#!/usr/bin/env python3
"""Independent finite audit: exact affine oracles, rank, limits and file parsing.

Run from anywhere with Python 3.10+: python3 path/to/independent_check.py.
Uses only the standard library. Finite tests are not a formal correctness proof.
"""

from copy import deepcopy
from fractions import Fraction as Q
import importlib.util
from itertools import product
import json
from pathlib import Path
import random
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("independently_reviewed_verify", ROOT / "verify.py")
v = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = v
SPEC.loader.exec_module(v)
COUNTS = {}


def check(condition, label):
    if not condition:
        raise AssertionError(label)


def invalid(call, label):
    try:
        call()
    except v.ValidationError:
        return
    raise AssertionError("invalid input accepted: " + label)


def affine(h, b, y, c=None, r=None):
    n = len(h)
    c = [Q(0)] * n if c is None else c
    r = [Q(1)] * n if r is None else r
    polys = []
    for row, constant in zip(h, b):
        terms = [{"coefficient": str(constant), "powers": [0] * n}]
        for j, coefficient in enumerate(row):
            powers = [0] * n
            powers[j] = 1
            terms.append({"coefficient": str(coefficient), "powers": powers})
        polys.append(terms)
    return {"schema_version": 1, "name": "independent affine oracle",
            "variables": ["x" + str(i) for i in range(n)], "polynomials": polys,
            "center": list(map(str, c)), "radii": list(map(str, r)),
            "preconditioner": [list(map(str, row)) for row in y]}


def determinant(matrix):
    # Leibniz/cofactor definition, independently of checker elimination.
    if len(matrix) == 1:
        return matrix[0][0]
    return sum((-1) ** j * matrix[0][j] * determinant(
        [row[:j] + row[j + 1:] for row in matrix[1:]])
        for j in range(len(matrix)))


def rank_audit():
    cases = []
    for flat in product([-1, 0, 1], repeat=4):
        cases.append([[Q(flat[0]), Q(flat[1])], [Q(flat[2]), Q(flat[3])]])
    rng = random.Random(20261015)
    for n in [1, 3, 4]:
        for _ in range(120):
            matrix = [[Q(rng.randrange(-3, 4), rng.randrange(1, 5)) for _ in range(n)]
                      for _ in range(n)]
            cases.append(matrix)
            if n > 1:
                matrix = deepcopy(matrix)
                matrix[-1] = [matrix[0][j] * 2 for j in range(n)]
                cases.append(matrix)
    for matrix in cases:
        actual = True
        try:
            v._check_invertible(tuple(map(tuple, matrix)))
        except v.ValidationError:
            actual = False
        check(actual == (determinant(matrix) != 0), "rank versus determinant")
    COUNTS["rank_cases"] = len(cases)


def affine_audit():
    rng = random.Random(812031)
    cases = 0
    for _ in range(640):
        h = [[Q(rng.randrange(-4, 5), rng.randrange(1, 5)) for _ in range(2)]
             for _ in range(2)]
        y = [[Q(rng.randrange(-4, 5), rng.randrange(1, 5)) for _ in range(2)]
             for _ in range(2)]
        if determinant(y) == 0:
            continue
        b = [Q(rng.randrange(-4, 5), 5) for _ in range(2)]
        c = [Q(rng.randrange(-4, 5), 7) for _ in range(2)]
        r = [Q(rng.randrange(1, 5), 3) for _ in range(2)]
        out = v.analyze(affine(h, b, y, c, r))
        f = [sum(h[i][j] * c[j] for j in range(2)) + b[i] for i in range(2)]
        step = [sum(y[i][k] * f[k] for k in range(2)) for i in range(2)]
        e = [[Q(int(i == j)) - sum(y[i][k] * h[k][j] for k in range(2))
              for j in range(2)] for i in range(2)]
        mr = [sum(abs(e[i][j]) * r[j] for j in range(2)) for i in range(2)]
        q = max(mr[i] / r[i] for i in range(2))
        eta = max(abs(step[i]) / r[i] for i in range(2))
        selfmap = all(abs(step[i]) + mr[i] <= r[i] for i in range(2))
        check(list(map(Q, out["residual"])) == f, "affine residual")
        check(list(map(Q, out["step"])) == step, "affine preconditioned residual")
        check(Q(out["q"]) == q and Q(out["eta"]) == eta, "weighted norm bounds")
        check(out["certified"] == (q < 1 and selfmap), "acceptance versus affine oracle")
        for i, j in product(range(2), repeat=2):
            check(list(map(Q, out["J"][i][j])) == [h[i][j]] * 2, "affine Jacobian")
            check(list(map(Q, out["E"][i][j])) == [e[i][j]] * 2, "signed matrix defect")
        if out["certified"]:
            error = eta / (1 - q)
            check(Q(out["weighted_error_bound"]) == error, "raw weighted error")
            check(list(map(Q, out["coordinate_error_bounds"])) ==
                  [min(r[i], r[i] * error) for i in range(2)], "coordinate clipping")
        else:
            check(out["weighted_error_bound"] is None and out["coordinate_error_bounds"] is None,
                  "failed test has no certified error")
        cases += 1
    # Worst rows differ, so eta+q > 1 yet every self-map row passes.
    out = v.analyze(affine([[Q(1), Q(0)], [Q(0), Q(1, 10)]], [Q(-9, 10), Q(0)],
                           [[Q(1), Q(0)], [Q(0), Q(1)]]))
    check(out["certified"] and Q(out["weighted_error_bound"]) == 9 and
          list(map(Q, out["coordinate_error_bounds"])) == [1, 1], "different worst rows")
    COUNTS["affine_cases"] = cases + 1


def power_audit():
    cases = 0
    for lo, hi in product(range(-3, 4), repeat=2):
        if lo > hi:
            continue
        for exponent in range(33):
            interval = v.Interval(lo, hi) ** exponent
            # For this continuous power function extrema occur at endpoints
            # and possibly zero. These extrema are exact rational values.
            values = [Q(lo) ** exponent, Q(hi) ** exponent]
            if lo <= 0 <= hi:
                values.append(Q(0) ** exponent)
            check(interval.lo == min(values) and interval.hi == max(values), "power range")
            cases += 1
    COUNTS["power_cases"] = cases


def boundary_and_parser_audit():
    base = affine([[Q(1)]], [Q(-1)], [[Q(1)]])
    cases = 0
    with tempfile.TemporaryDirectory(prefix="certified-roots-independent-") as temp:
        path = Path(temp) / "input.json"

        def load(text):
            path.write_text(text, encoding="utf-8")
            return v.load_certificate(path)

        text = json.dumps(base)
        bad_texts = [text.replace('"schema_version": 1', '"schema_version": 1, "schema\\u005fversion": 1'),
                     text.replace('"powers": [0]', '"powers": [0], "powers": [0]', 1),
                     "[" * 3000 + "0" + "]" * 3000,
                     text.replace('"schema_version": 1', '"schema_version": ' + '9' * 5000)]
        for literal in ["NaN", "Infinity", "-Infinity", "1.0", "1e0"]:
            bad_texts.append(text.replace('"schema_version": 1', '"schema_version": ' + literal))
        for bad in bad_texts:
            invalid(lambda bad=bad: load(bad), "file parser adversary")
            cases += 1
        # Exact size boundary: the file limit is inclusive, not approximate.
        sized = deepcopy(base)
        sized["name"] = ""
        padded = json.dumps(sized)
        sized["name"] = "a" * (v.MAX_BYTES - len(padded.encode("utf-8")))
        exact = json.dumps(sized)
        check(len(exact.encode("utf-8")) == v.MAX_BYTES, "size test construction")
        check(v.analyze(load(exact))["certified"], "1 MiB input accepted")
        invalid(lambda: load(exact + " "), "1 MiB plus one byte")
        cases += 2
        for payload, expected in [(base, 0), (affine([[Q(1)]], [Q(-2)], [[Q(1)]]), 1),
                                  ({**base, "q": "0"}, 2)]:
            path.write_text(json.dumps(payload), encoding="utf-8")
            run = subprocess.run([sys.executable, str(ROOT / "verify.py"), str(path)],
                                 capture_output=True, text=True, check=False)
            check(run.returncode == expected, "CLI exact exit code")
            result = json.loads(run.stdout)
            check(result["certified"] == (expected == 0), "CLI success flag")
            cases += 1
        run = subprocess.run([sys.executable, str(ROOT / "verify.py")],
                             capture_output=True, text=True, check=False)
        check(run.returncode == 2, "missing CLI argument")
        cases += 1

    # All maximum supported input dimensions/degrees/term counts are accepted.
    n = v.MAX_DIMENSION
    identity = [[Q(int(i == j)) for j in range(n)] for i in range(n)]
    check(v.analyze(affine(identity, [Q(0)] * n, identity))["certified"], "dimension 8")
    maximum = deepcopy(base)
    maximum["polynomials"] = [[{"coefficient": "0", "powers": [32]}] * 254 +
                               [{"coefficient": "1", "powers": [1]},
                                {"coefficient": "-1", "powers": [0]}]]
    check(v.analyze(maximum)["certified"], "256 terms and degree 32")
    maximum["center"] = ["0/" + "9" * 128]
    maximum["radii"] = ["9" * 128 + "/" + "9" * 128]
    check(v.analyze(maximum)["certified"], "128 digit rational parts")
    COUNTS["parser_boundary_cli_cases"] = cases + 3


def example_audit():
    expected = {
        "circle-line": (True, "1/70", "5/7", ["1/138", "1/138"]),
        "circle-parabola": (True, "3/22", "4/11", ["2/95", "2/95"]),
        "tiny-residual-no-root": (False, "501/500", "1/1000000000", None),
        "tiny-residual-two-roots": (False, "501/500", "1/1000000000", None),
    }
    for name, (accepted, q, eta, bounds) in expected.items():
        out = v.analyze(v.load_certificate(ROOT / "examples" / (name + ".json")))
        check((out["certified"], out["q"], out["eta"], out["coordinate_error_bounds"]) ==
              (accepted, q, eta, bounds), "hand-derived example " + name)
    COUNTS["hand_example_cases"] = len(expected)


def long_output_audit():
    # Independent parser uses 64-digit left-to-right chunks, unlike the
    # checker's 500-digit right-to-left serializer. Do not change Python's
    # process-wide integer-conversion limit to make this regression pass.
    def integer(text):
        sign = -1 if text.startswith("-") else 1
        text = text.lstrip("-")
        result = 0
        for start in range(0, len(text), 64):
            chunk = text[start:start + 64]
            result = result * 10 ** len(chunk) + int(chunk)
        return sign * result

    def rational(text):
        parts = text.split("/")
        return Q(integer(parts[0]), 1 if len(parts) == 1 else integer(parts[1]))

    large = 10 ** 5000 + 1
    expected = "1" + "0" * 4999 + "1"
    check(v._integer_string(large) == expected, "large positive serialization")
    check(v._integer_string(-large) == "-" + expected, "large negative serialization")
    denominator = 10 ** 127 + 1
    c, r = Q(1, denominator), Q(1, denominator + 2)
    data = affine([[Q(1)]], [Q(0)], [[Q(1)]], [c], [r])
    data["polynomials"] = [[{"coefficient": "1", "powers": [32]}]]
    out = v.analyze(data)
    check(list(map(rational, out["J"][0][0])) == [32 * (c - r) ** 31, 32 * (c + r) ** 31],
          "degree 32 long-output derivative")
    check(rational(out["q"]) == 1 - 32 * (c - r) ** 31, "long-output contraction")
    check(rational(out["eta"]) == c ** 32 / r and not out["certified"], "long-output residual")
    with tempfile.TemporaryDirectory(prefix="certified-roots-long-") as temp:
        path = Path(temp) / "long.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        run = subprocess.run([sys.executable, str(ROOT / "verify.py"), str(path)],
                             capture_output=True, text=True, check=False)
        check(run.returncode == 1 and json.loads(run.stdout) == out, "long-output CLI roundtrip")
    COUNTS["long_output_cases"] = 6


if __name__ == "__main__":
    rank_audit()
    affine_audit()
    power_audit()
    boundary_and_parser_audit()
    example_audit()
    long_output_audit()
    print(json.dumps({"status": "passed", "counts": COUNTS}, sort_keys=True))
