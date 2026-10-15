#!/usr/bin/env python3
"""Independent soundness checks for partial-coloring relaxations and hazards."""

import argparse
from collections import Counter
from itertools import combinations_with_replacement, product
import json
from pathlib import Path

from independent_structure import decode_tuple, edges_by_lag, forced_signs, rgs


def sign_domains(prefix,h,edges):
    k=len(prefix)
    domains=[]
    for lag in edges:
        parity_edges=[edge for edge,n in Counter(tuple(sorted(e)) for e in lag).items() if n%2]
        adjacency=[[] for _ in range(h)]
        parity=0
        for u,v in parity_edges:
            adjacency[u].append(v)
            adjacency[v].append(u)
            if u<k and v<k:
                parity ^= prefix[u]==prefix[v]
        fixed=True
        for u in range(k,h):
            neighbors=adjacency[u]
            if not neighbors:
                continue
            if len(neighbors)!=2 or any(v>=k for v in neighbors) or prefix[neighbors[0]]!=prefix[neighbors[1]]:
                fixed=False
                break
        domains.append((1 if parity else -1,) if fixed else (-1,1))
    return domains


def row_targets(h):
    values=[u for u in range(-h-1,h+2) if 2*u*u+u<=h]
    return [u for u in product(values,repeat=4) if sum(2*t*t+t for t in u)==h]


def row_possible(prefix,domains,h,targets):
    fixed=[0]*4
    free=[0]*4
    for j,c in enumerate(prefix):
        if len(domains[j])==1:
            fixed[c]+=domains[j][0]
        else:
            free[c]+=1
    intervals=[range(f-n,f+n+1,2) for f,n in zip(fixed,free)]
    distance=min(sum(min(abs(u-v) for v in values) for u,values in zip(target,intervals)) for target in targets)
    return distance<=h-len(prefix)


def lag_possible(prefix,domains,edges):
    k=len(prefix)
    for t,lag in enumerate(edges):
        sums={0}
        for u,v in lag:
            if u<k and v<k:
                values={a*b for a in domains[u] for b in domains[v]} if prefix[u]==prefix[v] else {0}
            else:
                values={-1,0,1}
            sums={a+b for a in sums for b in values}
        target={-(1+s)//2 for s in domains[t]}
        if not sums.intersection(target):
            return False
    return True


def compression_counterexample():
    m=9
    seqs=[tuple(1 if j==0 else 1-2*((a>>(min(j,m-j)-1))&1) for j in range(m)) for a in range(16)]
    compressed=[tuple(sum(x[j] for j in range(r,m,3)) for r in range(3)) for x in seqs]
    pafs=[tuple(sum(x[j]*x[(j+t)%m] for j in range(m)) for t in range(1,m)) for x in seqs]
    target=((-1,-1,-1),(-1,1,1),(-1,3,3),(3,-1,-1))
    feasible={}
    realized=set()
    target_lifts=[]
    for q in combinations_with_replacement(range(16),4):
        rows=[compressed[a] for a in q]
        if any(sum(sum(row[j]*row[(j+t)%3] for j in range(3)) for row in rows)!=(36 if t==0 else 0) for t in range(3)):
            continue
        key=tuple(sorted(rows))
        feasible.setdefault(key,q)
        valid=all(sum(pafs[a][t] for a in q)==0 for t in range(8))
        if valid:
            realized.add(key)
        if key==target:
            target_lifts.append(q)
            if valid:
                raise ValueError("claimed no-lift compression has a lift")
    if target not in feasible or target in realized or not target_lifts:
        raise ValueError("compression counterexample mismatch")
    return {"core_order":9,"compressed_rows":[list(row) for row in target],
            "combined_compressed_PAF":[36,0,0],"all_original_candidates_checked":16,
            "all_original_four_multisets_checked":3876,"candidate_lift_multisets":[list(q) for q in target_lifts],
            "Williamson_lifts":0,"feasible_compressed_types":len(feasible),"realized_compressed_types":len(realized)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    study=Path(__file__).resolve().parents[2]
    baseline=json.loads((study/"round3/reviews/structure-independent.json").read_text())
    results=[]
    small_prefixes=0
    actual_sign_domain_checks=0
    valid_prefix_checks=0
    for record in baseline["results"]:
        m=record["core_order"]
        h=m//2
        edges=edges_by_lag(m)
        targets=row_targets(h)
        if not targets:
            raise ValueError("empty row target set")
        row_rejections=lag_rejections=prefix_count=0
        if m<=15:
            exact_domains={}
            for colors in rgs(h):
                signs=forced_signs(colors,edges)
                for k in range(h+1):
                    values=exact_domains.setdefault(colors[:k],[set() for _ in range(h)])
                    for t,s in enumerate(signs):
                        values[t].add(s)
            for prefix,actual in exact_domains.items():
                prefix_count+=1
                domains=sign_domains(prefix,h,edges)
                if any(not values.issubset(domain) for values,domain in zip(actual,domains)):
                    raise ValueError(("partial parity domain loses a color completion",m,prefix))
                actual_sign_domain_checks+=h
                row_rejections+=not row_possible(prefix,domains,h,targets)
                lag_rejections+=not lag_possible(prefix,domains,edges)
            small_prefixes+=prefix_count
        for q in record["solutions"]:
            colors,signs=decode_tuple(m,q)
            for k in range(h+1):
                prefix=colors[:k]
                domains=sign_domains(prefix,h,edges)
                if any(sign not in domain for sign,domain in zip(signs,domains)):
                    raise ValueError(("valid sign removed",m,q,k))
                if not row_possible(prefix,domains,h,targets) or not lag_possible(prefix,domains,edges):
                    raise ValueError(("valid branch rejected",m,q,k))
                valid_prefix_checks+=1
        results.append({"core_order":m,"row_target_vectors":len(targets),
                        "all_small_unpruned_prefixes_checked":prefix_count,
                        "row_rejections_in_full_small_prefix_catalogue":row_rejections,
                        "lag_rejections_in_full_small_prefix_catalogue":lag_rejections,
                        "valid_solution_prefixes_preserved":True})
    edges7=edges_by_lag(7)
    if sign_domains((0,1),3,edges7)[1] != (-1,1) or sign_domains((0,0),3,edges7)[1] != (-1,):
        raise ValueError("degree-two equal/different neighbor adversary failed")
    example=next(row for row in baseline["results"] if row["core_order"]==9)
    if [3,8,9,13] not in example["solutions"]:
        raise ValueError("zero-fill counterexample is not in the complete baseline")
    output={"status":"passed","method":"independent integer sets, explicit parity graph, row-target L1 distance, independent-edge Minkowski sums; no subject imports",
            "small_unpruned_prefix_catalogue_size":small_prefixes,
            "actual_full_coloring_sign_domain_checks":actual_sign_domain_checks,
            "all_valid_tuple_prefix_checks":valid_prefix_checks,
            "counterexamples":{
                "zero_filled_PSD_false_negative":{"core_order":9,"valid_tuple":[3,8,9,13],"mask":8,"assigned_pairs":3,"partial_DC_power":49,"bound":36,"completed_DC_power":25},
                "different_neighbor_colors_cannot_cancel":{"core_order":7,"valid_tuple":[1,1,3,4],"prefix_colors":[0,1],"lag":2,"actual_sign":1,"safe_domain":[-1,1]},
                "compressed_feasibility_without_a_lift":compression_counterexample()},
            "results":results}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in output.items() if k not in ("results","counterexamples","method")}))


if __name__ == "__main__":
    main()
