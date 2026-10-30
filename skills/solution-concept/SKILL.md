---
name: solution-concept
description: Use when sketching what the ProSeed solution could look like, exploring solution alternatives, or producing the one-page concept after customer discovery — Step 4 (Technical)
---

# Step 4 — Concept (Technical)

## Purpose

Explore what the solution could look like and which alternatives it would compete with. The output is a one-page concept built on what discovery actually found — not the product you walked in wanting to build.

The solution could be a machine, software, a service, or a mix. Stay honest about which form the problem wants.

## Inputs

- `proseed/03-customer-discovery/` — synthesis and interview evidence
- `proseed/02b-tech-baseline/tech-baseline.md` — the performance gap the concept must close

## Method

1. Re-read the discovery synthesis. Extract the customer's process, the moment the problem bites, and the metrics that define "better".
2. Sketch the candidate solution forms — machine, software, service, hybrid. For each: what the customer does differently, what changes for them, what they stop paying for.
3. For the leading form, identify what it competes with: the incumbent solutions from the tech baseline plus the status-quo option ("keep doing what we do").
4. Write the one-page concept: the problem as the customer described it, the solution form, how it works at the level a smart outsider needs, what it competes with, and the single strongest reason it wins.
5. Flag the assumptions the concept rests on — these become the test list for Step 5a.

## Deliverable

`proseed/04-concept/concept-one-pager.md` — one page, literally. If `templates/` contains a template, use it.

Update `proseed/STATUS.md`.

## Red Flags

| Thought | Reality |
|---------|---------|
| "Obviously it's a machine" | Discovery decides the form. Check what customers actually asked for. |
| "Three pages is close enough to one" | The limit forces the choice. Cut until the core claim survives. |
| "The concept is what we always planned" | If discovery changed nothing, you weren't listening. |
| "Assumptions go in the footnotes" | Assumptions are Step 5a's test list. List them visibly. |

## Next

Invoke `proseed:feasibility` (Step 5a, Technical) — prove the concept works before anyone prices it.
