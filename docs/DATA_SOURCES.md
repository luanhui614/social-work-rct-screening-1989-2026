# Data sources and variables

The underlying bibliographic data and basic source variables come from the [Social Work Meta-Data Project](https://github.com/beperron/SocialWork-MetaData), which distributes the **Social Work Research Database (SWRD)** and **SSWR Conference Database**. The upstream documentation was checked at commit `1444be06a0d47467d83afeaa9f7913e0bca33710` on 31 October 2026. Linkage metadata retained for this study were obtained from its `data-v1.4` export.

This study uses the supplied screening extracts: 65,290 journal records and 23,793 conference records. After source-flag and corroborated bibliographic deduplication and exclusion of one insufficient journal abstract, this study retains 63,803 journal records and 23,772 conference abstracts. The upstream project's 62,602-article *scientific-research core* has a different document-type scope and is not substituted for this study's denominator. The exact numbered upstream release used to create the initial screening extracts has not been established; their file hashes are retained in `data/source_registry.json`.

Source variables include identifiers, title, abstract, author metadata, year, journal or conference format, and DOI where available. The public study data retain identifiers, year, venue/format and DOI, original model labels, final reference labels and analysis-status flags. The record-level screening files omit source abstracts, author names, internal reviewer identities, free-text correspondence and draft decisions. Bibliographic QC summaries retain source publication-author strings where relevant to identity checking; these are not reviewer identities. Join to the upstream source by the documented IDs and verify title/DOI where appropriate; the study does not redefine upstream author identities.

The studies documenting database construction are:

Perron, B. E., Victor, B. G., & Qi, Z. (2026a). AI-assisted curation of conference scholarship: Compiling, structuring, and analyzing two decades of presentations at the Society for Social Work and Research (2005–2026). *Journal of the Society for Social Work and Research*. Advance online publication. https://doi.org/10.1086/741324

Perron, B. E., Victor, B. G., & Qi, Z. (2026b). Evolution of social work knowledge production over 35 years: An AI-enabled analysis of trends in empiricism, methodology, collaboration, citation patterns, and output. *Research on Social Work Practice, 36*(8), 1576–1590. https://doi.org/10.1177/10497315261416833

The source project's semantic-search instructions and any embedded credentials are not copied into this repository. No new license is assigned to upstream data by this study. The current repository contains no study-code license, following the author's release choice.

Current frozen counts and the original-versus-cleaned worklist denominators are in [Count flow](COUNT_FLOW.md). Final source flags and category decisions are in the frozen record file; source duplicate flags alone are not the full cleaning procedure.
