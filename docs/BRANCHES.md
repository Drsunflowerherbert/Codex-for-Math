# Branch roles and rename map

[Repository home](../README.md) · [Project catalog](CATALOG.md) · [Migration](MIGRATION.md)

The repository default is now **`main`**, a small directory branch. The 14
research branches use stable topic names. `research/` identifies recommended
project branches; `archive/` identifies earlier source checkpoints. Paused,
conditional and ordinary-proof status remains explicit in the catalog.

## Complete old-to-new mapping

The final column records each retained head immediately before this rename
round. Renames preserve those commits exactly; later topic-root edits change
navigation only. Original research editions remain pinned in the catalog.

| Current branch | Former branch | Purpose and status | Retained pre-rename head |
| --- | --- | --- | --- |
| [`research/certified-roots`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/certified-roots) | `codex/certified-roots-2026-10-15` | Ordinary contraction proof and exact rational checker; no Lean claim. | [94be4cea79](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/94be4cea7925cdd2c027a40b968c7380d3cf6b27/README.md) |
| [`research/contest-library`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/contest-library) | `codex/contest-library-2026-10-13` | Bounded practice library; provisional source coverage remains identified. | [ce6041879a](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/ce6041879a80c230da5f8d98a25154ded5f1b852/README.md) |
| [`research/critical-points`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/critical-points) | `codex/critical-points-2026-10-15` | Ordinary proof and exact rank-one local classifier; no Lean claim. | [a35e088c65](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/a35e088c655fa5b5877124c7dcc4c95f7dc1f94f/README.md) |
| [`archive/evidence-hardening-source`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/archive/evidence-hardening-source) | `codex/evidence-hardening-2026-10-13` | Earlier hardening companion source checkpoint; prefer integrated copy. | [0a5c28b3e9](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/0a5c28b3e9cf8c48911ff363a5e491763a84c196/README.md) |
| [`research/hadamard-study`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/hadamard-study) | `codex/hadamard-study-2026-10-15` | Three cumulative bounded rounds; explicitly paused after round 3. | [e444609e39](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e444609e39ccd6c6715ea804cf76fd2fb2fb0ddf/README.md) |
| [`research/holomorphic-anosov-review`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/holomorphic-anosov-review) | `codex/holomorphic-anosov-review-2026-10-16` | Expanded paper review; explicit rigidity premise and no comparator verdict. | [54633c5947](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/54633c594792df75a09f2f6d69a8de31d4275a7b/README.md) |
| [`research/integral-examples`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/integral-examples) | `codex/integral-examples-2026-10-15` | 16 worked analysis examples; reviewed ordinary educational material. | [e82f957239](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e82f957239980cb78034c95664bbc6daf47c7775/README.md) |
| [`archive/lp-certificates-source`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/archive/lp-certificates-source) | `codex/lp-certificates-2026-10-13` | Earlier LP toolkit; later executable-binding hardening is in the integrated edition. | [208af16989](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/208af169896a30552bd3962cd317d31ebcb6dfa8/README.md) |
| [`research/lp-paper`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/lp-paper) | `codex/lp-paper-2026-10-13` | Reviewed standalone LP exposition, not a new solver. | [53db69cbda](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/53db69cbdad205b18d1054536018bcd182654395/README.md) |
| [`archive/lp-sparse-discovery-source`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/archive/lp-sparse-discovery-source) | `codex/lp-sparse-discovery-2026-10-13` | Original ordinary support study and fixture experiments; integrated copy available. | [ef3ad84022](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/ef3ad840222ce27b1d0112642fa7b5405041144b/README.md) |
| [`research/integrated`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/integrated) | `codex/research-2026-10-11` | Shared integrated collection; recommended LP/transport/evidence publication copies. | [51fb9a3e2f](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/51fb9a3e2facd03d8c1116510723b65443009985/README.md) |
| [`research/research-map`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/research-map) | `codex/research-map-2026-10-13` | Source-pinned reference/metadata map and partial scope audit. | [aef3c10ae3](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/aef3c10ae3c33a805b0eceb1a16e598eb7eb8744/README.md) |
| [`research/tangent-limit`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/tangent-limit) | `codex/tangent-limit` | Original conditional cubic tangent project; the sharp extension is separate. | [6b660e717c](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/6b660e717c4afca52b173cfe040037f3e695910c/README.md) |
| [`archive/transport-sharpness-source`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/archive/transport-sharpness-source) | `codex/transport-sharpness-2026-10-13` | Scoped transport source checkpoint; prefer integrated publication copy. | [766be27fa6](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/766be27fa6bb76772aaa0c6b59d7c73fcd4d2bd3/README.md) |

Machine-readable mapping: [branch-map.json](branch-map.json).

## Directory history

`main` is a single-parent descendant of the previous default head
`6b660e717c4afca52b173cfe040037f3e695910c`. It is connected to the existing history, not an orphan branch,
and it does not merge unrelated research branches. Its current tree contains
only `README.md` and four navigation files in `docs/`.

Relative to its parent, the new main tree no longer includes `tangent-limit/`.
That complete project tree stays byte-identical on `research/tangent-limit`,
and its original commits remain in main's ancestry. No research is removed
from a topic branch or erased from Git history. The former tangent branch's
catalog paths are retained as compatibility pointers to main.

## Ancestry and shared files

The original tangent commit is `d00a89dd9ce6c8ef782234d28c93e69cb712c947`. It is the common ancestor of every
research branch. The holomorphic review forks from it directly and inherits
`tangent-limit/` unchanged.

The 11 October publication sequence reaches baseline `b1d6c20e2f02b484d09c5285e67d842b369f9df0`. Four sibling
continuations add evidence hardening, transport, LP certificates and sparse LP
discovery. The integration branch later incorporates reviewed publication
copies of those directories; these are content integrations rather than merges
of the sibling tips. The LP integration then adds executable-binding hardening
and confirmation. Thus a sibling tip is not necessarily the recommended edition
merely because it has the topic's name.

The integrated research head is `e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f`. Seven later sibling branches add only
their named project directory: `lp-paper/`, `integral-examples/`,
`critical-points/`, `certified-roots/`, `hadamard-study/`, `contest-library/` and
`research-map/`. At the audited research heads, all pre-existing directories
are byte-identical to the integrated baseline. Those inherited copies should
be counted once and read at the catalog's recommended links.

The Hadamard branch has three cumulative rounds, not three separate projects.
Read `round3/README.md` for its latest paused checkpoint. The holomorphic branch's
expanded review and compiled evidence supersede its initial limited review.
The research starter's affine/Egyptian snapshots are historical; the research
README points to the corrected ordinary studies. Original tangent and extended
sharp-tangent scope remain separately accessible.

Branch dates described in older project prose are provenance, not the current
naming convention. Use the mapping above to resolve an old branch name. Source
files, substantive project documentation, evidence, PDFs, datasets, manifests
and toolchain pins remain untouched on topic branches.

## Evidence and snapshot integrity

The organization update does not rerun research scripts, experiments or Lean.
Whole-tree manifests apply to their own recorded source/baseline, which can
predate a branch's later added directory. Root navigation edits add a documented
difference; no historical manifest is rewritten to imply fresh verification.
Use the catalog's exact research links and project notices for original inputs
and scope. Inherited directories should be counted once rather than as new
results on every branch.

The preflight found no pull requests, protected branches, rulesets or repository
workflows. GitHub's supported branch-rename API preserves browser redirects.
Raw URLs and local tracking need the updates in [MIGRATION.md](MIGRATION.md).
