---
name: unit-economics
description: Use when assessing whether the economics work for the final product versus the best existing solutions, or building and iterating the Excel unit-economics model — Step 7b (Commercial)
---

# Step 7b — Unit Economics (Commercial)

## Purpose

Determine whether the economics actually work: can ProSeed deliver the product at a cost and price that beats the best existing solutions for the customer AND sustains the business. A brilliant concept with broken economics is a hobby.

## Inputs

- `proseed/07a-concept-assumptions/` — cost drivers, roadmap, reachable specs (iterating in parallel)
- `proseed/06-customer-requirements/customer-requirements.md` — what customers pay for today and what they'd pay for
- `proseed/05b-competition/` — competitor prices and business models

## Method

Build an Excel model and iterate with the technical team on Step 7a:

1. **Customer-side value:** what the problem costs them today (from Steps 3 and 6) and what the ProSeed outcome is worth in their units — savings, yield, throughput, avoided losses.
2. **ProSeed-side economics:** cost to build and deliver one unit (or serve one customer), driven by 7a's cost structure — BOM, manufacturing, installation, service, overhead.
3. **Price vs. best alternative:** position against the best existing solution's total cost, not its sticker price — include consumables, service, energy, downtime.
4. **Payback for the customer:** industrial buyers think in payback periods. Compute it and compare with the buying expectations found in Step 6.
5. **Iterate with 7a.** When the model doesn't close, that's information: shrink the spec, change the cost structure, resegment the customer. Log each round in `proseed/STATUS.md`.
6. **Stress the assumptions:** sensitivity on the two or three inputs that swing the result. Know which single assumption the whole model rests on.

## Deliverable

`proseed/07b-unit-economics/` — the Excel model plus `unit-economics-summary.md`: per-unit economics, customer payback, comparison vs. best alternative, key sensitivities. If `templates/` contains templates, use them.

Update `proseed/STATUS.md`, logging each 7a↔7b iteration round.

## Red Flags

| Thought | Reality |
|---------|---------|
| "We'll figure out pricing later" | Unit economics IS the pricing foundation. Model now. |
| "Compare with the incumbent's price" | Compare with the incumbent's total cost to the customer. |
| "The model works if we assume X" | Write X in the assumptions. Unwritten assumptions kill deals at due diligence. |
| "One iteration is enough" | If spec, cost and price converged in one pass, you probably weren't honest. |

## Next

Iterate with `proseed:concept-assumptions` (7a). When both converge, invoke `proseed:value-proposition` (Step 8, Together).
