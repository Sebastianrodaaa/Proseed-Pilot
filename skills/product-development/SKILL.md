---
name: product-development
description: Use when developing the pilot unit, MVP, or first product — building and installing the working version the market validated — Step 15 (Technical)
---

# Step 15 — Product Development (Technical)

## Purpose

Build the pilot unit, MVP, or first product — a working version installed and running at a customer site or in production conditions. Contracts were signed on the promise; this step delivers it.

## Inputs

- `proseed/12-product-concept-design/` — the product spec, design report, installation approach
- `proseed/11-ip-strategy/ip-strategy.md` — the IP decisions to apply in the build
- `proseed/14-market-validation/` — who signed, and what they were promised

## Method

1. **Develop against the product spec** — the build target is the Step-12 specification, not the lab prototype and not the next version's wishlist.
2. **Apply the IP decisions:** what ships embodies the protection choices from Step 11 — in design, in documentation, in what the customer can inspect.
3. **Build for installation, not demonstration:** the deliverable works in the customer's environment, with their operators, under real load. A demo unit that needs an engineer babysitting it is not a product.
4. **Install and commission:** execute the installation approach defined in Step 12; record what it actually cost in time and effort vs. plan.
5. **Verify the running system against the spec:** the requirements the customer signed for, measured in their conditions.
6. **Instrument for feedback:** Step 16 needs data — what's used, what breaks, what operators do. Build the logging, access, and relationships that let learning happen.

## Deliverable

`proseed/15-product-development/` — build records, installation & commissioning report, spec-verification results from the installed system, known issues list. The product itself ships. If `templates/` contains templates, use them.

Update `proseed/STATUS.md`.

## Red Flags

| Thought | Reality |
|---------|---------|
| "The prototype basically works, ship it" | Prototype shortcuts become installed-base debt. Build to spec. |
| "It works in our facility" | The spec is measured in THEIR conditions. Verify on site. |
| "Feedback can be collected informally" | Instrument now. Retrofitting data collection never happens. |
| "IP was last month's topic" | What ships discloses. Recheck the IP list before delivery. |

## Next

Invoke `proseed:customer-feedback` (Step 16, Together) — the installed product starts generating the requirements for Version 2.
