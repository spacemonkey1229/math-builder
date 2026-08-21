# Research Log — Bathroom Problems

This case combined `case-write` and `case-research` into one pass (same approach as
`food-rationing` and `family-trip`): every figure the case needs comes directly from the
family's own given scenario data in the source docx, so no `{{NEEDS_SOURCE}}` placeholder was
ever opened. This log records what was checked and what, if anything, was researched externally.

## Given scenario data (no external sourcing needed)

All of the following are the Thomason family's own tracked/given data, taken directly from
`source/Y2/Session 3/Bathroom Problems/Case Study_ Bathroom Problems.docx` — treated as HIGH
confidence per S1, the same treatment `food-rationing` gave the Murray family's own boat
inventory (a real source document reproduced verbatim, describing a fictional family's own
scenario, not an independently-verifiable real-world claim requiring external citation):

- Per-person morning bathroom-activity times and "needs to leave the house by" times (Appendix A)
- Master bathroom fixture data: showerhead GPM, bathtub gallons/bath, water heater First Hour
  Rating (Appendix C)
- The flood backstory, the three house sharing-rules, Thomas's 6:45 AM wake time and the daily
  five-minute family devotional (Background)
- The Twist (Grandma Polly and Grandpa Ben arriving with suitcases) — from
  `Guide Notes.docx`, reproduced in `FACILITATOR.md`

No number derived from these was flexed, rounded, or altered from the source table except the
explicit, disclosed derivation in D1–D4 (which is the student's own work, not case-research's).

## What was genuinely researched externally

Two real-world grounding citations were added — not because any of the case's own numbers were
unsourceable, but to confirm the case's key water/plumbing terms are real, standard concepts
(matching `food-rationing`'s Appendix G "real-world context" treatment):

1. **"First Hour Rating"** — searched to confirm this is a real, standard published water-heater
   specification (not an invented term). Found and fetched ENERGY STAR's own product-criteria
   page, which gives the term's real definition. Recorded as S2, HIGH confidence, directly
   fetched.
2. **Typical U.S. showerhead flow rates** — searched to confirm the case's given 2.25 GPM
   showerhead figure is realistic. Found and fetched the EPA WaterSense showerhead program page,
   which states standard showerheads run about 2.5 GPM and WaterSense-labeled showerheads run at
   or below 2.0 GPM. Recorded as S3, HIGH confidence, directly fetched. The case's own 2.25 GPM
   figure sits realistically between these two real-world reference points — not altered to match
   either.

Both are supplemental grounding (Appendix E), not load-bearing sourced figures — dropping either
citation would not change any computation in the case; they exist to show a Hero that "First Hour
Rating" and shower flow rates are real household-engineering concepts they can research further in
Challenge 1.

## Modeling Assumption disclosed (not a NOT FOUND)

MA1 (case.md's Modeling Assumptions block, `case.json.modeling_assumptions`) is a genuine
author judgment call, not an unsourceable figure: the source states the family devotional happens
"before anyone leaves the house" but never states exactly when in the morning. This conversion
places it first thing (6:45–6:50 AM), immediately after Thomas's given wake time, which sets the
shared 70-minute morning window used throughout D1 and D4. This was a designed choice, not a
research dead end — recorded openly per SPEC.md section 5's "no third category" rule (cited,
or a stated Modeling Assumption; this is the latter, explicitly).

## Verification pass

```
placeholders remaining in case.md: 0
citation markers with no source row: none ([S1], [S2], [S3] all resolve)
source rows never cited in text: none
LOW-confidence sources: none (all three are HIGH)
```

Next step: run `case-readiness` on `bathroom-problems`.
