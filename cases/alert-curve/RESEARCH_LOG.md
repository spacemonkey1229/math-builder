# RESEARCH_LOG — alert-curve

Stage: `case-research`. 31 `{{NEEDS_SOURCE}}` placeholders enumerated. 2 resolved with a real
cited source (SOURCED). 29 resolved as explicit Modeling Assumptions grouped into 6 MA entries
(MA1–MA6), because — after a genuine search attempt on each — the underlying quantities turned
out to be either (a) proprietary to specific vendors/SOCs and never published, or (b) inherently
narrative/scenario values with no real-world referent to source in the first place. Zero DROPPED.
Zero left OPEN.

---

## P01–P03 — Appendix A coefficients (p,q,r / k,m / c)

**Searched:** "quadratic traffic model SOC edge node coefficients", "SIEM detection engine
pattern-match count accumulation rate benchmark", "threat scoring square root transform
coefficient documentation", plus a direct check of the Verizon DBIR's public summary pages for
any published per-node traffic-volume model.

**Found:** Nothing. No SIEM/SOAR/detection-engine vendor (Splunk, Microsoft Sentinel, CrowdStrike,
Elastic, Chronicle) publishes the literal coefficients of an internal scoring-transform or a
per-node traffic-volume curve — this is proprietary detection-engine internals, not the kind of
thing any vendor discloses in a spec sheet or benchmark report.

**Outcome:** NOT FOUND → **Modeling Assumption MA1, MA2, MA3.** This was anticipated by
case-write's own Appendix E stub, which flagged the composite function's *form* as
assumption-bound. Values were picked to produce a numerically clean derivative story (V(t)
climbing through the hundreds-to-low-thousands requests/min, S(t) landing in a bounded 0–100-style
severity range) while keeping the scale plausible against the alert-volume research found for
MA6 (below).

## P04 — Threshold, raw alerts/hour

**Searched:** "SIEM SOAR default alert threshold escalation rule alerts per hour", "automated
escalation threshold financial services SOC benchmark", and read Microsoft's own Sentinel
"Scheduled analytics rules" documentation in full to check whether Sentinel ships a fixed default.

**Found:** Confirmed the opposite of a fixed default: Microsoft Sentinel's docs state the alert
threshold "applies separately to each time the rule runs" and is configured per rule by the SOC
that owns it — there is no platform-wide or industry-wide numeric default. Multiple secondary
sources on SIEM alert tuning confirm thresholds are environment-specific by design.

**Outcome:** NOT FOUND (confirmed no such published default exists) → **Modeling Assumption MA4.**
500 alerts/hour, chosen to sit inside the range of the constructed Appendix D log (410–710) so the
log has genuine mixed outcomes under the Threshold Trip rule. Flagged HIGH sensitivity — this is
the single most dilemma-flippable number in the case.

## P05 — Sampling interval length, minutes

**Searched:** "SIEM typical alert polling interval minutes", then went straight to a primary
vendor doc once general search returned only a loose range (1–15 min across various monitoring
contexts, not SOC-alert-specific).

**Found:** Microsoft Sentinel's own documentation states plainly: "The allowed range for both of
these parameters [query interval and lookback period] is from 5 minutes to 14 days" for a
scheduled analytics rule — 5 minutes is the fastest cadence a real, current, mainstream SIEM/SOAR
platform supports.

**Outcome:** **SOURCED — S1, HIGH confidence.** Primary vendor documentation, dated, unambiguous
units, exactly the quantity needed (a real platform's sampling interval floor).

## P06 — Current sampling instant t0

**Searched:** Nothing to search — this is explicitly a "scenario value," i.e., where in the
monitoring window Jordan is standing right now. No real-world quantity underlies it.

**Outcome:** NOT FOUND by construction → **Modeling Assumption MA5.** 42 minutes into the 60-minute
window (18 minutes / 3+ sampling intervals remain), chosen so "wait one more interval" is a live
option rather than time running out. Low sensitivity — it only changes D4's numeric tangent-line
prediction, not which policy the D5 ratio favors.

## P07 — Mean time to detect (MTTD), IBM Cost of a Data Breach Report

**Searched:** "IBM Cost of a Data Breach Report 2025/2026 mean time to identify MTTD days."
Confirmed IBM's 2026 edition (published 2026-07-29) is the current "most recent edition,"
superseding 2025's 241-day figure.

**Found:** IBM's own report page (ibm.com/reports/data-breach) returned HTTP 403 on direct fetch
— gated behind a JS wall / lead form. Fell back to a reputable secondary outlet (Help Net
Security) directly reporting IBM's named 2026 figure: mean time to identify **and** contain a
breach, global average, 247 days.

**Outcome:** **SOURCED — S2, MEDIUM confidence.** Two soft points, both noted: (1) tier-3 sourcing
(secondary outlet quoting the primary report, not the report itself, because of the 403), and
(2) this is a combined identify+contain metric used as a proxy for "detect" alone, since IBM's
2026 summary does not appear to break MTTI and MTTC out separately in any publicly reachable page.
Both caveats are recorded in the source's `note` field.

## P08–P31 — Appendix D historical escalation log (6 rows × 4 columns)

**Searched:** "Verizon DBIR share of security alerts that convert to confirmed incidents" (the
anchor case-write's own Appendix D stub named), in two framings, plus a direct look at Verizon's
DBIR landing/archive pages for any alert-triage-outcome statistic.

**Found:** No such statistic in the Verizon DBIR — it reports on confirmed breaches/incidents, not
on SOC alert-triage outcomes, so the originally proposed anchor doesn't exist in that report.
Found instead: a 2026 Omdia survey (commissioned by Microsoft, N=300 SOC practitioners) reporting
46% of SOC alerts are false positives and 42% go uninvestigated; and a 2026 Ponemon Institute
"State of SecOps Report" (commissioned by Crogl) reporting an average 4,330 alerts/day per
organization with only 37% investigated.

**Outcome:** NOT FOUND for the specific named anchor (Verizon DBIR alert-conversion stat) and NOT
FOUND in principle for the per-interval log entries themselves (no real institution's per-shift
SOC log is, or should be, public) → **redesigned the anchor** to S3/S4 above, which measure the
same underlying phenomenon (alert signal-to-noise) with real, dated, named-organization figures,
and recorded the whole 6-row table as **Modeling Assumption MA6.** The constructed log deliberately
includes: two clean true positives (rows 1, 3), two false escalations that Curve Check correctly
declines (rows 2, 4), one real incident the raw count under-threshold misses but the derivative
check catches (row 5), and one accelerating-but-ultimately-false alarm that fools both policies
(row 6) — so Challenge D5's ratio comparison has genuine signal in both directions, not a rigged
one-sided outcome. Flagged HIGH sensitivity, correctly: this table is the direct input to D5's
percentage-margin comparison, which FACILITATOR.md records as intentionally undetermined at
write time.

---

## Summary

| Placeholder(s) | Resolution | Confidence |
|---|---|---|
| P01 (p,q,r) | MA1 | — (assumption) |
| P02 (k,m) | MA2 | — (assumption) |
| P03 (c) | MA3 | — (assumption) |
| P04 (threshold) | MA4 | — (assumption) |
| P05 (sampling interval) | S1 | HIGH |
| P06 (t0) | MA5 | — (assumption) |
| P07 (MTTD) | S2 | MEDIUM |
| P08–P31 (Appendix D log, 24 cells) | MA6 | — (assumption) |

**NOT FOUND total: 29 of 31 placeholders**, all resolved via the **Modeling Assumption** exit
(grouped into 6 MA entries rather than 29 separate ones, since most share one basis/sensitivity
story). **Redesign exit** used once, informally, to replace the originally-proposed but
nonexistent Verizon DBIR alert-conversion anchor with S3/S4. **Drop** exit not used — every
placeholder is load-bearing to at least one Challenge (D1–D5) or to Appendix B/C's narrative
logic, so nothing was decorative enough to cut.

Next step: `Run case-qa on alert-curve.`
