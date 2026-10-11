#!/usr/bin/env bash
# Source this file to use the pinned compiler without changing shell profiles.
TANGENT_PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ -z "${ELAN_HOME:-}" ]]; then
  export ELAN_HOME="$TANGENT_PROJECT_DIR/.elan"
fi
export PATH="$ELAN_HOME/bin:$PATH"
export MATHLIB_CACHE_DIR="${MATHLIB_CACHE_DIR:-$TANGENT_PROJECT_DIR/.cache/mathlib}"
export USE_FRO_CACHE=1
