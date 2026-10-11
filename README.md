# Codex for Math

The standalone project in [tangent-limit/](tangent-limit/README.md) proves that
`tan(n)/n³ → 0` over positive integers and that `Σ |tan(n)|/n³` converges,
conditional on an explicit π-approximation hypothesis. It does not prove or
assert that hypothesis.

The results compiled with pinned Lean/mathlib 4.24.0. Sources, mathematical
proof, theorem statements, axiom audits, build logs, source attribution, and
milestone records are included. There are no proof placeholders or added axioms.

```bash
cd tangent-limit
./scripts/setup.sh
./scripts/verify.sh
```

See the [project README](tangent-limit/README.md) for dependency pins,
reproduction requirements, verification evidence, and its scope.
