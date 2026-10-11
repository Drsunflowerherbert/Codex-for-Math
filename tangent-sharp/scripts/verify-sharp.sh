#!/usr/bin/env bash
set -euo pipefail
source "$(dirname -- "${BASH_SOURCE[0]}")/environment.sh"
cd "$TANGENT_PROJECT_DIR"

# This extension writes fresh evidence separately from the historical cubic logs.
export TANGENT_RESEARCH_LOG_DIR="${1:-$TANGENT_PROJECT_DIR/.cache/research/verify-sharp}"
for log_name in build.log public-inventory.log private-inventory.log source-audit.log; do
  log_path="$(realpath -m "$TANGENT_RESEARCH_LOG_DIR/$log_name")"
  if git ls-files --error-unmatch -- "$log_path" >/dev/null 2>&1; then
    printf '%s\n' 'Refusing to overwrite a tracked verification log.' >&2
    exit 1
  fi
done
mkdir -p "$TANGENT_RESEARCH_LOG_DIR"
manifest_before="$(sha256sum lake-manifest.json)"
check_manifest() {
  local result=$?
  trap - EXIT
  if [[ "$manifest_before" != "$(sha256sum lake-manifest.json)" ]]; then
    printf '%s\n' 'ERROR: lake-manifest.json changed during verification.' >&2
    result=1
  fi
  exit "$result"
}
trap check_manifest EXIT

{
  date -u '+%Y-%m-%d %H:%M:%S UTC'
  lean_version="$(lake env lean --version)"
  printf '%s\n' "$lean_version"
  [[ "$lean_version" == *'version 4.24.0,'* ]]
  [[ "$lean_version" == *'commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b'* ]]
  test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = f897ebcf72cd16f89ab4577d0c826cd14afaafc7
  git -C .lake/packages/mathlib rev-parse HEAD
  lake build
} 2>&1 | tee "$TANGENT_RESEARCH_LOG_DIR/build.log"
lake env lean scripts/TheoremInventory.lean 2>&1 | tee "$TANGENT_RESEARCH_LOG_DIR/public-inventory.log"
lake env lean scripts/PrivateInventory.lean 2>&1 | tee "$TANGENT_RESEARCH_LOG_DIR/private-inventory.log"
python3 -E - <<'PY' | tee "$TANGENT_RESEARCH_LOG_DIR/source-audit.log"
from pathlib import Path
import hashlib
import os
import re

files = [Path('TangentLimit.lean'), *sorted(Path('TangentLimit').glob('*.lean'))]
public_names = set()
private_names = set()
for path in files:
    text = path.read_text()
    for forbidden in (r'\bsorry\b', r'\badmit\b', r'^\s*(?:unsafe\s+)?axiom\b'):
        assert not re.search(forbidden, text, re.M), (path, forbidden)
    public_names.update('TangentLimit.' + name for name in
                        re.findall(r'(?m)^(?:theorem|lemma|def)\s+(\w+)', text))
    private_names.update(re.findall(r'(?m)^private\s+(?:theorem|lemma|def)\s+(\w+)', text))
    print(f'PASS: {path} SHA256={hashlib.sha256(path.read_bytes()).hexdigest()}')
allowed = {'propext', 'Classical.choice', 'Quot.sound'}
public_count, private_count = len(public_names), len(private_names)
for name, expected in [('public-inventory.log', public_count), ('private-inventory.log', private_count)]:
    text = (Path(os.environ['TANGENT_RESEARCH_LOG_DIR']) / name).read_text()
    assert 'sorryAx' not in text, name
    axiom_lists = re.findall(r'depends on axioms: \[([^\]]*)\]', text)
    assert len(axiom_lists) == expected, (name, len(axiom_lists), expected)
    observed_names = re.findall(r"'([^']+)' depends on axioms:", text)
    assert len(set(observed_names)) == expected, (name, 'duplicate audit entries')
    if name == 'public-inventory.log':
        assert set(observed_names) == public_names, (name, 'inventory does not match source names')
    else:
        assert {item.rsplit('.', 1)[-1] for item in observed_names} == private_names
    observed = {item.strip() for group in axiom_lists for item in group.split(',') if item.strip()}
    assert observed <= allowed, (name, observed)
    print(f'PASS: {name}: {expected} declarations; axioms={sorted(observed)}')
print(f'PASS: {public_count + private_count} source declarations audited '
      f'({public_count} public, {private_count} private); no placeholders or added axioms')
PY
