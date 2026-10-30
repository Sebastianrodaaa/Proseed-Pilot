# Step 15 — Product Development: PW-500 Unit 001

## Build & install record

| Item | Result |
|------|--------|
| Unit | PW-500 s/n 001 — built to Step-12 spec, magnetron array, bypass-first skid |
| Site | Mid-tier gold operation (Step-14 contract) |
| Install | 2 planned shutdowns, 16 h total vs 18 h budget — splice-in went clean |
| Commission | 5 days; ore-calibrated on live feed |

## Spec verification on the installed system (their conditions, their ore)

| Spec | Target | Measured |
|------|--------|----------|
| Throughput uplift | ≥15% | **+17%** sustained 60-day average at same grind |
| Circuit energy reduction | ≥10% | **−11%** (below the ore-test −14% bench result — see feedback) |
| Dose | ≤3 kWh/t | 1.4 kWh/t steady-state |
| Availability | ≥95% | **92%** — see known issues |
| RF leakage | <5 mW/cm² | 2.1 mW/cm² at 1 m ✅ |
| Fail-safe trip | Works | Exercised twice in anger; mill ran untreated both times |

## Known issues list (feeds Step 16)

1. **Availability 92% not 95%** — waveguide dust ingress on 2 cells → unplanned cleaning stops. Sealing redesign needed.
2. **Energy saving −11% vs −14% bench** — dose uniformity degraded at belt edges on coarser size fractions.
3. Permittivity sensor drifts on wet-season ore → dose loop defaults to conservative (leaves uplift on the table).
4. Remote telemetry dropout on site satlink — buffering fix needed.

## IP applied (per Step 11)

Applicator + dose-control filings preceded site disclosure ✅; ore data handled under customer NDA; FTO search completed — design-around confirmed for the cavity geometry (narrow margin, documented).
