# SCORE — maya-w · catering

**Status:** `machine-first-pass` · **Scored:** 2026-08-09 · **Tier:** T2

> **INTERIM.** This is a machine first pass, not a verdict. It does not count toward a badge and renders as INTERIM on the dashboard until a guide confirms it. Machine drafts, human promotes.

## The two outputs — never averaged

| | |
|---|---|
| **Mastery gate** — badge eligible? | **NO** — blocked on C3 |
| **Growth score** (0–100, guide-only, never a grade) | **62.0** |

All-Proficient scores 70. The score tracks trajectory; the gate tracks readiness. If a learner asks what their score is, the answer is that it is a tool for their guide, and the number that matters is which criteria are still Not Yet.

## Surface to the guide first — LOW confidence on C2, C3, C7

## The seven criteria

| | Criterion | Weight | Verdict | Confidence |
|---|---|---|---|---|
| C1 | Research — the 'how to' resource | 5 | **Proficient** | MEDIUM |
| C2 | The pitch — a firm stance, defended | 20 | **Exemplary** | LOW |
| C3 | Mathematical correctness | 20 | **Not Yet** | LOW |
| C4 | Required deliverables | 15 | **Proficient** | MEDIUM |
| C5 | Visual display and appendix of work | 15 | **Proficient** | MEDIUM |
| C6 | Socratic participation | 15 | **Proficient** | MEDIUM |
| C7 | Framing the question | 10 | **Proficient** | LOW |

### C1 · Research — the 'how to' resource — Proficient (MEDIUM confidence)
- 2 link(s) found, first: https://www.mathsisfun.com/algebra/equations-solving.html
- names a 'how to…' skill in prose: ['How to solve a multi-step equation with a variable on one side']
- no evidence of the skill being LEARNED (a false start, a correction) — not Exemplary
- link liveness and topical match to Appendix G NOT verified — the machine cannot fetch

### C2 · The pitch — a firm stance, defended — Exemplary (LOW confidence)
- pitch word count (appendix excluded) = 1112
- position statement: 'I recommend Option A — the Beal wedding'
- names an argument against its own position: 'the strongest argument against'
- Exemplary on C2 requires that the counter-argument is actually ANSWERED, not just named. LOW confidence — a guide must read it.
- tier gate — the trade-off between the two competing variables is named explicitly: MET

### C3 · Mathematical correctness — Not Yet (LOW confidence)
- recomputed 29 case quantities: 16 agree, 3 to check, 10 not addressed
- AGREES · wedding order qty wedding_order_qty = 118.0
- AGREES · wedding revenue wedding_revenue = 3186.0
- AGREES · wedding ingredient cost wedding_ingredient_cost = 1700.38
- AGREES · wedding gross profit wedding_gross_profit = 1485.62
- CHECK THIS (advisory, not a finding of error) · machine has 1365.32, the Hero's figure next to this label is 1485.62. The Hero may be right — check before acting.
- CHECK THIS (advisory, not a finding of error) · machine has 134.0, the Hero's figure next to this label is 100.0. The Hero may be right — check before acting.
- CHECK THIS (advisory, not a finding of error) · machine has 1098.86, the Hero's figure next to this label is 897.42. The Hero may be right — check before acting.
- units are carried in the prose
- HARD LIMIT 1 — a machine BLOCKER on C3 is ADVISORY, not final. The Hero may be right and the check may be wrong, especially where the Hero declared their own assumption. The guide adjudicates. Do not report this to the learner as an error.

### C4 · Required deliverables — Proficient (MEDIUM confidence)
- deliverables present: ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']
- deliverables missing: -
- presence detected by id and keyword overlap; whether each is 'in a form a reader can actually use' is a guide judgment
- Exemplary requires a deliverable that goes beyond the ask IN SERVICE of the argument — not detectable mechanically

### C5 · Visual display and appendix of work — Proficient (MEDIUM confidence)
- visuals detected: 1 image(s), 0 chart(s)
- underlying data (tables adjacent to the visual): 6 value(s), 2 appear VERBATIM in the case appendices = 33% copied
- majority of the plotted values are the Hero's own: [7.61, 8.16, 760.62, 897.42]
- Exemplary requires the visual to make the argument BY ITSELF — a guide must look at it

### C6 · Socratic participation — Proficient (MEDIUM confidence)
- 2 discussion record(s) in submissions.json for this learner and case
- 1 record(s) note engagement with another Hero's reasoning
- Exemplary requires changing position under evidence and saying why, or holding under pressure and saying why — not visible in a contribution count

### C7 · Framing the question — Proficient (LOW confidence)
- acknowledges an alternative metric: 'under a different metric'
- only one half of the Proficient bar is evidenced — borderline
- HARD LIMIT 2 — the machine may NEVER mark C7 Exemplary. Recognising that someone reframed the question well requires reading an argument, not scanning one. Ceiling clamped to Proficient.
- C7 is the criterion the machine is guessing at entirely (RUBRIC). Always LOW.

## Recomputation of the Hero's numbers

> A machine BLOCKER on C3 is **advisory, not final**. Where the machine disagrees, the Hero may be right and the check may be wrong — especially where the Hero declared their own assumption. Presented as *check this*, never as *wrong*.

| quantity | machine | Hero | status |
|---|---|---|---|
| wedding guests · wedding_guests | 110.0 | — | NOT ADDRESSED |
| wedding order qty · wedding_order_qty | 118.0 | 117.7 | AGREES |
| wedding revenue · wedding_revenue | 3186.0 | 3186.0 | AGREES |
| wedding ingredient cost · wedding_ingredient_cost | 1700.38 | 1700.38 | AGREES |
| wedding gross profit · wedding_gross_profit | 1485.62 | 1485.62 | AGREES |
| wedding event fee · wedding_event_fee | 575.0 | 575.0 | AGREES |
| wedding delivery fee · wedding_delivery_fee | 13.2 | 13.2 | AGREES |
| wedding net profit · wedding_net_profit | 897.42 | 897.42 | AGREES |
| corporate guests · corporate_guests | 100.0 | — | NOT ADDRESSED |
| corporate order qty · corporate_order_qty | 107.0 | 107.0 | AGREES |
| corporate revenue · corporate_revenue | 3135.1 | 3135.1 | AGREES |
| corporate ingredient cost · corporate_ingredient_cost | 1769.78 | 1769.78 | AGREES |
| corporate gross profit · corporate_gross_profit | 1365.32 | 1485.62 | CHECK |
| corporate event fee · corporate_event_fee | 575.0 | 575.0 | AGREES |
| corporate delivery fee · corporate_delivery_fee | 29.7 | 29.7 | AGREES |
| corporate net profit · corporate_net_profit | 760.62 | 760.62 | AGREES |
| loan payment target · loan_payment_target | 950.0 | — | NOT ADDRESSED |
| wedding margin per serving · wedding_margin_per_serving | 12.59 | 12.59 | AGREES |
| wedding fixed fees · wedding_fixed_fees | 588.2 | — | NOT ADDRESSED |
| wedding servings for loan target · wedding_servings_for_loan_target | 123.0 | — | NOT ADDRESSED |
| corporate margin per serving · corporate_margin_per_serving | 12.76 | 12.76 | AGREES |
| corporate fixed fees · corporate_fixed_fees | 604.7 | — | NOT ADDRESSED |
| corporate servings for loan target · corporate_servings_for_loan_target | 122.0 | — | NOT ADDRESSED |
| wedding loan shortfall · wedding_loan_shortfall | 52.58 | — | NOT ADDRESSED |
| corporate loan shortfall · corporate_loan_shortfall | 189.38 | — | NOT ADDRESSED |
| twist wedding guests · twist_wedding_guests | 125.0 | — | NOT ADDRESSED |
| twist wedding order qty · twist_wedding_order_qty | 134.0 | 100.0 | CHECK |
| twist wedding net profit · twist_wedding_net_profit | 1098.86 | 897.42 | CHECK |
| margin pct · margin_pct | 17.99 | 17.99 | AGREES |

## Tier adjustment (T2)

- Requirement: the trade-off between the two competing variables is named explicitly
- Gates: C2
- The tier note changes what Proficient *requires*; it does **not** scale the score. A Proficient T1 and a Proficient T4 both score 70.

## Guide confirm

```bash
python3 skills/submission-score/scripts/guide_confirm.py \
    --learner maya-w --case catering --by "<your name>" \
    --override C3=Proficient --reason "Hero declared their own assumption; machine recomputed against the case default"
```

Every override is logged to `readmodel/score_overrides.json`. **Overrides are the training signal** — a criterion the machine gets wrong more than ~30% of the time is demoted to guide-only.
