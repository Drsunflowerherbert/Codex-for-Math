#!/usr/bin/env python3
"""Unfiltered moderate baseline: support-overlap PAFs and full-lag byte keys.

No study implementation is imported for enumeration. Every original sequence
and unordered pair with repetitions is retained. Root filtered results are
imported only after each independent complete search has finished.
"""

import argparse
from collections import defaultdict
import gc
import importlib.util
from itertools import combinations_with_replacement
import json
from pathlib import Path
import time


def enumerate_independently(m):
    n=1 << (m//2)
    profiles=[]
    for a in range(n):
        negatives=sum(1 << j for j in range(1,m)
                      if a >> (min(j,m-j)-1) & 1)
        weight=negatives.bit_count()
        profiles.append(tuple(m-4*weight+4*(negatives & ((negatives>>t) | ((negatives & ((1<<t)-1))<<(m-t)))).bit_count()
                              for t in range(1,m)))
    buckets=defaultdict(list)
    for a,b in combinations_with_replacement(range(n),2):
        key=bytes(x+y+2*m for x,y in zip(profiles[a],profiles[b]))
        buckets[key].append(a*n+b)
    solutions=[]
    joins=0
    for key,pairs in buckets.items():
        partners=buckets.get(bytes(4*m-value for value in key),())
        joins += len(pairs)*len(partners)
        for first in pairs:
            a,b=divmod(first,n)
            for second in partners:
                c,d=divmod(second,n)
                if b<=c:
                    solutions.append([a,b,c,d])
    if len(solutions) != len({tuple(q) for q in solutions}):
        raise ValueError("duplicate solution tuple")
    return {"core_order":m,"normalized_sequences":n,"unfiltered_pairs":n*(n+1)//2,
            "full_nonzero_lags":m-1,"joined_pair_combinations":joins,
            "solutions":sorted(solutions)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    started=time.perf_counter()
    results=[]
    for m in (19,21):
        result=enumerate_independently(m)
        results.append(result)
        print(f"m={m}: independently enumerated {len(result['solutions'])} solutions",flush=True)
    # Both independent complete searches finish before the subject is imported.
    gc.collect()
    study=Path(__file__).resolve().parents[2]
    spec=importlib.util.spec_from_file_location("round2_subject",study/"round2/scripts/search.py")
    subject=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(subject)
    for result in results:
        m=result["core_order"]
        filtered=subject.run(m,"filtered-mitm")
        with_key=subject.run(m,"filtered-mitm-product-key")
        if result["solutions"] != filtered["solutions"] or result["solutions"] != with_key["solutions"]:
            raise ValueError(("moderate solution-set mismatch",m))
        if result["joined_pair_combinations"] != filtered["counts"]["joined_pair_combinations_before_sorted_order_test"] or result["joined_pair_combinations"] != with_key["counts"]["joined_pair_combinations_before_sorted_order_test"]:
            raise ValueError(("moderate join-count mismatch",m))
        result["exact_filtered_tuple_sets_match"]=True
    output={"status":"passed","method":"unfiltered full-lag byte-key MITM; PAF computed from negative-support cyclic overlaps; no subject imports until after enumeration","elapsed_seconds_not_a_comparative_benchmark":time.perf_counter()-started,"results":results}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2,sort_keys=True)+"\n")


if __name__ == "__main__":
    main()
