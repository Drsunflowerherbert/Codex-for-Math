#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
source scripts/environment.sh
convex_output=${1:-logs/current}
mkdir -p "$convex_output"
{
  printf '%s\n' 'COMMAND: lean --version'
  lean --version
  printf '%s\n' 'COMMAND: lake --version'
  lake --version
  python3 scripts/verify-evidence.py pins
  printf '%s\n' 'EXIT: 0'
} > "$convex_output/final-environment.log" 2>&1
{
  printf '%s\n' 'COMMAND: remove only the task-local .lake/build and run lake build (all root imports)'
  rm -rf .lake/build
  lake build
  printf '%s\n' 'EXIT: 0'
} > "$convex_output/final-build.log" 2>&1
{
  printf '%s\n' 'COMMAND: lake env lean scripts/Audit.lean'
  lake env lean scripts/Audit.lean
  printf '%s\n' 'EXIT: 0'
} > "$convex_output/final-type-axiom-audit.log" 2>&1
python3 scripts/verify-evidence.py audit "$convex_output/final-type-axiom-audit.log" > "$convex_output/final-source-audit.log" 2>&1
cat "$convex_output/final-environment.log"
cat "$convex_output/final-build.log"
cat "$convex_output/final-source-audit.log"
lake env lean scripts/SupplementalAudit.lean > "$convex_output/supplemental-type-axiom-audit.log" 2>&1
