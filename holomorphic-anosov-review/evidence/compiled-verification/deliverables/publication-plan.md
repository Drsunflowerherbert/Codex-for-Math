# Publication selection and normalization plan

Prepared by independent inspection of the compiled-verification records on
16 October 2026. At preparation time the final `selected-targets-replay-02.json`
record did not yet exist. No staging copy was executed by this subtask.

`scripts/stage_public_evidence.py` contains an exact file allowlist. Its list
is the selection authority; no directory is copied recursively and newly
created files are excluded unless explicitly added. The selected files are
audit-owned scripts/harnesses, explanatory notes, official provenance metadata,
hash manifests and complete successful/failed/stopped-attempt text logs. It
excludes the toolchain, build/dependency trees, caches, downloads, generated
proof exports, source PDFs/OCR/articles, internal handoff notes, publication
remote-head data and legacy standalone comparator/Landrun metadata.

Before running the script, finalize the direct replay's terminal JSON record
and update `deliverables/verification-method.md` to the recorded result. The
script refuses to stage without the final step's integer exit code/duration,
or while the method's opening still reports that replay pending. Exit 0,
rejection, deliberate termination, resource stop and incomplete checks must
retain their distinct meanings. The configured comparator remains blocked
by its required Bubblewrap UID-map setup irrespective of the direct replay.

After that prerequisite, validate without copying:

```sh
python3 scripts/stage_public_evidence.py --dry-run
```

Then the verification owner may run the script without `--dry-run` to stage
into its default review-payload evidence destination. It refuses to write
over a nonempty destination. No network access, tool installation, repository
proof execution or public push is performed by this script.

Normalization replaces the private verification root by `$VERIFY_ROOT`, the
source-audit extension root by `$SOURCE_AUDIT`, and enclosing review$WORKSPACE_ROOT
roots by `$REVIEW_ROOT` / `$WORKSPACE_ROOT`. Additional mappings require an
explicit `--private-root PATH=$UPPER_CASE` argument. Unmapped private paths,
attachment/conversation identifiers, recognizable tokens/keys or URL
credentials cause refusal; this pattern check complements human inspection
and is not a universal guarantee against all secret formats.

Original raw log SHA-256 fields are verified before any copy. Public JSON
status copies rename them to `original_log_sha256` or
`original_stderr_sha256`, add corresponding `published_normalized_*` fields,
and identify their related logs explicitly. The generated manifest records
each original file's bytes/hash, each distributed copy's bytes/hash, prefix
replacement counts, and any JSON hash-field relabelling. `SHA256SUMS` hashes
the files actually distributed, including the manifest. No original hash is
presented as authenticating normalized bytes. Artifact/source/export hashes
remain identities of their original, omitted artifacts.

Some inspection notes state that their particular author/subtask did not run
Lean. Those are scoped historical facts. Public readers should use the final
method document and terminal logs for actual execution status. The generated
`PUBLICATION.md` explains this distinction and labels the replay plan as a
preparatory plan. `checks/README.md` contains historical absolute command
paths; normalization replaces their prefix in the public copy. All included
scripts deriving a verification root use `Path(__file__)`; the streaming
presence script instead takes explicit input/output arguments.

The inspected method document correctly distinguishes build success, exact
type/definition checks, a global axiom inventory, direct same-kernel replay,
and the blocked comparator. A clean inventory leaves the explicit
`HomotopyTorusRigidity` premise of A/1.1/1.3 intact. Theorem 1.2 has no such
premise. The presence scan is solely evidence that all four named theorem
declarations occur in the finalized export, not a kernel/axiom check. Source
and artifact manifests are hash inventories, not copies of upstream sources
or proofs. No critical overclaim was identified in these inspected records
while their direct replay was still marked pending.

After staging, inspect the destination for accidental extra files/symlinks,
verify its checksums, review the final outcome wording, and regenerate the
outer repository's own manifest before any separately authorized publication.
The large proof export is deliberately absent; its exact original byte count
and SHA-256 remain in the evidence. The user-supplied paper remains unchanged
and is not part of the publication payload.
