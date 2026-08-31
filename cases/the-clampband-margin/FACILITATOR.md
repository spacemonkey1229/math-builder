# FACILITATOR.md — The Clampband Margin

**Status:** retuned (case-research + retune pass, 2026-08-30; anchor-ladder rewrite, 2026-08-31).
Appendix B and Appendix C are sourced — see "The margin" section below for the real numbers, a
correction to which document the numeric margins actually come from, and a second correction (the
retune pass) to what "the RSS Stack" actually models. This document, plus `case.json`'s `balance`
object, is the only place the balance argument and the margin may live — none of this
appears in `case.md`.

**Retune note (2026-08-30):** this case originally failed SPEC.md §2's balance test — the
Worst-Case Stack and (naive) RSS Stack differed by 39.9% at this build's real n=3, well over the
~20% ceiling. Rather than force a fake-close number, further research found that real
tolerance-stacking practice does not actually use naive, textbook RSS the way the case originally
modeled it — see "The margin" section below for the full correction. See RESEARCH_LOG.md for the
complete retune research trail.

---

## Argument for A — the Worst-Case Stack

The Worst-Case Stack is the position a flight-safety reviewer will find hardest to argue with:
it guarantees that *any* combination of individually in-spec parts from the three suppliers still
releases correctly, because it assumes the worst combination could actually occur. It requires no
statistical-independence assumption about the three suppliers' manufacturing variation — an
assumption that is genuinely easy to defend across a large production run, and genuinely harder to
defend for one specific flight joint built from one specific set of three parts that already
exist. If NASA-adjacent industry's own release-element margin threshold (Appendix B) is checked
against the Worst-Case number, Option A clears it with room that does not depend on an assumption
holding.

## Argument for B — the Modified RSS Stack

The Modified RSS Stack is standard, industry-accepted practice precisely because both the
Worst-Case Stack AND naive RSS have known weaknesses: Worst-Case is overly conservative for a
statistically well-behaved supply chain, while naive RSS is known to be overly optimistic, because
it assumes every supplier's printed ± tolerance is a genuine 3-sigma bound on a centered, normal,
independent process — an assumption real practitioners have found routinely fails (Appendix F,
S6). The Modified RSS Stack corrects for this with a real, well-documented ×1.5 factor, and still
predicts a materially tighter total tolerance than Worst-Case, which means fewer of the three
suppliers' already-inspected, already-in-spec parts get rejected or sent back for rework — a real
cost and schedule cost that Option A imposes without a corresponding gain in the typical case.
Modified RSS still needs to clear NASA-adjacent industry's margin thresholds, and industry
practice treats that as sufficient sign-off.

## The margin — SOURCED (case-research, 2026-08-30)

**Correction first:** the design-margin thresholds are real and cited, but not both from the
document originally assumed. NASA GD-ED-2214 (read in full) states only a *qualitative* preload
criterion — "no gapping occurs when the maximum expected load is applied" — and contains no
numeric margin factor. The numeric values **1.25** (gapping margin) and **>2.00** (release-element
margin) are real and industry-cited, but their actual source is a separate 2012 Sierra Nevada
Corporation engineering paper (Lazansky, ESMATS/Aerospace Mechanisms Symposium — Appendix F, S2),
not GD-ED-2214. S2 is graded MEDIUM confidence (re-checked 2026-08-31): ESMATS/AMS is a real,
committee-reviewed proceedings series and Lazansky is a named engineer at a real aerospace prime,
which supports real credibility — but the release-element figure (>2.00) is itself only
second-hand within S2 (attributed further to a 1995 Purdy & Hurley Clementine paper) and was not
independently re-verified, which is why this is MEDIUM and not HIGH. See RESEARCH_LOG.md for the
full trail. Appendix B and Appendix F in case.md now cite each document correctly for what it
actually contains.

**Per-interface real tolerances (Appendix C):** Supplier B's flange OD and Supplier C's bolt+shim
stack height are governed by ISO 2768-1 tolerance class f (fine) — ±0.0079 in and ±0.0039 in
respectively, at the case's assumed (MA3) nominal sizes of 15.000 in and 0.500 in. Supplier A's
ring ID uses Protolabs' published standard CNC machining tolerance, ±0.0050 in.

**The bridge (MA4 — the most load-bearing assumption in the case):** neither real source connects
a dimensional tolerance-stack value (inches) to the dimensionless 1.25/2.00 load-safety factors.
No public formula exists to cite here, so the case states its own transparent rule: margin =
0.070 in (a stated nominal per-joint gapping allowance) ÷ predicted total tolerance. A result
≥ 1.25 clears the gapping threshold; ≥ 2.00 clears the release-element threshold.

**RETUNE CORRECTION (2026-08-30) — what "the RSS Stack" actually models:** the original run modeled
Option B as naive, textbook RSS — $T_{RSS}(n) = \sqrt{\sum t_i^2}$ with no correction. That put
Worst-Case and RSS 39.9% apart at n=3, failing SPEC.md §2's ~20% balance ceiling. Further research
(RESEARCH_LOG.md) found this doesn't actually match real tolerance-stacking practice: naive RSS
assumes every supplier's printed ± tolerance is a genuine 3-sigma bound on a centered, normal,
independent process, and real practitioners have found this routinely fails — tolerances printed
from limited shop-floor experience often really describe something closer to a 2-sigma range. A.
Bender's 1962 tolerance-stacking study ("Benderizing") corrected for this with a flat ×1.5
multiplier on the RSS result; Motorola's Six Sigma mechanical-design tolerancing practice later
adopted the same correction (the "Motorola formula"). Both are documented directly, with the
original equation reproduced, in a Boeing Research & Technology report (F. Scholz, "Tolerance
Stack Analysis Methods," 1995 — Appendix F, S6). **Modeling Option B as this real, corrected
version of RSS — not naive RSS — is the fix**: it isn't a different supplier count, a new
allowance, or an invented number; it's simply modeling the RSS method the way real tolerance
engineers actually apply it. Scholz's paper is itself worth noting for a striking fact that shows
this correction is a genuine, non-trivial engineering result and not a number chosen to make this
case's math work: for n=2 contributing tolerances, 1.5×RSS is proven to be *more* conservative
than plain worst-case addition. It only becomes less conservative than Worst-Case once n grows
past roughly 2–3 real interfaces of comparable magnitude — which is exactly this build's n=3.

**Computed results (Modified RSS Stack = 1.5 × RSS):**

| n | $T_{WC}(n)$ | WC margin | Passes 1.25 / 2.00? | $T_{MRSS}(n)$ | MRSS margin | Passes 1.25 / 2.00? |
|---|---|---|---|---|---|---|
| 3 (real) | 0.0168 in | 4.17 | Yes / Yes | 0.0152 in | 4.61 | Yes / Yes |
| 6 | 0.0336 in | 2.08 | Yes / Yes (barely) | 0.0206 in | 3.40 | Yes / Yes |
| 7 | 0.0392 in | 1.79 | Yes / **NO** | 0.0222 in | 3.15 | Yes / Yes |
| 10 | 0.0560 in | 1.25 | Yes (exactly at floor) / **NO** | 0.0266 in | 2.64 | Yes / Yes |

**`margin_pct` = 9.6** — the percent difference between the two methods' predicted total
tolerance at n=3 today: (0.0168 − 0.0152) / 0.0168 = 9.55% ≈ 9.6%. Comfortably under the ~20%
ceiling, and it's a genuine, close dilemma: at n=3 **both options clear both thresholds**, and now
their raw numbers are close too — neither is disqualified by the numbers alone at the current
build, and a Hero has to actually engage the argument, not just eyeball which number is bigger.
**Winning option: B (the Modified RSS Stack)** — but only once the scaling frame (D1–D3) is
engaged. Worst-Case fails the release-element margin starting at n=7 and sits exactly at the
gapping-margin floor by n=10; Modified RSS clears both thresholds at every modeled n. This is a
genuine consequence of Worst-Case growing linearly in n while Modified RSS grows like 1.5√n
(Appendix D) — a constant multiplier does not change which growth rate wins. Changing MA4's
0.070 in allowance moves *where* the crossover lands, not *whether* Worst-Case eventually falls
behind Modified RSS. The asymptotic fact holds under the actual sourced tolerance values: the
ratio $T_{MRSS}(n)/T_{WC}(n) \to 0$ as $n \to \infty$ (the constant 1.5 factor does not change a
horizontal asymptote of 0).

**Mechanically verified (2026-08-31, `sensitivity_model.py`, Tier 2 Probe 5):** the 9.6% n=3
margin figure is a raw-tolerance ratio, not the quantity that actually decides the case — see
"Probe 5 finding" below for what a large symmetric flex on the ×1.5 correction factor and on the underlying
ISO 2768/Protolabs tolerance values does to the real winning logic (does each option clear both
NASA-adjacent thresholds at every modeled n).

## Five Socratic questions

1. Both stack-up methods clear NASA-adjacent industry's thresholds for this build's actual three suppliers, and their predicted numbers are now genuinely close — if neither method is currently failing, and they're not far apart either, what is Wes actually deciding between?
2. Your D2 answer says the ratio of the Modified RSS Stack to the Worst-Case Stack has a horizontal asymptote as the supplier count grows — what does that asymptote actually mean for a future joint with many more contributing interfaces than this one has?
3. If your D3 table shows one method's pass/fail outcome against the threshold jumping at a specific supplier count, what real design decision would the company have to make differently once it crosses that count?
4. Worst-Case guarantees release for every combination of in-spec parts, while Modified RSS assumes the three suppliers' variation is independent and random even after its own ×1.5 correction — whose assumption is riskier to bet a single flight joint on, and does the number of suppliers change your answer?
5. Suppose the company's next satellite line uses five contributing supplier interfaces instead of three — does Wes's sign-off today commit the company to a policy for that future joint, or only to this one, and what would have to be true for today's choice to still be the right one then?

## The trap

The plausible reasoning that produces a confident wrong answer: Heroes will compute the n=3 case
(D4), see that both methods clear the thresholds by comparable amounts, and conclude the dilemma
is trivial or already resolved — "just pick whichever number is bigger/safer, it barely matters,
they both pass and they're close." That misses the entire reason the case exists: Wes isn't only
signing off on *this* joint, he is implicitly setting a policy for how the company evaluates
*every future* joint of this kind, and the two methods diverge sharply as the number of
contributing supplier interfaces grows (D1–D3). A Hero who never builds the table past n=3 never
sees that divergence, and will defend whichever option "looks safer" at a glance without engaging
the actual limiting-behavior math the case is built to force.

## Sensitivity note

None required beyond the standard SPEC §6 check. This is a mechanical-engineering tolerancing and
quality trade-off — no protected-subject flag applies. Facilitators should still keep classroom
framing on the engineering trade-off (safety margin vs. rework cost/schedule) rather than treating
mission failure as background color; NASA's real, cited margin thresholds are what make the case
concrete, not any dramatized failure scenario.

---

## Intro

Frame the format: this is a real aerospace engineering sign-off, not a hypothetical. Open with:
"You have to sign a drawing today that can never be revisited once the satellite ships. What do
you check before you sign?" Let that land before moving to the Launch.

## Launch

Show or describe the Appendix C schematic (three toleranced interfaces meeting at one joint) and
read the Overview aloud. Do not confirm or correct any gut reactions here.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet.** "Is anyone courageous enough to stand with the
Worst-Case Stack? With the Modified RSS Stack?" Show of hands, both options, no discussion. Record
the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this about whether the joint releases *this time*, or about something else?"** Let confusion
grow — most Heroes will initially frame this as a single pass/fail check on today's three parts
and miss the scaling angle entirely. If the room lands on "Wes is setting a policy for every
future joint, not just certifying this one" on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we build the stack-up table across a growing supplier count, how will that change how we
decide?"** Once the room separates "does today's joint pass" from "does the policy hold as the
company scales," ask them to name the actual steps before touching the appendices: pull each
supplier's real tolerance (D1, Appendix C), stack them both ways across a growing n (D1, Appendix
D), find the ratio's horizontal asymptote algebraically (D2), check both methods' pass/fail
outcome against Appendix B's thresholds at every n (D3), and pin down today's real n=3 numbers
(D4) before graphing it all (D5). Re-ask: "Is our question still the right question?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions about future joint designs to answer this? Which ones are
load-bearing?"** Point toward Appendix E's MA1/MA2/MA4 once Heroes reach for them. The honest
answer is that MA4 (the 0.070 in gapping allowance that bridges NASA-adjacent industry's
dimensionless margin factors to Appendix C/D's dimensional tolerance stack) is the single most
load-bearing figure in the case — it moves *where* the crossover in D3 lands, though not *whether*
Worst-Case eventually falls behind Modified RSS. Let a sharp Hero find this themselves before
confirming it.

## Data Deep Dive

Now the numbers: Appendix B's NASA thresholds, Appendix C's real per-supplier tolerances, Appendix
D's stack-up table. Walk D1's growing table and D4's n=3 numbers together as a room, cold-calling
for D4 specifically — this is where a Hero who never built the table past n=3 will visibly
struggle to explain why the dilemma is more than "pick the safer-looking number." That struggle is
useful information for the facilitator, not a moment to rescue.

## Twist

**Beat 1 — the scaling reveal (~15-minute mark):** reveal that the company's next satellite
program is already contracted to use a clampband joint with substantially more contributing
supplier interfaces than this one (the exact count is in Appendix D, MA1) — and that Wes's
sign-off memo is being adopted as the *default policy* for that program too, not re-derived from
scratch. This invalidates any position that was reasoned only from the n=3 case ("both methods
pass, so it doesn't matter"), without making either method obviously correct at the larger count —
that still depends on where each method's predicted tolerance actually sits relative to NASA's
thresholds as $n$ grows, which is exactly what D1–D3 were built to establish.

Follow-up: "What just broke in your original model? Were you wrong about the math — or just
missing information about how far this decision actually reaches?"

**Beat 2 — press the confident B-defender on the correction factor itself (immediately after Beat
1 lands, once the room has recommitted to B as the durable choice):** by this point a room that
has engaged D1–D3 will have converged on B as the safe, durable pick — clears both thresholds at
every modeled $n$, "safety margin built in twice over" (once from the ×1.5 correction, once from
$\sqrt{n}$ growth). This is exactly the moment to push harder, not to confirm and move on. Ask the
room's most confident B-defender directly: **"You're trusting a ×1.5 correction factor from a 1962
study, carried into practice by a 1988 Motorola guide. What if it's not exactly 1.5 — what if the
real correction for *this* build's suppliers should be larger, say 2.25? Does B still win?"**

Do not answer it for them. Let the room work it by hand or by gut before confirming: **at n=10 —
the largest modeled count, the one B's whole "durable" case rests on — a ×2.25 correction factor
pushes Modified RSS's own predicted tolerance past NASA-adjacent industry's release-element
threshold too, and B is disqualified right alongside A.** The case's clean "B wins durably"
verdict does **not** survive this pressure symmetrically: a correction factor that's too *small*
(down to ×0.75) only makes B's case stronger; a correction factor that's too *large* (up to ×2.25)
breaks it at exactly the largest supplier count the case was built to worry about. (Mechanically
verified, `sensitivity_model.py` Probe 5 — see `case.json.sensitivity_disclosure[]` and
QA_REPORT.md for the exact numbers; do not read the numeric result off this page or off `case.md`,
per the standing no-leak rule.)

Follow-up: "So which is it — is B actually the safer bet, or did we just trade one unstated
assumption (a small $n$) for another (the correction factor is exactly 1.5)? What would you need
to see to trust that number the way you trusted the n=3 arithmetic a few minutes ago?" This is the
question that should make a room that felt *done* after Beat 1 genuinely wobble again — the case
has no equally solid replacement for ×1.5 to offer, and that is the point: Wes's real sign-off
rests on a real, well-sourced, but not infinitely precise number, same as most real engineering
judgment calls do.

## Close

**VOTE AGAIN.** "Did we ask the right question? What math was new to you, and how did you attack
it?" Compare the closing vote to Anchor 1's — a room that voted for the Modified RSS Stack at
Anchor 1 purely on "it lets more parts through" and stays there after the twist for a
*different, growing-n/asymptote-based* reason has genuinely moved, even if the vote count looks
unchanged.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "MA4 is the load-bearing figure, not MA1/MA2" finding landed as a discovery
  or had to be told outright.
- Whether the "both methods pass at n=3, so it's trivial" trap was the actual sticking point, or
  whether D2's algebraic horizontal-asymptote derivation was the harder gate for most Heroes.
- Whether the twist (the next program's larger, already-contracted supplier count) felt like a
  genuine new constraint or felt like the case dodging a clean numeric answer at n=3.
- Whether Twist Beat 2 (pressing the confident B-defender on the ×1.5 correction factor itself)
  actually made the room wobble, or whether by that point the room had over-anchored on B and
  waved the question off without engaging it.

## Standards Touched On

Limit · Asymptote · Continuity (Informal) · How to estimate a limit from a table or graph · How to
identify a vertical or horizontal asymptote from a function's equation

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just safer" |
| 10:00–15:00 | Pressure-test the models: "Whose plan is most fragile as more suppliers get added?" |
| **15:00** | **TWIST BEAT 1** — the next program's supplier count, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict: (1) safety-conservatism vs. cost/rework-efficiency; (2) single-build adequacy vs. long-run scalability of the sign-off policy; **TWIST BEAT 2** once the room has resettled on B — press the confident B-defender on the ×1.5 correction factor itself ("what if it's really 2.25?") and let the room see B wobble too |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands

See `case.json`'s `cohort_bands[]` — reproduced here for the facilitator's convenience:

- **Full (12-16):** both deep-conflict threads run as written above.
- **Compressed (6-8):** Anchors 2-3 combine; only the safety-conservatism vs. cost/rework thread
  runs live; the scalability thread folds into the close-out.
- **1:1 / pair (1-2):** no vote — Anchor 1 becomes a stated initial position; the guide argues the
  other method's case directly; "who reverses" becomes "would you reverse, and why."

## Probe 5 finding — does the ×1.5 correction factor / tolerance base survive a large flex?

See `sensitivity_model.py` and the QA_REPORT.md for the full, mechanically-verified answer. Do not
restate the numeric result of that probe in `case.md` — it stays here and in QA_REPORT.md/
RESEARCH_LOG.md, same leak rule as the rest of this file.
