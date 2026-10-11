#!/usr/bin/env bash
set -euo pipefail
source "$(dirname -- "${BASH_SOURCE[0]}")/environment.sh"
cd "$TANGENT_PROJECT_DIR"
mkdir -p logs
if [[ ! -x "$ELAN_HOME/bin/elan" ]]; then
  curl --fail --location --retry 3 \
    https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh \
    -o logs/elan-init.sh
  sh logs/elan-init.sh -y --no-modify-path --default-toolchain none \
    > logs/setup-elan.log 2>&1
fi
elan toolchain install leanprover/lean4:v4.24.0 > logs/setup-lean.log 2>&1
if [[ -f lake-manifest.json ]]; then
  printf '%s\n' 'Using the checked-in lake-manifest.json without updating dependencies.' \
    > logs/setup-lake-update.log
else
  MATHLIB_NO_CACHE_ON_UPDATE=1 lake update mathlib > logs/setup-lake-update.log 2>&1
fi
lake exe cache get > logs/setup-mathlib-cache.log 2>&1
lake env lean --version > logs/setup-version.log 2>&1
cat logs/setup-version.log
