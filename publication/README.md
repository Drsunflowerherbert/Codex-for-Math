# Publication record

This publication is based on exact commit
`d00a89dd9ce6c8ef782234d28c93e69cb712c947`, on branch
`codex/research-2026-10-11`. The original tangent files are unchanged.

[INPUT-ARCHIVES.json](INPUT-ARCHIVES.json) records the five supplied archive
fingerprints. All five archives were retrieved and their SHA256 values verified
in this publication environment before extraction. Entry paths and file types
were inspected first; no traversal entries or symlinks were present. No archive
script was executed automatically.

[SOURCE-MAP.json](SOURCE-MAP.json) records each candidate's source hash and its
publication disposition. Exclusion records give filenames and reasons without
private contents. Modified files have both original and published hashes.
[FILES.json](FILES.json) binds the current publication files, excluding itself
to avoid self-reference. Run `python3 publication/verify.py` to check it.
Integrity checks establish byte consistency, not mathematical truth.

Historical supplied manifests, review hashes, commands, verdicts, and build
receipts describe the original supplied snapshots. They have not been rewritten
to make privacy edits appear independently reviewed. Their hashes can reference
omitted or sanitized files. Root archive manifests are explicitly named
`*.supplied.*`; nested historical records retain stable names and are subject
to this same interpretation. Use the publication manifest for the current tree.
No review verdict is upgraded by a new hash.

Radial v2's supplied successful receipt is preserved under
`radial-contact/evidence/supplied-v2/`; its current `evidence/validation.json`
records a separate publication build. Egyptian supplied receipts remain under
`egyptian-exact/evidence/`; fresh publication commands and logs are under
[evidence/](evidence/). Source and dependency pins remain byte-identical.

The Lean implementations' starter-input failures are historical provenance
limits. Both independently implemented supplied mathematical specifications.
Later successful archive retrieval does not retroactively certify that the
formalizers inspected the starter or that every ordinary record is equivalent
to a formal theorem.

The public set excludes launch instructions, private identifiers and transfer
metadata, cache/download diagnostics, the nested binary checkpoint, and the
original private packaging helper. No credentials, personal emails, screenshots,
account details, installed dependencies, or build binaries were found in the
retained publication set. Independent automated publication/privacy and
mathematical-status reviews inspected all initial candidates; their scope and
the final review are recorded in [REVIEW.md](REVIEW.md).

No overall license has been invented for the new research or Lean implementations.
Retained third-party text is separately attributed and accompanied by the
upstream license; see [THIRD-PARTY.md](../THIRD-PARTY.md).
