#!/usr/bin/env python3
"""Compare subject code with independent polynomial and complete baselines."""

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys

from independent_anf import exponent_polys
from independent_prefix import lag_possible, row_possible, row_targets, sign_domains
from independent_structure import decode_tuple, edges_by_lag, rgs, sequence_masks


def decode_polynomial(algebra,value):
    out=set()
    while value:
        low=value & -value
        out.add(algebra.supports[low.bit_length()-1])
        value ^= low
    return frozenset(out)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    study=Path(__file__).resolve().parents[2]
    sys.path.insert(0,str(study/"round3/scripts"))
    import structure as subject
    import phase_search as phase_subject
    from phases import (PhaseAlgebra, grouped_lag_possible, grouped_row_possible,
                        signed_sum_possible, row_group_decision)
    baseline=json.loads((study/"round3/reviews/structure-independent.json").read_text())
    polynomial_checks=predicate_checks=valid_prefix_checks=0
    results=[]
    for record in baseline["results"]:
        m=record["core_order"]
        h=m//2
        expected=[tuple(q) for q in record["solutions"]]
        graphs=subject.quotient_edges(m)
        own_edges=edges_by_lag(m)
        if any(Counter(edges)!=Counter(tuple(sorted(e)) for e in own) for edges,own in zip(graphs,own_edges)):
            raise ValueError(("quotient graph mismatch",m))
        targets=subject.row_targets(h)
        if set(targets)!=set(row_targets(h)):
            raise ValueError(("row target mismatch",m))
        algebra=PhaseAlgebra(h,graphs)
        parities=subject.parity_graphs(graphs,h)
        if m<=15:
            prefixes={colors[:k] for colors in rgs(h) for k in range(h+1)}
            for prefix in prefixes:
                k=len(prefix)
                colors=list(prefix)+[-1]*(h-k)
                phases=algebra.initial
                for j,c in enumerate(prefix):
                    phases=algebra.assign(phases,j,c)
                own_polys=exponent_polys(prefix,h,own_edges)
                if tuple(decode_polynomial(algebra,p) for p in phases)!=tuple(own_polys):
                    raise ValueError(("ANF polynomial mismatch",m,prefix))
                polynomial_checks+=h
                own_domains=sign_domains(prefix,h,own_edges)
                signs=subject.sign_domains(colors,k,parities)
                if [(-1,1) if not s else (s,) for s in signs]!=own_domains:
                    raise ValueError(("basic phase-domain mismatch",m,prefix))
                if subject.row_prefix_possible(colors,k,signs,targets)!=row_possible(prefix,own_domains,h,targets):
                    raise ValueError(("step-two row predicate mismatch",m,prefix))
                if subject.lag_prefix_possible(colors,k,signs,graphs)!=lag_possible(prefix,own_domains,own_edges):
                    raise ValueError(("independent-edge lag predicate mismatch",m,prefix))
                predicate_checks+=3
        for strategy in ("natural","collisions"):
            order=phase_subject.coordinate_order(algebra,strategy)
            if sorted(order)!=list(range(h)):
                raise ValueError("coordinate order is not a permutation")
            for q in expected:
                colors,signs=decode_tuple(m,q)
                labels={}
                for vertex in order:
                    labels.setdefault(colors[vertex],len(labels))
                canonical=[labels[c] for c in colors]
                if sequence_masks(canonical,signs)!=q:
                    raise ValueError(("order recanonicalization changed raw multiset",m,q,strategy))
                phases=algebra.initial
                prefix_colors=[-1]*h
                for k in range(h+1):
                    own_polys=exponent_polys(prefix_colors,h,own_edges)
                    if tuple(decode_polynomial(algebra,p) for p in phases)!=tuple(own_polys):
                        raise ValueError(("ordered prefix polynomial mismatch",m,q,k,strategy))
                    polynomial_checks+=h
                    if not grouped_row_possible(prefix_colors,k,phases,targets):
                        raise ValueError(("grouped-row false negative",m,q,k,strategy))
                    for expanded in (False,True):
                        if not grouped_lag_possible(prefix_colors,k,phases,graphs,algebra,expanded):
                            raise ValueError(("grouped-lag false negative",m,q,k,expanded,strategy))
                    valid_prefix_checks+=1
                    if k<h:
                        vertex=order[k]
                        prefix_colors[vertex]=canonical[vertex]
                        phases=algebra.assign(phases,vertex,canonical[vertex])
        modes=("row","relations","expanded") if m<=15 else ("expanded",)
        counts={}
        for strategy in ("natural","collisions"):
            for mode in modes:
                result=phase_subject.search(m,mode,strategy)
                if [tuple(q) for q in result["solutions"]]!=expected:
                    raise ValueError(("complete phase-search tuple mismatch",m,mode,strategy))
                c=result["counts"]
                if c["raw_RGS_color_leaves"]!=record["unpruned_RGS_colorings"] or c["nodes_entered"]!=sum(c["nodes_by_depth"]) or c["complete_color_assignments_entered"]!=c["nodes_by_depth"][-1] or c["complete_color_assignments_entered"]+sum(c["skipped_leaves_by_prefix_depth"])!=c["raw_RGS_color_leaves"]:
                    raise ValueError(("generation-count accounting",m,mode,strategy))
                counts[strategy+"/"+mode]=c
        if m<=15:
            for mode in ("leaf","row","lag","all"):
                result=subject.search(m,mode)
                if [tuple(q) for q in result["solutions"]]!=expected:
                    raise ValueError(("complete basic search tuple mismatch",m,mode))
        results.append({"core_order":m,"exact_tuple_sets_match":True,"phase_modes_checked":list(modes),"phase_generation_counts":counts})
        print(f"m={m}: subject outputs match {len(expected)} exact tuples",flush=True)
    for constant,coefficients,extra,expected_value in (
        (0,(1,),(),False),(1,(1,),(),True),(0,(1,1),(),True),(0,(2,),(),False),
        (2,(),((0,2),),False),(-2,(),((0,2),),True)):
        if signed_sum_possible(constant,coefficients,extra)!=expected_value:
            raise ValueError("constant/domain/multiplicity cache-signature adversary failed")
    empty_scalars=((),(),(),())
    if not row_group_decision((0,0,0,0),empty_scalars,((1,-1,0,0),),0,((1,-1,0,0),)):
        raise ValueError("whole cross-vector sign normalization adversary failed")
    if row_group_decision((0,0,0,0),empty_scalars,((1,1,0,0),),0,((1,-1,0,0),)):
        raise ValueError("coordinatewise cross-vector absolute values would be unsound")
    output={"status":"passed","independent_ANF_polynomials_compared":polynomial_checks,
            "basic_predicates_compared_with_independent_sets":predicate_checks,
            "valid_tuple_prefixes_checked_against_grouped_and_expanded_filters":valid_prefix_checks,
            "scope":"all small natural prefixes through15; every valid prefix through23 in both orders; smallallmodes and moderateexpanded bothorders versus complete independent unpruned baselines",
            "cache_signature_adversarial_cases":"passed: constants, one-sided domains, repeated coefficients, cross-vector whole-sign versus coordinatewise normalization",
            "results":results}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2,sort_keys=True)+"\n")


if __name__ == "__main__":
    main()
