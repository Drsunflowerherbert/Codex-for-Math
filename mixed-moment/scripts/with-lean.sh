#!/usr/bin/env bash
set -euo pipefail
if [[ -n "${MIXED_MOMENTS_LEAN_BIN:-}" ]]; then
  export PATH="$MIXED_MOMENTS_LEAN_BIN:$PATH"
fi
exec "$@"
