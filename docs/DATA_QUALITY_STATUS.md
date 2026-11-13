# Data quality and statistical release status

As of 13 November 2026, final statistical release is on hold for bibliographic identity reconciliation. Computational checks reproduce the retained labels and reported arithmetic; this does not prove that the underlying source IDs are unique publications.

## Confirmed duplicate indexing affecting the journal numerator

|Case|Source IDs|Article DOI|Open action|
|---|---|---|---|
|J-DUP-001|25098 / 73534|10.1093/swr/19.3.131|Merge two source records for one article; one title contains a typographic omission|
|J-DUP-002|33736 / 82759|10.1300/J079v21n01_04|Merge one article indexed with different years; reconcile INDIVIDUAL versus CLUSTER|
|J-DUP-003|34120 / 82763|10.1300/J079v20n01_07|Merge one article indexed with different years; check eligibility against the existing analogue-task exclusion|

The evidence sources and precise issue status are retained in [machine-readable cases](../data/identity_qc_cases.json). The retained source flags mark these records as non-duplicates, so relying solely on those flags misses the duplicate publications. An additional near-title group, 82865 / 122194, requires identity checking and label reconciliation. Its two abstracts differ in whether random allocation is explicitly stated.

A same-journal, normalized-title scan generated 520 candidate groups, including 271 with matching normalized abstract text. These are candidate groups, not numbers of additional exclusions; the 271 groups are a subset of 520. Generic same-title items, distinct publications and reprints require bibliographic review. None of the unconfirmed candidates has been automatically deleted or recoded.

## Implication for current materials

The previous 388-journal-report snapshot and its denominator must not be cited as final deduplicated results. Merging only the three confirmed double-counted articles would reduce that numerator by three while preserving eligibility, but this conditional calculation is not a replacement final total. Other denominator candidates and the listed classification issues remain unresolved.

The current linkage snapshot contains 90 SAME, 99 RELATED_ONLY, 9 INDETERMINATE and 361 NOT_IDENTIFIED conference-report outcomes. The six source IDs in the three confirmed duplicate groups do not occur in the current pair file, so those three merges would not directly change these linkage outcomes. Global article-identity checks may still affect the journal search universe and linked-article summaries. These are recorded snapshot outcomes, not a newly certified final result.

## Resolution required before a final release

Establish a traceable source-ID-to-publication mapping; reconcile duplicate publications and publication years; resolve substantive label conflicts through the latest author decision; then regenerate denominators, verification summaries, annual and venue distributions, linkage aggregates, tables and figures. All original source IDs and decisions remain available for audit. The publication gate stays closed until this reconciliation and final checks are documented.

Earlier v1.0.0 and v1.1.0 releases are historical snapshots. They have not been retroactively rewritten as corrected datasets. Superseded generated outputs have been removed from the active branch and preserved locally; no force-push or tag rewrite is used.
