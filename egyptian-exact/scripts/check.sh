#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
task_root="$(pwd)"
if [[ -x "$task_root/tooling/elan/bin/lake" ]]; then
  export ELAN_HOME="$task_root/tooling/elan"
  export PATH="$task_root/tooling/elan/bin:$PATH"
fi
export MATHLIB_CACHE_DIR="${MATHLIB_CACHE_DIR:-$task_root/tooling/mathlib-cache}"
mkdir -p evidence
lake build 2>&1 | tee evidence/final-build.log
lake env lean Evidence.lean 2>&1 | tee evidence/public-statements.log
python3 scripts/check_exact.py | tee evidence/exact-check.log
