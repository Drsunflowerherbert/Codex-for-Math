#!/usr/bin/env python3
"""Independent brute-force check of the bounded Williamson search.

Uses every four-element multiset directly, every nonzero correlation lag, and
ordinary integer arithmetic.  It does not import the study's enumerator,
matrix constructor, or verifier and does not use pair-bucket matching.
"""

from __future__ import annotations

import argparse
from itertools import combinations_with_replacement, product
import json
from math import comb
from pathlib import Path
import time


def direct_study(m: int) -> dict:
    if m < 1 or m % 2 != 1:
        raise ValueError("expected a positive odd core order")
    h = (m - 1) // 2
    candidates = []
    for independent_signs in product((1, -1), repeat=h):
        first_half = (1,) + independent_signs
        candidates.append(tuple(first_half[min(j, m - j)] for j in range(m)))
    full_correlations = [
        tuple(sum(row[j] * row[(j + lag) % m] for j in range(m))
              for lag in range(1, m))
        for row in candidates
    ]
    considered = 0
    solved = 0
    solution_index_multisets = []
    row_sum_type_counts: dict[tuple[int, ...], int] = {}
    for ia, ib, ic, id_ in combinations_with_replacement(range(len(candidates)), 4):
        considered += 1
        a, b, c, d = (full_correlations[i] for i in (ia, ib, ic, id_))
        for lag_index in range(m - 1):
            if a[lag_index] + b[lag_index] + c[lag_index] + d[lag_index]:
                break
        else:
            solved += 1
            # Encode the independently generated sequences in the study's
            # documented little-endian bit convention solely for comparison.
            solution_index_multisets.append(sorted(
                sum((candidates[i][j] == -1) << (j - 1) for j in range(1, h + 1))
                for i in (ia, ib, ic, id_)
            ))
            sums = tuple(sorted(abs(sum(candidates[i])) for i in (ia, ib, ic, id_)))
            if sum(r * r for r in sums) != 4 * m:
                raise RuntimeError("a solution violates the row-sum identity")
            row_sum_type_counts[sums] = row_sum_type_counts.get(sums, 0) + 1
    expected_considered = comb(len(candidates) + 3, 4)
    if considered != expected_considered:
        raise RuntimeError("brute-force candidate count mismatch")
    feasible = [
        values for values in combinations_with_replacement(range(1, m + 1, 2), 4)
        if sum(value * value for value in values) == 4 * m
    ]
    return {
        "core_order": m,
        "normalized_sequences": len(candidates),
        "four_element_multisets_considered": considered,
        "solving_multisets": solved,
        "solving_sequence_index_multisets": sorted(solution_index_multisets),
        "all_nonzero_lags_checked": list(range(1, m)),
        "realized_absolute_row_sum_types": [
            {"absolute_row_sums": list(values), "solution_multisets": count}
            for values, count in sorted(row_sum_type_counts.items())
        ],
        "arithmetically_feasible_absolute_row_sum_types": [list(values) for values in feasible],
        "unrealized_absolute_row_sum_types": [list(values) for values in feasible if values not in row_sum_type_counts],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    results = []
    for m in range(1, 16, 2):
        result = direct_study(m)
        results.append(result)
        print(f"m={m}: brute multiset candidates={result['four_element_multisets_considered']}; solutions={result['solving_multisets']}", flush=True)
    output = {
        "status": "passed",
        "method": "direct enumeration of every four-element multiset and full nonzero-lag integer autocorrelations",
        "scope": "symmetric sign sequences of odd length 1 through 15, first coordinate +1; sorted block multisets",
        "counts_are_equivalence_classes": False,
        "elapsed_seconds": round(time.perf_counter() - started, 6),
        "results": results,
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
