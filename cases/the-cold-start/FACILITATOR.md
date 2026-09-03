# FACILITATOR.md — The Cold Start

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Cold Start · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Matrices — Matrix, Matrix Dimension, Determinant, Identity Matrix, and their three
how-tos (see `case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-01) — all 11 `{{NEEDS_SOURCE}}` tokens closed (6
SOURCED, 5 ASSUMPTION, 0 DROPPED, 0 OPEN; see `RESEARCH_LOG.md`). `case.json.status` is
`"researched"`. `margin_pct` is `4.76` (see the Balance section below) — not `null`. Not yet run
through `case-qa`; treat the numbers as sourced-and-computed but not yet QA-adjudicated.

## Real-world grounding (for the facilitator's own background, not for case.md)

- **GroupLens Research, MovieLens 25M Dataset** — real, published, 25,000,000 ratings across
  162,000 users and 62,000 movies, i.e. a real user-item matrix that is 99.75% empty even at
  full maturity. This is the grounding fact that makes Appendix C's "sparse, not empty" framing
  real rather than invented.
- **Rashid, Albert, Cosley, Lam, McNee, Konstan, Riedl — "Getting to Know You" (IUI '02)** — the
  real MovieLens platform's actual 2002 onboarding design literally asked new users to rate pages
  of ten movies until they'd rated ten or more, exactly Option B's mechanic, not an invented
  premise. Their live online experiment measured real dropout: 49 of 351 users (13.96%) abandoned
  before finishing. This is the strongest real precedent in the case, and also the one place a
  Hero is most likely to over-trust a dated (2002), self-selected research population as if it
  were a 2026 general-audience number — see the Twist.
- **Gomez-Uribe & Hunt, "The Netflix Recommender System" (ACM TMIS, 2015)** — real, ~80% of hours
  streamed at a real major platform are influenced by its recommender system. Useful for Anchor
  2/Intro framing on why this decision is worth Priya's forty minutes at all, not why either
  specific option is correct.
- **Baymard Institute, Cart Abandonment Rate Statistics** — real, 17% of US online shoppers abandon
  an order specifically over checkout complexity, in a flow far shorter and lower-friction than a
  10-item rating gate. Useful as a floor, not a transferable number — a Hero who tries to use 17%
  directly as the Ratings Gate's dropout rate has under-scaled the friction difference.

## Intro

Frame the format: this is a real product decision under a deadline, not a worksheet. Name the
opener — "You have forty minutes to decide what a brand-new account sees on its very first
screen. One version shows something instantly. The other version makes them work for it first.
You don't get both, and the metric your bosses agreed to use isn't the one that makes either
option look easy." Mention, once, that real streaming platforms measure recommender influence in
double digits of viewing hours (Netflix, ~80%, S3) — this is a real, high-stakes design space, not
an academic toy.

## Launch

Show the two mockups exactly as the Overview describes — the instant shelf, and the ten-poster
gate with the grey button — with no numbers yet. Ask: "Which one would you ship, just from what
you see here?" Do not confirm or correct. Record the split; Close will re-ask it.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Ratings Gate — the version that makes a brand-new
visitor do ten things before the app shows them anything?" Show of hands, both options, no
discussion yet. Record the count.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'personalized'?"**

Let confusion grow here on purpose. Heroes will want to jump straight to "which one gets more
clicks," but push on what the metric actually counts: "If the Ratings Gate reliably surfaces the
premiere for everyone who finishes it, does that mean it's the better choice — or does it depend
on how many people never finish?" If the room lands on "clicks per person who finished is a
different number than clicks per person who started," the case is working as designed — this is
the whole reason Appendix D exists.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "does the personalization actually work" from "does the metric hide the
cost of getting it," ask them to name the steps before touching the appendices: compare the two
matrices' dimensions and sparsity (D1); work the addition example and connect it to why Option A
is mathematically "do nothing" (D2); check whether the adjustment matrix is reversible (D3); solve
the weighted-blend system (D4); and use all of that, plus Appendix D's table, to recommend (D5).
Re-ask: "Is our question still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: Northline is fictional, so its actual click-through rates and its
actual 2026 sign-up cohort's patience are both open `{{NEEDS_SOURCE}}` tokens that could only be
closed as stated Modeling Assumptions (MA2, MA3, MA4) — not independently verified the way the
*matrix scale* (MovieLens, real) and the *mechanic itself* (rate 10 before recommendations, real,
per Rashid et al.) could be. Ask which of the open assumptions is actually load-bearing. The honest
answer: MA3 (the modeled 2026 dropout rate) is the single most load-bearing open item in the whole
case — using the literal 2002 MovieLens number instead pushes the margin from a close 4.76% to a
lopsided 33.6%, which is a materially different question than "is the Ratings Gate better."

## Data Deep Dive

Now, and only now, the numbers (Appendices B, C, D, E). Walk D1's sparsity comparison, D2's
addition-and-identity argument, D3's determinant, and D4's system together as a room, cold-calling
for D5 specifically — this is where a Hero who did the matrix work correctly but never connects it
to Appendix D's per-100-starters table will visibly struggle to answer "so which one do you
actually ship, tonight."

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses, once Appendix D is worked: "The 13.96% dropout number in Appendix C
isn't invented — it's real. It's from a real live experiment, on the real MovieLens site, using
the exact same 'rate ten things before you get recommendations' design as the Ratings Gate. If we
use that real number instead of the case's modeled 40%, the Ratings Gate doesn't just win — it
wins by 33.6%, comfortably past the ~20% line this whole project uses to flag a case as not
actually close."

"So here's the twist: the more real your data gets, the less close this case is. Does that make
you trust the Popularity Path more, or does it make you distrust the 2002 number instead? What
exactly is different about the people who dropped out of a MovieLens research study in 2002 and
the people who'll open Northline this Friday because a friend texted them?"

**Facilitator-only: what this does and doesn't change.** The real 13.96% figure (S2) is not wrong
— it's a real, well-measured number from the closest possible real precedent. It is a *population*
mismatch (self-selected, patient, already-engaged research volunteers vs. impulsive 2026
friend-referral sign-ups), not a bad measurement. This is the case's own version of the
retune-vs.-hide distinction from `SPEC.md` §2: the case-research pass explicitly computed both
numbers, disclosed both, and only used the retuned 40% because a real, stated basis exists for why
the 2002 population undercounts modern dropout — not to make an inconvenient number disappear.

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote (Anchor 1) — no explanation. |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just faster or more personalized" (Anchor 2 — what does the per-100-starters metric actually reward?). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — name the D1-D5 steps, surface MA2/MA3/MA4 as open choices. |
| 15:00–25:00 | Data Deep Dive — D1-D5 together; cold-call D5's recommendation specifically. |
| **25:00** | **DROP THE TWIST** — the real 13.96% MovieLens dropout figure and what it does to the margin, delivered slowly, with pauses. |
| 25:00–30:00 | Immediate recommit: who reverses? "What just broke — the math, or your trust in which population it came from?" |
| 30:00–40:00 | Threaded deep conflict — see the three named threads below. |
| 40:00–45:00 | Close, re-vote, reflection, Lessons Learned. |

## Deep conflict — threads (20–30 min)

1. **A metric that scores completers only is not the same metric as one that scores starters.**
   The Ratings Gate wins by a landslide if you only count people who finished it — and loses real
   ground the instant you also count the ones who didn't. Push: "Whose idea was it to score by
   starters instead of completers, and what would the case look like if Priya's team had let
   Option B's own designers pick the metric?"
2. **A real number from the wrong population is still a real number.** The 13.96% dropout figure
   is not fabricated — it's a genuine, peer-reviewed, measured result. Push: "If you can't prove
   MA3's 40% is more correct than S2's real 13.96%, on what basis did the case actually choose
   40% instead of just using the real number?"
3. **"Sparse" is not "empty."** D1 forces the distinction between Option A's premiere-column (truly
   zero cells filled) and Option B's completer-row (only 10 of 62,000 filled, but real). Push: "If
   both matrices are almost entirely empty, why does only one of them actually work?"

## The trap

Heroes will treat Option B's completer-only click-through rate (35%, nearly double Option A's 20%)
as the whole story and recommend the Ratings Gate on that basis alone, without ever pricing in
Appendix C's dropout — missing that the case's own analytics team specifically forbade scoring
that way. A second, related trap: treating the real 13.96% MovieLens figure (S2) as automatically
more trustworthy than the modeled 40% (MA3) simply because it's "real data" — a Hero who does this
has not reckoned with the difference between a real number and a number measured on the right
population; the Twist exists specifically to force that distinction.

## Socratic questions

1. Appendix D scores both options per 100 starters, not per 100 completers. Compute what Option B's clicks-per-100 would be if the metric only counted completers instead — how much does that change which option looks better, and does it change which option Priya should actually ship?
2. The Ratings Gate's 13.96% real historical dropout figure comes from a 2002 research study, but the case uses 40% instead — is that a fair thing to do, and what would you need to know about Northline's actual 2026 users to decide whether 40% is too high, too low, or about right?
3. Option A's item-similarity matrix and Option B's completer-row are both mostly empty — use your D1 sparsity numbers to explain why "mostly empty" doesn't mean "equally useless" for the two options?
4. If Priya's team could add just one thing to Option A — say, a small manual boost for same-week premieres — would that close the gap with Option B, and what would that boost need to do mathematically to Appendix B's matrix?
5. Appendix E's identity-matrix framing says Option A is "the same as multiplying by I" — is that framing actually fair to Option A, or does it undersell what a pure-popularity ranking is doing?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare to Anchor 1's vote — a room that moves after the
twist should be pressed to explain the move using D1/D4/Appendix D, not just the twist's emotional
weight.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Matrix · Matrix Dimension · Determinant · Identity Matrix · How to add and multiply matrices · How
to find the determinant of a 2x2 matrix · How to solve a system of equations using a matrix

## Balance argument (SPEC §2)

**Argument for A (the Popularity Path).** Zero onboarding friction means literally all 100 starters
reach a recommendation shelf — nobody is lost to the flow itself. A real precedent shows even a
much shorter, lower-friction, already-purchase-intent flow (e-commerce checkout) already loses 17%
of users to complexity alone (S4); a 10-item rating requirement before a first-time visitor has
even decided whether they like the app risks losing meaningfully more. The premiere's own row and
column in the similarity matrix are completely empty on day one, but under the modeled 20%
click-through rate (MA2), a real fraction of all 100 starters still click it — and nobody is turned
away at the door to do so.

**Argument for B (the Ratings Gate).** Its personalization is real, not decorative: once an
account clears the gate, its own sparse row gives the system actual signal to match genre-relevant
content, converting at a modeled 35% among completers (MA4) — nearly double A's modeled 20% (MA2).
The required-ratings mechanic is not invented for this case: it is the literal onboarding design
the real MovieLens research platform used, live, with real users (S2). That same precedent also
measured real abandonment — 13.96% of a patient, already-engaged 2002 research population dropped
before finishing — and a modern, mobile-first, friend-referral cohort is modeled as dropping out
even more (MA3), which is exactly the cost the per-100-starters metric is designed to charge
against B.

**Margin — COMPUTED 2026-09-01 (case-research).** `margin_pct: 4.76`. **Winner: Option B, The
Ratings Gate** — by a genuinely close margin. Pass 1, using S2's literal real 2002 dropout rate
(13.96%, completion 86.04%): Option A = 20.0 clicks/100; Option B = 86.04 × 0.35 = 30.11
clicks/100; margin = 33.6% — over SPEC §2's ~20% cap. **One retune pass performed**, per SPEC §2's
own instruction: S2's real figure is from a dated (2002), self-selected, already-engaged research
population, not a general 2026 friend-referral streaming cohort — a legitimate constraint to
retune, anchored above two real cited floors (S2's own 13.96%, and S4's real 17% checkout-
complexity figure from an even shorter, lower-friction flow). Retuned to MA3 = 40% modeled 2026
dropout. Pass 2 (retuned): Option A = 100 × 0.20 = 20.0 clicks/100; Option B = 60.0 × 0.35 = 21.0
clicks/100; margin = (21.0−20.0)/21.0 × 100 = **4.76%.**

**What this means for facilitation.** This case's margin is genuinely close under the case's own
(disclosed, justified) modeling choice, and genuinely lopsided under the literal historical number
— both facts are true and both are in the case's own appendices for a Hero to find. The room's
real work is deciding whether MA3's retune is honest modeling or convenient cherry-picking; that
tension IS the Twist. Full arithmetic trail: `case.json.balance.margin_note`.

## Facilitator note — sensitivity (SPEC §6)

NONE. This is routine product-analytics/recommender-systems math — no subject-matter sensitivity
flag applies.
