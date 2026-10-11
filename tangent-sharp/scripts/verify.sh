#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/environment.sh"
cd "$TANGENT_PROJECT_DIR"
mkdir -p logs
{
  lake env lean --version
  git -C .lake/packages/mathlib rev-parse HEAD
  lake build
} 2>&1 | tee logs/final-build.log
inventory_file=scripts/MainInventory.lean
if [[ -f scripts/TheoremInventory.lean ]]; then inventory_file=scripts/TheoremInventory.lean; fi
lake env lean "$inventory_file" 2>&1 | tee logs/final-theorem-inventory.log
python3 - <<'PY' | tee logs/source-audit.log
from pathlib import Path
import re
files = [Path('TangentLimit.lean'), *sorted(Path('TangentLimit').glob('*.lean'))]
for path in files:
    text = path.read_text()
    for forbidden in (r'\bsorry\b', r'\badmit\b', r'^\s*axiom\b'):
        assert not re.search(forbidden, text, re.M), (path, forbidden)
    print(f'PASS: {path}')
inventory = Path('logs/final-theorem-inventory.log').read_text()
assert 'sorryAx' not in inventory
axiom_lists = re.findall(r'depends on axioms: \[([^\]]*)\]', inventory)
allowed_axioms = {'propext', 'Classical.choice', 'Quot.sound'}
observed_axioms = {
    item.strip() for group in axiom_lists for item in group.split(',') if item.strip()
}
declaration_count = sum(
    len(re.findall(r'(?m)^(?:theorem|lemma|def)\s+\w+', path.read_text()))
    for path in files
)
assert len(axiom_lists) == declaration_count, len(axiom_lists)
assert observed_axioms <= allowed_axioms, observed_axioms
print('PASS: no proof placeholders or added axiom declarations; no sorryAx in theorem inventory')
print(f'PASS: {len(axiom_lists)} declarations audited; only standard foundational axioms observed')
PY
