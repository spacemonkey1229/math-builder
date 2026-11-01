# Guide Notes: The Hub Choice

MS | Guide Notes | Adventure | 2026
**Tier:** T2 (MS core) · **Primary metric:** minutes of weekly travel time saved per dollar of annual route operating cost · **Margin:** 15.89% (A, the Hub Link, at the case's shared ridership/ground-overhead assumptions — confirmed robust across the full disclosed ground-overhead range; see Robustness Check below.)

---

## FACILITATOR ONLY — Balance Argument

**Argument for A (Route A, The Hub Link).** Route A connects two airports Finger Lakes Regional
Air already serves — BGM and ART already have the airline's ground crew, gates, and existing
network reach. Today, the only way to fly between them uses the existing network's three-leg
connection (BGM→MSS→OGS→ART), which takes over four hours door-to-door once ground time at each
stop is counted — so in practice nearly everyone drives the 135-minute route instead. A new
direct flight at 79.7 minutes door-to-door saves 55.3 minutes per traveler over driving, and at
the shared 25-traveler/week estimate and $289,145/year operating cost, that's **0.24849 minutes
saved per dollar** — the higher of the two options on this case's own figures.

**Argument for B (Route B, The New City Link).** Route B creates a route from nothing: today,
anyone traveling between the ART hub area and Cortland drives the entire 110-minute trip because
no commercial air option exists at all. A new direct flight saves 37.6 minutes per traveler — a
smaller per-rider gap than Route A's, but the route is also shorter and cheaper to fly
($228,024/year). At the same shared 25-traveler/week estimate, Route B comes in at **0.21442
minutes saved per dollar — only 15.89% behind Route A**, close enough that a change in either
route's actual ridership (not assumed, but observed once flying) could plausibly flip which
option looks better in hindsight.

**Margin basis** (`case.json.balance.margin_basis`): (shared weekly travelers × minutes saved per
traveler vs. driving × 52 weeks) ÷ annual operating cost, computed separately for A and B from
Appendix B–E's sourced/derived figures and Appendix F's shared ground-overhead (MA1) and
ridership (MA2) assumptions. **`margin_pct` = 15.89** (Route A wins).

### Robustness Check — completed, PASSED (case retuned after an initial fragile result)

An earlier draft of this case set ground-time overhead (MA1) to 30 minutes and gave Route A and
Route B *different, independently-guessed* weekly-ridership figures (22/week and 20/week). That
version's base margin looked fine (a defensible ~15%) but was **not robust**: flexing either route's
ridership assumption independently by ±50% flipped the winner (Route A's ridership at −50% let
Route B win; Route B's ridership at +50% let it overtake Route A). Per this project's own rule —
a verdict that flips under a ±50% assumption flex is retuned in case-write/case-research, never
hidden — the case was redesigned:

1. **Ridership became a single shared assumption (25/week, applied identically to both routes)**
   instead of two independent guesses. Because it multiplies both routes' numerators by the same
   factor, it now cancels out of the A-vs-B ratio *by construction* and can never flip the winner.
2. **Ground overhead (MA1) — the one assumption that actually determines the winner — was
   retuned from 30 to 45 minutes.** The numeric flip point (bisected in `sensitivity_model.py`)
   is ~16.7 minutes, a fixed property of the route geometry. At a 30-minute base, that flip point
   sat inside the ±50% flex band (15–45 min); at a 45-minute base, the same flip point sits well
   outside the new band (22.5–67.5 min).

**`sensitivity_model.py` ran the required sweep** (`FLEX = ["ground_oh_min", "weekly_travelers"]`)
across MA1's full ±50% range:

| ground_oh_min | winner | margin |
|---|---|---|
| 22.5 min (−50%) | A | 1.99% |
| 33.8 min (−25%) | A | 6.86% |
| 45.0 min (base) | A | 15.89% |
| 56.2 min (+25%) | A | 24.06% |
| 67.5 min (+50%) | A | 41.53% |

**Result: STABLE.** Route A wins across the entire ±50% range; the margin narrows to ~2% at the
low end (a genuinely close call worth surfacing to a room) and widens to ~41.5% at the high end.
The shared ridership assumption (MA2) was independently confirmed to produce **zero** margin
change at ±50% (12.5 and 37.5 travelers/week both reproduce the base 15.89% margin exactly),
since it cancels out of the ratio by construction. `case.json.modeling_assumptions[]` records
both checks.

**One honest caveat for whoever runs the discussion:** at ground-overhead near the low end of its
disclosed range (~17–25 minutes), Route A's lead shrinks close to a coin flip. A Hero who argues
small regional airports could plausibly run closer to 20–25 minutes of ground time (no security
line, quick boarding) is making a legitimate point, and the case should be presented as "Route A
wins on the stated figures, by a margin that is real but not overwhelming" — not as a landslide.

---

## Five Socratic Questions

1. "Your D4 table gives Route A a 15.89% edge. Which single number in Appendices C–E, if it
   turned out to be wrong, would worry you most — and is that number sourced, derived, or
   assumed?" *(The strongest answer names MA1, ground-time overhead — it's the only assumption
   that actually moves the winner; MA2 and MA3, ridership and frequency, are shared across both
   routes and cancel out.)*
2. "Appendix F applies the *same* 25-travelers-per-week estimate to both routes. Is that fair?
   Make the case for why Route A (an already-connected corridor) or Route B (a brand-new market)
   deserves a different number — and recompute D4 with your alternative." *(Either direction is
   defensible; press on whether the Hero's new numbers are themselves sourced, derived, or just a
   different guess.)*
3. "Route A's 'today' alternative includes a genuinely terrible existing-network option (three
   legs, four-plus hours) that almost nobody actually takes. Why does the case still show you
   that number in D2, if the D3/D4 math uses driving time instead?" *(Because it explains WHY the
   route doesn't exist yet despite the network technically connecting the two airports — the
   binomial coefficient in D1 shows 15 possible pairs but only 5 are flown; this is one of the
   10 unflown pairs, and the existing-network path shows why flying the long way was never worth
   it.)*
4. "Ground-time overhead (45 minutes) is the single assumption this case's own robustness check
   flexed. If a facilitator told you real regional-airport turn times run closer to 60 minutes,
   would your D4 recommendation change? What about 20 minutes?" *(At 60 min, Route A wins by
   ~30%+; at 20 min — near the ~16.7-minute flip point — the recommendation gets genuinely
   shaky. Press for the actual recomputed numbers, not a guess.)*
5. "Your ops director said 'don't make me explain a route nobody flies.' Which route's ridership
   estimate is more exposed if the real number comes in at half of what Appendix F assumes?"
   *(Trick question — since the shared ridership assumption cancels out of the A-vs-B comparison,
   NEITHER route's recommendation changes if ridership undershoots uniformly. It only matters if
   the two routes' real ridership diverges from each other, which is exactly Question 2.)*

## The Trap

Heroes will compute D1's binomial coefficient correctly, feel like they've done "the hard math,"
and then quietly skip forward to comparing raw operating costs (Appendix E) between A and B
without ever building the D3 weekly-time-saved figure — because Route A costs more to fly
($289,145 vs. $228,024), a Hero who stops there will wrongly conclude Route B is the more
efficient choice. The actual deciding variable is never the raw cost column — it's the
*time-saved-per-dollar ratio* in D4, where Route A's larger per-rider time savings (55.3 vs. 37.6
minutes) more than makes up for its higher cost. A Hero who never builds D3/D4 and just eyeballs
Appendix E has built half the case, and reached the wrong recommendation from it.

## Twist

**Twist:** During the Data Deep Dive, reveal that the ops director has just gotten word that
Cortland's county government is separately funding a free shuttle-van service to the ART hub —
timed to launch the same quarter as any new air route. The van uses the same roads Appendix D's
110-minute driving figure is based on, so it does **not** save anyone time — it is free, not
fast. Ask: *"You have sixty seconds. Route B's whole case assumes 25 people a week will pay to
fly rather than drive. If a free (if equally slow) van to the same hub now exists, does that
change how many people you'd expect to actually book Route B? What would you need to re-check?"*
This does not hand anyone a new number — it invalidates the *assumption that flying is the only
realistic way to close Cortland's access gap*, attacking Route B's ridership assumption (MA2)
rather than its time-saved figure, without making Route A obviously correct either (Route A's
driving-time baseline and the van's existence are both unaffected there — a Hero should ask
whether a similar shuttle could exist for BGM↔ART too, and why the case doesn't mention one).

## Anchor Ladder

#### Intro
Frame the format: this is a Harvard/Acton-style case, no answer key, defend your choice
to peers. Opener: *"Marcus has one route to fund and a board that already said no once. Which
sticky note does he bring to Monday's meeting?"*

#### Launch
Show the six-airport map with the 5 existing routes drawn as edges and the 10 unflown
pairs left blank. Ask: *"If the network already connects every airport to every other one, why
does it matter which NEW route gets built?"*

#### Anchor 1 — Take a stand and vote.
Route A or Route B. No reasoning yet. Hands up for A, hands up for B. Write the split
on the board. *"Is anyone courageous enough to stand with the town that has zero flights today?"*

#### Anchor 2 — What is the problem we're solving?
Do not let them calculate yet.
- Is the question "which route is cheaper to fly"? "Which route saves more total time"? "Which
  route serves more people"? Those have different answers — say which one out loud.
- Someone will say "the new-city route obviously matters more, it's going from nothing to
  something." More *per what*?
- Let the confusion grow. *"Wow, this is a harder question than it looked."*

#### Anchor 3 — What is the process?
- If we just compare which route costs less to operate, are we done? What's missing?
- If Option A wins on raw ridership and Option B wins on time saved per rider, how do we combine
  those into one number?
- Is our question still the right question?

#### Anchor 4 — What don't we know?
- Where does the 25-travelers-per-week number in Appendix F actually come from? Do we believe it
  applies equally to both routes?
- Have them re-run D4 with ground-overhead doubled, then halved. Does the recommendation survive?
- What are we assuming about how many people would actually show up to a brand-new airport in a
  town that's never had one?

#### Data Deep Dive
Now, and only now, work through D1–D5 with the real sourced/derived numbers.

#### Twist
Drop the Cortland shuttle-van reveal (above), slowly, with pauses.

#### Close
Re-vote. *"Did we ask the right question? What math was new to you, and how did you attack it?"*

#### Lessons Learned / Standards Touched On
Vertex, Edge, Graph (Vertices And Edges), Weighted Graph, Binomial Coefficient, Fundamental
Counting Principle — see Appendix G.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote — no explanation |
| 3:00–10:00 | Position defense: "Convince us it's the better route, not just the cheaper one" |
| 10:00–15:00 | Pressure-test the models: "Whose recommendation is most fragile if ground overhead or ridership is wrong?" |
| **15:00** | **DROP THE TWIST** — the Cortland shuttle-van reveal, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke in your model?" |
| 20:00–30:00 | Threaded deep conflict (2–3 named threads): raw-cost vs. time-saved-per-dollar thinking; "equal ridership is fair" vs. "the two markets are structurally different"; whether a real alternative (the shuttle) changes what "no service exists" even means |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Cohort Bands

| Band | Typical size | What changes |
|---|---|---|
| **Full** | 12–16 Heroes | The Socratic plan and Anchor timings run as written above. |
| **Compressed** | 6–8 Heroes | Anchors 2–3 combine into one pass; the twist still drops at 15:00 but the deep-conflict section (20:00–30:00) runs one thread instead of two or three — the "equal ridership is fair" thread is the strongest single thread if only one fits; total runtime shortens proportionally, not the content. |
| **1:1 / pair** | 1–2 Heroes | There is no vote to take — Anchor 1 becomes a stated initial position instead of a show of hands. The guide plays devil's advocate directly, arguing the other route, rather than cold-calling peers. The twist still lands, but "who reverses" becomes "would you reverse, and why — walk me through your D4 numbers again." |

## Sensitivity Note

See the Robustness Check section above — this is the load-bearing note for this case. SPEC §6's
"None required" scoping from the concept sheet stands for the *subject-matter* sensitivity note
(no death-toll/casualty/hardship framing issue here — this is an infrastructure-investment
decision). The **numeric robustness check on ground-time overhead (MA1)** has been run and
**passed**: the winner is stable across the full disclosed ±50% range (22.5–67.5 minutes), and
`sensitivity_disclosure[]` is correctly empty since nothing swept flips the winner. The one real,
disclosed sensitivity that remains is the **shared ridership assumption (MA2)** — not a fragility
(it provably cancels and cannot flip the winner), but a genuine, debatable modeling choice worth
pressing on in discussion (Socratic Question 2).
