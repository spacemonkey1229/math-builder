# Learning Goals — Free Money, With Strings

Bidirectional deliverable ↔ skill matrix. Run at `case-write` time per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — contribution ledger (own contribution, employer match, extra-dollar destination, per pay period and per year) | `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-how-to-convert-percents-to-numbers` |
| D2 — ten-year projected value per strategy, compound growth, exponent step shown | `advanced-operations-exponent-also-power`, `advanced-operations-how-to-evaluate-an-exponential-expression` |
| D3 — marginal-return table at the match-cap discontinuity | `calculus-instantaneous-rate-of-change` |
| D4 — total ten-year value comparison, dollar and percent margin, recommendation | `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number` |

**Forcing test applied to each row:** could a competent student produce this deliverable correctly
without ever performing the listed skill(s)?

- **D1** — no. Every line of the ledger is a percentage of salary (contribution rate, match rate)
  converted into a dollar amount. A student who cannot convert a percent to a number or find the
  percent of a number cannot produce a correct dollar figure for a single row.
- **D2** — no. "Ten-year projected value... using the compound-growth calculation... with the
  exponent step shown explicitly" is a direct instruction to evaluate an exponential expression
  (base = 1 + growth rate, exponent = number of compounding periods) — the deliverable's own text
  requires showing that step, not just a final number a calculator produced silently.
- **D3** — no. The deliverable is explicitly a rate-of-change comparison: the return earned on the
  marginal dollar just below the cap versus just above it. Naming *why* the rate changes abruptly
  at one specific point rather than gradually is exactly what the vocabulary term Instantaneous
  Rate Of Change describes (a rate evaluated at, and changing discontinuously around, a single
  point) — this is the case's central "free money, with strings" mechanism, not decoration.
- **D4** — no. Stating "the dollar and percent margin" between two totals is, by definition, an
  application of percent-of-a-number / percent-conversion to the D2 outputs; a student cannot state
  a percent margin without performing that computation.

## Claimed skills → deliverables (reverse direction)

| Claimed skill (spine id) | n (live, 2026-09-04) | Forced by |
|---|---|---|
| `advanced-numbers-percent` | 57 | D1, D4 |
| `advanced-numbers-how-to-find-the-percent-of-a-number` | 63 | D1, D4 |
| `advanced-numbers-how-to-convert-percents-to-numbers` | 18 | D1 |
| `advanced-operations-exponent-also-power` | 5 | D2 |
| `advanced-operations-how-to-evaluate-an-exponential-expression` | 5 | D2 |
| `calculus-instantaneous-rate-of-change` | 3 | D3 |

## LEARNING GOAL CHECK

```
deliverables: 4    claimed skills: 6    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Note on `new_coverage: 0`:** every claimed skill above already has `n >= 3` in
`readmodel/standards_spine.json` as of 2026-09-04 (confirmed live). This case is not being written
to close a skill-*count* gap — it is being written to close a **topic** gap (Taxes & tax-advantaged
accounts / employer match had zero published-case coverage; see `case.json.topic_gap_closed`) while
deliberately reinforcing three of the thinnest skills in the entire 437-skill spine
(`advanced-operations-exponent-also-power` and `advanced-operations-how-to-evaluate-an-exponential-expression`,
both n=5; `calculus-instantaneous-rate-of-change`, n=3 — see `case.json.reinforcement_note` for the
adjacent-skill check performed before settling on this set). Consistent with the disclosed-empty-
`new_coverage` precedent in `cases/the-two-offers/case.json`. Flagged explicitly so `case-readiness`
/ a human reviewer can confirm the empty array is intentional, not an oversight.
