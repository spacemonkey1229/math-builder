# Guide Notes: Seton Hall

**Case:** Seton Hall · **Tier:** T3 · **Band:** MS-stretch/HS-entry · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (30 skills — scatter plots, coordinate
planes, decimal arithmetic, variable expressions, comparison, rounding, mean, percent)

Legacy conversion, 2026-08-13, built from the original case study docx
(`source/Y1/Session 6/Seton Hall/Case Study_ Seton Hall.docx`) plus its data workbook
(`NCAA Basketball Team Statistics.xlsx`) onto the current 11-anchor ladder. The season data is
real, verified 2019-20 Division I data. **The legacy Guide Notes.docx found alongside this case is
for an unrelated case ("College Admissions") and contains no usable Seton Hall content** — this
entire guide, including the twist, is authored fresh from case.md's own real, sourced data, per
case-write SKILL.md step 5.

**Critical fact this guide is built around:** the real 2020 NCAA Tournament was canceled outright
on March 12, 2020, before any bracket or seed list was ever finalized. No real vote like the one
this case dramatizes was ever made public. Two real rankings *did* exist the day the season froze —
the final AP media poll (No. 15) and the NCAA's own NET ranking (No. 12) — and they are the twist
below, not background color to mention early.

## Intro

Frame the format: this is a real team's real, frozen-in-time season, and a real decision the actual
NCAA committee never got to finish. Name the opener — "Eleven people, one tie vote, and a season
that got frozen mid-argument by history itself."

## Launch

Read Seton Hall's real profile aloud from Background — 21-9, Big East co-champion — with **no
rating data from Appendix B yet, and no mention of Appendix A's real rankings**. Ask: "Just from a
21-9 record and a share of the conference title, does this team belong in the top 16 — gut read,
no math yet?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Yea or nay — is Seton Hall a top-16 team?" Show of hands, no discussion. Record the count — Close
asks them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do we mean by 'top 16'?"**

Push on what actually makes a team "top 16" here: is it who's the best team on a neutral court
today, who's had the best season, or who's beaten the toughest schedule? Let the room discover
these are three different questions that can have three different answers before any data appears.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked what "top 16" means to them, name the actual steps: pick the rating
columns that matter (Appendix B), build a formula that combines them (D2), rank the field (D3), and
compare Seton Hall's position to the No. 16 line. Re-ask: "Is our question still the right
question?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix D's real conventions: the 25-team bubble field was curated by the case, not handed
down by the real committee (MA1), and "top 16" means the four No. 1-4 overall seed lines (MA2). Ask
which assumption, if changed, would actually move the answer.

## Data Deep Dive

Now, and only now, the ratings. Walk D1's scatter plot and D2's formula-building together as a
room. Cold-call specifically for **which columns each Hero chose** for their Power Score — this is
where the wrong path named below begins to show itself: Heroes who reach only for Team Offensive
and Team Defensive Rating, because those "belong" to Seton Hall, are about to build a formula that
misses the case's real story.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Before you vote again — here are the two real, dated national rankings that existed on the actual
day this season stopped. Nobody made these up for this case."

**Facilitator-only.** Reveal Appendix A: the final AP media poll had Seton Hall at **No. 15** — one
spot inside the cutoff. The NCAA's own real NET system, the actual tool the real committee uses,
had Seton Hall at **No. 12**. Both are real. Neither is a landslide.

This invalidates two overconfident positions at once, from opposite directions:

- Heroes who built a Power Score from opponent-adjusted columns (Opp Off/Def Rating) and landed
  Seton Hall around 6th-9th of 25 will find the real world agrees they're in — but by a much
  thinner margin (No. 15 of 16, not "comfortably 9th") than their own algorithm suggested.
- Heroes who built a Power Score from raw Team Off/Def Rating alone (skipping opponent adjustment
  entirely — the wrong path named below) and landed Seton Hall near or below the cutoff will find the real world's own
  committee-grade tool, NET, put them solidly inside at No. 12 — a real signal their formula was
  missing the schedule-strength half of the picture the whole time.

Ask: "What just broke in your model? Were you wrong — or just missing information your formula
never asked for?"

## Immediate recommit

Re-vote immediately. Ask by name: "Does the real AP/NET data change your vote — or does it just
tell you your own formula needs a column it didn't have?"

## Deep conflict — two threads (20-30 min)

1. **Opponent-adjusted vs. raw stats.** A team's own offense and defense feel like "their" number —
   but the whole reason the real committee (and NET) adjusts for opponents is that a 21-9 record
   against a soft schedule and a 21-9 record against a brutal one are not the same résumé. Which
   Heroes' D2 formulas actually captured that, and which didn't?
2. **A résumé frozen incomplete.** Every other bubble team in Appendix B got to finish its
   conference tournament — win or lose. Seton Hall didn't get the chance to add a signature win or
   survive a bad loss. Is an incomplete real résumé worth less than a complete one with the same
   numbers, or does that penalize Seton Hall for something outside its control?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read the 21-9 record aloud, cold-call for a gut read, no rating data yet |
| 3:00–10:00 | Position defense — *"Convince us using your own Power Score, not just the win-loss record"* |
| 10:00–15:00 | Pressure-test the models — *"Which columns did your formula actually use — and which did it skip?"* |
| **15:00** | **DROP THE TWIST** — the real AP (No. 15) and NET (No. 12) rankings, delivered slowly |
| 15:00–20:00 | Immediate recommit — did the real data change anyone's vote |
| 20:00–30:00 | Threaded deep conflict (opponent-adjustment; a résumé frozen incomplete) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

A Hero builds their Power Score using only Team Offensive Rating and Team Defensive Rating —
the two numbers that feel most obviously "Seton Hall's own" — and confidently votes nay, since
those two columns alone (rank 29 and rank 25 nationally) land Seton Hall in a virtual tie for
14th-15th in the bubble field, right on the line. What the trap-formula misses is the *opponent*
half of the data: Seton Hall's Opponents' Offensive Rating ranks 7th nationally and its Opponents'
Rating Difference ranks 12th — real, disclosed evidence of a hard schedule that a raw-stats-only
formula throws away entirely. This is exactly the number the real NCAA added the NET system
specifically to capture. Watch for Heroes whose D2 formula never touches the Opp Off/Def columns
at all — that is the tell.

## Twist soundness check

Checked against SPEC.md §6's requirement that the twist survive both a **sequential** and a
**simultaneous** reading of every stated assumption (MA1-MA3):

- **Sequential:** MA1 (bubble-field curation) → MA2 ("top 16" = 4 seed lines) → MA3 (353-team
  field) each hold independently; the twist (real AP/NET rankings) doesn't depend on any of them —
  it's an external, independently sourced fact laid on top of whichever curation or field-size
  convention the room used.
- **Simultaneous:** applying all three assumptions at once still leaves the twist intact, because
  the AP and NET rankings are real historical facts, not derived from the case's own modeling
  choices. No combination of MA1-MA3 can make the twist stop being true or turn it into a
  "gotcha" that contradicts something the case told Heroes to assume.

## Socratic questions

1. Your Power Score put Seton Hall at [rank] of 25 — the real NET system, built by the actual NCAA for this exact job, had them at No. 12 of 353 (out of a real field of 353 teams). Does your formula agree with that, or did it miss something?
2. Seton Hall's Team Offensive Rating ranks only 29th nationally, but its Opponents' Offensive Rating ranks 7th. What does the gap between those two numbers tell you that either one alone doesn't?
3. The real AP poll margin is exactly one spot — 15th of a 16-cutoff, a real 6.25% margin. If you had to defend that margin as "clearly in" versus "basically a coin flip," which would you pick, and what number would you point to?
4. Seton Hall's win-loss rank alone (ignoring schedule strength entirely) is 50th out of the 270 teams with a usable record in this case's data. Why might that number be misleading on its own?
5. Every other team in Appendix B got to finish its conference tournament. Seton Hall didn't. Should an incomplete résumé count against a team, for or against, when the reason it's incomplete had nothing to do with how they played?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that doesn't
move much after the twist is worth asking about directly: did the real AP/NET numbers confirm what
the room already believed, or did nobody's formula actually predict them?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes' D2 formulas tended to include the opponent-adjusted columns unprompted, or
  whether most fell into the raw-stats trap and needed the twist to notice it.
- Whether the scatter plot (D1) helped Heroes see the bubble-field clustering before they built
  their formula, or whether it was treated as an afterthought produced after the ranking was done.
- Whether the corrupted-data note in Appendix C (83 of 353 win-loss records unrecoverable) came up
  naturally, or needs to be pointed out directly for Heroes to notice real data is sometimes broken.

**Sensitivity disclosure (Tier 2 probe P5, mechanical FAIL, not eliminated):** the case's real,
graded margin — AP poll No. 15 against the No. 16 cutoff — is genuinely fragile: `sensitivity_model.py`
shows the verdict flips if the AP voters had placed Seton Hall just two spots lower (No. 17). This is
not a modeling assumption the case chose (MA1-MA3 do not touch this margin); it is how thin the real,
cited data itself is. **Do not defend "No. 15 of 16" to the room as an unshakeable margin** — it is a
real number, and it is a close one, and both of those things are true at once. If a Hero pushes on
"what if the AP poll had been slightly different," the honest answer is "the vote would flip, and
that's exactly why the room is split" — not a reassurance that the margin is safe.

## Standards Touched On

Scatter Plot · Coordinate Plane · X-Axis · Y-Axis · Origin · Coordinate Pair (also Ordered Pair) ·
Decimal · Decimal Number · Operation · Variable · Constant · Coefficient · Greater Than · Less Than
· Rounding · Mean · Percent · How to create a scatter plot given a set of data · How to graph a
coordinate pair on the coordinate plane · How to add decimal numbers · How to subtract decimal
numbers · How to multiply decimal numbers · How to divide decimal numbers · How to evaluate an
expression with multiple operations without exponents · How to evaluate a variable expression
(Substitution Property) · How to compare two or more values · How to round a number to a specified
place value · How to find the mean of a set of data · How to convert numbers to percents · How to
write a linear equation given a set of data

## Facilitator note — sensitivity

This case touches a real disappointment — a canceled season that denied a genuinely excellent team
its shot (SPEC.md §6). Keep the discussion frame on the math and the real, disclosed data. Avoid
turning the cancellation itself into a debate topic; it is real, historical, and not up for a vote.
If any Hero has strong personal fandom (Seton Hall, Big East, or a rival program), gently redirect
to the numbers — this case is designed to be answerable from the data regardless of who anyone was
rooting for.
