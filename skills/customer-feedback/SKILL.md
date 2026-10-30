---
name: customer-feedback
description: Use when collecting and analyzing feedback on the installed product, validating real-world unit economics, identifying what must improve, or generating new requirements that loop back into design and engineering — Step 16 (Together)
---

# Step 16 — Customer Feedback / Next Version (Together)

## Purpose

Close the loop and open the next one. Understand what works, what does not, what must improve, and which new requirements and specifications the next version needs. The process doesn't end at a working product — it compounds.

## Inputs

- `proseed/15-product-development/` — the installed product, instrumentation, known issues
- `proseed/14-market-validation/` — what was promised vs. what was delivered
- `proseed/13-pricing-and-model/` — the economics to re-validate against reality

## Method

Together — commercial and technical both own this reading:

1. **Test the product in the field:** usage data, performance against spec in real conditions, failure modes, actual cost to serve.
2. **Discuss with users:** what they use, what they avoid, what broke, what they wish it did — observed behavior over stated preference.
3. **Validate unit economics with real numbers:** actual build cost, install cost, service cost, customer value delivered. Compare with the Step 13 model — the deltas are the truth about your assumptions.
4. **Synthesize what works, what doesn't, what must improve** — ranked by customer impact and economic impact, not by how interesting the fix is.
5. **Generate the new requirements and specifications** for Version N+1 — written in the same form Step 6 produces, because they re-enter the process at Step 10a.

## Deliverable

`proseed/16-customer-feedback/` — `feedback-report.md`: field results, user findings, real-vs-model economics, ranked improvement list, and the Version N+1 requirements document. If `templates/` contains templates, use them.

Update `proseed/STATUS.md`: bump the Version field; the loop restarts at 10a.

## Red Flags

| Thought | Reality |
|---------|---------|
| "Feedback is mostly positive" | Observe behavior. Users say nice things; usage data doesn't lie. |
| "Economics were validated at 13" | 13 used model costs. 16 has real ones. Rerun the comparison. |
| "List everything customers asked for" | Rank by impact. An unprioritized wishlist is not a requirements doc. |
| "Version 2 is a fresh start" | It's a loop: new requirements re-enter at 10a with all evidence attached. |

## Next

Loop: feed the new requirements into `proseed:design-and-engineering` (Step 10a) for Version N+1 — the process continues until the product is done evolving.
