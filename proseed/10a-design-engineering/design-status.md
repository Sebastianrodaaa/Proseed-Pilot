# Step 10a — Design & Engineering Status: H7 (Version 1)

**Scope released:** Tranche 1 (M1 ore panel + M2 applicator) per `decision-gate.md`. Tranche 2 (M3–M5) gated on 10b trial signal.

## Requirement-by-requirement validation

| Cahier des charges spec | Design status | Evidence |
|------------------------|---------------|----------|
| 500 t/h per module | 🟡 In design | Multi-cavity array of 4×125 t/h cells; sim-verified geometry |
| ±10% field uniformity, full belt width | 🟡 Sim-verified | FDTD model: ±8% on 1.2 m belt; cold mockup pending |
| Closed-loop dose 0.5–3 kWh/t | ⏳ Tranche 2 | Sensor selection: NIR moisture + belt-load + permittivity probe |
| ≥95% availability | 🟡 Design intent | n+1 magnetron redundancy; derated 70% duty; hot-swap drawer |
| Fail-safe bypass | ✅ In design | Module trips → belt feeds mill untreated; no interlock risk |
| Zone 22 dust / IP65 | 🟡 In design | Standard mining enclosure package |
| RF leakage <5 mW/cm² | 🟡 Sim-verified | Choke + absorber tunnel ends; mockup measurement pending |
| ≤2-shutdown install | ✅ By design | Skid-mounted, conveyor splice-in points only |

## Budget/timeline vs. roadmap

Tranche 1 tracking on plan: M1 lab work 60% done (ore panel: 4/8 bodies mapped, all ≥10% BWi response so far — kill condition 1 currently safe), M2 applicator sim complete, cold mockup queued.

## Design decisions taken (and why)

1. **Magnetron array over solid-state** for v1: cost/kW is 5–8× lower at this power class; solid-state revisited in v2 (control bandwidth would simplify M3).
2. **Modular cavity architecture**: 125 t/h cells arrayed across belt width — uniformity scales by adding cells, not by bigger fields (the scaling insight that kills assumption-1 risk).
3. **Bypass-first mechanical design**: the module can never block the mill — the retrofit promise that gets us past plant-manager veto.

## Open engineering risks

- Dust ingress into waveguide feeds (sealing design under test)
- Permittivity sensor drift on wet ore — fallback: gravimetric moisture + feed-forward dosing
