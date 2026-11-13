# Frozen figures

Figures 1–3 retain the manuscript panel layouts. PNG and PDF files are paired with their numerical source data under `source_data/`. These are descriptive report-level figures, not distinct-trial counts.

## Supplementary Figure S1: analytical workflow

[PNG](Figure_S1.png), [PDF](Figure_S1.pdf) and [editable SVG](Figure_S1.svg) show the final analytical data flow. [Workflow documentation and caption](../docs/WORKFLOW.md) give definitions and reporting references. Counts are derived from the unchanged frozen `data/flow_counts.json`; the existing Figures 1–3 are unchanged.

To rebuild the count source with standard-library Python:

```bash
python3 scripts/build_workflow_data.py
```

Optional figure rendering uses D3 and Playwright (`npm install d3 playwright`, plus a Playwright Chromium browser or `CHROME_PATH` pointing to an existing Chrome executable):

```bash
node scripts/render_workflow.mjs
```

The figure's rendering dependencies are separate from numerical reproduction and its automated checks.
