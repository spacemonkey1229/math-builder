# Guide Notes: Turbine Channel

MS | Guide Notes | Launchpad | 2026-27
**Tier:** T4 (HS) · **Primary metric:** kilowatt-hours of generation potential per cubic meter of water moved, per tidal cycle · **Margin:** **9.21% — the Reach wins**

---

## Status note — updated after case-research (2026-09-11)

This file's numbers are now real. `case.md`'s Appendices A/B/C/D are filled with real NOAA current
data (stations ca0101 "Cape Cod Canal, West End" for the Narrows and cb0102 "Cape Henry LB 2CH" for
the Reach), real channel/turbine geometry, and one disclosed Modeling Assumption for the Reach's
array-site width (MA1) plus one derived Modeling Assumption for the generation-potential conversion
factor (MA2). Full source trail and rejected paths: `RESEARCH_LOG.md`. Full record entries:
`case.json.sources[]` and `case.json.modeling_assumptions[]`.

**The flagged assumption candidate resolved:** Appendix D's generation-potential conversion factor
had no public "kWh per m³" spec anywhere (no manufacturer or DOE/NREL report publishes that ratio
directly). It is now MA2: **derived** (not invented) from a real, deployed small tidal-turbine
array's real published rated output and design current speed (Verdant Power's Gen5 KHPS array,
Roosevelt Island Tidal Energy project, East River NYC — 1,050 kW combined at 2.25 m/s through a
589.0 m² swept footprint), giving 0.00022 kWh/m³, applied identically to both channels.

---

## Argument for A (the Narrows)

The Narrows' current-speed curve is tall and narrow — a short flow window with a high peak speed.
Because the definite integral of speed over time gives total distance the water travels (which,
multiplied by cross-sectional area, gives volume), a high peak can move a large amount of water
even in a short window, *if* the channel's cross-section is large enough. The Narrows is also the
site where a small array's swept footprint is more likely to occupy a meaningful share of the
total channel cross-section, which could mean less of the fast water actually clears the array's
face unobstructed. The strongest real argument for A is that peak-speed sites are traditionally
preferred for kinetic turbines because power extraction (not modeled directly in this case, but
worth knowing as a fact) scales with the *cube* of current speed, so a channel with a much higher
peak, even briefly, may still come out ahead on total energy potential.

## Argument for B (the Reach)

The Reach's curve is short and wide — lower peak, longer duration. A long, flat flow window can
integrate to a comparable or larger total volume than a narrow spike, the same way a long, low
rectangle can have the same area as a tall, narrow one. The Reach is also less likely to see the
turbine array's own footprint distort the flow (a wider channel is less "clogged" by a fixed-size
array), and a slower current is mechanically gentler on the array over the life of the pilot
program — a real operational consideration even though it is not part of this case's primary
metric.

## Margin

**Computed: 9.21%, the Reach wins.** Using numerical (trapezoidal) integration over each station's
complete real 6-minute NOAA series:

| Channel | Flow window | ∫speed dt | Cross-section | Volume/cycle | kWh/cycle |
|---|---|---|---|---|---|
| Narrows (ca0101) | 366 min, peak 5.28 kn | 34,675 m | 1,427.0 m² [S3, S8] | 49,480,854 m³ | 10,889 |
| Reach (cb0102) | 456 min, peak 1.53 kn | 12,702 m | 4,290.6 m² [MA1] | 54,498,397 m³ | 11,993 |

`margin_pct = |10,889 − 11,993| / 11,993 × 100 = 9.21%`. Because Appendix D's conversion factor
(MA2) is applied identically to both channels, the kWh margin equals the volume margin exactly —
the case's real decisive variable is total volume moved (Challenge D3), not a per-channel-varying
efficiency ratio. See "A note on the 'ratio vs. total' trap," below, for what this means for the
Socratic plan's second deep-conflict thread.

**How the margin was tuned to land inside SPEC §2's ~20% cap:** the two real NOAA stations were
already well-suited (Cape Cod Canal's peak speed is 3.4× the Reach candidate's, and its flow window
is markedly shorter) — no station swap was needed. What *did* need tuning was MA1, the Reach's
array-site cross-sectional width, since the real bay entrance the Reach is modeled on is ~12 miles
wide end to end and has no single real "array site" width. An early attempt to also let the
generation-potential conversion factor vary by channel (scaling with each channel's characteristic
speed squared, grounded in the real v³ power-vs-v flow-rate relationship) was tried and rejected: it
made the Narrows win by 77%–96% regardless of the Reach's cross-section, even at unrealistically
large sizes. MA1's width (256 m, real charted depth 16.76 m) was the one lever both grounded in real
scale and capable of producing genuine balance — full reasoning in `RESEARCH_LOG.md`.

---

## Five Socratic questions

1. "Your definite integral says the Narrows moves about 49.5 million m³ per cycle and the Reach
   moves about 54.5 million m³. Which channel would you have guessed wins, just from looking at
   the two scatter plots — and were you right?"
2. "If you had used a Riemann sum instead of your fitted curve's antiderivative, would your D4 and
   D3 answers for the Narrows agree closely, or not? What does a big disagreement between the two
   methods tell you about how well your polynomial actually fits the peaked curve?"
3. "The Narrows has a much higher peak current speed than the Reach. Does a higher peak necessarily
   mean more total water moved? Show me the calculation that answers that, not just your intuition."
4. "Appendix D's generation-potential conversion factor turned out to be a stated assumption, not a
   sourced fact. If that number were 20% higher for both channels, would your recommendation
   change? What if it changed by a different amount for the Narrows than for the Reach?"
5. "You assumed the channel's cross-section stays constant across the whole flow window. Is that
   more true for the Narrows or for the Reach? Which channel's real answer is more sensitive to
   that simplification?"

## The trap

**The trap is treating peak current speed as a proxy for total volume moved.** A learner who sees
the Narrows' current racing past at multiples of the Reach's peak speed will often assume, without
computing anything, that the Narrows must move more water. That is exactly the intuition a definite
integral is built to correct: area under a tall, narrow curve is not automatically bigger than area
under a short, wide one — it depends on both height *and* width together, which is the entire reason
this case forces an actual integral instead of "just compare the peaks." A student who reports a
recommendation using only the peak-speed column from Appendix A/B, without ever completing D2-D3's
curve-fit-and-integrate work, has fallen into the trap and should be asked directly: "where in your
work did you account for how *long* each channel's current runs, not just how *fast*?"

A second, quieter version of the same trap, **updated after case-research**: with this case's real
sourced data, Appendix D's generation-potential conversion factor (MA2) is a single value applied
identically to both channels, so whichever channel wins Challenge D3's volume automatically wins
Challenge D5's total kWh too — they do not diverge in this case's real numbers. The trap here is
narrower but still real: a pitch that reports only D3's volume, or only D5's final kWh figure,
without showing the compound-unit conversion chain that connects them (m³ → kWh via a kWh-per-m³
factor) has not actually completed Challenge D5, which exists specifically to force that unit-
conversion step (`measurement-how-to-convert-an-amount-with-compound-units`) — not to reveal a
different winner. A sharp Hero may notice this on their own and ask *why* the ratio and the total
agree here; that observation (MA2 is shared, not channel-specific) is itself worth surfacing in
discussion — see Deep Conflict Thread 2 below.

## Twist

**N/A**, per the concept sheet's own scoring: this is a siting/business decision with real technical
tension already (the peak-vs-duration trade-off), but no personal stakes and no natural piece of
withheld information that would invalidate a popular position without simply changing the inputs.
Authors should still consider one during case-research if a genuine complication surfaces — e.g., if
the two real NOAA stations turn out to have meaningfully different data-record lengths or gaps that
would force a "which curve do you trust more" discussion — but none is manufactured here just to
check a box.

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. Show the two channels' scatter plots side by side, unlabeled by A/B. *"Thirty seconds — which curve do you think moves more water, just from looking at it?"* Stand/sit vote. No calculation yet. |
| **3:00–10:00** | Position defense. *"Convince us — not just that your channel looks faster, but that it moves more water."* Press anyone arguing from peak speed alone: *"Where's your integral?"* |
| **10:00–15:00** | Pressure-test the models. *"Whose curve fit do you trust least? Where does your Riemann sum (D4) disagree with your FTC answer (D3), and why might that be?"* |
| **15:00–20:00** | Deep dive on the conversion factor. *"Appendix D's kWh-per-m³ figure (0.00022) was derived from a real turbine's real rated output, not published directly — and it's the same number for both channels. What happens to your recommendation if it's wrong by 20% — does it matter that it's wrong by the same amount for both?"* |
| **20:00–30:00** | Two threads: **(1) height vs. width** — "does a taller peak or a longer window matter more, and does that answer change depending on the channel's cross-section?"; **(2) volume vs. ratio** — "your D3 volume and your D5 kWh always agree here, since Appendix D's factor is shared. Why does that make sense? What would have to be true for a channel to win on total water but lose on kWh per m³?" |
| **30:00–45:00** | Close, re-vote against the Anchor 1 board, reflection, lessons learned. |

---

## Guide Notes — the anchor ladder

### Intro
Heroes, today's case is a real engineering trade-off: fast-and-short versus slow-and-long, and the
only way to settle it honestly is to actually integrate the two curves instead of eyeballing them.

### Launch
Show the two channels' current-speed scatter plots side by side, axes unlabeled by channel name.
*"One of these is a channel that could knock you off your feet. The other one you could wade
across at slack water and barely notice it start to pull. Which one do you think generates more
power?"*

### Anchor 1 — Take a stand and vote
Narrows or Reach. No reasoning yet. Hands up, write the split on the board.
*"Is anyone courageous enough to stand with the slow one?"*

### Anchor 2 — What is the problem we're solving?
Do not let them calculate yet.
- What is the actual question? Is it "which channel is faster"? "Which channel moves more total
  water"? "Which channel makes more electricity per cubic meter of water"? **Those are three
  different questions.**
- Someone will say "obviously the fast one generates more power." What do they mean by *more* —
  more total, or more per unit of water?
- Let the confusion grow. *"Wow. This is a genuinely hard question to even state precisely."*

### Anchor 3 — What is the process?
- If we just compare peak speeds, are we done? (No — the Narrows' peak is 3.4x the Reach's, and it
  still loses on total volume.)
- With this case's real data, whichever channel wins Challenge D3's total volume also wins Challenge
  D5's total kWh (Appendix D's factor is one shared number, not two). Ask the room: does that mean
  D5 was pointless? (No — D5 still forces the actual unit-conversion chain, m³ into kWh, which is
  its own real skill; it just happens not to change the winner here. Push further: *what would have
  to be different about Appendix D for D3 and D5 to disagree?*)
- Is our question still the right question?

### Anchor 4 — What don't we know?
- What's missing that we'd need to answer this properly? (Now answered by real data — but ask what
  Dana still doesn't know: how much of the Reach's real ~12-mile-wide entrance would actually be
  usable for a turbine array, whether 256 m is really achievable, whether cross-section truly stays
  constant across the whole flow window.)
- Appendix D's generation-potential conversion factor is a stated (though real-data-derived)
  assumption. Do you believe it? What would you need to see to trust it more?
- Does the "constant cross-section" simplification in Appendix C matter more for one channel than
  the other?

## Data Deep Dive
Walk the room through fitting a curve to the real Appendix A/B data, taking its antiderivative by
the power rule, evaluating the definite integral via FTC, cross-checking against a Riemann sum, and
converting to the final kWh figure. Ground truth for cross-checking a Hero's own work (from
case-research's numerical integration over the *complete* real series, not just the seven
representative rows in case.md):

| Channel | Volume/cycle | kWh/cycle |
|---|---|---|
| Narrows | ≈49,480,854 m³ | ≈10,889 kWh |
| Reach | ≈54,498,397 m³ | ≈11,993 kWh |

A Hero's own polynomial-fit-based D2/D3 answer will not match these exactly — a lower-degree
polynomial fit to only the seven representative table rows will diverge somewhat from a numerical
integration over the complete 61/77-point series, and that divergence is itself worth discussing
(see D4's cross-check purpose, and Socratic question 2).

## Close
- Vote again. Who moved, and why?
- Was "which channel moves more water" the right question, or was it really "which channel
  generates more power per cubic meter"?
- What math was new to you here — the curve fitting, the antiderivative, or converting the units
  at the end?

## Lessons Learned
The case's real lesson sits in the gap between three different numbers that can each look like "the
answer": total volume moved (D3), the Riemann-sum cross-check (D4), and the generation-potential
ratio (D5). A student who only computes the first has answered a question the case never actually
asked. The trade-off between a tall, narrow curve and a short, wide one is a genuine application of
the definite integral, not a manufactured one — the physical situation forces exactly the tool this
case is built to teach.

## Standards Touched On

**New coverage:** none — see `case.json.reinforcement_note`. This case reinforces all seven
Calculus/Integrals skills from n=2 to n=3, the group's entire remaining thin set.

**Claimed:** Antiderivative · Definite Integral · Indefinite Integral · Riemann Sum · How to find an
antiderivative using the power rule · How to evaluate a definite integral using the Fundamental
Theorem of Calculus · How to approximate area under a curve using a Riemann sum · How to convert an
amount with compound units · How to create a scatter plot given a set of data

## Facilitator note — sensitivity

None required. This is a siting/business decision (which channel to recommend to a utility board)
with no death, illness, or family-hardship stakes — SPEC §6 does not apply.
