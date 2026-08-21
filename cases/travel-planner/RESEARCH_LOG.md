# Research Log — Travel Planner

2026-08-20. Six load-bearing placeholders (four theme-park ticket prices, two hotel nightly rates)
were researched directly during case-write/case-research (combined pass for this case, given the
task scope) rather than left as `{{NEEDS_SOURCE}}` for a separate stage. Every figure below is
cited in `case.json.sources[]` and reproduced with a `[S#]` marker in `case.md` Appendix C/D.

## P1 — Universal Studios Hollywood 1-Day ticket price (adult + child)

- Searched: "Universal Studios Hollywood ticket price 2026 1-day 2-day child adult official";
  attempted direct fetch of `universalstudioshollywood.com/web/en/us/tickets` (301-redirects to
  `store.universalstudioshollywood.com`, a JS-rendered payment app — fetched, returned only a
  "processing" placeholder, no price data).
- Also tried `store.universalstudioshollywood.com/PurchaseTickets.aspx` indirectly via search;
  same JS-store problem. Universal's own retail site does not expose a static, fetchable price.
- Fell back to aggregator tier: lajollamom.com (adult gate $159, reseller aRes Travel bundle
  pricing), thebettervacation.com (range only, no age split), and mickeyvisit.com (clean tiered
  table: Tier 1 adult $109 / child $103, Tier 7 adult $154 / child $148).
- **Used mickeyvisit.com's Tier 1 (lowest) figures: $109 adult / $103 child.** MEDIUM confidence —
  dynamic date-based pricing, secondary aggregator, but independently corroborated by two separate
  WebSearch syntheses converging on the same $109/$99–103 pair.
- **Also confirmed: Universal Studios Hollywood does not sell an official 3-day ticket product** —
  only 1-Day and "Buy a Day, Get a 2nd Day Free" (effectively 2 admission days for 1 price). This
  surfaced a real tension with the human-approved dilemma lock's framing ("3+ day pass, 6%
  discount tier") — resolved as Modeling Assumption MA2: 3 separate 1-Day tickets, purchased
  together, qualify for Gina's firm's own 6% tier (her tier is defined by cumulative admission
  days in her firm's deal with the park, not by which ticket SKU exists on Universal's own site).

## P2 — Disneyland 1-Day and 2-Day ticket price (adult + child)

- Searched: "Disneyland ticket price 2026 1-day 2-day child adult official"; direct fetch of
  `disneyland.disney.go.com/admission/tickets/` timed out.
- Fell back to mickeyvisit.com's tiered table (Tier 0 lowest: adult $104/child $98; 2-Day: adult
  $335/child $315), corroborated by a second WebSearch synthesis citing disneyparknerds.com and
  travelusaguide.com converging on the same figures.
- **Used the 2-Day, 1-Park adult/child prices ($335/$315) for Plan B.** MEDIUM confidence.

## P3 — San Diego Zoo 1-Day ticket price (adult + child)

- Direct fetch of `zoo.sandiegozoo.org/tickets` (official primary source) succeeded cleanly:
  Any-Day 1-Day pass $78 adult (12+) / $68 child (3-11); Value Days (select dates only) $73/$63.
- **Used the Any-Day price ($78/$68)** since Value Days eligibility for Jan 12-16, 2026 specifically
  was not confirmed. HIGH confidence — official primary source, directly fetched.

## P4 — LEGOLAND California 1-Day ticket price

- Direct fetch of `legoland.com/california/tickets-passes/tickets/` (official primary source)
  succeeded: gate price $139/person (ages 2+, no separate child tier), online starting price $69.
- Cross-checked with lajollamom.com's LEGOLAND discount guide, which also states a flat per-person
  rate with no age-based tier for ages 3+.
- **Used the $69 online starting price**, flat per person for all 5 paying family members. HIGH
  confidence — official primary source.

## P5 — Hotel near Universal Studios Hollywood (Plan A, "modest, farther from the park")

- Searched for a family suite near Universal, then pivoted to a realistic budget option once "near
  the park" priced at $254+/night (Tripadvisor aggregate) — Plan A's own design (Background,
  human-approved lock) calls for a hotel *farther* from the park to keep the budget balanced.
- Found the Hampton Inn & Suites Los Angeles/Burbank Airport, Burbank CA (~20 min drive from
  Universal, not walking distance) — a real, named, family-friendly property with a 2-queen room
  type. KAYAK: "rates start from $139," cheapest month (November) averages $179/night.
- **Used $139/night.** MEDIUM confidence — aggregated live rate, not a routed date-specific quote
  for Jan 12-16, 2026 exactly, but a real starting rate for a real, named property.

## P6 — Hotel near Disneyland (Plan B, "divided executive suite near the park")

- Background's own family-preference data (Appendix A) specifies a divided suite: separate
  sleeping space for James/Elizabeth/Henrietta vs. the three older children. Searched and found
  two real Good Neighbor / Anaheim-area candidates with two-room suite configurations: Anaheim
  Marriott Suites (371 two-room suites, separate living area and bedroom) and Anaheim Resort
  Suites. Direct fetches of Disney's own Good Neighbor rates pages both timed out (dynamic booking
  widgets).
- Fell back to KAYAK's listing for Anaheim Marriott Suites: standard/king rooms from $102/night,
  up to $210/night for higher room types (the page did not label a room type "executive suite"
  explicitly, but the property's own two-room-suite structure matches Background's requirement).
- **Used $210/night — the top of the observed range**, since Plan B specifically needs the
  two-room divided suite, not the cheaper standard room. Disclosed as Modeling Assumption MA4, and
  flagged as the case's single largest, most sensitivity-relevant assumption (see
  `case.json.sensitivity_disclosure[]` — a -50% flex on this one figure flips which plan is
  cheaper; no other input in the case does).

## Rejected / not used

- Universal Studios Hollywood gate prices ($153-$169 depending on source) — real, but the case
  uses the lower online-advance-purchase price consistently for all four destinations (Zoo and
  LEGOLAND's official sites both quote online-advance prices too), so gate prices would mix
  inconsistent purchase channels across destinations.
- San Diego Zoo "Value Days" pricing ($73/$63) — real and cited on the official site, but requires
  a specific eligible calendar date not confirmed for the Betteridges' actual travel week; using it
  would imply a level of date-specific precision the case cannot actually verify.
- LEGOLAND's "$39 kids ticket with 2-day Hopper + hotel room" bundle promotion — real, but tied to
  a 2-day resort package this case's 1-day LEGOLAND deliverable does not use, and the promotion's
  own stated end date (September 28, 2026) falls before the family's January 2026 travel dates in
  some read of the source — excluded to avoid a stale/conditional figure.
- Gas costs, food costs, and travel snack costs — named in the original source docx's own
  open-ended Challenge 3, but not part of the human-approved dilemma lock's "data to use" list, and
  no real Boulder-CO-to-Southern-California driving distance or food-cost data was found or
  computable without inventing a number. Dropped per SPEC §5 (never fabricate) — see
  `case.json.legacy_conversion_note`.

## Verification

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources: []
```

Next step: run Tier 1 structural gate (`skills/case-readiness/scripts/tier1_structural.py`).
