# RESEARCH_LOG — Pattern Rights

One row per placeholder enumerated from `case.md` at hand-off from `case-write` (11 tokens), plus
a note on a write-stage geometric error this research pass caught and corrected.

| # | Placeholder (abbreviated) | Searched | Found | Outcome |
|---|---|---|---|---|
| P01 | Citation confirming a half-drop's true tile is twice its visual step in some dimension | "half drop repeat pattern true repeat double height textile design"; then, after the first attempt returned nothing conclusive on *height*, "half drop repeat 'twice' OR 'double' the height tile canvas true repeat" | Multiple independent tutorials (Linda Matthews, Color on Cloth) describing the standard Photoshop/Illustrator construction method all resize the working canvas to **twice its width**, not its height, before applying the offset | **SOURCED — S5, and a write-stage correction.** The original `case-write` draft asserted the true tile was twice the *height* of the visual step, reasoning from "it takes two drops to realign a column." That reasoning is wrong: two drops realign a *single column's own* vertical position, but the *offset pattern across columns* (dropped/un-dropped/dropped/…) only repeats every second column — a horizontal periodicity, not a vertical one. Verified independently by hand: a half-drop lattice is a centered-rectangular lattice with basis vectors (w, h/2) and (0, h) for column width w and repeat height h; the smallest axis-aligned rectangular cell describing it is 2w × h (double width, same height), not w × 2h. Both `case.md` (Appendix A and Background) and `case.json` were corrected before publication of this research pass. |
| P02 | Total count of distinct wallpaper groups, for a supplemental (non-load-bearing) note | "17 wallpaper groups classification symmetry math"; "Federov 1891 proof 17 wallpaper groups crystallographic groups plane"; "Wolfram MathWorld wallpaper groups 17" | Wolfram MathWorld's own "Wallpaper Groups" article states plainly: "The wallpaper groups are the 17 possible plane symmetry groups," first established by Fedorov in 1891 | SOURCED — S4, HIGH confidence (a canonical, non-perishable mathematical reference). Used only as color in Appendix A; not load-bearing in any calculation, and the case says so explicitly. |
| P03 | Real printable fabric width for a home-décor/rotary-screen-printed fabric | "rotary screen printing fabric standard printable width inches home decor mill 2026"; ""54 inches" home decor fabric width mill specification rotary print" | Indigo & Luxe's decorator-fabric explainer states 54 inches is the US industry-standard decorator/home-décor fabric width, tracing the convention to historical carriage-width transport constraints; independently corroborated by multiple commercial home-décor fabric listings (Fabric Warehouse, Amazon/Waverly) all selling 54"-wide goods | SOURCED — S1, MEDIUM (design-industry explainer rather than a single mill's own spec sheet, but corroborated across several independent commercial listings — this project's Tier-3 standard). |
| P04 | Rated print run of a rotary printing screen/cylinder before replacement | "rotary print screen lifespan meters before replacement wear textile"; fetched hanzeltd.com's nickel-mesh-screen FAQ directly | HANZE INTL (a named rotary-screen manufacturer) states screens used with water-based printing paste last 30,000–50,000 meters of fabric before wear necessitates replacement | SOURCED — S3, HIGH (named manufacturer's own technical FAQ, clear figure and units, clearly stated ink-chemistry condition). This case adopts the conservative low end (30,000 m) rather than the midpoint or high end — see `case.json.modeling_assumptions` MA1 — because the source gives a range, not a scheme-specific figure, and no source distinguishes screen life by repeat type (straight-grid vs. offset). |
| P05 | One-time engraving/setup cost for The Straight Set | "rotary screen engraving cost per screen textile printing USD price"; fetched finetex.net's own published engraving price sheet directly | Fine Line Engraving publishes real per-screen prices by repeat size and color count (e.g. 27"/688mm repeat, single color: $410–$470) — but the page's own stated effective date is 2011-04-01, roughly 15 years stale as of this case, and the pricing structure does not distinguish a uniform straight-grid repeat from an offset half-drop repeat at the same repeat size | **NOT FOUND (no current, dated, scheme-specific figure), then ASSUMPTION.** Per SPEC §5's precedent for stale/unverifiable figures (the "50% of vaccines wasted" and this project's own prior "$70 password reset" exclusions), a 15-year-old price list is not treated as this case's current cost figure. Fine Line Engraving's real (if dated) price range is used only as an anchoring reference for a stated Modeling Assumption (MA2, $650.00), disclosed openly rather than presented as sourced. |
| P06 | One-time engraving/setup cost for The Half-Drop | (same search pass as P05) — additionally searched "rotary screen engraving offset half drop repeat cost premium registration" and "textile screen engraving price difference straight grid vs offset pattern"; no results distinguished pricing by offset type at all | No source anywhere breaks out engraving price by straight-grid vs. offset/half-drop registration complexity — every price list found (Fine Line Engraving and others surfaced in the P05 search) prices strictly by repeat *size* and color count, treating registration/offset complexity as invisible to the published price schedule | **NOT FOUND, as anticipated by the brainstorm sheet's own MEDIUM-feasibility grading.** ASSUMPTION — MA2, $750.00 (a stated $100/15% premium over The Straight Set), on the disclosed basis that an offset lattice requires tighter cross-column registration during engraving than a uniform grid — a plausible engineering claim consistent with how rotary-screen engraving works, but not itself a figure any source publishes. Flagged in `case.json.modeling_assumptions` MA2 as the case's single most load-bearing, least certain dial. |
| P07 | Appendix D stub (Modeling Assumptions) | n/a — resolved by P05/P06's NOT FOUND outcomes | — | Resolved into MA1 and MA2 rows in `case.md` Appendix D and `case.json.modeling_assumptions`. |
| P08 | Appendix E stub (Sources) | n/a — resolved as P01-P06 were sourced | — | Resolved into S1–S5 rows in `case.md` Appendix E and `case.json.sources`. |
| P09 | Facilitator-only Balance argument, Argument for A | n/a — drafted from D1/D4's now-computed figures | — | SOURCED (drafted); see `case.md` facilitator-only section and `case.json.balance.argument_a`. |
| P10 | Facilitator-only Balance argument, Argument for B | n/a — drafted from D1/D2's now-computed figures | — | SOURCED (drafted); see `case.md` facilitator-only section and `case.json.balance.argument_b`. |
| P11 | Facilitator-only Balance argument, margin_pct | n/a — computed from D4's figures once Appendix B/C landed | — | Computed: margin_pct = 13.3. See `case.json.balance` and `case.json.derived`. |

## A note on the write-stage correction — the actual finding of this research pass

The single most consequential result of this research session was not a sourced number — it was
catching and correcting a **geometric error made at `case-write` time**, before any research had
been done. The original draft asserted that a half-drop repeat's true, fully-tiling rectangular
unit is twice the *height* of its visual offset step, reasoning informally that "it takes two
drops to realign a column." That reasoning conflates two different periodicities: a single
column's own vertical realignment (which does take two drops, i.e. one full motif height — but
that is simply the motif's *existing* repeat height, not a doubling of it) with the *horizontal*
periodicity of the offset pattern across columns (dropped, un-dropped, dropped, …), which only
returns to its starting arrangement every second column.

Every real source found during research (independent surface-pattern-design tutorials describing
the standard construction method) doubles the working canvas's **width**, not height, before
applying a half-drop offset — confirmed independently by hand via the lattice basis vectors of a
centered-rectangular lattice. `case.md` (Background and Appendix A) and `case.json` were both
corrected to reflect this before this research pass concluded. The corrected geometry still
produces the same qualitative result the case's design depends on — The Half-Drop's true tile
holds double the floral elements of The Straight Set's — it is simply *why* that doubling happens
that changed. This is exactly the kind of error `case-research`'s sourcing discipline exists to
catch: a plausible-sounding claim that was never actually checked against a real, citable
description of the technique.

## Verification (case-research SKILL.md step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
INCOMPLETE sources: none
LOW-confidence sources: none
```

MEDIUM-confidence sources (S1, S2, S5) are not load-bearing on the case's dilemma-flipping
quantities except via `case.json.modeling_assumptions` MA1/MA2, which are themselves openly
disclosed assumptions rather than presented as sourced facts.
