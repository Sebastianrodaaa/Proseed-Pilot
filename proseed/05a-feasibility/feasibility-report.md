# Step 5a — Feasibility Report: H7

**Question:** Does a continuous microwave pre-treatment unit for ore comminution actually work?

## Assumption test results (ranked by kill-power)

| # | Assumption | Evidence | Verdict |
|---|------------|----------|---------|
| 3 | Dielectric advantage holds across ore bodies | **Published measured data**: Palabora Cu BWi 13.06→9.2 kWh/t (10 s, 2.6 kW); Nottingham pilot A*b −7–14%, BWi −3–9% across tested ores at 10–150 t/h. Ore-dependence is real but the response direction is consistent. | ✅ Supported — must extend per-ore (see test list) |
| 1 | Dose uniformity at plant throughputs | Pilot ran continuous 10–150 t/h belt feed (published). Scaling to 1,000+ t/h is applicator engineering: multi-cavity arrays, belt geometry — MicroHammer claims a 150 t/h demo scalable to 3,000 t/h. | 🟡 Plausible — the core engineering risk |
| 5 | No downstream penalty | No published evidence of flotation/selectivity harm; some evidence of *improved* liberation (feeds H8). Liner-wear neutral (same grinding media). | 🟡 Indicated positive — needs ore-specific confirmation |
| 2 | Closed-loop dose control vs. ore variability | Unpublished — no public reference. Dielectric response varies with moisture/mineralogy; control needs inline NIR/permittivity sensing. | ⚠️ Unproven — must be built & tested |
| 4 | Hardware cost inside payback | Depends on magnetron vs. solid-state supply at ~1–3 MW cumulative power. No public capex figure for plant-scale MW. | ⚠️ Unproven — priced in Step 7b sensitivity |

## Verdict

**Feasible with named engineering risks.** The physics is published, piloted, and replicated at industrially-relevant throughputs by independent groups — unusually strong evidence for this stage. What remains is engineering (uniformity, control, enclosure/ATEX-adjacent dust handling) and per-ore verification — both testable, neither fundamental.

## Test program the report prescribes (input to Steps 7a/9b)

1. **Ore panel** — dielectric loss factor vs. temperature for 5–8 target ore bodies (customer-supplied samples). Kill-test for assumption 3.
2. **Bench continuous run** — BWi before/after at 3 dose levels on top-3 ores. Confirms the dose-response curve used for sizing.
3. **Applicator simulation + cold mockup** — field uniformity across belt width at target throughput. De-risks assumption 1 before steel.
4. **Downstream check** — standard flotation response on irradiated vs. control samples. Closes assumption 5.

## Evidence files

Sources carried in `proseed/research/h7-mining-ore-weakening.json` and `proseed/02b-tech-baseline/sources.md`. Note: all measured figures here are **third-party published data** (Nottingham, SAIMM, UQ) — ProSeed's own trial data does not yet exist; the test program above creates it.
