---
name: requirements-validation
description: Use when technically validating the requirements and specifications, producing the technical specification document (cahier des charges), or building the development roadmap with budget, resources, timeline and milestones — Step 9b (Technical)
---

# Step 9b — Concept, Requirement and Specification Validation (Technical)

## Purpose

Validate technically that the requirements and specifications the market demands are achievable — and produce the technical specification (*cahier des charges*) plus a real development roadmap: budget, resources, timeline, milestones. This is the technical input to the go/no-go gate.

## Inputs

- `proseed/07a-concept-assumptions/` — the reachable-spec assessment and first roadmap
- `proseed/06-customer-requirements/customer-requirements.md` — the spec to validate
- `proseed/05a-feasibility/feasibility-report.md` — proven vs. unproven performance

## Method

Run workshops with experts and companies:

1. **Re-validate each requirement** against current evidence: met, reachable with dated milestone, or unachievable. Anything that changed since 7a gets flagged — discovery has a way of adding requirements.
2. **Write the technical specification (*cahier des charges*):** the complete, buildable spec — performance targets, interfaces, environment, standards, constraints. This is what engineering will be held to.
3. **Build the development roadmap:** milestones, timeline, budget, and resources per milestone — concrete enough that the gate can weigh the spend against the market traction from 9a.
4. **External validation:** workshops with experts and partner companies to challenge the spec and roadmap. A spec only insiders reviewed is a spec with undiscovered blind spots.
5. **Cost the unknowns:** where validation depends on unresolved technical risk, name the experiment that resolves it and what it costs.

## Deliverable

`proseed/09b-requirements-validation/` — the technical specification (`cahier-des-charges.md`) and `development-roadmap.md` with budget, resources, timeline, milestones — plus workshop outputs. If `templates/` contains templates, use them.

Update `proseed/STATUS.md`.

## Red Flags

| Thought | Reality |
|---------|---------|
| "7a already covered this" | 7a estimated reachability; 9b validates it and prices the roadmap. Different bar. |
| "The roadmap needs no budget" | The gate weighs traction against spending. No budget, no gate decision. |
| "Experts slow us down" | A wrong spec costs more than a workshop. Bring them in. |
| "Round the budget up, safety first" | Inflated budgets kill viable projects at the gate too. Be accurate. |

## Next

When this step and `proseed:market-traction` (9a) are both complete, invoke `proseed:move-forward-decision` — the gate.
