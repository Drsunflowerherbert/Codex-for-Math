# Follow-up publication review

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

The finished follow-up was independently reviewed and tested before publication.
It preserves first checkpoint `44329696c0a8a7fd3405d1b7b7261a14bf7ebbbd` and
publishes only `lp-certificates/` on `codex/lp-certificates-2026-10-13`.

The completed aggregate receipt, three complete checked packages, two independent
reports, code hashes, original inputs, semantic tables and generated statements
are retained. All 38 aggregate active-input hashes and all 20 captured output
byte counts/hashes were rechecked against the successful receipt; they matched.
All three packages passed byte-preserving relocation and current strict package
consistency validation. Those inspections are not additional Lean executions.
The actual fresh observations are separately identified in their receipts.

Read-only repository metadata on 2026-10-13 at approximately 03:12 UTC still
reported `private: false`, `visibility: public`, `license: null`, `archived:
false`, and `disabled: false`. No license is assigned or changed by the task.
The packages contain original task code and a copy of the unchanged existing
repository evidence helper, not dependency source trees, compiled products,
Lean binaries, private input archives, or book/PDF content. Existing attribution
and license notices remain unchanged.

A pre-staging inspection covered 633 candidate files, including 570 newly
created files: all were regular UTF-8 files and no runtime-cache directory,
binary product or symlink was included. The targeted private-key, GitHub-token,
OpenAI-key, AWS-access-key and URL-token patterns had zero matches. New files
had zero agent-routing-identifier matches. The historical first-checkpoint
reports and hashes were preserved; any normalization by integration must be a
separately described publication derivative. The added publication review and
self-excluded manifest are checked again in the staged inspection.

Scope and preservation commands from `${PROJECT_REPOSITORY}`:

```sh
git diff --quiet 44329696c0a8a7fd3405d1b7b7261a14bf7ebbbd -- . ':!lp-certificates'
git -C ${PINNED_REPOSITORY} rev-parse HEAD
git -C ${PINNED_REPOSITORY} status --porcelain
git ls-remote --heads origin codex/lp-certificates-2026-10-13 codex/research-2026-10-11 codex/tangent-limit
```

All exited `0`. The scope comparison was empty, the original checkout was clean
at `d00a89dd9ce6c8ef782234d28c93e69cb712c947`, and the observed remote heads
were the first checkpoint `44329696...`, research baseline `b1d6c20...`, and
tangent commit `d00a89d...`. No shared publication manifest or other branch
was edited. The active executable/model hashes are bound in
`FOLLOWUP-PROVENANCE.json` and the final verification receipt.

The final staged review compares every staged byte with the inspected file,
rechecks the follow-up file inventory and active-input hashes, and enforces the
assigned path prefix. Publication is an ordinary non-force fast-forward push;
the final task response supplies the observed remote commit hash. Committed
metadata does not invent its own content-dependent Git hash. No PR, merge,
account/credential/security change, usage purchase, or Library intermediate is
part of this task.

The remaining limitations are explicit: trusted parser/literal fidelity and
dependency caches, same-kernel replay, bounded incomplete finder/resource
behavior, no strong duality or completeness proof, and Linux-only observed
execution. There is no unresolved proof, test, or publication blocker within
the reviewed bounded scope.
