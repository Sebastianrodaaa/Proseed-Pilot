---
name: proseed-workflow
description: Use when starting a ProSeed validation, when you need to locate your position in the process, decide which step comes next, or understand how the 16 steps, parallel branches, iteration loops, and decision gate fit together
---

# ProSeed Workflow — The Master Map

You are the navigator for a 16-step hypothesis-validation process. Your job is to know where the project is, keep every step honest about its inputs and outputs, and route work to the right step skill.

The canonical process description lives in `references/proseed-hypothesis-validation-workflow.md`. When a step description here seems thin, read it.

## The Map

**Part 1 — Find the value proposition**

```text
1. Problem hypotheses (Together)
   → 2a. Market scan (Commercial) ‖ 2b. Tech baseline (Technical)   [parallel]
   → 3. Customer discovery (Commercial)
   → 4. Concept (Technical)
   → 5a. Feasibility (Technical) → 5b. Competition (Commercial)
   → 6. Customer requirements & specifications (Commercial)
   → 7a. Concept/req/spec assumptions (Technical) ‖ 7b. Unit economics (Commercial)   [iterate together]
   → 8. Value proposition (Together)
   → PART 1 COMPLETE
```

**Part 2 — Sell, build and learn**

```text
9a. Market traction (Commercial) ‖ 9b. Req/spec validation (Technical)   [parallel]
   → DECISION: MOVE FORWARD?
       ├─ Already met → skip to 12. Product concept design
       ├─ Develop    → 10a. Design & engineering (Technical) → 11. IP strategy
       └─ Trial      → 10b. Paid trials (Commercial) → 11. IP strategy
   → 12. Product concept design (Technical)
   → 13. Pricing and model (Commercial)
   → 14. Market validation (Commercial)
   → 15. Product development (Technical)
   → 16. Customer feedback / next version (Together)
   → new requirements loop back to 10a for Version 2
```

## Step → Skill Routing

| Step | Owner | Skill to invoke |
|------|-------|-----------------|
| 1 | Together | `proseed:problem-hypotheses` |
| 2a | Commercial | `proseed:market-scan` |
| 2b | Technical | `proseed:tech-baseline` |
| 3 | Commercial | `proseed:customer-discovery` |
| 4 | Technical | `proseed:solution-concept` |
| 5a | Technical | `proseed:feasibility` |
| 5b | Commercial | `proseed:competition` |
| 6 | Commercial | `proseed:customer-requirements` |
| 7a | Technical | `proseed:concept-assumptions` |
| 7b | Commercial | `proseed:unit-economics` |
| 8 | Together | `proseed:value-proposition` |
| 9a | Commercial | `proseed:market-traction` |
| 9b | Technical | `proseed:requirements-validation` |
| Gate | Decision | `proseed:move-forward-decision` |
| 10a | Technical | `proseed:design-and-engineering` |
| 10b | Commercial | `proseed:paid-trials` |
| 11 | Technical | `proseed:ip-strategy` |
| 12 | Technical | `proseed:product-concept-design` |
| 13 | Commercial | `proseed:pricing-and-model` |
| 14 | Commercial | `proseed:market-validation` |
| 15 | Technical | `proseed:product-development` |
| 16 | Together | `proseed:customer-feedback` |

## Artifact Conventions

All deliverables live under `proseed/` in the working project directory:

```text
proseed/
  STATUS.md                        # position tracker — always current
  01-problem-hypotheses/
  02a-market-scan/
  02b-tech-baseline/
  03-customer-discovery/
  04-concept/
  05a-feasibility/
  05b-competition/
  06-customer-requirements/
  07a-concept-assumptions/
  07b-unit-economics/
  08-value-proposition/
  09a-market-traction/
  09b-requirements-validation/
  decision-gate.md                 # decision record (written at the gate)
  10a-design-engineering/
  10b-paid-trials/
  11-ip-strategy/
  12-product-concept-design/
  13-pricing-and-model/
  14-market-validation/
  15-product-development/
  16-customer-feedback/
```

Each step skill names its deliverable file. Steps that run **per hypothesis** (1, 2a, 2b, and later fan-out work) produce **one filled template document per hypothesis** — not one merged report.

Where a `.dotx` template exists in the skill's `templates/` directory: copy it to a working `.docx`, replace every `[Remove when filled]` guidance block with content, keep the structure exactly — including the **Personal input** sign-off and the **Decision** checkboxes — then render the deliverable as **`.pdf`** (`scripts/docx_to_pdf.py` or Word/Pages export). The `.docx` stays as the editable master for rework decisions. That Decision block is a per-hypothesis micro-gate at every step; fill it honestly — "drop" is a legitimate outcome that stops wasted work downstream.

**Sources travel with claims.** Every market size, competitor spec, price point, and performance number carries a citation inside the deliverable. A sourced claim that turns out wrong is useful; an unsourced claim is a guess wearing a costume.

## STATUS.md

`proseed/STATUS.md` is the single source of truth for position. Initialize it when the project starts; every step skill updates it when its deliverable lands.

```markdown
# ProSeed Validation Status

- Project: <name>
- Current step: <e.g. 2b — tech baseline>
- Version: <1, 2, ... — increments each time Step 16 loops back>
- Updated: <date>

## Completed
| Step | Deliverable | Date |
|------|-------------|------|
| 1 | proseed/01-problem-hypotheses/problem-hypotheses.md | YYYY-MM-DD |

## In progress
<parallel branches currently open, e.g. 7a ↔ 7b iteration round 3>

## Decision gate
<not yet reached | outcome, date, and evidence pointer>

## Iteration log
<7a↔7b rounds, Step-16 feedback loops, what changed each round>
```

## PORTFOLIO.md — the multi-hypothesis board

`STATUS.md` tracks the live workstream; `proseed/PORTFOLIO.md` tracks the **whole slate**. Hypotheses move through the process at different speeds — one can be at Step 15 while others sit parked at Step 2. Update the portfolio whenever a hypothesis changes step or status, and whenever a micro-gate Decision is marked.

```markdown
# ProSeed Portfolio — <project name>

| Hypothesis | Step | Status | Note |
|------------|------|--------|------|
| H1 — <short name> | 2b | Live | one line of context |
| H2 — <short name> | — | Parked | why it's waiting |

## Dropped
| Hypothesis | Dropped at | Reason (evidence) | Date |
|------------|-----------|--------------------|------|
```

**Status values:** `Live` (actively being worked), `Parked` (deliverables exist, waiting on capacity or a decision), `Dropped` (killed by evidence — move to the Dropped table).

**The drop log is organizational memory.** Record where each hypothesis died, the evidence that killed it, and the date. It stops the company re-testing dead ideas a year later — a parked hypothesis can always come back, a dropped one needs new evidence first.

## Locating Yourself Mid-Flight

When there is no `proseed/STATUS.md` but work may already exist:

1. Look for `proseed/` directories, deliverable files, research docs, interview transcripts, Excel models, letters of interest — wherever your human partner keeps them.
2. Ask which steps have produced deliverables, not which steps were "done" — the artifacts are the truth.
3. Reconstruct STATUS.md from the evidence, note gaps where a step was claimed but no deliverable exists, and show it to your human partner before continuing.
4. A step with no deliverable is not done. Either produce the deliverable or record explicitly in STATUS.md why the step is considered satisfied (with evidence).

## Process Rules

- **Parallel branches are real parallel work.** 2a/2b, 7a/7b, and 9a/9b can run concurrently — with different people, or with subagents on separate artifacts. They rejoin only when both deliverables exist.
- **7a ↔ 7b is an iteration loop, not a sequence.** The concept assumptions and the economics constrain each other; expect several rounds. Log each round in STATUS.md.
- **The decision gate is a gate.** After 9a and 9b, invoke `proseed:move-forward-decision`. Nothing in steps 10a–15 happens before the gate records an outcome.
- **10b paid trials are part of the route, not an optional extra.** In markets where customers buy through pilots, trials are the commercial engine. Check Step 6's buying-process evidence before deciding whether the gate can route around them.
- **Step 16 loops back, it does not end.** Feedback generates new requirements; Version N+1 re-enters at 10a. Bump the Version field in STATUS.md.

## Red Flags

| Thought | Reality |
|---------|---------|
| "We're basically past step 3" | No deliverable, no pass. Check `proseed/` for the artifact. |
| "Let's just build the thing" | That is Step 15, and twelve steps of evidence precede it. |
| "The gate is a formality" | The gate exists to kill or redirect projects. Run `proseed:move-forward-decision` honestly. |
| "7a and 7b can be done once each" | They iterate. One pass means the economics probably don't close. |
| "We can do 9a and 9b in any order, or skip one" | Both deliverables are inputs to the gate. |
| "The template is optional" | Templates encode the expected shape of the deliverable. Use them. |
| "Unsourced numbers are fine for now" | For now becomes forever. Cite or mark as assumption. |
