#!/usr/bin/env python3
"""Finite exact checks; observed step counts are not universal runtime bounds."""
import json
from fractions import Fraction
from pathlib import Path

from exact import cleanup, pad_one, reciprocal_sum, sorted_representations

records = []
for n in range(1, 5):
    for x in [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]:
        states = list(sorted_representations(n, x))
        max_steps = 0
        for state in states:
            history = cleanup(state)
            final = history[-1]
            assert len(final) == n and len(set(final)) == n
            assert reciprocal_sum(final) == x
            max_steps = max(max_steps, len(history) - 1)
        records.append({"length": n, "value": str(x), "representations": len(states),
                        "observed_max_cleanup_steps": max_steps})
assert list(sorted_representations(2, Fraction(1))) == [(2, 2)]
examples = []
for denominators in [[3, 3], [4, 4], [4, 4, 6], [10, 10, 6, 30]]:
    history = cleanup(denominators)
    examples.append({"input": denominators, "value": str(reciprocal_sum(denominators)),
                     "states": [list(s) for s in history], "weights": [sum(s) for s in history]})
padding_checks = 0
for n in [3, 4]:
    for state in sorted_representations(n, Fraction(1)):
        if len(set(state)) == len(state):
            for marker in state:
                pad_one(state, marker)
                padding_checks += 1
assert pad_one([2, 6, 7, 14, 15, 20, 420], 420) == (2, 6, 7, 14, 15, 22, 220, 420)
padding_checks += 1
result = {"status": "passed", "arithmetic": "fractions.Fraction", "enumeration_checks": records,
          "padding_checks": padding_checks,
          "examples": examples, "scope": "companion validation; not formal refinement or runtime bound"}
Path("evidence/exact-examples.json").write_text(json.dumps(result, indent=2) + "\n")
print(f"PASS: {sum(r['representations'] for r in records)} cleanup states, boundary enumeration, "
      f"{padding_checks} marker padding checks")
