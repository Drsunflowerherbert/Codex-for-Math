# Source audit — 2026-10-13

This map uses the official [OpenAI/math repository](https://github.com/openai/math), whose URL was already recorded in the integrated research inventory. The working baseline is [Codex-for-Math commit e4f337c3](https://github.com/Drsunflowerherbert/Codex-for-Math/commit/e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f). This audit checks sources, versions and counting units; it does not verify mathematical proofs.

## Current and historical pins

The freshly checked official `HEAD` and `main` both resolve to **[1581d4cbdd69a0faf34b2089614fe2a814316a6a](https://github.com/openai/math/commit/1581d4cbdd69a0faf34b2089614fe2a814316a6a)**, committed **2026-10-12 21:55:24 UTC**. Its tree is `45074722c918576d65b4c8be9686c76f508ba696`. Verification used `git ls-remote --symref`, the pinned GitHub commit API, and pinned raw-file retrieval. See [source-audit.json](source-audit.json) for hashes, counts and retrieval details.

The saved inventory was pinned to [fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/commit/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb), committed 2026-10-08 05:20:00 UTC. The [two-commit comparison](https://github.com/openai/math/compare/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb...1581d4cbdd69a0faf34b2089614fe2a814316a6a) changes only `.github/workflows/lock-prs.yml`. Fresh current and historical raw copies of `README.md`, `CONTENTS.md`, `history.md` and `lean/formalization.yaml` are byte-identical. No mathematical corpus change was found between these pins.

[upstream-inventory.json](upstream-inventory.json) therefore preserves the earlier family/manuscript relationships and descriptions, with current source links repinned and historical provenance retained. An independent parse of current `CONTENTS.md` found **719 manuscript PDF links and 372 unique family headings**. Their path and family orders exactly match the saved inventory. The **17 discipline groups** carry forward from that inventory. There are also **3 withdrawn manuscript records**, giving 722 active-plus-withdrawn records; neither manuscript nor family counts are counts of solved problems.

## Primary entry points and evidence limits

| Source | What it supports | What it does not establish |
| --- | --- | --- |
| [Current manuscript map](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/CONTENTS.md) | Author descriptions, active manuscript links and family membership | Proof correctness, novelty or acceptance |
| [Repository README](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/README.md) | Collection scope and warning that verification stages differ | Corpus-wide verification |
| [History](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/history.md) | Documented withdrawals, repairs and citation updates | Exhaustive issue detection or successful repair validation |
| [Lean manifest](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/formalization.yaml) | Listed sources, exact declaration names and comparator configurations | A reproduced kernel check or informal/formal correspondence |
| [Official announcement](https://openai.com/index/sharing-ai-progress-in-mathematics/) | Release context | Acceptance of every manuscript claim |
| [Scoped local research](../research/README.md) and individual project evidence | Precisely scoped supporting results and their recorded checks | Proof of the original source's headline claim |

Fresh manifest parsing confirmed **173 paper-source entries, 200 main-result declarations and 189 distinct comparator configurations**; 242 families have scope links in the inventory. The manifest's own `review.status` is `unchecked`, and its scope is `Partial progress.` The claimed **300/719 top-line formalizations** have not been independently reconstructed. One of the 173 paper paths still names the September 23 Taming manuscript while the active map names October 6; 172 paths match active PDFs. Listing, kernel checking, mathematical validation and established acceptance remain separate evidence stages.

## Withdrawals and repairs

All **30 relevant README files** were freshly retrieved: 27 revision notes and 3 withdrawal notices. The 27 revision notes match the saved notes apart from terminal-newline normalization. These documents preserve previous-edition links; the map must preserve those relations rather than treating each edition as a separate solved problem.

The three withdrawn **family032** manuscripts are:

- [Algebraicity of Weil classes on split abelian eightfolds](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026/README.md): a sign error prevents the stabilization-trace cancellation needed for the subsequent construction.
- [Algebraicity of Kuga–Satake Correspondences for K3 Surfaces](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Algebraicity-of-Kuga-Satake-Correspondences-for-K3-Surfaces-October-3-2026/README.md): depends on an adaptation of that flawed construction.
- [The rational Hodge conjecture for products of K3 surfaces](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-rational-Hodge-conjecture-for-products-of-K3-surfaces-October-4-2026/README.md): depends on an adaptation of that flawed construction.

The notices date withdrawal October 6; the history groups it under October 7; the public merge occurred October 8. These are distinct dates. Withdrawal concerns the proofs and does **not** establish that the statements are false. Family032 still contains five active manuscripts, including restricted and conditional claims; none inherits validity merely from remaining in the catalog.

The history records **14 other revisions** involving repairs, statements, hypotheses, dependencies or one obsolete citation, plus **13 citation-only updates**. They include four Lipschitz-height/Ashkin–Teller papers; six Kähler MMP/abundance papers; Taming and hypersymplectic deformation; Box Transport; and the low-Selmer-corank BSD paper. Taming's cone equality was restricted and a strict-inclusion example added. Conditional Kähler results explicitly retain outstanding input hypotheses. [source-audit.json](source-audit.json) contains all 27 version notes and current/previous paths. These are documented histories, not a claim that only three problems or fourteen repair needs exist, and this audit does not certify the repaired proofs.

## Hash normalization and reuse

The saved source manifest hashes for the four corpus files each represent the raw upstream bytes **plus one terminal newline**. Fresh hashes differ for that exact reason; adding one newline reproduces all four recorded hashes. The audit stores both forms. It claims byte identity between fresh current and historical raw files, not between raw bytes and the normalized saved snapshot.

## License and modification notice

OpenAI/math material is attributed to OpenAI under [Apache License 2.0](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/LICENSE). The freshly retrieved license is byte-identical to the [retained copy](../publication/upstream/OpenAI-math-LICENSE.txt); SHA-256 `c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4`. No root `NOTICE` file appears in the pinned root directory listing. Existing [third-party attribution](../THIRD-PARTY.md) remains applicable.

This research map reorganizes source metadata and abstracts, adds explicit status and verification annotations, and repins source links after corpus-equivalence checks. It does not modify upstream mathematical proofs or redistribute whole papers. No license is assigned here to independently written project proofs or checkers.

## Open work

The next audit should check each important claim's actual theorem hypotheses, proof dependencies, configured formal statement, admitted axioms and informal/formal correspondence; reproduce scoped checks; and seek independent mathematical evaluation. No upstream code or Lean build was run in this source audit. External peer review, novelty, priority and established acceptance were not demonstrated.
