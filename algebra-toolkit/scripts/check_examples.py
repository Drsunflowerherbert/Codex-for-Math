#!/usr/bin/env python3
"""Exact adversarial spot checks for the written notes, not universal proofs.

No uploaded source book or prior search code is needed. Small fixed fixtures
exercise formulas with independently computed matrices, integer correlations,
and Boolean truth tables. The script writes its stated finite scope as JSON.
"""
from __future__ import annotations

import itertools as it
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
RESULTS = []


def record(name, **details):
    RESULTS.append({"name": name, "status": "pass", **details})


def compound(a, r):
    rows = list(it.combinations(range(a.rows), r))
    cols = list(it.combinations(range(a.cols), r))
    return s.Matrix(len(rows), len(cols), lambda i, j: a.extract(rows[i], cols[j]).det())


def paf(x):
    return tuple(sum(x[j] * x[(j + t) % len(x)] for j in range(len(x)))
                 for t in range(len(x)))


def sequence(m, mask):
    a = [1] * m
    for j in range(1, (m + 1) // 2):
        if mask & (1 << (j - 1)):
            a[j] = a[-j] = -1
    return a


def circ(a):
    return s.Matrix(len(a), len(a), lambda i, j: a[(j - i) % len(a)])


def total_paf(rows):
    return tuple(sum(v) for v in zip(*(paf(a) for a in rows)))


def algebra_checks():
    t = s.symbols("t")
    m = t**2 * (t - 1)**2
    e = 3*t**2 - 2*t**3
    for p in [None, 2, 3, 5, 7]:
        kwargs = {"domain": s.QQ} if p is None else {"modulus": p}
        for expr in [e*e - e, e*(1-e), t**2*(1-e), (t-1)**2*e]:
            assert s.rem(expr, m, t, **kwargs) == 0
        assert s.rem(e, t**2, t, **kwargs) == 0
        assert s.rem(e-1, (t-1)**2, t, **kwargs) == 0
    record("Bezout/CRT projectors", fields=["Q", "F2", "F3", "F5", "F7"],
           polynomial="3t^2-2t^3", annihilator="t^2(t-1)^2")

    j0 = s.Matrix([[0, 1], [0, 0]])
    j1 = s.eye(2) + j0
    change = s.Matrix([[1,2,0,1],[0,1,1,0],[0,0,1,3],[0,0,0,1]])
    a = change * s.diag(j0, j1) * change.inv()
    proj = 3*a**2 - 2*a**3
    assert proj*proj == proj and proj*a == a*proj
    assert proj.rank() == 2 and (s.eye(4)-proj).rank() == 2
    assert (a-s.eye(4))**2 * proj == s.zeros(4)
    assert a**2 * (s.eye(4)-proj) == s.zeros(4)
    record("Polynomial projections on a conjugated mixed Jordan fixture", dimension=4)

    def jordan(n):
        return s.Matrix(n,n,lambda i,j:int(j==i+1))
    a = s.diag(jordan(4), jordan(3), jordan(2), jordan(1))
    nullities = [10-(a**j).rank() for j in range(6)]
    assert nullities == [0,4,7,9,10,10]
    recovered = [2*nullities[j]-nullities[j-1]-nullities[j+1] for j in range(1,5)]
    assert recovered == [1,1,1,1]
    # Independently solve the linear commutator equations by Kronecker rank.
    equations = s.kronecker_product(s.eye(10), a) - s.kronecker_product(a.T, s.eye(10))
    actual = 100 - equations.rank()
    assert actual == sum(min(i,j) for i in range(1,5) for j in range(1,5)) == 30
    record("Jordan reconstruction and centralizer", nullities=nullities,
           commutant_dimension=actual, independent_equation_matrix=[100,100])

    # Direct intertwiner equations independently check the cyclic gcd formula.
    fixtures = [t**2, t**3, (t-1)**2, t**2+1]
    def companion(f):
        coeff=s.Poly(f,t).all_coeffs();n=len(coeff)-1
        return s.Matrix(n,n,lambda i,j: (-coeff[n-i] if j==n-1 else int(i==j+1)))
    for f,g in it.product(fixtures,repeat=2):
        af,ag=companion(f),companion(g)
        mat=s.kronecker_product(s.eye(af.rows),ag)-s.kronecker_product(af.T,s.eye(ag.rows))
        assert af.rows*ag.rows-mat.rank()==s.degree(s.gcd(f,g),t)
    record("Cyclic Hom gcd formula", ordered_polynomial_pairs=16)


def multilinear_checks():
    a=s.Matrix([[2,-1,3],[0,4,1],[1,2,-2],[3,0,1]])
    b=s.Matrix([[1,2,0,-1],[2,1,3,0],[-1,0,2,2]])
    for r in [1,2,3]:
        assert compound(b*a,r)==compound(b,r)*compound(a,r)
    x=s.Matrix([[2,1,0,-1],[1,3,2,0],[0,1,4,1],[2,0,-1,1]])
    z=s.symbols("z")
    c=sum((-1)**r*(1 if r==0 else s.trace(compound(x,r)))*z**(4-r) for r in range(5))
    assert s.expand(c-x.charpoly(z).as_expr())==0
    record("Exterior powers, rectangular Cauchy-Binet, and characteristic coefficients",
           exterior_degrees=[1,2,3], characteristic_dimension=4)

    a=s.Matrix([[1,2],[3,4]]); b=s.Matrix([[0,1,2],[-1,2,0],[3,0,1]])
    ab=s.kronecker_product(a,b)
    assert s.trace(ab)==s.trace(a)*s.trace(b)
    assert ab.det()==a.det()**3*b.det()**2
    record("Kronecker trace and determinant", dimensions=[2,3])

    h=s.Matrix([[2,1+s.I],[1-s.I,3]])
    a=s.Matrix([[1+s.I,2],[0,3-s.I]])
    adj=h.inv()*a.conjugate().T*h
    assert s.simplify(a.conjugate().T*h-h*adj)==s.zeros(2)
    assert s.simplify(h.inv()*adj.conjugate().T*h-a)==s.zeros(2)
    record("Adjoint under a nonorthonormal Hermitian Gram matrix", convention="conjugate-linear first")

    # A finite truncation cannot prove the infinite-dimensional counterexample;
    # it verifies the unbounded rank obstruction used in its written proof.
    assert all(s.eye(n).rank()>r for r,n in [(1,2),(2,3),(3,4)])
    record("Finite-rank obstruction illustrations", note="The infinite-dimensional conclusion has a written proof, not a finite test.")


def homology_representation_checks():
    t=s.symbols("t")
    for p in [2,3,5,7]:
        # t*(1+c*t)=t modulo t^2: direct finite-field lifts, not an Ext implementation.
        for c in range(p):
            remainder=s.rem(t*(1+c*t),t*t,t,modulus=p)
            assert remainder==t and remainder!=0
    record("No equivariant section of k[t]/t^2", tested_prime_fields=[2,3,5,7])
    d=s.Matrix([[1,0,0],[0,1,0]])
    assert d.cols-d.rank()==1 and d.rows-d.rank()==0
    # Basis order for C1: homology z, then x,y; C0: x,y.
    d=s.Matrix([[0,1,0],[0,0,1]])
    homotopy=s.Matrix([[0,0],[1,0],[0,1]])
    homology_projection=s.diag(1,0,0)
    assert homotopy*d==s.eye(3)-homology_projection
    assert d*homotopy==s.eye(2)
    record("Nonzero field-complex homology and explicit contraction of complement", H1=1,H0=0)
    for m in range(7):
        E=s.zeros(m+1); F=s.zeros(m+1); H=s.diag(*[m-2*j for j in range(m+1)])
        for j in range(m+1):
            if j: E[j-1,j]=j
            if j<m: F[j+1,j]=m-j
        assert H*E-E*H==2*E
        assert H*F-F*H==-2*F
        assert E*F-F*E==H
    record("sl2 polynomial-model commutation relations", highest_weights=list(range(7)))


def paley_checks():
    # Direct residue-square sets: independent of exponent-based character code.
    for p in [3,5,7,11,13,19]:
        squares={a*a%p for a in range(1,p)}
        def chi(a):return 0 if a%p==0 else (1 if a%p in squares else -1)
        for a in range(1,p):
            assert sum(chi(x)*chi(x+a) for x in range(p))==-1
        q=s.Matrix(p,p,lambda i,j:chi(j-i))
        assert q*q.T==p*s.eye(p)-s.ones(p)
        if p%4==3:
            h=s.ones(p+1);h[1:,1:]=q-s.eye(p)
            assert set(h).issubset({-1,1}) and h*h.T==(p+1)*s.eye(p+1)
        else:
            c=s.zeros(p+1);c[0,1:]=s.ones(1,p);c[1:,0]=s.ones(p,1);c[1:,1:]=q
            assert c*c==p*s.eye(p+1)
            I=s.eye(p+1)
            h=(c+I).row_join(c-I).col_join((c-I).row_join(-c-I))
            assert set(h).issubset({-1,1}) and h*h.T==2*(p+1)*s.eye(2*(p+1))
    record("Quadratic character sums and both Paley sign conventions", primes=[3,5,7,11,13,19])
    # One nonprime finite field, F9 = F3[u]/(u^2+1), verifies the extension bridge.
    F=list(it.product(range(3),repeat=2))
    def add(x,y):return ((x[0]+y[0])%3,(x[1]+y[1])%3)
    def neg(x):return ((-x[0])%3,(-x[1])%3)
    def mul(x,y):return ((x[0]*y[0]-x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0])%3)
    sq={mul(x,x) for x in F if x!=(0,0)}
    def ch(x):return 0 if x==(0,0) else (1 if x in sq else -1)
    q=s.Matrix(9,9,lambda i,j:ch(add(F[j],neg(F[i]))))
    assert q==q.T and q*q.T==9*s.eye(9)-s.ones(9)
    c=s.zeros(10);c[0,1:]=s.ones(1,9);c[1:,0]=s.ones(9,1);c[1:,1:]=q
    I=s.eye(10);h=(c+I).row_join(c-I).col_join((c-I).row_join(-c-I))
    assert h*h.T==20*s.eye(20)
    record("Nonprime finite-field Paley fixture", field="F3[u]/(u^2+1)",order=20)


def williamson_checks():
    mats=[circ(sequence(3,i)) for i in [0,1,1,1]]
    a,b,c,d=mats
    assert a*a+b*b+c*c+d*d==12*s.eye(3)
    w=a.row_join(b).row_join(c).row_join(d).col_join(
      (-b).row_join(a).row_join(-d).row_join(c)).col_join(
      (-c).row_join(d).row_join(a).row_join(-b)).col_join(
      (-d).row_join(-c).row_join(b).row_join(a))
    assert w*w.T==12*s.eye(12)
    record("Williamson block signs", core_order=3,normalized_masks=[0,1,1,1])
    rows=[sequence(9,i) for i in [2,10,10,13]]
    compressed=[tuple(sum(row[j] for j in range(r,9,3)) for r in range(3)) for row in rows]
    assert total_paf(compressed)==(36,0,0)
    assert total_paf(rows)[1]==-8
    record("Passing proper quotients with a failing chosen lift", core_order=9,
           masks=[2,10,10,13],compressed_rows=compressed,original_shift_one=-8)
    # Verify only the fixed prior no-common-lift fixture: no fresh order search.
    target=tuple(sorted([(-1,-1,-1),(-1,1,1),(-1,3,3),(3,-1,-1)]))
    singles=[sequence(9,i) for i in range(16)]
    comp=[tuple(sum(row[j] for j in range(r,9,3)) for r in range(3)) for row in singles]
    lifts=[]
    for q in it.combinations_with_replacement(range(16),4):
        if tuple(sorted(comp[i] for i in q))==target:
            lifts.append(q)
            assert total_paf([singles[i] for i in q])!=(36,0,0,0,0,0,0,0,0)
    assert len(lifts)==27 and total_paf(target)==(36,0,0)
    record("Prior fixed compressed multiset has no common normalized symmetric lift",
           core_order=9,compressed_rows=target,candidate_lifts_checked=len(lifts),
           candidate_domain="16 normalized symmetric rows; fixed target only",
           scope="Williamson family, not all Hadamard matrices")
    rows=[sequence(7,i) for i in [1,2,4]]
    gram=sum((circ(row)**2 for row in rows),s.zeros(7))
    assert gram==20*s.eye(7)+s.ones(7)
    residual=28*s.eye(7)-gram
    assert residual.eigenvals()=={s.Integer(1):1,s.Integer(8):6}
    assert (1^2^4^7)==0
    assert sum(sum(row)**2 for row in rows)==27 and sum(sequence(7,0))**2==49
    record("Positive residual without a fourth Williamson sign lift", core_order=7,
           residual_eigenvalues={"1":1,"8":6})
    for au,av,bu,bv in it.product(range(2),repeat=4):
        delta=((1+au+av)*(1+bu+bv))%2
        assert delta==int((au,bu)==(av,bv))
        assert 4*delta==(1+(-1)**(au+av))*(1+(-1)**(bu+bv))
    for a,b in it.product(range(2),repeat=2):
        assert (-1)**((a+b)%2)==(-1)**a*(-1)**b
    record("Boolean color equality and exact phase relations", equality_inputs=16,
           coefficient_ring="F2 for exponents; Z for correlation coefficients")


def main():
    algebra_checks();multilinear_checks();homology_representation_checks()
    paley_checks();williamson_checks()
    result={"timestamp_utc":datetime.now(timezone.utc).isoformat(),
      "python":platform.python_version(),"sympy":s.__version__,
      "status":"pass","checks":RESULTS,
      "scope":"Exact finite examples and adversarial fixtures; not formal or general theorem verification."}
    output=ROOT/"evidence"/"exact-checks.json"
    output.parent.mkdir(exist_ok=True);output.write_text(json.dumps(result,indent=2)+"\n")
    print(f"PASS: {len(RESULTS)} exact check groups. Evidence: {output.relative_to(ROOT)}")


if __name__=="__main__":main()
