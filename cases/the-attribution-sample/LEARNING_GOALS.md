# LEARNING_GOALS.md — The Attribution Sample

Bidirectional deliverable ↔ skill matrix (SPEC §7 / case-write step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Pooled Random Sample precision table (per-channel standard error) | statistics-and-probability-simple-random-sampling, statistics-and-probability-sample-size |
| D2 — Channel-Stratified Sample design (minimum floor + proportional remainder) | statistics-and-probability-stratified-sampling, statistics-and-probability-sample-size |
| D3 — Analyst-hours cost table, compared to the weekend budget | statistics-and-probability-sample-size, advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 — Primary-metric comparison (pooled SE ÷ hours, both options) | statistics-and-probability-simple-random-sampling, statistics-and-probability-stratified-sampling, advanced-numbers-percent |
| D5 — Recommendation memo, defended with D1-D4 | statistics-and-probability-population, statistics-and-probability-sample |

**Forcing test applied:** *could a competent student produce this deliverable correctly without
ever performing this skill?* For each mapping above, no — D1 cannot be produced without actually
computing √(p(1−p)/n) for each channel's *expected* simple-random-sample count, which requires
understanding what a simple random sample's per-stratum yield looks like in expectation; D2
requires the student to actually design a stratified allocation (apply a minimum floor, then
allocate the remainder proportionally) rather than just being handed the numbers; D3 requires
converting sample counts into verification time via a per-channel rate and comparing the total
against a stated budget (a real percent/rate application); D4 requires combining D1/D2's
channel-level results into the *pooled* standard error (a weighted combination across strata, not
just averaging) and dividing by D3's hours — a student who never engaged with why a small stratum's
poor estimate barely moves the *pooled* number, yet dominates the *channel-level* one, cannot
correctly interpret this deliverable; D5 requires weighing D4's numeric winner against D1/D2's
channel-level precision gap and D3's budget fit — a student who never engaged with what "sample"
and "population" mean in this context (is Derek's report about the *pooled population* of clicks,
or about *each channel's own population*?) cannot write a defensible memo.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 8    new_coverage: 0 (reinforcement — see note below)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**new_coverage note.** All 8 claimed skills (`statistics-and-probability-simple-random-sampling`,
`statistics-and-probability-stratified-sampling`, `statistics-and-probability-multistage-sampling`,
`statistics-and-probability-sample-size`, `statistics-and-probability-sample`,
`statistics-and-probability-population`, `advanced-numbers-percent`,
`advanced-numbers-how-to-find-the-percent-of-a-number`) already show `n>=1` in
`readmodel/standards_spine.json` before this case (simple-random-sampling n=4,
stratified-sampling n=3, multistage-sampling n=1, sample-size n=6, sample n=6, population n=8,
percent n=54, how-to-find-the-percent-of-a-number n=59). `new_coverage[]` is set to `[]` per SPEC
§4's literal rule (a skill already at `n>=1` cannot be claimed as newly-closed), and `case.json`
carries a `reinforcement_note` explaining that this case exists to *reinforce* the case's actual
comparison (simple random sampling vs. stratified sampling) and to thicken the one genuinely thin
skill in the Sampling And Experiments group — `multistage-sampling` (n=1) — which is touched here
as a contrasting vocabulary term (case.md Appendix H) rather than a computed deliverable, per the
source concept write-up's own framing (`CONCEPTS_pim-sector-gaps_2026-08-24.md`, C8). This mirrors
the disclosed, deliberate reinforcement-pass precedent set by `cases/prove-it-scales/case.json` —
flagged for `case-qa` to confirm rather than silently treated as a normal zero-new-coverage case.
