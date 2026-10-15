# External data provenance and exact replay

Checked 2026-10-15 UTC. Only our independently authored code is run in the
commands below. The downloaded files are read as sign/numeric data. Do not
execute, import, `load`, or `exec` the downloaded `.py` file.

## Order 668

The construction is externally attributed to Levent Alpöge, Philippe Voinov,
Saul Reynolds-Haertle, and Claude; see the qualified primary/public account in
[SOURCES.md](SOURCES.md). Sumeet Motwani's CSV was linked in David E Speyer's
[MathOverflow verification](https://mathoverflow.net/a/514202).
The nreff repository reports reconstruction from the X sign payload, with its
own [pinned provenance](https://github.com/nreff/hadamard-search/blob/30afdda2a8ecfcc9733e26f979a1c5af36e73975/fixtures/known/hm-668/README.md).
We checked the matrices, not that reconstruction or the discovery method.

| Encoding | Bytes | SHA-256 of downloaded bytes |
| --- | ---: | --- |
| nreff sign rows | 446,892 | `bdeb5059d77e2703211082627b60441b8c888c928a55cc6f295e011941a387b0` |
| Motwani CSV | 1,115,894 | `5eaef5f4c814469a1f0815756876b83e8c4944ff7ccf4f023ee479de5e8f9a8b` |

The nreff source is pinned to `30afdda2a8ecfcc9733e26f979a1c5af36e73975`
(2026-08-13). The Drive file has no immutable revision URL available in this
audit; the byte hash identifies the checked version. Both parse to exactly the
same ordered sign matrix. The canonical representation is 668 sign rows with
one LF after each row, and has the nreff hash above. The independent comparison
checked byte-for-byte equality after its own CSV-to-sign serialization.

From the repository root:

```bash
curl --fail --location --silent --show-error \
  https://raw.githubusercontent.com/nreff/hadamard-search/30afdda2a8ecfcc9733e26f979a1c5af36e73975/fixtures/known/hm-668/matrix.txt \
  -o /tmp/hadamard-668.txt
python hadamard-study/scripts/hadamard.py /tmp/hadamard-668.txt \
  --expected-sha256 bdeb5059d77e2703211082627b60441b8c888c928a55cc6f295e011941a387b0
python hadamard-study/reviews/independent_check.py /tmp/hadamard-668.txt \
  --expected-order 668 --output /tmp/order-668-independent.json

curl --fail --location --silent --show-error \
  'https://drive.google.com/uc?export=download&id=1kxRbFEF5QFn7lWTSDhEDJCAETTgaSAsV' \
  -o /tmp/hadamard-668-primary.csv
python hadamard-study/scripts/hadamard.py /tmp/hadamard-668-primary.csv --format csv \
  --expected-sha256 5eaef5f4c814469a1f0815756876b83e8c4944ff7ccf4f023ee479de5e8f9a8b
```

Expected: order 668, 446224 entries, 222778 row pairs, all off-diagonal dot
products zero. Results are in [evidence/order-668-exact.json](evidence/order-668-exact.json),
[evidence/order-668-primary-csv.json](evidence/order-668-primary-csv.json), and
[reviews/order-668-independent.json](reviews/order-668-independent.json).
The independent data comparison is in
[reviews/source-data-comparison-independent.json](reviews/source-data-comparison-independent.json).

No explicit redistribution license was found for the nreff repository or the
Drive data. The full matrices, sign payload, compact seed, and third-party
implementation are therefore not bundled. Their absence is a deliberate
provenance/licensing choice; the replay recipe does require public host access.

## Order 2060

Credit: **Loïc Schneider**, as named by current Sage source; the repository
[MIT license](https://github.com/schneiderlo/hadamard-2060/blob/ad794186b6788328a2de6e6f6d68f7c493464735/LICENSE)
uses “Loic Schneider.” Source revision:
`ad794186b6788328a2de6e6f6d68f7c493464735` (2026-10-01); initial repository
commit 2026-08-25. Its README publishes the explicit data and the byte hash.
Our contribution is independent finite verification of the supplied matrix.
We did not run the Sage constructor or re-prove its Cooper–Wallis construction.

Downloaded `H2060.py`: **14,882,482 bytes**, SHA-256
`8c81090db76e2b503561ba82598b514e0c2e39940a3703783c5b1b2c6b80a37a`.
Canonical sign-row bytes after parsing have SHA-256
`c7a145d86210740dd3f8ea21ca896a54d6916007a042638f17c8c47f097200f7`.

```bash
curl --fail --location --silent --show-error \
  https://raw.githubusercontent.com/schneiderlo/hadamard-2060/ad794186b6788328a2de6e6f6d68f7c493464735/H2060.py \
  -o /tmp/hadamard-2060-data.py
python hadamard-study/scripts/hadamard.py /tmp/hadamard-2060-data.py --format h2060-data \
  --expected-sha256 8c81090db76e2b503561ba82598b514e0c2e39940a3703783c5b1b2c6b80a37a
python hadamard-study/reviews/independent_2060_check.py /tmp/hadamard-2060-data.py \
  --expected-sha256 8c81090db76e2b503561ba82598b514e0c2e39940a3703783c5b1b2c6b80a37a \
  --output /tmp/order-2060-independent.json
```

Expected: order 2060, 4243600 entries, 2120770 distinct row pairs, all
off-diagonal dot products zero. Both parsers require a fixed assignment header,
numeric sign rows, and a closing bracket; arbitrary Python is rejected.
No general expression evaluation or external-code execution is involved.
Results: [primary](evidence/order-2060-exact.json) and
[independent](reviews/order-2060-independent.json).
The large matrix is not bundled; no third-party MIT material is redistributed
or incorporated into our source code. Its license is not assigned to our work.

After the two 668 downloads, replay the independent Paley reconstruction,
all 13 stored Williamson witness matrices, exact source-entry comparison, and
full small-search solution-set comparison with:

```bash
python hadamard-study/reviews/independent_williamson_check.py \
  --output /tmp/williamson-independent.json
python hadamard-study/reviews/supplemental_review.py \
  --matrix-signs /tmp/hadamard-668.txt --matrix-csv /tmp/hadamard-668-primary.csv \
  --independent-williamson /tmp/williamson-independent.json \
  --output-dir /tmp/hadamard-supplemental-review
```

## Our code, data, and review boundaries

The Python study, tests, and independent review code are authored for this task
using the standard library. Paley/Williamson constructions and proofs are
classical, with bibliographic attribution in [PROOFS.md](PROOFS.md) and
[SOURCES.md](SOURCES.md). The small JSON sequences are generated by our complete
enumeration, not copied fixtures. No software dependencies were downloaded or
executed, and no license is assigned here to newly authored work.

External hashes identify bytes; row-pair checks establish orthogonality. Neither
check establishes the historical division of credit, the seed discovery method,
or universal Hadamard existence. Exact case coverage is recorded separately
from external reports. Independent review evidence records runtime/path metadata;
replays may differ in those fields while reproducing mathematical results.
