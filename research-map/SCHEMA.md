# Schema, status rubric and counting rules

Edition 1.0.0, 13 October 2026. A catalog entry is a manuscript at an identified version, not an independently solved mathematical problem. The hierarchy is official field → provisional subfield → upstream problem family → manuscript/version, with separately identified claim-scope audits and local scoped results. Family IDs remain upstream labels, including gaps and family032's surviving and withdrawn members.

`catalog.json` contains provenance, coverage, 372 family records, manuscript records, targeted claim-scope audits and separate scoped results. `catalog.csv` is a flat manuscript export; JSON-valued columns preserve versions, links and gaps. The more detailed audit objects also live in `major-claims.json` and `scoped-results.json`. `taxonomy.json` records the basis for every subfield assignment. `source-audit.json` records freshness checks, hashes and source consistency. `version-history.json` preserves the 27 recorded directory revisions and three withdrawals. `schema.json` supplies a structural validation schema; structural validation is not proof verification.

The following axes must be read separately:

| Axis | Meaning and allowed conclusions |
|---|---|
| `catalog_status` | Active or withdrawn at the pinned source revision. Active means listed, without mathematical endorsement. |
| `statement_basis` | Author abstract metadata, precise theorem inspected, or an independently reviewed scoped statement. Metadata excerpts may omit essential qualifications. |
| `result_kind` | `full`, `partial`, `conditional`, `counterexample`, `technique`, or `unassessed`. Full applies to the identified statement under its stated hypotheses, never automatically to a broader famous problem. Unassessed is an intentional gap. |
| `evidence_review` | Manuscript rows default to metadata-only. Supplemental targeted entries explain exactly which theorem, scope note, notice or dependency was inspected. A whole family is never promoted because one member was read. |
| `formalization_source_listed` | A manifest reference, not a successful build or a correspondence certificate. |
| `formal_check_this_round` | No upstream checks were run in this organization round. Prior local receipts are dated and recorded separately; inspecting a receipt grants no fresh Lean pass. |
| `informal_formal_correspondence` | Requires the formal type, definitions, hypotheses and interpretation to match the precise informal statement. Kernel acceptance alone does not establish this. |
| `independent_mathematical_validation` | Separate from author review, author formalization, finite tests and our catalog review. Unknown validation is recorded as not established, not as disproved. |
| `established_acceptance` | Requires independent, attributable evidence of community acceptance for the precise result. Repository publication alone is insufficient. |
| `version` / `withdrawal` | Current path, historical path, recorded repair category and dated notices. A repair note does not establish the revised proof's correctness; withdrawal undermines a proof, not necessarily a statement. |

## Reliability tiers

These tiers describe the evidence in this map, not an ordinal probability of truth. Targeted major claims additionally use the explicit rubric within their own index; it refines these source and scope distinctions.

| Tier | Minimum evidence | Permitted description |
|---|---|---|
| R0 | Pinned author title/abstract/catalog | Author claim; theorem and correspondence pending review |
| R1 | Precise statement/hypotheses and relevant scope or correction notes inspected | Scoped claim audited; proof not thereby validated |
| R2 | Independent ordinary argument review for a precisely bounded statement | Reviewed scoped mathematical result; no machine certificate inferred |
| R3 | Identified formal statement, pinned build/type/axiom evidence, with assumptions explicit | Formally checked scoped statement at the recorded run; correspondence remains separate |
| R4 | Independent mathematical validation, completed correspondence where formal evidence is used, and attributable acceptance for the precise claim | Eligible for established-result assessment; famous-problem solution requires exact full-problem match |
| RX | Author withdrawal or unsupported proof notice | Withdrawn proof; statement truth unresolved |

No upstream famous-problem claim reaches R4 in this edition. No corpus-wide Lean verification, proof correctness, novelty, priority or external peer review is asserted. A conditional theorem cannot be promoted by silently treating its premise as proved.

## Learning priority and dependency hints

- L0: Audit a withdrawal, repair, dependency or correspondence risk before reuse.
- L1: Begin with a concrete scoped result with explicit hypotheses and manageable prerequisites.
- L2: Study after the listed analytic/algebraic prerequisites; verify the scope first.
- L3: Extract the precise statement and dependency contract before investing in proof reuse.

The major-claim index uses `P0: correspondence and dependency audit` for immediate prerequisite/scope assessment. The scoped-result index has its own supported vocabulary: `high` prioritizes accessible reusable study, `medium` recommends study after the stated prerequisites, and `advanced` signals a demanding analytic or formal prerequisite load. Its `learning_priority_basis` explains each choice. These are not reliability tiers or a direct conversion to the manuscript audit codes above.

Priorities guide study and audit effort, not importance or novelty. Prerequisites and dependency hints are supplied only where the inspected sources or scoped studies support them. Empty lists in metadata-only manuscript rows mean not yet mapped, rather than no dependencies. `hypotheses: null` means not exhaustively extracted, never no hypotheses. Subfields are editorial inferences from author metadata, explicitly marked provisional.

## Coverage units

The historical source inventory has 719 active manuscripts, 372 families, 17 fields, three withdrawn manuscripts, and 27 directory changes: 13 citation-only and 14 correction/repair/hypothesis-related. These units are not additive. Formalization source entries, declarations, comparator configurations and author top-line result counts are also different units.

`coverage.json` is generated from the actual catalog, rather than hand-written totals. All 719 active manuscript rows remain metadata-only, with supplemental targeted audits tracked separately. Three withdrawal notices have been reviewed. The number of targeted entries is not a count of fully reviewed manuscripts, and local scoped-result groups are not a theorem count. Zero upstream manuscripts have been independently mathematically validated or freshly Lean checked in this round. Unreviewed means not reviewed here; it does not assert that nobody else has reviewed the work.
