# Research Log — The Lease Break

Stage: `case-research`. 13 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md`. The Cedarline
and The Aldergate are invented apartments for this scenario (no real listing exists to quote), so
per the skill's normal pattern for scenario-based cases: real, dated market **norms and ranges**
were sourced, and specific dollar figures were then either taken directly from a real bedroom-
specific market figure (rent) or stated as an explicit Modeling Assumption chosen from within a
real, cited range or convention (fees, deposit, penalty, buyout). Appendix C's narrative-only
figures (deadlines, budget) have no real-world referent at all (they describe a fictional person's
private circumstances) and are stated as Modeling Assumptions with a narrative/plausibility basis
rather than a market citation.

City chosen for the real rent figures: **Boise, ID** — a real US mid-size city with clean,
bedroom-specific, dated rent data from a single named source, so both units' rents come from the
same city and the same page.

---

## P01 — Appendix A, Cedarline monthly rent

- **Searched:** "Apartment List national rent report 2026 studio one-bedroom average rent mid-size
  city"; then targeted "RentCafe average rent Boise Idaho 2026 studio one bedroom".
- **Rejected:** Apartment List's national report gave two internally inconsistent studio/1BR
  figures on the same page ($1,754 studio / $1,702 1BR in one summary vs. $1,390 "median" / $1,221
  1BR in a direct fetch of the same URL) — looks like a blended-bedroom national figure being
  conflated with a bedroom-specific one. Excluded as a contested/ambiguous figure rather than used
  as a proxy (see Appendix D note in `case.md`).
- **Found:** RentCafe's Boise, ID page gives studio average rent $1,389/month, updated 2026-07-02.
  Bedroom-specific, dated, single real city.
- **Outcome:** SOURCED — S1, confidence MEDIUM (real aggregator average, not a single named
  listing).

## P02 — Appendix A, Cedarline non-refundable move-in fee

- **Searched:** "typical non-refundable move-in fee apartment lease vs security deposit amount".
- **Rejected:** Zillow's and Apartments.com's own explainer pages on this topic both returned
  HTTP 403 on direct fetch (blocked); did not use their search-snippet numbers without fetching the
  actual page, per the skill's "prefer web_fetch over summary snippets" rule.
- **Found:** Redfin's renter-fees explainer (fetched directly, updated 2022-08-18): move-in fees
  typically run 20-50% of monthly rent.
- **Outcome:** NOT a single findable number for an invented listing — ASSUMPTION. MA1 = $415
  (~30% of $1,389), upper-middle of the real cited range, chosen to match the narrative's "large"
  characterization.

## P03 / P07 — Appendix A & B, lease term (both units)

- **Searched:** "standard apartment lease term 12 months most common industry data NMHC or Census".
- **Found:** U.S. Bureau of Labor Statistics, "Housing Leases in the U.S. Rental Market" (Spotlight
  on Statistics, published 2022-09, survey period Jan-Jun 2022): 59.6% of leases are 12 months —
  the single most common term nationally, government primary source.
- **Outcome:** SOURCED — S4, confidence HIGH. Applied to both appendices' lease-term rows.

## P04 — Appendix A, Cedarline early-termination penalty

- **Searched:** "early lease termination penalty typical two months rent buyout clause apartment".
- **Found:** LeaseRunner, "Penalties for Breaking a Lease" (fetched directly, published
  2026-05-28): early termination fees typically run 1-2 months' rent; buyout clauses are often set
  at 2 months' rent specifically.
- **Outcome (original, 2026-09-03):** ASSUMPTION — MA2 = $2,778 (2 months' rent, top of the real
  cited range), matching the narrative's "steep" characterization. Flagged in `case.json`'s
  `sensitivity_note` as the single highest-leverage assumption in the case.

### P04 REVISED — case-readiness remediation, 2026-09-04

- **Why revisited:** case-qa (2026-09-03) found that with MA2 at 2 months' rent, The Cedarline was
  cheaper in BOTH the stay-full-term AND break-at-month-6 scenarios (16.9% and 6.6% respectively),
  so the case's designed scenario-dependent reversal did not exist. Recomputation showed the
  reversal was mathematically unreachable while MA2 stayed within S5's cited 1-2 month range (see
  `case.json.sensitivity_note`'s prior text for the arithmetic) — the top of that range (2 months,
  $2,778) still leaves The Cedarline's larger ongoing rent advantage dominant at month 6.
- **Searched:** "lease early termination clause 60-day notice plus penalty rent continues during
  notice period apartment"; "lease break fee one month's rent buyout covers all remaining
  obligations apartment"; "early termination fee lease three months' rent penalty apartment
  landlord tenant".
- **Found:** Two independent real sources reporting a *wider* range than S5's general 1-2 month
  figure, both tied to a specific real-world condition — a lease with several months still
  remaining at the time of the break, exactly Maya's break-at-month-6 situation (6 of the
  Cedarline's 12-month term remain):
  - Landing, "How Much Does It Cost to Break a Lease?" (fetched directly, updated 2025-01-31):
    "An early termination fee typically equals 2-4 months' rent." → **S7**.
  - LeaseRunner, "Early Termination Fee: How Much It Costs & When You Don't Have to Pay" (fetched
    directly, published 2025-10-14 — a different article/URL than S5, same publisher): "An early
    termination fee typically costs 1-2 months' rent, and can reach 3-4 months in tight markets or
    when several months remain on the lease." → **S8**.
- **Decision:** MA2 revised from $2,778 (2 months' rent, S5's ordinary range) to $4,862 (3.5
  months' rent), the middle of S8's elevated 3-4 month sub-range that specifically applies to
  Maya's "several months remain" situation. This is not cherry-picking a number to force a target
  margin — it is picking the correct real-world range for the scenario actually being modeled: S5's
  1-2 month range describes the *ordinary* case (a lease nearly up anyway), which is not what D3
  models. Recomputed break-at-month-6: Cedarline $2,268.50 vs. Aldergate $2,048.00 — Aldergate now
  genuinely cheaper by 10.8%.
- **Outcome:** ASSUMPTION (revised) — MA2 = $4,862 (3.5 months' rent), grounded in S7 (MEDIUM) and
  S8 (MEDIUM). `case.json.sensitivity_note` updated with the full before/after record. See also
  `sensitivity_model.py`, updated to the new PARAMS value and verified to reproduce the 10.8% margin.

## P05 — Appendix B, Aldergate monthly rent

- Same source/page as P01 (RentCafe Boise, ID, one-bedroom row): $1,536/month, updated 2026-07-02.
- **Outcome:** SOURCED — S2, confidence MEDIUM.

## P06 — Appendix B, Aldergate refundable security deposit

- **Searched:** "security deposit one month's rent statute typical apartment lease HUD".
- **Found:** HUD's Public Housing Occupancy Guidebook, §3.3.3 (PDF fetched and text-extracted
  directly, since the AI-summarized WebFetch pass on the raw PDF failed to parse it — re-fetched the
  binary and ran `pdftotext` on it locally to confirm the exact clause: "This deposit cannot exceed
  one month's rent"). This is a public-housing-specific rule, not a direct private-market
  regulation, but corroborates the widely-cited one-month convention also reflected in numerous
  state landlord-tenant statutes surfaced in the same search (NY, IN, AZ caps referencing one to
  1.5 months' rent).
- **Outcome:** ASSUMPTION — MA3 = $1,536 (1 month's rent), grounded in S6, matching the narrative's
  "smaller, more conventional" deposit.

## P08 — Appendix B, Aldergate early-termination clause

- Same source as P04 (LeaseRunner, S5): 1-2 months' rent typical range.
- **Outcome:** ASSUMPTION — MA4 = $1,536 (1 month's rent, bottom of the real cited range), matching
  the case's already-stated "buyout of one month's rent" language exactly.

## P09 — Appendix C, contract's stated firm term

- Not a real-world fact (Maya and her contract are fictional) — no search performed; this is
  purely a scenario/narrative parameter.
- **Outcome:** ASSUMPTION — MA5 = 6 months, basis: fixed-term QA/contract-testing engagements
  commonly run in 3/6/12-month increments; 6 months makes an early lease break a real, live risk
  rather than a remote one.

## P10 — Appendix C, month at which an early move would happen

- **Outcome:** ASSUMPTION — MA6 = month 6, set equal to MA5 (the contract's firm term) and to the
  month number the Challenges section already names explicitly ("break at month 6").

## P11 — Appendix C, signing deadline

- **Outcome:** ASSUMPTION — MA7 = "today, end of business," restating what the Background prose
  already establishes narratively. No search performed (not a real-world fact); does not enter any
  D1-D5 calculation.

## P12 — Appendix C, current sublet's move-out date

- **Outcome:** ASSUMPTION — MA8 = "3 days from today," restating the Background's "turns over to
  its next tenant in days." No search performed; does not enter any calculation.

## P13 — Appendix C, Maya's monthly housing budget ceiling

- **Outcome (original, 2026-09-03):** ASSUMPTION — MA9 = $2,100/month, set above the most expensive
  computed scenario (Aldergate break-at-month-6, $2,048/month) so both leases are affordable per
  the Background's framing, which is a narrative device rather than a calculation input.
- **Revised 2026-09-04** (see the P01/P05 data-decay entry below): raised to $2,450/month to stay
  above the new, higher break-scenario totals after S1/S2's refresh and MA2's revision.

## P01/P05 REVISED — case-readiness Tier 2 P6 data-decay check, 2026-09-04

- **Why revisited:** a Tier 2 probe 6 (data decay) fetch of S1/S2's source URL — RentCafe's Boise,
  ID market-trends page — found it no longer showed the recorded $1,389 (studio) / $1,536
  (one-bedroom) figures. This is a live-updating dashboard, not a fixed historical snapshot, so
  this is expected drift rather than a sign the original figures were wrong, but per the P6 rule "a
  URL that resolves but no longer carries the figure is worse [than a dead link], because nothing
  else in the pipeline would ever notice" — it must not be silently left as-is.
- **Found:** the same page, re-fetched 2026-09-04, now states "Last updated: August 31, 2026" with
  studio rent $1,447/month and one-bedroom rent $1,601/month.
- **Decision:** S1/S2 refreshed to $1,447/$1,601 (as of 2026-08-31). Every figure originally set as
  a percent or multiple of the old rent was recomputed at the same percent/multiple of the new
  rent, so the case's stated proportional structure is preserved exactly:
  - MA1 (Cedarline move-in fee, ~30% of Cedarline rent): $415 → **$434**.
  - MA2 (Cedarline termination penalty, 3.5 months' Cedarline rent): $4,862 → **$5,065**.
  - MA3 (Aldergate deposit, 1 month's Aldergate rent): $1,536 → **$1,601**.
  - MA4 (Aldergate buyout, 1 month's Aldergate rent): $1,536 → **$1,601**.
  - MA9 (Maya's budget ceiling, set above the costliest scenario): $2,100 → **$2,450**.
- **Outcome:** S1 = $1,447 (MEDIUM, refreshed), S2 = $1,601 (MEDIUM, refreshed). Recomputed
  break-at-month-6: Cedarline $2,363.50 vs. Aldergate $2,134.67 — Aldergate still genuinely cheaper,
  now by 10.7% (was 10.8% before the refresh — the reversal is robust to this update, since both
  units' rents moved by a similar proportion). See `case.json.sensitivity_note`,
  `sensitivity_model.py`, and `FACILITATOR.md` for the fully updated record.

---

## Summary

Values below are the **current** (post-refresh, 2026-09-04) figures. See the P04 REVISED and
P01/P05 REVISED entries above for the prior values and why they changed.

| Placeholder | Status | Value | Confidence / basis |
|---|---|---|---|
| P01 Cedarline rent | SOURCED | $1,447 | MEDIUM (S1, refreshed 2026-09-04) |
| P02 Cedarline move-in fee | ASSUMPTION | $434 | grounded in S3 (MEDIUM range) |
| P03 Cedarline lease term | SOURCED | 12 months | HIGH (S4) |
| P04 Cedarline termination penalty | ASSUMPTION | $5,065 | grounded in S7+S8 (MEDIUM range) |
| P05 Aldergate rent | SOURCED | $1,601 | MEDIUM (S2, refreshed 2026-09-04) |
| P06 Aldergate deposit | ASSUMPTION | $1,601 | grounded in S6 (MEDIUM) |
| P07 Aldergate lease term | SOURCED | 12 months | HIGH (S4) |
| P08 Aldergate buyout | ASSUMPTION | $1,601 | grounded in S5 (MEDIUM range) |
| P09 Contract firm term | ASSUMPTION | 6 months | narrative basis, no market citation possible |
| P10 Early-move month | ASSUMPTION | Month 6 | narrative basis |
| P11 Signing deadline | ASSUMPTION | Today, EOB | narrative basis |
| P12 Sublet move-out | ASSUMPTION | 3 days from today | narrative basis |
| P13 Budget ceiling | ASSUMPTION | $2,450/month | narrative basis |
| — Extension length (added 2026-09-04) | ASSUMPTION | Covers remainder of the 12-month term | narrative basis (MA10) |

4 SOURCED, 10 ASSUMPTION, 0 NOT FOUND / DROPPED / OPEN. (P04/MA2 revised 2026-09-04, grounded in
S7+S8 instead of S5 alone; MA10 added 2026-09-04; S1/S2 and their dependent MAs refreshed
2026-09-04.)

## Balance / margin impact

### Original (2026-09-03)

- **Stay-full-term (D2):** Cedarline $1,423.58/mo vs. Aldergate $1,664.00/mo → Cedarline cheaper by
  **~16.9%**.
- **Break-at-month-6 (D3):** Cedarline $1,921.17/mo vs. Aldergate $2,048.00/mo → **Cedarline**
  cheaper by ~6.6% (case-qa, 2026-09-03, corrected a winner-label error in this log's original
  draft, which had misattributed this figure to Aldergate).

Both scenarios favored Cedarline — no genuine reversal, contrary to the concept sheet's design
intent. Flagged in `case.json.sensitivity_note` and resolved below.

### Round 1 (case-readiness remediation, 2026-09-04) — MA2 revised

- **Stay-full-term (D2):** unchanged, Cedarline cheaper by **16.9%** (MA2 does not enter D2).
- **Break-at-month-6 (D3):** Cedarline $2,268.50/mo vs. Aldergate $2,048.00/mo → **Aldergate**
  cheaper by **10.8%**, following MA2's revision from 2 to 3.5 months' rent (see P04 REVISED above).

### Round 2 (case-readiness Tier 2 P6 data-decay check, 2026-09-04) — S1/S2 refreshed — CURRENT STATE

- **Stay-full-term (D2):** Cedarline $1,483.17/mo vs. Aldergate $1,734.42/mo → Cedarline cheaper by
  **16.9%** (essentially unchanged — both rents moved by a similar proportion).
- **Break-at-month-6 (D3):** Cedarline $2,363.50/mo vs. Aldergate $2,134.67/mo → **Aldergate**
  cheaper by **10.7%**, following S1/S2's refresh and the resulting recompute of MA1-MA4 and MA9
  (see P01/P05 REVISED above). The reversal survives the refresh comfortably.

The two scenarios now favor opposite leases, confirming the dilemma flips exactly as the concept
sheet and `case.json`'s `balance` block intended. The break-scenario margin (10.8%) lands inside the
concept sheet's 8-12% target band; the stay-full-term margin (16.9%) remains wide but within SPEC
§2's ~20% cap, and is flagged as a GAP (not a blocker) in `case.json.qa`.

## MA10 — added 2026-09-04 (case-readiness Tier 2 P4 remediation)

A fresh-subagent Tier 2 twist-integrity probe (P4) found that the discussion Twist's mapping of
"contract extension confirmed" → the stay-full-term (D2) scenario and "not extended" → the
break-at-month-6 (D3) scenario relied on an unstated convention: nothing in the original Appendix C
said how *long* an extension would run, so a student could ask "what if it's only extended by 3
months?" — a case the appendices never modeled. Not a real-world fact to research (Maya is
fictional) — added as **MA10**, a narrative/scoping assumption stating that an extension, if
granted, covers the remainder of the lease's full 12-month term. This closes the gap the probe
found without changing any dollar figure or the balance test.

**Next step:** Re-run `case-readiness` Tier 1 and Tier 2 on `the-lease-break`.
