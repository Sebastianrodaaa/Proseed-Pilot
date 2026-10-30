---
name: problem-hypotheses
description: Use when starting a ProSeed validation, framing who has a problem worth solving, or formulating "we believe [customers] want [outcome] because [problem]" statements — Step 1 (Together)
---

# Step 1 — Problem Hypotheses (Together)

## Purpose

Identify which customers have a problem worth solving and what they are trying to achieve. This is the seed everything else grows from — a weak problem hypothesis produces a confident, well-researched answer to a question nobody asked.

Start from the customer's goal, not from your solution. The technology is not the protagonist here.

## Inputs

Nothing. This is the entry point — bring what you know about the technology and the domains it might serve.

## Method

1. List candidate customer types who might have a problem the technology could address. Be specific about *who*: not "food producers" but "seed processors treating >500 t/yr of grain".
2. For each customer, work out what they are trying to achieve — the job, the outcome, the metric they are judged on.
3. Identify what stands between them and that outcome today: cost, quality losses, throughput, regulation, energy, labor.
4. Write one hypothesis per customer-problem pair in the canonical form:

   > **"We believe [customers] want [outcome] because [problem]."**

   The template frames the same statement as three fields — **Target customers** (who has the need and what they do: precise enough to find and call, broad enough to be a real market), **What they want** (the type of product or solution they are looking for, seen from *their* side, not our technology), and **Because** (what they want to achieve and how this type of solution helps them get there).
5. Rank hypotheses by how painful the problem is likely to be and how reachable the customer is, not by how well the technology fits.
6. If `proseed/` does not exist yet, create it and initialize `proseed/STATUS.md` (see `proseed:proseed-workflow`).

## Deliverable

**One filled document per hypothesis.** Copy `templates/attachment_202610_1_Hypothesis_Problem_Template.dotx` to `proseed/01-problem-hypotheses/<hypothesis-slug>.docx` and fill it, replacing each `[Remove when filled]` guidance block with content. Keep the template's structure exactly — including the **Personal input** sign-off (name, date) and the **Decision** checkboxes (☐ Go to next step / ☐ Rework / ☐ Drop the hypothesis).

A `.dotx` is a Word template: copy it to `.docx` and edit with Word, LibreOffice, or `python-docx`. Note: `python-docx` refuses `.dotx` directly — after copying to `.docx`, patch `[Content_Types].xml` inside the zip, replacing `template.main+xml` with `document.main+xml`.

Also write `proseed/01-problem-hypotheses/problem-hypotheses.md` — the ranked list of all hypotheses, each linking to its document, so parallel Step-2 work can pick them up.

Update `proseed/STATUS.md`: mark Step 1 complete, set current step to 2a/2b.

## Red Flags

| Thought | Reality |
|---------|---------|
| "Our technology does X, who wants it?" | Solution-first framing. Start from the customer's goal. |
| "Everyone has this problem" | Then the hypothesis says nothing. Narrow the customer. |
| "One hypothesis is enough" | Steps 2–4 test hypotheses against reality. Bring several. |
| "We can skip writing them down" | Steps 2a/2b research *per hypothesis*. Write them. |

## Next

Dispatch both parallel investigations — `proseed:market-scan` (2a, Commercial) and `proseed:tech-baseline` (2b, Technical).
