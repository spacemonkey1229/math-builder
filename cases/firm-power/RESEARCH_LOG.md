# Research Log — Firm Power

## Placeholders and resolution

| # | Placeholder | Searched | Found | Resolution |
|---|---|---|---|---|
| P01 | Real hourly demand data for a real balancing authority | (1) EIA API v2 (`api.eia.gov`) — requires a registered API key this session does not hold; not used. (2) CAISO's own public "Today's Outlook" data feed — searched for its download URL format. | `https://www.caiso.com/outlook/history/{YYYYMMDD}/{report}.csv` — a real, public, key-free CSV feed (5-minute resolution), confirmed live via direct `curl` fetch for 2026-09-01. | SOURCED — S1, HIGH confidence. On-the-hour readings extracted for all 24 hours; full 289-row raw file retained locally during research. |
| P02 | Gas peaking levelized cost | Web search for NREL ATB 2026 combustion turbine capital cost (surfaced a real EIA capital-cost-study PDF figure, $836/kW, but that is a CAPEX figure, not LCOE, and a direct WebFetch of that PDF failed to extract readable text). Pivoted to Lazard's "Levelized Cost of Energy+" report, per `readmodel/domains.json`'s own energy-grid data-availability note recommending it. | Lazard LCOE+ June 2025 (v18.0) PDF, fetched and read directly (page 8): Gas Peaking unsubsidized LCOE $149-$251/MWh, national range. | SOURCED — S2, HIGH confidence, primary industry report, page image read directly. |
| P03 | Solar-plus-storage levelized cost and a real capacity-reliability discount mechanism | Same Lazard report, "Cost of Firming Intermittency" section (pages 25-30) — read directly via the PDF page-image tool. | CAISO row of the real ELCC/Net CONE table (page 28): 4-Hour Lithium-Ion Battery firming source; Solar ELCC 7%, PV+Storage ELCC 41%, Wind ELCC 12%; Net CONE $18.92/kW-month. Results chart (page 30): CAISO PV+Storage LCOE $73/MWh + Levelized Firming Cost $69/MWh = $142/MWh total (internally verified: $73+$69=$142 matches the printed total, corroborating both sub-figures were read correctly). | SOURCED — S3, HIGH confidence. See also "the formula-reproduction attempt," below. |
| P04 | CCA share of CAISO's total system demand | Fictional district; searched for real comparable-scale California CCA peak-demand figures. | No single real figure applies to a fictional entity. Real CCAs vary from under 100,000 to several million customers (Clean Power Alliance / CalCCA public reporting). | NOT FOUND (for a specific real figure) → resolved as MA1, a disclosed 3% scenario assumption. |
| P05 | Board's monthly capacity-tranche budget | No public figure exists for a fictional district's internal budget. | N/A | NOT FOUND → resolved as MA2, a disclosed $10,000/month scenario assumption, stated specifically to give Challenge D4 a solvable equation. |

## The formula-reproduction attempt (why S3's note flags it)

Lazard's report (page 29) gives the Levelized Firming Cost formula explicitly:

```
Levelized Firming Cost ($/MWh) =
  [Nameplate Capacity (kW) x (1 - ELCC%) x Net CONE ($/kW-month) x 12 months]
  / [Nameplate Capacity (MW) x Regional Capacity Factor (%) x 8,760 hours]
```

Attempting to reproduce CAISO's own $69/MWh figure using the page-28 table's inputs (ELCC 41%,
Net CONE $18.92/kW-month) and the page-30 table's reported CAISO PV+Storage capacity factor (43%):

```
numerator (per 1 MW nameplate) = 1,000 kW x (1 - 0.41) x $18.92/kW-mo x 12 = $133,970.40 / year
denominator = 1 MW x 0.43 x 8,760 h = 3,766.8 MWh / year
result = $133,970.40 / 3,766.8 MWh = $35.57/MWh
```

This does **not** match Lazard's own published $69/MWh figure. Two distinct search framings and a
direct re-read of the fetched PDF page images did not resolve the gap — plausible explanations
include a rounding difference in a transcribed input, a regional-methodology adjustment (the
report's own footnotes mention CAISO- and PJM-specific storage-configuration assumptions — "50% of
PV capacity and 4-hour duration" — that may enter the real calculation in a way not fully legible
in this fetch) or a capacity-factor figure that applies to a different quantity than assumed here.

**Resolution: this case cites Lazard's own published $69/MWh and $142/MWh output figures directly
(S3) rather than presenting a self-derived, non-matching number as sourced** — consistent with
SPEC §5's rule against fabrication and with `case-research`'s own instruction to report a
discrepancy honestly rather than launder it. Challenge D4 was redesigned specifically so that
students work the real Net CONE figure through its own unit-conversion and a separate, fully
self-contained equation, rather than being asked to reproduce the full firming-cost formula
end-to-end and risk hitting this same unexplained gap themselves.

## Full arithmetic: from sourced figures to the published numbers

**Descriptive statistics (Appendix A's real 24-value CAISO series), before redaction:**

```
values (MW) = [26956,25795,24558,23822,23371,23893,25151,26390,26699,26137,24908,24577,
               24473,24811,25821,27257,29388,30943,32842,33087,32456,31496,30224,28115]
n = 24, sum = 653,170, mean = 27,215.4 MW
sorted min = 23,371 (04:00), max = 33,087 (19:00), range = 9,716 MW
median = 26,263.5 MW  (average of the two middle values, 26,137 and 26,390)
Q1 = 24,694.0 MW (median of the lower 12 values)
Q3 = 29,806.0 MW (median of the upper 12 values)
IQR = 5,112.0 MW; outlier fence = [Q1 - 1.5*IQR, Q3 + 1.5*IQR] = [17,026, 37,474]
No value in the set falls outside the fence -- this real day's data has NO statistical outlier
by the 1.5xIQR test. (Challenge D1 asks students to show this test, not to find one that doesn't
exist.)
```

**Peak window (hours where demand exceeds Q3):**

```
17:00 = 30,943 | 18:00 = 32,842 | 19:00 = 33,087 (redacted in case.md, see below)
20:00 = 32,456 | 21:00 = 31,496 | 22:00 = 30,224
-> 6 consecutive hours exceed Q3 (29,806 MW).
```

**Missing-data reconstruction (Challenge D2), the arithmetic a Hero should reproduce:**

```
missing = 24 x mean - sum(23 known values)
        = 24 x 27,215.4 - (653,170 - 33,087)
        = 653,169.6 - 620,083
        = 33,086.6  ~= 33,087 MW (rounding in the stated mean accounts for the 0.4 MW gap)
```

**Capacity sizing (Challenge D3), applying MA1's 3% share:**

```
Q3_scaled  = 29,806 x 0.03 = 894.18 MW
peak_scaled = 33,087 x 0.03 = 992.61 MW
new_capacity_needed_MW = peak_scaled - Q3_scaled = 98.43 MW
MWh_needed = new_capacity_needed_MW x 6 hours = 590.58 MWh
```

**Net CONE conversion and budget equation (Challenge D4):**

```
$18.92/kW-month x 12 months/year x 1,000 kW/MW = $227,040 / MW-year

Budget = X(MW) x Net_CONE($/MW-yr)
$120,000/year (MA2: $10,000/month x 12) = X x $227,040/MW-yr
X = $120,000 / $227,040 = 0.5285 MW (~528.5 kW) of firming capacity the board's
    monthly budget alone could support -- illustrative only, not the case's own decision metric.
```

**Total cost comparison (Challenge D5):**

```
Option A (Peaker Contract):        590.58 MWh x $149/MWh = $87,996.42
Option B (Firmed Solar Contract):  590.58 MWh x $142/MWh = $83,862.36
margin_pct = |149 - 142| / max(149,142) x 100 = 4.70%
winner: B
```

## Rejected sources

- EIA's own capital-cost-study PDF (a real, HIGH-confidence primary source for a $836/kW gas
  combustion-turbine CAPEX figure) was found but not used directly — CAPEX ($/kW) is a different
  quantity from LCOE ($/MWh), and Lazard's report already gives a directly comparable $/MWh figure
  for both technologies on the same basis, which is what this case's primary metric needs.
- The NREL ATB website (`atb.nrel.gov`) could not be reached via WebFetch in this research pass
  (DNS resolution failure in this tool's sandbox) — not used; Lazard's report filled the same role.

## Verification sweep (per case-research §7 script)

- Placeholders remaining in case.md: 0.
- Citation markers [S1]-[S4] all resolve to a `sources[]` row.
- No source graded LOW; one (S4) graded MEDIUM, used only as supplemental basis for a disclosed
  Modeling Assumption, never as a load-bearing case number.
- `status` → `researched`.
