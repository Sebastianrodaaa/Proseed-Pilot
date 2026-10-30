---
name: using-proseed
description: Use when starting any conversation - establishes how to find and use the ProSeed hypothesis-validation skills, requiring skill invocation before ANY validation work including research, drafting, or analysis
---

<SUBAGENT-STOP>
If you were dispatched as a subagent to execute a specific task, ignore this skill.
</SUBAGENT-STOP>

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a ProSeed skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

## What This Plugin Is

ProSeed is a hypothesis-validation method for industrial innovation. It runs a technology idea through 16 steps in two parts:

- **Part 1 — Find the value proposition (Steps 1–8):** prove the problem is real, the market exists, the technology can beat the incumbent, and the economics work.
- **Part 2 — Sell, build and learn (Steps 9–16):** convert validation into commitments, engineer the product, close contracts, ship a working version, and feed learning back into the next iteration.

Work alternates between a **Commercial** track, a **Technical** track, and **Together** steps, with parallel branches, iteration loops, and one hard decision gate.

## The Rule

**Invoke the skill for the step you are on BEFORE doing the work** — including desk research, drafting hypotheses, sizing markets, planning interviews, or building models. If it turns out wrong for the situation, you don't have to use it.

Then announce "Using proseed:[skill] to [purpose]" and follow the skill exactly. If it has a checklist, create a todo per item.

## Finding Where You Are

The process is stateful and can span months. Do not guess your position:

1. Look for `proseed/STATUS.md` (the live workstream) and `proseed/PORTFOLIO.md` (the whole hypothesis slate) in the working directory.
2. If they exist, read them, then invoke the skill for the current step.
3. If they don't, invoke `proseed:proseed-workflow` — it shows the full map, helps you locate your position from the evidence that exists, and initializes both files.

## Skill Priority

Process skills come first — they set the approach — then step skills carry it out:

- "Where are we / what do we do next / start a validation" → `proseed:proseed-workflow` first.
- Doing the work of a specific step → the step's skill (`proseed:market-scan`, `proseed:unit-economics`, etc.).

## Red Flags

These thoughts mean STOP — you're rationalizing:

| Thought | Reality |
|---------|---------|
| "This is just a quick market question" | Quick research is still step work. Invoke the step skill. |
| "I know roughly which step we're in" | Read `proseed/STATUS.md`. Roughly is not enough. |
| "I can answer from general knowledge" | Steps require sourced deliverables. Invoke the skill, do the method. |
| "The step is overkill for this question" | If a skill exists for it, use it. |
| "I'll just sketch the economics quickly" | Unit economics is Step 7b. Invoke `proseed:unit-economics`. |
| "We're past the early steps, we don't need them" | Skipped steps produce unvalidated claims. Record evidence in STATUS.md or do the step. |
| "I remember this skill" | Skills evolve. Read the current version. |
| "Let me gather context first" | The step skill tells you HOW to gather. Invoke it first. |

## User Instructions

User instructions (CLAUDE.md, AGENTS.md, direct requests) take precedence over skills, which in turn override default behavior. Only skip skill workflows or instructions when your human partner has explicitly told you to.
