# Guide Notes: The Missing Hub

MS | Guide Notes | Adventure | 2026
**Tier:** T3 (MS stretch / HS entry) · **Primary metric:** share of the friend circle's 52
members whose reported degree count is fabricated-or-missing, per option · **Margin:** 0.00% —
a genuine structural tie (see Robustness Check below; this is a deliberately-designed dead heat,
not a rounding artifact).

---

## FACILITATOR ONLY — Balance Argument

**Argument for A (The Recovery).** Reconstructing the missing member's degree count keeps the
paper's reported circle at its true size — 52 members, matching what the lab has always claimed
about this ego-network. Every member gets a number. But that one number is only ever an estimate,
built from a five-week-old statistic Sam cannot verify tonight. Structurally, it is exactly as
"not exact" as any fabricated figure: **1 of the circle's 52 members (1.923%) is represented by
an estimate, not a known value.**

**Argument for B (The Clean Drop).** Dropping the missing member never risks reporting a single
fabricated number — every value in the resulting 51-member dataset is exact and independently
verified. But it silently shrinks the reported circle from 52 to 51 in every downstream statistic.
**1 of the circle's 52 members (1.923%) is not represented at all.**

**Margin basis** (`case.json.balance.margin_basis`): 51/52 (members with an exact, known degree
count), computed identically for A (the estimated member does not count as exact) and B (the
dropped member is not represented, so it does not count as exact either). **`margin_pct` = 0.0 —
a genuine tie.** Both options compromise exactly one member of the same 52; the case does not
resolve numerically which is "worse," by design.

### Robustness Check — completed, PASSED (case retuned after an initial fragile result)

An earlier draft of this case used a different primary metric: "percent deviation of each
option's reported mean degree from the circle's true current mean degree." That version had a
tight, attractive BASE margin (≈1.02%, Option A) — but **failed the required ±50% robustness
check**. Because Option A's reconstructed mean is, by construction, always exactly equal to
whatever cached mean-degree statistic (MA1) is fed into the reconstruction algebra, flexing MA1 by
±50% moves Option A's apparent accuracy by the same ±50% — which overwhelmed Option B's small,
MA1-independent cost almost everywhere in the flex band, flipping the winner to B across nearly
the entire required sweep. Per this project's own rule — a verdict that flips under a ±50%
assumption flex is retuned in case-write, never hidden — **the primary metric itself was
redesigned**, not merely re-tuned:

1. The metric changed from "how close is the estimate" (inherently as sensitive as the assumption
   feeding it) to "**is this member's reported number exact at all**" — a yes/no structural
   question that both options answer identically (no) for the same one member, **regardless of
   what MA1's value is.**
2. `sensitivity_model.py` confirms this is flip-proof by construction, not merely flip-resistant:
   it sweeps MA1 across the required ±50% band *and* a much wider 0×–3× stress test, and the
   metric (0.980769 for both A and B) never moves at all.

| cached_mean (MA1) | reconstructed value (D1) | winner | margin |
|---|---|---|---|
| 5.375 (−50%) | −268.5 (nonsensical — a negative degree) | TIE | 0.00% |
| 8.06 (−25%) | −128.8 | TIE | 0.00% |
| 10.75 (base) | 11 | TIE | 0.00% |
| 13.44 (+25%) | 150.8 | TIE | 0.00% |
| 16.13 (+50%) | 290.5 | TIE | 0.00% |

**Result: STABLE — the winner (TIE) never moves, at any flex level.** What *does* move, sharply,
is the reconstructed VALUE itself (D1's actual deliverable) — from a nonsensical negative number
to several hundred. That swing is real and is exactly what should worry a careful Hero: **the
number Option A reports is highly sensitive to an assumption nobody can verify tonight, even
though the CHOICE between A and B, on this case's own terms, structurally is not.**

**One honest caveat for whoever runs the discussion:** this case's true, unpublished data (the
real SNAP ego-network 3980 edge list) shows the missing member (ID 4030) is genuinely the
circle's own best-connected member — degree 36 out of 292 possible connections, the real
maximum. Reconstructing from the base assumption (10.75) yields 11 — a large miss in absolute
terms, badly *understating* how connected this member really is. Facilitators should not reveal
this number during the discussion (Sam does not know it either, and neither should the room) —
but it is worth knowing privately that this case's real data happens to land on the riskier side
of "what if it's secretly a hub," which is exactly the scenario the concept was built to explore.

---

## Five Socratic Questions

1. "Your D1 reconstruction and Option B's drop both change the paper by exactly one member out of
   fifty-two. If the math comes out to a tie, what actually should decide Sam's choice?" *(There
   is no numeric answer — press for a values-based argument: honesty about what's known vs.
   completeness of the record.)*
2. "Appendix C's mean-degree statistic is five weeks old. What would have to be true about this
   friend circle for that number to still be exactly right tonight? What would have to be true for
   it to be badly wrong?" *(Friend circles rarely lose or gain many connections in five weeks for
   most members — but a single very well-connected member gaining or losing several friendships
   would move the number by more than an average member would. This is the real risk Option A
   carries.)*
3. "If Sam picks Option A and it turns out the missing member was one of the circle's most
   connected people, what happens to every OTHER statistic in the paper that assumes this reported
   number is right?" *(Any downstream analysis — e.g., 'who are this circle's most connected
   members' — could misrank or entirely miss the true top connector, since the reconstructed
   value might sit nowhere near the top of the list even if the true value would have been the
   circle's actual maximum.)*
4. "Does either of your D3 box-and-whisker plots show an outlier? What does it mean that BOTH
   choices might make a real outlier invisible?" *(Correct read: at this case's base assumption,
   neither plot shows an outlier — the reconstructed value falls inside the whiskers, and the
   dropped dataset simply has one fewer point. Either way, if the true missing value actually was
   unusually high, the plot the reader sees would not show it. This is the case's central,
   uncomfortable insight.)*
5. "Sam's advisor said, 'don't let one bad row wreck a real dataset.' Which option is more likely
   to wreck it — reporting a wrong number, or reporting an incomplete one?" *(No single correct
   answer — this is the crux of the discussion. Press Heroes to defend their answer using D1–D4's
   actual numbers, not just intuition.)*

## The Trap

Heroes will build D1's reconstruction correctly, get a specific number (11, at the case's stated
assumption), and then treat that number as *known* for the rest of the case — building D2–D5 as
if Option A simply "fixed" the problem and is obviously the stronger choice because it "kept all
52 members." The trap is forgetting that the reconstructed value is an estimate whose accuracy the
case never actually lets anyone verify — a Hero who argues "Option A is better because now we have
a complete dataset" has quietly promoted an assumption to a fact. The case's real point is that
neither option produces a dataset anyone can fully trust for that one member; Option A trades a
visible gap for an invisible one.

**A sharper version of the same trap, confirmed by a fresh cold-read of this case:** D1's
reconstructed value is *solved for* using Appendix C's cached mean — so Option A's new 52-member
mean will always come back extremely close to that same cached mean, by construction, not by
discovery. A Hero who then checks "does my new mean match the last verified statistic?" and treats
a match as *proof the reconstruction worked* has reasoned in a circle: the formula was built to
produce exactly that match. Watch for this in D4 — a Hero citing "my reconstructed mean confirms
Appendix C's number" has not actually tested anything.

## Twist

**Twist:** During the Data Deep Dive, reveal that Sam's labmate has just found a mirrored backup
of the export tool's database on a shared drive — untouched by tonight's corruption. It is real
and it does have a complete row for the missing member. But it is a snapshot from a **different
week's crawl of this same circle** (not tonight's), and cross-checking it against tonight's other
51 rows to see whether anything else has changed would take about 45 minutes to parse by hand —
leaving very little runway before the midnight deadline. Ask: *"You have sixty seconds. Do you
spend the 45 minutes cross-checking a number that still isn't tonight's true value either, or do
you submit now with the choice you already made?"* This does not hand anyone the true answer — the
mirrored snapshot is itself just another imperfect, not-quite-current source, structurally similar
to MA1 — but it invalidates the "there is no way to check anything" premise several Heroes will
have leaned on to justify picking quickly, without crowning either option correct.

## Anchor Ladder

#### Intro
Frame the format: no answer key, defend your choice to peers. Opener: *"Sam has one blank cell
and a midnight deadline. Which sticky note goes in the email tonight?"*

#### Launch
Show the 51-member frequency table (Appendix B) with one row blacked out. Ask: *"If we're
missing exactly one number out of fifty-two, why does it matter which way we handle it?"*

#### Anchor 1 — Take a stand and vote.
Option A or Option B. No reasoning yet. Hands up for each. Write the split on the board.
*"Is anyone courageous enough to stand with 'we don't actually know'?"*

#### Anchor 2 — What is the problem we're solving?
Do not let them calculate yet.
- Is the question "which option is more accurate"? "Which option is more honest"? Those are
  different questions with different answers — say which one out loud.
- Someone will say "just reconstruct it, math doesn't lie." Whose math? Built on what?
- Let the confusion grow. *"Wow, this is a harder question than it looked."*

#### Anchor 3 — What is the process?
- If we reconstruct the missing value, are we done — do we trust it the same as the other 51?
- If we drop it, have we actually made the dataset MORE honest, or just smaller?
- Is our question still the right question?

#### Anchor 4 — What don't we know?
- Where does the "last verified mean" in Appendix C actually come from, and how sure are we it's
  still true tonight?
- Have them re-run D1 with the mean pushed 25% higher and 25% lower. How much does the
  reconstructed value move?
- What are we assuming about how much this one friend circle changes in five weeks?

#### Data Deep Dive
Now, and only now, work through D1–D5 with the real sourced/derived numbers.

#### Twist
Drop the mirrored-backup reveal (above), slowly, with pauses.

#### Close
Re-vote. *"Did we ask the right question? What math was new to you, and how did you attack it?"*

#### Lessons Learned / Standards Touched On
Mean, Outlier, How to find a missing data element given the mean and the remaining elements of
its set, How to create a box and whisker plot given a set of data — see Appendix D.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote — no explanation |
| 3:00–10:00 | Position defense: "Convince us it's the more defensible choice, not just the more complete-looking one" |
| 10:00–15:00 | Pressure-test the models: "Whose recommendation is most fragile if the five-week-old mean is wrong?" |
| **15:00** | **DROP THE TWIST** — the mirrored-backup reveal, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke in your model?" |
| 20:00–30:00 | Threaded deep conflict (2–3 named threads): honesty-about-a-gap vs. completeness-of-the-record; whether "the math ties" should ever be the end of an argument; what "trust the data" even means when part of it is missing |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Cohort Bands

| Band | Typical size | What changes |
|---|---|---|
| **Full** | 12–16 Heroes | The Socratic plan and Anchor timings run as written above. |
| **Compressed** | 6–8 Heroes | Anchors 2–3 combine into one pass; the twist still drops at 15:00 but the deep-conflict section (20:00–30:00) runs one thread instead of two or three — the honesty-vs-completeness thread is the strongest single thread if only one fits; total runtime shortens proportionally, not the content. |
| **1:1 / pair** | 1–2 Heroes | There is no vote to take — Anchor 1 becomes a stated initial position instead of a show of hands. The guide plays devil's advocate directly, arguing the other option, rather than cold-calling peers. The twist still lands, but "who reverses" becomes "would you reverse, and why — walk me through your D1 and D4 numbers again." |

## Sensitivity Note

See the Robustness Check section above — this is the load-bearing note for this case. SPEC §6's
subject-matter sensitivity note does not apply here (no death-toll/casualty/hardship framing — a
data-integrity decision in an academic setting). The **numeric robustness check on the circle's
only stated assumption (MA1)** has been run and **passed by construction**: the primary metric and
winner (a structural 0.00% tie) are mathematically independent of MA1's value and cannot flip
under any flex, verified across the required ±50% band and a wider 0×–3× stress test in
`sensitivity_model.py`. `case.json.sensitivity_disclosure[]` is correctly empty — nothing swept
threatens the winner or breaches SPEC §2's 20% cap, since the base margin is already 0.00%. The
one genuine, disclosed sensitivity that remains is **the reconstructed VALUE itself** — not a
fragility in the case's balance test, but the entire point of the discussion (Socratic Questions
2 and 3).
