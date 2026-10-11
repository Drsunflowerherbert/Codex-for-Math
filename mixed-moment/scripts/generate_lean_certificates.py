"""Generate the 77 Lean rational equality statements; Lean must check all proofs.

Input: exact expectations independently recomputed by independent_checks.py.
The generator is untrusted: kernel checking, not this script, establishes the
Lean equalities. A corrupt expected value makes the corresponding proof fail.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'evidence/supplied/logs/lean-certificate-cases.json').read_text())
lines = [
    'import MixedMoments.Cancellation', '',
    '/-! Exact rational regression certificates checked by the Lean kernel.',
    'Generated from the independent certificate implementation. No floating point',
    'or substitutions for the real constants occur. These are finite formal-array',
    'equalities, not statements about unevaluated integrals. -/', '',
    'namespace MixedMoments.Certificates', '', 'open MixedMoments', '',
]
proof = [
    '  ext k',
    '  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,',
    '    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,',
    '    Finset.sum_range_succ]', '',
]
for kind in ('M', 'Z'):
    for case in data[kind]:
        i, j = case['i'], case['j']
        a, b, c = case['triple']
        lines += [f'theorem {kind.lower()}_{i}_{j} : formal{kind} {i} {j} = Coordinates.mk ({a}) ({b}) ({c}) := by'] + proof
for case in data['P_1_D_t']:
    j = case['j']
    a, b, c = case['triple']
    lines += [f'theorem one_x_{j} : formalEntry 1 Polynomial.X {j} = Coordinates.mk ({a}) ({b}) ({c}) := by',
              '  rw [formalEntry_one_X]'] + proof
lines += ['end MixedMoments.Certificates', '']
(ROOT / 'MixedMoments/Certificates.lean').write_text('\n'.join(lines))
print('Generated 77 exact Lean equalities; run lake build MixedMoments.Certificates.')
