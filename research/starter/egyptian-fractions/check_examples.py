"""Original exact-arithmetic study certificates; not a Lean verifier."""
from fractions import Fraction
from collections import Counter
import json
from pathlib import Path
from math import isqrt
ROOT=Path(__file__).parent

def total(ds): return sum((Fraction(1,d) for d in ds),Fraction(0))
def cleanup(ds):
    a=sorted(ds); x=total(a); assert 0<x<1
    steps=[]
    while len(set(a))<len(a):
        d=next(d for d,c in sorted(Counter(a).items()) if c>1)
        p=d//2
        new=[p+1,p*(p+1)] if d%2==0 else [p+1,(p+1)*d]
        before=a.copy(); a.remove(d);a.remove(d);a=sorted(a+new)
        assert len(a)==len(ds) and total(a)==x and sum(a)>sum(before) and min(a)>=2
        steps.append({'repeated_denominator':d,'replacement':new,'denominator_sum_increase':sum(a)-sum(before)})
        if len(steps)>10000: raise RuntimeError('computation bound reached')
    return {'input':ds,'sum':str(x),'output':a,'steps':steps,'exact_checks_passed':True}

def expansions(x,k,start=2):
    if k==1:
        if x.numerator==1 and x.denominator>=start: yield [x.denominator]
        return
    lo=max(start,(x.denominator+x.numerator-1)//x.numerator)
    hi=(k*x.denominator)//x.numerator
    for d in range(lo,hi+1):
        r=x-Fraction(1,d)
        if r>0:
            for tail in expansions(r,k-1,d+1): yield [d]+tail

def padding(ds,m):
    a=sorted(ds); assert len(a)>=3 and len(set(a))==len(a) and total(a)==1 and m in a
    s=a[-1] if m!=a[-1] else a[-2]
    replacement=[s+1,s*(s+1)]
    if m==a[-1] and m in replacement:
        factor=next((d for d in range(2,isqrt(s)+1) if s%d==0),None)
        assert factor is not None, ('impossible prime exception',a,m)
        b=s//factor; replacement=[s+factor,b*(s+factor)]
    out=sorted([d for d in a if d!=s]+replacement)
    assert total(out)==1 and len(out)==len(a)+1 and len(set(out))==len(out) and m in out
    return out,replacement,s

cleanup_cases=[cleanup([d]*k) for d in range(3,13) for k in range(2,min(5,d-1)+1)]
padding_cases=[];counts={};exceptional=[]
for k in range(3,7):
    count=0
    for ds in expansions(Fraction(1),k):
        count+=1
        for m in ds:
            out,repl,s=padding(ds,m)
            padding_cases.append({'input':ds,'marker':m,'split_denominator':s,'replacement':repl,'output':out,'exact_checks_passed':True})
            if m==ds[-1] and m in [s+1,s*(s+1)]: exceptional.append({'input':ds,'marker':m,'output':out})
    counts[k]=count
special_input=[3,4,7,12,14,15,20,420]
special_out,special_repl,special_s=padding(special_input,420)
exceptional.append({'input':special_input,'marker':420,'output':special_out,'split_denominator':special_s,'replacement':special_repl,'exact_checks_passed':True})
record={'schema':'portable-math-study-examples-v1','verification':'Python Fraction exact arithmetic; not Lean; finite examples are not a universal proof','source_revision':'fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb','cleanup_cases':cleanup_cases,'enumeration_counts':counts,'padding_cases':padding_cases,'exceptional_composite_cases':exceptional}
(ROOT/'exact-examples.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'cleanup_cases':len(cleanup_cases),'enumeration_counts':counts,'padding_checks':len(padding_cases),'exceptional_cases':len(exceptional),'all_checks_passed':True}))
