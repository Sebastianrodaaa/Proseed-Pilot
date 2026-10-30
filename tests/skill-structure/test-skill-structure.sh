#!/usr/bin/env bash
# Validates plugin structure: every workflow step has a skill, every SKILL.md
# has valid frontmatter, and manifests parse.
set -uo pipefail

cd "$(dirname "$0")/../.."
FAIL=0

fail() { echo "FAIL: $1"; FAIL=1; }

# --- Required skills: meta + all workflow steps -------------------------------
REQUIRED=(
  using-proseed
  proseed-workflow
  problem-hypotheses market-scan tech-baseline customer-discovery
  solution-concept feasibility competition customer-requirements
  concept-assumptions unit-economics value-proposition
  market-traction requirements-validation move-forward-decision
  design-and-engineering paid-trials ip-strategy
  product-concept-design pricing-and-model market-validation
  product-development customer-feedback
)

for skill in "${REQUIRED[@]}"; do
  f="skills/$skill/SKILL.md"
  [ -f "$f" ] || fail "missing $f"
done

# --- Frontmatter checks on every SKILL.md -------------------------------------
for f in skills/*/SKILL.md; do
  dir="$(basename "$(dirname "$f")")"

  head -1 "$f" | grep -q '^---$' || fail "$f: frontmatter must start on line 1"
  name="$(sed -n 's/^name: //p' "$f" | head -1)"
  desc="$(sed -n 's/^description: //p' "$f" | head -1)"

  [ -n "$name" ] || fail "$f: missing name"
  [ -n "$desc" ] || fail "$f: missing description"
  [ "$name" = "$dir" ] || fail "$f: name '$name' != directory '$dir'"
done

# --- Manifests parse ----------------------------------------------------------
for j in .claude-plugin/plugin.json .claude-plugin/marketplace.json \
         .devin-plugin/plugin.json hooks/hooks.json; do
  python3 -m json.tool "$j" > /dev/null 2>&1 || fail "$j: invalid JSON"
done

# --- Hook plumbing ------------------------------------------------------------
[ -x hooks/run-hook.cmd ] || fail "hooks/run-hook.cmd not executable"
[ -x hooks/session-start ] || fail "hooks/session-start not executable"
grep -q 'using-proseed/SKILL.md' hooks/session-start \
  || fail "session-start does not inject using-proseed"
grep -q 'proseed/STATUS.md' hooks/session-start \
  || fail "session-start does not inject STATUS.md position"
grep -q 'proseed/PORTFOLIO.md' hooks/session-start \
  || fail "session-start does not inject PORTFOLIO.md position"
grep -q 'run-hook.cmd' hooks/hooks.json \
  || fail "hooks.json does not invoke run-hook.cmd"

# --- Slash commands ------------------------------------------------------------
for cmd in status next gate; do
  [ -f "commands/$cmd.md" ] || fail "missing commands/$cmd.md"
  grep -q '^description:' "commands/$cmd.md" \
    || fail "commands/$cmd.md missing description frontmatter"
done

# --- Workflow reference doc + provided deliverable templates ------------------
[ -f skills/proseed-workflow/references/proseed-hypothesis-validation-workflow.md ] \
  || fail "missing workflow reference doc"

for t in skills/problem-hypotheses/templates/*.dotx \
         skills/market-scan/templates/*.dotx \
         skills/tech-baseline/templates/*.dotx; do
  [ -f "$t" ] || fail "missing template: $t"
done

if [ "$FAIL" -eq 0 ]; then
  echo "All structure checks passed."
else
  exit 1
fi
