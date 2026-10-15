"""Structural color search with cancellation of shared unknown Boolean phases."""

import argparse
import json
from pathlib import Path
import resource
import time
from collections import Counter

from structure import (full_correlation, masks_from_structure, quotient_edges,
                       rgs_completions, row_square_cost, row_targets)
from phases import (PhaseAlgebra, grouped_lag_possible, grouped_row_possible,
                    sign_of_constant, clear_decision_caches, decision_cache_statistics)


def coordinate_order(algebra, strategy):
    """Choose a fixed order using only quadratic supports, never solution data.

    A shared residual phase needs identical quadratic parts. Greedily prefer
    the next vertex that creates most such potential collisions, counting the
    constant phase as well. Break ties by fewer remaining quadratic terms,
    then the original coordinate number. This is a heuristic, not a theorem
    that it improves pruning.
    """
    if strategy == "natural":
        return tuple(range(algebra.h))
    if strategy != "collisions":
        raise ValueError("unknown coordinate order")
    quadratic = sum(1 << k for k, s in enumerate(algebra.supports) if s.bit_count() == 2)
    remaining = set(range(algebra.h))
    residual = [p & quadratic for p in algebra.initial]
    order = []
    while remaining:
        choices = []
        for vertex in sorted(remaining):
            keep = ~(algebra.contains[2 * vertex] | algebra.contains[2 * vertex + 1])
            next_residual = [p & keep for p in residual]
            groups = Counter([0] + next_residual)
            collisions = sum(n * (n - 1) // 2 for n in groups.values())
            choices.append((-collisions, sum(p.bit_count() for p in next_residual),
                            vertex, next_residual))
        _, _, vertex, residual = min(choices)
        order.append(vertex)
        remaining.remove(vertex)
    return tuple(order)


def search(m, mode="expanded", order_strategy="natural"):
    if m < 1 or m % 2 == 0 or m > 25 or mode not in ("row", "relations", "expanded"):
        raise ValueError("bounded odd 1..25 and valid phase mode required")
    start = time.perf_counter()
    clear_decision_caches()
    h = (m - 1) // 2
    graphs = quotient_edges(m)
    targets = row_targets(h)
    algebra = PhaseAlgebra(h, graphs)
    order = coordinate_order(algebra, order_strategy)
    raw_leaves = rgs_completions(h, 0)
    prepared_at = time.perf_counter()
    colors = [-1] * h
    nodes = [0] * (h + 1)
    row_rejections = [0] * (h + 1)
    lag_rejections = [0] * (h + 1)
    skipped = [0] * (h + 1)
    complete_entered = full_checks = 0
    solutions = []

    def visit(depth, used, phases):
        nonlocal complete_entered, full_checks
        nodes[depth] += 1
        if depth == h:
            complete_entered += 1
        if not grouped_row_possible(colors, depth, phases, targets):
            row_rejections[depth] += 1
            if depth < h:
                skipped[depth] += rgs_completions(h - depth, used)
            return
        if mode != "row" and not grouped_lag_possible(colors, depth, phases, graphs, algebra,
                                                      expanded=mode == "expanded"):
            lag_rejections[depth] += 1
            if depth < h:
                skipped[depth] += rgs_completions(h - depth, used)
            return
        if depth == h:
            if any(p >= 2 for p in phases):
                raise RuntimeError("a phase still contains assigned variables")
            signs = tuple(sign_of_constant(p) for p in phases)
            if row_square_cost(colors, signs) != h:
                raise RuntimeError("row relaxation failed at a complete assignment")
            full_checks += 1
            if full_correlation(colors, signs, graphs):
                solutions.append(masks_from_structure(colors, signs))
            return
        vertex = order[depth]
        for color in range(min(used + 1, 4)):
            colors[vertex] = color
            visit(depth + 1, max(used, color + 1), algebra.assign(phases, vertex, color))
        colors[vertex] = -1

    visit(0, 0, algebra.initial)
    end = time.perf_counter()
    if len(solutions) != len(set(solutions)) or complete_entered + sum(skipped) != raw_leaves:
        raise RuntimeError("coverage or uniqueness accounting failed")
    return {"core_order": m, "method": "structural-phases", "mode": mode,
            "order_strategy": order_strategy, "coordinate_visit_order_one_based": [v + 1 for v in order],
            "counts": {"nodes_entered": sum(nodes), "nodes_by_depth": nodes,
                       "row_rejections_by_depth": row_rejections, "lag_rejections_by_depth": lag_rejections,
                       "raw_RGS_color_leaves": raw_leaves,
                       "complete_color_assignments_entered": complete_entered,
                       "structural_leaves_skipped_before_completion": sum(skipped),
                       "skipped_leaves_by_prefix_depth": skipped,
                       "full_correlation_checks_after_row_identity": full_checks,
                       "individual_sequence_pool_generated": 0, "stored_pairs": 0,
                       "output_row_masks_constructed_including_repetitions": 4 * len(solutions),
                       "solutions": len(solutions)},
            "solutions": [list(q) for q in sorted(solutions)],
            "timing_seconds": {"preprocessing": prepared_at - start, "search": end - prepared_at,
                               "total_in_process": end - start},
            "process_peak_rss_kib_observed_after_search": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "decision_caches": decision_cache_statistics(),
            "count_semantics": "same sorted normalized row-mask multisets as editions1/2; phases grouped only as a necessary relaxation"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core", type=int, required=True)
    parser.add_argument("--mode", choices=("row", "relations", "expanded"), default="expanded")
    parser.add_argument("--order", choices=("natural", "collisions"), default="natural")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = search(args.core, args.mode, args.order)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: result[k] for k in ("core_order", "mode", "counts", "timing_seconds")}))


if __name__ == "__main__":
    main()
