# Research Log — Survey Corner

Sourced 2026-08-12, `case-research`.

## S1 — Real NGS survey monument ("D 565," PID QX0584)

**Claim:** A real, publicly published NGS control monument near Gardiner, Park County, Montana,
with published NAD 83 coordinates and NAVD 88 elevation.
**Source:** National Geodetic Survey (NOAA) Data Sheet, PID QX0584 —
https://www.ngs.noaa.gov/cgi-bin/ds_mark.prl?PidBox=QX0584
**Accessed:** 2026-08-12. **Confidence:** HIGH.

**Verification history.** First located via a 2018-dated archival copy of the same datasheet
(Montana State Library GIS mirror, `NGS_QX0584.pdf`), which gave NAD 83(1986) position
45°01'46.29"N, 110°42'30.03"W. Before finalizing the case, re-fetched the **live** NGS retrieval
page directly (same URL cited above) and found the currently-published coordinates have since
drifted slightly — 45°01'46.22"N, 110°42'30.10"W — consistent with a routine NGS position
readjustment between the 2018 archival snapshot and today; the elevation (5,318.45 ft NAVD 88) is
unchanged. **Corrected the case to the live, current value** rather than the 2018 archival value,
since the live page is the actual, present source of record and MCS-21/MCS-28 require the cited
figure to be what a student would actually find if they followed the link today.

**Note on this monument's role in the case.** PID QX0584 is real-world context only — it is
explicitly *not* the disputed parcel in this case (SEE Appendix A's own framing). It establishes
that the federal survey control network this domain is built on is real and independently
checkable (the same real-source-for-context convention as Apron Order's FreeSewing citation, Vent
Cap's ESICUP citation), and is Challenge 1's research target. The disputed parcel's own plat angle
(Appendix B), field readings (Appendix C), and witness-tie data (Appendix D) are Priya's own
authored field survey for this specific case — no public database of real property-line disputes'
raw field books exists (same convention as every prior case's domain-specific authored data:
Cold Chain's route, Plaza Pavers' border cut, Vent Cap's nesting result, Apron Order's marker
layout).

## Modeling assumptions (not sourced — see Appendix F)

- **MA1 — Northwest corner plat-recorded angle (93°).** A real, general concern about historic
  deed/plat recording and rounding uncertainty, not tied to this specific plat. Swept ±50% on the
  angle's 3° excess-past-square (not on the whole 93° angle — see FACILITATOR.md's sensitivity note
  for why a whole-angle ±50% sweep would be physically implausible) in Tier 2 probe 5: margin holds
  8.33%-16.67%, winner (Pin 2) does not flip.
- **MA2 — Pin 1/Pin 2 field readings, witness-tie triangle angles, and the distance-check figures
  (Appendix C/D).** Priya's own authored field survey for this dispute. Not FLEX-swept.

## Search methodology

Direct WebFetch verification against the live NGS datasheet retrieval page on 2026-08-12, same day
as authoring — page reachable, station designation and PID confirmed, elevation confirmed exactly,
coordinates confirmed and corrected to match the live value. No figure in this case is fabricated:
every number is either traced to S1, is Priya's own authored field/plat data (MA1, MA2, explicitly
disclosed with basis and sensitivity), or is arithmetic derived from those inputs (`case.json.derived`,
`sensitivity_model.py`).
