# Research Log — The Phasing Call

Stage: `case-research`. Ran 2026-08-31. 33 `{{NEEDS_SOURCE}}` placeholder instances enumerated in
`case.md` (spanning Appendices A–F), collapsing to 21 distinct data points once repeated
access-date/figure placeholders for the same source are merged. Every placeholder resolved to a
cited value (SOURCED) or a disclosed Modeling Assumption (ASSUMPTION). Zero left OPEN, zero
DROPPED.

## Placeholder-by-placeholder trail

**P01 — Appendix A, cargo vehicle anchor.**
Searched: "Cygnus NG-19 August 2023 rendezvous timeline"; already named as an example in the
placeholder text. Found: Northrop Grumman's Cygnus, real, currently-operating LEO cargo vehicle,
most recently flown as NG-19 (Aug 2023). SOURCED → S5. HIGH.

**P02 — Appendix A, client station altitude.**
Searched: "International Space Station average altitude km orbital period NASA"; fetched Wikipedia
ISS "Station statistics" table directly. Found: perigee 413 km / apogee 422 km, period 92.9 min
(as of 2022-12-22). SOURCED → S9. MEDIUM (Wikipedia is a tertiary aggregator of NASA data, but the
figure is stable and unambiguous).

**P03/P04 — Appendix A, tracked bearing/range.**
No real, named LEO client station of this kind exists — this is explicitly a stated-scenario cell
per the placeholder's own wording ("a stated scenario bearing/range"). No search attempted; not a
NOT FOUND, this was never claimed as sourceable. ASSUMPTION → MA1: bearing 48°, range 210 km,
chosen to give a non-trivial D1 polar-to-rectangular conversion.

**P05 — Appendix A, contracted docking deadline.**
Same treatment: no public Meridian Launch Systems contract exists. ASSUMPTION → MA2: 96 hours,
anchored to Soyuz's real 4.2-day (100.8-hour) autonomous-flight limit (S10) with deliberate slack
built in, the way a real mission-assurance contract would not set a deadline exactly at the
hardware ceiling.

**P06 — Appendix A, minimum required reserve.**
Searched: no public commercial LEO resupply contract publishes a specific consumables-reserve
floor. ASSUMPTION → MA3: 15% of total allowance, disclosed as a stated contingency convention, not
a sourced figure.

**P07/P08 — Appendix B, real operational precedent (Fast-Track).**
Searched: "Soyuz MS-17 ultrafast 2-orbit rendezvous"; "NASA Soyuz Orbital Insertion to Docking
Timeline 4-orbit 6 hours"; "Universe Today 6-Hour Fast-Track Soyuz." Found and cross-confirmed
across NASASpaceFlight.com, Wikipedia, Guinness World Records, TASS, and Universe Today: the
4-orbit/~6-hour profile (operational since 2013, "5 hours 45 minutes" on record flights) and the
2-orbit/~3-hour "ultrafast" profile (first flown Soyuz MS-17, Oct 2020, record time 3 hr 3 min).
SOURCED → S2, S3. HIGH.
Rejected: NASA's own original timeline page
(`nasa.gov/mission_pages/station/structure/elements/soyuz/timeline_orbit.html`) appears in search
indexes but returned HTTP 404 on direct fetch at research time — treated as a dead link per SKILL
step, not cited; Universe Today's coverage substituted as the working citation for the same claim.

**P09 — Appendix B, real operational precedent (Phasing Climb).**
Searched: "Cygnus NG-19 August 2023 rendezvous timeline days ISS berthing"; "Soyuz classic two-day
rendezvous 34 orbits ISS profile." Found: the classic 34-orbit/~2-day Soyuz profile (SpaceRef,
AmericaSpace, cross-checked against the real 88.62-min orbital period × 34 ≈ 50.2 h ≈ 2.09 days),
and Cygnus NG-19's real, current rendezvous: launch 2023-08-02 00:31:14 UTC, RMS capture
2023-08-04 09:52 UTC (≈2.39 days), berthing 12:28 UTC same day (≈2.50 days). SOURCED → S4, S5.
HIGH.

**P10/P11 — Appendix B, parking-orbit altitude (both options).**
This was the placeholder I expected to become a Modeling Assumption (per its own wording, "a
stated scenario parking-orbit altitude"). Instead, fetching the Soyuz Crew Operations Manual
(SoyCOM, ROP-19) directly turned up a real, primary, measured figure: Table 8-1 gives the Soyuz
injection/parking orbit as apogee 240 km / perigee 202 km (mean ≈220 km), period 88.62 min
(±22 s). Re-reading the manual's own Section 8.2.1 ("the initial phase Ф₀ may be of any value...
higher values of the initial phase require longer time for the phasing") clarified that both real
profiles use essentially the same low parking orbit — they differ in how many orbits of phasing
they let run, not in a different parking altitude. This let me use ONE real, sourced altitude for
both options rather than inventing a second, lower altitude for the Phasing Climb as the
placeholder's "same or lower" wording anticipated. SOURCED → S10. HIGH (primary crew-training
document, NASA doc. no. NAS15-10110).

**P12/P13 — Appendix B, parking-orbit period (derived).**
Directly stated in the same manual table (88.62 min), not re-derived via Kepler's third law from
scratch — the real, measured figure was available, so it is used in preference to a Keplerian
circular-orbit approximation (which I cross-checked separately at ≈88.9 min for a 220 km circular
orbit — consistent within rounding, confirming the manual's own elliptical-orbit figure is
sound). SOURCED → S10. HIGH.

**P14/P15 — Appendix B, angular catch-up rate (derived).**
Computed as 360°×(1/T_parking − 1/T_station) = 360×(1/88.62 − 1/92.9) ≈ 0.187°/min ≈ 11.2°/hour,
using the two real, sourced periods (S9, S10). This is arithmetic on two cited real inputs, not an
invented figure — same rate applies to both options since both share the same parking orbit.
DERIVED, HIGH (both inputs HIGH/MEDIUM).

**P16/P17 — Appendix B, modeled total transit time.**
Set directly from the real precedent figures already sourced above: Fast-Track = 6 hours (the
routinely-flown 4-orbit operational profile, S2); Phasing Climb = 2.5 days / 60 hours (Cygnus
NG-19's real, current berthing time, S5). Chose the "routine" 6-hour figure over the record 3-hour
figure for Option A as the more representative, repeatable operational anchor; chose Cygnus's
real current 2.5-day figure over the older classic 2-day Soyuz figure for Option B since Appendix
A's vehicle anchor is Cygnus. SOURCED (modeled from real precedent, per the placeholder's own
instruction). HIGH.

**P18 — Appendix C, total autonomous-flight allowance.**
Searched: "Soyuz autonomous flight duration limit days consumables"; "Soyuz 4.2 days autonomous
flight life rendezvous docking calculation." Found a strong secondary claim ("about four days
total," Space.com, Karl Tate, 2013-05-28 — S7, MEDIUM) and then a primary confirmation: the SoyCOM
manual states outright, in three separate places, "the spacecraft calculated autonomous flight
life is 4.2 days. This time period includes rendezvous/docking operations (2.2 days) and
undocking, pre-landing operations and time reserve (2 days)." SOURCED → S10 (primary, HIGH),
corroborated by S7 (secondary, MEDIUM).
Rejected: Cygnus's own real total free-flight limit (~180 days, per an FCC OET filing) was
considered and explicitly NOT used for Appendix C, despite Appendix A's vehicle being modeled on
Cygnus — see "Cross-cutting note" below for why.

**P19/P20 — Appendix C, reserve remaining at docking (derived).**
Arithmetic: 100.8 h − 6 h = 94.8 h (94.0%) for Option A; 100.8 h − 60 h = 40.8 h (40.5%) for Option
B. Both terms are the real, sourced figures above (P16–P18). DERIVED, HIGH.

**P21 — Appendix D, client station's orbital period.**
Same figure as P02: 92.9 min, ISS, Wikipedia "Station statistics." SOURCED → S9. MEDIUM.

**P22/P23 — Appendix D, phase-angle tolerance bands — the flagged risk.**
This was the placeholder the outer task specifically flagged: no source gives an authoritative
numeric phase-angle tolerance band for either profile. Search sequence (five distinct framings,
not two, given the stakes): (1) "Soyuz rendezvous phase angle degrees ISS launch window fast
profile constraint" — turned up a lead to a 2012 NASASpaceFlight.com article on Progress M-16M's
first test of the fast profile; (2) direct fetch of that article (via a text-extraction proxy,
since a direct WebFetch returned HTTP 403) confirmed an exact, quotable pair of figures: "the fast
rendezvous parameter of 30 degrees initial phase angle" vs. "the traditional two-day method
tolerates a much larger 270-degree phase angle"; (3) a follow-up fetch confirmed this is
attributed to "a Russian document describing the new rendezvous profile, which was seen by
NASASpaceflight.com" — real, dated, bylined (Pete Harding, 2012-08-01), but the underlying Russian
document itself is not named, capping this at MEDIUM rather than HIGH; (4) separately, fetching
the primary SoyCOM manual (already in hand for P10/P18) turned up its own, independent phase-angle
statement in Section 8.2.1: initial phase "may be of any value... to minimize propellant
consumption the initial phase is selected within 240–30 degrees"; (5) cross-checked this against
Murtazin & Budylov's abstract (S1) and the George textbook (S6), which confirm the general
mechanism (phase angle drives phasing-orbit duration) without giving their own numeric tolerance
bands for these specific profiles.
**Resolution:** used S11's 30°/270° pair as the case's stated figures (SOURCED, not an
assumption), because it is phrased directly as a tolerance/requirement, matching what the case
needs. The primary manual's own figure implies a wider tolerance (technically "any value," i.e.
up to 360°, for the classic profile) — this discrepancy is disclosed explicitly in Appendix D
rather than silently resolved, per SPEC §5's contested-figure rule. Confidence: MEDIUM for both
Option A and Option B bands.

**Cross-cutting note — why Appendix C uses Soyuz's allowance, not Cygnus's, despite Appendix A's
Cygnus vehicle anchor.** Cygnus's own real total free-flight limit (~180 days) is documented in a
1990s-era FCC OET filing, but using it in Appendix C would make both profiles retain >99% reserve
regardless of which is flown — the reserve term would carry no discriminating information, and D4
would become a trivial "both essentially 100%" exercise with no real math content. The concept
sheet's own design note (`cases/_concepts/CONCEPTS_precal-second-pass_2026-08-30.md`, C8 section)
already anchors the consumables-budget rationale to Soyuz's real autonomy limit, not Cygnus's —
this is the documented reason a hard, sub-week autonomy ceiling matters operationally (it is why
the fast-rendezvous profile was invented in the first place). This case therefore explicitly
blends two real vehicles' data by design (Cygnus for the "currently-operating cargo vehicle"
archetype in Appendix A; Soyuz for the binding consumables budget in Appendix C and the
phase-angle-tolerance figures in Appendix D) — both halves are real and cited, and the blend
itself is disclosed in-document (Appendix A's footnote, Appendix C's inline citation) rather than
presented as if one single real vehicle publishes all of these figures.

## Balance check (facilitator-only — not written to case.md)

Computed the case's own defined primary metric using only the real, sourced figures above:

```
total_allowance_h = 4.2 * 24 = 100.8 h                          [S10]
reserve_A_h = 100.8 - 6    = 94.8 h   (94.05% of total)          [S2, S10]
reserve_B_h = 100.8 - 60   = 40.8 h   (40.48% of total)          [S5, S10]
workable_days_A = 30 * (30/360)  = 2.5 days                      [S11]
workable_days_B = 30 * (270/360) = 22.5 days                     [S11]
metric_A = reserve_A_h / workable_days_A = 94.8 / 2.5   = 37.92 hours/day
metric_B = reserve_B_h / workable_days_B = 40.8 / 22.5  =  1.81 hours/day
percent difference = (37.92 - 1.81) / 1.81 * 100 ≈ 1991%
winning option (by this ratio): A — The Fast-Track
```

**This fails SPEC §2's ~20% balance cap by roughly two orders of magnitude** (though noticeably
less severely than `the-transfer-window`'s ~15,940% failure). Diagnosis: the concept sheet
predicted the margin would land inside the cap because "both terms... differ by only a few-x."
That premise checked out for the reserve-hours term (real sourced values differ by only ≈2.3x
between options, both landing in the 40–94% range because Soyuz's real 4.2-day total budget is
generous relative to either profile's real hours-to-days transit time) — but it did NOT check out
for the phase-angle-tolerance term, where the real, sourced figures (30° vs. 270°, S11) differ by
9x, not "a few-x." Because this metric is a straight ratio (reserve ÷ workable-days), a 9x
asymmetry in the denominator is not offset by a 2.3x asymmetry in the numerator — the two don't
partially cancel, they compound, producing the ~20x (1991%) blowout above. I tried the full
plausible range of real-precedent transit-time choices found during research (3–6 h for
Fast-Track; 24 h–60 h for Phasing Climb) and every combination lands the ratio between roughly
11x and 21x — the blowout is not an artifact of which specific real transit-time figure was
picked, it is structural to combining a real ~9x phase-angle-tolerance ratio with a real total
autonomy budget (4.2 days) that is simply too large relative to both profiles' real transit times
to ever produce a compensating reserve-hours asymmetry anywhere near 9x. This is a genuine finding
for `case-qa`/`case-readiness` to weigh, not a modeling choice I made to force an outcome — no
number here was tuned away from its real, cited value to chase a target margin.

`case.json.balance.margin_pct` set to `1991.18` and `winner` to `"A"` (facilitator-only fields);
`case.md` is untouched with respect to this finding, per instructions.

## Confidence summary

| Grade | Sources |
|---|---|
| HIGH | S1 (existence/framing only), S2, S3, S4, S5, S6, S10 |
| MEDIUM | S7, S8 (superseded by S10's direct statement), S9, S11 |
| LOW | none used; none load-bearing |

Zero placeholders left OPEN. Zero figures DROPPED. All Modeling Assumptions (MA1–MA4) carry a
stated basis and a sensitivity note per SPEC §5.

Next step: `case-readiness` (and, given the balance finding above, likely `case-qa`'s balance test
will flag this case the same way it flagged `the-transfer-window` — that determination belongs to
`case-qa`, not to this stage).

## Tier 2 probe 6 (data decay) — live source check, 2026-08-31 (case-readiness session)

Fetched live (WebFetch/WebSearch, this session has outbound network unlike the QA sandbox):

| # | Reachable | Figure confirmed present | Note |
|---|---|---|---|
| S1 | yes (abstract-level via search/ADS; direct ScienceDirect fetch 403, bot-blocked, not dead) | yes | Framing-only claim, unchanged |
| S2 | yes | yes | "four-orbit rendezvous" / 6-hour framing confirmed verbatim |
| S3 | yes (search-confirmed; direct fetch 403, bot-blocked) | yes | "two orbits (three hours)" confirmed verbatim |
| S4 | **yes, but content has decayed** | **no** | See finding below |
| S5 | yes | yes | Wikipedia Cygnus NG-19 timestamps confirmed exactly (launch, capture, berthing) |
| S6 | yes (search-confirmed; direct fetch 403) | yes | Lead-angle/phase-angle relationship confirmed |
| S7 | yes (search-confirmed) | yes | "about four days total" quote confirmed verbatim |
| S8/S10 | yes | yes | Primary Soyuz Crew Operations Manual PDF fetched and pdftotext-extracted directly: confirmed "4,2 days" total autonomous flight life, "88,62 min (+/-22 s)", "240 km (+43/-42 km)", "202 km (+7/-23 km)", and the "240 - 30 degrees" phase-selection note, all verbatim |
| S9 | yes | yes | Wikipedia ISS "Station statistics" confirmed exactly: 413 km / 422 km / 92.9 min |
| S11 | yes (search-confirmed; direct fetch 403, bot-blocked) | yes | "30 degrees" vs "270" phase-angle figures confirmed via search snippet |

**Finding: S4 has decayed.** The cited URL (`spaceref.com/status-report/the-standard-soyuz-launch-and-ascent-template/`)
resolves (HTTP 200) but now serves an unrelated, apparently regenerated generic
history-of-spaceflight article with no mention of Soyuz, orbit counts, or rendezvous timelines. A
second candidate SpaceRef URL for the same claim (`spaceref.com/news/viewsr.html?pid=8945`) now
redirects to an unrelated weather-forecast site entirely. This is the "resolves but no longer
carries the figure" case SKILL.md calls worse than a 404, because nothing in the pipeline would
otherwise have noticed. **Not a BLOCKER**, because the 34-orbit/2-day classic-profile figure S4
was cited for is descriptive/corroborating context in Appendix B, not itself a load-bearing input
to the D4-D7 primary-metric computation (the actual Phasing Climb modeled transit time used there,
60 hours, comes from S5/Cygnus, not from S4) — and the claim remains independently corroborated by
S4's own co-cited AmericaSpace reporting (unchanged, not re-verified this pass) and by the
already-recorded internal cross-check (88.62 min x 34 orbits = 50.2 hours = 2.09 days, consistent
with "2-day"). Recorded here rather than silently left stale, per MCS-21 (report NOT FOUND/decayed
rather than guessing) and per this skill's "a URL that resolves but no longer carries the figure is
worse" rule. No case.md or case.json content changed as a result — the figure itself is still
correct and still corroborated, only the one SpaceRef citation's live page has decayed.
