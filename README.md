# Conditional tangent-limit project

Branch: `codex/tangent-limit`. This remains the repository default because the
GitHub integration rejected changing the default to `main` (HTTP 403). The planned
topic name `research/tangent-limit` is pending that administration step.

This branch preserves the original standalone Lean project; repository-wide
navigation is available on [main](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/main).

The project proves `tan(n)/n³ → 0` over positive integers and convergence of
`Σ |tan(n)|/n³`, **conditional on the explicit `PiDiophantine` approximation
hypothesis**. It does not prove that hypothesis.

## Start here

- [Project README](tangent-limit/README.md): assumptions, pinned dependencies and reproduction.
- [Original research edition](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/d00a89dd9ce6c8ef782234d28c93e69cb712c947/tangent-limit/README.md): exact project snapshot and saved build/type/axiom evidence.
- [Repository project catalog](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/main/docs/CATALOG.md).
- [Branch roles and old-to-new mapping](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/main/docs/BRANCHES.md).
- [Clone and link migration](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/main/docs/MIGRATION.md).

The complete `tangent-limit/` tree is preserved byte-for-byte. Saved evidence
describes its recorded source snapshot; this navigation change did not rerun
Lean or project scripts. The sharp-series extension is a separate project in
the [integrated collection](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/integrated/tangent-sharp).
