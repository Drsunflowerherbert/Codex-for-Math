# First-edition recovery record

Prepared for publication on 2026-10-13 UTC. The completed bounded edition has
236 detailed metadata entries (224 retrieved-source, 12 provisional indexed
Jarník entries), three accepted independent ordinary-proof reviews, separate
hints/answers, and explicit missing coverage.

Worktree: `/workspace/contest-library-worktree`.
Branch: `codex/contest-library-2026-10-13`.
Verified baseline: `e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f`.
Only `contest-library/` is changed; the original worktree and branches remain intact.

Catalog reviews and proof reviews are in `reviews/`. The source hash check can
be rerun with `python contest-library/scripts/validate.py --private-sources`
while private copies still exist under `/tmp/contest-library-research/`.
A normal public clone can run the same command without `--private-sources`.
Regenerate CSV/subject/coverage views with `scripts/build_index.py` only when
source metadata intentionally changes; refresh relevant review evidence after
substantive changes. Final-byte proof/hint hashes are in `authored-solutions.json`.

Source inspection rejected an initial Yau 2018 open-ball observation after
rendering exposed a closed-ball overbar lost in extraction. Independent review
also added the source-qualified Schweitzer 2023/8 wording warning. These fixes
are incorporated in the published candidate, rather than left as pending work.

No current/restricted 2026 problem content or submissions were read, solved or
published. The six 2026 Yau archive entries have central-directory filename/size
metadata only. Full third-party PDFs/ZIPs and extracted text are private research
copies outside Git. Jarník full-PDF access remains blocked by HTTP 503.

Publication is a normal push to the requested branch only. Remote head and
retrieved commit bytes are to be verified after the push; the final task response
reports that result and the commit ID. This record does not invent an in-file
self-referential final commit hash or assert a formal mathematical certificate.
