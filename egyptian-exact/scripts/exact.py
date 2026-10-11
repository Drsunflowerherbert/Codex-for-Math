#!/usr/bin/env python3
"""Exact rational companion; no floating-point decisions or universal step guard.

This program is mathematical support, not a Lean extraction/refinement theorem.
The public Lean theorem establishes finite-state termination of the transformation.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from math import isqrt
from typing import Iterator


def reciprocal_sum(denominators: tuple[int, ...] | list[int]) -> Fraction:
    if any(d <= 0 for d in denominators):
        raise ValueError("denominators must be positive integers")
    return sum((Fraction(1, d) for d in denominators), Fraction())


def replacement(d: int) -> tuple[int, int]:
    if d < 3:
        raise ValueError("strict-growth replacement requires d >= 3")
    if d % 2:
        k = (d + 1) // 2
        return k, d * k
    k = d // 2
    return k + 1, k * (k + 1)


def cleanup(denominators: list[int] | tuple[int, ...]) -> list[tuple[int, ...]]:
    state = tuple(sorted(denominators))
    value = reciprocal_sum(state)
    if not 0 < value < 1:
        raise ValueError("cleanup requires reciprocal sum strictly between 0 and 1")
    history = [state]
    while len(set(state)) != len(state):
        d = next(d for d, count in sorted(Counter(state).items()) if count >= 2)
        a, b = replacement(d)
        remaining = list(state)
        remaining.remove(d)
        remaining.remove(d)
        next_state = tuple(sorted(remaining + [a, b]))
        assert len(next_state) == len(state)
        assert reciprocal_sum(next_state) == value
        assert sum(next_state) > sum(state)
        history.append(next_state)
        state = next_state
    return history


def sorted_representations(n: int, value: Fraction, minimum: int = 1) -> Iterator[tuple[int, ...]]:
    """Enumerate positive nondecreasing length-n representations of a rational value.

    Head a is bounded by a <= n/value, and the tail has value value-1/a.
    The theorem also proves abstract finiteness for real values; execution requires
    exact rational inputs. Large finite enumeration can still be expensive.
    """
    if n < 0 or minimum < 1:
        raise ValueError("length must be nonnegative and minimum positive")
    if n == 0:
        if value == 0:
            yield ()
        return
    if value <= 0:
        return
    if n == 1:
        a = 1 / value
        if a.denominator == 1 and a.numerator >= minimum:
            yield (a.numerator,)
        return
    upper = int(n / value)
    lower = max(minimum, -((-value.denominator) // value.numerator))
    for a in range(lower, upper + 1):
        residual = value - Fraction(1, a)
        for tail in sorted_representations(n - 1, residual, a):
            yield (a,) + tail


def pad_one(denominators: list[int] | tuple[int, ...], marker: int) -> tuple[int, ...]:
    state = tuple(sorted(denominators))
    if reciprocal_sum(state) != 1 or len(state) < 3 or len(set(state)) != len(state):
        raise ValueError("padding requires a distinct expansion of one with at least three terms")
    if marker not in state:
        raise ValueError("marker must be an input denominator")
    maximum = state[-1]
    d = maximum if marker != maximum else state[-2]
    u, v = d + 1, d * (d + 1)
    if marker == maximum and maximum in (u, v):
        a = next((a for a in range(2, isqrt(d) + 1) if d % a == 0), None)
        if a is None:
            raise ArithmeticError("prime collision contradicts the sum-one invariant")
        b = d // a
        u, v = a * (b + 1), d * (b + 1)
    remaining = list(state)
    remaining.remove(d)
    result = tuple(sorted(remaining + [u, v]))
    assert len(result) == len(state) + 1
    assert len(set(result)) == len(result)
    assert reciprocal_sum(result) == 1
    assert marker in result
    assert max(result) <= maximum * (maximum + 1)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    clean = commands.add_parser("cleanup")
    clean.add_argument("denominators", nargs="+", type=int)
    enum = commands.add_parser("enumerate")
    enum.add_argument("length", type=int)
    enum.add_argument("value", type=Fraction)
    pad = commands.add_parser("pad")
    pad.add_argument("marker", type=int)
    pad.add_argument("denominators", nargs="+", type=int)
    args = parser.parse_args()
    if args.command == "cleanup":
        for i, state in enumerate(cleanup(args.denominators)):
            print(i, list(state), "weight", sum(state), "value", reciprocal_sum(state))
    elif args.command == "enumerate":
        for state in sorted_representations(args.length, args.value):
            print(list(state))
    else:
        print(list(pad_one(args.denominators, args.marker)))


if __name__ == "__main__":
    main()
