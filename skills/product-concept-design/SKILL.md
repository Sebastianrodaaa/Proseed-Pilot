---
name: product-concept-design
description: Use when completing the design of the commercial product or pilot — exact costs, installation and support approach, design readiness, and the final technical specification — Step 12 (Technical)
---

# Step 12 — Product Concept Design (Technical)

## Purpose

Complete the design of the commercial product or pilot: the thing that will actually be sold, at exact cost, with a defined installation and support approach. This is where "the technology works" becomes "here is the product, and here is what it costs to build and run".

## Inputs

- `proseed/09b-requirements-validation/` — the spec (direct input when the gate took the *already met* route)
- `proseed/10a-design-engineering/` — the engineered design (develop route)
- `proseed/11-ip-strategy/ip-strategy.md` — what can and cannot be shown in the product documentation
- `proseed/10b-paid-trials/` — field learnings to design in (when trials ran)

## Method

1. **Complete the commercial product design:** the final configuration a customer buys — hardware, software, service components, variants.
2. **Establish exact costs:** BOM, manufacturing, installation, commissioning, ongoing service — real numbers from suppliers and quotes, not estimates with asterisks. Step 13 builds margin on these; errors here corrupt pricing.
3. **Define the installation and support approach:** what installing one looks like (time, skills, site requirements), and how support works (response, spares, remote, on-site). Support economics belong in the cost model too.
4. **Assess design readiness:** what is production-ready, what remains engineering risk, what the pilot needs that the product won't.
5. **Produce the technical specification and report:** the complete product spec and a design report a manufacturer, partner, or investor can evaluate.

## Deliverable

`proseed/12-product-concept-design/` — the product technical specification plus `design-report.md`: exact costs, installation & support model, readiness assessment. If `templates/` contains templates, use them.

Update `proseed/STATUS.md`.

## Red Flags

| Thought | Reality |
|---------|---------|
| "Costs are roughly known" | Step 13 puts margin on these numbers. Rough corrupts everything downstream. |
| "Installation is the customer's problem" | Installation and support ARE the product in industrial sales. Design them. |
| "The pilot is the product" | Pilot shortcuts become production debt. Be explicit about readiness gaps. |
| "Document everything including the secret sauce" | Step 11 decided what's showable. Respect it in the spec. |

## Next

Invoke `proseed:pricing-and-model` (Step 13, Commercial) — they need your exact costs.
