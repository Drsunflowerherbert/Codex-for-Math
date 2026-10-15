#!/usr/bin/env python3
"""Exact local classifier for rational bivariate polynomials of Hessian rank one.

No floating-point arithmetic or third-party packages. See STUDY.md for the
ordinary proof and the source hypotheses behind the finite stopping bounds.
Terms use [x_exponent, y_exponent, exact_rational_coefficient].
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import comb
from pathlib import Path
import sys
from typing import Iterable

Poly = dict[tuple[int, int], Fraction]
TermInput = Iterable[tuple[int, int, str | int | Fraction]]
ZERO = Fraction(0)


def _rational(value: str | int | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (str, int, Fraction)):
        raise ValueError("coefficients must be exact rational strings or integers; floats are rejected")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"invalid rational coefficient: {value!r}") from exc


def parse_terms(terms: TermInput) -> Poly:
    """Collect duplicate terms and reject ambiguous/inexact representations."""
    result: Poly = {}
    for term in terms:
        if not isinstance(term, (list, tuple)) or len(term) != 3:
            raise ValueError("each term must be [nonnegative integer, nonnegative integer, rational]")
        i, j, value = term
        if type(i) is not int or type(j) is not int or min(i, j) < 0:
            raise ValueError("exponents must be nonnegative integers")
        result[i, j] = result.get((i, j), ZERO) + _rational(value)
    return {key: value for key, value in result.items() if value}


def _terms(poly: Poly) -> list[list[int | str]]:
    return [[i, j, str(c)] for (i, j), c in sorted(poly.items())]


def _derivative(poly: Poly, axis: int) -> Poly:
    result = {}
    for (i, j), c in poly.items():
        power = (i, j)[axis]
        if power:
            result[i - (axis == 0), j - (axis == 1)] = power * c
    return result


def normalize(terms: TermInput) -> dict:
    """Return P(X,Y)=sigma*(f(M*(X,Y))-f(0)), with Hessian diag(0,c), c>0.

    The matrix M has rational entries and determinant 1 (shear) or -1 (swap).
    There is no square-root/eigenvector computation in this normalization.
    """
    poly = parse_terms(terms)
    if poly.get((1, 0), ZERO) or poly.get((0, 1), ZERO):
        raise ValueError("the origin must be stationary")
    a, b, c = 2 * poly.get((2, 0), ZERO), poly.get((1, 1), ZERO), 2 * poly.get((0, 2), ZERO)
    if not (a or b or c) or a * c != b * b:
        raise ValueError("the Hessian must have rank exactly one")
    constant = poly.pop((0, 0), ZERO)
    transformed: Poly = {}
    if c:
        slope = -b / c
        matrix = [[Fraction(1), ZERO], [slope, Fraction(1)]]
        for (i, j), value in poly.items():
            for k in range(j + 1):
                key = (i + j - k, k)
                transformed[key] = transformed.get(key, ZERO) + value * comb(j, k) * slope ** (j - k)
    else:
        # Rank one implies b=0 and a!=0, so a coordinate swap suffices.
        matrix = [[ZERO, Fraction(1)], [Fraction(1), ZERO]]
        transformed = {(j, i): value for (i, j), value in poly.items()}
        c = a
    sigma = 1 if c > 0 else -1
    transformed = {key: sigma * value for key, value in transformed.items() if value}
    return {
        "terms": _terms(transformed),
        "sigma": sigma,
        "matrix": [[str(v) for v in row] for row in matrix],
        "constant": str(constant),
        "hessian": [[str(a), str(b)], [str(b), str(2 * poly.get((0, 2), ZERO))]],
        "positive_transverse_second_derivative": str(abs(c)),
    }


def _multiply(left: list[Fraction], right: list[Fraction], order: int) -> list[Fraction]:
    result = [ZERO] * (order + 1)
    right_terms = [(j, value) for j, value in enumerate(right[:order + 1]) if value]
    for i, a in enumerate(left[:order + 1]):
        if a:
            for j, b in right_terms:
                if i + j <= order:
                    result[i + j] += a * b
    return result


def _compose(poly: Poly, phi: list[Fraction], order: int) -> list[Fraction]:
    powers = [[Fraction(1)] + [ZERO] * order]
    for _ in range(max((j for _, j in poly), default=0)):
        powers.append(_multiply(powers[-1], phi, order))
    result = [ZERO] * (order + 1)
    for (i, j), value in poly.items():
        if i <= order:
            for k in range(order - i + 1):
                result[i + k] += value * powers[j][k]
    return result


def _validate_order(order: int, name: str) -> None:
    if type(order) is not int or order < 0:
        raise ValueError(f"{name} must be a nonnegative integer")


def _normalized_poly(terms: TermInput) -> Poly:
    poly = parse_terms(terms)
    if (poly.get((0, 0), ZERO) or poly.get((1, 0), ZERO) or poly.get((0, 1), ZERO)
            or poly.get((2, 0), ZERO) or poly.get((1, 1), ZERO)
            or poly.get((0, 2), ZERO) <= 0):
        raise ValueError("critical_series requires centered normalized terms with Hessian diag(0,c), c>0")
    return poly


def _critical_coefficients(poly: Poly, order: int):
    h = _derivative(poly, 1)
    c = h.get((0, 1), ZERO)
    phi = [ZERO] * (order + 1)
    for n in range(1, order + 1):
        # The new coefficient occurs only in c*phi at this order.
        phi[n] = -_compose(h, phi, n)[n] / c
        yield n, phi, _compose(poly, phi, n)[n]


def critical_series(terms: TermInput, order: int) -> tuple[list[Fraction], list[Fraction]]:
    """Return phi and g through order, for *normalized* terms. Both are exact jets.

    The lists have length order+1, including the constant coefficient. They do
    not assert that the analytic series terminate at this order.
    """
    _validate_order(order, "order")
    poly = _normalized_poly(terms)
    phi, residual = [ZERO] * (order + 1), [ZERO] * (order + 1)
    for n, phi, coefficient in _critical_coefficients(poly, order):
        residual[n] = coefficient
    return phi, residual


def classify(terms: TermInput, bound: str = "bezout", max_order: int | None = None) -> dict:
    """Classify the germ at the origin. A budget can return unresolved, never zero.

    Default bound uses the independently proved conservative Bezout bound.
    The optional Ploski bound uses Theorem 1.1 of arXiv:1305.5102v1, with
    hypotheses checked in STUDY.md. A degree-two input has zero residual.
    """
    if bound not in ("bezout", "ploski"):
        raise ValueError("bound must be 'bezout' or 'ploski'")
    if max_order is not None:
        _validate_order(max_order, "max_order")
    norm = normalize(terms)
    poly = _normalized_poly(norm["terms"])
    degree = max(i + j for i, j in poly)
    required = (degree - 1) ** 2 + 1
    if bound == "ploski" and degree >= 3:
        required -= degree // 2
    computed = min(required, max_order) if max_order is not None else required
    phi = [ZERO] * (computed + 1)
    coefficients: dict[str, str] = {}
    leading_order, leading = None, None
    for n, phi, coefficient in _critical_coefficients(poly, computed):
        if coefficient:
            leading_order, leading, computed = n, coefficient, n
            coefficients[str(n)] = str(coefficient)
            break
    # A truncated jet is not a proof of zero unless the full bound was reached.
    zero_residual = None if computed < required and leading_order is None else leading_order is None
    sigma = norm["sigma"]
    if leading_order is None:
        classification = ("non_strict_local_minimum" if sigma > 0 else "non_strict_local_maximum") if zero_residual else "unresolved"
    elif leading_order % 2 or leading < 0:
        classification = "saddle"
    else:
        classification = "strict_local_minimum" if sigma > 0 else "strict_local_maximum"
    return {
        "schema_version": 1,
        "classification": classification,
        "degree": degree,
        "value_at_origin": norm["constant"],
        "input_hessian": norm["hessian"],
        "sigma": sigma,
        "transform_matrix": norm["matrix"],
        "normalized_terms": norm["terms"],
        "positive_transverse_second_derivative": norm["positive_transverse_second_derivative"],
        "residual_order": leading_order,
        "normalized_leading_coefficient": str(leading) if leading is not None else None,
        "residual_identically_zero": zero_residual,
        "isolated_complex_critical_point": False if zero_residual else (True if leading_order else None),
        "milnor_number": leading_order - 1 if leading_order is not None else None,
        "bound": bound,
        "bound_order": required,
        "computed_order": computed,
        "phi_coefficients": {str(n): str(a) for n, a in enumerate(phi[:computed + 1]) if a},
        "residual_coefficients": coefficients,
        "neighborhood_radius": None,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON with terms, or an examples list")
    parser.add_argument("--example", help="select an id from examples.json; otherwise run every example")
    parser.add_argument("--bound", choices=("bezout", "ploski"), default="bezout")
    parser.add_argument("--max-order", type=int, help="optional computation budget; may return unresolved")
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("input must be a JSON object")
        if "examples" in data:
            selected = [example for example in data["examples"] if args.example is None or example["id"] == args.example]
            if not selected:
                raise ValueError(f"unknown example: {args.example}")
            result = [{"id": example["id"], **classify(example["terms"], args.bound, args.max_order)} for example in selected]
        else:
            if args.example:
                raise ValueError("--example requires a JSON examples collection")
            result = classify(data["terms"], args.bound, args.max_order)
        print(json.dumps(result, indent=2, sort_keys=True))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
