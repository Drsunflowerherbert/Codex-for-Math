#!/usr/bin/env bash
# Source this helper. Select Lean/Lake 4.24.0 explicitly; no installation is run.
if [[ -n "${CONVEX_LEAN_BIN:-}" ]]; then
  export PATH="$CONVEX_LEAN_BIN:$PATH"
fi
if ! command -v lean >/dev/null 2>&1 || ! command -v lake >/dev/null 2>&1; then
  printf '%s\n' 'Lean/Lake 4.24.0 required: set CONVEX_LEAN_BIN or put them on PATH.' >&2
  return 1 2>/dev/null || exit 1
fi
