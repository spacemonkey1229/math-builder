# Guide Notes: Clear-Sky Dome

MS | Guide Notes | Adventure | 2026-27
**Tier:** T3 (MS-stretch / HS-entry) · **Primary metric:** usable clear-sky observing hours per year, per dollar of dome-and-pier construction cost · **Margin:** **4.79% — Sable Hollow wins**

---

## Status note (after case-write + case-research, 2026-09-18)

This case was drafted and researched in one pass. Every figure in `case.md` is either a real, cited
source (Appendices A, B, C, D, F, I) or a stated, disclosed Modeling Assumption (Appendix G). Full
search trail: `RESEARCH_LOG.md`. Full source and assumption records: `case.json.sources[]` and
`case.json.modeling_assumptions[]`.

**The flagged construction-cost gap resolved:** the concept sheet (`CONCEPTS_astronomy_2026-09-12.md`)
flagged that no live dome-enclosure or pier-footing cost spec was confirmed at concept time. Two real
levers closed the gap: a real, dealer-hosted spec page for an actual installed Ash-Dome (5.0 m diameter,
real drum-wall and dome-cap steel weights) supplied the geometry and standard-spec material baseline,
and HUD's real, federally regulated Wind Zone I/II design speeds (24 CFR §3280.305) supplied a
defensible stand-in for "standard" vs. "reinforced" wind design, combined with a standard
structural-engineering thickness-vs-pressure relationship (MA2). No dome-specific wind-reinforcement
spec is publicly published, so MA2 is disclosed as a stated assumption, not presented as sourced.

---

## Argument for A (Vantage Mesa)

Vantage Mesa has a real, published clear-sky advantage: 77% Photometric+Clear nights (the ESO
Paranal-modeled figure) versus Sable Hollow's 62.6% ground-based clear-night fraction — about 23% more usable nights
per year, real and cited. The traditional siting instinct for a survey telescope is that more clear sky
always wins, full stop — raw observing time is the entire point of building the telescope in the first
place, and Vantage Mesa's astroclimate record is genuinely the better one on file.

## Argument for B (Sable Hollow)

Sable Hollow wins on this case's actual computed primary metric. Vantage Mesa's higher design wind
speed (100 mph vs. 70 mph, Appendix D) requires shell steel about 1.43× thicker throughout the drum
wall, dome cap, and windscreen (MA2) — pushing total dome-and-pier construction cost from $3,994.15 at
Sable Hollow to $5,159.99 at Vantage Mesa, a 29% cost increase bought for a 23% gain in usable
hours. Per dollar, Sable Hollow delivers 0.5148 usable clear-sky hours versus Vantage Mesa's 0.4902 —
Sable Hollow wins by only 4.79%, comfortably inside SPEC §2's ~20% balance cap and one of the thinnest
margins in the corpus.

## Margin

**Computed: 4.79%, Sable Hollow wins — a genuinely thin margin.**

| Site | Clear-sky fraction | Usable hours/year | Construction cost | Usable hrs/$ |
|---|---|---|---|---|
| Vantage Mesa (A) | 77% [S1] | 2,529.45 | $5,159.99 | 0.4902 |
| Sable Hollow (B) | 62.6% [S3] | 2,056.41 | $3,994.15 | 0.5148 |

`margin_pct = |0.4902 − 0.5148| / 0.5148 × 100 = 4.79%`.

**How the margin was tuned to land inside SPEC §2's ~20% cap — four corrections, in order:**

1. The first draft used HUD Wind Zone III (110 mph) as the reinforced design speed, which produced a
   margin above 27% no matter how the pier footing was sized — too lopsided. Wind Zone II (100 mph) was
   substituted instead, still a real, distinct, regulated wind-zone tier one step up from Zone I.
2. The pier footing (MA3) was deliberately kept identical at both sites — grounded in the real design
   principle that telescope piers are oversized for vibration damping rather than sized to wind load —
   specifically because an earlier draft that scaled the footing base by the same 1.43× factor pushed
   the margin to nearly 27% on its own. With (1) and (2), the margin stood at 16.94%.
3. Tier 2 P6 data-decay verification (a live re-fetch of every cited source) found the steel price was
   originally sourced to heavy structural *plate*, the wrong product category for a dome's thin
   sheet-metal shell — corrected to a real, re-confirmed hot-rolled *coil* price, dropping the margin to
   12.78%. Independently, two fresh Tier 2 subagents (P1 cold-solve, P2 both-sides) both computed the
   footing's formwork cost using only its four lateral faces (a real footing's base needs no formwork
   against the excavation) rather than its full total surface area — adopted as the case's official
   model, raising the margin to 14.85%.
4. The same P6 verification pass then found the worst problem: Appendix B's original "70% clear (95%
   summer), 60% photometric" figures, attributed to a real paper (della Valle et al., MNRAS 2010), were
   never actually confirmed by reading that paper — a direct fetch found the real paper states 62.6%
   (ground-based) and 71.9% (satellite-based) instead, figures that do not match what an earlier draft
   had cited. Corrected to the verified 62.6% figure, which widened Vantage Mesa's real clear-sky
   advantage and narrowed the case's final margin to **4.79%** — a thin, gold-standard-adjacent margin
   (cf. the corpus's own Robotics Engineering case at 0.09%), reached only because every cited number was
   checked against a live, direct fetch rather than trusted from a search summary.

Full reasoning, every rejected draft, and the exact fetch-and-quote trail for the correction in step 4:
`RESEARCH_LOG.md`.

---

## Five Socratic questions

1. "Vantage Mesa has a real, published clear-sky advantage of about 23% over Sable Hollow. Why does
   Sable Hollow still win on the case's actual primary metric? What has to be true about the cost side
   for that to happen?"
2. "If you only compared total dollars — not dollars per usable hour — which site would look cheaper,
   and would that be a fair comparison? What's missing from 'cheaper' alone?"
3. "Your D2/D3 tables show Vantage Mesa's steel volume is about 43% higher than Sable Hollow's, but its
   total construction cost is only about 29% higher. Why don't those two percentages match? (Look at
   what else is in the cost total besides steel.)"
4. "Appendix D's reinforcement factor came from HUD's Wind Zone I and Wind Zone II design speeds, not
   from a dome manufacturer. If a real dome-specific wind rating existed and required *even more* extra
   steel than this case assumes, would your recommendation change? What if it required less?"
5. "Appendix A and Appendix B don't report the exact same categories — one site's number is
   'Photometric + Clear,' the other's is just 'Clear.' Does that difference matter to your answer? How
   would you defend using these two numbers side by side anyway?"

## The trap

**The trap is treating "more clear-sky nights" as automatically the better answer, without normalizing
by the extra cost of the structure needed to survive at that site.** A learner who sees Vantage Mesa's
real, better astroclimate record will often recommend it immediately, the same instinct that makes
"the faster channel must move more water" or "the bigger dome must be the better deal" attractive traps
in other cases — a real quantity looks decisive in isolation and stops being decisive once it's divided
by what it costs. A student who reports a recommendation using only Appendix A/B's clear-sky
percentages, without ever completing D1–D4's construction-cost work, has fallen into the trap and should
be asked directly: "where in your work did you account for what it costs to capture that extra clear
sky?"

A second, quieter version of the trap: Appendix A and Appendix B report *differently defined* sky-clarity
categories (77% Photometric+Clear vs. 62.6% ground-based Clear) from two real but distinct monitoring
programs — and Sable Hollow's own real study reports two OTHER figures (71.9%, 70.8%) that would each
tell a different story if used instead. A
learner who notices this and refuses to compare the two numbers at all is being appropriately careful —
but a learner who never notices it, and treats the two percentages as perfectly equivalent without
comment, has missed a genuine data-literacy point the case is quietly testing.

## Twist

**The consortium's insurer requires every site in the program to carry the same minimum wind rating,
regardless of local exposure — Sable Hollow must now also be built to the reinforced (100 mph) spec.**
This is a real kind of constraint (insurers and lenders commonly impose blanket code minimums across a
portfolio of sites rather than site-by-site engineering judgment) and it does exactly what a twist
should: it invalidates the "Sable Hollow wins because it's cheaper to build" position without making
Vantage Mesa's win obvious in turn, since Vantage Mesa's better clear sky still has to be checked against
the now-equal cost. Recomputed: with both sites paying the reinforced $5,159.99 construction cost, the
metric becomes hours-per-dollar with a shared denominator — Vantage Mesa's 2,529.45 usable hours/year
beats Sable Hollow's 2,056.41 outright, flipping the recommendation to **Vantage Mesa, by 18.70%**
(still inside the 20% cap, though barely).
Verified mechanically by `sensitivity_model.py`'s `evaluate_twist()`.

**Important for the guide (added after adversarial Tier 2 review, MCS-style P4 finding):** post-twist,
this flip rests entirely on Appendix G's MA5 — treating Vantage Mesa's 77% "Photometric + Clear" figure
as comparable to Sable Hollow's 62.6% "Clear" figure, even though the two real monitoring programs define
those categories slightly differently. Pre-twist, MA5 was a secondary consideration (the cost gap alone
decided the base case). Post-twist, with construction cost now identical at both sites, MA5 is the
*entire* basis for the flip. A sharp Hero who challenges MA5 directly ("you've shown me equal costs, but
you haven't shown me the two clear-sky percentages measure the same thing") is not quibbling — they are
attacking the twist's actual foundation, and the guide should treat that as a first-rate move, not a
distraction from the "real" discussion.

*"You now have 60 seconds. The insurer just told you both sites need the same wind rating. Are you
changing your recommendation — or not?"*

Follow-up: **"What just broke in your original model? Were you wrong, or just missing information?"**
(Answer: not wrong — the arithmetic was correct under the assumption that only one site needed
reinforcement. The twist changes an input, not the method.)

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. Show Appendix A and Appendix B's clear-sky percentages side by side, sites unlabeled. *"Thirty seconds — which site do you think wins, just from these two numbers?"* Stand/sit vote. No cost data shown yet. |
| **3:00–10:00** | Position defense. *"Convince us — not just that your site has better sky, but that it's worth what it costs to build there."* Press anyone arguing from clear-sky percentage alone: *"Where's your construction cost?"* |
| **10:00–15:00** | Pressure-test the models. *"Whose D2/D3 steel-volume numbers do you trust least? Did you use outer-minus-inner, or did you shortcut it?"* |
| **15:00** | **DROP THE TWIST** — the insurer's uniform wind-rating requirement. Deliver it slowly, with a pause before the 60-second clock starts. |
| 15:00–20:00 | Immediate recommit. Who reverses, and why? *"What just broke in your model?"* |
| 20:00–30:00 | Two threads: **(1) percent vs. dollar** — "a 23% clear-sky advantage and a 29% cost increase are both real numbers; why does dividing one by the other matter more than either alone, and why is the winner so close either way?"; **(2) comparable categories** — "Appendix A's 77% and Appendix B's 62.6% aren't measuring identically defined things, and Appendix B alone has three OTHER real figures to choose from (see Appendix G, MA5). Does that change how confident you are in the 4.79% margin — or in the Twist's flip, which depends on nothing else?" |
| **30:00–45:00** | Close, re-vote against the Anchor 1 board, reflection, lessons learned. |

---

## Guide Notes — the anchor ladder

### Intro
Heroes, today's case is a real engineering trade-off: better sky versus stronger, more expensive
construction — and the only way to settle it honestly is to compute a rate, not just compare two raw
numbers.

### Launch
Show the two sites' real clear-sky percentages (Appendix A/B) side by side, unlabeled by site name.
*"One of these places has genuinely better sky. The other one is cheaper to build on. Which one would
you put a telescope enclosure that costs somewhere between $3,994 and $5,160 on?"*

### Anchor 1 — Take a stand and vote
Vantage Mesa or Sable Hollow. No reasoning yet. Hands up, write the split on the board.
*"Is anyone courageous enough to stand with the site with the worse sky?"*

### Anchor 2 — What is the problem we're solving?
Do not let them calculate yet.
- What is the actual question? Is it "which site has better sky"? "Which site is cheaper to build on"?
  "Which site gives more usable observing time per dollar spent"? **Those are three different
  questions.**
- Someone will say "obviously the better-sky site wins." What do they mean by *better* — better sky in
  isolation, or better once you pay for what that sky costs to capture?
- Let the confusion grow. *"Wow. This is a genuinely hard question to even state precisely."*

### Anchor 3 — What is the process?
- If we just compare the two clear-sky percentages, are we done? (No — even with a real ~23% advantage,
  Vantage Mesa still loses on the case's actual rate, by construction cost alone.)
- Appendix A and Appendix B report differently-labeled sky categories. Does that matter to how we set up
  the comparison?
- Is our question still the right question?

### Anchor 4 — What don't we know?
- What's missing that we'd need to answer this properly? (Now answered by real data — but ask what
  Kwame still doesn't know: whether a real dome-specific wind rating would require more or less steel
  than this case's HUD-based stand-in assumes, whether the pier footing really should be identical at
  both sites.)
- Appendix D's reinforcement factor is a stated assumption built from real wind-zone speeds, not a
  sourced dome-manufacturer spec. Do you believe it? What would you need to see to trust it more?

## Data Deep Dive
Walk the room through D1's surface-area formula, D2/D3's outer-minus-inner volume subtraction for the
drum, windscreen, and dome cap, D4's pyramid surface-area and volume formulas for the footing, D5's
independent-event probability model, and D6's final compound-unit chain from nights to hours to dollars.
Ground truth for cross-checking a Hero's own work:

| Site | Construction cost | Usable hours/year | Usable hrs/$ |
|---|---|---|---|
| Vantage Mesa | $5,159.99 | 2,529.45 | 0.4902 |
| Sable Hollow | $3,994.15 | 2,056.41 | 0.5148 |

## Close
- Vote again. Who moved, and why?
- Was "which site has better sky" the right question, or was it really "which site gives more usable
  hours per dollar"?
- What math was new to you here — the outer-minus-inner volume subtraction, the independent-event
  probability model, or chaining the unit conversions at the end?

## Lessons Learned
The case's real lesson sits in the gap between a real, true, favorable-looking percentage (Vantage
Mesa's better clear sky) and what it actually costs to act on it. A student who only compares Appendix
A/B's percentages has answered a question the case never actually asked. The twist reinforces this from
the other direction: once the cost difference is regulated away, the percentage *is* the whole answer —
which is exactly why checking cost mattered in the first place.

## Standards Touched On

**New coverage:** none — see `case.json.reinforcement_note`. This case reinforces six Geometry/Surface
Area And Volume how-to skills from n=2 to n=3 (the group's entire remaining thin how-to set) plus
Independent Event from Statistics And Probability/Probability.

**Claimed:** How to find the surface area of a cylinder · How to find the volume of a cylinder · How to
find the volume of a cone · How to find the volume of a sphere · How to find the surface area of a
pyramid · How to find the volume of a pyramid · Independent Event · How to convert an amount with
compound units.

## Facilitator note — sensitivity

None required. This is a siting/capital-expenditure decision (which parcel to recommend to a university
consortium) with no death, illness, or family-hardship stakes — SPEC §6 does not apply.
