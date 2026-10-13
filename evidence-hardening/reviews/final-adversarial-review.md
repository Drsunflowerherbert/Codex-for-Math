# Final independent adversarial review

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

Recommendation: publish this scoped companion, with its stated trust limits.
No remaining code-acceptance or formal-interpretation blocker was found in the
reviewed production snapshot. This recommendation covers `evidence-hardening/`
only and does not upgrade the baseline toolkit, tangent hypothesis, or imported
receipts to stronger proof claims.

The current fixture source commitment is
`738cae9009e2dc05dab9ff2081372326e87402bd4ea24e3845acf115d68b0500`
(27 entries including the policy). The fixture runner SHA-256 is
`46b8ec14ef8bfa1b24fcbaf7d0c1ab24a84795f42e6d41d176033db7618555f5`.
The reused Lean helper remains byte-identical to the baseline commitment
`bb71282fcb088498a9c40b0460694f1663e8f3a145fc15469050b8ade2f390dc`.

## Findings resolved

The original independent audit reproduced contradictory saved process metadata
and incomplete provenance logs being accepted as a complete reported closure,
and Git index flags hiding changed tracked source. The companion now binds
typed process records, complete fixed commands and their output, canonical
attempt/times, artifact descriptors and hashes, source/work files, and trust
boundaries. Saved inspection remains integrity only.

Development review additionally reproduced a FIFO evidence-file hang and Git
replacement refs substituting another tree for an exact commit. Final-component
regular-file checks and nonblocking opens reject the FIFO before reading;
`--no-replace-objects` makes the byte checker compare the original pinned tree.
Both the original index-flag mutations and replacement-ref mutation reject.

The original absolute compile argv binding was corrected. Launch failures now
record null process exit/signal, rather than mistaking Node's ENOENT close code
for an executed process exit. The hidden-premise fixture now includes its section
variable, and the wrong-name fixture resolves its imported definition, so both
compile before reaching the intended closed-type/name gate.

Build evidence and formal acceptance are distinct. The build result requires
error-free successful target compilation, captured products, and unchanged
source/compiler/evidence. Complete formal acceptance additionally requires the
type/axiom/body/replay gates. Postflight runs even after a proof gate fails.

## Verification assessed

I independently ran the public Node/filesystem/Git regression suite:

```sh
node evidence-hardening/tests/regression.cjs ${TEMP_ARTIFACT}
```

Result: exit 0, 49/49 tests, zero Lean passes. I also independently tested 25
malformed complete-receipt metadata/log variants; all rejected. These were
explicitly synthetic saved-receipt tests, with no Lean execution.

The independent verification agent confirmed production snapshot04 results:

| Evidence | Result | Interpretation |
| --- | --- | --- |
| Actual pinned Lean fixed corpus | 10/10 expected outcomes | One positive fixed fixture; nine negatives reject at their intended gates |
| Public Node/filesystem/Git regression | 49/49 | Process, parsing, I/O and source-identity regression |
| Independent v1 receipt mutations | 57/57 | Saved integrity rejection/compatibility tests |
| Independent fixed-fixture receipt imports | 45/45 | Current-policy integrity and malformed/stale receipt rejection |
| Actual runtime/source-policy tests | 5/5 | Timeout, observed AbortSignal, preabort, source-pin and stale-policy rejection |
| Actual nine pinned package trees | 9/9 | Tracked source bytes match unreplaced trees; caches remain separate |

The actual Lean corpus report's before/after source digest equals the current
commitment above. Hidden premise, statement drift, specialization, wrong name,
`sorry` and custom axiom reject at the whole-type/axiom gate. Predicate
substitution and changed imported bound reject at independent definition-body
matching. The kernel-bypass fixture passes compilation/type/axiom phases but
fails local same-kernel replay.

I independently inspected the actual baseline valid/general/tangent receipts:
the first two accepted 172-artifact reported closures and tangent accepted 208.
All returned no imported Lean pass or freshness. I independently inspected the
verifier's final04 positive fixture receipt, which returned integrity only, and
the earlier snapshot02 receipt, which rejected under the final policy:

```sh
node evidence-hardening/fixture-gate.cjs inspect ${VERIFICATION_WORK}/final-04/lean-corpus-1F4Yjr/valid
# exit 0; leanPass false; locallyObservedLeanPass false; freshness not_established
node evidence-hardening/fixture-gate.cjs inspect ${VERIFICATION_WORK}/fixture-corpus-02/valid
# exit 2; stale fixture source commitment
node evidence-hardening/inspect-v1.cjs ${TEMP_ARTIFACT}
# exit 2 promptly; nonregular or oversized path: receipt.json
node evidence-hardening/git-source.cjs ${TEMP_ARTIFACT} 8d78fe9ff7fea3b9da1f73228ed839a4e0688d1e
# exit 2; tracked source bytes differ from git tree: Dependency.lean
```

I reviewed the current README and migration notes. Their distinction between
builds, fresh formal fixture observation, conditional hypotheses, imported
integrity and trusted caches is appropriate. Exact `.git` origin spelling and
empty stderr are documented conservative migration requirements. Markdown
symlinks are checked as target bytes without following them; Lean/source
symlinks remain unsupported.

## Retained limits and publication obligations

The type/body harnesses cover fixed monomorphic declarations. The positive
identity keeps its premise `h : n = 2`; the conditional theorem has the checked
predicate body `False` and proves `False -> False`, not `False`. Tangent's
`PiDiophantine` premise remains unproved.

Core OLean caches and the host runtime remain trusted. Baseline tangent runs
separately trust pinned mathlib caches. Source byte checking does not rebuild
dependencies, authenticate an origin or discover arbitrary imports. Replay uses
the same Lean kernel and imported baseline, not an independent kernel.
No hostile Lean sandbox, native Mac/MRS integration or new mathematical novelty
is asserted. A coherent fabricated historical receipt can satisfy unsigned byte
consistency; saved inspection still grants no pass, freshness or authenticated
history. Report text such as `observedType` is not independently elaborated by
the saved inspector.

The verification agent owns the actual Lean execution records; my own reported
commands above are inspections and Node/filesystem/Git checks. I inspected the
completed scoped `evidence/independent-fixture-receipts.json` (45/45) and
`evidence/independent-runtime.json` (5/5); both report no failed cases and
`sourceUnchanged: true`. The runtime cases cover actual pinned Lean timeout,
observed Lean AbortSignal, preabort without a process, source-pin rejection
before an attempt, and stale-receipt rejection under a new reviewed policy.
The owning task must retain exact final-byte provenance, inspect publication
privacy/secrets/licensing, publish only the assigned scoped directory/branch,
and verify the remote commit. This review does not perform those actions.

This final review supersedes the pending code-review items in
`adversarial-audit.md`. Baseline files and shared publication manifests were
preserved by this reviewer.
