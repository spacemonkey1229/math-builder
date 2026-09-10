# RESEARCH_LOG.md — Pier Wheel

One row per figure needed. This case's `case-write` and `case-research` passes were run together
(same session, 2026-09-09) — every figure below started as a `{{NEEDS_SOURCE}}`-class need and was
resolved via live WebSearch/WebFetch before case.md was written to disk, rather than placeholder
-> fill in two passes. The searched/rejected trail is recorded here exactly as it happened.

## P01-P03 — Option A (Thames-side reference)

- Searched: "London Eye official height diameter rotation time specifications". Fetched
  `en.wikipedia.org/wiki/London_Eye` directly first (height 135 m, diameter 120 m, 32 capsules,
  25/capsule, ~800 total, 30 min rotation, £70M construction cost, opened 2000).
- Cross-checked against the operator's own site: fetched
  `londoneye.com/plan-your-visit/information-and-support/faqs/` — confirms height (135 m),
  capsule count (32), and rotation time (30 min) verbatim in the operator's own words. Promoted
  these three to S1/HIGH.
- Diameter and total capacity are not restated on the FAQ page. Kept as S2/MEDIUM (Wikipedia),
  cross-checked for internal consistency (25/capsule x 32 = 800, matches the "≈1,600
  passengers/hour" figure Wikipedia separately states: 800 x 2 rotations/hr = 1,600 — consistent).
- Ticket price: fetched `londoneye.com` homepage directly — "360° Views of London's Skyline from
  £29" confirmed in page heading and ticket section. S3/HIGH. Not load-bearing to the primary
  metric; included as appendix/background texture only, per the same convention other cases in
  this corpus use for over-complete data.
- Construction cost (£70M) was found but is **not used anywhere in this case** — the primary
  metric uses diameter, not cost, as its capital-scale proxy (see P07 below for why). Dropped as
  decorative to this case's actual math.

## P04-P06 — Option B (Las Vegas Strip reference)

- Searched: "High Roller Las Vegas official height diameter rotation minutes LINQ". Fetched
  `en.wikipedia.org/wiki/High_Roller_(Ferris_wheel)` (550 ft/167.6 m height, 520 ft/158.5 m
  diameter, 28 cabins, 40/cabin, 1,120 total, 30-min rotation, opened 2014).
- Attempted the operator's own page, `caesars.com/linq/things-to-do/attractions/high-roller` —
  the fetch returned only the page's `<title>` tag (JS-rendered content, not retrievable as
  static HTML by this tool). Could not promote to HIGH via the operator's own site; this is
  recorded as the reason S4/S5/S6 stay at MEDIUM rather than HIGH.
- Cross-checked via `onthestrip.com/on-the-strip/the-linq-high-roller/` — confirms diameter (520
  ft), 30-minute rotation, and 40-person cabin capacity independently of Wikipedia, though this
  same article contains an internal inconsistency (it states cabin count as both 28 and 32 in
  different places) — used only for the figures it corroborates against Wikipedia (diameter,
  rotation time, per-cabin capacity), not for cabin count, which is taken from Wikipedia's
  internally-consistent 28 alone. Promoted rotation time to S5/MEDIUM on this corroboration.
- Ticket price: searched "High Roller LINQ Las Vegas standard adult ticket price 2026 official".
  Official caesars.com page not fetchable (see above). Used `highroller-vegas.com`'s standard
  ticket page instead — "from $28" (daytime) / "from $40" (Anytime, evening-inclusive). Used the
  Anytime figure (relevant to a sunset-hour ticket) as S6/MEDIUM, explicitly flagged as a
  third-party reseller aggregator, not the operator's own price.

## P07 — Option B construction cost (rejected as load-bearing; excluded per SPEC section 5)

- Wikipedia and most press repeat "$550 million" for the High Roller's construction cost.
- Searched specifically: "High Roller Ferris wheel construction cost $550 million LINQ wheel only
  or entire project" to test whether this figure isolates the wheel or the surrounding
  development. Result: **the $550M figure is the entire LINQ retail/entertainment district**, not
  the wheel alone. A Las Vegas Review-Journal report (per search-result summary) puts the wheel's
  own share at roughly one-third of that ($183M); another figure found puts wheel-only
  construction cost at roughly $90M. These two wheel-only estimates disagree by roughly 2x with
  each other and neither is confirmed by a primary/official source in this research pass.
- **Decision: exit 3 (drop the figure) is not quite right here — the figure isn't decorative, a
  dollar-cost comparison is exactly what a capital review board would naturally reach for.
  Exit taken instead: redesign** (the worked-example pattern in `skills/case-research/SKILL.md`
  section "Worked example"). The case's primary metric was built around wheel **diameter** —
  which is not disputed by any source found — as the capital-scale proxy instead of a dollar
  figure, and Appendix B/F explicitly names the $550M figure and the dispute rather than quietly
  omitting it. This is the right move per SPEC.md section 5's own "50% of vaccines wasted"
  precedent: name a contested figure, don't smooth over it, and don't use any version of it.

## P08 — Qualifying sunset-view sightline height

- Searched for any real beach-town/boardwalk building-height ordinance to source a "clears the
  roofline" height, since Bellwether Point itself is necessarily fictional (no real site was
  named, so no real zoning record exists to fetch).
- **NOT FOUND** (expected — the site is fictional by design, matching this corpus's convention
  for a case built around a real product/market with a fictional operating company, e.g.
  `cases/feedback`'s fictional Ridgeline Playhouse and `cases/fermenter`'s fictional Riverbend
  Brewing).
- **Exit taken: stated Modeling Assumption (MA1)**, 250 ft (76.2 m), with basis and sensitivity
  disclosed in Appendix E and case.json.modeling_assumptions. Chosen to sit meaningfully above
  ordinary building heights and meaningfully below both options' maximum rider height, so the
  case is not decided by the assumption's placement alone.

## P09 — Boarding-platform height above ground

- No public figure exists for either reference installation's exact platform height above true
  ground datum (both are described qualitatively as "continuous loading at ground level" in
  available sources, without a precise clearance figure).
- **Exit taken: stated Modeling Assumption (MA2)**, 2 m, applied identically to both options, low
  sensitivity disclosed.

## Verification run

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: {'S7'}   # S7 is the excluded/contested-cost documentation row,
                                            # intentionally not cited with a [S7] marker in
                                            # case.md prose since its whole point is that it is
                                            # NOT used as a value; referenced by name in Appendix
                                            # B/F prose instead of a bracket marker.
LOW-confidence sources (must not be load-bearing): ['S7']   # by design -- S7 carries no figure
                                                              # used anywhere in this case's math.
```

**Next step:** `case-qa` on `pier-wheel` (not run by this session, per instructions).
