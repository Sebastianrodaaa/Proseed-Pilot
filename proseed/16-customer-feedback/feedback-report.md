# Step 16 — Customer Feedback / Next Version: H7 → Version 2

## What works / what doesn't / what must improve

| Finding | Evidence | Impact rank |
|---------|----------|-------------|
| Throughput promise delivered (+17%) | 60-day plant data | — the reason they bought |
| Availability 92% vs 95% spec — dust ingress | 2 cell failures, 11 downtime hours | **1** — availability is table stakes |
| Energy −11% vs −14% bench (belt-edge uniformity) | Dose mapping vs bench | **2** — directly hits the value prop |
| Sensor drift on wet ore | Wet-season dose fallback | **3** — control quality |
| Operators use manual dose override constantly | SCADA logs | **4** — UX/automation gap we didn't anticipate |
| "Can it also handle our pebble-crusher recycle stream?" | Customer request ×3 | **5** — new application, easy adjacency |

## Economics: real vs. model (Step 13)

| Item | Model | Real | Delta |
|------|-------|------|-------|
| Build cost | $3.9M | $4.1M | +5% — site logistics |
| Service cost | $140k/yr | $210k/yr | +50% — remote-site support underestimated (12 flagged it) |
| Customer value (this install) | ~$8M/yr at +17% | ~$8.5M/yr realized | Customer delighted; payback <9 mo |

## Version 2 requirements (→ Step 10a, v2)

Written in Step-6 form — new spec lines for the v2 *cahier des charges*:

1. **Sealed waveguide feeds**, ≥98% availability target (dust-rated redesign)
2. **Edge-zone power compensation** — recover belt-edge uniformity (close the −3% energy gap)
3. **Drift-tolerant moisture/permittivity sensing** — gravimetric + NIR fusion
4. **Operator-grade dose UI** — their crews want manual authority with guardrails
5. **Recycle-stream option** — evaluate pebble/scats stream as second applicator position (H8 liberation upside also attaches here)
6. **Vendor-credibility fix** (from 14 loss log): pursue OEM channel partner for large-miner deals — a commercial requirement, lands in 13/14 rather than 10a

## Loop status

Version bumped to **2** in STATUS.md. Requirements 1–5 route to `proseed:design-and-engineering` (10a) for v2; requirement 6 routes to pricing/model review. The process continues — the machine is installed, learning, and feeding its own next version.
