# Step 12 — Product Concept Design Report: H7 "PW-500" (v1 commercial product)

## The commercial product

**ProSeed PW-500**: skid-mounted continuous microwave pre-treatment module, 500 t/h nominal, retrofit-mounted on mill feed conveyor. Variants: PW-500 (single), PW-1500 (3-cell array for large concentrators).

## Exact costs (supplier-quoted; marked ~ where estimated)

| Cost block | Value | Basis |
|------------|-------|-------|
| RF power (8×100 kW magnetron generators + PSUs) | $1.9M | vendor quotes |
| Applicator cavities + enclosure | $0.6M | fabrication quote |
| Sensing + control (NIR, PLC, software) | $0.4M | BOM |
| Mechanical skid + install hardware | $0.3M | |
| Factory + site commissioning | $0.5M | crew + logistics ~ |
| **Build cost** | **$3.7M** | vs. 7b estimate $3.2M — +15%, flagged |
| Install (2 shutdowns, site labor) | $0.2M | |
| **Delivered cost** | **$3.9M** | |

## Installation & support approach

- **Install**: 2 planned shutdowns (~18 h total), conveyor splice-in; mechanical + electrical only, no mill modifications — honors the retrofit promise.
- **Commission**: 5 days, ore-calibrated on customer feed.
- **Support**: remote monitoring (dose, uniformity, uptime telemetry) + annual ore re-characterization; spares kit (2 magnetron tubes, PSU) stocked on site; <30 min tube swap, ≤4 h remote response.
- **Service contract**: $350k/yr — quarterly ore-panel refresh + dose-model updates (the database flywheel).

## Design readiness

| Area | Readiness |
|------|-----------|
| Mechanical/enclosure | Production-ready |
| RF power train | Ready — catalog industrial components |
| Applicator | Pilot-proven geometry; production tolerance review needed |
| Dose control | v1 feed-forward; closed-loop per-zone modulation = v1.5 firmware |
| Ore database ops | Process defined; tooling immature (manual for first 10 installs) |

## Remaining risk to Step 13 pricing

Support cost in remote geographies (logistics to mine sites) is under-modeled — service margin estimate may be optimistic until install base geography is known.
