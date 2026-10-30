---
description: Show where the ProSeed validation stands — reads proseed/STATUS.md and proseed/PORTFOLIO.md and reports position, open work, and the next action
---

Report the current state of the ProSeed validation in this project.

1. Read `proseed/STATUS.md` and `proseed/PORTFOLIO.md` in the working directory.
2. If neither exists, say so and suggest initializing via `proseed:proseed-workflow`.
3. Report, in under 20 lines:
   - which hypotheses are Live / Parked / Dropped (from PORTFOLIO.md)
   - current step and version for each live workstream (from STATUS.md)
   - what's in progress or blocked
   - the single next action
4. If the files look stale — deliverables exist in `proseed/NN-step/` that aren't logged — flag the discrepancy instead of trusting the ledger blindly.
