"""Experimental exact branch-and-bound comparator for eligible single sequences.

The output domain is the original round2 mask: bit i selects x[i+1]=-1,
x[0]=1, and x[j]=x[-j]. No symmetry quotient or Williamson quadruple search
is performed. Leaf eligibility is exactly round2 Prepared(m, filtered=True).
All arithmetic and pruning bounds use Python integers. No external code is
downloaded; round2 is imported only when explicitly running validation.

For a probe v and a partial sequence, C_x^T v=a+sum(y_i b_i), where
b_i[j]=v[j+i]+v[j-i]. With R[j]=sum_unknown abs(b_i[j]), the bound
sum_j max(0, abs(a[j])-R[j])**2 is safe despite all possible cancellation.
It relaxes the shared signs independently at each coordinate and may be weak.
"""

import argparse
from dataclasses import dataclass
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys
import time


def row_squares(m):
    """W and the exact finite sumset W+W+W used in round2."""
    squares = {r * r for r in range(1, m + 1, 2)}
    two = {a + b for a in squares for b in squares if a + b <= 4 * m}
    three = {a + b for a in two for b in squares if a + b <= 4 * m}
    return squares, three


def triangular_vectors(m):
    """Reproduce the complete round2 deterministic integer probe bank."""
    out = []
    for f in range(1, (m + 1) // 2):
        triangle = [m - 4 * min(f * j % m, m - f * j % m) for j in range(m)]
        center = sum(triangle)
        vector = tuple(m * value - center for value in triangle)
        if any(vector):
            out.append((f"triangular-{f}", vector))
    return out


def sequence_from_mask(m, mask):
    half = [1] + [-1 if mask >> i & 1 else 1 for i in range((m - 1) // 2)]
    return tuple(half + half[:0:-1])


def direct_probe_energy(sequence, vector):
    """Compute ||C_x^T v||^2 directly, without a PAF or float."""
    m = len(sequence)
    return sum(sum(sequence[i] * vector[(j + i) % m] for i in range(m)) ** 2
               for j in range(m))


def exact_leaf_rejection(sequence, three_squares, triangular):
    """Full round2 single conditions; returns the first failing stage."""
    m = len(sequence)
    if 4 * m - sum(sequence) ** 2 not in three_squares:
        return "row"
    if m % 3 == 0:
        compressed = tuple(sum(sequence[r::3]) for r in range(3))
        assert compressed[1] == compressed[2]
        if (compressed[0] - compressed[1]) ** 2 > 4 * m:
            return "order3"
    for _, vector in triangular:
        if direct_probe_energy(sequence, vector) > 4 * m * sum(x * x for x in vector):
            return "triangular"
    return None


@dataclass(frozen=True)
class Probe:
    name: str
    stage: str
    vector: tuple
    coefficients: tuple
    suffix_radii: tuple
    limit: int


def make_probe(m, name, stage, vector):
    h = (m - 1) // 2
    coefficients = tuple(tuple(vector[(j + i) % m] + vector[(j - i) % m]
                               for j in range(m)) for i in range(1, h + 1))
    radii = [None] * (h + 1)
    radii[h] = (0,) * m
    for depth in range(h - 1, -1, -1):
        radii[depth] = tuple(r + abs(b) for r, b in
                            zip(radii[depth + 1], coefficients[depth]))
    return Probe(name, stage, vector, coefficients, tuple(radii),
                 4 * m * sum(v * v for v in vector))


def energy_lower_bound(partial, radius):
    return sum(max(0, abs(a) - r) ** 2 for a, r in zip(partial, radius))


def attainable_rows(partial_row, unknown):
    """Every value occurs: k positive unknowns give this arithmetic progression."""
    return tuple(partial_row - 2 * unknown + 4 * k for k in range(unknown + 1))


def audit_node(m, depth, partial_row, probes, partials):
    """Exhaustively verify attainable rows and bound safety on this small node."""
    unknown = (m - 1) // 2 - depth
    assignments = list(product((-1, 1), repeat=unknown))
    rows = {partial_row + 2 * sum(signs) for signs in assignments}
    assert rows == set(attainable_rows(partial_row, unknown))
    for probe, partial in zip(probes, partials):
        minimum_energy = min(sum(
            (a + sum(sign * coefficients[j] for sign, coefficients in
                     zip(signs, probe.coefficients[depth:]))) ** 2
            for j, a in enumerate(partial)) for signs in assignments)
        bound = energy_lower_bound(partial, probe.suffix_radii[depth])
        assert bound <= minimum_energy, (m, depth, probe.name, bound, minimum_energy)
    return len(probes)


def search(m, pruning_probes="all", audit_bounds=False):
    """Return sorted original masks and disjoint, depth-resolved pruning counts.

    Every visited node first tests exact row attainability, then the selected
    probe stages in constant/order3/triangular order. A pruned node at depth d
    accounts for 2**(h-d) original masks. Nodes at depth h still undergo the
    independent complete leaf checks. Disabling a pruning probe never disables
    its corresponding leaf condition.
    """
    if m < 1 or m % 2 == 0 or m > 23:
        raise ValueError("bounded comparator accepts odd 1<=m<=23")
    if pruning_probes not in ("none", "triangular", "all"):
        raise ValueError("unknown pruning probe configuration")
    if audit_bounds and m > 11:
        raise ValueError("exhaustive per-node bound audit is limited to m<=11")
    started = time.perf_counter()
    h = (m - 1) // 2
    _, three = row_squares(m)
    triangular = triangular_vectors(m)
    probes = []
    if pruning_probes == "all":
        probes.append(make_probe(m, "constant", "constant", (1,) * m))
        if m % 3 == 0:
            order3 = tuple(2 if j % 3 == 0 else -1 for j in range(m))
            probes.append(make_probe(m, "order3", "order3", order3))
    if pruning_probes != "none":
        probes.extend(make_probe(m, name, "triangular", vector)
                      for name, vector in triangular)
    stages = ("row", "constant", "order3", "triangular")
    counts = {
        "raw_original_masks": 1 << h,
        "unpruned_full_binary_tree_nodes": (1 << (h + 1)) - 1,
        "nodes_visited": 0,
        "nodes_by_depth": [0] * (h + 1),
        "nodes_reaching_stage": {stage: 0 for stage in stages},
        "nodes_pruned_by_stage": {stage: 0 for stage in stages},
        "partial_nodes_pruned_by_stage": {stage: 0 for stage in stages},
        "nodes_pruned_by_stage_and_depth": {stage: [0] * (h + 1) for stage in stages},
        "original_masks_covered_by_pruning_stage": {stage: 0 for stage in stages},
        "leaf_checks_reached": 0,
        "leaf_rejected_by_stage": {stage: 0 for stage in ("row", "order3", "triangular")},
        "bound_audit_nodes": 0,
        "bound_audit_probe_comparisons": 0,
    }
    masks = []

    def prune(stage, depth):
        counts["nodes_pruned_by_stage"][stage] += 1
        counts["nodes_pruned_by_stage_and_depth"][stage][depth] += 1
        counts["original_masks_covered_by_pruning_stage"][stage] += 1 << (h - depth)
        if depth < h:
            counts["partial_nodes_pruned_by_stage"][stage] += 1

    def visit(depth, mask, partial_row, partials):
        counts["nodes_visited"] += 1
        counts["nodes_by_depth"][depth] += 1
        if audit_bounds:
            counts["bound_audit_nodes"] += 1
            counts["bound_audit_probe_comparisons"] += audit_node(
                m, depth, partial_row, probes, partials)
        counts["nodes_reaching_stage"]["row"] += 1
        if not any(4 * m - r * r in three for r in attainable_rows(partial_row, h - depth)):
            prune("row", depth)
            return
        for stage in stages[1:]:
            stage_probes = [(p, a) for p, a in zip(probes, partials) if p.stage == stage]
            if not stage_probes:
                continue
            counts["nodes_reaching_stage"][stage] += 1
            if any(energy_lower_bound(a, p.suffix_radii[depth]) > p.limit
                   for p, a in stage_probes):
                prune(stage, depth)
                return
        if depth == h:
            counts["leaf_checks_reached"] += 1
            rejection = exact_leaf_rejection(sequence_from_mask(m, mask), three, triangular)
            if rejection:
                counts["leaf_rejected_by_stage"][rejection] += 1
            else:
                masks.append(mask)
            return
        for sign, next_mask in ((1, mask), (-1, mask | (1 << depth))):
            next_partials = tuple(tuple(a + sign * b for a, b in
                                        zip(partial, probe.coefficients[depth]))
                                  for probe, partial in zip(probes, partials))
            visit(depth + 1, next_mask, partial_row + 2 * sign, next_partials)

    visit(0, 0, 1, tuple(probe.vector for probe in probes))
    masks.sort()
    assert len(masks) == len(set(masks))
    counts["eligible_single_masks"] = len(masks)
    accounted_masks = (sum(counts["original_masks_covered_by_pruning_stage"].values())
                       + counts["leaf_checks_reached"])
    assert accounted_masks == 1 << h, (m, accounted_masks)
    assert counts["leaf_checks_reached"] == len(masks) + sum(counts["leaf_rejected_by_stage"].values())
    return {
        "core_order": m,
        "pruning_probes": pruning_probes,
        "pruning_probe_names": [p.name for p in probes],
        "leaf_conditions": "round2 all: exact row-square residual, order3 if divisible by 3, full triangular bank",
        "mask_domain": "original little-endian masks; x[0]=+1 and x[i]=x[-i]; no symmetry quotient",
        "eligible_masks": masks,
        "counts": counts,
        "elapsed_seconds": time.perf_counter() - started,
    }


def load_round2():
    path = Path(__file__).resolve().parents[2] / "round2" / "scripts" / "search.py"
    spec = importlib.util.spec_from_file_location("round2_partial_single_reference", path)
    module = importlib.util.module_from_spec(spec)
    # The reference's imports are its own repository's code, never downloaded.
    spec.loader.exec_module(module)
    return module


def validate(max_core=21, audit_max_core=11):
    if max_core < 1 or max_core % 2 == 0 or max_core > 21:
        raise ValueError("validation accepts odd max-core from 1 to 21")
    if audit_max_core < 1 or audit_max_core % 2 == 0 or audit_max_core > 11:
        raise ValueError("bound audit accepts odd max-core from 1 to 11")
    reference = load_round2()
    results = []
    for m in range(1, max_core + 1, 2):
        prepared = reference.Prepared(m, filtered=True)
        triangular = triangular_vectors(m)
        assert [(name, vector) for name, vector in triangular] == [
            (f"triangular-{frequency}", vector) for frequency, vector, _, _ in prepared.probes]
        _, three = row_squares(m)
        direct_masks = [mask for mask in range(1 << ((m - 1) // 2))
                        if exact_leaf_rejection(sequence_from_mask(m, mask), three, triangular) is None]
        assert direct_masks == prepared.masks, (m, "direct leaf conditions differ from round2")
        configurations = []
        for configuration in ("none", "triangular", "all"):
            result = search(m, configuration, audit_bounds=m <= audit_max_core)
            assert result["eligible_masks"] == prepared.masks, (m, configuration)
            result["exact_mask_list_matches_round2"] = True
            configurations.append(result)
        results.append({"core_order": m, "round2_counts": prepared.counts,
                        "independent_direct_leaf_masks_match_round2": True,
                        "configurations": configurations})
    return {"validation": "passed", "max_core": max_core,
            "exhaustive_bound_audit_max_core": min(max_core, audit_max_core),
            "reference": "round2/scripts/search.py Prepared(m, filtered=True)",
            "results": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--core", type=int, help="enumerate one odd core order, at most 23")
    mode.add_argument("--validate-max-core", type=int, help="audit every odd core up to this value, at most 21")
    parser.add_argument("--pruning-probes", choices=("none", "triangular", "all"), default="all")
    parser.add_argument("--audit-bounds", action="store_true", help="exhaustively verify every visited node; requires core<=11")
    parser.add_argument("--audit-max-core", type=int, default=11, help="maximum core for exhaustive per-node bound checks during validation")
    parser.add_argument("--output", type=Path, help="optional JSON path; stdout is used otherwise")
    args = parser.parse_args()
    try:
        if args.validate_max_core is not None:
            result = validate(args.validate_max_core, args.audit_max_core)
        else:
            result = search(args.core, args.pruning_probes, args.audit_bounds)
    except ValueError as error:
        parser.error(str(error))
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    else:
        sys.stdout.write(encoded)


if __name__ == "__main__":
    main()
