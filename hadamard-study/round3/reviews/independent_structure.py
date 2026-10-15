#!/usr/bin/env python3
"""Independent coloring/sign representation and full unpruned structural check."""

import argparse
from collections import Counter
import json
from pathlib import Path
import time


def edges_by_lag(m):
    result=[]
    h=m//2
    for t in range(1,h+1):
        edges=[]
        loops=0
        for j in range(m):
            k=(j+t)%m
            if j==0 or k==0:
                continue
            reflected=(-j-t)%m
            if j==reflected:
                loops+=1
                continue
            if j>reflected:
                continue
            u=min(j,m-j)-1
            v=min(k,m-k)-1
            if u==v or min(u,v)<0:
                raise ValueError("unexpected quotient edge")
            edges.append((u,v))
        if loops!=1 or len(edges)!=h-1:
            raise ValueError(("quotient orbit count",m,t,loops,edges))
        result.append(edges)
    return result


def rgs(h):
    if h==0:
        yield ()
        return
    def walk(prefix,largest):
        if len(prefix)==h:
            yield tuple(prefix)
            return
        for color in range(min(3,largest+1)+1):
            prefix.append(color)
            yield from walk(prefix,max(largest,color))
            prefix.pop()
    yield from walk([], -1)


def forced_signs(colors,edges):
    return tuple(1 if sum(colors[u]==colors[v] for u,v in lag)%2 else -1 for lag in edges)


def sequence_masks(colors,signs):
    return tuple(sorted(sum((sign*(1-2*(color==row))==-1)<<j
                            for j,(color,sign) in enumerate(zip(colors,signs)))
                        for row in range(4)))


def check_structure(colors,signs,edges):
    return all(1+signs[t]+2*sum(signs[u]*signs[v] for u,v in lag if colors[u]==colors[v])==0
               for t,lag in enumerate(edges))


def decode_tuple(m,q):
    colors=[]
    signs=[]
    labels={}
    for j in range(m//2):
        column=[1-2*((a>>j)&1) for a in q]
        negatives=column.count(-1)
        if negatives not in (1,3):
            raise ValueError("baseline tuple violates product theorem")
        sign=1 if negatives==1 else -1
        row=column.index(-sign)
        if row not in labels:
            labels[row]=len(labels)
        colors.append(labels[row])
        signs.append(sign)
    return tuple(colors),tuple(signs)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    study=Path(__file__).resolve().parents[2]
    first=json.loads((study/"reviews/williamson-independent.json").read_text())
    moderate=json.loads((study/"round2/reviews/moderate-independent.json").read_text())
    expected={r["core_order"]:[tuple(q) for q in r["solving_sequence_index_multisets"]] for r in first["results"]}
    expected.update({r["core_order"]:[tuple(q) for q in r["solutions"]] for r in moderate["results"]})
    expected[23]=None
    started=time.perf_counter()
    results=[]
    for m,tuples in sorted(expected.items()):
        edges=edges_by_lag(m)
        for q in tuples or ():
            colors,signs=decode_tuple(m,q)
            if forced_signs(colors,edges)!=signs or sequence_masks(colors,signs)!=q:
                raise ValueError(("forced-sign or RGS encoding false negative",m,q,colors,signs))
        solutions=[]
        leaves=0
        row_feasible=0
        for colors in rgs(m//2):
            leaves+=1
            signs=forced_signs(colors,edges)
            sums=[sum(s for c,s in zip(colors,signs) if c==k) for k in range(4)]
            if sum(t*t for t in sums)==signs.count(-1):
                row_feasible+=1
            if check_structure(colors,signs,edges):
                solutions.append(sequence_masks(colors,signs))
        if len(solutions)!=len(set(solutions)) or (tuples is not None and sorted(solutions)!=tuples):
            raise ValueError(("complete structural baseline mismatch",m,len(solutions)))
        results.append({"core_order":m,"unpruned_RGS_colorings":leaves,
                        "forced_signs_row_feasible":row_feasible,
                        "solutions":[list(q) for q in sorted(solutions)],
                        "exact_preserved_baseline_tuple_set_equality":True if tuples is not None else None})
        print(f"m={m}: colorings={leaves}, solutions={len(solutions)}",flush=True)
    result={"status":"passed","method":"independent physical-edge quotient, parity-forced column signs, unpruned restricted-growth colorings; no study-module imports",
            "elapsed_seconds_not_comparative_benchmark":time.perf_counter()-started,"results":results}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")


if __name__ == "__main__":
    main()
