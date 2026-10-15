#!/usr/bin/env python3
"""Check a rational polynomial root certificate using exact arithmetic.

No numerical approximation or third-party package is used.  The trusted runtime
is Python's integer/Fraction arithmetic, JSON parser, and this source file.  A
successful result applies to the polynomial system actually supplied in the
input, on the reported *closed box*, not to every root of that system.  Neither
a small residual nor a failed sufficient test is a statement of nonexistence.

Input rationals are strings matching ``-?[0-9]+(?:/[1-9][0-9]*)?``.  Each
numerator (without its sign) and denominator has at most 128 decimal digits.
Leading zeros in numerators and unreduced fractions are accepted; denominators
must begin with a nonzero digit.  JSON numeric values are used only for the
schema version and exponents; floats, nonfinite constants, and booleans in
integer positions are rejected.  Other explicit limits are below.  These bound
the input, but this program is not a hardened service for hostile workloads.

Public API: ``load_certificate(path)`` returns validated JSON data;
``analyze(data)`` revalidates and returns a JSON-serializable report.  Invalid
input raises ``ValidationError``.  CLI exit codes: 0 certified, 1 valid but
uncertified, 2 invalid input or invocation.  Uncertified reports deliberately
have null error-bound fields.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
import re
import sys
from typing import Any


MAX_BYTES = 1_048_576
MAX_DIMENSION = 8
MAX_TOTAL_TERMS = 256
MAX_TOTAL_DEGREE = 32
MAX_RATIONAL_DIGITS = 128
RATIONAL_PATTERN = r"-?[0-9]+(?:/[1-9][0-9]*)?"
_RATIONAL_RE = re.compile(RATIONAL_PATTERN, re.ASCII)
_TOP_KEYS = frozenset({
    "schema_version", "name", "variables", "polynomials", "center", "radii",
    "preconditioner",
})
_TERM_KEYS = frozenset({"coefficient", "powers"})


class ValidationError(ValueError):
    """The candidate does not satisfy the exact input schema or resource limits."""


def _integer_string(value: int) -> str:
    """Serialize arbitrarily long exact results without a process-global change.

    Python may limit decimal conversion of a single large integer.  Input
    integers are small enough for that limit, but rational interval operations
    can create much longer numerators and denominators.  Base-10**500 chunks
    stay below Python's minimum configurable nonzero limit (640 digits).
    """
    sign = "-" if value < 0 else ""
    value = abs(value)
    base = 10 ** 500
    chunks = []
    while value >= base:
        value, chunk = divmod(value, base)
        chunks.append(str(chunk).zfill(500))
    return sign + str(value) + "".join(reversed(chunks))


def _rational_string(value: Fraction) -> str:
    numerator = _integer_string(value.numerator)
    if value.denominator == 1:
        return numerator
    return numerator + "/" + _integer_string(value.denominator)


def _fraction(value: Any) -> Fraction:
    """Convert an interval operand; never silently convert floats or strings."""
    if isinstance(value, Fraction):
        return value
    if type(value) is int:
        return Fraction(value)
    raise TypeError("interval operands must be integers or Fractions")


@dataclass(frozen=True)
class Interval:
    """Closed rational interval, with exact inclusive arithmetic operations.

    Endpoints and scalar operands are integers or Fractions.  Dependency between
    repeated variables may widen an enclosure, but cannot shrink it unsafely.
    In particular, powers use the range of the power function, including zero
    for positive even powers on intervals crossing zero.
    """

    lo: Fraction
    hi: Fraction | None = None

    def __post_init__(self) -> None:
        lower = _fraction(self.lo)
        upper = lower if self.hi is None else _fraction(self.hi)
        if lower > upper:
            raise ValueError("interval lower endpoint exceeds upper endpoint")
        object.__setattr__(self, "lo", lower)
        object.__setattr__(self, "hi", upper)

    @staticmethod
    def _coerce(value: Any) -> Interval:
        return value if isinstance(value, Interval) else Interval(_fraction(value))

    def __add__(self, other: Any) -> Interval:
        other = self._coerce(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self) -> Interval:
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: Any) -> Interval:
        return self + (-self._coerce(other))

    def __rsub__(self, other: Any) -> Interval:
        return self._coerce(other) + (-self)

    def __mul__(self, other: Any) -> Interval:
        other = self._coerce(other)
        products = (self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi)
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def __pow__(self, exponent: int) -> Interval:
        if type(exponent) is not int or exponent < 0:
            raise ValueError("interval powers require a nonnegative integer")
        if exponent == 0:
            return Interval(1)
        if exponent % 2:
            return Interval(self.lo ** exponent, self.hi ** exponent)
        high = max(self.lo ** exponent, self.hi ** exponent)
        low = (Fraction(0) if self.lo <= 0 <= self.hi
               else min(self.lo ** exponent, self.hi ** exponent))
        return Interval(low, high)

    def abs_max(self) -> Fraction:
        return max(abs(self.lo), abs(self.hi))

    def to_json(self) -> list[str]:
        return [_rational_string(self.lo), _rational_string(self.hi)]


@dataclass(frozen=True)
class _Certificate:
    name: str
    variables: tuple[str, ...]
    # Polynomials are lists of coefficient/exponent-vector pairs.  Duplicate
    # monomials, zero coefficients and empty (zero) polynomials are permitted.
    polynomials: tuple[tuple[tuple[Fraction, tuple[int, ...]], ...], ...]
    center: tuple[Fraction, ...]
    radii: tuple[Fraction, ...]
    preconditioner: tuple[tuple[Fraction, ...], ...]


def _keys(value: Any, expected: frozenset[str], where: str) -> None:
    if not isinstance(value, dict):
        raise ValidationError(f"{where} must be an object")
    if any(type(key) is not str for key in value):
        raise ValidationError(f"{where} keys must be strings")
    missing, unknown = expected - value.keys(), value.keys() - expected
    if missing or unknown:
        details = []
        if missing:
            details.append("missing keys: " + ", ".join(sorted(missing)))
        if unknown:
            details.append("unknown keys: " + ", ".join(sorted(unknown)))
        raise ValidationError(f"{where}: {'; '.join(details)}")


def _list(value: Any, length: int | None, where: str) -> list[Any]:
    if type(value) is not list:
        raise ValidationError(f"{where} must be an array")
    if length is not None and len(value) != length:
        raise ValidationError(f"{where} must have length {length}")
    return value


def _rational(value: Any, where: str) -> Fraction:
    if type(value) is not str:
        raise ValidationError(f"{where} must be a rational string")
    # Check length before the regular expression and integer conversion.
    if len(value) > 2 * MAX_RATIONAL_DIGITS + 2:
        raise ValidationError(f"{where} exceeds the rational digit limit")
    if _RATIONAL_RE.fullmatch(value) is None:
        raise ValidationError(f"{where} must match {RATIONAL_PATTERN}")
    parts = value.lstrip("-").split("/")
    if any(len(part) > MAX_RATIONAL_DIGITS for part in parts):
        raise ValidationError(f"{where} exceeds the rational digit limit")
    return Fraction(value)


def _check_invertible(matrix: tuple[tuple[Fraction, ...], ...]) -> None:
    """Prove full rank by exact rational Gaussian elimination."""
    rows = [list(row) for row in matrix]
    dimension = len(rows)
    for column in range(dimension):
        pivot_row = next((i for i in range(column, dimension)
                          if rows[i][column] != 0), None)
        if pivot_row is None:
            raise ValidationError("preconditioner must be nonsingular")
        rows[column], rows[pivot_row] = rows[pivot_row], rows[column]
        pivot = rows[column][column]
        for i in range(column + 1, dimension):
            multiplier = rows[i][column] / pivot
            for j in range(column, dimension):
                rows[i][j] -= multiplier * rows[column][j]


def _parse_certificate(data: Any) -> _Certificate:
    _keys(data, _TOP_KEYS, "certificate")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ValidationError("schema_version must be the integer 1")
    if type(data["name"]) is not str:
        raise ValidationError("name must be a string")
    variables = _list(data["variables"], None, "variables")
    n = len(variables)
    if not 1 <= n <= MAX_DIMENSION:
        raise ValidationError(f"dimension must be between 1 and {MAX_DIMENSION}")
    if any(type(variable) is not str for variable in variables):
        raise ValidationError("variables must be strings")
    if len(set(variables)) != n:
        raise ValidationError("variables must be unique")

    polynomials = []
    term_count = 0
    for i, raw_polynomial in enumerate(_list(data["polynomials"], n, "polynomials")):
        raw_terms = _list(raw_polynomial, None, f"polynomials[{i}]")
        term_count += len(raw_terms)
        if term_count > MAX_TOTAL_TERMS:
            raise ValidationError(f"at most {MAX_TOTAL_TERMS} total terms are allowed")
        terms = []
        for j, term in enumerate(raw_terms):
            where = f"polynomials[{i}][{j}]"
            _keys(term, _TERM_KEYS, where)
            coefficient = _rational(term["coefficient"], where + ".coefficient")
            powers = _list(term["powers"], n, where + ".powers")
            if any(type(power) is not int or power < 0 for power in powers):
                raise ValidationError(where + ".powers must be nonnegative integers")
            if sum(powers) > MAX_TOTAL_DEGREE:
                raise ValidationError(f"{where} exceeds total degree {MAX_TOTAL_DEGREE}")
            terms.append((coefficient, tuple(powers)))
        polynomials.append(tuple(terms))

    center = tuple(_rational(value, f"center[{i}]")
                   for i, value in enumerate(_list(data["center"], n, "center")))
    radii = tuple(_rational(value, f"radii[{i}]")
                  for i, value in enumerate(_list(data["radii"], n, "radii")))
    if any(radius <= 0 for radius in radii):
        raise ValidationError("radii must be strictly positive")
    preconditioner = tuple(
        tuple(_rational(value, f"preconditioner[{i}][{j}]")
              for j, value in enumerate(_list(row, n, f"preconditioner[{i}]")))
        for i, row in enumerate(_list(data["preconditioner"], n, "preconditioner"))
    )
    _check_invertible(preconditioner)
    return _Certificate(data["name"], tuple(variables), tuple(polynomials),
                        center, radii, preconditioner)


def _reject_real(value: str) -> Any:
    raise ValidationError(f"JSON floating-point/nonfinite value is forbidden: {value}")


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValidationError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_certificate(path: Any) -> dict[str, Any]:
    """Read at most 1 MiB of strict UTF-8 JSON, reject duplicates, and validate."""
    try:
        with open(path, "rb") as stream:
            raw = stream.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise ValidationError(f"certificate exceeds {MAX_BYTES} bytes")
        data = json.loads(raw.decode("utf-8"), object_pairs_hook=_unique_object,
                          parse_float=_reject_real, parse_constant=_reject_real)
        _parse_certificate(data)
        return data
    except ValidationError:
        raise
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        raise ValidationError(f"cannot read certificate: {exc}") from exc


def _evaluate_point(terms: tuple, point: tuple[Fraction, ...]) -> Fraction:
    result = Fraction(0)
    for coefficient, powers in terms:
        term = coefficient
        for coordinate, power in zip(point, powers):
            term *= coordinate ** power
        result += term
    return result


def _derivative_enclosure(terms: tuple, variable: int,
                          box: tuple[Interval, ...]) -> Interval:
    result = Interval(0)
    for coefficient, powers in terms:
        if powers[variable] == 0 or coefficient == 0:
            continue
        term = Interval(coefficient * powers[variable])
        for j, coordinate in enumerate(box):
            exponent = powers[j] - (1 if j == variable else 0)
            term *= coordinate ** exponent
        result += term
    return result


def analyze(data: Any) -> dict[str, Any]:
    """Recompute all bounds; accept iff q < 1 and d + M r <= r componentwise.

    J encloses DF on B.  E = I - Y J encloses the derivative of the *map*
    T(x) = x - Y F(x).  M is an entrywise bound for |DT|, not DF.  In the
    weighted maximum norm, q = max_i sum_j M_ij r_j/r_i is a Lipschitz bound.
    The self-map test and the contraction test are separately reported.  When
    both hold, Banach's theorem gives exactly one zero in B (Y is nonsingular),
    and ||x*-c||_r <= eta/(1-q), eta = max_i |(YF(c))_i|/r_i.  Per-coordinate
    bounds also use x* in B.  Nothing here asserts global uniqueness.
    """
    certificate = _parse_certificate(data)
    c, r, y = certificate.center, certificate.radii, certificate.preconditioner
    n = len(c)
    box = tuple(Interval(c[i] - r[i], c[i] + r[i]) for i in range(n))
    residual = [_evaluate_point(terms, c) for terms in certificate.polynomials]
    step = [sum((y[i][j] * residual[j] for j in range(n)), Fraction(0))
            for i in range(n)]
    d = [abs(value) for value in step]
    jacobian = [[_derivative_enclosure(terms, j, box) for j in range(n)]
                for terms in certificate.polynomials]
    e = [[Interval(1 if i == j else 0)
          - sum((y[i][k] * jacobian[k][j] for k in range(n)), Interval(0))
          for j in range(n)] for i in range(n)]
    m = [[entry.abs_max() for entry in row] for row in e]
    mr = [sum((m[i][j] * r[j] for j in range(n)), Fraction(0)) for i in range(n)]
    q = max(mr[i] / r[i] for i in range(n))
    eta = max(d[i] / r[i] for i in range(n))
    lhs = [d[i] + mr[i] for i in range(n)]
    slack = [r[i] - lhs[i] for i in range(n)]
    contraction = q < 1
    self_map = all(value >= 0 for value in slack)
    certified = contraction and self_map
    failure_reasons = []
    if not contraction:
        failure_reasons.append("contraction test failed: q must be strictly less than 1")
    for i in range(n):
        if slack[i] < 0:
            failure_reasons.append(f"self-map test failed in coordinate {i}: d + M r exceeds r")
    error = eta / (1 - q) if certified else None
    return {
        "schema_version": 1,
        "name": certificate.name,
        "variables": list(certificate.variables),
        "center": [_rational_string(value) for value in c],
        "radii": [_rational_string(value) for value in r],
        "box": [entry.to_json() for entry in box],
        "preconditioner_invertible": True,
        "residual": [_rational_string(value) for value in residual],
        "step": [_rational_string(value) for value in step],
        "d": [_rational_string(value) for value in d],
        "J": [[entry.to_json() for entry in row] for row in jacobian],
        "E": [[entry.to_json() for entry in row] for row in e],
        "M": [[_rational_string(value) for value in row] for row in m],
        "q": _rational_string(q),
        "eta": _rational_string(eta),
        "selfmap_lhs": [_rational_string(value) for value in lhs],
        "slack": [_rational_string(value) for value in slack],
        "contraction": contraction,
        "self_map": self_map,
        "certified": certified,
        "status": "certified" if certified else "not_certified",
        "failure_reasons": failure_reasons,
        "weighted_error_bound": _rational_string(error) if certified else None,
        "coordinate_error_bounds": ([_rational_string(min(r[i], r[i] * error)) for i in range(n)]
                                    if certified else None),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", help="path to a version-1 certificate JSON file")
    args = parser.parse_args(argv)
    try:
        result = analyze(load_certificate(args.certificate))
    except ValidationError as exc:
        print(json.dumps({"status": "invalid", "certified": False, "error": str(exc)},
                         sort_keys=True, ensure_ascii=True))
        return 2
    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True))
    return 0 if result["certified"] else 1


if __name__ == "__main__":
    sys.exit(main())
