# Guide Notes: The Parity Check

MS | Guide Notes | Adventure | 2026
**Tier:** T2 (MS core) · **Primary metric:** extra overhead bits transmitted per additional error pattern caught · **Margin:** 9.40% (B, the Full-Frame Guard, at the reported 35-byte packet size — confirmed robust across the full disclosed per-bit error-rate range; see Robustness Check below. An earlier draft reported this margin at exactly 32 bytes, the schemes' geometric tie point, and got a coin-flip 0.02% — retuned to 35 bytes to land inside SPEC section 2's ~5-15% target band without losing robustness.)

---

## FACILITATOR ONLY — Balance Argument

**Argument for A (The Featherweight Check).** Its overhead is fixed and tiny per byte — 12.5% of
the data stream, 1 bit per 8 data bits (Appendix A, [S3]). At the case's own smallest real payload
size (11 bytes, [S4][S5]), its total added bits (11) are far fewer in absolute terms than the
Full-Frame Guard's flat 4-byte (32-bit) tax — and by the case's own "catches per bit spent" metric,
A actually wins decisively at that size (margin ~191%, stable across the full disclosed error-rate
range). Appendix E's per-bit error rate is low enough, across its whole disclosed plausible range,
that the probability of an even, undetected flip per byte stays small — the cheap scheme's blind
spot genuinely does rarely cost anything at Renata's smallest packets.

**Argument for B (The Full-Frame Guard).** It catches essentially all realistic error patterns,
including the entire class of even-bit-flip errors A is blind to *by construction*, not as a rare
edge case — that gap exists on every single byte, always. Its fixed 32-bit cost is trivial as a
fraction of a large packet: at Renata's mid and largest real payload sizes (125 and 222 bytes,
[S5]), B wins by a landslide (margins ~291% and ~594%, both stable across the full disclosed
error-rate range) — the fixed tax is by then a *much smaller* overhead percentage than A's
per-byte cost. And even at 35 bytes — a compact multi-field payload only a few bytes past the two
schemes' raw arithmetic tie point (32 bytes: 1 bit/byte × 32 bytes = 32 bits = B's own sourced
overhead, exactly) — B is already ahead by a real, checkable margin (~9.4%), and that lead is the
one this case reports (margin_pct).

**Margin basis** (`case.json.balance.margin_basis`): for each scheme, compute
`P(scheme catches the frame's corruption) / (overhead bits that scheme adds)` — this case's own
"catches more corrupted frames per bit spent" framing. Compare the two efficiencies directly at
each Appendix C packet size. The raw arithmetic tie point is exactly n = 32 bytes (independent of
the error rate to leading order). An earlier draft set Appendix C row 2 exactly there (MA2) and
computed `margin_pct = 0.02` — a razor-thin, essentially coin-flip result: because the metric
compounds so steeply near the tie point (margin climbs from ~3% to ~66% between n=31 and n=53),
sitting exactly on n=32 meant a fresh solver's rounding choices could plausibly land the arithmetic
on either side. MA2 was retuned to **n = 35 bytes** — still close enough to the tie point to be a
genuinely live, non-landslide comparison (unlike n=11/125/222), but far enough off it that the
margin lands inside SPEC section 2's ~5–15% target band. **`margin_pct` = 9.40** (Full-Frame
Guard/B wins, at Appendix E's stated 6×10⁻⁵ error rate, computed at n = 35 bytes) — see the
Robustness Check immediately below for confirmation this margin holds across the full disclosed
error-rate range.

### Robustness Check — completed, PASSED (case retuned after an initial coin-flip result)

This session killed `cases/the-overlap-call` for a margin that *looked* close (1.11%) but was
non-robust: it flipped under small, realistic changes to a stated Modeling Assumption. **The Parity
Check had the identical fragility shape at write time** — its primary metric's denominator
(error patterns caught) depends on Appendix E's per-bit error rate, which turned out, as
anticipated, to have no single hard-sourced figure and to require a disclosed Modeling Assumption
(MA1, 6×10⁻⁵, informed by IEEE 802.15.4's real receiver-sensitivity definition — see
`RESEARCH_LOG.md`). That error-rate sweep passed cleanly (see below) — but a *second*, distinct
fragility surfaced afterward: `case-research`'s first draft set Appendix C row 2 (MA2) to exactly
32 bytes, the schemes' raw arithmetic tie point (1 bit/byte × 32 bytes = 32 bits = the CRC's
32-bit overhead), and reported `margin_pct = 0.02` — a coin-flip result for the same reason
`the-overlap-call` failed: a fresh solver's own rounding could plausibly land on either side. MA2
was retuned to **35 bytes** (see `RESEARCH_LOG.md`'s "Retune" entry) — this section reflects that
final, retuned state.

**`case-research` ran the required sweep** (`sensitivity_model.py`, `FLEX = ["error_rate"]`) across
MA1's full disclosed real-world-plausible range, **1×10⁻⁶ to 1×10⁻³** (three orders of magnitude,
bounded by real published wireless-link BER figures found during research), at the case's reported
packet size (**35 bytes**):

| error_rate | winner at n=35 | margin |
|---|---|---|
| 1e-6 | B | 9.3754% |
| 1e-5 | B | 9.3788% |
| 6e-5 (stated) | B | 9.3978% |
| 1e-4 | B | 9.4128% |
| 1e-3 | B | 9.7084% |

**Result: STABLE.** The winner (B) never flips across the full range, and the margin barely moves
(9.38%–9.71%, less than 0.4 percentage points across three orders of magnitude of error-rate
assumption) — comfortably inside SPEC section 2's ~5–15% target band and well under its 20% cap
throughout. The schemes' raw arithmetic tie point itself (where n bytes of parity overhead exactly
equals the CRC's 32-bit tax) stays at 31.90–32.00 bytes across the same sweep, unchanged by the
MA2 retune — only the *reported* packet size moved, from sitting exactly on that tie point to
sitting a defensible few bytes past it. This case is **not** in the-overlap-call's fragility class.
`case.json.balance.robustness_check` and `sensitivity_note` record this in full;
`sensitivity_disclosure[]` is correctly empty since nothing swept flips the winner or breaches the
SPEC §2 20% cap at the reported size.

One honest caveat for whoever runs the discussion: **away from n≈32–35, packet size alone — not
the error rate — decides the winner**, and decisively (A wins outright at 11 bytes, B wins outright
at 125 and 222 bytes, both by hundreds-of-percent margins, stable across the whole error-rate
range). The 9.40% figure is real and robust, but it describes one specific, deliberately-chosen
packet size close to the schemes' tie point, not "the" answer for every payload Renata ships —
Anchor 3/Anchor 4 below lean into exactly this.

---

## Five Socratic Questions

1. "Your D3 table shows the Featherweight Check's overhead as 11 bits (11 bytes × 1 bit/byte) on the smallest packet, and the Full-Frame Guard's overhead as a flat 32 bits on every packet. At what packet size, exactly, does the Featherweight Check's total overhead equal 32 bits? Show the arithmetic, not a guess." *(Answer: exactly 32 bytes — 1 bit/byte × 32 bytes = 32 bits. Appendix C's row 2 is 35 bytes, deliberately a few bytes past this tie point, not sitting on it — press on why the case would choose a size close to, but not exactly at, its own break-even.)*
2. "You classified byte #1 as having an EVEN number of flipped bits in D2 (4 ones → 6 ones is still even). If it had been ODD instead, would the Featherweight Check have caught it? What does that tell you about what 'even' actually means for this scheme — bad luck, or a guarantee?"
3. "D5 asks you to compute the packet size where the two schemes' raw arithmetic crosses (32 bytes). Appendix C row 2 reports the comparison at 35 bytes instead — three bytes past that crossover. Renata's actual packets run from 11 to 222 bytes. Does either number fall inside that range, and what does the gap between 'exact tie point' and 'reported comparison size' tell you about how sensitive this recommendation is to which packet size you pick?"
4. "Appendix E states a per-bit error rate of 6×10⁻⁵. If it turned out to be 1×10⁻⁶ instead — a hundred times better — would your D5 recommendation at 35 bytes change? What if it were 1×10⁻³ — over ten times worse? Defend your answer with the actual ratio, not intuition." *(A defensible answer: no, it would not change at 35 bytes — the Full-Frame Guard stays ahead across that whole range, with the margin moving only from about 9.4% to about 9.7%. Push on WHY it barely moves: is that a coincidence, or does it follow from where 35 bytes sits relative to the two schemes' fixed costs?)*
5. "The Full-Frame Guard needs 10 decimal digits to write out its largest possible check value (2³²−1 = 4,294,967,295); the Featherweight Check needs 1. Does that gap matter for Renata's decision, or is it a fact that's true but not load-bearing? Defend either answer."

## The Trap

Heroes will compare **raw overhead** — "4 bytes vs. basically nothing" — and conclude the
Featherweight Check obviously wins, without noticing that its "basically nothing" (1 bit per byte)
*scales with packet size* while the Full-Frame Guard's 4 bytes is *fixed regardless of size*. On a
large enough packet, the Featherweight Check's cumulative overhead can exceed the Full-Frame
Guard's flat tax — the comparison flips, and a Hero who anchored on the small-packet number never
re-checks it. The second, deeper trap: Heroes treat the Featherweight Check's blind spot as
occasional bad luck ("it usually still works") rather than a structural guarantee — *any* even
number of flipped bits in a byte is invisible to a single parity bit, every single time, not most
of the time. A Hero who says "parity mostly catches errors" has not understood the mechanism; a
Hero who says "parity catches every odd-count flip and zero even-count flips, full stop" has.

## Twist

**Twist:** During the Data Deep Dive, reveal that the hardware team has just confirmed the sensor
radio's real per-bit error rate is dominated by burst noise from a nearby transmitter during
specific weather conditions — not the flat, uniform bit-error rate Appendix E states as a baseline
assumption. Burst errors tend to flip *clusters* of adjacent bits, which changes the even/odd split
in ways a uniform-rate model does not predict. Ask: *"You have sixty seconds. Does your D5
break-even number still hold? What would you need to re-check?"* This does not hand anyone a new
number — it invalidates the *uniform-error* assumption underlying whichever recommendation the room
converged on, without making either scheme obviously correct on its own. (If `case-research` later
sources a single well-supported per-bit error rate with no meaningful burst-error caveat available,
this twist may be marked `N/A` with that finding noted here — but do not drop it solely for
convenience; a burst-vs-uniform distinction is a real, well-documented property of real radio links
and is worth pursuing as a genuine twist first.)

## Anchor Ladder

#### Intro
Frame the format: this is a Harvard/Acton-style case, no answer key, defend your choice
to peers. Opener: *"Renata has forty minutes and eleven thousand sensors she can't touch again.
What does she ship tonight?"*

#### Launch
Show a packet trace: a real Wi-Fi frame capture (or a diagram of one) with its 4-byte
FCS visibly labeled, next to a tiny 8–16 byte sensor payload with a single parity bit visibly
labeled. Ask: *"Which one of these feels expensive to you? Now — expensive relative to what?"*

#### Anchor 1 — Take a stand and vote.
Featherweight Check or Full-Frame Guard. No reasoning yet.
Hands up for A, hands up for B. Write the split on the board. *"Is anyone courageous enough to
stand with the parity bit alone?"*

#### Anchor 2 — What is the problem we're solving?
Do not let them calculate yet.
- Is the question "which scheme costs less"? "Which scheme catches more"? Those have different
  answers — say which one out loud.
- Someone will say "the one that catches more errors is obviously better." Catches more *per what*?
- Let the confusion grow. *"Wow, this is a harder question than it looked."*

#### Anchor 3 — What is the process?
- If we just compare raw bytes added, are we done? What's missing?
- If Option A wins on one packet size and Option B wins on another, how do we decide which packet
  size is the one that matters?
- Is our question still the right question?

#### Anchor 4 — What don't we know?
- What is Appendix E's error rate actually based on? Do we believe it?
- Have them re-run D5's break-even calculation with the error rate doubled, then halved. Does the
  recommendation survive?
- What are we assuming about whether every one of Renata's sensors uses the same packet size?

#### Data Deep Dive
Now, and only now, work through D1–D5 with real numbers once sourced.

#### Twist
Drop the burst-noise reveal (above), slowly, with pauses.

#### Close
Re-vote. *"Did we ask the right question? What math was new to you, and how did you
attack it?"*

#### Lessons Learned / Standards Touched On
Even, Odd, Digit, Number, Probability — see Appendix H.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote — no explanation |
| 3:00–10:00 | Position defense: "Convince us it's the better scheme, not just the cheaper one" |
| 10:00–15:00 | Pressure-test the models: "Whose recommendation is most fragile if the error rate is wrong?" |
| **15:00** | **DROP THE TWIST** — the burst-noise reveal, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke in your model?" |
| 20:00–30:00 | Threaded deep conflict (2–3 named threads): raw-overhead vs. per-bit-spent thinking; "occasional miss" vs. "structural guarantee"; uniform-error vs. burst-error assumptions |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Cohort Bands

| Band | Typical size | What changes |
|---|---|---|
| **Full** | 12–16 Heroes | The Socratic plan and Anchor timings run as written above. |
| **Compressed** | 6–8 Heroes | Anchors 2–3 combine into one pass; the twist still drops at 15:00 but the deep-conflict section (20:00–30:00) runs one thread instead of two or three — the "occasional miss vs. structural guarantee" thread is the strongest single thread if only one fits; total runtime shortens proportionally, not the content. |
| **1:1 / pair** | 1–2 Heroes | There is no vote to take — Anchor 1 becomes a stated initial position instead of a show of hands. The guide plays devil's advocate directly, arguing the other option, rather than cold-calling peers. The twist still lands, but "who reverses" becomes "would you reverse, and why — walk me through your D5 numbers again." |

## Sensitivity Note

See the Robustness Check section above — this is the load-bearing note for this case. SPEC §6's
"None required" scoping from the concept sheet stands for the *subject-matter* sensitivity note
(no death-toll/casualty framing issue here). The **numeric robustness check on the per-bit error
rate (MA1)** has now been run and **passed**: the winner at the case's reported packet size (35
bytes) is stable across the full disclosed 1×10⁻⁶–1×10⁻³ range, and `sensitivity_disclosure[]` is
correctly empty. The one real, disclosed sensitivity that remains is **packet size itself** (MA2,
`case.json.modeling_assumptions`) — not a fragility to hide, but the case's actual pedagogical
point: a Hero who only checks one packet size has not solved D5.
