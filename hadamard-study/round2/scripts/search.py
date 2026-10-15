"""Sound exact reductions for normalized odd symmetric Williamson sequences.

Counts always refer to original little-endian sequence masks and sorted block
multisets. No new symmetry quotient is applied. Integer-vector tests are finite
PSD probes, not a complete Fourier PSD oracle. External code is not imported.
"""

import argparse
from collections import defaultdict
from itertools import combinations_with_replacement
import json
from pathlib import Path
import resource
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from enumerate_williamson import paf, sequences


def square_sums(m):
    squares = {t * t for t in range(1, m + 1, 2)}
    two = {a + b for a in squares for b in squares if a + b <= 4 * m}
    three = {a + b for a in two for b in squares if a + b <= 4 * m}
    return two, three


def triangular_probes(m):
    """Deterministic integer directions only; no cosines, floats or tolerance."""
    out = []
    for f in range(1, (m + 1) // 2):
        triangle = [m - 4 * min(f * j % m, m - (f * j % m)) for j in range(m)]
        vector = tuple(m * x - sum(triangle) for x in triangle)
        norm = sum(x * x for x in vector)
        if norm:
            correlations = tuple(sum(vector[j] * vector[(j + t) % m] for j in range(m))
                                 for t in range(1, (m + 1) // 2))
            out.append((f, vector, norm, correlations))
    return out


def probe_score(profile, m, norm, correlations):
    return m * norm + 2 * sum(a * b for a, b in zip(profile, correlations))


def order3_energy(sequence):
    if len(sequence) % 3:
        raise ValueError("requires a length divisible by three")
    compressed = [sum(sequence[r::3]) for r in range(3)]
    if compressed[1] != compressed[2]:
        raise ValueError("requires a symmetric sequence")
    return (compressed[0] - compressed[1]) ** 2


class Prepared:
    def __init__(self, m, filtered, filters="all"):
        if m < 1 or m % 2 == 0 or m > 23:
            raise ValueError("bounded implementation accepts odd 1<=m<=23")
        self.m = m
        self.full_mask = (1 << ((m - 1) // 2)) - 1
        self.seqs = list(sequences(m))
        self.profiles = [paf(s) for s in self.seqs]
        self.squares = [sum(s) ** 2 for s in self.seqs]
        self.filtered = filtered
        if filters not in ("row", "row-order3", "all"):
            raise ValueError("unknown filter configuration")
        self.filters = filters if filtered else "none"
        self.two, three = square_sums(m)
        self.probes = triangular_probes(m) if filtered and filters == "all" else []
        self.limits = [4 * m * norm for _, _, norm, _ in self.probes]
        self.energies = {}
        self.e3 = {}
        masks = list(range(len(self.seqs)))
        self.counts = {"raw_normalized_sequences": len(masks)}
        if filtered:
            masks = [a for a in masks if 4 * m - self.squares[a] in three]
            self.counts["single_after_row_square_feasibility"] = len(masks)
            if m % 3 == 0 and filters != "row":
                self.e3 = {a: order3_energy(self.seqs[a]) for a in masks}
                masks = [a for a in masks if self.e3[a] <= 4 * m]
            self.counts["single_after_order3_energy"] = len(masks)
            for a in masks:
                self.energies[a] = tuple(probe_score(self.profiles[a], m, norm, corr)
                                         for _, _, norm, corr in self.probes)
            masks = [a for a in masks if all(score <= limit for score, limit in
                                             zip(self.energies[a], self.limits))]
            self.counts["single_after_integer_probes"] = len(masks)
        self.masks = masks
        self.mask_set = set(masks)

    def pair_rejection(self, a, b):
        """Zero passes; 1 row arithmetic; 2 exact order3; 3 integer-vector test."""
        if not self.filtered:
            return 0
        if 4 * self.m - self.squares[a] - self.squares[b] not in self.two:
            return 1
        if self.e3 and self.e3[a] + self.e3[b] > 4 * self.m:
            return 2
        if any(x + y > limit for x, y, limit in
               zip(self.energies[a], self.energies[b], self.limits)):
            return 3
        return 0


def pair_search(prepared, product_key=False):
    p = prepared
    buckets = defaultdict(list)
    pairs_considered = after_row = after_order3 = after_probes = 0
    if not p.filtered:
        # Keep the baseline's main loop free of filter calls/stage counters.
        # Its counts follow analytically from visiting every unordered pair.
        for a, b in combinations_with_replacement(p.masks, 2):
            profile = tuple(x + y for x, y in zip(p.profiles[a], p.profiles[b]))
            buckets[profile].append((a, b))
        pairs_considered = len(p.masks) * (len(p.masks) + 1) // 2
        after_row = after_order3 = after_probes = pairs_considered
    else:
        for a, b in combinations_with_replacement(p.masks, 2):
            pairs_considered += 1
            reason = p.pair_rejection(a, b)
            if reason == 1:
                continue
            after_row += 1
            if reason == 2:
                continue
            after_order3 += 1
            if reason == 3:
                continue
            after_probes += 1
            profile = tuple(x + y for x, y in zip(p.profiles[a], p.profiles[b]))
            key = (a ^ b,) + profile if product_key else profile
            buckets[key].append((a, b))
    solutions = []
    joined_pair_combinations = 0
    for key, pairs in buckets.items():
        if product_key:
            target = (p.full_mask ^ key[0],) + tuple(-x for x in key[1:])
        else:
            target = tuple(-x for x in key)
        partners = buckets.get(target, ())
        joined_pair_combinations += len(pairs) * len(partners)
        for a, b in pairs:
            for c, d in partners:
                if b <= c:
                    solutions.append((a, b, c, d))
    counts = {**p.counts, "pairs_considered_after_single_filters": pairs_considered,
              "pair_after_row_square_feasibility": after_row,
              "pair_after_order3_energy": after_order3,
              "pair_after_integer_probes": after_probes,
              "stored_pairs": after_probes, "bucket_keys": len(buckets),
              "joined_pair_combinations_before_sorted_order_test": joined_pair_combinations,
              "solving_normalized_multisets": len(solutions)}
    return sorted(solutions), counts


def product_search(prepared):
    """Fourth original sequence mask is forced; pair table is not stored."""
    p = prepared
    counts = {**p.counts, "triples_visited": 0,
              "after_forced_fourth_mask_and_order": 0, "after_quadruple_row_square_sum": 0,
              "after_pair_energy_tests": 0, "full_PAF_quadruples_tested": 0,
              "stored_pairs": 0}
    solutions = []
    for a, b, c in combinations_with_replacement(p.masks, 3):
        counts["triples_visited"] += 1
        d = p.full_mask ^ a ^ b ^ c
        if d < c or d not in p.mask_set:
            continue
        counts["after_forced_fourth_mask_and_order"] += 1
        if sum(p.squares[i] for i in (a, b, c, d)) != 4 * p.m:
            continue
        counts["after_quadruple_row_square_sum"] += 1
        if p.pair_rejection(a, b) or p.pair_rejection(c, d):
            continue
        counts["after_pair_energy_tests"] += 1
        counts["full_PAF_quadruples_tested"] += 1
        if all(sum(p.profiles[i][t] for i in (a, b, c, d)) == 0
               for t in range((p.m - 1) // 2)):
            solutions.append((a, b, c, d))
    counts["solving_normalized_multisets"] = len(solutions)
    return sorted(solutions), counts


def run(m, method, filters="all"):
    started = time.perf_counter()
    prepared = Prepared(m, filtered=method != "baseline-mitm", filters=filters)
    prepared_at = time.perf_counter()
    if method == "product-triples":
        solutions, counts = product_search(prepared)
    else:
        solutions, counts = pair_search(prepared, product_key=method == "filtered-mitm-product-key")
    ended = time.perf_counter()
    # On Linux ru_maxrss is KiB; the protocol requires Linux and a fresh process.
    return {"core_order": m, "method": method, "enabled_filters": prepared.filters, "counts": counts,
            "solutions": [list(q) for q in solutions],
            "timing_seconds": {"preprocessing": prepared_at - started,
                               "search": ended - prepared_at, "total_in_process": ended - started},
            "process_peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "memory_measurement": "Linux ru_maxrss, entire fresh worker process including interpreter and preprocessing",
            "count_domain": "original first-entry-positive symmetric sequence masks; sorted four-multisets; repetition allowed"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core", type=int, required=True)
    parser.add_argument("--method", choices=("baseline-mitm", "filtered-mitm", "filtered-mitm-product-key", "product-triples"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--filters", choices=("row", "row-order3", "all"), default="all")
    args = parser.parse_args()
    result = run(args.core, args.method, args.filters)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"core": args.core, "method": args.method, "solutions": len(result["solutions"]),
                      "seconds": result["timing_seconds"], "peak_rss_kib": result["process_peak_rss_kib"]}))


if __name__ == "__main__":
    main()
