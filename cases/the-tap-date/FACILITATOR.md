# Guide Notes: The Tap Date

MS | Guide Notes | Adventure | 2026
**Tier:** T3 (MS-stretch / HS-entry) · **Primary metric:** mean run days in the 42-day season window over 1996-2025 under the Primary Rule (high at least 35 F, low at most 27 F), higher is better · **Margin:** 4.7% (|A - B| / larger; the Early Tap, A, wins) · **SPEC Section 6:** applies (livelihood stress and unpaid leave; boxed note below).

> **SPEC §6 facilitator note (read first).** This case touches a family's livelihood and two relatives taking unpaid leave. Some students' families run on one season's income or on irregular work. Frame Ansel as someone making a planning decision with the best record available, not as someone who "should have known". Do not imply that any real producer chose wrongly in a given year, and do not ask students to imagine a specific family going without. If a student shares a personal experience, thank them and return to the decision.

**Status: every figure here is facilitator-only and recomputed in python from the NOAA GHCN-Daily file for USW00014742 fetched 2026-10-28** (`derive_run_days.py`, `sensitivity_model.py`). Unverified inputs: the 42-day tap-hole life and all three run-day rules are stated assumptions (MA1-MA3), not published figures.

---

## The central finding (what the room must discover and defend)

The winner is not a property of the two dates. It is a property of **(rule, record)**. Fixed scope, pre-committed in the case: Burlington airport, 42-day window, Feb 20 vs Mar 1, Primary Rule, judged on 1996-2025. That gives **Early Tap by 4.7%**. Change one choice and it can reverse:

| Rule | 1950-1979 | 1991-2020 | 1996-2025 | 2006-2025 | 1950-2025 |
|---|---|---|---|---|---|
| Primary Rule (35 / 27) | B 12.0% (12.20 / 13.87) | A 1.8% (13.03 / 12.80) | **A 4.7% (12.67 / 12.07)** | A 5.3% (12.15 / 11.50) | B 2.6% (12.67 / 13.01) |
| Plain Freeze-Thaw (32 / 32) | B 9.7% (23.80 / 26.37) | B 4.5% (24.77 / 25.93) | B 1.4% (24.97 / 25.33) | A 1.0% (25.40 / 25.15) | B 5.2% (24.18 / 25.50) |
| Warm Day, Any Frost (35 / 32) | B 14.2% (18.67 / 21.77) | B 8.1% (20.67 / 22.50) | B 5.0% (20.87 / 21.97) | B 3.0% (21.20 / 21.85) | B 8.9% (19.78 / 21.70) |

(Each cell: winner, margin = |A - B| / larger, then the two means A / B.) Over the five records and three rules, A wins 4 of 15 cells (Primary Rule 1991-2020, 1996-2025, 2006-2025 and Plain Freeze-Thaw 2006-2025). The mechanism is the night threshold: loosening "low at most 27" to "low at most 32" counts many barely-freezing March nights, which the Late Tap has more of; a hard-freeze night is more common in late February.

A wider sweep (Tmax 32, 33, 35, 37 x Tmin 25, 27, 30, 32 x window 35, 42, 49 days; 48 rules) gives, per record, Early Tap wins: 1950-1979 4 of 48; 1991-2020 24 of 48; 1996-2025 33 of 48; 2006-2025 35 of 48 (2 ties); 1950-2025 16 of 48. Largest margin anywhere in the sweep: 17.6%. For 1996-2025 with a 42-day window and any Tmin of 32, the Late Tap wins at every Tmax tested (32, 33, 35, 37: margins 1.4%, 2.3%, 5.0%, 6.6%); with Tmin of 25 or 27 the Early Tap wins at every Tmax tested.

**The honest bottom line for the guide:** there is no rule-free, record-free answer. A good pitch commits to a rule and record and says which cell would reverse it. A student who says "A, 4.7%" with no sensitivity has not answered the question the case asks; a student who says "it depends" with no commitment has not either.

---

## Argument for A (Early Tap, Feb 20)

Under the rule Ansel fixed before looking, the Early Tap leads on the 1996-2025 record, 12.67 run days against 12.07 (4.7%), and it was ahead in 17 of 30 seasons, behind in 9, tied in 4. The edge holds for every record starting 1976 or later under the Primary Rule (0.8% to 5.3%). The fitted lines (1950-2025) give the Early Tap a slope of +0.03 run days per decade and the Late Tap -0.34, and cross about 1997 (1996.8); the Late Tap line is falling and the Early Tap line is flat, so the recent edge is not a one-off. Extrapolated to 2027: 12.78 against 11.67. And a run day under a hard-freeze night is the most defensible stand-in for sap flow: the Late Tap's advantage under the looser rules comes from nights barely at freezing.

## Argument for B (Late Tap, Mar 1)

The Late Tap wins the full 1950-2025 record under all three rules (2.6%, 5.2%, 8.9%). Under two of the three rules it also wins the recent 30 seasons (Plain Freeze-Thaw by 1.4%, Warm Day, Any Frost by 5.0%), and with a night-low threshold of 32 F it wins at every daytime threshold tested for 1996-2025. The Primary Rule's 4.7% is about 1.5 standard errors of the paired season-by-season gap (mean +0.60, spread about 2.25, standard error 0.41), so it is thin. Late March and early April hold the best of the later run, and the Late Tap sits close to the best start date under the looser rules (the 3-day-grid optimum for Warm Day, Any Frost 1996-2025 is Mar 6, only 0.10 run days above Mar 1, while Feb 20 is 1.20 below). B is also the more robust pick: it wins 11 of the 15 cells above.

## The margin

**Convention (stated once):** margin = |A - B| / max(A, B) on mean run days. Primary: (12.67 - 12.07) / 12.67 = **4.7%**, inside the SPEC §2 cap of about 20%. Every one of the 15 cells above and the whole 48-rule sweep is inside 20% (largest 17.6%). Because the winner depends on the rule and record, the 4.7% is a number about one cell, not about the dates; the guide must say so.

| Quantity | Early Tap (A) | Late Tap (B) |
|---|---|---|
| Mean run days 1996-2025, Primary Rule | 12.67 | 12.07 |
| Mean run days 1950-1979 / 1991-2020 / 2006-2025 / 1950-2025 | 12.20 / 13.03 / 12.15 / 12.67 | 13.87 / 12.80 / 11.50 / 13.01 |
| Seasons ahead, 1996-2025 | 17 | 9 (4 ties) |
| Line 1950-2025, slope per decade | +0.03 (r = 0.02) | -0.34 (r = -0.24) |
| Crossing year, Primary Rule / Plain Freeze-Thaw / Warm Day, Any Frost (1950-2025 lines) | 1996.8 / 2022.6 / 2038.6 | |
| Slopes per decade, Plain Freeze-Thaw | +0.18 | -0.19 |
| Slopes per decade, Warm Day, Any Frost | +0.44 | +0.06 |
| Paired gap 1996-2025 (A - B), mean / standard error | +0.60 / 0.41 | |

Note on the lines: a line fitted to a shorter span changes slope and even sign (Primary Rule, 1996-2025 only: -0.82 and -1.18 per decade, crossing 1993.6, a year before the span starts), which is itself a lesson about fitting windows.

## Five Socratic questions

1. Your D3 table flips from the Late Tap on 1950-1979 to the Early Tap on 1996-2025 under the Primary Rule. Which seasons in Appendix C drive the change, and does a 4.7% margin on the recent 30 seasons outweigh a 2.6% margin the other way on all 76?
2. D2's crossing year is about 1997 under the Primary Rule, about 2023 under Plain Freeze-Thaw and about 2039 under Warm Day, Any Frost. What does each crossing year predict about 2027, and which, if any, would you bet a season on?
3. Under Plain Freeze-Thaw and Warm Day, Any Frost the Late Tap wins 1996-2025 by 1.4% and 5.0%. What kind of night does a low of 31 F add to the count that a low of 27 F does not, and which tap date has more of them?
4. Ansel fixed the Primary Rule before he looked. If your D4 map changes your mind, what have you done to the 4.7%, and is "I fixed it first" a reason or a habit?
5. The paired gap for 1996-2025 averages +0.60 run days with a season-to-season spread near 2.25. How many more seasons would you want before calling a 0.6-day edge real, and what would you do in the meantime?

## The trap

A hurried student will take the confident wrong answer in one of several forms:
1. **Stopping at the pre-committed cell.** "Early Tap by 4.7%, done." The 4.7% is true and it is one cell; the question the case asks is how far it travels. Ask for the D4 map before accepting a pick.
2. **Treating the crossing year as a forecast.** The Primary Rule lines cross in 1996.8, so "A has been ahead for 29 years" is a story the data do not tell: the paired gap is 0.6 run days with a spread of about 2.25 per season. Under Warm Day, Any Frost the same method says the lines have not crossed yet (2038.6).
3. **Reading "the rule disagrees" as "the data cannot decide".** The data decide very precisely, given a rule. What they cannot decide is which rule counts as a run day; that is a question about sap physics and the sugarbush, which the airport cannot answer.
4. **Switching to whichever cell looks best after seeing D4.** That is the garden-of-forking-paths move Ansel's January 26 note exists to prevent. Equally, refusing to look at D4 because the rule was fixed first is a habit, not a reason.
5. **Margin denominators.** Dividing the gap by the smaller mean gives 5.0% (0.60 / 12.07) instead of 4.7%. State the convention.
6. **Overriding the pre-committed record with "all the data".** A student computes the 76-season means (12.67 and 13.01 run days), sees the Late Tap win, and picks it because more data feels safer. The calculation is correct; the question is whether the record was chosen before or after seeing it. Equally, a student who never reports that the full record reverses the pick has hidden the cell the case asks them to name. (Found by the P3 blind reader as the most likely wrong path.)
7. **Bookkeeping slips.** Dropping the ties from the seasons-ahead count (17 and 9 leave 4 ties, 10 ties on 1950-2025), quoting per-year slopes as per-decade (0.0027 and -0.034 instead of +0.03 and -0.34), and calling r = -0.24 "strong". Ask for units on every slope.
8. **Breaking the tie with sap science from outside the data.** "Late is safer because early holes dry out by mid-April" (the S6 article). Both windows are 42 days by construction (MA1), so drying is equal in the model, and S6 gives no number of days. Keep the argument inside the data, or name the assumption (MA1) it leans on. (Found by the P3 blind reader.)
9. **Presenting the Primary Rule, the airport and the record as measurements.** Run days are a stand-in (MA2, MA7), the airport is not the sugarbush (MA4), and the thresholds are the author's choice. A pitch that never says so has treated the rule as a fact.
10. **Fitting lines to different spans and comparing slopes.** Slopes on 1950-2025 and on 1996-2025 have opposite signs for the Early Tap line (+0.03 and -0.82 per decade).

## Intro

Frame the format in two sentences: a planning decision, a binary choice, and a pitch defended against peers. Name the opener: "Feb 20 or Mar 1, and Corinne needs a day." Read the SPEC §6 note to yourself again before you begin; do not read it aloud.

## Launch

Have one student say, in a sentence, what maple sap is and why it needs freezing nights and thawing days (the case's two sources, S5 and S7, say so). Show the sugarbush picture only if the room has not seen one; otherwise go straight to the dilemma.

## Anchor 1: Take a stand and vote

"Feb 20 or Mar 1? Stand on the side of the room for the date you would give Corinne. No reasons yet." Record the split. Ask one student on each side for a single reason, and do not comment.

## Anchor 2: What is the problem we are solving?

"What does Ansel actually want?" Let the room argue: the most syrup, the most sap days, the least risk, the fewest wasted days of leave. Ask: "Is 'a run day' the right thing to count?" and "What do you mean by a good start?" Let the confusion grow; then say: "Wow, this is a challenging problem." Do not give the 42-day window or the Primary Rule more weight than the case does.

## Anchor 3: What is the process?

"If we have the daily highs and lows, how will we decide?" Draw the steps: fix a rule, count run days in each window, average, compare, test the compare. Re-ask: "Is our question still the right question?" Ask what Ansel's January 26 note buys him and what it costs.

## Anchor 4: What don't we know?

"Do we need to make assumptions? Which are critical?" Collect: how many days a tap hole lasts, what temperatures make sap flow, whether the airport tells you about the woods, whether 30 seasons is the right number. Ask which one would change the answer if it were off by 5%; then by 50%.

## Data Deep Dive

Now, and only now, the numbers. Walk D1 and D2 first (scatter, lines, crossing year), then D3, and hold D4 until last; let the room see for itself that the winner changes. Use the margin table above only after students show theirs. Do **not** mention anything that happened after the 2025 season.

## Twist

**Twist (post-decision; this is the only place 2026 appears).** After the vote, tell the room: "The 2026 season is over. Here are the run days in each window." Counted from the same station file (data through 2026-10-24; recent values are subject to NOAA quality review):

| Rule | Early Tap (Feb 20 - Apr 2) | Late Tap (Mar 1 - Apr 11) | 2026 winner |
|---|---|---|---|
| Primary Rule | 15 | 15 | tie |
| Plain Freeze-Thaw | 26 | 24 | Early Tap by 2 (7.7%) |
| Warm Day, Any Frost | 20 | 22 | Late Tap by 2 (9.1%) |

For reference the 2025 season was 11 against 11 under the Primary Rule and the 1996-2025 Primary Rule means were 12.67 and 12.07, so 2026 was a rich year under the Primary Rule and an ordinary one under the other two rules (1996-2025 means 24.97 and 25.33; 20.87 and 21.97). Say it slowly, with pauses. Then: "You have sixty seconds. Are you changing your plan, or not?" Follow with the transferable question: **"What just broke in your original model? Were you wrong, or just missing information?"** The twist pressures rather than refutes (a P4 reviewer rightly called it a soft twist): it breaks two popular positions at the margin: "the Primary Rule's 4.7% means the Early Tap is the safe pick" (one season gave a tie) and "the rule you fixed in advance was the right rule" (the other two rules disagree with each other in the same season, exactly as they do in the record). It does not make either date obviously right: no pick lost anything under the Primary Rule, and which date "won" in 2026 depends on the rule chosen after the fact. Pre-empt one miscount: a student who counts the 42 days from the day after the tap turns the Primary Rule tie into a Late Tap win by one (15 to 14). Push on both sides: "Was the 4.7% wrong, or only too small to see in one season?"

**Does the twist survive the case's assumptions?** The 2026 windows use the same 42-day length (MA1), the same three rules (MA2, MA3) and the same station (MA4). The twist depends on no convention the case leaves unstated: window dates, thresholds and the margin convention are all in the packet. `sensitivity_model.py` `evaluate_twist()` reproduces the Primary Rule row; under a window of 21 or 63 days or a different night threshold the twist row changes (see the sensitivity note).

## Close

Re-vote: "Did we ask the right question?" Count who moved and why. Ask: "What math was new to you, and how did you attack it?" and "What would you want Corinne to do about next year?"

## Lessons Learned

- A winner is a statement about a choice of rule and record, not only about the options.
- Fixing the question before the data protects you from fooling yourself, and it does not make the question right.
- A fitted line is only as good as its span; slopes and crossing years move when the span moves.
- A small margin against a spread of seasons is a reason for humility, not for a coin flip.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote on Feb 20 or Mar 1; no explanation |
| 3:00–10:00 | Position defense: "Convince us why it is better, not just why it won once." Anchors 2 and 3 run here before any numbers |
| 10:00–15:00 | Pressure-test the models: "Whose plan is most fragile?" Collect assumptions (Anchor 4) and the D3 and D4 cells |
| **15:00** | **DROP THE TWIST**: show the 2026 season slowly, with pauses |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke in your original model?" |
| 20:00–30:00 | Threaded deep conflict (two named threads): pre-commitment versus robustness across rules; what a run day should mean for sap |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Sensitivity note (SPEC §2 stability)

The verdict is **not stable**, and the guide should say so. It is the point of the case. Under the model's plus-or-minus 50% swing of the stated assumptions (`sensitivity_model.py`, 1996-2025): a 21-day window flips the winner to the Late Tap (5.57 against 6.63); a 63-day window keeps the Early Tap (15.53 against 13.50); a day threshold of 1.5 or 4.5 F above freezing keeps the Early Tap (5.0%, 4.5%); a night threshold of 2.5 F below freezing leaves the two dates nearly tied (15.97 against 15.93) and 7.5 F below favors the Early Tap (9.6%). Moving the rule to Plain Freeze-Thaw or Warm Day, Any Frost, or the record to 1950-1979, 1950-2025, flips it. Flexed margins never exceed 16.1%, inside the SPEC §2 cap. Disclosed in `case.json.sensitivity_disclosure[]`. A rounding check (rounding every converted temperature to whole degrees F before comparing) leaves every winner in the three 1996-2025 cells unchanged (Primary Rule A 4.2%, Plain Freeze-Thaw B 1.4%, Warm Day, Any Frost B 5.0%).

Other notes: neither date is the optimum of a start-date sweep every 3 days from Feb 1 (Primary Rule 1996-2025: Feb 19, 12.73; Warm Day, Any Frost 1996-2025: Mar 6, 22.07); the case limits Ansel to two dates because of the leave forms. Half the taps on each date (a hedge, outside the binary) gives 12.37 run days for 1996-2025 under the Primary Rule, between the two pure options. Not modelled: sap sugar content, volume per run day, labor, tap-hole health.

## Standards touched on

Scatter plot, line of best fit, correlation (D1); linear equation, slope, system of equations (D2); mean (D3, D4). New coverage: none (the spine has no skill at n = 0); the case carries a `reinforcement_note`.

## Cohort bands

See `case.json.cohort_bands[]`: Full (12-20), Compressed (6-11), 1:1 / pair (1-2).
