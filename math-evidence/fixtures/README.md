# Fixed live-gate test fixtures

These are test inputs, not project proofs. `Valid.lean` and `General.lean` test
successful fixed statements. `Sorry.lean`, `CustomAxiom.lean`,
`WrongStatement.lean` and `SkipKernel.lean` exercise separate rejection gates.
The skip-kernel fixture intentionally uses a Lean debugging option: compilation,
type and axiom checks alone can accept it, while required local replay rejects it.
The specialized plan checks against the full expected binder type.

Original live test results are historical in `../verification/HISTORICAL-EVIDENCE.json`.
Fresh public-package results are recorded separately in
`../verification/PUBLIC-VERIFICATION.json`. Fixture compilation does not certify
a project theorem or native Mac/MRS integration.
