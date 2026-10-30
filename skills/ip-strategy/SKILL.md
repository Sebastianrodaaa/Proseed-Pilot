---
name: ip-strategy
description: Use when validating the IP mix, deciding what must be protected before it is shown, or working with experts on patents and documented trade secrets — Step 11 (Technical)
---

# Step 11 — IP Strategy (Technical)

## Purpose

Decide what must be protected before it is shown. By now the design embodies real know-how — some patentable, some better kept as trade secrets, some not worth protecting. Getting this wrong in either direction costs: filing late loses rights; showing early loses secrets.

## Inputs

- `proseed/10a-design-engineering/` — the design as engineered (plus IP flags from 7a)
- `proseed/07a-concept-assumptions/` — the original IP flags
- `proseed/08-value-proposition/value-proposition-onepager.md` — the defensibility claim this strategy must support

## Method

Work with experts — patent attorneys, IP counsel:

1. **Inventory the protectable:** mechanisms, process parameters, system designs, software, know-how in the design. Include the unglamorous parts — process windows and calibration methods are often the real moat.
2. **For each item choose the instrument:** patent (novel, detectable, worth the disclosure), trade secret (hard to reverse-engineer, keep documented internally), publication (defensive, prevents others patenting it), or nothing.
3. **Decide what must be protected BEFORE it is shown** — trials, demos, partner discussions, and Step 12's product design all expose the design. Sequence protection before exposure.
4. **Document trade secrets properly:** written down, dated, access-controlled. A trade secret that exists only in someone's head isn't an asset.
5. **Check the value proposition's defensibility claim** — does this strategy actually deliver the "stay ahead" period Step 8 asserted? If not, send it back.

## Deliverable

`proseed/11-ip-strategy/ip-strategy.md` — the IP inventory with chosen instruments, filing/protection actions with deadlines, and the show-nothing-before-protected list. If `templates/` contains a template, use it.

Update `proseed/STATUS.md`.

## Red Flags

| Thought | Reality |
|---------|---------|
| "We'll patent everything" | Patents disclose. Some know-how is worth more as a secret. |
| "IP can wait until launch" | Showing before protecting can destroy patentability. Sequence it. |
| "Trade secrets = don't write it down" | Undocumented secrets aren't defensible assets. Document, then restrict. |
| "Legal will handle it" | The inventory of what's novel is a technical judgment. Own your half. |

## Next

Invoke `proseed:product-concept-design` (Step 12, Technical).
