# Review and verification record

This edition separates mathematical proof, implementation review, and finite
computational evidence. Reviewers were separate agents in the same research
session; this is not an external certification.

| Record | Responsibility |
| --- | --- |
| [Mathematical review](math-review.md) | Independent audit of the final study, source hypotheses, classification, finite stopping proof, and example claims |
| [Implementation review](code-review.md) | Independent exact normalization/jet comparisons, budget semantics, parser and sign handling |
| [Example review](examples-review.md) | Independent derivations of the catalog and direct classification witnesses |
| [Fresh validation receipt](../evidence/validation.json) | Final commands, exit codes, environment, and file hashes |
| [Regression log](../evidence/unittest.log) | Standard-library suite, including parameterized and CLI cases |
| [Independent symbolic receipt](../evidence/independent-check.json) | Exact SymPy coefficient and resultant identities, with no classifier import |
| [Source receipts](../evidence/sources.json) | Version-pinned primary sources, inspected sections, and downloaded PDF hashes |

The standard test suite requires only Python. To rerun the additional independent
symbolic identities, install SymPy in an environment of your choice and run:

```bash
python critical-points/independent_check.py
```

The recorded run used SymPy 1.14.0. This optional dependency is not used by the
classifier or the standard-library tests. Full example outputs from both modes
are saved as [Bézout results](../evidence/results-bezout.json) and
[Płoski results](../evidence/results-ploski.json).

The classification and finite stopping arguments are ordinary proofs. The Python
implementation has been reviewed and tested, but has no machine-checked
soundness theorem. Nothing in this directory has been verified in Lean. The
analytic existence arguments certify no numerical neighborhood radius. The
implementation handles exact rational polynomials, and an optional computation
budget can return `unresolved`; it cannot silently establish a zero residual.

Repository inspection found no `AGENTS.md` in the checkout, ancestor workspace,
or fetched base tree, and no applicable checkout-local skill files. The base
commit and publication branch are recorded in the parent README and validation
receipt. This edition adds files only under `critical-points/`.
