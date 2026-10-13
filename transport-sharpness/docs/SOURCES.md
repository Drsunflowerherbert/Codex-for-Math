# Sources, preservation, privacy and licenses

The starting research commit is
[`b1d6c20e2f02b484d09c5285e67d842b369f9df0`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/b1d6c20e2f02b484d09c5285e67d842b369f9df0).
The old tangent checkout was preserved. This task uses a new worktree and
branch `codex/transport-sharpness-2026-10-13`; its commit diff adds only
`transport-sharpness/`. Shared publication manifests and the main research
branch are left for the integration task.

The original study and review were read before development:

- [Transport proof](../../research/supplement/transport-stability/proof.md),
  theorem records, exact checker and fixtures; the starter proof is identical.
- [Prior independent audit](../../research/supplement/reviews/transport/audit-report.md),
  [optional fixed-mass refinement](../../research/supplement/reviews/transport/optional-refinements.md),
  and machine-readable review record.
- The retained upstream family 374 sharpness section, at
  `openai/math` revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

The upstream section was independently fetched this round from its
[revision-pinned official source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/build/source/sections/sharpness.tex).
The fetched file has 7,662 bytes and SHA-256
`2c1682fe0dc4bd8da5883760a909271382ec2a63ef68e8334b5491bb0985c902`.
The retained baseline section has 7,663 bytes and SHA-256
`f8732d68d0de8505d20f6c42aefce95d60b3e8363569681fa30632c997999590`:
it consists of exactly those upstream bytes followed by one newline.
No mathematical source text differs. The previous files are not normalized
or rewritten. The paper's upper bound and its formalization scope description
are source claims outside this round's review.

The upstream OpenAI/math snapshots are attributed under the existing
[THIRD-PARTY.md](../../THIRD-PARTY.md) and retained Apache 2.0
[license copy](../../publication/upstream/OpenAI-math-LICENSE.txt).
No additional third-party source snapshot or dependency tree is republished
in this directory. The new code and proof notes are not assigned the upstream
license; this task does not assign a new overall license. The exact checker
expands the prior independently written checker, with its relationship
identified in the file header.

The pinned official tools are Lean 4.24.0, compiler commit
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`, and mathlib
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, including all nine locked packages.
The verified saved archive SHA-256 is
`b14f5e5159219dd1a1956c3b806813319f5e94ccd5bdfd56f54520609a5bb5ec`.
The published [math-evidence toolkit](../../math-evidence/README.md) supplies
its compiler-byte audit and unchanged `EvidenceHarness.lean` helper. This is
a scoped custom full-type/body/replay check, not one of `live.cjs`'s fixed
accepted plans and not a native MRS receipt. No native Mac MRS integration is
claimed. Cached dependency OLeans and host runtime remain trusted inputs;
dependencies were not rebuilt from source and the same-kernel replay is not
an independently implemented kernel.

No `AGENTS.md` or relevant `.agents/skills` files were available at the
workspace, repository roots, or researched subtrees after explicit inspection.
No Library intermediate, account/credential/security change, purchase,
PR, merge, shared manifest edit or force push was used. The target repository
was inspected through existing authorized GitHub access and is public.
Published files contain mathematical source, rational fixtures and sanitized
local verification evidence; no credentials, private input archives,
compiled binaries or dependency caches are included. The publication audit
records the scoped paths, secret-pattern inspection and remote verification.
