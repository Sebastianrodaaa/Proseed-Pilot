---
name: design-and-engineering
description: Use when launching the validated development roadmap — designing and engineering the requirements and specifications into the product after the move-forward decision — Step 10a (Technical)
---

# Step 10a — Requirements and Specifications Design & Engineering (Technical)

## Purpose

Execute the validated roadmap: turn the technical specification into a working design through engineering. This step also runs on the **version loop** — Step 16 feeds new requirements back here for Version 2 and beyond.

## Inputs

- `proseed/decision-gate.md` — the go decision and route
- `proseed/09b-requirements-validation/` — the *cahier des charges* and roadmap with budget
- On version loops (v2+): `proseed/16-customer-feedback/` — new requirements from the field

## Method

1. **Launch the roadmap as written** — milestones, budget, resources from 9b. If the plan needs changing, change it in the open and note why.
2. **Design to the spec, not beyond it.** Every engineered element traces to a requirement in the *cahier des charges*. Gold-plating burns the budget the gate approved for something else.
3. **Validate requirements in design and concept** as you go — design reviews against the spec, simulation, prototyping where the roadmap calls for it. Record which requirements are met at each design stage.
4. **Track budget and timeline against the roadmap** — the gate approved specific numbers; deviations are decision points, not footnotes.
5. **On version loops:** triage incoming requirements from Step 16 — which are spec changes, which are new requirements, which are noise — and fold them into a Version N+1 roadmap before engineering starts.

## Deliverable

`proseed/10a-design-engineering/` — design documents, requirement-by-requirement validation status, budget/timeline tracking vs. the roadmap. Version loops go in `v2/`, `v3/` subdirectories. If `templates/` contains templates, use them.

Update `proseed/STATUS.md` (and Version field on loops).

## Red Flags

| Thought | Reality |
|---------|---------|
| "While we're in there, let's also…" | Scope creep spends the gate's budget. New features route through requirements. |
| "The roadmap was indicative" | The gate approved it. Deviations are decisions — surface them. |
| "We'll validate at the end" | Validate in design. Late discoveries are the expensive kind. |
| "v2 feedback can just be patched in" | Triage first: spec change vs. new requirement vs. noise. |

## Next

Invoke `proseed:ip-strategy` (Step 11) — before the design is shown outside, decide what's protected.
