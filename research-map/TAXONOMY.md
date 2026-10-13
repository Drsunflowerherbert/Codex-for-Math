# Subject taxonomy, first edition

Created 2026-10-13 UTC. [`taxonomy.json`](taxonomy.json) maps all **372 families** in the existing inventory to a subfield under their **17 unchanged source discipline labels**. The classification source is [`research/starter/catalog/inventory.json`](../research/starter/catalog/inventory.json), checked there on 2026-10-11 and pinned to official OpenAI Math revision [`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb). Its SHA-256 is recorded in the JSON. This is coverage of that inventory snapshot; current official-source verification belongs to the map's separate provenance audit.

## What the labels mean

The hierarchy is **source discipline → inferred subfield → source family ID**. A family can contain multiple manuscripts, statements, versions or withdrawn records. It is a source grouping, not a count of distinct mathematical problems or independently proved results. The five gaps in the numerical sequence—045, 061, 070, 123 and 163—are absent from this inventory and have not been filled with invented records.

Each subfield has `taxonomy_basis: author_metadata_inference`. This means that editors inferred a subject from the source's titles and, where useful, abstracts. It is not an authoritative Mathematical Subject Classification assignment and does not adopt the author's asserted theorem as an established fact. Cross-field topics retain the official source's discipline even when another placement would also be reasonable; for example, the Langlands-related families retain their different source disciplines.

Subfields use standard broad subject areas where possible, such as chromatic homotopy theory, kinetic equations, counting and sampling algorithms, or algebraic and complex singularities. Small fields sometimes require singleton subfields: type theory and model theory are different study paths despite each having one family here. A family with several themes receives one browsing label for its central topic. Additional cross-links can be added after paper-level reading.

## Evidence and review limits

The `evidence_terms` array contains a short exact fragment of the inventory's family title, with its location and pinned source URL. It locates the topic cue without copying full abstracts or papers. `abstract_consulted` distinguishes labels for which an abstract was also inspected in this taxonomy task. A title match is subject evidence, not mathematical evidence.

All 372 subject labels were inspected across two classification passes, including an independent review of the first 187 assignments. That review moved family 188, a random triangle-removal process, into probabilistic combinatorics and refined families 001 and 008. Mechanical checks verified that each inventory family appears once, that the discipline labels are unchanged and that every recorded fragment occurs in the corresponding title.

`taxonomy_confidence` concerns only the subject label. `high` means the title names a recognizable narrow subject; `medium` means the label is broader or crosses subjects. These are provisional editorial judgements, not calibrated probabilities. Neither value communicates proof correctness, informal-to-formal correspondence, independent validation or community acceptance. No mathematical proof or Lean declaration was validated by this classification work.

## Known interpretation cautions

Family 032 remains under Hodge theory and algebraic cycles. Its active record and the three archived withdrawn Hodge-related manuscripts share a family association; the taxonomy does not turn those manuscripts into extra families or erase their withdrawal flags. Withdrawal, correction and version status must be read from the result catalog. These three withdrawals are not asserted to be the corpus's only issues.

Family 134 illustrates why this taxonomy avoids encoding headline bounds. The inventory's family title says generalized star height “at most three,” while its first manuscript abstract says “at most thirteen.” Its subject label is automata and formal languages. The discrepancy requires checking the precise dated manuscript statement against the latest official source before describing its mathematical result.

For future study, select a subject here, then consult the map's statement, hypothesis, dependency and reliability fields. Subfield coverage alone does not answer which major problems have been solved.
