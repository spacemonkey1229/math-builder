# SCORE — jordan-reyes · robotics-engineer

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
- 2 link(s) found, first: https://www.khanacademy.org/math/geometry/hs-geo-analytic-geometry/hs-
- no 'how to…' phrasing in the text, so the link's relevance to Appendix G is unverified
- Exemplary requires visible evidence of the skill being LEARNED (a false start, a correction) — a guide must read for that

### C2 · The pitch — a firm stance, defended — Not Yet (HIGH confidence)
- pitch word count (appendix excluded) = 207
- under the 250-word floor — Challenge 2 requirement

### C3 · Mathematical correctness — Not Yet (LOW confidence)
- recomputed 21 case quantities: 0 agree, 2 to check, 19 not addressed
- CHECK THIS (advisory, not a finding of error) · machine has 12.042, the Hero's figure next to this label is 3.8. The Hero may be right — check before acting.
- CHECK THIS (advisory, not a finding of error) · machine has 3.78, the Hero's figure next to this label is 3.8. The Hero may be right — check before acting.
- no units detected anywhere in the submission
- HARD LIMIT 1 — a machine BLOCKER on C3 is ADVISORY, not final. The Hero may be right and the check may be wrong, especially where the Hero declared their own assumption. The guide adjudicates. Do not report this to the learner as an error.

### C4 · Required deliverables — Not Yet (MEDIUM confidence)
- deliverables present: -
- deliverables missing: ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']
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
| dist C A m · dist_C_A_m | 12.042 | 3.8 | CHECK |
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
| margin pct · margin_pct | 3.78 | 3.8 | CHECK |

## Tier adjustment (T2)

- Requirement: the trade-off between the two competing variables is named explicitly
- Gates: C2
- The tier note changes what Proficient *requires*; it does **not** scale the score. A Proficient T1 and a Proficient T4 both score 70.

## Guide confirm

```bash
python3 skills/submission-score/scripts/guide_confirm.py \
    --learner jordan-reyes --case robotics-engineer --by "<your name>" \
    --override C3=Proficient --reason "Hero declared their own assumption; machine recomputed against the case default"
```

Every override is logged to `readmodel/score_overrides.json`. **Overrides are the training signal** — a criterion the machine gets wrong more than ~30% of the time is demoted to guide-only.
