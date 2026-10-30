---
name: pricing-and-model
description: Use when validating the final business model and price, setting margin on real costs, running final unit economics, or assessing financial needs — Step 13 (Commercial)
---

# Step 13 — Pricing and Model (Commercial)

## Purpose

Validate the final business model and price — with margin on real costs this time, not the Step 7b estimates. This produces the offer customers will see at Step 14 and the financial picture the company plans around.

## Inputs

- `proseed/12-product-concept-design/` — exact costs, installation and support costs
- `proseed/07b-unit-economics/` — the model to update from estimates to real
- `proseed/09a-market-traction/` and `proseed/10b-paid-trials/` — price signals and objections from real selling
- `proseed/05b-competition/` — competitor models and pricing

## Method

1. **Update the unit economics with real costs** — every estimate in the 7b model replaced by a 12 number. Watch what moves; the deltas are your earlier assumption errors, worth naming.
2. **Choose the business model:** equipment sale, lease, per-unit-of-output, service subscription, consumables — and combinations. The model the market accepts beats the model you prefer; check competitor models and Step-9a/10b signals.
3. **Set price and margin:** margin on real costs, positioned against the best alternative's total cost, tested against what trial and funnel signals say the market will pay.
4. **Assess financial needs:** working capital, production ramp, sales cycle length (Step 6 told you the timeline), cash-flow shape of the chosen model. A lease model finances very differently than a sale.
5. **Write the offer:** price, model, terms — what Step 14 takes to customers for the final test.

## Deliverable

`proseed/13-pricing-and-model/` — updated unit-economics model plus `pricing-model.md`: business model, price structure, margins, financial needs assessment, the offer. If `templates/` contains templates, use them.

Update `proseed/STATUS.md`.

## Red Flags

| Thought | Reality |
|---------|---------|
| "7b already gave us the price" | 7b priced estimates. 13 prices real costs. Rerun the model. |
| "Higher margin is always better" | Price is positioned against alternatives and payback. Greed kills conversions at 14. |
| "The model is our choice" | The market's buying structure (Step 6) decides which models it accepts. |
| "Financial needs are a later problem" | Cash shape differs by model. Assess before offering terms you can't fund. |

## Next

Invoke `proseed:market-validation` (Step 14, Commercial) — the offer meets the funnel.
