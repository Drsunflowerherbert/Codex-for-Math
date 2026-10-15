"""Exact pre-generation structural search for odd symmetric Williamson tuples.

Four colors encode column directions; reflection-paired correlation parity
forces all signs. RGS color words quotient exactly the existing block-permutation
semantics. Prefix tests are necessary relaxations; full correlations accept.
No floating point quantity decides a rejection.
"""

import argparse
from collections import Counter
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
import resource
import time


def quotient_edges(m):
    if m < 1 or m % 2 == 0:
        raise ValueError("positive odd core required")
    h = (m - 1) // 2
    graphs = []
    for lag in range(1, h + 1):
        edges = []
        for j in range(m):
            mate = (-j - lag) % m
            if j > mate or j == mate:
                continue
            k = (j + lag) % m
            if j == 0 or k == 0:
                continue
            u, v = min(j, m - j) - 1, min(k, m - k) - 1
            if u == v:
                raise RuntimeError("unremoved reflection-fixed loop")
            edges.append((min(u, v), max(u, v)))
        if len(edges) != h - 1:
            raise RuntimeError("wrong edge-orbit multiplicity")
        graphs.append(tuple(edges))
    return tuple(graphs)


def row_targets(h):
    values = [u for u in range(-h, h + 1) if 2 * u * u + u <= h]
    return tuple(u for u in product(values, repeat=4)
                 if sum(2 * x * x + x for x in u) == h)


@lru_cache(maxsize=None)
def rgs_completions(remaining, used):
    if remaining == 0:
        return 1
    return (used * rgs_completions(remaining - 1, used)
            + (rgs_completions(remaining - 1, used + 1) if used < 4 else 0))


def parity_graphs(graphs, h):
    result = []
    for edges in graphs:
        odd_edges = tuple(edge for edge, multiplicity in Counter(edges).items() if multiplicity % 2)
        neighbors = [[] for _ in range(h)]
        for u, v in odd_edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        if any(len(row) > 2 for row in neighbors):
            raise RuntimeError("unexpected quotient degree")
        result.append((odd_edges, tuple(tuple(row) for row in neighbors)))
    return result


def sign_domains(colors, depth, parities):
    """0 means {-1,+1}; a nonzero sign is forced for every color completion."""
    h = len(colors)
    signs = []
    for edges, neighbors in parities:
        fixed = True
        for u in range(depth, h):
            adj = neighbors[u]
            if adj and not (len(adj) == 2 and adj[0] < depth and adj[1] < depth
                            and colors[adj[0]] == colors[adj[1]]):
                fixed = False
                break
        if not fixed:
            signs.append(0)
        else:
            parity = sum(colors[u] == colors[v] for u, v in edges if u < depth and v < depth) % 2
            signs.append(1 if parity else -1)
    return signs


def distance_to_step_two(value, fixed_sum, free_count):
    lo, hi = fixed_sum - free_count, fixed_sum + free_count
    if value < lo:
        return lo - value
    if value > hi:
        return value - hi
    return (value - lo) % 2


def row_prefix_possible(colors, depth, signs, targets):
    fixed = [0] * 4
    free = [0] * 4
    for i in range(depth):
        c = colors[i]
        if signs[i]:
            fixed[c] += signs[i]
        else:
            free[c] += 1
    remaining = len(colors) - depth
    return any(sum(distance_to_step_two(u[c], fixed[c], free[c]) for c in range(4)) <= remaining
               for u in targets)


def lag_prefix_possible(colors, depth, signs, graphs):
    for t, edges in enumerate(graphs):
        fixed = binary = ternary = 0
        for u, v in edges:
            if u < depth and v < depth:
                if colors[u] != colors[v]:
                    continue
                if signs[u] and signs[v]:
                    fixed += signs[u] * signs[v]
                else:
                    binary += 1
            else:
                ternary += 1
        radius = binary + ternary
        allowed = (0,) if signs[t] == -1 else ((-1,) if signs[t] == 1 else (0, -1))
        if not any(abs(target - fixed) <= radius
                   and (ternary > 0 or (target - fixed - binary) % 2 == 0)
                   for target in allowed):
            return False
    return True


def full_signs(colors, graphs):
    return tuple(1 if sum(colors[u] == colors[v] for u, v in edges) % 2 else -1
                 for edges in graphs)


def full_correlation(colors, signs, graphs):
    return all(1 + signs[t] + 2 * sum(signs[u] * signs[v]
                                      for u, v in edges if colors[u] == colors[v]) == 0
               for t, edges in enumerate(graphs))


def row_square_cost(colors, signs):
    u = [0] * 4
    for color, sign in zip(colors, signs):
        u[color] += sign
    return sum(2 * x * x + x for x in u)


def masks_from_structure(colors, signs):
    masks = [0] * 4
    for j, (color, sign) in enumerate(zip(colors, signs)):
        for c in range(4):
            value = sign * (-1 if c == color else 1)
            if value == -1:
                masks[c] |= 1 << j
    return tuple(sorted(masks))


def search(m, mode="all"):
    if m < 1 or m % 2 == 0 or m > 25 or mode not in ("leaf", "row", "lag", "all"):
        raise ValueError("odd core 1..25 and a valid bounded mode required")
    started = time.perf_counter()
    h = (m - 1) // 2
    graphs = quotient_edges(m)
    parities = parity_graphs(graphs, h)
    targets = row_targets(h)
    canonical_leaves = rgs_completions(h, 0)
    prepared_at = time.perf_counter()
    colors = [-1] * h
    solutions = []
    nodes = [0] * (h + 1)
    row_rejections = [0] * (h + 1)
    lag_rejections = [0] * (h + 1)
    skipped = [0] * (h + 1)
    complete_entered = full_checks = 0

    def visit(depth, used):
        nonlocal complete_entered, full_checks
        nodes[depth] += 1
        if depth == h:
            complete_entered += 1
        if mode != "leaf":
            signs = sign_domains(colors, depth, parities)
            if mode in ("row", "all") and not row_prefix_possible(colors, depth, signs, targets):
                row_rejections[depth] += 1
                if depth < h:
                    skipped[depth] += rgs_completions(h - depth, used)
                return
            if mode in ("lag", "all") and not lag_prefix_possible(colors, depth, signs, graphs):
                lag_rejections[depth] += 1
                if depth < h:
                    skipped[depth] += rgs_completions(h - depth, used)
                return
        if depth == h:
            signs = full_signs(colors, graphs)
            if row_square_cost(colors, signs) != h:
                return
            full_checks += 1
            if full_correlation(colors, signs, graphs):
                solutions.append(masks_from_structure(colors, signs))
            return
        for color in range(min(used + 1, 4)):
            colors[depth] = color
            visit(depth + 1, max(used, color + 1))
        colors[depth] = -1

    visit(0, 0)
    ended = time.perf_counter()
    if len(solutions) != len(set(solutions)):
        raise RuntimeError("RGS emitted duplicate sorted row multiset")
    if sum(skipped) + complete_entered != canonical_leaves:
        raise RuntimeError("prefix subtree coverage accounting mismatch")
    return {"core_order": m, "method": "structural-colors", "mode": mode,
            "counts": {"nodes_entered": sum(nodes), "nodes_by_depth": nodes,
                       "row_rejections_by_depth": row_rejections, "lag_rejections_by_depth": lag_rejections,
                       "raw_RGS_color_leaves": canonical_leaves,
                       "complete_color_assignments_entered": complete_entered,
                       "structural_leaves_skipped_before_completion": sum(skipped),
                       "skipped_leaves_by_prefix_depth": skipped,
                       "full_correlation_checks_after_row_identity": full_checks,
                       "individual_sequence_pool_generated": 0,
                       "stored_pairs": 0,
                       "output_row_masks_constructed_including_repetitions": 4 * len(solutions),
                       "solutions": len(solutions)},
            "solutions": [list(q) for q in sorted(solutions)],
            "timing_seconds": {"preprocessing": prepared_at - started,
                               "search": ended - prepared_at, "total_in_process": ended - started},
            "process_peak_rss_kib_observed_after_search": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "count_semantics": "sorted original normalized symmetric row-mask multisets; RGS quotients exactly row permutations, with repetitions allowed"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core", type=int, required=True)
    parser.add_argument("--mode", choices=("leaf", "row", "lag", "all"), default="all")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = search(args.core, args.mode)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: result[k] for k in ("core_order", "mode", "counts", "timing_seconds")}))


if __name__ == "__main__":
    main()
