---
name: move-forward-decision
description: Use at the decision gate after Steps 9a and 9b — weighing market traction against development spend, choosing between the already-met, develop, or paid-trial route, or deciding whether to proceed at all
---

# Decision — Move Forward? (Gate)

## Purpose

The one hard gate in the process. Assess whether market traction justifies the spending, and whether requirements and specifications are already met. Everything downstream — engineering budget, IP work, product development — commits real money. This is where an honest "no" or "not yet" saves the company.

## Inputs

- `proseed/09a-market-traction/` — LOIs, commitments, funnel conversion
- `proseed/09b-requirements-validation/` — validated spec, roadmap with budget
- `proseed/07b-unit-economics/` — whether the economics held

## Method

Together — this decision is owned by no single track:

1. **Weigh traction against spend.** Lay the commitment evidence (LOIs, paid interest, funnel conversion) next to the roadmap budget and timeline. Is the committed demand worth the spend?
2. **Check what the spec already satisfies.** If requirements and specifications are already met — the technology delivers what the market demands today — there is nothing to engineer. Route directly to Step 12.
3. **Choose the route:**

   | Route | When | Next step |
   |-------|------|-----------|
   | **Already met** | Specs already satisfied | → Step 12, `proseed:product-concept-design` |
   | **Develop** | Engineering needed to reach spec | → Step 10a, `proseed:design-and-engineering` |
   | **Trial** | Market or technical uncertainty remains | → Step 10b paid trials alongside the route |

4. **Also valid outcomes:** iterate (back to a specific earlier step, named), park, or kill. A gate that can only say "go" is not a gate.
5. **Write the decision record:** outcome, the evidence weighed, who decided, date, and what would change the answer.

## Deliverable

`proseed/decision-gate.md` — the decision record. Update `proseed/STATUS.md` with the outcome and chosen route.

## Red Flags

| Thought | Reality |
|---------|---------|
| "We've come this far, we go on" | Sunk cost. The gate weighs traction vs. spend, not effort spent. |
| "The LOIs will become orders" | Rank commitments honestly — verbal interest ≠ signature. |
| "Specs are close enough to met" | Check the validated spec, not vibes. "Close" routes to 10a, not 12. |
| "A kill decision is a failure" | Killing a weak project here is the method working. Record it cleanly. |

## Next

Route per the decision record: `proseed:design-and-engineering` (10a), `proseed:paid-trials` (10b), or `proseed:product-concept-design` (12).
