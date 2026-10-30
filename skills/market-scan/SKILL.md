---
name: market-scan
description: Use when identifying target customer segments, estimating how many potential customers exist, or researching who serves a need today, market size, and regulation — Step 2a (Commercial)
---

# Step 2a — Market Scan (Commercial)

## Purpose

For each problem hypothesis, determine whether a real market exists: which customers have the problem, roughly how many of them there are, who serves the need today, and what regulation shapes the space.

## Inputs

`proseed/01-problem-hypotheses/problem-hypotheses.md` — run the scan **per hypothesis**, not once for the whole idea.

## Method

Desk research, per hypothesis. The template asks four questions — each answered as plain text plus a small summary table:

1. **Market size.** How big is this market, and is it big enough for the long-term goal? Not a TAM/SAM/SOM exercise — an order-of-magnitude picture. Plain-text summary of findings, then the region table: Europe / Asia / America / Africa × size ($B).
2. **Target customers.** How many customers there are and whether they are large or small companies (order of magnitude), to judge how hard the market is to reach. Plain text, then the table: customer size (Large / Medium / Small) × approx. number × market share %. **No list of companies.**
3. **Players offering a solution today.** How many companies already sell a solution to these customers — does one dominate or is it split? Plain text, then the table: player × type of solution × market share %.
4. **Regulation.** The main regulations specific to this industry or market. Table: regulation × jurisdiction × what it means for us; add rows as needed.

Kill or deprioritize hypotheses whose market is too small, unreachable, or legally blocked — say so explicitly rather than quietly dropping them. Every number carries a source and a date.

## Deliverable

**One filled document per hypothesis.** Copy `templates/attachment_202610_2a_Market_Scan_Template_.dotx` to `proseed/02a-market-scan/<hypothesis-slug>-market-scan.docx` and fill it, replacing each `[Remove when filled]` guidance block. Keep the template's structure exactly — including the **Personal input** sign-off and the **Decision** checkboxes (☐ Go to next step / ☐ Rework / ☐ Drop the hypothesis).

A `.dotx` is a Word template: copy it to `.docx` and edit with Word, LibreOffice, or `python-docx`. Note: `python-docx` refuses `.dotx` directly — after copying to `.docx`, patch `[Content_Types].xml` inside the zip, replacing `template.main+xml` with `document.main+xml`.

Also write `proseed/02a-market-scan/market-scan.md` — the cross-hypothesis ranking of which markets hold up and which died, with links to each document.

Update `proseed/STATUS.md`.

## Red Flags

| Thought | Reality |
|---------|---------|
| "One scan covers all hypotheses" | Different customers live in different markets. Scan per hypothesis. |
| "Let's do a proper TAM/SAM/SOM" | The template says don't — order of magnitude per region is the point. |
| "List the companies we found" | Template says no company lists — sizes and counts, not names. |
| "Regulation is a later problem" | In industrial markets regulation often decides viability now. |
| "We'll fix the weak hypotheses later" | Kill them now, in writing. Later never comes. |

## Next

When this step and `proseed:tech-baseline` (2b) are both complete, invoke `proseed:customer-discovery` (Step 3).
