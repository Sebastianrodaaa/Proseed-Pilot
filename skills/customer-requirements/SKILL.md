---
name: customer-requirements
description: Use when defining the conditions a solution must satisfy, the properties customers expect, and how customers buy — who decides and the buying timeline — Step 6 (Commercial)
---

# Step 6 — Customer Requirements and Specifications (Commercial)

## Purpose

Define the conditions the solution must satisfy and the properties customers expect — in the customers' words and units. This is the commercial half of the spec: what the market demands before it will pay, and how the buying decision actually happens.

## Inputs

- `proseed/03-customer-discovery/` — transcripts, buying maps
- `proseed/05b-competition/` — what competing solutions already satisfy
- `proseed/05a-feasibility/feasibility-report.md` — what ProSeed can plausibly deliver

## Method

1. **Talk to buyers and decision-makers**, not just users — Step 3 mapped who they are. Users describe what hurts; buyers describe what they'd sign for.
2. **Collect requirements as conditions:** throughput, quality spec, footprint, energy, integration, certifications, service expectations, payback expectations. Each with the customer's number, not your estimate.
3. **Separate must-haves from nice-to-haves** — and note who insisted on each. A requirement only the reseller cares about is still a requirement.
4. **Map the buying process per segment:** who initiates, who specifies, who signs, who can veto, typical timeline, budget cycle, and what proof they need before signing (trials, references, certifications).
5. **Compare with competing solutions:** for each requirement, note whether incumbents meet it — requirements nobody meets are your opening; requirements everyone meets are table stakes.

## Deliverable

`proseed/06-customer-requirements/customer-requirements.md` — the requirements list with customer numbers, must/nice grading, the buying process map per segment, and the competitive coverage comparison. If `templates/` contains a template, use it.

Update `proseed/STATUS.md`.

## Red Flags

| Thought | Reality |
|---------|---------|
| "We know what they need from the interviews" | Users described pain. Ask buyers what they'd sign for. |
| "Requirements are qualitative" | A spec without numbers is a wish. Get the customer's numbers. |
| "The decision-maker is who we talk to" | It rarely is. Map initiator, specifier, signer, veto. |
| "Timeline doesn't matter yet" | An 18-month buying cycle changes everything about Part 2. |

## Next

The fork: `proseed:concept-assumptions` (7a, Technical) and `proseed:unit-economics` (7b, Commercial) run as an **iteration loop** — neither is finished until both agree.
