# Independent follow-up computational review

Follow-up starting commit: `44329696c0a8a7fd3405d1b7b7261a14bf7ebbbd`.
The independent verification reviewer authored only the two new independent
test files and this report. Existing first-round evidence is preserved.

## Finder review

The finder emits a certificate, or explicitly reports `unknown` with
`incomplete: true`. A returned certificate is checked independently against
the original row senses and original objective by the raw arithmetic predicate
from `tests/test_independent.py`. This review does not use the finder's RREF,
normalization or search helpers as an oracle.

All nine originally accepted fixture problems produce an independently valid
certificate. Repeating their searches yields identical results. A bounded
experiment covers all 27 one-dimensional rows with coefficient `-1,0,1`, sense
`<=,>=,=`, and right side `-1,0,1`; all ordered pairs of rows, objective
coefficients `-1,0,1`, and both objective senses are tested. Each of the 4,374
outputs is independently valid: 2,114 optimality certificates, 1,776
infeasibility certificates, and 484 unboundedness certificates. No invalid or
unknown output occurred in this finite experiment. This is a reported result
of that experiment, not a general completeness theorem.

An explicit incompleteness example lies within the documented dimensional and
row limits. For `3x-y=0` with objective maximizing `x`, `(0,0)+t(1,3)` is a
feasible improving ray. The supplied ray independently verifies, but the finder
returns `unknown`, with reason `no_certificate_in_bounded_search`, because its
integer direction grid is `[-2,2]^2`. Unknown therefore cannot classify the LP
as feasible, bounded, optimal, infeasible or unbounded. Exceeding the search
limits also returns unknown, including examples whose mathematical status is
easy to determine independently. Post-parse arithmetic limits may likewise
produce `search_arithmetic_limit`; this is another incomplete search outcome.

Additional cases cover zero variables, no constraints, negative feasible
coordinates, minimizing objectives, lower-dimensional equalities, noncanonical
but exact rational strings, malformed and duplicate-key JSON, injection strings
in numbers/senses/keys, forbidden floats and booleans, and CLI exit codes for
found, unknown and invalid.

## Exact arithmetic resource regression

The integrator found that the initially unbounded checker could multiply a
2,200-digit input by itself exactly, then raise `ValueError` while formatting
the 4,400-digit gain. The reproducer uses `a = "1" + "0" * 2199`, no rows,
maximization coefficient `a`, base `0`, and direction `a`.

The follow-up checker documents finite input and output budgets and fails closed
on exceeded budgets. Independent regressions verify that the exact reproducer
returns invalid, rather than acceptance or an exception. They also construct
sixteen individually permitted input fractions with approximately 1,000-bit
denominators whose combined arithmetic evidence exceeds the output budget.
The answer is invalid with `accepted: false`. A separate subprocess sets its
process-local decimal formatting limit to 640 digits and combines eight such
fractions; formatting fails closed to invalid without a traceback. This test
does not change persistent runtime settings.

Invalid or unsupported input and incomplete search results make no mathematical
claim about the LP. The generic Lean soundness statements remain about their
typed rational inputs; executable resource budgets are a separate boundary.

## Bridge review

The independent decoder parses only finite-vector syntax and rational literals
of the form `(integer : ℚ)` or `((integer : ℚ) / positiveinteger)`. It uses
`Fraction` directly and compares the generated problem's dimensions, every
original coefficient/right side/row sense, the original objective and its
sense, and every point/direction/combined source-order row weight with the
source document. It also checks the certificate-kind-specific acceptance
statement. No exporter normalization or semantic-table helper is an oracle.

All nine originally accepted fixture documents and four additional accepted
documents pass this decoding comparison. Additional documents cover an
interleaved minimizing problem with optimum `3`, a negative-coordinate
maximizing ray with objective gain `3`, a minimizing singleton written using
noncanonical exact rational strings, and the zero-dimensional no-row problem.
This is independent transcription evidence for these cases, not a formal
proof of the JSON parser or renderer.

Adversarial tests cover injection strings in numbers/senses/keys and paths,
forbidden floats and booleans, duplicate keys, invalid UTF-8, resource bounds,
malformed receipt records, unsafe or duplicate manifest paths, false hashes,
uncovered members, symlink paths, FIFO inputs and an existing destination.
Changing an original input, semantic table, generated source or trusted library
source remains invalid even after all package hashes are coherently rewritten.
Source tampering includes both an added arbitrary axiom and a purely numeric
coefficient change. None of these saved Lean texts is executed by the test.

A deliberately counterfeit, hash-consistent saved success receipt without
compilation phases is invalid. Blocking the fresh compiler produces failure,
despite the presence of that saved success flag. Package validation is an
integrity/consistency operation; only a new live `check_raw` or CLI recheck can
produce a fresh attempt. Recorded hashes do not authenticate historical
execution.

The serial independent live batch completed successfully at
`/tmp/lp-bridge-independent-live-20261013T024300Z`. All 75 recorded commands
exited `0`, all 13 inputs have final status `lean_checked`, the independently
specified Input gate passed, and each instance has the problem-definition
body gate, closed whole-type/axiom gates for acceptance and soundness, and
same-kernel replay. The three infeasibility instances replayed 177 declarations
each; the remaining ten instances replayed 178 each. Nineteen private task/helper
and instance products were built; no runtime `.work` or compiled products remain
in the portable 202-file package. The live-enabled suite ran 12 tests in
`315.706s`, exit `0`, with no skipped test.

The fixture documents in this independent run were read from their published
JSON files and reserialized without changing any field value. The preserved
input snapshots are the exact bytes fed to the live pipeline; their byte hashes
refer to those snapshots, rather than to whitespace in the original fixture
files. A subsequent supplemental audit starts from the observed valid package
and confirms that the input/semantic/generated/library tamper mutations really
change bytes before coherently rewriting hashes. It also confirms that arbitrary
saved command argv is metadata: validation does not execute it or make a fresh
acceptance claim.

A true CLI recheck then succeeded on a relocated one-certificate package copied
from the completed author smoke. Before rechecking, the reviewer changed the
saved first command argv to `['touch',
'/tmp/lp-bridge-untrusted-recorded-command-ran-20261013']` and rewrote the package
manifest hashes. Validation still treats this as metadata, rather than invoking
it or authenticating the old command history. The fresh CLI recheck generated
all sources again from the saved original JSON, rebuilt the six private modules,
ran all instance and postflight gates, and finished `lean_checked` with 63 new
commands exiting `0`. Its actual first command was the pinned Lean executable
with `--version`. The marker file never appeared. Both relocated input and fresh
output passed consistency validation with the same original JSON bytes.

The successful recheck output is
`/tmp/lp-bridge-independent-recheck-20261013T024900Z`. This is an observed fresh
execution, not acceptance derived from reading the saved receipt. No supplied
Lean source or saved command was executed.

## Corrections and retained failed attempts

This reviewer reported two bridge robustness issues, both corrected by the
author and covered by regressions. A receipt or input record that was not an
object could raise `AttributeError`; explicit object checks now reject it.
Opening a FIFO with blocking `O_RDONLY` could hang before the regular-file
check; `O_NONBLOCK` now lets the checker refuse it immediately. The CLI FIFO
regression returns invalid within its three-second subprocess timeout and
creates no attempt directory.

The first two real bridge attempts failed while compiling the preserved
`Examples.lean`, with exit `-6` and no diagnostics. Independent controlled
diagnosis compiled that same source with the pinned Lean command and existing
pinned caches: without an address-space cap it exited `0` in `5.79s`, with
maximum RSS `2,823,356 KiB`; adding only an `8 GiB` address-space cap reproduced
exit `-6` in `3.984s`, maximum RSS `2,762,796 KiB`. The author independently
confirmed that `16 GiB` works and raised the bounded virtual-address limit,
while retaining explicit `-j1 -M4096` and the CPU/time/log/file bounds. This
adjusts runtime capacity without weakening kernel checks.

The third real attempt compiled all six private task/helper modules and passed
the independent Input expected-statement gate, but failed at its first generated
instance. The offside indentation of the structure literal caused a parser
error; generated error-recovery `sorryAx` was explicitly rejected by the axiom
gate. The reviewer identified the alignment problem and the author aligned all
fields after newlines. No certificate acceptance is attributed to these failed
attempts. Their preserved attempt paths are:

```text
/tmp/lp-bridge-independent-live-20261013T022600Z
  failed: library-03 exit -6; independent suite 12 tests in 21.606s, exit 1
/tmp/lp-bridge-independent-live-20261013T022900Z
  failed: library-03 exit -6; independent suite 12 tests in 29.473s, exit 1
/tmp/lp-bridge-independent-live-20261013T023400Z
  failed: instance-0000 exit 1; independent suite 12 tests in 67.613s, exit 1
/tmp/lp-bridge-independent-live-20261013T023700Z
  failed: instance-0005 exit -9; independent suite 12 tests in 142.997s, exit 1
```

The fourth attempt was killed during concurrent Lean jobs. The environment has
a `16 GiB` cgroup memory limit and reported OOM kills; the simultaneously running
author process had approximately `6.2 GiB` RSS. This supports a resource-contention
diagnosis, rather than a source rejection. The runner reset every final input
status under global failure, preserving the partial logs without presenting a
completed checked package. Heavy Lean batches were subsequently serialized.
The next independent attempt completed with all 13 inputs and postflight gates.

## Commands and final results

Commands ran from `/workspace/lp-research/lp-certificates` under Python 3.12.14:

```text
$ python3 -m unittest discover -s tests -p 'test_finder_independent.py' -v
Ran 11 tests in 1.424s
OK
Independent finder counts: {'found': 4374, 'unknown': 0, 'invalid': 0} found kinds: {'optimal': 2114, 'infeasible': 1776, 'unbounded': 484}
exit code: 0

$ LP_BRIDGE_LEAN_BIN=/workspace/Codex-for-Math/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin LP_BRIDGE_KEEP_OUTPUT=/tmp/lp-bridge-independent-live-20261013T024300Z python3 -m unittest discover -s tests -p 'test_bridge_independent.py' -v
Ran 12 tests in 315.706s
OK
Independent fresh Lean package: /tmp/lp-bridge-independent-live-20261013T024300Z
Fresh Lean commands: 75 instances: 13
exit code: 0

$ LP_BRIDGE_EXISTING_PACKAGE=/tmp/lp-bridge-independent-live-20261013T024300Z python3 -m unittest discover -s tests -p 'test_bridge_independent.py' -v
Ran 13 tests in 0.642s
OK (skipped=1)
exit code: 0

$ python3 bridge.py recheck /tmp/lp-bridge-independent-relocated-input-20261013T024800Z --output /tmp/lp-bridge-independent-recheck-20261013T024900Z --lean-bin /workspace/Codex-for-Math/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin
{
  "failure": null,
  "receipt": "/tmp/lp-bridge-independent-recheck-20261013T024900Z/receipt.json",
  "status": "lean_checked"
}
exit code: 0

fresh status lean_checked; commands 63; all_zero True
old argv ['touch', '/tmp/lp-bridge-untrusted-recorded-command-ran-20261013']
fresh argv ['/workspace/Codex-for-Math/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lean', '--version']
marker exists False
fresh package consistency valid True
```

The supplementary test was added after the completed live batch; it does not
rerun Lean and explicitly skips the separate live test. The ordinary full
Python suite also passed at its observed pre-final-renderer snapshot: 142 tests
in `8.058s`, with one explicit live skip, exit `0`. Final aggregate verification
is the integrator's separate responsibility.

Completed independent live package hashes:

```text
receipt.json          ac9eb90fbc89dd03e22b2f2ff6b3b8df8a478058c4c2afc708c79c9e5b915c88
source-manifest.json  4dfedaee91a0a7b5306d5a6b46757fe18f7473d312be06aef91928644b4ca64f
package-manifest.json a7b50d6303cc43a425f987f254e92e69f7db5e157cb4a68470507277f731c6a9
started_utc 2026-10-13T02:43:06.698603+00:00
ended_utc   2026-10-13T02:48:22.092347+00:00
```

Completed relocated CLI recheck hashes:

```text
receipt.json          740610899a0d5ee2c42c64e2412cac7c8d9cfb2185323c206fe148a8449b7e0f
source-manifest.json  8cd1c3c38b977e1606c5f7c6479484cc938c27365619a8814a2d7638d5d21cc6
package-manifest.json ddec7875ae8b6226b382f8ca25141765e663974407686e6be3edeb4ec5f0d11d
started_utc 2026-10-13T02:48:58.615939+00:00
ended_utc   2026-10-13T02:50:12.603803+00:00
```

Reviewed final executable/test snapshots:

```text
bb55c5f57a91d9c8c225ab3dc219a718a383e13249314fff29b5a1ad33e290fb  verifier.py
c0fe2cbfc7511309f91524e86ed8e5342f0d891c090a343a0a1ee06736774dd2  bridge.py
bc91178bb5dd8b779ca6f565fa5cbea38c4feb2f0bbee7b9e07a795c43758876  finder.py
a4ce8d4544270acede387454157dc39af4046990ffef65cdb4e162d60625ea84  tests/test_bridge_independent.py
a701c339a869b91995286b55180a3e28a16fb54e3b834ee9a73d57895ba909f5  tests/test_finder_independent.py
```

No external service, Library operation, usage purchase, credential change,
commit or push was performed by this reviewer. The explicit live run is fresh
Lean acceptance for its thirteen supplied inputs; the arithmetic and source
decoding tests are computational evidence. No formal JSON/Python-to-Lean
refinement theorem, independent kernel implementation, certificate-finding
completeness, native Mac or installed MRS integration is claimed. The host
runtime and pinned dependency caches remain trusted.

No computational blocker remains in this reviewed scope. Aggregate formal
verification, publication scope/privacy/license inspection, and remote commit
verification are separate integration responsibilities.
