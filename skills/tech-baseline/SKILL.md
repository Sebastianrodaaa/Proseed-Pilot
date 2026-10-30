---
name: tech-baseline
description: Use when analyzing how customers solve a problem today, which incumbent technologies they use, their performance and limitations, and where ProSeed technology could do better — Step 2b (Technical)
---

# Step 2b — Tech Baseline (Technical)

## Purpose

Understand the status quo you must beat: how customers solve the problem today, which technologies they use, how well those work, and where the ProSeed technology could plausibly outperform them.

The output is a comparison, not an essay — you are establishing the baseline your concept will be measured against.

## Inputs

`proseed/01-problem-hypotheses/problem-hypotheses.md`, plus internal ProSeed trial data where it exists.

## Method

Desk research and ProSeed trial data, per hypothesis. The template has two sections:

1. **Technologies used in the market** — one block per technology already available for this application (copy the block per technology). For each: **How it works**, **How well it performs** (on the metrics the customer is judged by — throughput, energy, cost/unit, quality, yield), and **Limits** (its technical limits regarding the hypothesis). The point is to see how different the options are — one technology or several, and how well each performs.
2. **Why our solution can be better** — plain text summarizing our know-how and research: why our technology could beat the current ones and whether we'd hold a real technical advantage. Then **1–5 key assumptions** as bullet points, with figures where possible — each marked clearly as *measured* (trial data) or *assumed*.

## Deliverable

**One filled document per hypothesis.** Copy `templates/attachment_202611_2b_Tech_Baseline_Template.dotx` to `proseed/02b-tech-baseline/<hypothesis-slug>-tech-baseline.docx` and fill it, replacing each `[Remove when filled]` guidance block. Keep the template's structure exactly — including the **Personal input** sign-off and the **Decision** checkboxes (☐ Go to next step / ☐ Rework / ☐ Drop the hypothesis).

A `.dotx` is a Word template: copy it to `.docx` and edit with Word, LibreOffice, or `python-docx`. Note: `python-docx` refuses `.dotx` directly — after copying to `.docx`, patch `[Content_Types].xml` inside the zip, replacing `template.main+xml` with `document.main+xml`.

Also write `proseed/02b-tech-baseline/tech-baseline.md` — the cross-hypothesis picture of where ProSeed's advantage is strongest and weakest, with links to each document.

Update `proseed/STATUS.md`.

## Red Flags

| Thought | Reality |
|---------|---------|
| "List the technologies" | Without performance numbers there is no baseline. Quantify. |
| "ProSeed wins on everything" | Suspicious. Find where incumbents are better and say so. |
| "Trial results and guesses look the same" | Mark measured vs. assumed explicitly — Step 5a tests the assumptions. |
| "The metrics we like are the metrics" | Use the metrics the *customer* is judged on. |

## Next

When this step and `proseed:market-scan` (2a) are both complete, invoke `proseed:customer-discovery` (Step 3).
