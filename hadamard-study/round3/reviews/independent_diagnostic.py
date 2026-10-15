#!/usr/bin/env python3
"""Independent quadratic-cover diagnostic and a grouped-filter false positive."""

import argparse
from collections import Counter, defaultdict
from itertools import combinations, product
import json
from pathlib import Path

from independent_anf import ONE, ZERO, bit_poly, exponent_polys, phase
from independent_prefix import row_targets
from independent_structure import check_structure, edges_by_lag, forced_signs


def minimum_covers(h,edges):
    for size in range(h+1):
        covers=[]
        for chosen in combinations(range(h),size):
            vertices=set(chosen)
            if all(vertices.intersection(edge) for edge in edges):
                covers.append(sum(1<<v for v in chosen))
        if covers:
            return size,covers
    raise ValueError("a vertex cover must exist")


def grouped_row_states(colors,polys):
    groups=defaultdict(lambda:[0]*4)
    for i,c in enumerate(colors):
        if c>=0:
            sign,residual=phase(polys[i])
            groups[residual][c]+=sign
    states={tuple(groups.pop(ZERO,[0]*4))}
    for vector in groups.values():
        states={tuple(a[c]+s*vector[c] for c in range(4)) for a in states for s in (-1,1)}
    return states


def expanded_lag_sets(colors,polys,edges):
    possible=[]
    for t,lag in enumerate(edges):
        groups=defaultdict(int)
        sign,residual=phase(polys[t])
        groups[residual]+=2*sign
        for u,v in lag:
            p=polys[u]^polys[v]
            a=bit_poly(colors,u,0)^bit_poly(colors,v,0)
            b=bit_poly(colors,u,1)^bit_poly(colors,v,1)
            for polynomial in (p,p^a,p^b,p^a^b):
                sign,residual=phase(polynomial)
                groups[residual]+=sign
        states={2+groups.pop(ZERO,0)}
        for coefficient in groups.values():
            states={a+b for a in states for b in (-coefficient,coefficient)}
        possible.append(states)
    return possible


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    study=Path(__file__).resolve().parents[2]
    reference=json.loads((study/"round3/evidence/quadratic-obstruction.json").read_text())
    results=[]
    for record in reference["results"]:
        m=record["core_order"]
        h=m//2
        polys=[ZERO]+exponent_polys((),h,edges_by_lag(m))
        histogram=Counter()
        for pair in record["phase_pairs"]:
            i,j=pair["phase_pair"]
            physical_edges={frozenset(v//2 for v in range(2*h) if monomial>>v&1)
                            for monomial in polys[i]^polys[j] if monomial.bit_count()==2}
            size,covers=minimum_covers(h,physical_edges)
            encoded=sorted(sum(1<<v for v in edge) for edge in physical_edges)
            if encoded!=pair["quadratic_vertex_edge_masks"] or size!=pair["minimum_assigned_vertices_to_remove_quadratic_terms"] or len(covers)!=pair["number_of_minimum_covers"] or pair["one_minimum_cover_mask"] not in covers:
                raise ValueError(("quadratic-cover diagnostic mismatch",m,i,j))
            histogram[size]+=1
        if {str(k):v for k,v in sorted(histogram.items())}!=record["minimum_cover_size_histogram"]:
            raise ValueError("minimum-cover histogram mismatch")
        results.append({"core_order":m,"phase_pairs_checked":sum(histogram.values()),
                        "minimum_cover_size_histogram":dict(sorted(histogram.items()))})
    colors=(0,0,0,1,-1)
    edges=edges_by_lag(11)
    polys=exponent_polys(colors,5,edges)
    states=grouped_row_states(colors,polys)
    distance=min(sum(abs(u-v) for u,v in zip(target,state)) for target in row_targets(5) for state in states)
    lag_sets=expanded_lag_sets(colors,polys,edges)
    if distance>1 or any(0 not in values for values in lag_sets):
        raise ValueError("claimed grouped-filter false-positive prefix is rejected")
    completions=[]
    for last in range(4):
        complete=colors[:-1]+(last,)
        signs=forced_signs(complete,edges)
        valid=check_structure(complete,signs,edges)
        if valid:
            raise ValueError("claimed no-completion prefix has a completion")
        completions.append({"last_color":last,"forced_signs":list(signs),"full_correlation_passes":False,
                            "is_canonical_RGS_extension":last<3})
    output={"status":"passed","method":"independent monomial-set algebra and increasing-cardinality vertex-subset enumeration; no subject imports",
            "scope":"quadratic-cover obstruction concerns formal residual ANF equality under free four-color completion, not every logical pruning criterion",
            "results":results,
            "grouped_filter_false_positive":{"core_order":11,"partial_colors":list(colors),
                "exact_relaxed_row_target_distance":distance,
                "each_expanded_lag_sumset_contains_zero":True,"all_four_free_color_completions_fail":completions}}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":"passed","phase_pairs_checked":sum(r['phase_pairs_checked'] for r in results)}))


if __name__ == "__main__":
    main()
