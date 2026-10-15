# Independent review of the global guide

Reviewer role: source and conventions auditor, independent of the global-guide author.
Reviewed on 2026-10-15: `CONVENTIONS.md`, `COUNTEREXAMPLES.md`, `PROBLEMS.md`.
Reference crosscheck: `SOURCES.md`, Hunter's completed-product discussion, and
Simon's 2018 area/coarea statements. This is mathematical editorial review, not
proof-assistant verification or review of every individual solution.

| Finding | Disposition |
|---|---|
| The unqualified statement that all measure spaces used are sigma-finite would incorrectly include ambient H^k on R^n for k<n. Such an ambient measure is not sigma-finite. | Repaired in `CONVENTIONS.md`: scope sigma-finiteness to the Lebesgue/countable counting factors in product theorems; separately identify the restrictions used for geometric integration. |
| Fixed-integrand integrals were distinguished from functions, but parameter integrals also define functions. | Added the explicit distinction between the map F and its value F(t). |
| The area Jacobian is only defined almost everywhere by differentiability. | Specified its zero extension on the exceptional source set, which does not affect the area formula. |
| The expression w times multiplicity can contain 0 times infinity for nonnegative weights. | Specified a nonnegative Borel weight and the standard nonnegative-integration convention 0 times infinity equals zero. |
| “All maps used below” could incorrectly include the Cantor staircase in a Lipschitz assertion. | Narrowed the claim to parametrizations where area is applied; explicitly excluded the staircase counterexample. |
| The convergence paragraph did not explicitly repeat measurability. | Made measurability explicit and identified the nonnegative version of monotone convergence used. |
| The counterexample atlas attributed the general uniform-derivative theorem to the fundamental theorem without assuming continuous derivatives. | Identified the mean value theorem argument for differentiable functions, retaining the FTC argument for C1 functions. |

The following were checked and accepted without mathematical change:

- The Hausdorff factor is omega_k / 2^k, with H^0 counting measure, so k-plane
  values agree with k-dimensional Lebesgue measure. Using diameter at most delta
  versus diameter strictly less than delta gives the same limiting measure.
- Product measurability gives measurable sections everywhere, whereas completed
  Lebesgue measurability guarantees sections only almost everywhere. The outer
  integral uses a measurable representative. Both documents maintain this distinction.
- Signed Fubini requires absolute integrability. Nonnegative Tonelli may produce
  infinity. The positive/negative-part definition does not assign infinity minus
  infinity a value.
- Area uses the source-dimension Hausdorff measure on the image and counts all
  preimages with nonnegative weights. Coarea uses target Lebesgue measure and
  fiber Hausdorff dimension n-m. Division by the coarea Jacobian is confined to
  its positive set, with a separate zero-set contribution.
- Scalar Hausdorff integration has no orientation; circulation uses a directed
  tangent, and flux uses a chosen normal. Reversing those choices changes the
  corresponding oriented integral's sign.
- The problem index is spoiler-light: it lists goals and techniques, leaving
  numerical answers in the solution files. Its IDs and linked navigation need a
  final metadata/file-existence audit once all files are assembled.
- The atlas's finite-measure uniform-integrability statement is correct. Its
  infinite-space statement correctly requires both value tails and spatial
  tightness; the exact measurable-function and convergence hypotheses are
  intentionally delegated to E14. No additional sufficiency is inferred from
  bounded integral mass alone.

Follow-up: E14 and E15 were also read against the atlas after their full text
was available. The explicit value-tail condition, spatial tightness, finite-space
truncation proof, and local-convergence reduction in E14 support the atlas's
claims. E15's common full-measure differentiability set and local integrable
derivative majorant support its mean-value/dominated-convergence argument; its
one-sided endpoint variant has the required right differentiability. Accepted.

Remaining publication checks: validate the assembled metadata/source IDs and
links, and run the root's build and repository checks. No unresolved mathematical
defect remains in the three global files at the time of this review.


## Final assembled metadata and publication-guide audit

Completed 2026-10-15 after all 16 independently reviewed example hashes were
locked. All 16 titles, defining hypotheses, recorded results, measure conventions,
and source IDs were compared with the examples. The metadata and discovery index
have identical IDs, paths, titles and discovery fields; every problem-index link
points to its matching solution. All source IDs resolve to both `SOURCES.md` and
the primary snapshot records. No example source was edited in this audit.

A retrieval gap was repaired in metadata only: all explicitly written backtick
tags in each example's Reusable technique section were unioned with the author's
existing technique labels. E13 also received a manual `multiplicity` technique
tag, making 45 additions in total. The assembler then synchronized metadata, index and
review manifest; all original review hashes still match. Representative checks
now return E08/E11/E13 for `--technique multiplicity`, E12 for `--topic coarea`,
and E06/E13/E14/E15/E16 for `--text dominated`. Default retrieval does not print
the recorded result; `--solutions` does.

`README.md` now states that paths are relative to `integral-examples/` and that
`--text` searches discovery fields rather than full solution prose or recorded
hypotheses/results. This accurately describes the local helper. The separate
discovery index omits the result and hypotheses fields. Substring matching is
intended; semantic or full-text search is not claimed.

All six primary PDF links and the historical Simon comparison PDF link returned
HTTP 200 with PDF content types. `checks/source-references.json` records actual
downloaded SHA256 hashes, byte sizes, access dates, resolved URLs and theorem
locators. No cited PDF is redistributed. The mutable source URLs are not
represented as immutable versions.

`VERIFICATION.md` was checked against the reviewer records, concrete check log,
structural checker and PDF build record. Its 92-check total and zero failures
match the recorded log; E03 correctly has zero computational checks. Its claims
are explicitly limited to independent model audits, concrete symbolic/numerical
consistency, structural checks and document compilation. Human peer review,
certified quadrature error bounds and formal proof verification are not claimed.
Current Markdown input hashes also match the PDF build record. Final remote
publication and remote-content verification remain the root agent's task.

The hashes below identify the global documents and assembled retrieval artifacts
reviewed here. This review file does not hash itself.

| Reviewed file | SHA256 |
|---|---|
| `README.md` | `80dc2463768c7f992778896aa220ea41dfbb146a4b3b206489747b0356691c99` |
| `CONVENTIONS.md` | `b689b92b558d2a940362b381f0109de3badadec953a0b208e5fc4be6e9c5045a` |
| `COUNTEREXAMPLES.md` | `a94db2d8ad157c975c47b5ef1de17c62b00ad0569ace6b73eccb005b4824c0c3` |
| `PROBLEMS.md` | `c8983187d5f1831843e4d5903f6c30cddccb175a1723aa1e933444a18440a1f0` |
| `SOURCES.md` | `6687de2bd8f53220f205d724168bf2117fd1f55cbaddc9d3481c99ee791d3022` |
| `VERIFICATION.md` | `a8d300b6b58f514ef02b4c2be2e44603c8698f056f5bc377c658ee57a3e2ff69` |
| `metadata.json` | `4a6a35f14a77b77b713602a635706bc8b93396d327105cb0ea7abe9661635765` |
| `index.json` | `4d25498569bae7ee415e1eabbd990a8c95b661c97b97a12c1810605efb483f33` |
| `metadata.schema.json` | `23ce5c53bc310346035432203f2765c8927b27963a4ed73ebc42b7cce3e1505b` |
| `find_examples.py` | `9878a8ec2d4048cb594875c4d19fecf2e5c4076b6e4373590791d134bd171838` |
| `reviews/review-manifest.json` | `538e3cbd9d2a97988e653fb33eb4dda3af05dd39041f4f49d39982a41d1b304d` |
| `checks/source-references.json` | `0ff012848907d9126935c18b82cfae3b384983fd378c4a0d9b699437c6c4261d` |

Disposition: accepted for publication preparation; no unresolved mathematical,
source-link, metadata-consistency or navigation defect was found in this scope.
