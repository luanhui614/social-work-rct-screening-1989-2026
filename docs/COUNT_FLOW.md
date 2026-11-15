# Source-to-analysis count flow

Data freeze: `screening-human-adjudication-final-2026-11-13-v6`.

## Source records and data cleaning

|Stage|Journal|Conference|
|---|---:|---:|
|Source records|65,290|23,793|
|Source-designated duplicate indices excluded|872|21|
|Additional bibliographic duplicate indices excluded|614|0|
|All duplicate indices excluded|1,486|21|
|Records after deduplication|63,804|23,772|
|Insufficient abstract excluded|1|0|
|Eligible analysis records|63,803|23,772|

## Screening groups

|Model RCT judgments|Journal|Conference|Human-review route|
|---|---:|---:|---|
|Both positive|382|531|All records|
|One positive|70|55|All records|
|Both negative|63,351|23,186|Targeted candidate samples|
|Total|63,803|23,772|Separate corpus denominators|

## Verification denominators

|Stage|Journal|Conference|Total|
|---|---:|---:|---:|
|Selected source IDs|748|874|1,622|
|Duplicate indices excluded|9|0|9|
|Insufficient abstract excluded|1|0|1|
|Verification analysis records|738|874|1,612|

The original selected IDs are preserved for membership checks. One additional journal record reviewed during linkage is SECONDARY; it is stored separately from the designed verification sample.

## Human verification results

|Corpus and group|Reviewed|RCT|Non-RCT|Metric|
|---|---:|---:|---:|---|
|Journal: both positive|382|372|10|PPV 97.4%|
|Journal: disagreement|70|10|60|RCT yield 14.3%|
|Journal: both negative, targeted sample|286|2|284|Sample NPV 99.3%|
|Conference: both positive|531|527|4|PPV 99.2%|
|Conference: disagreement|55|28|27|RCT yield 50.9%|
|Conference: both negative, targeted sample|288|4|284|Sample NPV 98.6%|

Journal RCT reports: 372 + 10 + 2 = **384**. Conference RCT reports: 527 + 28 + 4 = **559**.

|Final outcome|Journal|Conference|
|---|---:|---:|
|INDIVIDUAL RCT reports|351|474|
|CLUSTER RCT reports|33|85|
|All RCT reports|384|559|
|Eligible records|63,803|23,772|
|RCT reports per 1,000 records|6.0|23.5|
|Wilson 95% interval per 1,000|[5.4, 6.6]|[21.7, 25.5]|

## Primary linkage outcome

|Conference subset|Reports|Confirmed same-trial outcome article|Without a confirmed same-trial outcome article|
|---|---:|---:|---:|
|2005–2026|559|90|469|
|2005–2021|423|79|344|

The 115 SAME pairs involve 90 conference reports and 73 distinct journal articles. Publication intervals use the earliest same-trial article for each linked conference report. [Figure 1](../figures/Figure_1.pdf) presents the screening workflow, and [Figure 4](../figures/Figure_4.pdf) presents linkage.
