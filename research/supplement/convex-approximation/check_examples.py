"""Original finite checks for the accompanying ordinary mathematical proof.

Standard library only. No downloaded code, installations, Lean execution, or
whole-source validation. Numerical samples are consistency checks, not proofs.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parent


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def norm(x):
    return math.sqrt(dot(x, x))


def logsumexp(values):
    m = max(values)
    return m + math.log(sum(math.exp(x - m) for x in values))


def log_phi(x, directions, support, epsilon, t):
    return logsumexp([
        t * (dot(u, x) - support(u) - epsilon) for u in directions
    ])


def radius(anchor, theta, directions, support, epsilon, t):
    def f(r):
        x = tuple(a + r * v for a, v in zip(anchor, theta))
        return log_phi(x, directions, support, epsilon, t)

    assert f(0.0) < 0.0
    lo, hi = 0.0, 1.0
    while f(hi) < 0.0:
        hi *= 2.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if f(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def circle_net(n):
    return [
        (math.cos((2 * k + 1) * math.pi / n),
         math.sin((2 * k + 1) * math.pi / n))
        for k in range(n)
    ]


def exact_checks():
    directions = [
        (Q(sx * a, 5), Q(sy * b, 5))
        for a, b in [(3, 4), (4, 3)]
        for sx in [-1, 1] for sy in [-1, 1]
    ]
    for u in directions:
        assert dot(u, u) == 1
    checked_pairs = 0
    for u in directions:
        for v in directions:
            distance_squared = sum((a - b) ** 2 for a, b in zip(u, v))
            assert dot(u, v) == 1 - distance_squared / 2
            checked_pairs += 1
    point = (Q(0), Q(3, 4))
    slacks = [abs(u[0]) - dot(u, point) for u in directions]
    assert all(s >= 0 for s in slacks)
    c, s, delta_squared = Q(4, 5), Q(3, 5), Q(2, 5)
    assert c == 1 - delta_squared / 2
    assert c * c + s * s == 1
    assert s * s == delta_squared * (1 - delta_squared / 4)
    assert min(slacks) == 0
    return {
        "arithmetic": "fractions.Fraction exact rational arithmetic",
        "unit_vector_identity_pairs": checked_pairs,
        "rational_normals": [[str(a), str(b)] for a, b in directions],
        "segment": "[-1,1] x {0}",
        "point_in_finite_support_polytope": ["0", "3/4"],
        "support_slacks": [str(x) for x in slacks],
        "distance_of_point_to_segment": "3/4",
        "covering_constant_c": str(c),
        "covering_radius_squared": str(delta_squared),
        "tangential_constant_s": str(s),
        "covering_constant_proof": "study.md section 8; not inferred from samples",
        "passed": True,
    }


def planar_checks():
    shapes = [
        ("singleton", 0.0, lambda u: 0.0, lambda x: norm(x)),
        ("segment", 3.0, lambda u: 1.5 * abs(u[0]),
         lambda x: math.hypot(max(abs(x[0]) - 1.5, 0.0), x[1])),
        ("disk", 4.0, lambda u: 2.0,
         lambda x: max(norm(x) - 2.0, 0.0)),
        ("rectangle", math.sqrt(5.0),
         lambda u: abs(u[0]) + 0.5 * abs(u[1]),
         lambda x: math.hypot(max(abs(x[0]) - 1.0, 0.0),
                            max(abs(x[1]) - 0.5, 0.0))),
    ]
    rows = []
    for n in [8, 16, 32]:
        directions = circle_net(n)
        delta = 2.0 * math.sin(math.pi / (2.0 * n))
        c = 1.0 - delta * delta / 2.0
        s = delta * math.sqrt(1.0 - delta * delta / 4.0)
        epsilon = 0.05
        t = 2.0 * math.log(n) / epsilon
        for name, diameter, support, distance in shapes:
            largest = 0.0
            max_residual = 0.0
            for k in range(96):
                angle = 2.0 * math.pi * k / 96.0
                theta = (math.cos(angle), math.sin(angle))
                r = radius((0.0, 0.0), theta, directions, support, epsilon, t)
                x = tuple(r * a for a in theta)
                largest = max(largest, distance(x))
                max_residual = max(max_residual, abs(
                    log_phi(x, directions, support, epsilon, t)))
            bound = (epsilon + s * diameter) / c
            assert largest <= bound + 1e-10
            assert max_residual < 1e-9
            row = {
                "shape": name, "normal_count": n,
                "sampled_boundary_directions": 96,
                "delta": delta, "epsilon": epsilon, "t": t,
                "sampled_maximum_distance": largest,
                "proved_general_bound": bound,
                "largest_log_level_residual": max_residual,
            }
            if name == "disk":
                ball_bound = (epsilon + 2.0 * delta * delta / 2.0) / c
                assert largest <= ball_bound + 1e-10
                row["proved_ball_bound"] = ball_bound
            if name == "segment":
                obstruction = 1.5 * math.tan(math.pi / n)
                assert largest >= obstruction - 1e-10
                row["proved_finite_direction_obstruction"] = obstruction
            rows.append(row)
    return rows


def exact_formula_numerical_checks():
    rows = []
    epsilon = 0.2
    for d in [1, 2, 3, 5]:
        directions = []
        for i in range(d):
            for sign in [-1.0, 1.0]:
                u = [0.0] * d
                u[i] = sign
                directions.append(tuple(u))
        t = 2.0 * math.log(2.0 * d) / epsilon
        diagonal = tuple(1.0 / math.sqrt(d) for _ in range(d))
        computed = radius((0.0,) * d, diagonal, directions,
                          lambda u: 0.0, epsilon, t)
        formula = math.sqrt(d) / t * math.acosh(math.exp(t * epsilon) / (2 * d))
        assert abs(computed - formula) < 1e-12
        rows.append({
            "example": "axes_singleton",
            "dimension": d, "epsilon": epsilon, "t": t,
            "formula_outer_radius": formula,
            "bisection_diagonal_radius": computed,
            "absolute_difference": abs(computed - formula),
        })
    for a, b in [(0.0, 0.0), (-1.0, 1.0), (2.0, 2.5)]:
        length, center = b - a, (a + b) / 2.0
        directions = [(-1.0,), (1.0,)]
        t = 2.0 * math.log(2.0) / epsilon
        support = lambda u: b if u[0] > 0 else -a
        computed = radius((center,), (1.0,), directions, support, epsilon, t)
        formula = math.acosh(math.exp(t * (length / 2 + epsilon)) / 2) / t
        error = formula - length / 2
        assert abs(computed - formula) < 1e-12
        assert 0.0 < error < epsilon
        rows.append({
            "example": "interval",
            "interval": [a, b],
            "formula_radius": formula,
            "bisection_radius": computed,
            "exact_formula_evaluated_error": error,
            "epsilon": epsilon,
        })
    return rows


def nesting_check():
    diameter = 2.0
    delta_1 = 0.5
    delta_2 = delta_1 / (8.0 * (1.0 + diameter))
    barriers = []
    support = lambda u: abs(u[0])
    for delta in [delta_1, delta_2]:
        n = math.ceil(math.pi / (2.0 * math.asin(delta / 2.0)))
        barriers.append((circle_net(n), delta, 2.0 * math.log(n) / delta))
    old, eps_old, t_old = barriers[0]
    new, eps_new, t_new = barriers[1]
    largest_old_value = -math.inf
    for k in range(48):
        angle = 2.0 * math.pi * k / 48
        theta = (math.cos(angle), math.sin(angle))
        r = radius((0.0, 0.0), theta, new, support, eps_new, t_new)
        x = tuple(r * a for a in theta)
        largest_old_value = max(largest_old_value,
                               log_phi(x, old, support, eps_old, t_old))
    assert largest_old_value < 0.0
    return {
        "shape": "[-1,1] x {0}",
        "delta_1": delta_1,
        "delta_2": delta_2,
        "normal_counts": [len(old), len(new)],
        "proved_interlevel_distance_lower_bound": delta_1 / 4.0,
        "sampled_new_boundary_directions": 48,
        "largest_old_log_barrier_on_sampled_new_boundary": largest_old_value,
        "note": "Samples supplement the full-set proof in study.md section 7.",
    }


def main():
    examples = {
        "scope": "Finite exact checks and numerical illustrations; not theorem proofs.",
        "exact_rational_checks": exact_checks(),
        "planar_boundary_checks": planar_checks(),
        "closed_formula_checks": exact_formula_numerical_checks(),
        "nested_neighborhood_check": nesting_check(),
    }
    (ROOT / "examples.json").write_text(json.dumps(examples, indent=2) + "\n")
    script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    verification = {
        "scope": "Only the local approximation lemma and derived results.",
        "ordinary_proof": {
            "status": "independently_reviewed_ordinary_proof",
            "files": ["study.md", "audit.md"],
            "reviewed_items": [
                "source planar construction", "quantitative finite-dimensional extension",
                "coercivity and Hessian positivity", "boundary identification",
                "analytic radial parametrization", "compact nesting",
                "dimension one and lower-dimensional cases",
                "exact examples and angular-order obstruction",
            ],
        },
        "computation": {
            "script": "check_examples.py",
            "script_sha256": script_hash,
            "dependencies": "Python standard library only",
            "downloaded_code_executed": False,
            "software_installed": False,
            "exact_rational_checks_passed": True,
            "numerical_cases": 12,
            "boundary_samples_per_case": 96,
            "closed_formula_cases": 7,
            "nesting_boundary_samples": 48,
            "all_assertions_passed": True,
            "interpretation": "Finite consistency checks; do not establish global analytic claims.",
        },
        "lean": {"status": "not_run", "files_created": [], "kernel_verified": False},
        "whole_paper_validated": False,
        "headline_theorem_validated": False,
        "novelty_claim": False,
        "native_mrs_imported": False,
    }
    (ROOT / "verification.json").write_text(json.dumps(verification, indent=2) + "\n")
    print(json.dumps({"all_assertions_passed": True,
                      "planar_cases": len(examples["planar_boundary_checks"]),
                      "formula_cases": len(examples["closed_formula_checks"])},
                     indent=2))


if __name__ == "__main__":
    main()
