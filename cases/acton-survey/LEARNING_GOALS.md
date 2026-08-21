# Learning Goals — Acton Survey

Bidirectional deliverable ↔ skill matrix (case-write §10, LEARNING GOAL CHECK).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 population-and-sample description | statistics-and-probability-population, statistics-and-probability-sample, statistics-and-probability-sample-size, advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number |
| D2 condensed campus roster table | statistics-and-probability-population, measurement-ratio, advanced-numbers-percent, advanced-numbers-how-to-convert-numbers-to-percents |
| D3 SRS risk analysis (probability a campus is shut out) | statistics-and-probability-random, statistics-and-probability-simple-random-sampling, statistics-and-probability-combination |
| D4 stratified allocation table | statistics-and-probability-stratified-sampling, measurement-proportion, measurement-how-to-find-a-missing-amount-in-a-proportion, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value |
| D5 total call-time comparison | measurement-time, measurement-how-to-convert-between-units-of-time, basic-operations-addition, basic-operations-multiplication, basic-operations-how-to-add-multi-digit-numbers, basic-operations-how-to-multiply-any-two-numbers |
| D6 two visual displays | number-sense-bar-graph, statistics-and-probability-pie-chart |

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 22    new_coverage: 0 (legacy-conversion carve-out — see case.json.legacy_conversion_note)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied to each skill:**
- `population`/`sample`/`sample-size` — D1 cannot be written without stating the real 1,420-learner population and the 142-learner sample and their relationship.
- `percent` / `how-to-find-the-percent-of-a-number` — D1's "what percent of the population is 142" and D2's per-campus share both require it directly.
- `how-to-convert-numbers-to-percents` — D2's per-campus N_i/1,420 conversion.
- `random` / `simple-random-sampling` — D3 is impossible to write without defining what a simple random sample is and why it can miss a campus entirely.
- `combination` — the hypergeometric probability in D3 (Appendix C) is a ratio of combinations; a student cannot compute it without using $\binom{n}{k}$.
- `stratified-sampling` — D4 is the direct definition-in-practice of a stratified sample.
- `proportion` / `how-to-find-a-missing-amount-in-a-proportion` — D4's $n_i = 142 \times N_i/1{,}420$ is solving a proportion.
- `rounding` / `how-to-round-a-number-to-a-specified-place-value` — D4's largest-remainder reconciliation is rounding with a constraint.
- `time` / `how-to-convert-between-units-of-time` — D5 converts total minutes of calls into hours to check against the deadline.
- `addition` / `multiplication` (+ how-tos) — D5's arithmetic: summing 50 allocation values, multiplying calls × minutes.
- `bar-graph` / `pie-chart` — D6's two mandatory visual displays.

**new_coverage[] is legitimately empty.** All 22 claimed skills already had `n >= 1` in `readmodel/standards_spine.json` before this conversion — 4 of them (`sample`, `population`, `random`, `combination`) were already tagged directly to "Acton Survey" by the pre-pipeline corpus scan (`readmodel/legacy_readiness.json`), and the other 18 are common cross-case skills (percent, proportion, rounding, time, basic arithmetic, bar/pie chart) already covered by many published cases. Every one is genuinely forced by a deliverable above — none is padding. This is the same pattern as `cases/family-trip` (see its `new_coverage_note`), and the case-readiness Tier 1 legacy-conversion carve-out on T1-10 applies (a legacy case with `legacy_conversion_note` downgrades an honest empty `new_coverage[]` from BLOCKER to GAP).
