# Classification-source discovery and access log

Private review performed 16 October 2026. This log records queries, URLs, and retrieval outcomes; it contains no copied search-result passages or source paragraphs. It makes no claim that a negative search proves the absence of an erratum. No new search was performed to prepare this log.

## Exact discovery queries

The following queries were sent to the web tool's `system2_search_query` engine during the extended audit, grouped in their request order.

**Initial discovery**

```text
Anthony Manning papers There are no new Anosov diffeomorphisms on tori pdf Warwick
"Franks" "Anosov diffeomorphisms on tori" "pdf" -site:scispace.com -site:researchgate.net -site:bishtref.com
"Manning" "There are no new Anosov" full text
"On homotopy tori II" "errata"
```

**Original articles and Franks's survey**

```text
"Anosov diffeomorphisms on tori" "Franks" 1969 filetype:pdf
"There are no new Anosov" pdf -site:scispace.com -site:researchgate.net -site:portal.mardi4nfdi.de
"Franks" "Anosov diffeomorphisms" "Global Analysis" pdf 1970 61
"Manning" "Anosov" "erratum"
"Franks" "Anosov diffeomorphisms" "10.1090" "0271990"
"Anosov diffeomorphisms on tori" "gkxjeli14m" pdf
"There are no new Anosov" "Manning" "gap"
"Franks–Manning" "exotic" proof
"Anosov diffeomorphisms" "John Franks" "1970" "scispace"
"There are no new Anosov diffeomorphisms on tori" proof regional recurrence
```

**Proof ingredients and alternate author sources**

```text
"There are no new Anosov diffeomorphisms on tori" "422" "Proof"
"Classification of Anosov diffeomorphisms on Tori" Manning pdf
"Manning" "1974" "regional recurrence"
"Franks" "Anosov diffeomorphisms" "pdf" "61-93" -site:researchgate.net -site:scribd.com
"Franks" "Anosov diffeomorphisms" "pspum014"
"Anosov diffeomorphisms" "John Franks" "1970" "Theorem 2.1"
"Manning" "There are no new" "1974" "Markov"
"Manning" "regional recurrence" Anosov
"There are no new Anosov" Manning filetype:pdf site:edu
"There are no new Anosov" Manning filetype:pdf site:ac.uk
"Anosov diffeomorphisms" "John Franks" "thesis" 1968 pdf
"Classification of Anosov diffeomorphisms on Tori" "10.1007"
```

A second engine, `system1_search_query`, was used once to check coverage with these exact queries:

```text
"Manning" "Anosov" "1974" filetype:pdf 422
"Franks" "Anosov diffeomorphisms" "1970" filetype:pdf
"Manning’s proof of regional"
```

## Exact correction/counterexample queries

The final targeted `system2_search_query` request used:

```text
"There are no new Anosov diffeomorphisms on tori" erratum correction counterexample
"On homotopy tori II" correction erratum
"Anosov diffeomorphisms on tori" Franks erratum correction
"Hsiang" "Shaneson" "fake tori" gap error
```

No relevant erratum or counterexample was located. One issue-table-of-contents hit mentioned corrections; inspection showed that the correction belonged to Kingman's preceding article, not to Hsiang–Wall. This limited search does not certify that no correction exists.

## URL attempts and outcomes

| Target and exact URL | Method and outcome |
| --- | --- |
| Franks 1969 publisher PDF: <https://www.ams.org/journals/tran/1969-145-00/S0002-9947-1969-0253352-7/S0002-9947-1969-0253352-7.pdf> | Shell fetch: HTTP 403. Earlier web fetch also returned 403. |
| Alternate publisher path: <https://www.ams.org/tran/1969-145-00/S0002-9947-1969-0253352-7/S0002-9947-1969-0253352-7.pdf> | Earlier shell and web attempts: HTTP 403. |
| Franks discovery page: <https://scispace.com/papers/anosov-diffeomorphisms-on-tori-gkxjeli14m> | Web page accessible. Following its actual PDF link obtained the original eight-page scan as web text. Shell page request: empty HTTP 202 response. |
| Franks original scan mirror: <https://scispace.com/pdf/anosov-diffeomorphisms-on-tori-gkxjeli14m.pdf> | Web PDF extraction accessible and inspected. Shell download: empty HTTP 202 HTML response, not a PDF. |
| Manning 1974: <https://www.jstor.org/stable/pdf/2373551.pdf> | Nominal PDF endpoint yielded HTML/client-challenge or metadata content, not article pages. |
| Manning discovery page: <https://scispace.com/papers/there-are-no-new-anosov-diffeomorphisms-on-tori-4m3bf6v576> | Metadata page accessible; no accessible PDF link. |
| Attempted Manning mirror: <https://scispace.com/pdf/there-are-no-new-anosov-diffeomorphisms-on-tori-4m3bf6v576.pdf> | Web tool: inaccessible. Shell: empty HTTP 202 HTML response. No article pages obtained. |
| Franks 1970 DOI: <https://doi.org/10.1090/pspum/014/0271990> | Web tool: inaccessible. DOI identity separately confirmed by Crossref metadata. |
| Book DOI: <https://doi.org/10.1090/pspum/014/0266227> | Search exposed book contents; direct web open failed. |
| AMS book page: <https://www.ams.org/books/pspum/014/> | Web tool: HTTP 403. |
| Alternate book page: <https://www.ams.org/pspum/014> | Web tool: HTTP 403. |
| Attempted chapter PDF: <https://www.ams.org/books/pspum/014/0271990/pspum014-0271990.pdf> | Web tool: inaccessible. This was an attempted path, not a confirmed downloadable URL. |
| Alternate attempted chapter PDF: <https://www.ams.org/pspum/014/0271990/pspum014-0271990.pdf> | Web tool: inaccessible. This was an attempted path, not a confirmed downloadable URL. |
| Manning 1972 thesis: <https://wrap.warwick.ac.uk/id/eprint/71348/1/WRAP_Thesis_Manning_1972.pdf> | HTTP 200 PDF; 1,803,517 bytes; 60 pages. Downloaded and relevant chapters inspected. It predates the missing 1974 proof. |
| Manning 1977 survey: <https://www.numdam.org/item/AST_1977__50__273_0.pdf> | HTTP 200 PDF; 680,887 bytes. Relevant semiconjugacy proposition inspected; it does not establish full recurrence by itself. |
| Warwick proceedings: <https://link.springer.com/book/10.1007/BFb0082572> | Contents accessible; followed the relevant chapter link. |
| Manning 1975 report: <https://link.springer.com/chapter/10.1007/BFb0082587> | Bibliographic page accessible; full chapter is subscription content. |
| Attempted report PDF: <https://link.springer.com/content/pdf/10.1007/BFb0082587.pdf> | Web tool: inaccessible. No proof pages obtained. |
| Hsiang–Wall original: <https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hsiawall2.pdf> | Extended-audit shell fetch: HTTP 200 PDF; 167,250 bytes. Both pages inspected; p. 342 rendered and visually checked. Earlier attempts had returned 503/timeouts. |
| Earlier alternate Hsiang–Wall host: <https://www.maths.ed.ac.uk/~v1ranick/papers/hsiawall2.pdf> | Earlier shell fetch: HTTP 503. |
| Attempted Wall earlier note: <https://webhomes.maths.ed.ac.uk/~v1ranick/papers/walltorus.pdf> | Shell fetch: HTTP 404. This was an attempted filename, not a verified source link. |
| Hsiang–Wall DOI: <https://doi.org/10.1112/blms/1.3.341> | Web redirect to Wiley failed; the original scan above was available. |
| Issue contents: <https://londmathsoc.onlinelibrary.wiley.com/toc/14692120/1969/1/3> | Accessible; checked correction attribution described above. |
| Topology reading list: <https://www.maths.gla.ac.uk/~mpowell/topological-manifolds.html> | Web fetch timed out. |
| Hyperbolic-dynamics survey: <https://citeseerx.ist.psu.edu/document?doi=9c4376ed2c47901d380ee29134e8737c97117157&repid=rep1&type=pdf> | Web fetch: HTTP 403. No source proof inspected there. |

Earlier audit sources retained as context: Fisher–Kalinin–Spatzier's primary research restatement at <https://jfdavis.pages.iu.edu/papers/fksd.pdf> was successfully downloaded and read; Hsiang–Shaneson's earlier PNAS scan at <https://www.maths.gla.ac.uk/~mpowell/hsiang-shaneson-homotopy-tori-II.pdf> was successfully downloaded and checked for its weaker finite-cover statement.

Metadata-only retrievals used the exact endpoints below. These were discovery checks, not access to proof pages:

```text
https://api.crossref.org/works/10.1090/pspum/014/0271990
https://api.crossref.org/works?query.title=Anosov%20diffeomorphisms%20Franks&rows=6
https://archive.org/advancedsearch.php?q=title%3A%28%22global+analysis%22%29+AND+year%3A1970&output=json
https://archive.org/metadata/globalanalysis0016vari
```

The Internet Archive candidate was a different volume and access-restricted; no restricted full text was fetched. Failed or HTML responses were never treated as checked PDFs. No access controls were bypassed, and no purchase, installation, public write, or author contact was attempted.

## Remaining limit

**UNVERIFIED:** the original Manning 1974 regional-recurrence/full-nonwandering-set proof and the original Franks 1970 proof. Accessible earlier material and later statements do not erase this proof-access limit. Hsiang–Wall's original proof was inspected, while its deep surgery and Kirby–Siebenmann inputs remain unreproved in this bounded audit.
