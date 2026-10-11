"""Independent read-only audit of positive-block example JSON, standard library only.

No author checker or repository code is imported. All arithmetic is exact.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

F = Fraction
ZERO = (F(0), F(0))
ONE = (F(1), F(0))

def parse(s):
    s = s.replace('*i', 'j')
    if not s.endswith('j'):
        return F(s), F(0)
    s = s[:-1]
    split = next((k for k in range(1, len(s)) if s[k] in '+-'), None)
    return (F(0), F(s)) if split is None else (F(s[:split]), F(s[split:]))

def add(z,w): return z[0]+w[0], z[1]+w[1]
def neg(z): return -z[0], -z[1]
def conj(z): return z[0], -z[1]
def times(z,w): return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]
def over(z,w):
    n=times(z,conj(w)); d=w[0]**2+w[1]**2
    return n[0]/d,n[1]/d

def mat(x): return [[parse(v) for v in row] for row in x]
def star(a): return [[conj(a[j][i]) for j in range(len(a))] for i in range(len(a[0]))]
def prod(a,b):
    assert len(a[0])==len(b)
    out=[]
    for row in a:
        rr=[]
        for j in range(len(b[0])):
            z=ZERO
            for k in range(len(b)): z=add(z,times(row[k],b[k][j]))
            rr.append(z)
        out.append(rr)
    return out

def scale(a,t): return [[times(z,(F(t),F(0))) for z in r] for r in a]
def diff(a,b): return [[add(z,neg(w)) for z,w in zip(r,s)] for r,s in zip(a,b)]
def trace(a):
    z=ZERO
    for i in range(len(a)): z=add(z,a[i][i])
    return z

def norm2(a): return sum(z[0]**2+z[1]**2 for r in a for z in r)
def nonzero(a): return any(z!=ZERO for r in a for z in r)
def rank(a):
    # Exact forward elimination with independent row selection, no normalization.
    a=[r[:] for r in a]; k=0
    for j in range(len(a[0])):
        selected=next((i for i in range(k,len(a)) if a[i][j]!=ZERO),None)
        if selected is None: continue
        a[k],a[selected]=a[selected],a[k]
        for i in range(k+1,len(a)):
            ratio=over(a[i][j],a[k][j])
            a[i]=[add(v,neg(times(ratio,w))) for v,w in zip(a[i],a[k])]
        k+=1
        if k==len(a): break
    return k

def diag(n,p,t):
    return [[(F(t if i<p else -1),F(0)) if i==j else ZERO for j in range(n)] for i in range(n)]

def audit(case):
    a,b,c,d=(mat(case[k]) for k in ['A','B','C','Delta'])
    p,q=len(a),len(c)
    assert len(b)==p and all(len(r)==q for r in b)
    assert d == [ra+rb for ra,rb in zip(a,b)]+[rb+rc for rb,rc in zip(star(b),c)]
    assert star(d)==d
    aa,cc,bb=norm2(a),norm2(c),norm2(b)
    assert [aa,cc,bb]==[F(case['squared_norms'][k]) for k in ['A','C','B']]
    assert F(case['sum_gap'])==aa+cc-2*bb
    assert F(case['product_squared_gap'])==aa*cc-bb*bb
    assert {k:rank(v) for k,v in zip(['A','B','C','Delta'],[a,b,c,d])}==case['ranks']
    if 'X' in case:
        x,y=mat(case['X']),mat(case['Y']); z=[r+s for r,s in zip(x,y)]
        pp,qq=prod(x,star(x)),prod(y,star(y))
        assert d==prod(star(z),z)
        assert a==prod(star(x),x) and b==prod(star(x),y) and c==prod(star(y),y)
        assert pp==mat(case['P']) and qq==mat(case['Q'])
        assert (aa,cc,(bb,F(0)))==(norm2(pp),norm2(qq),trace(prod(pp,qq)))
        assert aa+cc-2*bb==norm2(diff(pp,qq))
        for s in [F(2,3),F(1),F(5,2)]:
            assert s*s*aa+cc/(s*s)-2*bb==norm2(diff(scale(pp,s),scale(qq,1/s)))
        assert bb*bb<=aa*cc and 2*bb<=aa+cc
        eqsum=(2*bb==aa+cc); eqprod=(bb*bb==aa*cc)
        assert eqsum==case['sum_equality'] and eqprod==case['product_equality']
        assert eqsum==(pp==qq)
        assert eqsum==(not nonzero(prod(prod(d,diag(p+q,p,F(1))),d)))
        assert rank(a+star(b))==rank(a) and rank(c+b)==rank(c)
        assert rank(b)<=min(rank(a),rank(c))
        if aa and cc:
            t=trace(qq)[0]/trace(pp)[0]
            assert eqprod==(qq==scale(pp,t))
            intrinsic=prod(prod(d,diag(p+q,p,t)),d)
            assert eqprod==(not nonzero(intrinsic))
            if eqprod:
                assert F(case['nonzero_equality_t'])==t and t*t*aa==cc
                assert prod(b,star(b))==scale(prod(a,a),t)
                assert prod(star(b),b)==scale(prod(c,c),1/t)
                assert prod(b,c)==scale(prod(a,b),t)
                assert len(set(case['ranks'].values()))==1
        else:
            assert bb==0 and eqprod and eqsum==(aa==cc==0)
    else:
        v=[[parse(z)] for z in case['negative_witness']]
        value=prod(prod(star(v),d),v)[0][0]
        assert value==parse(case['quadratic_form']) and value[0]<0 and value[1]==0
        assert case['sum_inequality_holds']==(2*bb<=aa+cc)
        assert case['product_inequality_holds']==(bb*bb<=aa*cc)
        if 'negative_semidefinite_certificate' in case:
            w=mat(case['negative_semidefinite_certificate']['W'])
            assert scale(d,-1)==prod(star(w),w)
    return case['id']

path=Path(sys.argv[1])
data=json.loads(path.read_text())
named=[audit(c) for c in data['named_examples']]
sweep=[audit(c) for c in data['seeded_sweep']['cases']]
print(json.dumps({'status':'passed','named_count':len(named),'named_ids':named,'seeded_count':len(sweep),'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic':'independent Fraction-pair parser and matrix operations; standard library only','claims':'Finite examples, weighted gaps, intrinsic sum and product equality iff tests, kernels/ranks, and signed quadratic-form certificates; not a universal proof or formal verification.'},indent=2))
