---
description: Determine the next ProSeed step and run it — reads position, applies the process rules, and invokes the right step skill
---

Work out what comes next in this ProSeed validation and do it.

1. Read `proseed/STATUS.md` and `proseed/PORTFOLIO.md`.
2. If neither exists, invoke `proseed:proseed-workflow` to locate position first.
3. Apply the process rules to find the next step for the live hypothesis(es): parallel branches (2a‖2b, 7a↔7b, 9a‖9b) may mean more than one open thread; the decision gate and Step-16 version loop change the route.
4. State the next action(s) in one line each, then invoke the matching step skill (`proseed:<step-skill>`) and do the work.
5. Update `proseed/STATUS.md` and `proseed/PORTFOLIO.md` when deliverables land.
