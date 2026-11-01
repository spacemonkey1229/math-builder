# FACILITATOR.md — The Surge Trigger

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Surge Trigger · **Tier:** T4 (HS) · **Studio:** Launchpad
**Standards:** Calculus/Derivatives + Applications Of Derivatives — chain rule, product rule,
quotient rule, tangent line at a point, local maximum — see `case.json.standards[]` for exact ids.

**Status:** `case-research` complete (2026-09-18). All `{{NEEDS_SOURCE: ...}}` placeholders in
`case.md` are resolved — one real growth-rate figure [S1] and one real cost figure [S4] are sourced
and used directly, two supplemental real sources ([S2], [S3]) ground the framing and inform an
assumption's basis, and the outbreak's starting case count, growth-rate constant, capture-rate
model, trigger thresholds, and verification cost are disclosed Modeling Assumptions MA1–MA5,
because no publishable figure exists for any of them for this fictional county.
`case.json.balance.margin_pct` is a real, computed **10.12%**. Everything below is the case of
record, not a placeholder.

**Sensitivity note (SPEC §6):** ordinary public-health operational pressure — a county
epidemiologist making a same-day resource-redeployment call. No illness, death, or family hardship
depicted for a specific person. Framed as protection (getting the mobile unit to the neighborhood
that needs it), not destruction.

## Argument for A — The True-Curve Trigger

Option A fires at **t_A = 10.41 days**, the moment the modeled true-infection curve I(t)'s own
growth rate I'(t) crosses 1.00 new cases/day per day — found directly by the chain rule on
Appendix A's exponential model. Its cost is fixed and known in advance: the department's own
**$1,700.00** verification-protocol cost [MA5], charged flat because policy requires paying it
before acting on any unconfirmed model. A's real strength is certainty and speed: no matter how
the outbreak actually unfolds after t_A, A's total cost never changes, and it reacts earliest.

## Argument for B — The Reported-Curve Trigger

Option B waits for D(t) = I(t) × c(t) — the only curve the department can actually observe — to
cross its own 0.40 threshold, which happens at **t_B = 14.43 days**, found by the product rule.
**Under this case's own current numbers, B is the cheaper design overall**: the ~4.03-day lag
against A costs a real, computed **$1,527.92** in late-detection cost (the gap in that day's
new-case count, priced via [S4]'s real per-case figure), which is less than A's flat $1,700.00.
B's real case is that A's verification cost is certain and paid regardless of outcome, while B's
cost — though real — comes in lower under the case's disclosed assumptions.

## The margin — real numbers, and how fragile this case actually is

`case.json.balance.margin_pct` = **10.12%**, within the approved concept's 8–15% margin target.

- **Trigger days:** t_A = 10.406 days (chain rule on I'(t) = threshold_A). t_B = 14.434 days
  (product rule on D'(t) = threshold_B, on the rising branch before D(t)'s own local maximum).
- **Lag:** t_B − t_A ≈ 4.028 days. **Gap in that day's new-case count:** I(t_B) − I(t_A) ≈ 4.897.
- **Option A (The True-Curve Trigger):** $1,700.00 flat (MA5) (loser, higher cost).
- **Option B (The Reported-Curve Trigger):** 4.897 × $312.00 [S4] = **$1,527.92** (winner, lower
  cost).
- **Margin:** |$1,700.00 − $1,527.92| / $1,700.00 = **10.12%**.

**Why this matters for the facilitator, specifically:** `sensitivity_model.py`'s FLEX[] contains
exactly one genuine, safely-sweepable assumption — `verification_cost` (MA5). I0 (MA1) and the
capture-rate pair c0/m (MA3) were tested and found structurally unsafe to flex ±50% (they change
whether/when D'(t) crosses threshold_B at all, not just the answer's scale — a scenario redesign,
not a dial); k (MA2) and the two thresholds (MA4) are held fixed for the same reason cases like
`the-approval-gate` hold their own structural thresholds fixed. **MA5 is genuinely unstable**: a
−50% flex FLIPS the winner to A (44.4% margin, breaks the 20% cap) and a +50% flex also breaks the
cap in the other direction (40.1% margin, B still wins). Both are disclosed in
`case.json.sensitivity_disclosure[]` as Category X. **Do not treat a student who challenges the
$1,700.00 verification-cost figure as having missed the point — that is exactly the case's most
defensible line of attack, since no public source publishes this figure directly.**

## Five Socratic questions

1. Option A reacts about four days earlier than Option B — if earlier is safer, why might Option A still not be the cheaper design overall?
2. Appendix C's capture rate declines over time — using D2's product-rule result, is the reported-case curve's shape ever really "the true curve, just smaller and delayed," or does it genuinely diverge?
3. D3 found that D(t) has a local maximum around day 32.695, but I(t) never turns over in this window — if a health director sees reported cases start falling, what would you tell them before they conclude the outbreak is under control?
4. Appendix D's $1,700.00 verification cost is a disclosed estimate, not a sourced fact — if the real cost were meaningfully lower, does the recommendation flip to Option A?
5. Both trigger designs watch for the same kind of signal — a growth-rate threshold — and disagree only about which curve to trust. Why does that one choice of curve matter this much in dollar terms?

## The trap

**A learner who assumes the reported-case curve D(t) is simply "the true curve, delayed by a few
days" — a shifted copy, not a differently-shaped curve — has fallen into the case's central trap.**
D(t)'s own local maximum (Challenge 3, D3) is real and occurs because the capture rate keeps
declining, eventually dragging D(t) down even while the true, unmitigated curve I(t) keeps rising
in this window. A pitch that never produces D3's classification, or that treats the two curves as
simple time-shifts of each other, has not done the deliverable's real work even if it lands on a
confident recommendation.

**A second, related trap:** a student who correctly finds both trigger days can still recommend
the wrong design by comparing raw *speed* (Option A reacts first) without ever pricing out the
actual dollar cost of each option's own consequence — a flat, certain protocol cost for A versus a
lag-sized, disclosed-assumption-driven cost for B. Reacting earlier is not automatically cheaper.

## Twist

The structural twist lives in the fact that "the only curve we can see" and "the curve that tells
us the truth" are not the same curve, and the case is built so a room's early instinct — trust the
observable dashboard, since it's real data, not a model — is complicated by the fact that the
dashboard curve has its own, different mathematical shape, not just a lag. Facilitators can
manufacture the twist moment directly by asking Socratic Question 3 if no student raises D(t)'s
local maximum unprompted, then letting the room sit with the fact that a real reported-case
plateau or decline can happen for reasons that have nothing to do with the true outbreak slowing
down.

---

## Guide Notes — the anchor ladder (SPEC Section 7, anchor-ladder subsection)

### Intro

Frame the format: a county epidemiologist has to redeploy the department's one mobile
vaccination-and-testing unit today, and has two different signals telling her two different things
about when to move — the room's job is to work out which signal to trust and what that choice
actually costs.

### Launch

Read the Overview aloud. Stop at "she just has to find it — and defend which curve she trusted."
Ask the room: "Before you've differentiated anything, which curve would you trust more: the one
you built yourself, or the one everyone else can already see? Why?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "The True-Curve Trigger or the Reported-Curve Trigger — show of hands." Record
the split.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which curve is more trustworthy" toward "what does each curve's derivative
actually tell us, and on what day does each one cross the line." Let the room sit with the fact
that neither trigger is free — every choice here has a real, disclosed cost attached.

### Anchor 3 — WHAT IS THE PROCESS?

Before touching Appendix D's cost numbers, get the room to state the actual comparison method out
loud: differentiate I(t) via the chain rule and solve for t_A (D1), build and differentiate D(t)
via the product rule and solve for t_B (D2), classify D(t)'s critical point (D3), verify the
capture-rate relationship via the quotient rule and compute the cost comparison (D4). Re-ask: "Is
'which curve is more trustworthy' still the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknowns explicitly: Two Rivers County's own case counts, capture-rate
curve, and internal trigger-threshold policy are not public data anywhere — every one is either a
disclosed Modeling Assumption or informed by real, cited research. "Which of these figures would
you most want to challenge, and why?"

### Data Deep Dive

Now open Appendices A–E. Run D1–D5 as a room, or have groups report out.

### Twist

Once D3's local-maximum finding is on the table, run Socratic Question 3 directly if it hasn't
come up yet: "If reported cases started falling around day 32.695, would you believe the outbreak is
under control?" Let the room discover that D(t)'s peak is a testing-capacity artifact, not
necessarily a real slowdown.

### Close

VOTE AGAIN. "Did the vote move? For the people who didn't move, what would it take to change your
mind?"

### Lessons Learned

The core transferable idea: the only data you can observe in real time is not automatically the
same shape as the truth it's supposed to represent — checking that with calculus (not assuming it)
is the actual skill. A second, equally real lesson: reacting earlier is not automatically cheaper
once each option's own real cost is priced out.

### Standards Touched On

Chain rule, product rule, quotient rule, tangent line at a point, local maximum.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no derivatives shown yet |
| 3:00–8:00 | Position defense: "Convince us your trigger is the right call, not just that it reacts sooner or uses real data" |
| 8:00–20:00 | Data Deep Dive — differentiate I(t) via the chain rule (D1) and D(t) via the product rule (D2) as a room, solving for t_A and t_B |
| 20:00–30:00 | Classify D(t)'s critical point (D3), verify the quotient-rule relationship and build D4's cost comparison; confirm the margin and where it comes from |
| **30:00** | **DROP THE TWIST** — Socratic Question 3: does a reported-case plateau mean the outbreak is actually slowing? |
| 30:00–38:00 | Pressure-test the case's assumptions directly: how close is the margin to flipping, and what would a defensible challenge to the verification-cost figure actually change? |
| 38:00–45:00 | Close, re-vote, lessons learned |

## Cohort bands (SPEC Section 7, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12–20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6–11)** | smaller room | Anchors 2–3 combine into one pass; the 20:00–30:00 quotient-rule/cost build-out runs as a single worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1–2)** | tutoring context | No vote at Anchor 1 — a stated initial position instead; facilitator plays devil's advocate directly; the 30:00–38:00 sensitivity pressure-test still runs in full |
