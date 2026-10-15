#!/usr/bin/env python3
"""Optional independent symbolic checks (requires SymPy).

This script intentionally imports no classifier implementation.  It checks
explicit polynomial identities and elimination certificates, rather than
reimplementing the classifier.  Its output is suitable for a saved evidence
log.  The standard-library regression suite needs no SymPy installation.
"""

import json
import sympy as sp


def check():
    x, y, z = sp.symbols("x y z")
    records = []
    for sign in (1, -1):
        f = (y - x**2)**2 + sign * y**4
        phi = x**2 - 2 * sign * x**6 + 12 * x**10 - 96 * sign * x**14 + 880 * x**18
        h_sub = sp.Poly(sp.diff(f, y).subs(y, phi).expand(), x)
        g_sub = sp.Poly(f.subs(y, phi).expand(), x)
        expected = {8: sign, 12: -4, 16: 24 * sign}
        assert all(h_sub.nth(k) == 0 for k in range(19))
        assert all(g_sub.nth(k) == expected.get(k, 0) for k in range(19))

        # E(x,g(x))=0.  E_z(0,0)=-1, so this resultant has a unique
        # analytic branch through (0,0); its first x term is sign*x^8.
        elimination = sp.expand(sp.resultant(sp.diff(f, y), f - z, y) / 16)
        expected_elimination = (16 * x**12 - 48 * x**8 * z + sign * x**8
                                + 48 * x**4 * z**2 - 20 * sign * x**4 * z
                                - 16 * z**3 - 8 * sign * z**2 - z)
        assert sp.expand(elimination - expected_elimination) == 0
        assert sp.diff(elimination, z).subs({x: 0, z: 0}) == -1
        records.append({
            "case": "(y-x^2)^2" + ("+y^4" if sign > 0 else "-y^4"),
            "phi_through_order_18": str(phi),
            "residual_through_order_18": str(sum(c * x**k for k, c in expected.items())),
            "critical_equation_remainder_first_order": min(k[0] for k, c in h_sub.terms() if c),
            "resultant_divided_by_16": str(elimination),
            "checks": "exact symbolic coefficient and resultant identities passed",
        })

    # A degree-three polynomial already hides order four and a negative sign.
    f = y**2 + 2 * x**2 * y
    assert sp.expand(f.subs(y, -x**2)) == -x**4
    assert sp.diff(f, y).subs(y, -x**2) == 0

    # Identically-zero residual with a curved critical locus, even after
    # multiplication by a nonconstant unit which is positive at the origin.
    f = (y - x**2)**2 * (1 + x + 2 * y)
    assert f.subs(y, x**2) == 0
    assert sp.diff(f, x).subs(y, x**2) == 0
    assert sp.diff(f, y).subs(y, x**2) == 0
    return {
        "tool": "SymPy", "version": sp.__version__, "status": "passed",
        "stress_cases": records,
        "other_checks": ["degree-three hidden negative quartic",
                         "zero residual with positive nonconstant unit"],
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2, sort_keys=True))
