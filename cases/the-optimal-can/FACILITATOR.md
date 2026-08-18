# Guide Notes: The Optimal Can

**Case:** The Optimal Can · **Tier:** T2 · **Band:** HS · **Studio:** Launchpad
**Standards:** Calculus / Applications Of Derivatives — the complete seven-skill group, all
`new_coverage` — plus three closely related Calculus/Derivatives skills also `new_coverage`
(derivative, instantaneous rate of change, power rule), plus two already-covered supports
(compound-unit conversion, percent of a number). Exact ids in `case.json.standards[]`.

**Status:** drafted at `case-write`, filled at `case-research`, both 2026-08-13. Every figure
quoted below resolves in `case.json.derived` once research completes.

## Intro

Frame the format before anything else: this is a real capital-request decision with Priya's name
on it, not a word problem about cylinders. Name the opener: *"You have one shot at Thursday's
capital review. The math has to hold up in the room."* Say plainly that both options are legal,
already-running proportions somewhere in the industry, and that the room's job is to decide which
one they would put their own recommendation behind.

## Launch

Show a real can-forming/necking line video or photo sequence — any public beverage-can
manufacturing footage works, as long as the room sees a flat aluminum disc become a can shape in
seconds. Ask one question and take answers without correcting any of them: *"If you could change
the shape of every can in the world by one millimeter, would it matter?"* Let the gut reads stand;
the Close revisits them.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

*"Is anyone courageous enough to stand with Priya on spending the retooling money?"* Stand-or-sit,
both options, no discussion permitted. Record the count — the Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'the better shape'?"**

Let confusion grow here; it is deliberate. The room will want to say "the one that uses less metal"
without asking less metal *per what*, or over *how many cans*. Push:

- *"Less metal costs less — but does it cost less than what?"* (Per can? Per year? Compared to the
  retooling bill?)
- *"If the better shape only saves two cents a year, does that change your vote?"*
- *"Whose money is the retooling bill, and whose money is the savings?"*

Do not resolve this. A room that leaves Anchor 2 arguing about *what* is being compared to *what*
is exactly where it should be.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Make them name the steps before any appendix is opened:

1. Write the surface area of a cylinder as a function of one variable, using the fixed volume to
   eliminate the other (D1).
2. Differentiate it and find where the rate of change is zero (D1, D2).
3. Prove that zero is a minimum, not a maximum (D2).
4. Convert the resulting shape's area advantage into a weight, then a dollar figure, per can (D3).
5. Scale the per-can dollar figure up to a year, and compare it against what the retooling costs
   and how long the plant is willing to wait for it back (D4).

Re-ask: *"Is our question still the right question, now that we can see the steps?"*

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gaps, all of which live in `case.md` Appendix D:

- The exact sheet gauge (thickness) of the aluminum Ridgeline currently buys is not public.
- The exact retooling cost for this specific die-and-tooling changeover is not public.
- Ridgeline's actual annual can volume on this line is not public — Ridgeline is fictional.
- Plant leadership's capital-approval payback ceiling is a stated company policy, not a published
  figure.

Ask which of these changes the recommendation if it moves, and which only changes the size of the
answer. All four are load-bearing here — unlike a case where one assumption cancels out, every
stated assumption in this case pushes the payback period in a real direction. That is itself worth
naming: a Hero who assumes this case must have one "safe" assumption and three decorative ones has
misread the structure.

## Data Deep Dive

Now, and only now, the numbers.

Work D1 → D4 as a room. Cold-call specifically on **D2**, the classification step: a Hero who
finds r* by solving dS/dr = 0 and stops has found *a* critical point, not *the minimum*. Fish for
the sentence *"how do we know this isn't the worst shape instead of the best one?"*

Two facilitator-only notes to hold in reserve:

- **The optimum is flatter than it looks.** S(r) is quite shallow near its minimum for a
  fixed-volume cylinder — being noticeably off the optimal aspect ratio costs surprisingly little
  area. This is *why* real cans are not built to the calculus optimum: ergonomics and shelf-stacking
  cost the industry very little in material to satisfy. Do not let the room assume "the standard
  can must be badly designed" going in.
- **A won on this run for a boring reason: the ceiling, not the shape.** The optimal shape really
  does use less aluminum, every single can, forever. It still loses because the retooling bill
  divided by the (small, real) annual saving takes longer to pay back than the plant is willing to
  wait — not because the math was wrong or the saving was fake.

Full worked figures are in `case.json.derived` and reproduced in the **Facilitator-only numbers**
section below.

## Twist

**Twist: N/A.** Research considered the natural candidate — a change to Ridgeline's annual volume
assumption (MA3), e.g. the brand client doubling its order — but every mechanically clean version
of that move only restates the break-even calculation D4 already asks the Hero to compute
(case.md D4, `case.json.derived.breakeven_annual_cans`). Introducing it a second time as a
mid-discussion "twist" would either leak the break-even figure early or require a second, distinct
unsourced number this case's research did not turn up a defensible basis for (SEE APPENDIX D — all
four stated assumptions are already load-bearing without a fifth). Rather than manufacture an
unsourced fifth dial to force a twist beat, this case ships without one; Anchor 4 and the Deep
Conflict section already carry the "what if the numbers move" pressure a twist would otherwise add.

## Deep conflict — one thread (T2 compression: pick one, do not attempt three)

**A saving that is certain per can versus a bill that is certain in dollars.** The Slim Retool's
material saving is real and permanent, but small per can; the retooling bill is a real, one-time
cost. Is a two-cent-per-can saving worth a five- or six-figure bet on how long the plant keeps
running this exact line at this exact volume? Push: *"What has to be true about Ridgeline's future
for the retooling to have been the right call in hindsight, even if it misses the payback ceiling
this year?"*

## The trap

A Hero who computes only the surface-area reduction (2.09%, D1–D2) and treats "a smaller shape
uses less material, therefore retool" as self-evident has skipped D3's dollar conversion and D4's
payback calculation entirely — where the actual decision lives. The trap runs the other way too: a
Hero who sees "25.6 months against a 24-month ceiling" and calls it a clean, decisive "no" has
missed how thin that 6.24% margin is against assumptions Appendix D states plainly are not sourced.
Watch for either shortcut and send the Hero back to the number they skipped.

## Socratic questions

1. Your D2 work proves r* is a minimum and not a maximum — what would the sign pattern of dS/dr have looked like on either side of r* if it had been a maximum instead, and how would you have caught that mistake?
2. The optimal shape uses less aluminum on every single can. Why doesn't that automatically make it the right call?
3. Which of your four stated assumptions, if it moved by 20%, would flip your recommendation — and which one could move by 50% and still not flip it?
4. If Ridgeline signed a new contract tomorrow that doubled this line's annual volume, would you change your Thursday pitch? By how much would the payback period move?
5. Priya's name is on this recommendation, not just the math. If the payback period comes out at 25.6 months against a 24-month ceiling, is that a "no," or is that a "close enough to fight for" — and what would you need to know to tell the difference?

## 45-minute Socratic plan

| Time | Beat |
|---|---|
| 0:00–3:00 | Intro + Launch — frame the capital-review stakes, show the can-line footage, take the gut-read question without correcting anyone |
| 3:00–8:00 | Anchor 1 — take a stand and vote, no reasoning yet |
| 8:00–15:00 | Anchor 2 — "what is the problem we're solving?" Let the room sit in the ambiguity of "less metal costs less than *what*" |
| 15:00–20:00 | Anchor 3 — name the five-step process before opening any appendix |
| 20:00–25:00 | Anchor 4 — surface the four assumptions (MA1–MA4); ask which are load-bearing |
| 25:00–35:00 | Data Deep Dive — work D1→D4 as a room, cold-call on D2's classification step |
| 35:00–40:00 | Deep conflict — the certain-per-can saving vs. the certain-dollar bill. No twist to drop in this case (see Twist: N/A above); this slot carries the "what if the numbers move" pressure instead |
| 40:00–45:00 | Close — re-vote, "did we ask the right question?", lessons learned |

## Close

**VOTE AGAIN.** Then: *"Did we ask the right question at the start?"* and *"What math was new to
you tonight, and how did you actually attack it?"*

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Critical Point · Local Maximum · Local Minimum · Concavity · Derivative · Instantaneous Rate Of
Change · How to find critical points of a function · How to use the first derivative test to
classify a critical point · How to solve an optimization problem using derivatives · How to find a
derivative using the power rule · How to convert an amount with compound units · How to find the
percent of a number

## Facilitator note — sensitivity

None required (SPEC §6). The stakes are commercial and professional — a capital budget line and a
process engineer's credibility in a review meeting. No personal loss, no family hardship, no safety
trade-off; both can shapes are legal and safe to fill and ship.

## Facilitator-only numbers

Every figure below resolves in `case.json.derived`.

| | Hold The Line | The Slim Retool |
|---|---|---|
| Radius | 1.301 in | 1.5105 in |
| Height | 4.0727 in | 3.0211 in (h/r = 2.0 exactly) |
| Surface area | 43.9266 in² | 43.0101 in² |
| Weight/can | 0.018567 lb | 0.018180 lb |
| Cost/can | $0.044933 | $0.043995 |

Savings: **$0.000938/can (2.0866%)**. At 300,000,000 cans/yr [MA3]: **$281,268.82/yr**. Against a
$600,000 retool [MA2]: **payback 25.60 months**. Against the 24-month ceiling [MA4]: **misses by
6.24%**. Break-even annual volume for a 24-month payback: **319,978,587 cans/yr** — only 6.7% above
the stated assumption.

**Sensitivity, one dial at a time (±50%):** sheet thickness [MA1] 0.00215–0.00645 in → payback
51.2–17.1 months; retooling cost [MA2] $300,000–$900,000 → payback 12.8–38.4 months; annual volume
[MA3] 150M–450M cans/yr → payback 51.2–17.1 months. Any one of the three, alone, can flip the
verdict. The 24-month ceiling [MA4] is the threshold, not an input — moving it to 30 months flips
the base-case verdict to B.

**The verdict.** Hold The Line wins this run's stated numbers by a margin of **6.24%** on the
primary metric — narrow enough that a Hero should treat it as "no, but only just," not as a
lopsided case.
