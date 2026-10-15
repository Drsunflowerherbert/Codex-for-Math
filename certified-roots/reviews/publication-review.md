# Independent publication assembly review

Date: 15 October 2026. Reviewer: a separate publication-review agent, who did
not author the study, checker, test suite, or evidence assembly. **Disposition:
approved for final manifest assembly and publication; no unresolved content
blocker found.** This review is a release-consistency check, not external peer
review or formal verification.

## Scope and findings

The README, input/output contract, structural JSON Schema, verification notes,
study, examples, and both independent technical reviews were read. The
distinction between the authoritative Python validator and the structural
JSON Schema is explicit. Advertised input limits, exact rational outputs,
exit codes, box-specific uniqueness, error-bound clipping, and trust limits
agree with the implementation and evidence. No claim of Lean verification,
global root enumeration, or correctness proved by finite tests was found.
The material accurately separates failed certification from nonexistence and
small residuals from existence certificates.

All 19 file-hash entries across the mathematics and checker reviews match the
current bytes. The evidence record's 17 source hashes also match. The two
technical reviews approve their stated scopes without an unresolved blocker;
this review checks their assembly rather than replacing their mathematical
and implementation examinations.

The publication reviewer independently executed:

```text
python3 -B -m unittest discover -s certified-roots/tests -v
Ran 45 tests
OK

python3 -B certified-roots/reviews/independent_check.py
{"counts": {"affine_cases": 604, "hand_example_cases": 4, "long_output_cases": 6, "parser_boundary_cli_cases": 18, "power_cases": 924, "rank_cases": 681}, "status": "passed"}
```

The audit counts sum to 2,237. Fresh CLI executions of all four fixture files
were compared to every field in `evidence/example-results.json`, with exact
JSON equality and the documented exit codes: `0`, `0`, `1`, `1` for circle/line,
circle/parabola, no-root failure, and two-root failure respectively. The saved
test transcript has 45 successful test lines and an `OK` conclusion. The
saved audit transcript matches the verification record; its environment agrees
with the executed CPython 3.12.14 runtime. Evidence files therefore describe
the reviewed source bytes and reproducible observed results.

Twenty-five local Markdown links were checked before this review was added.
All resolve except the deliberately pending `evidence/manifest.json`, to be
assembled after this review. The final manifest should include this review
and every deliverable except itself, avoiding a self-hash cycle. This review
does not attest to a manifest that has not yet been generated.

The supplied PDF is a ten-page reading copy. Its extracted text contains the
study's theorem, proof, interval rules, source comparison, workflow, and all
four worked examples in source order. The canonical Markdown hashes match
the approved mathematical review. Independent `pdftotext -bbox-layout`
inspection found 3,916 extracted words, no replacement glyphs, and no word
bounding box outside a page. The assembly author separately performed the
representative theorem/example page visual inspection documented in
`VERIFICATION.md`. This reviewer did not perform a second raster-based visual
inspection or rebuild the PDF; text extraction is not a proof of every
typographical detail. No severe display issue was identified by these checks.

At review time, `HEAD` is the required baseline
`e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f`, on branch
`codex/certified-roots-2026-10-15`. The tracked diff against that baseline is
empty, and all untracked additions are within `certified-roots/`; generated
Python caches are ignored. No baseline file outside the assigned directory
is changed. The pre-publication remote snapshot records ten existing branch
heads, including the required integrated baseline. Remote publication and
post-push byte/ref verification remain the publisher's next steps; this local
review does not claim they have already happened.

## Reviewed release bytes

SHA-256 values below are relative to `certified-roots/`. They exclude this
review itself and the pending manifest. Later content edits require renewed
review of the affected scope.

```text
862263fa1f46c20f0d1e4dac5ffcc75abd55c08211b2c3864c5f8764b9d87793  .gitignore
9b7954535b74f8dbb6099b2c59091a186ddc8792d1b6bc0886878c414250445a  EXAMPLES.md
e4b2469d2f6ab731df6ac39f26f4c78f3ba455c49b629841cfd071595447aac8  README.md
3225926fb8d3e2824b3ac99f44d37d8c597115a1e640d092b5f10c365a4ba9b8  SCHEMA.md
e116be25ba4683dbea8e23648dfb1ee28c8b00e1fb74a889a5303b5b655d529b  STUDY.md
cb7471fb6dfd7cd7e09e328a5aafc3666a22988af413048c3f9d5ff4e33dd451  STUDY.pdf
028b230f28f1e1e91208a7bf8e72e4741aa10a369ef874decb198ffe7306d5e2  VERIFICATION.md
a3d8541e689a0de5d4150a3ffc107aae78941c2b75adcdfe31ec913a16e1a04f  certificate.schema.json
099befd14e711f87087c885727f5f3b6810c031c3985ab3aa14cc66298025f20  evidence/example-results.json
f3e18ca50cbcf94afdf666182c99dd4d73d427e29e1b4fc4adb06ba38e75bd65  evidence/independent-results.txt
45f95adfa3a4969b8889339998e75969df8ce9660b70cd6bf7373bc2381701e6  evidence/remote-before.json
a5fa4310cfabb40a9e308053f20f31a01099007bdba82c856079c5170e68496b  evidence/test-results.txt
969e0ce39032186cb5930a452064835ce9c98d172aed7f74baa40a2c842bdc92  evidence/verification.json
904ef6da1c413ba0a686bdc3cde0d911883895013e3f7dca248bb2bfe9fb5293  examples/circle-line.json
3528298bfd450555079b9d49468429dd8b931de44d66f383423ed6a9c6928cdd  examples/circle-parabola.json
20588a667c8700a37faa7f8ea0f4294e9abeba1213249706d57ec20e7f578e2d  examples/tiny-residual-no-root.json
52083e36e8ad1258bb1ff79884fdabd7a463e2deb2a1637170516e8d9b54367f  examples/tiny-residual-two-roots.json
da357861fa611bf883efaf2d81b83d5ddf0545385f4f34f45da595c2d5c6d575  reviews/checker-review.md
82e8f9841314cbb862f1d79414a2ea38503d5a578e347b72bad3e3e25ba1bde5  reviews/independent_check.py
891caf91be5bf5155c752249339ebfb5f0f3a6fc05bfdab3c085a4b80baebf1a  reviews/mathematics-review.md
295848feee8cf6b023863d9a8f96abcf2a34c78558c0cfbf27694863a4c2c5c9  tests/test_verify.py
e99f15513430c980e2c5dd0ab2a09c0e1c41963007125491df8f11d7f9940264  verify.py
```

The remaining trust assumptions are those already disclosed: the reviewed
source, Python runtime and exact arithmetic, faithful input transcription,
and the mathematical proof. This release review adds reproducible consistency
checks; it does not remove those assumptions.
