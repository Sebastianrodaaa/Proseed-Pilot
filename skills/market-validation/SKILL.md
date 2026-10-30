---
name: market-validation
description: Use when testing whether customers will sign the final offer, converting the sales funnel, or securing contracts — Step 14 (Commercial)
---

# Step 14 — Market Validation (Commercial)

## Purpose

The final commercial test: will customers sign the final offer? Not "are they interested" — Step 9a answered that. This is signatures: finalized terms, converted funnel, contracts.

## Inputs

- `proseed/13-pricing-and-model/` — the offer: price, model, terms
- `proseed/09a-market-traction/` — the funnel and the most-interested customers
- `proseed/10b-paid-trials/` — trial customers, the warmest prospects
- `proseed/06-customer-requirements/customer-requirements.md` — buying process and timeline per segment

## Method

1. **Take the offer to the funnel**, warmest first: trial customers, committed LOIs, then the broader pipeline.
2. **Sell for signature.** The question changed from "would you?" to "will you, on these terms?" Expect the objections that only surface when money is real — contract terms, liability, service level, delivery dates.
3. **Convert the funnel:** track stage-by-stage conversion. Where prospects stall is diagnostic — price, terms, spec gaps, or wrong segment.
4. **Secure contracts.** The deliverable metric is signed commitments, not pipeline size.
5. **Record every loss with its reason.** Lost deals at this stage are the most expensive and most instructive data you own — they feed Step 16 and the next iteration's requirements.

## Deliverable

`proseed/14-market-validation/` — `validation-report.md`: conversion per funnel stage, contracts secured, objection and loss log with reasons, and the verdict — does the market sign at this price and model? If `templates/` contains templates, use them.

Update `proseed/STATUS.md`.

## Red Flags

| Thought | Reality |
|---------|---------|
| "They're very positive about the offer" | Positive is not signed. The metric is contracts. |
| "They'll sign once the product exists" | Maybe. Record it as conditional, not validation. |
| "We lost on price, cut it" | Diagnose first — loss reasons are rarely just price. Log before acting. |
| "Enough interest, let's build" | Step 14's bar is signatures. Interest was Step 9a's bar. |

## Next

Invoke `proseed:product-development` (Step 15, Technical) — build the thing they signed for.
