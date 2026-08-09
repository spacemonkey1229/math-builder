# Guide Notes: Baseball Lineup

**Case:** Baseball Lineup · **Tier:** T2 · **Band:** MS · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (12 skills — decimal division,
fractions, rounding, percent, mean, comparison, bar graph, and the Fundamental Counting Principle)

Legacy conversion, 2026-08-01, reformatted from the original 2020-21 Guide Notes
(`source/Y3/Additional/Baseball Lineup/Guide Notes.docx`) onto the current 11-anchor ladder. The
original recorded 5 anchors (Anchor 1–4 + Lessons Learned) and two informal twists; this version
keeps the original's real narrative beats (Paul's cameo, the order-matters question) but grounds
the formal Twist in real Appendix A arithmetic instead of an unquantified opinion.

## Intro

Frame the format: this is not a stats worksheet, it's a hiring decision Carly has to defend out
loud, using math two candidates already handed her without knowing it would be graded. Name the
opener — "You have two folders. Same résumé, same interviews. One phone call left before you have
to pick."

## Launch

Read Ash's and Venicia's two lineups aloud, batting order and all (Appendix B), with no stats
attached yet — just the two lists of names side by side. Ask: "Just from the fact that they picked
different people, what do you think each one was optimizing for?" Do not confirm or correct
answers here; the point is a gut read on strategy before anyone touches a calculator.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who would hire Ash? Who would hire Venicia?" Show of hands, both options, no discussion. Record
the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'the better lineup'?"**

Let confusion grow here, deliberately. Heroes will want to jump straight to "whoever has the
higher average wins," but push: "Is it just as simple as identifying the best batters, or does the
order they bat in matter too?" — the exact question the original 2020-21 Guide Notes recorded. If
the room lands on "we need to define 'better' before we can measure it" on its own, that's the case
working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has a working definition of "better," ask them to name the actual steps before
touching Appendix A: compute each player's batting average, compute each lineup's combined figure,
decide whether to also look at power. Re-ask: "Do we agree on that algorithm? How did you get these
numbers?" — straight from the original Guide Notes' own Anchor 3 language.

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix C's two real conventions honestly: at-bats exclude walks, and percentages use
plate appearances as the denominator — both are stated rules, not something to derive, and mixing
them up is the single most common error. Ask which convention actually changes a Hero's answer if
they get it backwards (both do).

## Data Deep Dive

Now, and only now, the numbers. Walk the batting-average table (D1) and the combined-vs-mean
comparison (D3) together as a room, cold-calling for the rounding convention specifically — this
is where a Hero who skipped Appendix C visibly disagrees with everyone else's numbers, which is
useful information for the facilitator, not a moment to rescue.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"You're walking down the hall with your recommendation ready. Paul — the assistant Ash or Venicia
would be replacing — stops you. 'Before you send that,' he says, 'have you actually counted the
home runs?'"

**Facilitator-only: what the numbers actually do (`case.json.derived`).** Ash's lineup leads on
combined batting average, .514 to .475 — an 8.2% edge, the number most Heroes will have already
computed and committed to by this point. But Venicia's lineup combines for 39 home runs against
Ash's 24 (62.5% more), and a team slugging percentage — total bases per at-bat, the standard
measure of raw power — of .958 against Ash's .917, a 4.5% edge in the *other* direction. Both
numbers are real, both come from the same Appendix A table every Hero already has, and no
deliverable explicitly asked for team home-run totals or slugging — so most groups will not have
computed it unprompted. **The twist does not overturn the batting-average verdict; it puts a second,
equally real verdict next to it that points the other way.**

Do not tell a Hero which number should win. If asked "so which one is right," the honest answer is
"they're both right — they're measuring different things, and Carly has to decide which one tells
her more about how Venicia and Ash think, not just how their picks perform." That framing question
is the whole point of the twist, not a script to hand over unprompted.

## Immediate recommit

Re-vote immediately. Ask by name: "What just broke in your model? Were you wrong — or just missing
a number you hadn't thought to compute yet?" That distinction is the transferable skill, not the
vote itself.

## Deep conflict — three threads (20-30 min)

1. **Average vs. power.** Two real, correct numbers point in opposite directions. Is there a
   principled reason to trust one over the other for *this specific job* — evaluating a hire, not
   just a roster — or is picking one a value judgment dressed up as math?
2. **Whose lens is Carly's own?** Carly grew up around a hitting coach, not a general manager who
   thinks in slugging percentages. Does her own background make her more likely to weight average
   over power, and should Heroes correct for that or work with it?
3. **The Paul problem.** Paul, who raised the home-run question, later turns out to be close with
   Venicia's family. Does knowing that change how much weight his question should carry — even
   though the numbers he pointed at are real either way?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read both lineups aloud, cold-call for a gut read on strategy, no stats yet |
| 3:00–10:00 | Position defense — *"Convince us why your candidate's lineup is better, not just different"* |
| 10:00–15:00 | Pressure-test the models — *"Whose combined average is doing the most work in your pitch?"* |
| **15:00** | **DROP THE TWIST** — Paul's home-run question, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (average vs. power; Carly's own lens; the Paul problem) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

A Hero computes combined batting average, finds Ash ahead, and stops — treating the first real
number they calculated as the whole answer. The case's real tension is that "ahead on average" and
"ahead on power" are two different, equally defensible claims from the same data, and Carly's
actual job is to decide which one should carry more weight in a hiring decision, not to find the
one true number. Watch for a pitch that reports one statistic and calls the case closed.

## Socratic questions

1. Ash's lineup leads by 8.2% on combined batting average — what would Venicia's lineup need to add or change to close that gap?
2. Venicia's lineup leads by 4.5% on slugging percentage — is a 4.5% edge on power as meaningful as an 8.2% edge on average, or are these two numbers not actually comparable at all?
3. If Carly values "gets on base reliably" over "hits for power" for this specific front-office job, is that a fact about baseball or a fact about what she thinks the job actually needs?
4. Your D5 answer said there are 362,880 possible batting orders for either 9-player lineup — why doesn't that number change who Carly should hire?
5. Paul's home-run question turned out to matter mathematically, but he also turns out to have a personal connection to Venicia — does that connection make his question less trustworthy, even though the numbers behind it are real either way?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't
move at all after the twist is worth asking about directly: did the power numbers not land, or did
the room already have both lenses in mind?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes reached for slugging percentage on their own before the twist, or whether every
  group needed Paul's prompt.
- Whether the at-bats-exclude-walks convention (Appendix C, Assumption 1) was the place most Heroes
  actually got tripped up, matching the guide's prediction.
- Whether D5's batting-order count landed as a genuine "oh, that's why order doesn't matter" moment
  or felt like a disconnected extra task.

## Standards Touched On

Fractions · Percent · Rounding · Mean · Bar Graph · Fundamental Counting Principle · How to divide
decimal numbers · How to convert numbers to percents · How to round a number to a specified place
value · How to find the mean of a set of data · How to compare two or more values · How to apply
the Fundamental Counting Principle to count outcomes

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes here are a hiring decision and workplace comparison, not
personal loss, illness, or hardship.
