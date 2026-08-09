# SCORE — ben-okafor · robotics-engineer

**Status:** `machine-first-pass` · **Scored:** 2026-08-08 · **Tier:** T2

> **INTERIM.** This is a machine first pass, not a verdict. It does not count toward a badge and renders as INTERIM on the dashboard until a guide confirms it. Machine drafts, human promotes.

## The two outputs — never averaged

| | |
|---|---|
| **Mastery gate** — badge eligible? | **NO** — blocked on C3, C7 |
| **Growth score** (0–100, guide-only, never a grade) | **55.0** |

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
| C7 | Framing the question | 10 | **Not Yet** | LOW |

### C1 · Research — the 'how to' resource — Proficient (MEDIUM confidence)
- 2 link(s) found, first: https://www.basic-mathematics.com/units-of-speed.html
- names a 'how to…' skill in prose: ['How to convert an amount from one unit to another unit']
- no evidence of the skill being LEARNED (a false start, a correction) — not Exemplary
- link liveness and topical match to Appendix G NOT verified — the machine cannot fetch

### C2 · The pitch — a firm stance, defended — Exemplary (LOW confidence)
- pitch word count (appendix excluded) = 798
- position statement: 'I recommend Route C-B-A'
- names an argument against its own position: 'The strongest argument against'
- Exemplary on C2 requires that the counter-argument is actually ANSWERED, not just named. LOW confidence — a guide must read it.
- tier gate — the trade-off between the two competing variables is named explicitly: MET

### C3 · Mathematical correctness — Not Yet (LOW confidence)
- recomputed 21 case quantities: 0 agree, 0 to check, 21 not addressed
- units are carried in the prose
- no recomputable quantity was found in the submission at all — either the work is missing or the labels do not match the case's

### C4 · Required deliverables — Proficient (MEDIUM confidence)
- deliverables present: ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']
- deliverables missing: -
- presence detected by id and keyword overlap; whether each is 'in a form a reader can actually use' is a guide judgment
- Exemplary requires a deliverable that goes beyond the ask IN SERVICE of the argument — not detectable mechanically

### C5 · Visual display and appendix of work — Proficient (MEDIUM confidence)
- visuals detected: 1 image(s), 0 chart(s)
- underlying data (tables adjacent to the visual): 6 value(s), 0 appear VERBATIM in the case appendices = 0% copied
- majority of the plotted values are the Hero's own: [0.284, 45.66, 92.582, 92.866, 1208.1, 1253.76]
- Exemplary requires the visual to make the argument BY ITSELF — a guide must look at it

### C6 · Socratic participation — Proficient (MEDIUM confidence)
- 2 discussion record(s) in submissions.json for this learner and case
- 1 record(s) note engagement with another Hero's reasoning
- Exemplary requires changing position under evidence and saying why, or holding under pressure and saying why — not visible in a contribution count

### C7 · Framing the question — Not Yet (LOW confidence)
- no evidence the Hero noticed the question was theirs to choose
- HARD LIMIT 2 — the machine may NEVER mark C7 Exemplary. Recognising that someone reframed the question well requires reading an argument, not scanning one. Ceiling clamped to Proficient.
- C7 is the criterion the machine is guessing at entirely (RUBRIC). Always LOW.

## Recomputation of the Hero's numbers

> A machine BLOCKER on C3 is **advisory, not final**. Where the machine disagrees, the Hero may be right and the check may be wrong — especially where the Hero declared their own assumption. Presented as *check this*, never as *wrong*.

| quantity | machine | Hero | status |
|---|---|---|---|
| dist C A m · dist_C_A_m | 12.042 | — | NOT ADDRESSED |
| dist C B m · dist_C_B_m | 10.817 | — | NOT ADDRESSED |
| dist A B m · dist_A_B_m | 21.587 | — | NOT ADDRESSED |
| route C A B total m · route_C_A_B_total_m | 33.629 | — | NOT ADDRESSED |
| route C B A total m · route_C_B_A_total_m | 32.404 | — | NOT ADDRESSED |
| rough terrain speed m per hr · rough_terrain_speed_m_per_hr | 96.56 | — | NOT ADDRESSED |
| route C A B minutes · route_C_A_B_minutes | 20.896 | — | NOT ADDRESSED |
| route C B A minutes · route_C_B_A_minutes | 20.135 | — | NOT ADDRESSED |
| container B integrity pct via A first · container_B_integrity_pct_via_A_first | 92.582 | — | NOT ADDRESSED |
| container B integrity pct via B first · container_B_integrity_pct_via_B_first | 92.866 | — | NOT ADDRESSED |
| twist AB direct m · twist_AB_direct_m | 21.587 | — | NOT ADDRESSED |
| twist AB detour via C m · twist_AB_detour_via_C_m | 22.858 | — | NOT ADDRESSED |
| twist detour extra m · twist_detour_extra_m | 1.271 | — | NOT ADDRESSED |
| twist route C A B minutes · twist_route_C_A_B_minutes | 21.686 | — | NOT ADDRESSED |
| twist route C B A minutes · twist_route_C_B_A_minutes | 20.925 | — | NOT ADDRESSED |
| twist margin pct · twist_margin_pct | 3.64 | — | NOT ADDRESSED |
| triangle check sum CA CB m · triangle_check_sum_CA_CB_m | 22.858 | — | NOT ADDRESSED |
| triangle check sum CA AB m · triangle_check_sum_CA_AB_m | 33.629 | — | NOT ADDRESSED |
| triangle check sum CB AB m · triangle_check_sum_CB_AB_m | 32.404 | — | NOT ADDRESSED |
| triangle check margin m · triangle_check_margin_m | 1.271 | — | NOT ADDRESSED |
| margin pct · margin_pct | 3.78 | — | NOT ADDRESSED |

## Tier adjustment (T2)

- Requirement: the trade-off between the two competing variables is named explicitly
- Gates: C2
- The tier note changes what Proficient *requires*; it does **not** scale the score. A Proficient T1 and a Proficient T4 both score 70.

## Guide confirm

```bash
python3 skills/submission-score/scripts/guide_confirm.py \
    --learner ben-okafor --case robotics-engineer --by "<your name>" \
    --override C3=Proficient --reason "Hero declared their own assumption; machine recomputed against the case default"
```

Every override is logged to `readmodel/score_overrides.json`. **Overrides are the training signal** — a criterion the machine gets wrong more than ~30% of the time is demoted to guide-only.
