# Navigation — Learning Goal Check

Bidirectional deliverable ↔ skill matrix (SPEC §1.7 / `case-write` step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 labeled route drawing, using the map's scale bar against Appendix C's given distances | `measurement-distance`, `measurement-ratio`, `measurement-proportion`, `measurement-how-to-find-a-missing-amount-in-a-proportion`, `measurement-unit`, `measurement-how-to-convert-an-amount-from-one-unit-to-another-unit` |
| D2 Clean Run (Option A) segment-by-segment drive-time table, ending in one grand total | `measurement-time`, `measurement-how-to-convert-between-units-of-time`, `measurement-how-to-add-and-subtract-time`, `measurement-how-to-find-elapsed-time`, `basic-operations-multiplication`, `basic-operations-how-to-multiply-any-two-numbers`, `basic-operations-division`, `basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number`, `basic-operations-addition`, `basic-operations-how-to-add-multi-digit-numbers` |
| D3 Hot Run (Option B) segment-by-segment drive-time table, plus time saved in minutes/seconds and as a percent | `measurement-time`, `measurement-how-to-convert-between-units-of-time`, `measurement-how-to-add-and-subtract-time`, `basic-operations-multiplication`, `basic-operations-how-to-multiply-any-two-numbers`, `basic-operations-division`, `basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number`, `basic-operations-addition`, `basic-operations-how-to-add-multi-digit-numbers`, `basic-operations-subtraction`, `basic-operations-how-to-subtract-multi-digit-numbers`, `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `number-sense-how-to-compare-two-or-more-values` |
| D4 total-risk calculation and dollars-risked-per-minute-saved rate, plus the pitch's required visual display | `basic-operations-division`, `basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number`, `basic-operations-multiplication`, `basic-operations-how-to-multiply-any-two-numbers`, `number-sense-bar-graph`, `number-sense-data` |

## LEARNING GOAL CHECK

```
deliverables: 4    claimed skills: 22    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

Every skill in `standards[]` appears in at least one deliverable's skill list above ("forces"
test: a competent student cannot produce D2/D3's grand total without converting hours to
minutes/seconds and adding four segment times plus their stop-sign delays; cannot produce D1's
scaled drawing without applying the map's stated ratio; cannot produce D4's rate without dividing
a dollar total by a time total). Every deliverable maps to at least one skill. Both lists are
empty by inspection above.

## new_coverage[] — honest empty, not padded

This is a legacy conversion (`case.json.legacy_conversion_note`). "Navigation" was already tagged
into `readmodel/standards_spine.json`'s `covered_by[]` before this conversion, and all 22 skills
this case's actual deliverables force were already covered by other cases (n ranges from 3 to 36
across the claimed set — see the spine query below). `new_coverage[]` is legitimately empty.
`skills/case-readiness/SKILL.md`'s T1-10 legacy-conversion carve-out (2026-08-13) downgrades this
from a BLOCKER to a recorded GAP for exactly this situation — a case being *formalized*, not
freshly authored, whose deliverables were checked and honestly don't reach an uncovered skill in
the closest adjacent group (Measurement/Ratios And Proportions and Measurement/Time were both
checked directly for n==0 skills; none exist — see spine query below).

```
n= 3 how-to  measurement-how-to-find-a-missing-amount-in-a-proportion
n= 4 how-to  measurement-how-to-find-equivalent-ratios         (considered, not forced — D1
                                                                 uses the map's given ratio, it
                                                                 does not ask the student to find
                                                                 an *equivalent* ratio)
n= 8 term    measurement-proportion
n= 9 how-to  measurement-how-to-find-elapsed-time
n=10 how-to  measurement-how-to-convert-an-amount-from-one-unit-to-another-unit
n=11 how-to  measurement-how-to-convert-between-units-of-time
n=12 term    measurement-distance
n=12 term    measurement-ratio
n=13 how-to  measurement-how-to-add-and-subtract-time
n=17 term    measurement-time
n=23 term    measurement-unit
```

No skill in the Ratios/Proportions or Time groups has `n == 0`; the two closest adjacent,
genuinely-considered-but-not-forced skills (`measurement-how-to-find-equivalent-ratios` and
`measurement-how-to-find-the-start-or-end-time-given-the-start-or-end-and-the-elapsed-time`) were
checked and excluded because no deliverable requires them — adding either would be exactly the
padding this check exists to catch.
