# Facilitator Guide — Movie Executive

MS | Guide Notes | 2026-27

*Adapted from the original 2021 "Movie Executive" Guide Notes (source/Y1/Session 5/Movie
Producer/Guide Notes.docx), rebuilt to this pipeline's five-anchor / timed-plan / twist format.*

---

## Intro

You are launching a case about a studio executive who has to pick between two competing films
using nothing but test-audience survey data and a production budget. Frame it as: "Every year,
studios green-light movies that lose tens of millions of dollars — and every year, some of those
decisions looked reasonable on the page." Play or describe a short clip or headline about a real
box-office bomb to set the stakes before revealing the two folders on Rebecca's desk.

---

## Launch

Read the Overview aloud, or have a Hero read it. Stop exactly where the case stops — Rebecca
reaching for the legal pad, the marketing team still waiting on her call. Do not preview the
Dilemma yet.

---

## Anchor 1

**Take a stand and vote.** No reasoning yet, just commit: "Is anyone courageous enough to stand
with Waves In The Tales? With The Flower's Ice?" Get a show of hands or a stand/sit vote. Record
the count — you will need it again at Close.

Let confusion and chaos grow a little here. If someone asks "wait, which one has better data?"
before the vote, say "hold that thought" and take the vote anyway.

---

## Anchor 2

**What is the problem we're solving?**

- "Is this just about which survey had more people, or is there something else we need to
  consider?"
- "What do you mean when you say Flower's Ice's data is 'better' — better how?"
- "Is this the right question, or are we actually trying to answer something more specific?"

Let the room arrive, on its own, at something like: *we're trying to predict how a film will
actually perform, and weigh that against what it costs* — not just "which survey is bigger."

---

## Anchor 3

**What's the process we're going to go through?**

- "If we just count total survey respondents — 87 vs. 835 — and stop there, will we have
  actually answered the question?"
- "What would we need to do with each film's (score, price) data to turn it into a dollar
  prediction?"
- "Once we have a projected revenue for each film, how do we decide — do we compare the raw
  dollar totals, or something else?"

Re-ask: "Is our question still the right question?" Push toward: *we need a rate or ratio that's
comparable across two very differently-priced films, not just a raw total.*

---

## Anchor 4

**What don't we know that would be critical here?**

- "Do we know how many people nationwide will actually consider seeing either of these films on
  opening weekend? Do we need to?"
- "What do we assume, and what do we look up?"

Point Heroes at Appendix E's stated assumption (the addressable-audience number) as *exactly*
this kind of gap — a real quantity nobody in the room can look up, that the case has to state
and defend rather than pretend to know.

---

## Data Deep Dive

Now, and only now, the numbers. Walk the room through building both scatter plots on the board
side by side. Let Heroes discover for themselves that Waves' 15-point dataset lines up almost
perfectly (r ≈ 0.97) while Flower's Ice's 23-point dataset is visibly noisier (r ≈ 0.80) even
though it has more points. Do not tell them which correlation is "better" — ask them what a
tighter line of best fit means for how much you can trust a prediction built from it.

---

## Twist

**Drop this at roughly the 15-minute mark**, slowly, with pauses:

> "Marketing just forwarded something else. A national research group — Pew Research Center —
> studied exactly this problem: when you survey people who *chose* to be somewhere (like a
> convenience sample gathered inside a movie theater) instead of picking them at random, how much
> can you fix that bias afterward with statistics? Their answer, across 24 real benchmark tests:
> the best correction techniques recovered only about **30%** of the bias. Roughly 70% of the gap
> between a convenience sample and a true random sample doesn't wash out, no matter how you weight
> the numbers afterward."

**Follow-up, immediately:** "You now have 60 seconds. If only 30% of Flower's Ice's *extra*
enthusiasm over Waves' definite-buyer rate is trustworthy signal — and the rest is just who
happened to be standing in that theater lobby that day — does that change your position? Whose
plan is most fragile to this?"

The math: Flower's Ice's definite-buyer rate (34.78%) exceeds Waves' (26.67%) by an "excess" of
8.11 points. Keeping only 30% of that excess as trustworthy (per the Pew finding) and applying it
to Flower's Ice's own $8.625 average price drops its revenue-per-production-dollar from $0.2332
to roughly $0.1951 per dollar — widening Waves' lead from a thin **13.8%** margin to a decisive
**36.0%**. The winner does not flip — Waves was already ahead — but the twist **invalidates anyone
who argued "it's basically a toss-up, so go with the bigger number."** It is not close anymore
once the sample's real reliability is priced in.

**Unstated convention, disclosed here:** this calculation treats Waves' own observed definite-buyer
rate (26.67%) as the "un-biased" reference point, and corrects only the *excess* Flower's Ice shows
above it — it does not treat either film's number as an independently-known ground truth, since
neither survey is a true national random sample. This is a reasonable but not the only defensible
convention: a Hero could instead apply the 30% retention directly to the dollar gap between the two
films' projected revenues, which produces a somewhat larger margin (~42.6%) but the same winner. If
a Hero pushes on "why does Flower's Ice's bias correct toward Waves' specific number," the honest
answer is: it doesn't have to — any reasonable way of discounting Flower's Ice's convenience-sample
excess widens Waves' lead, because Waves was already ahead before the twist. The twist is designed
to be robust in direction, not in exact magnitude.

**What just broke?** Ask: "Were you wrong, or just missing information?" This directly punctures
the wrong-path reasoning named in the next section.

---

## Close

**Vote again.** "We asked: which film should Rebecca green-light? Did we ask the right question?"

- "Did anyone move after the Twist? Why?"
- "What math was new to you in this case, and how did you attack it — Google, a fellow traveler,
  something else?"
- "If you got a similar case next time, what would you check first?"

---

## Lessons Learned

A bigger sample is not automatically a better sample. Flower's Ice's 835-person convenience
sample sounds like overwhelming evidence next to Waves' 87-person phone survey — until you notice
*how* each sample was gathered. Sample size and sample quality are different axes, and this case
is built so that the "obviously bigger" option is not the one with the tighter, more trustworthy
signal. The second lesson is normalization: comparing raw dollar totals instead of a rate
(revenue per production dollar) is the single most common way Heroes talk themselves into the
wrong recommendation here.

---

## Standards Touched On

Scatter Plot · Line Of Best Fit · Correlation · Slope · Sample · Population · Sample Size ·
Random · Stratified Sampling · Convenience Sampling · Mean · Percent · Decimal — plus the nine
"how to…" procedures in Appendix F of `case.md`.

---

## The Trap

**Heroes will treat "bigger sample" as automatically "better evidence."** Flower's Ice's raw
survey numbers (835 people, 23 responses, higher definite-buyer rate, higher average price, and a
larger raw projected revenue of $24.0M vs. $17.1M) all look more impressive on their face than
Waves' smaller, cheaper, quieter dataset. A Hero who stops at "bigger number wins" will pick
Flower's Ice — without checking (a) that the sample was gathered by convenience, not randomly,
which threatens generalizability, and (b) that the fair comparison is revenue *per production
dollar*, not raw revenue, since Flower's Ice also costs 60% more to make. Both mistakes point the
same direction, which is exactly what makes the trap effective: a Hero doesn't have to make only
one error to land on the wrong recommendation.

---

## Balance (facilitator-only — never state this in case.md)

| | Waves In The Tales | The Flower's Ice |
|---|---|---|
| Production budget | $64,300,000 | $102,900,000 |
| Sample | n=87 phone, stratified random (n=15 shown, 13-30 stratum) | 835 approached, convenience (n=23 usable) |
| Correlation (r) | 0.9704 | 0.7982 |
| Definite-buyer (top-2-box) rate | 26.67% (4/15) | 34.78% (8/23) |
| Definite-buyer mean price | $8.00 | $8.625 |
| Projected opening-weekend revenue (MA1 = 8,000,000) | $17,066,667 | $24,000,000 |
| Revenue per production dollar | $0.2654 | $0.2332 |

**Argument for A:** the smaller, cheaper film's survey is almost perfectly linear (r=0.97) and
was gathered by stratified random sampling, so its definite-buyer rate is the more defensible
real-world prediction; its revenue-per-dollar leads.

**Argument for B:** the sheer scale of a 835-person reach and a higher definite-buyer rate and
price nearly close the gap despite the convenience-sample's weaker generalizability and Flower's
Ice costing 60% more to produce.

**Margin: 13.8%**, Waves In The Tales ahead on revenue-per-production-dollar. Under the Twist's
Pew-sourced bias correction, the margin widens to roughly 36% — the winner does not change, but
the case for treating this as "close" collapses.

**Five Socratic questions** (answerable only with this case's numbers):

1. Waves' definite-buyer rate is 26.67% from just 15 respondents. Flower's Ice's is 34.78% from
   23. How many more (or fewer) definite buyers would Flower's Ice need, out of its same 23, to
   match Waves' revenue-per-dollar exactly?
2. If the addressable-audience assumption (8,000,000) were cut in half, whose recommendation
   would you have to rewrite — and whose would stay exactly the same?
3. Waves' correlation is 0.97 and Flower's Ice's is 0.80. If you had to bet real money on which
   film's survey data predicts real ticket sales more accurately, which correlation number
   would you trust — and what would have to be true about *how* each sample was gathered for
   that trust to be justified?
4. The Twist says only 30% of Flower's Ice's "excess" enthusiasm over Waves is trustworthy. What
   if it were 60% instead — does Waves still win?
5. Flower's Ice's raw projected revenue ($24.0M) beats Waves' ($17.1M) by nearly $7M. Why is that
   the wrong number to base Rebecca's recommendation on?

---

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote on A vs. B — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just bigger" |
| 10:00–15:00 | Pressure-test the models: "Whose plan is most fragile? What haven't we checked about how each survey was actually gathered?" |
| **15:00** | **DROP THE TWIST** — the Pew Research correction-bias finding, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke in your original model?" |
| 20:00–30:00 | Threaded deep conflict — Thread 1: sample size vs. sample quality; Thread 2: raw revenue vs. revenue-per-dollar |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

---

## Cohort Bands

**10-16 (Full):** the plan and Anchor timings above run as written; both scatter plots go up on
the board side by side.

**5-9 (Compressed):** Anchors 2-3 combine into one pass; the 20:00–30:00 deep-conflict block
drops to one thread instead of two; total runtime shortens proportionally, not the content.

**1-2 (1:1/pair):** there is no vote to take — Anchor 1 becomes a stated initial position instead
of a show of hands; the guide plays devil's advocate directly; the Twist still lands but "who
reverses" becomes "would you reverse, and why."

---

## Sensitivity Note

The case's verdict is intentionally *insensitive* to the size of Appendix E's national
addressable-audience assumption (MA1 = 8,000,000) — that figure scales both films' projected
revenue equally and cancels out of the revenue-per-dollar ratio between them. What genuinely
drives the case's thin 13.8% margin is each film's own survey-derived definite-buyer rate and
price, weighed against its own budget. See the Twist above for the one input that *does* move
the margin materially.
