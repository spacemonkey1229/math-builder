# Learning Goals — How Long Can We Last

Bidirectional deliverable ↔ skill matrix. Run at `case-write` time per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — essential-expense percent breakdown | `advanced-numbers-percent`, `advanced-numbers-how-to-convert-numbers-to-percents` |
| D2 — Julian's typical monthly freelance income, derived from a part and a percent | `advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole`, `advanced-numbers-how-to-find-the-percent-of-a-number` |
| D3 — dollar size of both fund options via a proportion | `measurement-ratio`, `measurement-proportion`, `measurement-how-to-find-a-missing-amount-in-a-proportion` |
| D4 — survival test: months of coverage and percent of the dry spell each fund covers | `measurement-how-to-find-a-missing-amount-in-a-proportion`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-how-to-convert-numbers-to-percents` |

**Forcing test applied to each row:** could a competent student produce this deliverable correctly
without ever performing the listed skill(s)?

- **D1** — no. Identifying "what percent of the total is housing" requires converting a dollar
  amount into a percent of a whole; there is no way to answer "which category is largest, as a
  share of the budget" without that conversion.
- **D2** — no, and this is the case's deliberately central deliverable for the thinnest skill in
  the group. The case never states Julian's typical monthly income directly — only his slow-month
  invoice total ($756) and that figure's percent of a typical month (21%). A student who cannot
  find a whole given a percent and a part cannot produce a numeric answer at all here, only a
  guess. (A student could compute $756 ÷ 0.21 by rote without understanding *why* that operation
  answers the question — the Socratic discussion's Anchor 3, see `FACILITATOR.md`, is built to
  surface that distinction.)
- **D3** — no. Both fund sizes are explicitly required to be shown "using a proportion" in
  Challenge 3's own text; a bare dollar total with no proportion shown does not satisfy the
  deliverable as written, and setting up dollars-per-month-of-coverage scaled to a target number of
  months is exactly what a proportion is for.
- **D4** — no. "How many months of coverage does $17,622 provide against a $2,891/month shortfall"
  is precisely a missing-amount-in-a-proportion problem (months is the unknown), and converting
  that months figure into "what percent of the 7-month stretch" requires the percent-of-a-number
  and percent-conversion skills a second time, applied to a genuinely different unit (months
  covered vs. dollars) than D1 used.

## Claimed skills → deliverables (reverse direction)

| Claimed skill (spine id) | n (before this case) | Forced by |
|---|---|---|
| `advanced-numbers-percent` | 57 | D1 |
| `advanced-numbers-how-to-convert-numbers-to-percents` | 38 | D1, D4 |
| `advanced-numbers-how-to-find-the-percent-of-a-number` | 63 | D2, D4 |
| `advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole` | 2 | D2 |
| `measurement-ratio` | 25 | D3 |
| `measurement-proportion` | 17 | D3 |
| `measurement-how-to-find-a-missing-amount-in-a-proportion` | 10 | D3, D4 |

## LEARNING GOAL CHECK

```
deliverables: 4    claimed skills: 7    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Note on `new_coverage: 0`:** every claimed skill above already has `n >= 2` in
`readmodel/standards_spine.json` as of 2026-09-04 (confirmed live). This case is not being written
to close a skill-*count* gap — it is being written to close a **topic** gap (cash-flow/money-
mechanics: how big an emergency fund should be, and why 3-6 months is a range and not a round
number — see `case.json.topic_gap_closed`), while also reinforcing the two thinnest skills in the
Advanced Numbers/Measurement group it draws from: `advanced-numbers-how-to-find-a-whole-given-
the-percent-and-the-part-of-the-whole` (n=2, the thinnest skill in the entire spine) and
`measurement-how-to-find-a-missing-amount-in-a-proportion` (n=10). This is flagged explicitly, per
the precedent in `cases/the-two-offers/LEARNING_GOALS.md`, so `case-readiness`/a human reviewer can
confirm the empty array is an intentional topic-gap-plus-reinforcement case, not an oversight.
