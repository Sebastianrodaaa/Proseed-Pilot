---
description: Run the move-forward decision — weigh market traction and the validated roadmap, choose a route, write the decision record
---

Run the ProSeed decision gate for the live hypothesis.

1. Invoke `proseed:move-forward-decision` and follow it exactly.
2. Gather its inputs: the 9a traction evidence (`proseed/09a-market-traction/`), the 9b validated spec and budgeted roadmap (`proseed/09b-requirements-validation/`), and the unit economics (`proseed/07b-unit-economics/`).
3. Weigh traction against spend honestly — rank commitments (verbal < LOI < conditional < paid), check whether requirements are already met, and price the routes.
4. Write `proseed/decision-gate.md`: outcome (Already met / Develop / Trial / Iterate / Park / Kill), the evidence weighed, who decided, date, kill conditions, and what would change the answer.
5. Update `proseed/STATUS.md` and `proseed/PORTFOLIO.md` with the outcome and chosen route.
