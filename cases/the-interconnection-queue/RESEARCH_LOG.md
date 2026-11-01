# Research Log — The Interconnection Queue

Stage 3 (`case-research`) run on `cases/the-interconnection-queue/`. 8 `{{NEEDS_SOURCE}}`
placeholders enumerated from `case.md`. Worked in load-bearing order: the capacity-block MW size
(Appendix C/D, since Appendix B's bid sizes read against it) first, then Appendix F's four
background statistics.

## P01–P04 — Capacity block size, in megawatts (Appendix C, and Appendix D's MA1 value/basis/sensitivity)

**Searched:** "utility large load interconnection study capacity block MW increment substation
planning data center", "large load MW threshold transmission interconnection data center",
"Southern Company SPP Dominion large load MW threshold substation".

**Fetched directly:**
- `https://gridlab.org/wp-content/uploads/2025/03/GridLab-Report-Large-Loads-Interim-Report.pdf` —
  fetch returned raw/undecoded PDF content, not usable as a quotable source.
- `https://rmi.org/understanding-large-load-interconnection/` — RMI, a named nonprofit energy
  research organization, states directly: "larger loads — those exceeding approximately 20
  megawatts (MW) such as data centers — require direct connection to the transmission system."
  This is a real, dated, fetchable, general-industry reference point for the order of magnitude
  utilities use when defining a "large load" study threshold.

**Search also surfaced** (not fetched to a quotable state, but corroborating the same order of
magnitude): Southern Company's ≥50 MW threshold for transmission-connected large loads, SPP's
>10 MW at 69 kV / >50 MW at higher voltages threshold, and Dominion's 100 MW ring-bus / 300 MW
per-substation limits — all in the same tens-to-low-hundreds-of-MW range as RMI's ~20 MW figure,
reported secondhand via search-result synthesis rather than a directly fetched, quotable page, so
not used as a standalone citation.

**Outcome:** No public source states a capacity-block size specific to a fictional substation
("Fenwick Creek") that does not exist. Per the project instruction ("If exact substation-level
capacity figures for a specific real utility aren't public, use a disclosed, realistic Modeling
Assumption grounded in real, published regional capacity/queue-size statistics"), this is a
**stated Modeling Assumption (MA1)**, not a sourced figure: 24 MW, chosen near RMI's real ~20 MW
large-load interconnection reference point [S5], scaled up slightly so the case's stated total
(4-5/8 blocks) and committed (1-1/4 blocks) capacities land on whole-megawatt figures for the
pitch's narrative. Recorded as ASSUMPTION in `case.json.needs_source[]` and
`case.json.modeling_assumptions[MA1]`, and disclosed in `case.json.sensitivity_disclosure[]`
(Category F). **Load-bearing check:** unlike a typical scenario assumption, MA1 does *not* change
which option wins — the A-vs-B comparison is a same-units fraction comparison in blocks, and the
MW scale cancels out of it entirely (confirmed algebraically and will be confirmed mechanically by
Tier 2 P5). It only rescales the real-world MW figures reported in the pitch.

## P05 — Median interconnection queue wait time (Appendix F, S1)

**Searched:** "LBNL Queued Up 2025 report interconnection queue wait time years generation
storage."

**Attempted direct fetch:** `https://emp.lbl.gov/queues` and
`https://emp.lbl.gov/sites/default/files/2026-06/Queued%20Up%202026%20Edition.pdf` — both
returned HTTP 403 Forbidden on direct fetch; unusable as a directly-quotable source despite being
the primary publisher.

**Fetched directly (secondary, explicitly quoting the primary):**
`https://loopback.systems/insights/lawrence-berkeley-2025-interconnection-queue-report-overview` —
states directly: "The typical project reaching commercial operation in 2024 spent an average of
4.5 years (55 months) in the interconnection queue. This represents a significant increase from
2008 (22 months)." Names the report ("Queued Up," 2025 Edition), its publication date (Dec 15,
2025), and its as-of date (end of 2024).

**Outcome:** SOURCED as [S1], value 4.5 years (55 months), MEDIUM confidence (a secondary summary
explicitly naming and quoting the primary LBNL report, used because the primary report's own pages
returned an access error on direct fetch). Background texture establishing the real, widely
reported national bottleneck — not load-bearing to the A-vs-B fraction arithmetic, which is this
case's own fixed Appendix A/B scenario data.

## P06 — Total capacity in US interconnection queues, GW (Appendix F, S2)

**Searched:** "2026 total capacity in US interconnection queues gigawatts LBNL report."

**Fetched directly:** same Loopback Systems page as P05 — states directly: "As of the end of 2024,
approximately 2,290 gigawatts (GW) of capacity remains active in interconnection queues,
representing nearly twice the capacity of the current U.S. power plant fleet."

**Outcome:** SOURCED as [S2], value approximately 2,290 GW, MEDIUM confidence (same source and
access caveat as S1). Background texture only.

## P07 — Typical/representative AI data-center campus power demand, MW (Appendix F, S3)

**Searched:** "AI data center campus power demand megawatts 2026 hyperscale typical size", "DOE
report AI data center campus power demand 100 MW to 1 GW 2025 2026."

**Attempted fetch:** `https://uspeglobal.com/articles/ai-data-center-power-requirements/` returned
HTTP 403 Forbidden.

**Fetched directly:**
`https://www.datacenterknowledge.com/energy-power-supply/doe-says-ai-data-centers-are-rewriting-america-s-transmission-map`
— confirms the direct quote: "AI campuses at 500 MW or more become transmission-planning events,"
attributed to the U.S. Department of Energy's draft 2026 National Transmission Needs Study.

**Outcome:** SOURCED as [S3], value 500 MW threshold, MEDIUM confidence (trade press directly
quoting and naming a federal study; the study itself was not directly fetched). Background texture
establishing that AI campus loads of the scale this case discusses are a real, currently reported
phenomenon — this case's own bid sizes are stated in the substation's own capacity-block units
(Appendix B), not numerically tied to this figure.

**Correction (2026-09-09):** the original entry above mis-cited a paraphrase ("AI campuses at 500
MW or more become transmission-planning events") as a direct quote attributed to the DOE study
itself. Re-fetch of the same article confirms the actual verbatim sentence is: "At 500 MW or more,
transmission is not a downstream interconnection issue... The campus itself becomes a
transmission-planning event" — said by Ihab Osman, an independent strategist specializing in data
center and other mission-critical infrastructure, quoted *in* the article's coverage of DOE's draft
National Transmission Needs Study, not a line from the DOE study text. `case.md` Appendix F and
`case.json`'s `sources[S3]` have been corrected to use this verbatim quote with the correct
attribution (Ihab Osman, quoted in Data Center Knowledge).

## P08 — Regulatory reform on clustered/combined interconnection requests (Appendix F, S4)

**Searched:** "FERC Order 2023 first-ready first-served cluster study interconnection queue
reform", ""Order No. 2023" FERC July 28 2023 first-ready first-served effective date
interconnection."

**Attempted fetch:** `https://www.ferc.gov/explainer-interconnection-final-rule` returned HTTP 403
Forbidden — the primary regulator's own page was not directly fetchable.

**Fetched directly:**
`https://www.klgates.com/Order-No-2023-Interconnection-Reform-is-Finally-Here-9-7-2023` — a law
firm's published summary, confirms the direct quote: "Order No. 2023 replaces the current serial
interconnection process with an annual cluster study process, which allows for the study of a
group of interconnection requests by multiple generating facilities at the same time rather than
individually and sequentially," and confirms the issue date of July 28, 2023.

**Outcome:** SOURCED as [S4], MEDIUM confidence (a law firm's summary of a real, independently
verifiable federal order, not the order's own text, and dated 2023 rather than 2026 — used because
it is the real regulatory grounding for why this case's central dilemma, approving a single ready
bid now vs. holding for a better-fitting combination, is a live, current policy tension and not an
invented one). Not itself load-bearing to the A-vs-B fraction arithmetic.

## Verification sweep

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
```

All 5 source rows (S1–S5) carry `claim`, `value`, `units`, `org`, `title`, `url`, `accessed`,
`confidence`. No LOW-confidence sources; all five are MEDIUM (see Appendix F's summary paragraph in
`case.md` for why). No source is load-bearing to the case's own fixed fraction/mixed-number
arithmetic (Appendices A and B, and the block-size Modeling Assumption MA1) — all five ground the
case's real-world premise and the plausibility of MA1's magnitude, matching the "current-events
sourcing focus" instruction for this case.
