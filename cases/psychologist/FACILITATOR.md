# Guide Notes: Psychologist

**Case:** Psychologist · **Tier:** T3 · **Band:** MS-stretch / HS-entry · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (7 skills — ratio, percent, percent
conversion, mean, comparison, bar graph)

Legacy conversion, 2026-08-20, reformatted from the original source Guide Notes
(`source/Y3/Additional/Psychologist/Guides Notes.docx`) onto the current anchor ladder. The
original recorded 4 named anchors plus a discriminatory "Twist" (converting AFCR to single-gender
admissions, framed around which gender "produces better court reporters"). **That framing is
discarded entirely and does not appear anywhere below** — not as content, not as a contrast, not
as a "here's what we changed" aside. This guide keeps the original's real narrative beats (Paul's
sticky note and phone call, the folder of 27 real applicants, the single-day deadline) and builds
an entirely new Twist grounded in the case's own Appendix B data.

## Intro

Frame the format: this is not a stats worksheet, it's an admissions decision Harriet has to
defend out loud, using real test data on 27 kids who don't know they're about to be ranked two
different ways. Name the opener — "Harriet has one folder, three seats, and until tomorrow
morning."

## Launch

Read Appendix A's five test descriptions aloud, with no scores attached yet — just what each test
measures. Ask: "If you were building a program that trains the country's best court reporters,
which of these five things would you weight most heavily, and why?" Do not confirm or correct
answers here; the point is a gut read on what "best" should mean before anyone touches a number.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who would build the Standout Slate — reward the specialists? Who would build the Balanced Slate —
reward the generalists?" Show of hands, both options, no discussion. Record the count — Close will
ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'the best three'?"**

Let confusion grow here, deliberately. Heroes will want to jump straight to "just add up the
scores," but push: "Is it just as simple as finding the highest numbers, or does it matter *how*
you combine five differently-scaled tests into one ranking?" If the room lands on "we need to
agree on how to compare a memory-test score to a typing speed before we can rank anyone" on its
own, that's the case working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has a working sense of "we need a common scale," ask them to name the actual steps
before touching Appendix B: convert every raw score to a percent of the category's best score
(Appendix C, MA1), then either take each applicant's best percent or average all five. Re-ask: "Do
we agree that's the algorithm? What would change if we picked a different one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix C's two load-bearing assumptions honestly: MA1 (normalize against this year's
pool's own best score, not an external maximum) and MA2 (weight all five categories equally,
absent evidence any one predicts success better). Ask which one a Hero would challenge first if
they were an excluded applicant's family — both are real, defensible, and both are *choices*, not
facts.

## Data Deep Dive

Now, and only now, the numbers. Walk the normalized-score table (D1) and the two per-applicant
figures (D2 — single-best and composite) together as a room, cold-calling for which normalization
basis a Hero used. This is where a Hero who skipped Appendix C visibly disagrees with everyone
else's numbers, which is useful information for the facilitator, not a moment to rescue.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Harriet's phone rings. It's Paul. 'Before you send the list — Sophia just called. She's
withdrawing. She accepted a full scholarship at a rival transcription program an hour ago.' Sophia
— the applicant every single Hero in this room ranked #1 on both lists — is gone. You have five
minutes. Recompute both slates without her."

**If a Hero asks whether the category maximums (Appendix B's bottom row) should be recomputed now
that Sophia is out of the pool: no.** Appendix C's MA1 fixes those maximums once, from the
original 27-applicant field — they do not shift when someone later withdraws. This matters here
because Sophia held or tied the pool max in three of five categories; a Hero who re-derives new
maximums from the remaining 26 applicants will get a different, messier answer (several ties at
100%, and a different third seat on the Balanced Slate) than the one below. That's a legitimate
modeling choice to surface if a sharp Hero raises it — "why should Sophia's number still set the
bar for a competition she's no longer in?" is a fair question — but the case's own convention,
stated in MA1, is to keep the scale fixed.

**Facilitator-only: what the numbers actually do (`case.json.derived`).** With Sophia removed, the
Standout Slate becomes Spencer, Riley, Tyler (Tyler moves up to the third specialist seat) and the
Balanced Slate becomes Tyler, Brigitte, Riley (Riley moves up to the third generalist seat). The two
rosters now **share two of three names** — Tyler and Riley appear on both. The entire disagreement
that felt like it spanned three seats collapses to exactly one: **Spencer** (the Standout Slate's
pick) **vs. Brigitte** (the Balanced Slate's pick) for the final chair. Neither slate's own metric
flips which philosophy wins overall (Standout still leads on average best-score; Balanced still
leads on average composite) — the margins narrow slightly, but the practical fight in the room
should visibly shrink from "three names each" to "one name each."

Do not tell a Hero which of Spencer or Brigitte should get the seat. If asked "so which one is
right," the honest answer is "you were arguing about three names, and now you're really only
arguing about one — does that change how confident you are in either philosophy?"

## Immediate recommit

Re-vote immediately. Ask by name: "What just broke in your model? Were you wrong — or just missing
information you hadn't needed yet?" That distinction is the transferable skill, not the vote
itself.

## Deep conflict — three threads (20–30 min)

1. **Spencer vs. Brigitte, head to head.** Spencer is AFCR's fastest typist in the pool by a wide
   margin but posts the weakest memory-test showing of anyone discussed today. Brigitte never
   leads the pool in any single category but has no real weakness either. Which one would you
   actually want transcribing a live, high-stakes trial tomorrow?
2. **MA1 vs. MA2 — which assumption is doing more work?** Ask the room to vote: if you had to
   change exactly one of Appendix C's two load-bearing assumptions, which would move the needle
   more — how scores are normalized, or how the five categories are weighted? Have them defend it
   with a number, not a hunch.
3. **Harriet's own accountability.** She funds AFCR herself and answers personally if its
   reputation slips. Does that change what kind of applicant she should actually want — insurance
   against one weak spot (Balanced), or a shot at producing the single most spectacular graduate
   AFCR has ever had (Standout)?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read the five test descriptions aloud, cold-call for a gut read on what should matter most, no scores yet |
| 3:00–10:00 | Position defense — *"Convince us your slate is better, not just different"* |
| 10:00–15:00 | Pressure-test the models — *"Which of your three names is most fragile if the numbers moved a little?"* |
| **15:00** | **DROP THE TWIST** — Sophia withdraws, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (Spencer vs. Brigitte; MA1 vs. MA2; Harriet's own stakes) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will build whichever ranking they land on first, assume it is simply *the* answer, and
never build the other one to discover it disagrees. They will assume "best single score" and "best
composite score" must land on the same three names — the case's real tension is that they don't,
and Harriet's actual job is to decide which reading she trusts more, not to find the one true
ranking. Watch for a pitch that skips building both required rankings (D3 explicitly requires both)
and calls the case closed.

## Socratic questions

1. The Balanced Slate leads by 9.3% on composite score — what would the Standout Slate need to change about even one applicant's profile to close that gap?
2. Sophia was #1 on both of your original rankings — why did losing just one applicant out of 27 collapse the disagreement between the two methods from three seats down to one?
3. Spencer posts the pool's single fastest typing speed by a wide margin but the weakest showing on Test 3 of anyone discussed today — is an applicant's single best skill more predictive of future success than their weakest one, or less?
4. Appendix C's MA1 scales every category to *this year's* best score, not a fixed external maximum — what would happen to every applicant's normalized scores in a year with a much stronger (or much weaker) applicant pool?
5. If AFCR is funded entirely out of Harriet's own pocket and her reputation is on the line personally, does that make her more likely to want a Standout Slate or a Balanced Slate — and is that a fact about test scores, or a fact about what Harriet personally has to lose?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't
move at all after the twist is worth asking about directly: did the Spencer-vs-Brigitte question
not land, or did the room already see both sides coming?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes built both required rankings (D3) before committing, or whether most groups built
  only the one that matched their gut read from the Launch.
- Whether the MA1-vs-MA2 question in the deep-conflict thread produced a genuine debate about which
  assumption matters more, or whether most groups treated both as equally arbitrary.
- Whether the Sophia-withdrawal twist's "the fight collapses to one seat" framing landed as intended,
  or whether Heroes needed more prompting to notice the two rosters now share two names.

## Standards Touched On

Ratio · Percent · Mean · Bar Graph · How to convert numbers to percents · How to find the mean of a
set of data · How to compare two or more values

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes are a competitive admissions decision, not personal loss,
illness, or hardship. Facilitators should still be aware that some Heroes may personally know
someone who didn't make a selective team or program, and can find exclusion decisions resonant;
no case-specific content changes are needed. Note for any facilitator familiar with this case's
legacy version: the original single-gender "Twist" concept from the source Guide Notes is not part
of this case in any form and should never be introduced, referenced, or improvised into a
discussion of this case.
