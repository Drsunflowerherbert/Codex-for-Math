# Future MRS adapter contract

`math-exchange/v1` and `research-collection/v1` are explicitly portable formats.
They are not native MRS schemas. No installed MRS API, database, command, native
export bytes or Mac runtime was accessed or validated for this public toolkit.
No native schema translation or integration is claimed.

Before implementing a separate explicit adapter, obtain the documented native
export/import contract, representative original bytes and transaction/backup
behavior. Review identifier and statement formats; assumption versus axiom
semantics; proof dependencies and premise discharge; revisions and attachments;
review identity/status meanings; finite-experiment scope; Lean receipt trust;
conflict and deletion behavior; dry-run support and restoration.

A converter must preserve original IDs, assumptions, revisions, attachment hashes
and reported statuses. Unsupported fields require an auditable unmapped-field
report or preserved original attachment. Test field-level mapping and round trips
against representative exports before any native write. Do not silently repair
status or infer native integration from a schema-validation result.

An ordinary review cannot become Lean checked; finite examples cannot become a
theorem proof; missing evidence cannot become a successful receipt. Imported
historical Lean reports remain historical. Saved receipt inspection remains
integrity-only even when all reported artifacts are consistent.
