"""Freshly build this project and verify its exact toolchain/dependency pins.

Run with the Lean 4.24.0 `lake` on PATH after materializing pinned dependencies.
Only this project's generated .lake/build directory is removed.
"""
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,default=ROOT/'logs/current')
LOGS = parser.parse_args().output
LOGS.mkdir(parents=True,exist_ok=True)
PIN = "f897ebcf72cd16f89ab4577d0c826cd14afaafc7"
assert (ROOT / "lean-toolchain").read_text().strip() == "leanprover/lean4:v4.24.0"
manifest = json.loads((ROOT / "lake-manifest.json").read_text())
assert next(p for p in manifest["packages"] if p["name"] == "mathlib")["rev"] == PIN
lake = shutil.which("lake")
if lake is None:
    raise SystemExit("Place the Lean 4.24.0 Lake executable on PATH.")
version = subprocess.check_output([lake, "env", "lean", "--version"], cwd=ROOT, text=True)
assert "version 4.24.0," in version, version
mathlib = ROOT / ".lake/packages/mathlib"
assert subprocess.check_output(["git", "-C", str(mathlib), "rev-parse", "HEAD"],
                               text=True).strip() == PIN
assert not subprocess.check_output(["git", "-C", str(mathlib), "status", "--porcelain"],
                                   text=True).strip()
sources = sorted((ROOT / "PositiveBlocks").glob("*.lean"))
sources = [p for p in sources if "Scratch" not in p.name]
sources.append(ROOT / "PositiveBlocks.lean")
hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
          for p in sources}
build = ROOT / ".lake/build"
assert build.resolve().is_relative_to(ROOT.resolve())
if build.exists():
    shutil.rmtree(build)
started = datetime.now(timezone.utc)
with (LOGS / "fresh-build.log").open("w") as log:
    result = subprocess.run([lake, "build"], cwd=ROOT, stdout=log,
                            stderr=subprocess.STDOUT, text=True)
finished = datetime.now(timezone.utc)
assert hashes == {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in sources}, "Source changed during the fresh build"
report = {"status": "passed" if result.returncode == 0 else "failed",
          "exit_code": result.returncode, "started_utc": started.isoformat(),
          "finished_utc": finished.isoformat(), "lean_version": version.strip(),
          "mathlib_rev": PIN, "fresh_project_build": True,
          "dependencies": "Pinned clean-source mathlib; dependency OLeans reused",
          "source_sha256": hashes}
(LOGS / "fresh-build.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
sys.exit(result.returncode)
