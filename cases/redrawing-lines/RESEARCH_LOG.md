# RESEARCH LOG — Redrawing Lines

**Run:** 2026-08-12 · **Stage:** 3 (`case-research`) · **Placeholders at entry:** 20 · **OPEN at exit:** 0

Every URL below was fetched in this session (WebFetch, or `curl` for the two bulk data files that
are too large for a page fetch) and confirmed to carry the figure cited. Nothing here is a
remembered URL (MCS-21).

---

## Sourcing outcome, by placeholder

| P | Figure needed | Outcome | Source / MA |
|---|---|---|---|
| P01 | Maine 2020 apportionment population + House seats | SOURCED | S1 |
| P02 | Five-county core shortfall from the ideal | SOURCED (derived) | S2 + S6 |
| P03 | 2020 Census population, all 16 Maine counties + state total | SOURCED | S2 |
| P04 | Ideal district population | SOURCED | S6 (cross-checked against S2 ÷ S1) |
| P05 | Maine county adjacency, all 16 counties + border count | SOURCED | S4 |
| P06 | Kennebec municipalities in CD-1, with populations | SOURCED | S5 + S3 |
| P07–P08 | Kennebec Split district populations | SOURCED | S6 |
| P09 | Kennebec's split shares | SOURCED (derived) | S3 + S5, cross-checked to S6 |
| P10 | Kennebec Split county-line crossings | **DROPPED from case.md by design** — left as "a Hero computes this"; the value lives in `case.json.derived` and `sensitivity_model.py` | derived from S2 + S4 + MA1 + MA2 |
| P11–P12 | Hancock Line district populations (683,062 / 679,297) | SOURCED (derived) | S2 |
| P13 | Hancock Line county-line crossings | **DROPPED from case.md by design** — same reason as P10 | derived from S4 |
| P14 | Appendix D one-county add-on menu | SOURCED (derived); deviations and crossings deliberately withheld as student work | S2 + S4 |
| P15 | Karcher v. Daggett deviation + holding | SOURCED | S8 |
| P16 | Tennant v. Jefferson County Commission variance + holding | SOURCED | S9 |
| P17 | Fundamental Counting Principle total | SOURCED (derived) | S2 (county list) |
| P18 | Contiguous-plan count | SOURCED (derived) | S2 + S4 |
| P19 | Weight of a severed county, in crossings | **ASSUMPTION** | MA1 |
| P20 | Commission report delivery date | SOURCED | S7 |

Two placeholders (P10, P13) resolved to **DROPPED** rather than SOURCED, and that is a design
decision, not a research failure: publishing each plan's crossings score in `case.md` would hand
the student the entire D5 deliverable. Both figures are fully computed, reproducible from
Appendix B by hand, and recorded in `case.json.derived` and `sensitivity_model.py`. The same
reasoning withheld the deviation and crossings columns from Appendix D.

---

## What was searched, fetched, and rejected

### The population data — two numbers that are both correct and not equal

First search framing: *"Maine 2020 census apportionment population two congressional seats."*
Reached the Maine Secretary of State's own apportionment pages, which state the ideal district
(**681,179.5**) and the two enacted district populations (**681,179** / **681,180**) — fetched and
confirmed at `maine.gov/sos/elections-voting/2020-census-apportionment-overview` (S6). The
companion *Details* page carries the commission's **September 27, 2021** delivery date (S7).

**Rejected:** the Census Bureau's own API (`api.census.gov/data/2020/dec/pl`) — it 302s to a
`missing_key.html` page without an API key. Recorded so nobody re-runs it.

Second framing: go to the primary file instead. Downloaded the official **2020 Census P.L. 94-171
Redistricting Data Summary File for Maine** (`me2020.pl.zip`, 6.1 MB) and parsed table P1 at
summary level 050 (counties) and 060 (county subdivisions). This produced all 16 county
populations and all 30 Kennebec municipality populations directly from the primary file (S2, S3).

**The discrepancy, and why the case names it.** Census apportionment Table 1 gives Maine
**1,363,582**; the P.L. 94-171 resident count is **1,362,359**. The gap is overseas federal
employees, who count for apportionment and belong to no county. Both figures are correct and they
answer different questions. The case prints both and explains the difference (Appendix A) rather
than quietly using whichever one made the arithmetic tidy.

### The statute, and a cross-check that came out exact

Fetched `legislature.maine.gov/statutes/21-a/title21-Asec1205-A.html` (S5) twice — once for the
district definitions, once to pull the Kennebec municipality lists exactly. First District: 12
Kennebec municipalities (Albion, Benton, China, Clinton, Litchfield, Pittston, Unity Township,
Vassalboro, Waterville, West Gardiner, Windsor, Winslow). Second District: the other 18. 12 + 18 =
30, which matches the number of Kennebec county subdivisions in the Census file exactly.

**The cross-check that makes this case trustworthy.** The five whole southern counties sum to
627,584 (S2). The twelve statutory municipalities sum to 53,595 (S3). 627,584 + 53,595 = **681,179**
— exactly the enacted CD-1 population the Secretary of State publishes (S6). Three independent
sources agree to the person. This is why the Kennebec split shares (53,595 / 70,047) are graded as
a derivation from HIGH sources rather than an estimate.

### County adjacency

Fetched the Census Bureau's county adjacency landing page, which named the current file as
`county_adjacency2025.txt`. Downloaded it and extracted the 16 Maine rows (S4): 34 distinct
county-to-county borders. **Cross-checked** against the older `county_adjacency.txt` (2010 vintage,
also downloaded) — the Maine adjacency is byte-identical between vintages, which is what you would
expect and is worth knowing.

**Caveat carried into the case, not smoothed over.** The file counts Hancock and Knox as
neighbours; their legal boundary meets across Penobscot Bay. That is the Census definition, and
the case says so in Appendix B and invites the student to argue with it.

### The case law

`supreme.justia.com` and `supremecourt.gov` both returned **403** to the fetcher (the
supremecourt.gov PDF URL served an HTML block page, confirmed by `file`). Recorded so nobody
retries them from this sandbox.

Second framing: Cornell Legal Information Institute, which republishes the official opinions.
Fetched and confirmed:

- **Karcher v. Daggett**, 462 U.S. 725 (1983) — 3,674 people, **0.6984%** maximum deviation,
  struck down; holding quoted verbatim in Appendix E (S8).
- **Tennant v. Jefferson County Commission**, 567 U.S. 758 (2012) — 4,871 people, **0.79%**
  variance, upheld; the "valid, neutral state districting policies" language quoted verbatim, plus
  the finding that West Virginia had never divided a county between congressional districts (S9).

These two are the contested pair SPEC §5 asks an author to name rather than paper over. Appendix E
prints both, says plainly that they point different ways, and says that neither opinion fixes a
ceiling — which is the honest state of the law and is also the case's central argument.

### Sourced and then deliberately not used

**Compactness scores.** Polsby-Popper, Reock and the other standard compactness measures need
district perimeters and areas. No public file publishes those for a plan nobody drew, and
computing them would need shapefile geometry the case cannot cite for both plans on the same
basis. Rather than quote a score for one plan and estimate it for the other, the case measures
**county-line crossings**, which is computable for any plan from S4 alone. Appendix G states this
exclusion and what a student would need in order to get a perimeter-based score instead. This is
the `case-research` redesign exit, taken deliberately: the metric changed so that no figure had to
be invented.

**Election results and party registration.** Available (MIT Election Data & Science Lab, cited in
the concept sheet as a live source) and **deliberately not fetched or used**. The case is built
only on population, geography and case law; adding partisan data would change what the case is
about and would not improve the math.

---

## Modeling assumptions accepted

| # | Why no source exists | Exit taken |
|---|---|---|
| MA1 | No published redistricting rubric assigns a numeric weight to severing a county. Searched framings: state statutory compactness tests, commission scoring rubrics. Nothing numeric and general. | Stated Modeling Assumption, value 1, with its sensitivity written out — it is the dial that decides the primary metric. |
| MA2 | "Which borders does the line run along?" is undefined for a divided county without a convention, and resolving it from real geography would need town-level boundary data the case does not model. | Stated Modeling Assumption (majority assignment), with the explicit warning that the opposite convention roughly triples the gap and pushes the margin past SPEC §2's cap. |
| MA3 | The five-county shortlist rule is staff practice in this fictional scenario; no source establishes it as Maine practice. | Stated Modeling Assumption, flagged as practice and not statute — and it is exactly what the discussion twist attacks. |
| MA4 | The protagonist and the internal deliberation are invented. | Stated in the open, with the boundary between what is real (commission, statute, populations, case law) and what is not drawn explicitly. |

## Verification at exit

```
placeholders remaining: 0
citation markers with no source row: none
source rows never cited in text: none
LOW-confidence sources: none
```

**Next step:** `case-readiness` on `redrawing-lines`.
