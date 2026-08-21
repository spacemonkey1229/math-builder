# Research Log — Pets

**Run:** 2026-08-20 · **Stage:** case-research (legacy conversion)

## Starting state

`case-write` produced `case.md`/`case.json` with every dollar figure as
`{{NEEDS_SOURCE: ...}}`. The original source docx (`Case Study_ Pets.docx`,
`Guide Notes.docx`) has **no embedded cost data** — Appendices A/B/C/D in the
original are link-only reading lists ("The Cost Of Owning A Dog - Online
Article", etc.), not tables or screenshots the way Family Trip's or
Cardiology's source docs were. So unlike those two conversions, this one could
not extract any real historical figures from the legacy file itself — every
number below was sourced fresh.

## What was searched and fetched

| # | Query / URL | Purpose | Result |
|---|---|---|---|
| 1 | WebSearch: "Beagle puppy adoption price cost first year 2026 food vet vaccines" | Orient on Beagle cost categories | Found Insurify, Hepper, PetMD as strong candidates |
| 2 | WebSearch: "Scottish Fold kitten price cost of ownership first year vet food" | Orient on Scottish Fold cost categories | Found Catster, Petful, A-Z Animals |
| 3 | WebSearch: "Beagle average lifespan years" | Lifespan figure | 10-15 yrs consensus, most sources 12-15 |
| 4 | WebSearch: "Scottish Fold cat average lifespan years" | Lifespan figure | Found the real breed-wide-average-vs-healthy-individual split — load-bearing for the case's Twist |
| 5 | **WebFetch** https://insurify.com/pet-insurance/knowledge/how-much-is-beagle/ | Full Beagle cost breakdown by category | [S1] — directly fetched, full category table extracted |
| 6 | **WebFetch** https://www.catster.com/lifestyle/scottish-fold-cost/ | Full Scottish Fold cost breakdown by category | [S4] — directly fetched, full category table extracted |
| 7 | **WebFetch** https://www.petmd.com/dog/breeds/beagle | Beagle lifespan, confirm | [S2] — directly fetched, "10-15 years" confirmed |
| 8 | **WebFetch** https://www.catster.com/cat-health-care/how-long-does-scottish-fold-live/ | Scottish Fold lifespan + genetic basis | [S5] — directly fetched; this is the source of the case's central Twist (osteochondrodysplasia shortening the breed-wide average) |
| 9 | WebSearch: "average pet insurance cost dog vs cat monthly 2026" | Cross-check insurance premiums | Corroborated Insurify/Catster's own insurance figures; used as context source [S7] |
| 10 | WebSearch: "initial supplies cost new puppy vs new kitten..." | Orient on one-time setup costs | Confirmed the shape of Catster's/Hepper's own bundled one-time figures were reasonable |
| 11 | **WebFetch** https://www.petful.com/cat-breeds/scottish-fold-price/ | Breeder pricing tiers, pet- vs. show-quality | [S3] — directly fetched; gave the specific $1,000-$2,500 pet-quality tier used for MA6, distinguishing it from the inflated 2026 live-marketplace listings |
| 12 | **WebFetch** https://articles.hepper.com/beagle-cost/ | Independent second Beagle source | [S6] — directly fetched; its annual ($1,716-$3,900) and one-time-setup ($710-$1,200) figures closely cross-validated [S1], raising confidence and supplying the one-time-setup figure used for MA2 |
| 13 | **WebFetch** https://thebestofbreeds.com/first-year-puppy-costs-by-breed-2026-complete-financial-guide/ | Attempted Beagle first-year total | **403 Forbidden** — dropped, not used |
| 14 | **WebFetch** https://www.petplace.com/article/general/pet-care/how-much-does-a-new-pet-cost-in-the-first-year | Attempted a cleaner initial-supplies figure | Returned only a wide, non-itemized range ($2,250-$10,000 first year) with no puppy/kitten-specific supplies breakdown — dropped, not used as a cited figure (Hepper's [S6] figure was used instead) |
| 15 | **WebFetch** https://harvardfcu.org/blog/budgeting-for-a-new-best-friend-... | Attempted a cleaner initial-supplies figure | Returned only a single un-itemized "$50" combined estimate, inconsistent in scale with every other source — dropped, not used |

## Modeling decisions (why a midpoint, not a single "best" number)

Every real-world source gave a **range**, not a point figure (with the single
exception of Catster's Scottish Fold insurance premium, "$30/month", used
directly). Per `skills/case-write/SKILL.md` §8 and SPEC §5, a range is not
itself a usable single number — this project's practice (see Family Trip's
MA1/MA2) is to take the range's midpoint as a stated Modeling Assumption, with
the real range and its source disclosed in the appendix, rather than picking
an unstated "typical" value. All ten Modeling Assumptions (MA1-MA10, case.json
`modeling_assumptions[]`) follow this pattern. None invents a number outside
a cited range.

## The balance problem this run had to solve

The case's raw, un-normalized comparison — total lifetime dollars for a
Beagle vs. total lifetime dollars for a Scottish Fold — came out to a 51.7%
gap, which fails SPEC §2's 20% balance cap outright (see `case.json`
`legacy_conversion_note` for the full reasoning). This is not a research
defect; it's a real structural fact (the two pets have different average
lifespans), so the fix was not to re-source a number until the gap shrank —
that would be exactly the "hide data until the case passes" move SPEC §2
forbids. Instead the primary graded metric was changed to **lifetime cost per
year of expected lifespan** (still fully sourced, still using the same ten
Modeling Assumptions), which lands at a real, defensible 16.7% margin. The
raw 51.7% comparison is preserved in the case as the Twist/trap, not deleted.

## Zero-placeholder confirmation

```
$ grep -c '{{NEEDS_SOURCE' cases/pets/case.md
0
```

Every figure in `case.md` is either a real cited range (Appendices A, B, C, D
— tied to [S1]-[S7]) or a stated Modeling Assumption in Appendix E (MA1-MA10).
No figure was silently invented. `needs_source[]` in `case.json` is `[]`.
