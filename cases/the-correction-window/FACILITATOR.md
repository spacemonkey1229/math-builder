# FACILITATOR.md — The Correction Window

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the end of case.md.*

**Case:** The Correction Window · **Tier:** T4 (HS) · **Studio:** Launchpad
**Standards:** Calculus's Taylor Series (term) and its "how to find the Taylor series of a
function at a point" (new coverage, both n=0 before this case); Sequence, Series, and "how to
determine whether a series converges or diverges" (reinforcement); Measurement's "how to convert
an amount with compound units" and Advanced Numbers' "how to find the percent of a number"
(reinforcement). See `case.json.standards[]` for exact ids.

**Status:** `case-research` complete (2026-09-05). All `{{NEEDS_SOURCE}}` placeholders are
resolved — three real, cited facts (Appendix G: S1 STM32F405 clock speed, S2 Arm's own single-cycle
arithmetic claim, S3 Betaflight's documented 8kHz loop-rate practice) and two disclosed Modeling
Assumptions (MA1 gust-tilt distribution, MA2 correction-error tolerance) plus two plain scenario
constraints (90-second transit, 15-foot offset). `case.json.balance.margin_pct` is a real, computed
**11.7%**. Everything below is the case of record, not a placeholder.

**Sensitivity note (SPEC §6):** this case touches a real but bounded stress scenario — a missing
hiker in dropping temperatures, a closing daylight/battery window. Framed around protection
(finding Dana, flying the drone safely) rather than harm, per SPEC §6's guidance. No illness,
death, or family hardship is depicted, but facilitators should still name the stakes plainly in
the Intro rather than letting the drone-engineering framing bury them.

## Argument for A — Build 3 (3rd-order Taylor polynomial)

Build 3 is cheap: 3 single-cycle floating-point operations per correction [S2] against Build 5's
5, at the STM32F405's 168 MHz clock [S1] — 12.857 ms of total flight-computer time spent on the
trig approximation across the whole 720,000-cycle, 90-second transit, against Build 5's 21.429 ms.
Build 3's raw accuracy is genuinely worse: it exceeds Appendix E's 0.0003 tolerance at the 30°, 40°
and 50° gust bands, which under MA1's weights account for 33% of all correction cycles over the
mission. **Argument A does not deny this** — its case is that the primary metric explicitly names
in Challenge 3 (D5) weighs accuracy against the compute budget it costs, and on that specific,
graded ratio, Build 3's much lower compute cost outweighs its worse error rate. This is the
correct, quantitatively defensible route to Build 3 — very different from a Hero who picks Build 3
by comparing operation counts alone and never checking Appendix E's tolerance at all.

## Argument for B — Build 5 (5th-order Taylor polynomial)

Build 5's real, quantitative case is that it clears Appendix E's tolerance at every tested gust
band — its worst-case error across the whole range is roughly 0.00008, more than 50 times smaller
than Build 3's worst-case error of about 0.0041 at the 50° band. Its argument is that a missed
correction this close to a rock wall (Appendix B's 15-foot offset) is a categorically worse kind of
failure than a few extra milliseconds spread across a 90-second flight — especially since both
builds' total compute cost is a small fraction of the correction loop's available budget at 8 kHz
[S3]. This is a legitimate, defensible position to argue in discussion, but it is arguing that raw
failure-avoidance should outweigh the case's own graded metric — it does not carry Challenge 3
(D5)'s primary-metric comparison under the case's current numbers.

## The margin — real numbers, and which way the fragility runs

`case.json.balance.margin_pct` = **11.7%**, inside the SPEC §2 target 8-12% band. The arithmetic,
in full:

- **Operations per correction** [S2]: Build 3 = 3 (θ², θ³ = θ²·θ, one fused multiply-add for
  θ − θ³/6). Build 5 = 5 (the same 3, plus θ⁵ = θ³·θ², plus a second fused multiply-add for
  + θ⁵/120).
- **Cycle time** [S1]: 1 ÷ 168,000,000 Hz = 5.952 ns.
- **Total correction cycles** [S3]: 90,000 ms ÷ 0.125 ms/cycle = 720,000 cycles.
- **Total compute budget:** A = 720,000 × 3 × 5.952 ns = **12.857 ms**. B = 720,000 × 5 × 5.952 ns
  = **21.429 ms**.
- **Error rate** (MA1 weights, MA2 tolerance = 0.0003): A fails the 30°/40°/50° bands
  (20% + 10% + 3% = **33%**). B fails none (**0%**).
- **Metric = (1 − error rate) ÷ total compute budget (ms):** A = 0.67 ÷ 12.857 = **0.052111/ms**.
  B = 1.00 ÷ 21.429 = **0.046667/ms**.
- **Margin** (project convention: winner-minus-loser over loser): (0.052111 − 0.046667) ÷ 0.046667 = **11.7%**. Build 3 (A) wins.

**Why this matters for the facilitator, specifically:** the case is built so that the *naive*
comparison (which polynomial is more accurate?) and the *graded* comparison (which polynomial wins
the named ratio metric?) point in **opposite directions**. A Hero who compares Build 3's 33% error
rate against Build 5's 0% and stops there will confidently recommend Build 5 — and will be wrong
about what the case's own primary metric says, every time, unless they also weigh the compute cost.
**Do not treat a student who picks Build 5 on raw accuracy alone as having engaged with the case's
actual math — the section below this one explains why that shortcut is not a legitimate alternate
reading.** A Hero who explicitly argues
that raw failure-avoidance should outweigh the metric (Argument for B, above) has engaged with the
case correctly and reached a defensible, arguable conclusion — that is different from never running
the ratio at all.

`sensitivity_model.py`'s Tier 2 P5 sweep found the case's own margin is genuinely fragile in one
specific place: raising MA1's 30° gust-tilt band weight from 20% to 30% (a +50% relative increase,
with the 20°/10°/3% bands unchanged) flips the recommendation to Build 5 — at that weighting,
Build 3's error rate rises to 43%, dropping its metric below Build 5's. Two other flexes do not
flip the winner but do push the margin outside the SPEC §2 20% band in the other direction —
lowering the 30° band weight by 50% widens the margin to 28.3%, and loosening MA2's tolerance by
50% widens it to 45.0% — both disclosed in `case.json.sensitivity_disclosure[]` rather than hidden.
No other flex, in either direction, moved the winner. The 30° band is the single most
leverage-sensitive number in Appendix E, because it sits exactly at Build 3's tolerance boundary
(its exact error there, 0.000326, is only barely above MA2's 0.0003 tolerance) — a small, entirely
defensible argument that gusts land in the 30° band more often than assumed can flip the case.

## Five Socratic questions

1. Build 5 is far more accurate than Build 3 at every gust angle in Appendix E — so why might a flight-software engineer choose the less accurate option anyway?
2. Appendix E's 30° gust band sits right at the edge of Build 3's tolerance — if that threshold, or the frequency of 30° gusts, were even a little different, would your D4/D5 answer change?
3. Both polynomials come from the exact same general Taylor series formula in Appendix D — why does keeping just one more term buy so much extra accuracy at the larger gust angles but comparatively little at the small ones?
4. In D2, you checked your computed error against the size of the next un-kept term of the series — does that check tell you the error would keep shrinking forever if the flight computer could afford infinitely more terms?
5. Appendix A shows both builds' total compute cost is a small fraction of the correction loop's full time budget at 8 kHz — if compute cost is that cheap in absolute terms, why does the case's own metric still favor the cheaper option?

## The trap

**A learner who compares Build 3's and Build 5's raw approximation error and stops there — never
computing D3's operation counts or D4's total compute-budget figures — will confidently recommend
Build 5 every single time, because Build 5 genuinely is far more accurate at every tested angle.**
This is exactly the trap named at concept approval: raw accuracy comparison, unweighted by compute
cost, always favors the higher-order polynomial. The case's actual graded metric in Challenge 3
(D5) is a *ratio* — (1 − error rate) ÷ compute cost — and only a pitch that genuinely builds D3's
operation-count derivation and D4's compute-budget totals can discover that Build 3 wins the named
metric despite being the less accurate build. A pitch that argues for Build 5 purely on accuracy,
without ever running the ratio, has fallen into this trap even if its prose sounds confident and
even if Build 5 is, on its own separate accuracy-only merits, a defensible real-world engineering
choice (see Argument for B, above — the trap is skipping the metric, not the conclusion itself).

**A second, related trap:** a student who does attempt D3's operation count may double- or
under-count operations by not tracking which intermediate values (θ², θ³) are reused between the
cubic and fifth-order terms — e.g., computing θ⁵ from scratch as θ·θ·θ·θ·θ (4 multiplies) instead
of reusing θ³·θ² (1 multiply), inflating Build 5's true compute cost and exaggerating the case's
already-real cost gap. Watch for a D3 table whose Build 5 operation count is much higher than 5;
ask the student to show which values they reused.

## Twist

Not a scripted mid-discussion reveal — the twist here is structural, the same shape as
the-deferred-repair's: **the specific gust-tilt band a student is most likely to treat as
unremarkable (30°, right in the middle of Appendix E's table) is also the exact lever that flips
the case's recommendation.** Facilitators can manufacture the twist moment directly by running
Socratic Question 2 once a recommendation has started to form: ask the room whether Build 3's
error at 30° is comfortably under tolerance or uncomfortably close to it (it is the latter — compute
it live: θ = 30° = 0.5236 rad, error ≈ 0.000326 against a 0.0003 tolerance), then ask what happens
to the whole case if that band turns out to be a little more common than Appendix E assumes.

**Two conventions the facilitator must state OUT LOUD when running this twist, found necessary by
an adversarial Tier 2 P4 pass (2026-09-05) — without them, the twist can be read as inert:**

1. **Where the extra 30° weight comes from.** State explicitly that the 30° band's share rises
   *on its own* — matching `sensitivity_model.py`'s actual `FLEX` convention, the same one used
   for every other case's Tier 2 P5 sweep in this pipeline — not that it is reallocated from
   another band. (If a room instead assumes the extra weight is pulled from the already-failing
   40°/50° bands rather than the passing 10°/20° bands, Build 3's error rate does not change at
   all and the twist correctly "does nothing" — that is a real, defensible reading the facilitator
   should be ready for, not a broken twist. Naming the convention up front prevents the room from
   splitting on an unstated assumption instead of the case's real math.)
2. **What Appendix E's tolerance actually gates.** State explicitly that Challenge 3 (D5) treats
   the tolerance as a graded input into the named ratio metric — an exceeded band counts against
   `error_rate`, which is *weighed against* compute cost, not an automatic disqualification. A room
   that instead treats the tolerance as a hard pass/fail safety veto (a legitimate reading of
   Appendix E's "maximum acceptable" language, and exactly Argument for B's position, above) will
   correctly conclude Build 3 is already disqualified before the twist even lands, and the twist
   will feel like it changes nothing — because for that room, under that reading, it doesn't. Both
   readings are legitimate; the facilitator's job is to make the room commit to one before running
   the twist, and to name the other explicitly afterward as the position Argument for B occupies.

---

## Guide Notes — the anchor ladder (SPEC facilitator-artifacts section, anchor-ladder subsection)

### Intro

Frame the format: two identical-looking USB drives, one folding table at a trailhead, ninety
seconds of usable light, and a missing hiker whose thermal signature is fading with the
temperature. Name the stakes plainly before the drone-engineering framing takes over.

### Launch

Read the Overview aloud. Stop at "her thumb hovers between two identical-looking USB drives."
Ask the room: "Before you know a single number about either build, what would make you trust the
*more accurate* code less than the *cheaper* code, in a situation like this?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "Build 3 or Build 5 — show of hands." Most rooms will lean toward Build 5 on
instinct (more accurate sounds safer); record the split and hold the room to it.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push past "which build is more accurate" toward "what is the case actually asking you to
optimize?" Get the room to read Challenge 3 (D5)'s metric out loud — (1 − error rate) ÷ compute
cost — and sit with the fact that this is not the same question as "which build is more accurate."

### Anchor 3 — WHAT IS THE PROCESS?

Before touching Appendix E's numbers, get the room to state the actual build order out loud:
derive both polynomials from the general Taylor formula (D1), compute exact errors at each gust
angle (D2), count operations and convert to real time (D3), scale up to the whole mission and
compute each build's error rate and total compute budget (D4), then and only then compute the
metric (D5). Re-ask: "Now that we have a process, is 'which build is more accurate' still the
right question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknowns explicitly: nobody has flown this exact canyon before, so nobody
knows the real gust-tilt frequency distribution (MA1) or whether 0.0003 (MA2) is the right
tolerance. "Is 40/27/20/10/3 a fact, or a defensible guess? What would make a different guess just
as defensible?"

### Data Deep Dive

Now open Appendices A–E. Run D1–D5 as a room, or have groups report out. This is also the moment
to run Socratic Questions 1, 3, and 4 (the metric-vs-accuracy framing, the Taylor derivation
itself, and the convergence check).

### Twist

Once D4's numbers are on the table and a recommendation has started to form, run Socratic
Question 2 directly: compute Build 3's error at the 30° band live (≈0.000326) against the 0.0003
tolerance, and ask what happens if 30°-band gusts are a little more common than Appendix E assumes.
Let the room discover that the margin is only 11.7% and the 30° band is the single most
leverage-sensitive number in the whole case.

### Close

VOTE AGAIN. "Did the vote move? For the people who didn't move, what would it take to change your
mind — a different number, or a different assumption entirely?"

### Lessons Learned

The core transferable idea: a more mathematically accurate model is not automatically the better
engineering choice once you weigh what accuracy actually costs to achieve — and a margin this thin
(11.7%, hinging on one gust band sitting right at a tolerance boundary) is exactly the kind of
result that should make an engineer state their assumptions out loud rather than trust the "obvious"
answer.

### Standards Touched On

Taylor Series; How to find the Taylor series of a function at a point; Sequence; Series; How to
determine whether a series converges or diverges; How to convert an amount with compound units;
How to find the percent of a number.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00–8:00 | Position defense: "Convince us your build is the right engineering choice, not just the one that sounds more precise" |
| 8:00–15:00 | Derive both Taylor polynomials from scratch (D1); confirm neither build's coefficients were just quoted |
| 15:00–25:00 | Build D2's exact-error table and D3's operation-count/compute-cost derivation as a room |
| 25:00–32:00 | Build D4's whole-mission error-rate and compute-budget table; compute D5's metric and confirm the 11.7% margin |
| **32:00** | **DROP THE TWIST** — Socratic Question 2: Build 3's error at the 30° band is only barely under (in fact just over) tolerance; what happens if that band is a little more common than assumed? |
| 32:00–40:00 | Pressure-test MA1 directly: how close is 11.7% to flipping, and what would a defensible challenge to the 30° band's weight actually change? |
| 40:00–45:00 | Close, re-vote, lessons learned |

## Cohort bands (SPEC facilitator-artifacts section, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12-20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6-11)** | smaller room | Anchors 2-3 combine into one pass; the D3/D4 compute-cost build-out runs as a single worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1-2)** | tutoring context | No vote at Anchor 1 — ask for a stated initial position and why instead; the facilitator plays devil's advocate directly rather than cold-calling the room; the MA1/MA2 pressure-test (32:00-40:00) still runs in full, since it is the single most important move in the case |
