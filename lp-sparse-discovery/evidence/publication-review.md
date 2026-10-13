# Scoped publication review

Reviewed on 2026-10-13 before the branch publication. This report concerns the
new `lp-sparse-discovery/` directory only.

## Scope and preserved material

The worktree was created on the assigned new branch
`codex/lp-sparse-discovery-2026-10-13` at the exact verified research baseline
`b1d6c20e2f02b484d09c5285e67d842b369f9df0`. No `AGENTS.md` or `SKILL.md` was
found in the supplied workspace or the baseline tree; no root `AGENTS.md`
was present. No applicable local skill instructions were omitted.

Before developing the study, the existing `lp-certificates/` component was
inspected at `032db09354d41b58c2e9211ed7e69024a3e74010`: README, mathematical
notes, deliberately incomplete finder and its notes, verifier interface and
Lean core. Its finder blob is
`aa51c335f878f3e61cfc5b29fd0ffa2d42d02403`. No source from that component was
copied, imported or altered. Its original soundness/export and incompleteness
claims retain their meaning.

This branch is based on the research baseline rather than the frozen LP
branch. Integrating the two branches is deferred to the parent. Shared
manifests, existing studies, existing branches, the original working checkout
and existing attribution files are preserved. Publication is a normal push
of the new branch, with no PR, merge or force push.

## Mathematical and computational evidence

The independent [mathematical review](../reviews/mathematical-review.md)
checked both support bounds, existence assumptions, equality reconstruction,
rationality, finite exhaustive search, safe pruning and every worked-example
section. The primary PDFs and page references were independently checked.
Review corrections were incorporated; no mathematical blocker remains.

The independent [computational review](../reviews/computational-review.md)
and additional [benchmark review](../benchmark/REVIEW.md) approved the stated
fixture scope. The root also ran the 14-test suite successfully under Python
3.12.14 and reproduced `benchmark/results.json` byte for byte. The independent
determinant/Cramer checker completed successfully: 44 fixture runs, 6
original-coordinate identities, 2 affine parametrizations, 5,040 toy inputs
and 10,080 toy searches, 13 zero-dimensional searches, and 2 searches for the
augmented first-success counterexample.

All of this is ordinary mathematical review and exact Python evidence.
No Lean build or formal verification of this study was performed or claimed.
No general solver, arbitrary input parser, improving-ray finder or end-to-end
verified discovery implementation is supplied.

## Privacy, attribution and licenses

The added public files are newly authored mathematical prose, rational
fixtures, Python research code, generated fixture results and scoped review
records. No third-party PDF text, images, dependency source, binaries or
compiled products are included. No private datasets, source archives,
credentials, tokens or secret keys occur in these files. A targeted scan for
common key/token markers and private relay addresses found no matches.

The locally configured private author email is not used for this publication.
A generic Codex author/committer identity is selected for the commit only;
no saved configuration, account, authentication or credential changes are
made. Private author details are not copied into the public evidence.

The baseline repository's `THIRD-PARTY.md` and retained upstream notices were
read and preserved. Cited sources are linked and paraphrased, not redistributed.
The repository reports no overall license; this study assigns no new license
and does not apply upstream license terms to the independently written files.

The scoped [provenance manifest](../PROVENANCE.json) binds the public file
bytes other than itself. Its self-exclusion avoids circular hashing. The final
remote commit and branch must be checked separately after publication; the
parent-facing completion report records that result.
