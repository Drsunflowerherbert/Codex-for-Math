# Scoped publication review

Reviewed 2026-10-13 UTC after the fresh verification passed and the independent
isolated Lean rerun completed. Only `lp-certificates/` is authorized for this
task's new publication. The user explicitly authorized finished reviewed files
in `Drsunflowerherbert/Codex-for-Math` on
`codex/lp-certificates-2026-10-13`; no new publication permission is needed.

## Baseline and preservation

The selected checkout initially used local branch `work` at tangent commit
`d00a89dd9ce6c8ef782234d28c93e69cb712c947`. Exact commands obtaining the
research baseline and creating the isolated assigned checkout were:

```sh
git ls-remote --heads origin
git fetch origin b1d6c20e2f02b484d09c5285e67d842b369f9df0
git fetch origin codex/research-2026-10-11
git worktree add -b codex/lp-certificates-2026-10-13 /workspace/lp-research b1d6c20e2f02b484d09c5285e67d842b369f9df0
```

All exited `0`. The research branch's observed remote head was exactly the
verified `b1d6c20...` baseline. The assigned branch was absent remotely.

Post-review commands:

```sh
git diff --quiet b1d6c20e2f02b484d09c5285e67d842b369f9df0 -- . ':!lp-certificates'
git -C /workspace/Codex-for-Math status --porcelain
git -C /workspace/Codex-for-Math rev-parse HEAD
git ls-remote --heads origin codex/research-2026-10-11 codex/tangent-limit codex/lp-certificates-2026-10-13
```

The scope comparison exited `0`; the original checkout was clean and remained
at `d00a89dd9ce6c8ef782234d28c93e69cb712c947`. The research and tangent remote
heads remained `b1d6c20...` and `d00a89d...`; the new assigned branch was still
absent before publication. No shared publication manifest, old research file,
or previous branch was edited. Existing dependency sources remain clean.

## Privacy, secrets, and licenses

Read-only repository metadata was obtained with HTTPS from
`https://api.github.com/repos/Drsunflowerherbert/Codex-for-Math` and projected to
the relevant fields with Python. Both subprocesses exited `0`. Observed result:

```json
{
  "full_name": "Drsunflowerherbert/Codex-for-Math",
  "private": false,
  "visibility": "public",
  "default_branch": "codex/tangent-limit",
  "license": null,
  "archived": false,
  "disabled": false
}
```

The scoped files were inspected for content and a bounded credential-pattern
scan ran before staging:

```sh
rg -n --hidden -g '!.lake/**' -g '!__pycache__/**' -g '!tests/__pycache__/**' '(-----BEGIN [A-Z ]*PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-(proj-)?[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16}|[?&](access_token|token|key)=[A-Za-z0-9_-]{16,})' .
```

No matches, `rg` exit `1` as expected. This is a targeted scan and content
review, not a universal secret-detection guarantee. Logs contain public
dependency URLs, exact compiler/source identity, and generic cloud paths; no
credential values or private mathematical input archives are included.
The staged-file inspection is repeated immediately before the commit.

The repository has no overall license reported. This task assigns none and
does not change existing licenses/notices. Proofs, checker, tests, hand examples,
and exposition are newly written. The lockfile was copied from the same
repository's pinned project and its package name changed for this project.
The published evidence helper is referenced unchanged from the existing
repository, with hash recorded by both reviewers and the fresh receipt.
No dependency tree, Lean binary, book/PDF, substantial source quotation, or
private archive is redistributed. Primary mathematical sources and their
access/copyright limits are disclosed in `notes/sources.md`.

## Validation and remaining obligations

The final fresh runner and isolated independent rerun passed. A postflight
read-only Python check compared all nine package HEADs/origins/clean tracked
status, all 29 active-input hashes, and the unchanged published-helper hash
against the receipt; all matched. Another check verified all 18 captured
output byte counts/hashes and the 3 type, 5 body, and 111-declaration replay
records. These consistency checks do not create an additional Lean pass.

The exact verification commands/results and hypotheses are retained in the
fresh receipt and three independent reviews. Python/JSON refinement,
certificate discovery/completeness, strong duality, full dependency-source
rebuild, an independent kernel implementation, and native Mac/installed MRS
integration remain explicitly unproved or unperformed.

This review precedes the publication commit. The intended commands are
`git add -- lp-certificates`, a scoped commit, and the ordinary non-force push
`git push origin HEAD:refs/heads/codex/lp-certificates-2026-10-13`, followed by
`git ls-remote` and commit/file-scope comparison. The final task response
records the actual remote commit observation. A commit cannot contain its own
content-dependent Git hash, so committed metadata does not fabricate that hash.
No PR, merge, force push, credential/account change, or usage purchase is part
of this publication.
