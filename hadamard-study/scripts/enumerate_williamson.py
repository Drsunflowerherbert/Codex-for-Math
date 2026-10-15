"""Complete small normalized symmetric Williamson search, no heuristic pruning.

For odd m, x[0]=1 and x[i]=x[-i]. Enumerate all 2**((m-1)//2)
sequences. Index ordered pairs a<=b by half-lag PAF sum; match exact negative
profiles and require b<=c<=d. This visits each multiset of four sequences once.
Counts refer to these multisets, NOT Hadamard equivalence classes.
"""

import argparse
from collections import defaultdict
from itertools import combinations_with_replacement
import json
from pathlib import Path

from hadamard import sign_bytes, verify, williamson


def sequences(m):
    if m < 1 or m % 2 == 0:
        raise ValueError("positive odd core order required")
    h = (m - 1) // 2
    for mask in range(1 << h):
        first = [1] + [-1 if mask >> i & 1 else 1 for i in range(h)]
        yield tuple(first + first[:0:-1])


def paf(sequence):
    m = len(sequence)
    return tuple(sum(sequence[j] * sequence[(j + t) % m] for j in range(m))
                 for t in range(1, (m + 1) // 2))


def all_quadruples(m):
    seqs = list(sequences(m))
    profiles = [paf(s) for s in seqs]
    buckets = defaultdict(list)
    for a, b in combinations_with_replacement(range(len(seqs)), 2):
        key = tuple(x + y for x, y in zip(profiles[a], profiles[b]))
        buckets[key].append((a, b))
    for key, pairs in buckets.items():
        partners = buckets.get(tuple(-x for x in key), ())
        for a, b in pairs:
            for c, d in partners:
                if b <= c:
                    yield (a, b, c, d)


def feasible_row_sum_types(m):
    return [r for r in combinations_with_replacement(range(1, m + 1, 2), 4)
            if sum(x * x for x in r) == 4 * m]


def study(m):
    seqs = list(sequences(m))
    types = {}
    count = 0
    for indices in all_quadruples(m):
        count += 1
        chosen = [seqs[i] for i in indices]
        row_type = tuple(sorted(abs(sum(s)) for s in chosen))
        if row_type not in types:
            result = verify(williamson(chosen))
            types[row_type] = {"normalized_sequence_indices": list(indices),
                "sequences": ["".join("+" if x == 1 else "-" for x in s)
                              for s in chosen], "matrix_verification": result}
    feasible = feasible_row_sum_types(m)
    return {"core_order": m, "hadamard_order": 4 * m,
            "normalized_sequences": len(seqs),
            "unordered_sequence_pairs_with_repetition": len(seqs) * (len(seqs) + 1) // 2,
            "normalized_sequence_multisets_solving_PAF": count,
            "count_is_not_equivalence_classes": True,
            "arithmetically_feasible_absolute_row_sum_types": [list(r) for r in feasible],
            "unrealized_row_sum_types_in_this_family": [list(r) for r in feasible if r not in types],
            "realized_types_with_one_verified_witness_each": [
                {"absolute_row_sums": list(r), **types[r]} for r in sorted(types)]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-core", type=int, default=15)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.max_core < 1 or args.max_core > 15 or args.max_core % 2 == 0:
        parser.error("this bounded study supports odd max-core from 1 to 15")
    result = {"family": "symmetric circulant Williamson; s[0]=+1; block multiset",
              "complete_for_odd_core_orders": list(range(1, args.max_core + 1, 2)),
              "arithmetic": "exact Python integers; all complementary PAF pair buckets",
              "results": [study(m) for m in range(1, args.max_core + 1, 2)]}
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    for r in result["results"]:
        print(f"m={r['core_order']}: sequences={r['normalized_sequences']}; "
              f"solving_multisets={r['normalized_sequence_multisets_solving_PAF']}; "
              f"unrealized_types={r['unrealized_row_sum_types_in_this_family']}")


if __name__ == "__main__":
    main()
