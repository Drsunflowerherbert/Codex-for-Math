#!/usr/bin/env bash
set -euo pipefail
source "$(dirname -- "${BASH_SOURCE[0]}")/environment.sh"
cd "$TANGENT_PROJECT_DIR"
mkdir -p logs
BUILD_STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
BUILD_LOG="logs/build-$BUILD_STAMP.log"
{
  lake env lean --version
  git -C .lake/packages/mathlib rev-parse HEAD
  lake build
} 2>&1 | tee "$BUILD_LOG"
cp "$BUILD_LOG" logs/build-latest.log
