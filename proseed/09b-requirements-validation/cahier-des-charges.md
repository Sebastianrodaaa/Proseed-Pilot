# Step 9b — Technical Specification (Cahier des Charges): H7 Pre-Treatment Unit

## Product: continuous microwave pre-treatment module, v1

### Performance
| Spec | Target | Basis |
|------|--------|-------|
| Throughput per module | 500 t/h nominal (arrayable to 1,500+) | Std. conveyor widths; 7a M5 |
| Comminution energy reduction | ≥10% circuit-level, verified per-ore | Step 6 must-have |
| BWi reduction on qualified ores | ≥10% | Pilot data −3..−30%, conservative floor |
| Dose | 0.5–3 kWh/t, closed-loop controlled | Pilot range + 7a M3 |
| Availability | ≥95% (n+1 generator redundancy) | Step 6 table stakes |
| Fail-safe | Mill runs untreated on module trip | Non-negotiable retrofit requirement |

### Interfaces
- Bolt-on to existing feed conveyor ahead of primary mill; ≤2 planned shutdowns for install
- Belt-width applicator, uniform ±10% field across full width
- Ore feed: ≤150 mm top size, moisture 0–8%

### Environment & compliance
- Zone 22 dust-rated enclosure; IP65; −20..+50 °C
- ISM-band emission limits (CISPR 11 / IEC 60519 analogs); RF leakage <5 mW/cm² at 1 m
- Remote telemetry: dose, field uniformity, ore-property estimate, uptime

### Constraints (the engineering that must be true)
- Multi-magnetron array with per-zone power modulation (the control differentiator)
- Inline sensing: belt-speed + moisture + permittivity proxy for dose loop
- Magnetron tube life ≥8,000 h at derated duty; hot-swap replacement <30 min
