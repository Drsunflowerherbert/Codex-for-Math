#!/usr/bin/env python3
"""Check concrete identities in E01--E16; this is NOT analytic verification.

Run from any directory with Python 3, SymPy and mpmath installed::

    python integral-examples/checks/check_examples.py

The script checks exact finite algebra/antiderivatives and selected high-precision
quadratures. It does not prove measurability, integrability, convergence theorem
hypotheses, Hausdorff normalization, area/coarea applicability, nonmeasurability,
or the infinite-stage Cantor claims. Those require the written proofs and
independent mathematical review. Finite samples never establish an infinite limit or a divergence claim.
The JSON report records this scope, every performed check, package versions, and
hashes of the example sources present during this actual run. No Lean is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
mp.mp.dps = 70
TOLERANCE = mp.mpf("1e-50")
RESULTS: dict[str, dict] = {}


def example(identifier: str, limitations: str) -> None:
    RESULTS[identifier] = {"checks": [], "analytic_limitations": limitations}


def exact(identifier: str, name: str, actual, expected=0) -> None:
    difference = sp.simplify(sp.sympify(actual) - sp.sympify(expected))
    passed = difference == 0
    RESULTS[identifier]["checks"].append(
        {"name": name, "method": "exact SymPy simplification", "passed": passed,
         "actual": str(actual), "expected": str(expected), "difference": str(difference)}
    )


def finite(identifier: str, name: str, passed: bool, detail: str) -> None:
    RESULTS[identifier]["checks"].append(
        {"name": name, "method": "exact finite rational/integer arithmetic",
         "passed": bool(passed), "detail": detail}
    )


def numeric(identifier: str, name: str, actual, expected) -> None:
    actual, expected = mp.mpf(actual), mp.mpf(expected)
    error = abs(actual - expected)
    passed = error <= TOLERANCE * max(1, abs(expected))
    RESULTS[identifier]["checks"].append(
        {"name": name, "method": "mpmath quadrature, 70 decimal digits",
         "passed": bool(passed), "actual": mp.nstr(actual, 65),
         "expected": mp.nstr(expected, 65), "absolute_error": mp.nstr(error, 8),
         "relative_or_absolute_tolerance": str(TOLERANCE)}
    )


def check_all() -> None:
    x, y, u, v, r, t = sp.symbols("x y u v r t", real=True)
    p, a, b, radius, delta, eps = sp.symbols("p a b R delta epsilon", positive=True)
    n, k = sp.symbols("n k", integer=True, positive=True)

    example("E01", "Algebra and quadrature do not establish Fubini/Tonelli or the series-exchange hypotheses.")
    exact("E01", "Useful antiderivative", sp.diff(sp.exp(y*y)/2, y), y*sp.exp(y*y))
    exact("E01", "Triangle integral", sp.integrate(y*sp.exp(y*y), (y, 0, 1)), (sp.E-1)/2)
    exact("E01", "Power-series coefficient reindexing", 1/(2*(k+1)*sp.factorial(k)), 1/(2*sp.factorial(k+1)))
    numeric("E01", "Independent nested quadrature in original order",
            mp.quad(lambda xx: mp.quad(lambda yy: mp.exp(yy*yy), [xx, 1]), [0, 1]),
            (mp.e-1)/2)

    example("E02", "Finite-stage arithmetic does not prove the infinite intersection's measure, empty interior, boundary claim, or Riemann failure.")
    length = 2**(-n-1) + 2**(-2*n-1)
    exact("E02", "Component-length recurrence", (length.subs(n, n-1)-4**(-n))/2, length)
    exact("E02", "Removed length through stage n", sp.summation(2**(k-1)*4**(-k), (k, 1, n)), (1-sp.Rational(1,2)**n)/2)
    exact("E02", "Remaining length through stage n", 2**n*length, sp.Rational(1,2)+2**(-n-1))
    exact("E02", "Weighted region integral from computed base measure", sp.Rational(1,2)*sp.integrate(2*y, (y, 0, 1)), sp.Rational(1,2))

    example("E03", "No computational test can construct/test the nonmeasurable Vitali set or prove the completion and exceptional-section assertions. This example is proof-only.")

    example("E04", "Primitive identities and finite lower-bound arithmetic do not by themselves prove sign-part divergence or permit signed Fubini.")
    f = (x*x-y*y)/(x*x+y*y)**2
    exact("E04", "Primitive in y", sp.diff(y/(x*x+y*y), y), f)
    exact("E04", "Primitive in x", sp.diff(-x/(x*x+y*y), x), f)
    exact("E04", "Positive iterated value", sp.integrate(1/(1+x*x), (x, 0, 1)), sp.pi/4)
    exact("E04", "Negative iterated value", sp.integrate(-1/(1+y*y), (y, 0, 1)), -sp.pi/4)
    exact("E04", "Dyadic rectangle lower mass", sp.Rational(12,25)*2**(2*n)*2**(-2*n-3), sp.Rational(3,50))
    exact("E04", "Antisymmetry", f + f.xreplace({x:y, y:x}), 0)
    xx, yy = mp.mpf("0.375"), mp.mpf("0.625")
    numeric("E04", "Fixed-x section quadrature", mp.quad(lambda z:(xx*xx-z*z)/(xx*xx+z*z)**2,[0,1]), 1/(1+xx*xx))
    numeric("E04", "Fixed-y section quadrature", mp.quad(lambda z:(z*z-yy*yy)/(z*z+yy*yy)**2,[0,1]), -1/(1+yy*yy))

    example("E05", "Finite rectangles illustrate the stated identities; no finite test establishes an infinite series result. Absolute divergence and the iterated limits require the written argument.")
    def entry(nn, mm):
        return int(nn == mm)-int(mm == nn+1)
    rectangles_ok = all(sum(entry(nn,mm) for nn in range(1,nn_max+1) for mm in range(1,mm_max+1)) == min(nn_max,mm_max)-min(nn_max,mm_max-1)
                        for nn_max in range(1,25) for mm_max in range(1,25))
    finite("E05", "Rectangular partial-sum formula", rectangles_ok, "All N,M in {1,...,24}; S_NM=min(N,M)-min(N,M-1).")
    finite("E05", "Complete finite-support rows and columns",
           all(sum(entry(nn,mm) for mm in range(1,nn+2)) == 0 for nn in range(1,101))
           and all(sum(entry(nn,mm) for nn in range(1,mm+1)) == int(mm==1) for mm in range(1,101)),
           "Rows/columns 1,...,100, summing their entire known finite supports.")
    finite("E05", "Square versus rectangular exhaustion samples",
           all(sum(entry(nn,mm) for nn in range(1,N+1) for mm in range(1,N+1)) == 1
               and sum(entry(nn,mm) for nn in range(1,N+1) for mm in range(1,N+2)) == 0
               for N in (1,2,8,20)), "S_NN=1 and S_N,N+1=0 at N=1,2,8,20.")

    example("E06", "Sample positive parameters do not prove the improper integral for all parameters or justify Tonelli/DCT. The local derivative majorant is checked in the written proof.")
    q = (sp.exp(-a*x)-sp.exp(-b*x))/x
    exact("E06", "Parameter derivative of integrand", sp.diff(q, b), sp.exp(-b*x))
    exact("E06", "Derivative of logarithmic answer", sp.diff(sp.log(b/a), b), 1/b)
    exact("E06", "Exponential inner integral", sp.integrate(sp.exp(-p*x),(x,0,sp.oo)), 1/p)
    for aa, bb in ((mp.mpf("0.7"),mp.mpf("2.3")), (mp.mpf("2.3"),mp.mpf("0.7")), (mp.mpf("1.25"),mp.mpf("1.25"))):
        lo, hi = min(aa,bb), max(aa,bb)
        sign = 1 if bb >= aa else -1
        def stable_frullani(z):
            return bb-aa if z == 0 else sign*mp.exp(-lo*z)*(-mp.expm1(-(hi-lo)*z))/z
        numeric("E06", f"Improper quadrature a={aa}, b={bb}", mp.quad(stable_frullani,[0,1,mp.inf]), mp.log(bb/aa))

    example("E07", "The Jacobian and integrals are checked; injectivity, Hausdorff normalization, and the area-formula hypotheses need the written proof.")
    exact("E07", "Squared speed", sp.Matrix([1,2*t]).dot(sp.Matrix([1,2*t])), 1+4*t*t)
    weighted = (5*sp.sqrt(5)-1)/12
    length_answer = sp.sqrt(5)/2+sp.asinh(2)/4
    exact("E07", "Weighted arc integral", sp.integrate(t*sp.sqrt(1+4*t*t),(t,0,1)), weighted)
    exact("E07", "Arc length", sp.integrate(sp.sqrt(1+4*t*t),(t,0,1)), length_answer)
    numeric("E07", "Weighted-arc quadrature", mp.quad(lambda z:z*mp.sqrt(1+4*z*z),[0,1]), (5*mp.sqrt(5)-1)/12)
    numeric("E07", "Arc-length quadrature", mp.quad(lambda z:mp.sqrt(1+4*z*z),[0,1]), mp.sqrt(5)/2+mp.asinh(2)/4)

    example("E08", "Trigonometric identities do not establish every fibre count or remove the endpoint exception; orientation and scalar integration are distinguished in the proof.")
    velocity = sp.Matrix([-sp.sin(t),sp.cos(t)])
    exact("E08", "Squared speed and circulation density", velocity.dot(velocity), 1)
    exact("E08", "Once-counted scalar circle integral", sp.integrate(sp.cos(t)**2,(t,0,2*sp.pi)), sp.pi)
    exact("E08", "Twice-traversed scalar integral", sp.integrate(sp.cos(t)**2,(t,0,4*sp.pi)), 2*sp.pi)
    exact("E08", "Double-traversal circulation", sp.integrate(1,(t,0,4*sp.pi)), 4*sp.pi)
    numeric("E08", "Twice-traversed scalar quadrature", mp.quad(lambda z:mp.cos(z)**2,[0,mp.pi,2*mp.pi,3*mp.pi,4*mp.pi]), 2*mp.pi)

    example("E09", "The Gram determinant and radial integrals are checked. The graph area formula and planar polar substitution require the written regularity/measure arguments.")
    derivative = sp.Matrix([[1,0],[0,1],[2*x,2*y]])
    exact("E09", "Graph Gram determinant", (derivative.T*derivative).det(), 1+4*x*x+4*y*y)
    exact("E09", "Graph height moment", 2*sp.pi*sp.integrate(r**3*sp.sqrt(1+4*r*r),(r,0,1)), sp.pi*(25*sp.sqrt(5)+1)/60)
    exact("E09", "Graph area", 2*sp.pi*sp.integrate(r*sp.sqrt(1+4*r*r),(r,0,1)), sp.pi*(5*sp.sqrt(5)-1)/6)
    numeric("E09", "Height-moment quadrature", 2*mp.pi*mp.quad(lambda z:z**3*mp.sqrt(1+4*z*z),[0,1]), mp.pi*(25*mp.sqrt(5)+1)/60)
    numeric("E09", "Graph-area quadrature", 2*mp.pi*mp.quad(lambda z:z*mp.sqrt(1+4*z*z),[0,1]), mp.pi*(5*mp.sqrt(5)-1)/6)

    example("E10", "Angular identities do not prove chart injectivity or the missing meridian's Hausdorff nullity. The parameter constraints R>0, 0<=cap height<=2R are assumptions.")
    exact("E10", "Sphere angular moment", sp.integrate(sp.cos(t)**2*sp.sin(t),(t,0,sp.pi)), sp.Rational(2,3))
    exact("E10", "Sphere area", 2*sp.pi*radius**2*sp.integrate(sp.sin(t),(t,0,sp.pi)), 4*sp.pi*radius**2)
    exact("E10", "Sphere second coordinate moment", 2*sp.pi*radius**4*sp.integrate(sp.cos(t)**2*sp.sin(t),(t,0,sp.pi)), 4*sp.pi*radius**4/3)
    exact("E10", "Cap-area algebra", 2*sp.pi*radius**2*(1-(1-a/radius)), 2*sp.pi*radius*a)
    rr = mp.mpf("1.7")
    numeric("E10", "Sphere moment quadrature R=1.7", 2*mp.pi*rr**4*mp.quad(lambda z:mp.cos(z)**2*mp.sin(z),[0,mp.pi]), 4*mp.pi*rr**4/3)

    example("E11", "Exact Jacobian and polynomial integrals do not prove the complete fibre classification or the weighted area theorem.")
    derivative = sp.Matrix([[2*u,0],[0,1]])
    exact("E11", "Squared area Jacobian", (derivative.T*derivative).det(), 4*u*u)
    exact("E11", "Unsigned area factor integral", 2*sp.integrate(2*u,(u,0,1)), 2)
    exact("E11", "Weighted two-sheet integral", 2*sp.integrate(sp.integrate((u*u+v)*2*u,(v,0,1)),(u,0,1)), 2)
    exact("E11", "Once-counted image integral", sp.integrate(sp.integrate(x+y,(y,0,1)),(x,0,1)), 1)
    exact("E11", "Signed determinant cancellation", sp.integrate(2*u,(u,-1,1)), 0)
    numeric("E11", "Two-sheet weighted quadrature", mp.quad(lambda z:2*abs(z)*(z*z+mp.mpf("0.5")),[-1,0,1]), 2)

    example("E12", "These check explicit radial identities only. The all-Borel-weight pushforward formula, the critical-level treatment, and coarea applicability are proved analytically.")
    exact("E12", "Squared coarea Jacobian", sp.Matrix([2*x,2*y]).dot(sp.Matrix([2*x,2*y])), 4*(x*x+y*y))
    exact("E12", "Gradient integral on disk", 2*sp.pi*sp.integrate(2*r*r,(r,0,1)), 4*sp.pi/3)
    exact("E12", "Circle length divided by regular gradient", 2*sp.pi*sp.sqrt(p)/(2*sp.sqrt(p)), sp.pi)
    for exponent in (sp.Rational(-1,2),sp.Rational(0),sp.Rational(1),sp.Rational(3,2)):
        exact("E12", f"Radial power a={exponent}", 2*sp.pi*sp.integrate(r**(2*exponent+1),(r,0,1)), sp.pi/(exponent+1))
    exact("E12", "Borderline truncated power a=-1", sp.integrate(1/t,(t,eps,1)), -sp.log(eps))
    exact("E12", "Annulus squared-radius interval [a,b]", sp.pi*(sp.sqrt(b)**2-sp.sqrt(a)**2), sp.pi*(b-a))
    numeric("E12", "Gradient radial quadrature", 2*mp.pi*mp.quad(lambda z:2*z*z,[0,1]), 4*mp.pi/3)
    numeric("E12", "Extra smooth pushforward check phi(t)=exp(-t)", 2*mp.pi*mp.quad(lambda z:mp.exp(-z*z)*z,[0,1]), mp.pi*(1-mp.exp(-1)))

    example("E13", "Only exact finite Cantor stages are checked. No finite computation proves nullity, uniform convergence, the limit derivative, non-absolute-continuity, or the infinite fibre statement.")
    intervals = [(sp.Rational(0),sp.Rational(1),sp.Rational(0),sp.Rational(1))]
    for stage in range(1,9):
        next_intervals, new_plateaux = [], []
        for left,right,low,high in intervals:
            third, mid = (right-left)/3, (low+high)/2
            next_intervals += [(left,left+third,low,mid),(right-third,right,mid,high)]
            new_plateaux.append(mid)
        intervals = next_intervals
        source_mass = sum(right-left for left,right,low,high in intervals)
        derivative_mass = sum((high-low)/(right-left)*(right-left) for left,right,low,high in intervals)
        expected_plateaux = {sp.Rational(2*j+1,2**stage) for j in range(2**(stage-1))}
        finite("E13", f"Cantor stage {stage}",
               len(intervals)==2**stage and source_mass==sp.Rational(2,3)**stage
               and derivative_mass==1 and set(new_plateaux)==expected_plateaux
               and all((high-low)/(right-left)==sp.Rational(3,2)**stage for left,right,low,high in intervals),
               f"{len(intervals)} source intervals; source measure {source_mass}; total derivative mass {derivative_mass}; new plateaux are the expected odd dyadics.")

    example("E14", "Finite interval arithmetic does not prove pointwise/in-measure convergence, lack of domination, uniform integrability, tightness failure, or the positive sufficient criteria.")
    exact("E14", "Shrinking-interval mass", n*(1/n), 1)
    exact("E14", "Escaping unit-interval mass", (n+1)-n, 1)
    exact("E14", "Diluting-interval mass", (1/n)*n, 1)
    finite("E14", "Diluting tail interval samples",
           all(sp.Rational(max(N-R,0),N)==max(1-sp.Rational(R,N),0) for N in (1,2,10,100) for R in (1,3,20)),
           "For n=1,2,10,100 and R=1,3,20, overlap length/n=max(1-R/n,0).")

    example("E15", "Derivative/primitive algebra and numerical samples do not supply domination or justify differentiation under the integral. The failure of domination is proved using shrinking intervals.")
    f_parameter = p*p/(x*x+p*p)
    exact("E15", "Parameter derivative", sp.diff(f_parameter,p), 2*p*x*x/(x*x+p*p)**2)
    exact("E15", "Primitive of parameter function", sp.diff(p*sp.atan(x/p),x), f_parameter)
    exact("E15", "Primitive of difference quotient", sp.diff(sp.atan(x/p),x), p/(x*x+p*p))
    exact("E15", "Right derivative of integrated function", sp.limit(sp.atan(1/p),p,0,dir="+"), sp.pi/2)
    exact("E15", "Shrinking-interval quotient mass", sp.integrate(1/(1+u*u),(u,0,1)), sp.pi/4)
    exact("E15", "Derivative-layer mass", sp.integrate(2*u*u/(1+u*u)**2,(u,1,2)), sp.atan(2)-sp.pi/4+sp.Rational(1,10))
    for pp in (mp.mpf("0.1"),mp.mpf("0.01"),mp.mpf("0.001")):
        # Split at the layer scale p; this checks the original x-integrand.
        numeric("E15", f"Difference-quotient quadrature t={pp}", mp.quad(lambda z:pp/(z*z+pp*pp),[0,pp,1]), mp.atan(1/pp))
    numeric("E15", "Rescaled derivative-layer quadrature", mp.quad(lambda z:2*z*z/(1+z*z)**2,[1,2]), mp.atan(2)-mp.pi/4+mp.mpf("0.1"))

    example("E16", "Kernel identities and one test function do not prove recovery for every bounded Borel function continuous at zero. The DCT and epsilon-tail proofs establish that result.")
    exact("E16", "Kernel normalization", sp.integrate(p*sp.exp(-p*x),(x,0,sp.oo)), 1)
    exact("E16", "Kernel first moment", sp.integrate(p*sp.exp(-p*x)*x,(x,0,sp.oo)), 1/p)
    exact("E16", "Kernel tail", sp.integrate(p*sp.exp(-p*x),(x,delta,sp.oo)), sp.exp(-p*delta))
    exact("E16", "Kernel mass on shrinking interval", sp.integrate(p*sp.exp(-p*x),(x,0,1/p)), 1-sp.exp(-1))
    exact("E16", "Test function g(x)=exp(-x)", sp.integrate(p*sp.exp(-(p+1)*x),(x,0,sp.oo)), p/(p+1))
    for N in (1,7,100):
        numeric("E16", f"Rescaled test-function quadrature n={N}", mp.quad(lambda z:mp.exp(-z)*mp.exp(-z/N),[0,1,mp.inf]), mp.mpf(N)/(N+1))


def write_report(destination: Path) -> bool:
    for identifier, record in RESULTS.items():
        checks = record["checks"]
        record["status"] = "proof_only_no_computational_claim" if not checks else ("passed" if all(c["passed"] for c in checks) else "FAILED")
        record["performed_check_count"] = len(checks)
        record["source_files"] = [{"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
                                  for path in sorted((ROOT/"examples").glob(identifier+"-*.md"))]
    total = sum(len(r["checks"]) for r in RESULTS.values())
    failures = sum(not c["passed"] for r in RESULTS.values() for c in r["checks"])
    report = {
        "schema_version": 1, "run_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Concrete identity checks only; not proofs of analytic hypotheses or formal verification.",
        "not_checked": ["measurability and nonmeasurability", "Fubini/Tonelli/DCT hypotheses", "area/coarea theorem applicability and Hausdorff normalization", "all-parameter and infinite-stage assertions", "independent mathematical review", "Lean/formal verification"],
        "environment": {"python": platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__,"mpmath_decimal_digits":mp.mp.dps},
        "script": {"path":str(Path(__file__).resolve().relative_to(ROOT)),"sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
        "summary": {"examples":len(RESULTS),"performed_checks":total,"failed_checks":failures,"status":"passed" if failures==0 else "FAILED"},
        "examples": RESULTS,
    }
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    for identifier, record in RESULTS.items():
        print(f"{identifier}: {record['status']} ({record['performed_check_count']} concrete checks)")
    print(f"{total} concrete checks; {failures} failed. Report: {destination}")
    print("Analytic hypotheses require the written proofs and independent review. No Lean/formal verification.")
    return failures == 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=ROOT/"checks"/"check-results.json")
    args = parser.parse_args()
    check_all()
    return 0 if write_report(args.output.resolve()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
