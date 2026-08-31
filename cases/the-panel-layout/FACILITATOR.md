# FACILITATOR.md — Panel Layout

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — case.md
carries no marker comment for this by design (see the "Balance argument" guidance in `case-write`
SKILL.md); the balance argument, margin, and sensitivity notes live only here and in `case.json`'s
`balance` object.*

**Case:** Panel Layout · **Tier:** T2 · **Band:** MS-core · **Studio:** MS Adventure
**Standards:** Calculus / Applications Of Derivatives — `calculus-critical-point`,
`calculus-how-to-find-critical-points-of-a-function`,
`calculus-how-to-use-the-first-derivative-test-to-classify-a-critical-point`,
`calculus-how-to-solve-an-optimization-problem-using-derivatives`. All four already at `n=2`
before this case (covered by The Curve's Turn and The Optimal Can) — a second-pass/redundancy
case; `new_coverage[]` is correctly empty and `case.json.reinforcement_note` records what was
checked. Exact ids in `case.json.standards[]`.

**Status:** drafted at `case-write` 2026-08-30, researched at `case-research` 2026-08-31, gated at
`case-readiness` 2026-08-31. Appendix A's endpoint specs and Appendix C's tested miss rates are
stated Modeling Assumptions (MA1–MA13; Meridian Medical is an invented device — SEE Appendix D of
`case.md` and `RESEARCH_LOG.md`); Appendix B's Fitts's Law coefficients (a=0.6992 s, b=0.1714 s/bit)
are a real, cited source (S1: Hassan, Magee & MacKenzie, HCII 2019 — MEDIUM confidence, a
touchpad-tap proxy for the panel's hand-reach task).

**Computed result (facilitator-only — never state this exact figure in `case.md`).** All figures
below are reproduced mechanically in `cases/the-panel-layout/sensitivity_model.py` and recorded in
`case.json.derived`.
- The whole-panel raw-time model T(x) has exactly one critical point in [0,1] — the root of
  24x² − 36x + 11 = 0 in the feasible domain — at x* = 3/4 − √15/12 ≈ 0.4273, and it is a genuine
  local (and, checked against both endpoints in D3, global) **minimum** of raw movement time:
  T(0) ≈ 4.625 s, T(1) ≈ 4.611 s, T(x*) ≈ 4.607 s.
- Once Appendix C's tested miss rates are folded in (D4), the ranking on the actual primary
  metric — expected seconds per successful actuation — is **Option B, Long Reach, wins**:
  E(Long Reach) ≈ 4.777 s vs. E(Close Reach) ≈ 4.894 s. **margin_pct = 2.46%** (well under the
  ~20% retune threshold — not flagged).
- This is a genuinely close, non-forced result. Three Modeling Assumptions are the real levers,
  not the sourced Fitts's-law coefficients, and all three flip thresholds below are mechanically
  verified against `sensitivity_model.py`, not just asserted in prose: MA8 (count of other
  required controls — verified flip threshold n* ≈ 2.365, i.e. flips between the integers n=2 and
  n=3; the case uses n=3), MA6 (Close Reach's other-controls distance — verified flip threshold
  ≈118.07 mm; the case uses 140 mm), and MA13 (Close Reach's other-controls miss rate — verified
  flip threshold ≈4.12%; the case uses 7%). A Hero who challenges one of those three in discussion
  is doing the case's intended sensitivity-analysis move, not nitpicking.

## Sensitivity note

Medical-device framing (SPEC §6). This case must stay strictly about the layout-optimization
engineering decision — panel space, predicted movement time, tested miss rate — and never drift
into depicting an actual patient-harm incident. `case.md`'s Overview and Background were written
in a routine engineering register on purpose: the stakes are a tooling sign-off and a
design-history-file finding, never a described clinical event. Facilitators should keep the
discussion in that same register — the wrong-path warning, the twist, and the Socratic questions
below are all framed as an engineering optimization problem, not a life-or-death one. If a discussion drifts
toward "what if a patient is hurt," redirect to the actual math question: which layout minimizes
predicted time and rework across the whole control sequence.

## Balance argument

**Argument for A (Close Reach).** The Confirm control is the single most-used control in the
sequence — it is reached every pass, unlike the other required controls, which the Confirm
control's near-zone allocation trades against collectively. Close Reach minimizes the Confirm
control's own predicted movement time and tested miss rate. If the other required controls'
movement time is not very sensitive to losing a little near-zone space, Close Reach's advantage on
the panel's single most-used control can dominate the whole-sequence total even after the
first-derivative-test/optimization work is done.

**Argument for B (Long Reach).** There are more "other required controls" than there are Confirm
controls, and Long Reach keeps every one of them close and easy. A small movement-time or
miss-rate cost on the Confirm control, paid once per pass, can be outweighed by a smaller-looking
benefit that is paid once per other control and summed across all of them. Long Reach may also sit
closer to the domain's true interior time-minimizing allocation than either engineer's
single-control intuition would predict — that is exactly what D1–D3's critical-point work is
built to reveal.

**The margin.** Computed at `case-research` and re-verified mechanically at `case-readiness` (see
the boxed result above): margin_pct = 2.46%, Option B (Long Reach) wins on the miss-rate-weighted
primary metric. Method: build T(x), differentiate it, classify its critical point(s), compare
T(x) at x=0, x=1, and every interior critical point (D3), then fold in the tested miss-rate data
to compute the expected seconds per successful actuation at all three x-values (D4) and compare.
`case.json` records the method as `balance.margin_basis` and the number as `balance.margin_pct`.

## Intro

Frame the format before anything else: this is a real hardware sign-off with a hard deadline, not
a worksheet. Name the opener — "You're Marcus Feld, Human Factors Engineer at Meridian Medical.
Both prototype panels are on your bench. Once you submit this sign-off, the injection-mold cavity
gets cut and the layout is locked for the life of this hardware revision — and if a miss-rate
problem ever turns up in the field, it's your name on the sign-off line." Let the stakes land
before moving to the Launch.

## Launch

Hand out (or project) the two named prototype descriptions — Close Reach and Long Reach — with no
numbers yet, just the trade-off in plain language: a bigger Confirm control close to the hand vs.
smaller and farther, with the other required controls trading the opposite way. Ask: "If you had
to guess right now, with nothing but the description, which one finishes the whole sequence
faster?" Take the answers without correcting anyone. Most rooms will jump to "Close Reach, because
the Confirm control is the one you use every time" — that instinct is worth recording out loud
before anyone opens Appendix A's numbers, because it is exactly the wrong path named in the
Facilitator-only section near the end of this guide.

## Anchor 1

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Long Reach — the option with the *smaller* Confirm
control?" Show of hands, both options, no discussion. Record the count — Close will ask them to
vote again.

## Anchor 2

**"Is 'which control is faster' the right question, or is it 'which whole sequence is faster'?"**

Push on what Marcus's recommendation actually has to be judged on: "The Background says outright
that the answer isn't the Confirm control's own time in isolation — so what *is* the whole panel
actually being judged on, and why does that make this harder than just picking the option with the
bigger Confirm control?" If the room lands on "we need the whole-sequence predicted time per
successful actuation, not the Confirm control alone" on its own, the case is working as designed.
Also push: "Could the actual fastest layout be a design nobody has built yet?" — let the room sit
with that discomfort before Anchor 3 resolves it.

## Anchor 3

**"If we go through this process and find the data, how will we decide?"**

Make the room name the steps before opening an appendix: (1) express every control's width and
distance as a function of one allocation variable x (Appendix A), (2) build the whole-sequence
predicted time T(x) from Fitts's Law (Appendix B), (3) differentiate T(x) and solve T'(x)=0 for
every critical point (D1), (4) classify each critical point with the first-derivative test (D2),
(5) compare T(x) at both domain endpoints and every interior critical point (D3), (6) fold in
Appendix C's tested miss-rate data for the final recommendation (D4). Re-ask: "Now that we can see
the steps, is our question still the right one?"

## Anchor 4

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gaps: Appendix A's endpoint dimensions and Appendix C's tested miss rates are
all stated Modeling Assumptions (MA1–MA13), not measurements of a real product — Meridian Medical
and this hardware revision are invented for this case. Ask which ones actually change the *graded*
D4 result if they move. The honest answer, which a sharp Hero should find before it's confirmed:
MA8 (how many other required controls there are), MA6 (how far Close Reach pushes those controls
out), and MA13 (how often those pushed-out controls get missed at Close Reach) are the three
load-bearing figures — each one alone can flip the recommendation; the sourced Fitts's-law
coefficients (Appendix B) cannot.

## Data Deep Dive

Now, and only now, open Appendices A–C and work D1–D4 together as a room, cold-calling for D4
specifically — this is where a Hero who correctly built T(x) and found x* ≈ 0.4273 but never
folded in Appendix C's miss rates will visibly struggle to explain why Long Reach, not the
time-minimizing x*, is the actual recommendation. That struggle is useful information for the
facilitator, not a moment to rescue.

**Facilitator-only arithmetic note.** T(x) = 4a + b·log2(D_c(x)/W_c(x)+1) + 3b·log2(D_o(x)/20+1)
where D_c(x)=120−60x, W_c(x)=10+20x, D_o(x)=80+60x (Appendix A's linear interpolation, MA9), and
a=0.6992, b=0.1714 (Appendix B, S1). T'(x)=0 reduces to 24x²−36x+11=0, giving the single feasible
root x*=3/4−√15/12≈0.4273 — a genuine local and global minimum of raw T(x): T(0)≈4.625 s,
T(1)≈4.611 s, T(x*)≈4.607 s (D1–D3). Folding in Appendix C's tested miss rates for D4 (expected
attempts = 1/(1−miss rate) per control): E(Long Reach) = MTc(0)/(1−0.06) + 3·MTo(0)/(1−0.02) ≈
4.777 s; E(Close Reach) = MTc(1)/(1−0.01) + 3·MTo(1)/(1−0.07) ≈ 4.894 s. Long Reach wins by
(4.894−4.777)/4.777 = **2.46%**. No tested miss rate exists for x*, so it cannot be scored in D4
at all (see the Twist). Full derivation and the mechanically-verified flip thresholds for MA6/MA8/
MA13 in `cases/the-panel-layout/sensitivity_model.py`.

## Twist

Deliver slowly, with pauses, at ~15 minutes into the discussion:

"Someone points out that your D1–D3 work already found something interesting: the layout that
actually minimizes raw movement time isn't either prototype on your bench. It's x* ≈ 0.43 — a
layout roughly 43% of the way from Long Reach toward Close Reach, faster than *both* named options
on raw time: T(x*) ≈ 4.607 s beats T(Long Reach) ≈ 4.625 s and T(Close Reach) ≈ 4.611 s. If you
had a third prototype milled at that exact allocation, would you recommend it instead of either of
the two panels actually on your bench?"

Let the room want to say yes. Then ask the follow-up: "Appendix C's usability lab has never tested
a layout at x* — it only tested the two named endpoints. What miss rate would that third panel
actually have in the field?"

**Facilitator-only: what this actually does, and does not, change.** x* ≈ 0.4273 and its raw time
T(x*) ≈ 4.607 s are not new numbers — they are already the direct output of D1–D3, which every
Hero has already computed by this point in the discussion; the twist is not a new sourced figure,
it is a consequence of the case's own math that most rooms will not have connected to the actual
recommendation on their own. Walk a Hero through the honest limitation Challenge D4 itself states
explicitly: no layout strictly between the two named prototypes has ever been physically built or
tested, so there is no tested miss-rate figure for x* — and Appendix D says outright that MA9's
linear interpolation of *width and distance* between the two endpoints is not license to assume
miss rate interpolates the same simple way. Recommending x* would mean recommending an unbuilt,
untested panel purely on a raw-time projection that ignores the very failure mode (misses and
retries) the whole case exists to weigh. **The twist reframes, it doesn't resolve:** "which x
minimizes raw movement time" is a different question from "which panel Marcus can actually
defend in a design-history file," and a Hero who only answers the first has picked the
mathematically prettier number over the one the sign-off form actually asks for. Do not hand the
room a specific answer for whether x* "would" have a good or bad miss rate if it were built — the
case has no sourced basis for that, and inventing one would be exactly the fabrication SPEC §5
forbids.

## Immediate recommit

Re-vote immediately. Ask by name: "Does knowing x* exists change your vote — or does it just tell
you that neither named prototype is the mathematically perfect layout, only the two that have
actually been tested?" That distinction is the transferable skill, not the vote itself.

## Deep conflict

Three threads, 20–30 minutes:

1. **A closed-domain critical point is a candidate, not a guarantee.** x* beats both named
   endpoints on raw time (D1–D3) — yet it loses the actual recommendation because D4's miss-rate
   data doesn't exist for it. What does that say about the difference between "the calculus says
   this point is optimal" and "this point is buildable, tested, and defensible today"?
2. **The Confirm control is used every pass; the other controls are used collectively more often.**
   How does that asymmetry show up in T(x)'s derivative, and why doesn't the Confirm control's own
   movement-time advantage at Close Reach automatically translate into a whole-panel advantage?
3. **Three assumptions, not the sourced Fitts's-law coefficients, drive the whole result.** MA6,
   MA8, and MA13 each independently flip the recommendation (verified in
   `sensitivity_model.py`); the real, cited human-factors data (Appendix B) never does. Is a
   2.46%-margin recommendation built on three contested assumptions one Marcus should state
   flatly, or one he should hedge in the sign-off form?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both prototypes side by side, cold-call for a gut read, no numbers yet |
| 3:00–10:00 | Position defense — *"Convince us your layout wins the whole sequence, not just the Confirm control"* |
| 10:00–15:00 | Pressure-test the models — *"Which of MA6, MA8, or MA13 would have to change, and by how much, for your answer to flip?"* |
| **15:00** | **DROP THE TWIST** — x* beats both named options on raw time, but has no tested miss-rate figure |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (critical point vs. buildable/tested layout; Confirm-control-only optimization vs. whole-sequence optimization; how much to trust a 2.46% margin built on three contested assumptions) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

The trap is comparing Close Reach and Long Reach only on the **Confirm control's own** predicted
movement time and miss rate — exactly the number Close Reach is built to win, since it is the only
option that improves the Confirm control in isolation. A Hero who stops there has quietly ignored
that the Confirm control is only one of several required controls in the same sequence, and that
the near-zone space Close Reach claims for itself has a real, non-decorative cost paid by every
other control, every single pass. The case's primary metric is explicitly the *whole-sequence*
predicted time per successful actuation, not the Confirm control's own time — a Hero who never
builds and optimizes T(x) across the full sequence (D1–D3) has answered a narrower, easier
question than the one Marcus actually has to sign off on, and may confidently recommend the wrong
layout as a result. A second, subtler version of the same trap, which the Twist is built to
surface: assuming the interior critical point x* must be the right recommendation just because it
beats both named options on raw time, without checking whether it can actually be scored on the
case's real primary metric at all — a critical point on a closed interval is a candidate for the
global minimum of *movement time*, not automatically a recommendable, tested, buildable panel.

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" Ask what math was new to each Hero,
and specifically whether checking the domain endpoints in D3 (rather than stopping at the interior
critical point), or discovering x* has no tested miss rate at all, changed anyone's answer.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "MA6/MA8/MA13 are the load-bearing figures, not the sourced Fitts's-law
  coefficients" finding landed as a discovery or had to be told outright.
- Whether the Twist's "the math-optimal layout has no tested data" moment felt like a genuine
  constraint or felt like the case dodging a clean numeric answer.
- Whether the "Confirm-control-only vs. whole-sequence" trap was the actual sticking point, or
  whether D4's miss-rate-weighting arithmetic itself was the harder gate for most Heroes.

## Standards Touched On

Critical Point; How to find critical points of a function; How to use the first derivative test
to classify a critical point; How to solve an optimization problem using derivatives.

## Cohort bands (cohort-size bands, minimum specification)

| Band | Typical size | What changes |
|---|---|---|
| **Full** | the size this T2 case is authored for (a full MS-core class section) | the Socratic plan below runs as written; both stand/sit votes are taken as a group |
| **Compressed** | roughly half | Anchors 2–3 combine into one pass; the deep-conflict thread runs as a single thread instead of three; total runtime shortens proportionally |
| **1:1 / pair** | 1–2 learners | no vote to take — Anchor 1 becomes a stated initial position instead of a stand/sit count; the guide plays devil's advocate directly rather than cold-calling; whether x* is actually recommendable still lands but is asked directly rather than opened to the room |

Recorded in `case.json.cohort_bands[]`.

## Socratic questions

1. Your D3 table found x* beats both named endpoints on raw time — so why doesn't Marcus recommend a third panel built at x*?
2. The Confirm control is reached once per pass and the other required controls are reached collectively more often — how does that asymmetry show up in T(x)'s derivative?
3. D3 asks you to check T(x) at both domain endpoints, not just at the interior critical point from D1–D2 — what would have to be true about T(x)'s shape for an endpoint to beat the interior point?
4. D4 asks you to state explicitly what is and is not known about miss rate at x* — what should Marcus do with a result that depends on an untested layout's assumed miss rate?
5. MA6, MA8, and MA13 each independently flip this case's recommendation on their own — what would you need to see in a real usability report before trusting any one of those three assumed figures?

## Facilitator note — sensitivity (SPEC §6)

Medical-device framing declared by the concept sheet (see `case.json.content_sensitivity` and the
Sensitivity note above) — kept strictly to the layout-optimization engineering decision, never to
a depicted patient-harm incident. Separately, per `case-write` SKILL.md §8, this note also records
the *direction* only (never the size) of the case's real modeling-assumption sensitivity, even
though the actual computed thresholds are recorded elsewhere in this file and in
`case.json.derived`/`sensitivity_model.py` for facilitator reference: MA6, MA8, and MA13 are the
figures most likely to flip the recommendation — if Close Reach's other-controls distance (MA6)
were shorter, if there were fewer other required controls (MA8), or if Close Reach's other-controls
miss rate (MA13) were lower, the Long Reach margin narrows and can flip to favor Close Reach.
