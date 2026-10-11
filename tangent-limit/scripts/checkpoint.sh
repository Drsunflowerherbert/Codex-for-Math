#!/usr/bin/env bash
set -euo pipefail
project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
checkpoint_label="${1:-checkpoint}"
checkpoint_stamp="$(date -u +%Y%m%dT%H%M%SZ)"
checkpoint_dir="$project_root/milestones/$checkpoint_stamp-$checkpoint_label"
mkdir -p "$checkpoint_dir"
cd "$project_root"
checkpoint_files=(TangentLimit TangentLimit.lean docs logs scripts lean-toolchain lakefile.toml PROGRESS.md)
if [[ -f lake-manifest.json ]]; then checkpoint_files+=(lake-manifest.json); fi
if [[ -f README.md ]]; then checkpoint_files+=(README.md); fi
tar -czf "$checkpoint_dir/project-state.tar.gz" "${checkpoint_files[@]}"
(cd "$checkpoint_dir" && sha256sum project-state.tar.gz > SHA256SUMS)
date -u +%FT%TZ > "$checkpoint_dir/timestamp.txt"
cp PROGRESS.md "$checkpoint_dir/PROGRESS.md"
printf '%s\n' "$checkpoint_dir"
