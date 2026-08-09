---
name: case-research
description: "Fill the {{NEEDS_SOURCE}} placeholders in a drafted math case study with real, cited data — value, units, source organization, document title, URL, publication date, and a HIGH/MEDIUM/LOW confidence grade. Use when the user says \"source the numbers\", \"research the case\", \"fill the placeholders\", \"find real data for the Fermenter case\", \"where can we get tank prices\", \"cite this case\", or after case-write reports N open placeholders. Also gathers supplemental appendix materials — articles, Desmos graphs, Google Maps routes, spec sheets, price lists — and appends everything to sources[] in case.json. Anything unsourceable comes back as NOT FOUND and becomes either an explicit stated Modeling Assumption or a case redesign. It is NEVER quietly invented: a plausible number is not a true number."
---

# case-research — cited numbers, or an honest hole

Stage three. Turns a number-free spine into a solvable case. The entire value of this skill is
that it is **allowed to fail loudly**. A `NOT FOUND` is a good outcome. A plausible-looking
invented figure is a corpus-poisoning outcome, because nobody downstream can tell the difference.

> SPEC §5: *Never fabricate a number. Every figure in an appendix is either (a) cited to a real
> source, or (b) explicitly labeled as a stated scenario assumption in a `Modeling Assumptions`
> block. There is no third category.*

## Inputs

- `cases/<id>/case.md` and `cases/<id>/case.json` from `case-write`.
- Tools: `WebSearch` and `web_fetch` (load via ToolSearch if deferred:
  `select:WebSearch`). Prefer `web_fetch` on a specific document over search-result summaries.

## Outputs

- `cases/<id>/case.md` — placeholders replaced with values + `[S<n>]` citation markers, plus a
  `Modeling Assumptions` block if any were accepted, plus a `Sources` appendix.
- `cases/<id>/case.json` — `sources[]` populated, `needs_source[]` statuses updated,
  `modeling_assumptions[]` populated.
- `cases/<id>/RESEARCH_LOG.md` — every placeholder, what was searched, what was found or not.

---

## Procedure

### 1. Enumerate the open placeholders

```bash
cd "$PROJECT" && python3 - <<'PY'
import json,re
cid="fermenter"
md=open(f'cases/{cid}/case.md').read()
for i,m in enumerate(re.finditer(r'\{\{NEEDS_SOURCE:\s*([^}]*)\}\}', md),1):
    line = md[:m.start()].count('\n')+1
    print(f"P{i:02d}  line {line:4d}  {m.group(1).strip()}")
PY
```

Work them in order of **load-bearing weight**, not document order. Ask of each: *if this number
is wrong by 30%, does the answer to the dilemma flip?* Those are the ones to spend effort on. A
decorative figure that changes nothing can be dropped from the case entirely — say so.

### 2. Source each one

Search strategy, in priority order. Stop at the first tier that yields the figure:

| Tier | Source class | Typical grade |
|---|---|---|
| 1 | Primary publisher of the fact: a government statistical agency, a regulator, the manufacturer's own spec sheet or price list, a company's own filing, a published tariff/fare/fee schedule, a standards body | HIGH |
| 2 | An institution that republishes tier 1 with attribution: a trade association, a university extension service, a national lab, an established industry database | HIGH or MEDIUM |
| 3 | Reputable journalism or an aggregator citing a named tier-1 source | MEDIUM |
| 4 | A blog, forum, undated page, AI summary, or a site that gives a number with no provenance | LOW — **do not use for a load-bearing figure** |

Grading rules, applied strictly:

- **HIGH** — primary or well-attributed republication, **and** it carries a date or a clearly
  stated period, **and** the units are unambiguous, **and** the figure is the thing the case
  needs (not a proxy for it).
- **MEDIUM** — one of those four is soft: undated, a proxy quantity, a wide range you had to pick
  a midpoint from, a regional figure used for a different region, or a secondary source.
- **LOW** — you found a number but cannot defend its provenance. A LOW figure may appear in a
  case **only** as deliberately messy appendix noise the student is meant to filter out, and only
  when labeled as such. It may never carry a constraint.

Record the arithmetic when you derive. If the case needs "cost per barrel" and the source gives
total cost and barrel count, the derivation is yours and must be shown; the source entry cites
the two inputs, and `derived: true` marks the output.

### 3. Write the source record

Append to `case.json` `sources[]`. SPEC §4 requires `claim`, `value`, `url`, `confidence`; the
rest are pipeline extensions and all of them are required by `case-qa`:

```json
{
  "id": "S3",
  "placeholder": "P07",
  "claim": "List price of a 40 bbl conical stainless fermenter",
  "value": "18,450",
  "units": "USD",
  "as_of": "2026-03",
  "org": "<manufacturer name>",
  "title": "<exact document title>",
  "url": "https://…",
  "accessed": "2026-07-31",
  "confidence": "HIGH",
  "derived": false,
  "note": "List price, does not include freight or glycol package — freight is a separate placeholder."
}
```

Rules:
- `url` must be the page that actually contains the figure, not a homepage or a search URL.
- `accessed` is the date you fetched it. Sources rot; the case must record when it was true.
- `note` carries every caveat: what is excluded, what region, what year's dollars. This is where
  a careful case earns its credibility.
- **Contested figures.** Where a widely repeated number is poorly sourced or conflates
  categories, say so in the case rather than using it (SPEC §5 — the "50% of vaccines wasted"
  precedent). A one-line note in the appendix that a commonly cited figure was excluded and why
  is itself good teaching material.

### 4. Substitute into `case.md`

Replace the placeholder with the value plus a citation marker keyed to the Sources appendix:

```
| List price (USD) | $18,450 [S3] | $26,900 [S4] |
```

Then add or extend the **Sources** appendix (it is a normal lettered appendix, referenced from
Background — "All figures in this case are sourced in (SEE APPENDIX F)"):

```markdown
### Appendix F — Sources
| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S3 | 40 bbl conical fermenter list price | $18,450 | <Org> — <Doc title> ([link](https://…)) | 2026-03 | HIGH |
```

Never leave a `[S<n>]` marker without a matching row, and never leave a row unreferenced.

### 5. Handle NOT FOUND — the important part

When a figure cannot be sourced after a genuine attempt (at least: two distinct search framings,
and a direct fetch of the most likely primary publisher), return it as **NOT FOUND** and present
the human with exactly three exits. Do not choose for them on a load-bearing figure.

1. **Stated Modeling Assumption.** The case declares the number in the open. Requires all of:
   a plausible basis you can articulate, a stated range, and placement in a visible
   `Modeling Assumptions` block — never buried in a table as though it were sourced.

   ```markdown
   ## Modeling Assumptions
   > These figures are **not sourced**. They are stated scenario assumptions chosen by the case
   > author. A Hero may challenge them in discussion — that is a legitimate move.

   | # | Assumption | Value used | Basis | Sensitivity |
   |---|---|---|---|---|
   | MA1 | Mezzanine cut-and-reframe cost | $12,000 | No public price exists for a one-off structural cut; the case fixes a value so both options are comparable. | Option B wins below ~$19,000; above that A wins. The margin is sensitive to this number. |
   ```

   The **Sensitivity** column is mandatory for any assumption that can flip the dilemma. At T4,
   a flippable assumption is a *feature* — SPEC §3 requires T4 cases to make the student state
   and defend an assumption.

2. **Redesign.** Change the case so the unsourceable quantity is not needed. Usually the best
   answer: swap the constraint for one with public data. Report this as a recommendation with
   the specific edit.

3. **Drop the figure.** If it was decorative, cut it. Then cut whatever referenced it.

**There is no fourth exit.** Never write a number that looks sourced but is not. Never write
"approximately", "industry standard", or "typically around" as a laundering device.

### 6. Supplemental appendix materials

Beyond the placeholders, gather what makes the case feel real (SPEC §1.6):

- A news article or trade-press piece that establishes the situation is a real kind of situation.
- A **Desmos** graph for anything with a functional relationship (build the URL, verify it loads).
- A **Google Maps** route or measured distance for anything geographic — record the measured
  value in-document, since the link may die.
- Manufacturer spec sheets, published price lists, timetables, calendars, floor plans.
- Deliberately over-complete data at T3+: real tables carry columns the student must decide to
  ignore. Include them. Do not annotate which are irrelevant.

Every external link gets the same treatment: **anything load-bearing is reproduced in-document.**
Verify each URL resolves before shipping it. A dead link in a student packet is a QA GAP.

### 7. Update `case.json` and log

- `needs_source[].status` → `SOURCED` | `ASSUMPTION` | `DROPPED` | `OPEN`.
- `sources[]` appended.
- `modeling_assumptions[]` populated with the MA table rows.
- `status` → `"researched"` once zero placeholders remain OPEN.
- Write `cases/<id>/RESEARCH_LOG.md`: one row per placeholder — what you searched, what you
  fetched, what you found, what you rejected and why. The rejections are the valuable part; they
  stop the next person re-running the same dead search.

Verify nothing was missed:

```bash
cd "$PROJECT" && python3 - <<'PY'
import json,re
cid="fermenter"
md=open(f'cases/{cid}/case.md').read(); c=json.load(open(f'cases/{cid}/case.json'))
left=re.findall(r'\{\{NEEDS_SOURCE:[^}]*\}\}',md)
marks=set(re.findall(r'\[(S\d+)\]',md)); srcs={s['id'] for s in c['sources']}
print("placeholders remaining:",len(left))
print("citation markers with no source row:", marks-srcs)
print("source rows never cited in text:",     srcs-marks)
for s in c['sources']:
    miss=[k for k in ("claim","value","units","org","title","url","accessed","confidence") if not s.get(k)]
    if miss: print("INCOMPLETE",s.get('id'),"missing",miss)
low=[s['id'] for s in c['sources'] if s['confidence']=='LOW']
print("LOW-confidence sources (must not be load-bearing):", low)
PY
```

### 8. Report

A table: placeholder → value → confidence → source org. Then, separately and prominently:
**NOT FOUND count**, each with the recommended exit. Then the next step —
`Run case-qa on <id>.`

## Worked example

`{{NEEDS_SOURCE: 304 stainless sheet price, USD per pound, US spot, 2026 or most recent}}`

1. Tier-1 attempt: search for a government or exchange-published stainless price series. Metals
   pricing is largely paywalled — expect this to fail, and record that it failed.
2. Tier-2 attempt: a trade association or a public metals-service-center price page.
3. Outcome A — found a dated public price page: grade MEDIUM (a service-center list price is a
   proxy for spot, and it is regional), note the caveat, cite it.
4. Outcome B — nothing public and dated: return **NOT FOUND**, and recommend a **redesign**:
   the case does not actually need steel *price*, it needs **relative** steel *quantity* between
   two tanks — which is pure geometry the student computes, with the manufacturer's list price
   (which is public) as the cost input. The redesign removes the unsourceable figure and makes
   the case more purely geometric. **This is the right move, and finding it is the job.**

## Never

- Never invent, estimate-and-present-as-fact, or round a remembered figure into a case.
- Never let a LOW-confidence figure carry a constraint or a dilemma-flipping quantity.
- Never bury an unsourced number in a data table. Assumptions live in a visible
  `Modeling Assumptions` block, labeled.
- Never cite a homepage, a search results page, or a URL you did not fetch.
- Never smooth over a contested figure — name the dispute in the case.
- Never edit the Overview, the Dilemma, the boilerplate Challenges, or the final "How To…"
  appendix. Structure belongs to `case-write`; if research forces a structural change, say so and
  hand it back.
- Never set `qa.verdict`, never touch `readmodel/standards_spine.json`.
