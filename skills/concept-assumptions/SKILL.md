---
name: concept-assumptions
description: Use when defining the concept assumptions, requirements and specifications ProSeed meets today or could reach, building the first technical roadmap, or identifying potential IP — Step 7a (Technical)
---

# Step 7a — Concept, Requirement and Specification Assumptions (Technical)

## Purpose

Define what ProSeed commits to: the concept assumptions, requirements, and specifications the technology meets today or could credibly reach — and when. This is the technical answer to Step 6's commercial requirements, and it iterates directly with the unit economics (7b).

## Inputs

- `proseed/06-customer-requirements/customer-requirements.md` — the customer's numbers
- `proseed/05a-feasibility/feasibility-report.md` — measured performance
- `proseed/02b-tech-baseline/tech-baseline.md` — assumed vs. measured map

## Method

Desk research and tests, with expert support:

1. For each customer requirement from Step 6, state where ProSeed stands: **met today** (with evidence), **reachable** (with development path and confidence), or **not reachable** (say so).
2. For reachable targets, estimate *when* — this becomes the roadmap's spine.
3. **Build the first roadmap:** milestones from current state to full spec, what each milestone costs in time and resources, and which assumptions must hold.
4. **Identify potential IP** as you go: novel mechanisms, process parameters, system designs worth protecting. Flag them now — Step 11 formalizes the strategy.
5. Feed the cost drivers to 7b: what the machine/service costs to build and run shapes whether the economics close. When 7b pushes back on cost or price, iterate — adjust spec, target, or timeline, and log the round in `proseed/STATUS.md`.

## Deliverable

`proseed/07a-concept-assumptions/` — a 1–2 page concept statement plus the first roadmap (`roadmap.md`): requirements met/reachable/not-reachable, milestones, cost drivers, IP flags. If `templates/` contains templates, use them.

Update `proseed/STATUS.md`, logging each 7a↔7b iteration round.

## Red Flags

| Thought | Reality |
|---------|---------|
| "We'll hit all the specs" | Claim it only with a development path. Otherwise it's a hope. |
| "The roadmap can wait for the spec" | The roadmap IS the deliverable — when each target becomes real. |
| "IP is a legal-team problem" | IP found late is IP lost. Flag as you define the concept. |
| "7a is done after one pass" | It iterates with 7b until spec, cost, and price agree. |

## Next

Iterate with `proseed:unit-economics` (7b). When both converge, invoke `proseed:value-proposition` (Step 8, Together).
