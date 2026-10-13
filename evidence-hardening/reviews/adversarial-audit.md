# Independent adversarial audit of the published evidence toolkit

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

Audit baseline: `b1d6c20e2f02b484d09c5285e67d842b369f9df0` in
`Drsunflowerherbert/Codex-for-Math`. Audit performed on Linux with Node
`v24.19.0` and Python 3; baseline files were not edited. This is a source/process
evidence audit, not independent mathematical proof acceptance.

Final disposition: the reproduced acceptance/I/O/Git findings and fixture/reporting
construction issues were corrected and rechecked. See
[final-adversarial-review.md](final-adversarial-review.md) for the tested final
source commitment, completed evidence counts, recommendation and retained limits.
Its final status supersedes the development-stage pending obligations below.

## Existing protections and limits

I read `math-evidence/README.md`, `SCHEMA.md`, `LEAN-RECEIPTS.md`,
`VERIFICATION.md`, `MRS-ADAPTER.md`, `core.cjs`, `live.cjs`, `process.cjs`, the
Lean helper/expected harnesses, and published adversarial-test sources.
No `AGENTS.md` or repository `.agents/skills` was present at this baseline.

The baseline correctly distinguishes generic schema/hash consistency, ordinary
review, finite experiments, historical reports, fresh local Lean observation,
and imported receipt inspection. Imported receipts always return
`leanPass: false` and `locallyObservedLeanPass: false`. Whole-type matching
includes implicit/forall binders. Tangent definition-body matching protects
against changing `PiDiophantine` into an easier proposition; it does not prove
that premise. Local replay uses the same Lean kernel against imported trusted
dependencies, rather than an independent verifier. Native Mac/MRS integration
and hostile-workspace sandboxing are explicitly unvalidated.

## Reproduced findings

### A. Receipt structure admits malformed process and provenance metadata

`live.cjs:118` validates exact top-level field sets and some phase fields, but
does not type-check phase timestamps/duration/output limits/environment/error,
exit code/signal/PID/group, package objects, or most trust-boundary values.

Actual Node calls to both `validateReceiptStructure` and `inspectReceipt`
accepted a temporary receipt containing:

- an attempt identifier consisting of 36 hyphens;
- phase `started`/`finished` equal to `not a date`, duration `-999`, and output
  limit `-4`;
- string `environment`, numeric `error`, string exit code `zero`, numeric signal
  `123`, PID `-1`, and no process group;
- an arbitrary package object and boundary claims such as `authenticated`,
  `proved_without_evidence`, and `rebuilt_and_proved`.

The two empty log files had valid byte hashes. Inspection returned `ok: true`
with `integrityStatus: failed_or_incomplete_attempt`; it correctly returned no
Lean pass. Thus this is a schema/internal-consistency weakness, not a bypass
of the imported-receipt no-pass rule. Successful receipt inspection also lacks
binding of compiler/package/dependency stdout, argv and cwd to fixed expected
commands, so similar inconsistencies can affect a reported complete closure.

Reproduction artifact: `${TEMP_ARTIFACT}/receipt.json`.
Actual command result: Node exited 0. No Lean was run for this reproduction.

A second, stronger reproduction built a clearly labeled synthetic complete
closure with all 172 required source/work/product/log artifacts. All fixed source
and build-input bindings were preserved, but every phase had empty argv and
executable, malformed dates/environment, negative duration/output limit,
`error: 900` despite `success: true`, and PID `-1`. Compiler-version, compiler-
commit, package and dependency-search logs were empty; `packages` was empty;
products contained the explicit text `synthetic product; never Lean accepted`.
The valid arithmetic theorem's marker used the arbitrary `observedType: False`.
Baseline inspection nevertheless returned `ok: true` and
`integrityStatus: complete_reported_execution_closure`, with both pass fields
correctly false. No Lean process was executed.

This synthetic adversarial artifact is at
`${TEMP_ARTIFACT}/receipt.json`. Its purpose is to test
rejection, not to claim mathematical or process evidence. The problem is
contradictory internal process/provenance metadata being called a complete
reported closure; fabrication alone cannot be excluded by unsigned hashes.

Bounded fix: a companion with strict typed schema validation, exact trust enums,
UUID/ISO timestamp rules, ordered phase intervals, consistent termination/error
states, bounded output counts, exact descriptor keys, attempt-marker identity,
and fixed phase command/log bindings. Continue returning no pass for all saved
receipts, including internally coherent fabricated historical closures.

### B. Git diff can call changed tracked dependency source clean

`live.cjs:174` obtains package HEAD/origin and runs:

```sh
git -c core.fsmonitor=false diff --no-ext-diff --no-textconv --exit-code HEAD --
```

In a disposable git repository, I committed
`def audited : Nat := 1`, then changed the working bytes to
`def audited : Nat := 2` after separately enabling each of:

```sh
git update-index --assume-unchanged Dependency.lean
git update-index --skip-worktree Dependency.lean
```

For both flags the exact baseline preflight command exited 0 with no diff. The
committed SHA-256 was
`4e757552844724c28da17afc133340e3fd34da33284346b0b11cc74e23008a82`;
the actual working SHA-256 was
`f226505852f4dc72ba4ad390390b9bbd2d5610f118f761d294ff443f4b93ed7e`.

Reproduction repository: `${TEMP_ARTIFACT}`. Neither baseline
package source nor its index was changed. This challenges the stated clean
tracked-source preflight; it does not establish compromised Lean acceptance,
because the baseline separately trusts dependency OLean caches and does not
rebuild dependency proof bodies.

Bounded fix: compare independently enumerated required transitive source bytes
with fixed commitments (or git tree blobs) before and after the run. Do not use
git diff as the only byte-identity check. Explicitly retain external cache trust
when caches are not fully pinned/rebuilt. A fixed small fixture closure is a
useful tested scope; do not claim complete arbitrary-package import discovery.

### C. Generic exchange permits omitted binders and namespace substitution

An actual `core.cjs` generic `validate` call accepted source:

```lean
namespace Hidden
variable (h : False)
theorem claimed : False := h
end Hidden
```

The corresponding record had `name: Claimed.claimed`, statement excerpt
`theorem claimed : False`, empty assumptions and empty dependencies.
The source namespace differs, and a section variable used by the proof is absent
from the excerpt. Validation exited 0 while reporting `statementBinding:
textual_excerpt_only`, `assumptionCompleteness: not_established`,
`leanTypeMatching: not_performed` and zero Lean passes.

This behavior is expressly within the published heuristic boundary, not a false
baseline proof claim. A stronger acceptance corpus should keep it as a negative
case for independently specified declaration identity and closed whole types.
No Lean compilation was performed in this audit reproduction.

The exact textual probe above was not claimed to elaborate. In pinned Lean, a
section variable omitted from a theorem's type must be included explicitly to
exercise the intended hidden-premise case; the corrected actual fixture uses
`include hidden`. Thus this probe establishes the disclosed textual-only
validator boundary, including acceptance of incompletely elaborable source,
while the separate pinned fixture establishes closed-type rejection of a real
extra hypothesis.

## Recommended bounded regression corpus

Use fixed sources and expected harnesses rather than executing imported plans.
Include these actual pinned Lean fixture pairs where tooling is available:

1. A valid closed elementary theorem: compile, whole-type/axiom audit and
   same-kernel replay succeed.
2. A legitimate theorem `False -> False`: accepted with an explicitly retained
   hypothesis; it is not evidence for `False`.
3. A section-variable/implicit binder hidden by an excerpt: compilation succeeds,
   but comparison with the incorrectly unconditional expected type fails.
4. An expected theorem specialized from a general statement: compilation succeeds,
   but closed whole-type matching fails.
5. An unchanged theorem type using a substituted predicate definition: compile
   and potentially named-type matching succeed, independent definition-body
   matching fails. Expected definitions must not simply re-import the candidate
   definition as their purported reference.
6. A changed imported local dependency: committed transitive source identity
   changes, so source preflight fails before a fresh acceptance claim.
7. `sorry`, a custom axiom, and kernel-check bypass: compilation alone is
   insufficient; axiom or replay gates reject as appropriate.
8. Saved receipt with changed source/log/product, stale fixture commitment,
   missing phase, duplicate marker, malformed UTF-8/JSON or exit evidence,
   contradictory success, unknown trust enum, malformed times, or compiler/
   package argv/log disagreement: strict saved inspection rejects.
9. A valid saved receipt inspection: integrity only, no freshness or new Lean
   pass. A coherent forged historical receipt likewise cannot become a fresh
   observation.

## Companion-review obligations

Pin the companion runner, original helper, fixture sources, reference types and
reference bodies independently. Reject a change to this transitive closure,
including changes to a source that the top-level theorem text does not mention.
Use strict JSON before parsing any receipt. Check every compile JSON stream for
errors and bound both output channels. Reproduce exact pinned compiler identity
and release bytes before any fresh fixture execution. Do not run argv contained
in a saved receipt.

A provenance report should separate exact byte identity, process observation,
compiler version/pins, local source closure, imported cache trust, theorems'
explicit hypotheses, axiom closure, and same-kernel replay. A timestamp is a
reported observation, not authenticated history. A narrow fixed-fixture runner
does not supply arbitrary Lean sandboxing, arbitrary import-closure discovery,
an independent kernel, or native MRS integration.

Before publication, record exact commands/results, hashes, retained limitations,
and any unperformed pinned Lean tests. Preserve baseline directories and shared
publication manifests.

## Initial companion review

I independently reviewed the initial `inspect-v1.cjs`, `io.cjs`,
`process-contract.cjs`, `capture.cjs`, `git-source.cjs`, pinned baseline metadata,
and small Lean fixture sources. Review outcomes below describe the development
snapshot; the final publication must identify its tested bytes.

- All 92 toolkit commitments in `baseline.json` matched the exact baseline;
  its catalog contains 26 source/evidence files and nine locked packages.
- The original malformed complete receipt is rejected by the strict inspector.
- A deliberately synthetic but structurally coherent complete receipt is accepted
  only as integrity with no freshness, no imported formal proof acceptance and no
  Lean pass. This checks the integrity boundary, not historical authenticity.
- Twenty-five independent malformed metadata/log mutations were all rejected.
  The report is `${TEMP_ARTIFACT}/report.json`, labeled
  `synthetic_saved_receipt_shapes_only_no_Lean_executed`.
- The initial compile argv contract used a relative final source path, while the
  original runner records an absolute path. This compatibility defect was
  reported and corrected; the coherent shape subsequently reaches every gate.
- A FIFO named `receipt.json` hangs before the initial reader checks regular-file
  type. `${TEMP_ARTIFACT}` required the independent subprocess
  timeout after 1.003 seconds. The bounded fix is final-component regular-file
  validation before open plus nonblocking open followed by the existing fstat
  checks. Schema/expected artifact coverage should precede expensive artifact I/O.
- Git replacement refs bypass the initial `git-source.cjs` tree check. In
  `${TEMP_ARTIFACT}`, HEAD/requested original commit
  `8d78fe9ff7fea3b9da1f73228ed839a4e0688d1e` contains `def audited : Nat := 1`.
  Replacing it with `b3bbb37a05bafe029597f0413468b1293bf617e3` and leaving working
  bytes `def audited : Nat := 2` causes `ls-tree` to enumerate the replacement
  tree. The initial companion returned `ok: true` for the original revision and
  changed working SHA. Every provenance Git invocation must use
  `--no-replace-objects` (or an equivalently enforced clean environment), and the
  replacement-ref fixture must reject after the fix.

These probe results do not claim any pinned Lean execution. Actual positive and
negative fixture execution, final-byte verification, and publication remain
separate obligations of the owning task.

Subsequent review rechecks confirmed the reported reader/Git fixes:

```sh
node evidence-hardening/inspect-v1.cjs ${TEMP_ARTIFACT}
# exit 2: nonregular or oversized path: receipt.json; no hang
node evidence-hardening/git-source.cjs ${TEMP_ARTIFACT} 8d78fe9ff7fea3b9da1f73228ed839a4e0688d1e
# exit 2: tracked source bytes differ from git tree: Dependency.lean
```

The new Git checker likewise rejects the original skip-worktree mutation.
An actual `capture.cjs` launch failure initially recorded Node's ENOENT close
code `-2`, which is not an executed process exit and contradicted the strict
contract. The owning task normalized launch-failure exit/signal to null while
retaining its error report.

I independently ran the current strict inspector on the verification agent's
actual pinned Lean receipts for valid and general fixtures (172 artifacts each)
and the tangent project (208 artifacts). All three exited 0 for integrity-only
inspection, with `leanPass: false`, `locallyObservedLeanPass: false`, freshness
and receipt authenticity not established, trusted imported dependency caches,
and no independent kernel claim. The tangent hypothesis remains unproved.
The new fixed-fixture valid receipt from the verifier's snapshot02 also inspected
successfully as integrity only. I did not independently launch Lean in these
inspection commands; the verifier owns the actual execution records.

Formal fixture review confirms that an unchanged named predicate type alone
would be insufficient, and that the separate reference body `False` is the
necessary substitution guard. The imported `bound` affects the `answer` reference
body, exercising transitive definition changes. Replay uses the original reviewed
helper against `[Init, EvidenceHarness]` with explicit local targets, and remains
the same kernel. Negative hidden-premise and wrong-namespace fixtures must compile
successfully before reaching their intended audit failures; their construction
issues were reported to the owner for correction. Build observation must be
reported separately from full formal gate acceptance.
