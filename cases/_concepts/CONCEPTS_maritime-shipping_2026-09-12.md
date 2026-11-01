# Concept sheet — Shipping, Ports & Global Trade (`maritime-shipping`)

**Target and why.** `readmodel/domains.json`'s `maritime-shipping` entry is HIGH authoring priority /
HIGH data grade with only **one** existing case (`Navigation`) touching the domain — the brief's
named target. Cross-checked live against `readmodel/standards_spine.json` this session: every one
of the domain's 12 `signature_skills[]` is confirmed present in the spine, but the entry's own
`uncovered_signature_skills: ["number-sense-depth"]` undercounts what's actually thin — 8 of the 12
signature skills sit above `n=2` and are not gap material at all (`measurement-currency` n=26,
`measurement-how-to-find-elapsed-time` n=12, `measurement-how-to-convert-an-amount-with-compound-units`
n=18, `geometry-how-to-graph-a-coordinate-pair-on-the-coordinate-plane` n=7, `geometry-coordinate-plane`
n=6, `discrete-mathematics-*` graph-theory skills n=4-5 each). Only `number-sense-depth` (n=2) is
genuinely thin among the signature list. So this brief does not chase the (stale) signature-skill
list; it goes to `readmodel/gap_queue.json` directly and scores against the corpus-wide **n<=2
thin convention** confirmed this session (zero true zero-coverage skills exist anywhere in the
437-skill spine — verified independently, matching the sweep the brief cited).

The four concepts below target four different *actually*-thin spine groups that a shipping
scenario can genuinely force: Discrete Mathematics/Set Theory (8/8 thin — full group), Number
Sense/Measurement And Data (1/10 thin, closeable outright), Statistics And Probability/Probability
(4/15 thin, all 4 closeable together), and Geometry/Surface Area And Volume (6/10 thin, partial).

**Live spot-checks performed this session** (per the brief's instruction not to grade HIGH on an
unchecked source): Suez Canal Authority (`suezcanal.gov.eg`) — **LIVE**, confirmed to publish a
"Tolls Calculator," a "Tolls Table," and rebate policy pages; Panama Canal Authority (`pancanal.com`)
— **LIVE**, confirmed "Tarifas Marítimas" / "Peajes Aprobados 2025" tariff pages; UNCTADstat — **LIVE**,
confirmed "Merchant fleet," "Freight volume, by sea," and "Liner shipping connectivity" indicator
sections; U.S. EIA petroleum spot-price series — **LIVE**, confirmed free, downloadable historical
fuel-oil spot prices. Two sources I attempted and could **not** confirm this session: Port of Los
Angeles container statistics (`portoflosangeles.org`, HTTP 403 on two paths — bot-blocked, not
necessarily down) and Ship & Bunker (`shipandbunker.com/prices`, HTTP 403). Neither is used as the
sole named source below; where a concept leans on one, I say so and name a live-confirmed fallback.

| # | Concept | Score | Tier | Group closed |
|---|---|---|---|---|
| C1 | The Manifest Split | **4.56** | T2 | Discrete Mathematics / Set Theory (8/8, full group) |
| C2 | The Draft Line | **2.6** | T3 | Number Sense / Measurement And Data (1/1 remaining thin) |
| C3 | The Reefer Plug | **1.3** | T3 | Statistics And Probability / Probability (4/4 remaining thin) |
| C4 | The Bunker Call | **1.2** | T2 | Geometry / Surface Area And Volume (2/6 remaining thin, partial) |

**Recommendation.** Write **C1, The Manifest Split** first — it is the only concept that closes a
*fully*-thin spine group outright (all 8 Set Theory skills sit at n=2), the customs/manifest framing
is a natural, non-forced fit for union/intersection/Venn-diagram reasoning (which containers need
*both* hazmat *and* reefer handling is a real operational question, not a wrapper), and it is the
domain's highest scorer even at MEDIUM feasibility. Write **C2, The Draft Line** second, not
instead — it is small (raw 0.6 before bonus) but it closes the one signature skill `domains.json`
itself flagged as uncovered, it sits on the best-confirmed live source of the four (Suez Canal
Authority, confirmed live with an actual toll calculator and depth/draft transit rules), and it is
the domain's headline decision archetype (Suez vs. the Cape) told honestly rather than inflated —
earlier drafting attempts to force coordinate-plane or trig skills onto this same archetype scored
zero genuine new coverage and are not included here as a result. **C3** is a legitimate third pick
but its feasibility is LOW, not MEDIUM: the probability of a container needing re-handling or dual
inspection is internal terminal-operations data I could not name a public source for; it would
lean heavily on stated Modeling Assumptions. **Kill C4** for this round relative to the other three
— it only partially closes its group (2 of 6 remaining thin skills), and while the EIA fuel-price
fallback is confirmed live, it's a proxy (heating-oil spot price, not marine bunker fuel), which
keeps it at MEDIUM rather than HIGH.

---

### C1 — The Manifest Split   ·   score 4.56   ·   tier T2

**Protagonist.** Marcus Feld, a customs and logistics coordinator at a container terminal, who signs
off on which containers get flagged for dual inspection before the ship's cutoff.

**The dilemma.** A.) Route every flagged container through the terminal's single combined
hazmat-and-reefer inspection lane — fewer lane changes, but the lane's throughput caps out fast when
both categories back up at once OR B.) Split hazmat and reefer containers into two separate lanes —
higher combined throughput, but any container that is *both* hazmat and refrigerated has to be
physically moved between lanes, adding a re-handle.

**Primary metric.** Containers cleared per inspector-hour (a ratio, not a total container count —
a lane that clears more containers isn't better if it needs proportionally more inspectors to do it).

**Why it's close.** Plan A's single lane never re-handles a container, but its combined queue means
every hazmat delay also slows reefer clearance (and vice versa) — the union of the two categories
all competes for one lane. Plan B's two lanes clear the disjoint parts of each set faster, but the
intersection (containers that are both hazmat and reefer) pays a re-handling cost that Plan A never
incurs. Which plan wins turns on how large that intersection actually is relative to the two sets —
exactly a Venn-diagram question, not a guess.

**Would close (8 skills, 2 how-to / 6 term, all currently n=2, all of Discrete Mathematics/Set Theory):**

| id | kind | label | n |
|---|---|---|---|
| discrete-mathematics-set | term | Set | 2 |
| discrete-mathematics-subset | term | Subset | 2 |
| discrete-mathematics-union | term | Union | 2 |
| discrete-mathematics-intersection | term | Intersection | 2 |
| discrete-mathematics-empty-set | term | Empty Set | 2 |
| discrete-mathematics-venn-diagram | term | Venn Diagram | 2 |
| discrete-mathematics-how-to-find-the-union-and-intersection-of-two-sets | how-to | How to find the union and intersection of two sets | 2 |
| discrete-mathematics-how-to-represent-a-set-relationship-using-a-venn-diagram | how-to | How to represent a set relationship using a Venn diagram | 2 |

**Already-covered skills it also exercises.** `number-sense-data` (n=33); `statistics-and-probability-how-to-create-a-bar-graph-given-a-set-of-data`-style
displays of per-lane throughput are plausible but not scored here since they're not forced.

**Data feasibility: MEDIUM.** I did not attempt a live check of a specific manifest-classification
document this session (per the brief's "don't web-search unless confirming a named source" norm
applied honestly — I have no single named document to check). The category is real and public: the
IMO's IMDG Code defines the hazmat classification categories a manifest actually uses, and U.S.
Harmonized Tariff Schedule categories similarly exist; both are the kind of standing government/IMO
classification lists case-research usually can find. Not confident about: a real, public dataset
giving the actual *count* of containers in each category and their overlap for any one sailing —
that will almost certainly be a disclosed, stated scenario (a manifest built to represent realistic
proportions), not a sourced figure.

**Sensitivity (SPEC §6).** None required — an operations/compliance decision, no personal stakes.

**Split risk.** None — 8 skills, one coherent deliverable arc (classify → Venn diagram → compare
lane throughput).

---

### C2 — The Draft Line   ·   score 2.6   ·   tier T3

**Protagonist.** Aisha Rahman, a route planner for a container line, who has to commit a laden
vessel's routing before the next voyage's stowage plan is finalized.

**The dilemma.** A.) Route the vessel through the Suez Canal, paying the toll and accepting the
canal's charted maximum-draft restriction — which means offloading some cargo at the load port to
get under it OR B.) Route around the Cape of Good Hope, carrying the full load as planned but adding
the extra sailing days. (This is `domains.json` maritime-shipping's own decision archetype #1,
made concrete: "Route Asia–Europe via Suez with the toll and the risk surcharge, or around the Cape
at 11 extra days.")

**Primary metric.** Net revenue per TEU actually carried (dollars saved on time and fuel by taking
Suez, minus the toll, divided across whatever TEU count the draft restriction allows — vs. the full
TEU count on the longer Cape route). A ratio, because "which route is cheaper" alone ignores that
Suez may force carrying less cargo.

**Why it's close.** The Suez transit is shorter and the toll is a known, published cost — but if the
laden vessel's draft exceeds the canal's charted depth limit, some cargo has to come off first,
which is a real capacity loss, not just an inconvenience. The Cape route carries everything but costs
eleven extra sailing days of fuel, crew, and schedule risk. Whether trimming cargo to clear the
canal beats carrying it all the long way around is genuinely not obvious until both are priced per
TEU actually delivered.

**Would close (1 skill, term, n=2 — the sole remaining thin skill in Number Sense/Measurement And
Data, and the exact signature skill `domains.json` itself flags as uncovered):**

| id | kind | label | n | group closed |
|---|---|---|---|---|
| number-sense-depth | term | Depth | 2 | Number Sense / Measurement And Data — 1/1 remaining thin skill |

**Already-covered skills it also exercises.** `measurement-currency` (n=26, toll payment and revenue
figures); `measurement-how-to-find-elapsed-time` (n=12, the 11 extra Cape days vs. Suez transit time);
`measurement-how-to-convert-an-amount-with-compound-units` (n=18, tonnage/toll-unit conversions);
`number-sense-distance` (n=13). None of these score — they were checked and none sit at n<=2 — which
is why this concept's raw score before the group bonus is honestly small (0.6): an earlier version of
this same archetype, built around coordinate-plane plotting of the two routes, was dropped because it
could not honestly force any thin coordinate-plane skill and would have scored zero.

**Data feasibility: HIGH.** Named sources confirmed live this session:
- Suez Canal Authority (`https://www.suezcanal.gov.eg/`) — confirmed live; publishes a Tolls
  Calculator, a Tolls Table ("the basis for calculating Suez Canal normal tolls"), and navigation
  rules pages that state transit draft/depth restrictions.
- Panama Canal Authority (`https://pancanal.com/`) — confirmed live with published tariffs, useful
  as a cross-check on how canal toll schedules are structured even though this concept uses Suez.

Not confident about: a real named vessel's exact laden draft and the current-cycle depth
restriction number for a specific Suez segment — `case-research` should build this around a stated,
disclosed vessel-class draft (as `domains.json` itself already recommends for this domain: "build the
case on published port stats plus a stated vessel spec rather than a real voyage") rather than a real
named ship's AIS-derived draft, which is commercial data.

**Sensitivity (SPEC §6).** None required — a commercial routing decision.

**Split risk.** None — small and single-arc, though authors should resist the temptation to bolt on
unrelated skills just to raise the count (see the dropped coordinate-plane version above).

---

### C3 — The Reefer Plug   ·   score 1.3   ·   tier T3

**Protagonist.** Renee Osei, a port terminal planner, deciding how to allocate a limited number of
refrigerated (reefer) power plugs among more containers than there are plugs, on a yard where any
unplugged reefer container risks spoilage.

**The dilemma.** A.) Assign plugs by strict arrival order (first-in-first-served) — fast to
administer, but the assignment is effectively random with respect to which containers most need
early power OR B.) Run a priority draw restricted to the subset of containers already flagged
temperature-critical — fairer to that subset, but requires computing how many valid priority
orderings exist before terminal ops will approve deviating from the simple first-in rule.

**Primary metric.** Expected number of containers held above safe temperature per shift (a rate,
not a total, since the count of reefer containers varies shift to shift).

**Why it's close.** Plan A is administratively simple, but treating plug assignment as one big pool
means whether a temperature-critical container gets an early plug is an independent event no more
likely than any other container's — the case has to show this with actual independent-event
reasoning, not just assert unfairness. Plan B's priority draw requires counting how many ways the
limited plugs can be assigned among the priority subset (permutations, since plug order/timing
matters) versus how many ways the full pool could be arranged (combinations, when only *which*
containers get a plug matters, not the order) — the comparison is a genuine counting problem, not
decoration.

**Would close (4 skills, 2 how-to / 2 term, all currently n=2 — every remaining thin skill in
Statistics And Probability/Probability):**

| id | kind | label | n | group closed |
|---|---|---|---|---|
| statistics-and-probability-independent-event | term | Independent Event | 2 | part of Probability — 4/4 remaining thin skills |
| statistics-and-probability-permutation | term | Permutation | 2 | part of Probability — 4/4 remaining thin skills |
| statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation | how-to | How to determine the number of outcomes of a permutation | 2 | part of Probability — 4/4 remaining thin skills |
| statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination | how-to | How to determine the number of outcomes of a combination | 2 | part of Probability — 4/4 remaining thin skills |

**Already-covered skills it also exercises.** `statistics-and-probability-combination` (n=4);
`statistics-and-probability-probability` / `outcome` / `event` (n=17/14/14).

**Data feasibility: LOW.** I could not name a specific public source for the actual rate at which
reefer containers miss timely power hookup, or for real plug-count-to-container-count ratios at a
named terminal — this is internal terminal operations data. The scenario numbers (plug count,
container count, temperature-critical fraction) would almost entirely be disclosed Modeling
Assumptions, not sourced figures, which is exactly the LOW grade's definition, not a MEDIUM I can't
back up.

**Sensitivity (SPEC §6).** None required — an operations decision.

**Split risk.** None — 4 scored skills, one deliverable arc.

---

### C4 — The Bunker Call   ·   score 1.2   ·   tier T2

**Protagonist.** Dev Kapoor, a fleet operations manager for a container line, deciding how a vessel
should be refueled before its next leg.

**The dilemma.** A.) Slow-steam at 16 knots — burns less fuel overall, so the vessel's existing
cylindrical bunker (fuel) tanks hold enough for the whole leg without a top-up call OR B.) Hold 21
knots to keep the scheduled berth window — burns enough more fuel that the vessel must call at an
intermediate port to top off the bunker tanks, and the tanks' remaining capacity (after whatever
fuel is already aboard) has to actually hold what's needed. (This is `domains.json` maritime-
shipping's own decision archetype #2: "Slow-steam at 16 knots to cut fuel or hold 21 knots to keep
the berth window.")

**Primary metric.** Total voyage cost (fuel + port/berth-window penalty) per day saved versus the
slower option — a ratio, since burning more fuel to arrive faster is only worth it per unit of
schedule value actually protected.

**Why it's close.** Slow-steaming is cheaper on fuel and needs no extra port call, but risks missing
the berth window and whatever contractual penalty that carries. Fast-steaming protects the berth
window but the tank math has to actually check whether the remaining ullage (empty space) in the
ship's cylindrical wing tanks can physically hold the extra bunker fuel a top-up call would add —
a real volume/surface-area constraint, not just a cost comparison.

**Would close (2 skills, both how-to, both currently n=2 — a partial cut of Geometry/Surface Area
And Volume's 6 remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| geometry-how-to-find-the-surface-area-of-a-cylinder | how-to | How to find the surface area of a cylinder | 2 |
| geometry-how-to-find-the-volume-of-a-cylinder | how-to | How to find the volume of a cylinder | 2 |

**Already-covered skills it also exercises.** `geometry-volume` (n=5); `geometry-surface-area` (n=8);
`measurement-how-to-convert-an-amount-with-compound-units` (n=18, fuel units to tank-volume units).

**Data feasibility: MEDIUM.** Ship & Bunker (`shipandbunker.com/prices`), the obvious named source
for real marine bunker fuel prices, returned HTTP 403 when I tried to confirm it live this session
— not confirmed, so not used as the sole basis for a HIGH grade. Confirmed live instead: the U.S.
EIA petroleum spot-price series (`https://www.eia.gov/dnav/pet/pet_pri_spt_s1_d.htm`) — free,
downloadable historical fuel-oil spot prices — but this is heating-oil/distillate pricing, a proxy
for marine bunker fuel, not the real VLSFO/IFO380 index, so it can only support a disclosed proxy,
not a claimed real bunker price. Not confident about: real cylindrical bunker-tank dimensions for a
named vessel class — a stated, disclosed spec (as with C2) is the honest path.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None — 2 scored skills plus reinforcement, small and single-arc.
