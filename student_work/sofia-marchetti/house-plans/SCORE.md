# SCORE — sofia-marchetti · house-plans

**Status:** `machine-first-pass` · **Scored:** 2026-08-12 · **Tier:** T2

> **INTERIM.** This is a machine first pass, not a verdict. It does not count toward a badge and renders as INTERIM on the dashboard until a guide confirms it. Machine drafts, human promotes.

## The two outputs — never averaged

| | |
|---|---|
| **Mastery gate** — badge eligible? | **NO** — blocked on C2, C3, C5, C6, C7 |
| **Growth score** (0–100, guide-only, never a grade) | **14.0** |

All-Proficient scores 70. The score tracks trajectory; the gate tracks readiness. If a learner asks what their score is, the answer is that it is a tool for their guide, and the number that matters is which criteria are still Not Yet.

## Surface to the guide first — LOW confidence on C1, C3, C6, C7

## The seven criteria

| | Criterion | Weight | Verdict | Confidence |
|---|---|---|---|---|
| C1 | Research — the 'how to' resource | 5 | **Proficient** | LOW |
| C2 | The pitch — a firm stance, defended | 20 | **Not Yet** | HIGH |
| C3 | Mathematical correctness | 20 | **Not Yet** | LOW |
| C4 | Required deliverables | 15 | **Proficient** | MEDIUM |
| C5 | Visual display and appendix of work | 15 | **Not Yet** | MEDIUM |
| C6 | Socratic participation | 15 | **Not Yet** | LOW |
| C7 | Framing the question | 10 | **Not Yet** | LOW |

### C1 · Research — the 'how to' resource — Proficient (LOW confidence)
- 2 link(s) found, first: https://www.khanacademy.org/math/pre-algebra/pre-algebra-ratios-rates/
- no 'how to…' phrasing in the text, so the link's relevance to Appendix G is unverified
- Exemplary requires visible evidence of the skill being LEARNED (a false start, a correction) — a guide must read for that

### C2 · The pitch — a firm stance, defended — Not Yet (HIGH confidence)
- pitch word count (appendix excluded) = 234
- under the 250-word floor — Challenge 2 requirement

### C3 · Mathematical correctness — Not Yet (LOW confidence)
- recomputed 17 case quantities: 0 agree, 5 to check, 12 not addressed
- CHECK THIS (advisory, not a finding of error) · machine has 432635.84, the Hero's figure next to this label is 549212.8. The Hero may be right — check before acting.
- CHECK THIS (advisory, not a finding of error) · machine has 454792.8, the Hero's figure next to this label is 549212.8. The Hero may be right — check before acting.
- CHECK THIS (advisory, not a finding of error) · machine has 458593.99, the Hero's figure next to this label is 549212.8. The Hero may be right — check before acting.
- CHECK THIS (advisory, not a finding of error) · machine has 482080.37, the Hero's figure next to this label is 549212.8. The Hero may be right — check before acting.
- CHECK THIS (advisory, not a finding of error) · machine has 0.11, the Hero's figure next to this label is 0.1. The Hero may be right — check before acting.
- no units detected anywhere in the submission
- HARD LIMIT 1 — a machine BLOCKER on C3 is ADVISORY, not final. The Hero may be right and the check may be wrong, especially where the Hero declared their own assumption. The guide adjudicates. Do not report this to the learner as an error.

### C4 · Required deliverables — Proficient (MEDIUM confidence)
- deliverables present: ['D1', 'D2', 'D3', 'D4', 'D5']
- deliverables missing: -
- presence detected by id and keyword overlap; whether each is 'in a form a reader can actually use' is a guide judgment
- Exemplary requires a deliverable that goes beyond the ask IN SERVICE of the argument — not detectable mechanically

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
| true ceiling · true_ceiling | 550000.0 | — | NOT ADDRESSED |
| farmhouse sqft · farmhouse_sqft | 2912.0 | — | NOT ADDRESSED |
| ranch sqft · ranch_sqft | 4494.0 | — | NOT ADDRESSED |
| farmhouse build cost · farmhouse_build_cost | 432635.84 | 549212.8 | CHECK |
| farmhouse amenity cost · farmhouse_amenity_cost | 117200.0 | — | NOT ADDRESSED |
| farmhouse total · farmhouse_total | 549835.84 | — | NOT ADDRESSED |
| farmhouse pct of ceiling · farmhouse_pct_of_ceiling | 99.9702 | — | NOT ADDRESSED |
| ranch build cost · ranch_build_cost | 454792.8 | 549212.8 | CHECK |
| ranch amenity cost · ranch_amenity_cost | 94420.0 | — | NOT ADDRESSED |
| ranch total · ranch_total | 549212.8 | — | NOT ADDRESSED |
| ranch pct of ceiling · ranch_pct_of_ceiling | 99.8569 | — | NOT ADDRESSED |
| twist lumber increase pct · twist_lumber_increase_pct | 6.0 | — | NOT ADDRESSED |
| twist farmhouse build cost · twist_farmhouse_build_cost | 458593.99 | 549212.8 | CHECK |
| twist ranch build cost · twist_ranch_build_cost | 482080.37 | 549212.8 | CHECK |
| twist farmhouse increase · twist_farmhouse_increase | 25958.15 | — | NOT ADDRESSED |
| twist ranch increase · twist_ranch_increase | 27287.57 | — | NOT ADDRESSED |
| margin pct · margin_pct | 0.11 | 0.1 | CHECK |

## Tier adjustment (T2)

- Requirement: the trade-off between the two competing variables is named explicitly
- Gates: C2
- The tier note changes what Proficient *requires*; it does **not** scale the score. A Proficient T1 and a Proficient T4 both score 70.

## Guide confirm

```bash
python3 skills/submission-score/scripts/guide_confirm.py \
    --learner sofia-marchetti --case house-plans --by "<your name>" \
    --override C3=Proficient --reason "Hero declared their own assumption; machine recomputed against the case default"
```

Every override is logged to `readmodel/score_overrides.json`. **Overrides are the training signal** — a criterion the machine gets wrong more than ~30% of the time is demoted to guide-only.
