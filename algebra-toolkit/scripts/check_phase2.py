#!/usr/bin/env python3
"""Run the continuation's exact checks and bind results to executed sources."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import platform
import subprocess
import sys

import sympy

root = Path(__file__).resolve().parents[1]
evidence = root / "evidence"
evidence.mkdir(exist_ok=True)
cases = [
    ("check_sylvester.py", 7),
    ("check_averaging.py", 5),
    ("check_integral_crt.py", 12),
    ("check_lifting.py", 4),
]
records = []
for name, expected_groups in cases:
    path = root / "scripts" / name
    result = subprocess.run([sys.executable, str(path)], cwd=root,
                            text=True, capture_output=True, check=False)
    log_name = name.removesuffix(".py") + ".log"
    (evidence / log_name).write_text(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(f"{name} failed; inspect evidence/{log_name}")
    if name == "check_sylvester.py":
        actual_groups = result.stdout.count("\nPASS ") + result.stdout.startswith("PASS ")
        detail = {"summary": result.stdout.splitlines()}
    else:
        detail = json.loads(result.stdout)
        if name == "check_lifting.py":
            actual_groups = len(detail["checks"])
            assert detail["status"] == "pass"
        else:
            actual_groups = detail["groups"]
            assert detail.get("passed", detail.get("status") == "passed")
    assert actual_groups == expected_groups, (name, actual_groups)
    records.append({"script": f"scripts/{name}", "groups": actual_groups,
                    "script_sha256": sha256(path.read_bytes()).hexdigest(),
                    "log": f"evidence/{log_name}", "detail": detail})
    print(f"PASS {name}: {actual_groups} exact groups", flush=True)

# Check the narrow source erratum by the definition, independently of
# the printed example: Disc(f) = (-1)^(3*2/2) Res(f,f') for monic cubics.
t, p, q = sympy.symbols("t p q")
f = t**3 + p*t + q
res = sympy.resultant(f, sympy.diff(f, t), t)
assert sympy.expand(res - 4*p**3 - 27*q**2) == 0
assert sympy.discriminant(t**3 + t, t) == -4
erratum = {"statement": "Disc(t^3+p*t+q)=-4*p^3-27*q^2",
           "resultant": str(res), "specialization_p1_q0": -4}
record = {
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "status": "pass",
    "runner_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    "python": platform.python_version(), "sympy": sympy.__version__,
    "chapter_check_groups": sum(r["groups"] for r in records),
    "source_erratum_check_groups": 1, "checks": records,
    "source_erratum": erratum,
    "scope": "Exact fixed examples and finite identity checks, not formal verification or a search campaign.",
}
(evidence / "phase2-checks.json").write_text(json.dumps(record, indent=2) + "\n")
print("PASS: 28 continuation groups and 1 cubic-discriminant check.")
