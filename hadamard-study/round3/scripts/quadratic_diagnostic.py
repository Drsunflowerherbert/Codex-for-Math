"""Exact bounded obstruction to *constant residual phase* detection.

Eliminating every quadratic monomial is necessary, not sufficient, for equality
of two residual phases under the free four-color completion relaxation. A
monomial involving one physical vertex gives a loop in the required vertex
cover. Enumerate every assigned subset, without guessing a minimum cover.
This says nothing about other rejection criteria or global Hadamard existence.
"""

import argparse
from collections import Counter
import json
from pathlib import Path

from phases import PhaseAlgebra
from structure import quotient_edges


def analyze(m):
    h = m // 2
    algebra = PhaseAlgebra(h, quotient_edges(m))
    phases = (0,) + algebra.initial
    pairs = []
    for i in range(len(phases)):
        for j in range(i):
            difference = phases[i] ^ phases[j]
            edges = set()
            for k, support in enumerate(algebra.supports):
                if support.bit_count() != 2 or not (difference >> k & 1):
                    continue
                vertices = 0
                for v in range(2 * h):
                    if support >> v & 1:
                        vertices |= 1 << (v // 2)
                edges.add(vertices)
            covers = [s for s in range(1 << h) if all(s & edge for edge in edges)]
            minimum = min(s.bit_count() for s in covers)
            witnesses = [s for s in covers if s.bit_count() == minimum]
            pairs.append({"phase_pair": [i, j], "quadratic_vertex_edge_masks": sorted(edges),
                          "minimum_assigned_vertices_to_remove_quadratic_terms": minimum,
                          "number_of_minimum_covers": len(witnesses), "one_minimum_cover_mask": witnesses[0]})
    counts = Counter(p["minimum_assigned_vertices_to_remove_quadratic_terms"] for p in pairs)
    return {"core_order": m, "independent_coordinates": h, "all_assigned_subsets_tested_per_pair": 1 << h,
            "minimum_cover_size_histogram": dict(sorted(counts.items())), "phase_pairs": pairs}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cores", nargs="+", type=int, default=[15, 19, 21, 23])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if any(m < 3 or m % 2 == 0 or m > 23 for m in args.cores):
        parser.error("odd cores3..23 required")
    args.output.write_text(json.dumps({"scope": __doc__, "results": [analyze(m) for m in args.cores]}, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
