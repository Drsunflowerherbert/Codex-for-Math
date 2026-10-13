# Small deterministic exact certificate search

`finder.py` is an explicitly incomplete helper for hand-sized inputs. It accepts
problem-only JSON `{ "version": 1, "problem": ... }` using the same objective,
row, dimension, and rational conventions as the verifier. A full certificate
document is not a problem-only input. Every result contains `incomplete: true`.

```sh
python3 finder.py notes/finder-example.json > /tmp/found.json
python3 - <<'PY'
import json
from pathlib import Path
d = json.loads(Path('/tmp/found.json').read_text())
if d['status'] != 'found':
    raise SystemExit('No certificate found by this bounded search')
Path('/tmp/certificate.json').write_text(json.dumps(d['certificate_document']) + '\n')
PY
python3 verifier.py /tmp/certificate.json
python3 bridge.py check /tmp/certificate.json --output /tmp/found-lean-new \
  --lean-bin /absolute/lean-4.24.0-linux/bin
```

The extraction step runs only when the finder actually returned a witness.
`found` means the emitted certificate passed the exact Python verifier.
`lean_checked` from the last command additionally requires a fresh Lean proof
of the generated original-input instance. The finder itself grants no Lean
acceptance. The supplied example's objective maximum is `10`.

The search supports at most three variables and eight original rows. It uses
deterministic exact rational row reduction to test candidate points formed from
constraint/coordinate-zero hyperplanes, then solves small-support rational
systems for optimality or strict contradiction weights. For improving rays it
tests the finite integer grid `[-2,2]^n`. All points, weights, and directions
remain in the original variable space; no slack or artificial decision variables
are introduced. Equality weights may be negative. Proposed witnesses are passed
through `verifier.verify` before any `found` result is emitted.

The same input yields the same result. Ties and underdetermined systems use a
fixed row/coordinate order and a particular solution with free coordinates set
to zero. These conventions do not choose a unique mathematical certificate or
an optimal normalization. No mathematical completeness or termination theorem
for all rational LPs is claimed.

An unsuccessful supported search returns `unknown` with a reason and search
counts; exceeding finder limits also returns `unknown`. Malformed or unsupported
verifier-schema inputs return `invalid`. Computed arithmetic/formatting limits
return `unknown` with `reason: "search_arithmetic_limit"`. None of these outcomes
classifies the LP. CLI exits are `0` for `found`, `1` for `unknown`, and `2` for
`invalid`.

The incompleteness occurs even inside the advertised dimension/row limits.
For `maximize x` subject to `3x-y=0`, the point `(0,0)` is feasible and the
direction `(1,3)` certifies unboundedness. The helper's finite ray grid contains
no nonzero direction satisfying that equation, so it returns `unknown`.
The general exact verifier can still check the manually supplied certificate.

The independent bounded experiment examined 4,374 one-dimensional two-row
problems and independently verified every emitted witness against original row
directions and the original objective. All nine existing accepted example
problems also produced valid witnesses. These finite experiments are evidence
about this implementation, not a completeness proof or a substitute for the
checked bridge's per-instance Lean rechecking.
