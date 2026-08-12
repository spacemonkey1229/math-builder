# SCORE — malik-thompson · catering

**Status:** `machine-first-pass` · **Scored:** 2026-08-12 · **Tier:** T2

> **INTERIM.** This is a machine first pass, not a verdict. It does not count toward a badge and renders as INTERIM on the dashboard until a guide confirms it. Machine drafts, human promotes.

## The two outputs — never averaged

| | |
|---|---|
| **Mastery gate** — badge eligible? | **NO** — blocked on C2, C3, C4, C5, C6, C7 |
| **Growth score** (0–100, guide-only, never a grade) | **3.5** |

All-Proficient scores 70. The score tracks trajectory; the gate tracks readiness. If a learner asks what their score is, the answer is that it is a tool for their guide, and the number that matters is which criteria are still Not Yet.

## Surface to the guide first — LOW confidence on C1, C3, C6, C7

## The seven criteria

| | Criterion | Weight | Verdict | Confidence |
|---|---|---|---|---|
| C1 | Research — the 'how to' resource | 5 | **Proficient** | LOW |
| C2 | The pitch — a firm stance, defended | 20 | **Not Yet** | HIGH |
| C3 | Mathematical correctness | 20 | **Not Yet** | LOW |
| C4 | Required deliverables | 15 | **Not Yet** | MEDIUM |
| C5 | Visual display and appendix of work | 15 | **Not Yet** | MEDIUM |
| C6 | Socratic participation | 15 | **Not Yet** | LOW |
| C7 | Framing the question | 10 | **Not Yet** | LOW |

### C1 · Research — the 'how to' resource — Proficient (LOW confidence)
- 2 link(s) found, first: https://www.khanacademy.org/math/pre-algebra/pre-algebra-ratios-rates/
- no 'how to…' phrasing in the text, so the link's relevance to Appendix G is unverified
- Exemplary requires visible evidence of the skill being LEARNED (a false start, a correction) — a guide must read for that

### C2 · The pitch — a firm stance, defended — Not Yet (HIGH confidence)
- pitch word count (appendix excluded) = 149
- under the 250-word floor — Challenge 2 requirement

### C3 · Mathematical correctness — Not Yet (LOW confidence)
- recomputed 29 case quantities: 3 agree, 2 to check, 24 not addressed
- AGREES · wedding event fee wedding_event_fee = 575.0
- AGREES · wedding net profit wedding_net_profit = 897.42
- AGREES · corporate event fee corporate_event_fee = 575.0
- CHECK THIS (advisory, not a finding of error) · machine has 760.62, the Hero's figure next to this label is 3186.0. The Hero may be right — check before acting.
- CHECK THIS (advisory, not a finding of error) · machine has 1098.86, the Hero's figure next to this label is 3186.0. The Hero may be right — check before acting.
- no units detected anywhere in the submission
- HARD LIMIT 1 — a machine BLOCKER on C3 is ADVISORY, not final. The Hero may be right and the check may be wrong, especially where the Hero declared their own assumption. The guide adjudicates. Do not report this to the learner as an error.

### C4 · Required deliverables — Not Yet (MEDIUM confidence)
- deliverables present: ['D2', 'D3', 'D4']
- deliverables missing: ['D1', 'D5', 'D6']
- presence detected by id and keyword overlap; whether each is 'in a form a reader can actually use' is a guide judgment

### C5 · Visual display and appendix of work — Not Yet (MEDIUM confidence)
- visuals detected: 0 image(s), 0 chart(s)
- no original visual found. If the Hero submitted a visual in a format the machine cannot read (a photo of paper, a link to a Desmos graph), this is a false negative — check the appendix link.

### C6 · Socratic participation — Not Yet (LOW confidence)
- 2 discussion record(s) in submissions.json for this learner and case
- 0 record(s) note engagement with another Hero's reasoning
- Proficient requires at least one contribution that engages another Hero's reasoning rather than restating their own; the notes do not record that. Almost certainly a recording gap rather than a learner gap — ask the guide.

### C7 · Framing the question — Not Yet (LOW confidence)
- no evidence the Hero noticed the question was theirs to choose
- HARD LIMIT 2 — the machine may NEVER mark C7 Exemplary. Recognising that someone reframed the question well requires reading an argument, not scanning one. Ceiling clamped to Proficient.
- C7 is the criterion the machine is guessing at entirely (RUBRIC). Always LOW.

## Recomputation of the Hero's numbers

> A machine BLOCKER on C3 is **advisory, not final**. Where the machine disagrees, the Hero may be right and the check may be wrong — especially where the Hero declared their own assumption. Presented as *check this*, never as *wrong*.

| quantity | machine | Hero | status |
|---|---|---|---|
| wedding guests · wedding_guests | 110.0 | — | NOT ADDRESSED |
| wedding order qty · wedding_order_qty | 118.0 | — | NOT ADDRESSED |
| wedding revenue · wedding_revenue | 3186.0 | — | NOT ADDRESSED |
| wedding ingredient cost · wedding_ingredient_cost | 1700.38 | — | NOT ADDRESSED |
| wedding gross profit · wedding_gross_profit | 1485.62 | — | NOT ADDRESSED |
| wedding event fee · wedding_event_fee | 575.0 | 575.0 | AGREES |
| wedding delivery fee · wedding_delivery_fee | 13.2 | — | NOT ADDRESSED |
| wedding net profit · wedding_net_profit | 897.42 | 897.42 | AGREES |
| corporate guests · corporate_guests | 100.0 | — | NOT ADDRESSED |
| corporate order qty · corporate_order_qty | 107.0 | — | NOT ADDRESSED |
| corporate revenue · corporate_revenue | 3135.1 | — | NOT ADDRESSED |
| corporate ingredient cost · corporate_ingredient_cost | 1769.78 | — | NOT ADDRESSED |
| corporate gross profit · corporate_gross_profit | 1365.32 | — | NOT ADDRESSED |
| corporate event fee · corporate_event_fee | 575.0 | 575.0 | AGREES |
| corporate delivery fee · corporate_delivery_fee | 29.7 | — | NOT ADDRESSED |
| corporate net profit · corporate_net_profit | 760.62 | 3186.0 | CHECK |
| loan payment target · loan_payment_target | 950.0 | — | NOT ADDRESSED |
| wedding margin per serving · wedding_margin_per_serving | 12.59 | — | NOT ADDRESSED |
| wedding fixed fees · wedding_fixed_fees | 588.2 | — | NOT ADDRESSED |
| wedding servings for loan target · wedding_servings_for_loan_target | 123.0 | — | NOT ADDRESSED |
| corporate margin per serving · corporate_margin_per_serving | 12.76 | — | NOT ADDRESSED |
| corporate fixed fees · corporate_fixed_fees | 604.7 | — | NOT ADDRESSED |
| corporate servings for loan target · corporate_servings_for_loan_target | 122.0 | — | NOT ADDRESSED |
| wedding loan shortfall · wedding_loan_shortfall | 52.58 | — | NOT ADDRESSED |
| corporate loan shortfall · corporate_loan_shortfall | 189.38 | — | NOT ADDRESSED |
| twist wedding guests · twist_wedding_guests | 125.0 | — | NOT ADDRESSED |
| twist wedding order qty · twist_wedding_order_qty | 134.0 | — | NOT ADDRESSED |
| twist wedding net profit · twist_wedding_net_profit | 1098.86 | 3186.0 | CHECK |
| margin pct · margin_pct | 17.99 | — | NOT ADDRESSED |

## Tier adjustment (T2)

- Requirement: the trade-off between the two competing variables is named explicitly
- Gates: C2
- The tier note changes what Proficient *requires*; it does **not** scale the score. A Proficient T1 and a Proficient T4 both score 70.

## Guide confirm

```bash
python3 skills/submission-score/scripts/guide_confirm.py \
    --learner malik-thompson --case catering --by "<your name>" \
    --override C3=Proficient --reason "Hero declared their own assumption; machine recomputed against the case default"
```

Every override is logged to `readmodel/score_overrides.json`. **Overrides are the training signal** — a criterion the machine gets wrong more than ~30% of the time is demoted to guide-only.
