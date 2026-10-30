---
name: feasibility
description: Use when validating that the proposed solution technically works, running or documenting a proof of concept, lab tests, software demos, or drawings — Step 5a (Technical)
---

# Step 5a — Feasibility (Technical)

## Purpose

Determine whether the proposed solution actually works. Not "should work in principle" — demonstrated. This is where assumed performance from the tech baseline becomes measured performance, or dies.

## Inputs

- `proseed/04-concept/concept-one-pager.md` — including its flagged assumptions
- `proseed/02b-tech-baseline/tech-baseline.md` — the metrics you must beat and which ProSeed numbers are still *assumed*

## Method

Validate the technology with a proof of concept:

1. Take the assumption list from the concept. Rank by kill-power: which assumption, if false, ends the concept?
2. Design the cheapest test that settles the highest-risk assumption — bench test, lab run, software prototype, simulation, drawing review. Start there.
3. Run it. Record conditions, setup, and raw results, not just conclusions.
4. Where applicable, collect the evidence: lab test reports, pictures, software, drawings.
5. Compare measured results against the incumbent baseline metrics. State plainly where ProSeed wins, ties, and loses.
6. Update the tech baseline's *assumed* entries to *measured* — or record the assumptions that failed and what that does to the concept.

## Deliverable

`proseed/05a-feasibility/feasibility-report.md` plus the evidence files (test reports, photos, code, drawings). The report states: assumptions tested, method, results vs. baseline, verdict per assumption, and what remains unproven. If `templates/` contains a template, use it.

Update `proseed/STATUS.md`.

## Red Flags

| Thought | Reality |
|---------|---------|
| "The physics obviously works" | The doc exists because obvious has failed before. Test it. |
| "Let's test what's easy to test" | Test what kills the concept if it's wrong. Easy is a trap. |
| "The test mostly worked" | Mostly is a result too. Record what failed and under which conditions. |
| "We'll document the setup later" | Undocumented tests can't be repeated or defended. Record as you go. |

## Next

Invoke `proseed:competition` (Step 5b, Commercial) — then `proseed:customer-requirements` (Step 6).
