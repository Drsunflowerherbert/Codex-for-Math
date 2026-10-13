#!/usr/bin/env python3
"""Independent rational slice check of all nine affine-cell joint masses.

The expected values are integrated from interval intersections, without using
polygon clipping or the closed-form joint mass matrix. The scoped checker is
loaded only to obtain the actual polygon-geometry result being compared.
This is finite exact arithmetic evidence, not a Lean or uniform real proof.
"""

from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]


def joint_by_slices(a: F, b: F) -> list[list[F]]:
    if not 0 < a < 1:
        raise ValueError("the independent fixed-strip calculation needs 0<a<1")
    # The moving half-width is clamp(a+b*t,0,1). Every affine expression
    # changes only where its unclipped value equals 0, a, or 1.
    cuts = {F(-1), F(1)}
    if b:
        cuts |= {t for t in (-a/b, F(0), (1-a)/b) if -1 < t < 1}
    cuts = sorted(cuts)
    fixed = [(-F(1), -a), (-a, a), (a, F(1))]

    def lengths(t: F) -> list[list[F]]:
        h = max(F(0), min(F(1), a+b*t))
        moved = [(-F(1), -h), (-h, h), (h, F(1))]
        return [[max(F(0), min(r, s)-max(l, q))
                 for q, s in moved] for l, r in fixed]

    out = [[F(0) for _ in range(3)] for _ in range(3)]
    for left, right in zip(cuts, cuts[1:]):
        ll, rr = lengths(left), lengths(right)
        for i in range(3):
            for j in range(3):
                # Exact trapezoid integral times the square density 1/4.
                out[i][j] += (right-left)*(ll[i][j]+rr[i][j])/8
    return out


def main() -> None:
    script = ROOT / "scripts" / "check_exact.py"
    spec = importlib.util.spec_from_file_location("review_exact", script)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load the scoped geometry checker")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    parameters: set[tuple[F, F]] = set()
    for name in ("exact-cases.json", "regression-grid.json"):
        for case in json.loads((ROOT / "data" / name).read_text())["cases"]:
            parameters.add((F(case["a"]), F(case["b"])))
    # These independent choices include negative tilt and clipped widths.
    for a in (F(1,7), F(1,4), F(1,2), F(3,4), F(8,9)):
        for b in (F(-2,3), F(-1,8), F(0), F(1,8), F(2,3)):
            parameters.add((a, b))

    for a, b in sorted(parameters):
        expected = joint_by_slices(a, b)
        actual = module.common_source_geometry(a, b)["common_source_joint_mass_matrix"]
        if expected != actual:
            raise ValueError(f"joint mass mismatch at a={a}, b={b}: {expected} != {actual}")
    print("Independent interval-slice integration agrees with all 9 polygon joint "
          f"masses for {len(parameters)} distinct rational pairs, including clipped "
          "and negative-b cases.")


if __name__ == "__main__":
    main()
