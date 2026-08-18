---
name: case-write
description: "Write the SPINE of a math case study from an approved concept — title block, Overview, Background, binary Dilemma, the fixed five Challenges, appendix stubs, and the mandatory 'How To…' standards appendix — conforming to SPEC.md §1. Use when the user says \"write the case\", \"draft case study X\", \"turn concept C2 into a case\", \"write up the Fermenter case\", \"build the case spine\", \"I approve concept 3, write it\", or hands over an approved concept sheet from cases/_concepts/. Runs the bidirectional LEARNING GOAL CHECK (every Challenge-3 deliverable must map to a named spine skill; every claimed skill must be forced by some deliverable) and emits case.json per SPEC.md §4. Leaves EVERY figure as a {{NEEDS_SOURCE: ...}} placeholder — this skill never invents a number and never sources one; case-research does that."
---

# case-write — the case spine

Stage two of the pipeline. Takes an **approved concept** and produces a structurally complete,
number-free case study document plus its `case.json`. The document it emits is not yet readable
by a student: every figure is a placeholder. That is deliberate. **The writer never invents
figures.** Numbers arrive in stage three from `case-research`, cited.

## Inputs required

1. An approved concept — from `cases/_concepts/CONCEPTS_*.md`, or stated directly by the user.
   If the concept is vague on the **binary dilemma** or the **primary metric**, stop and ask.
   Those two are load-bearing; everything else you can draft.
2. `SPEC.md` — read §1, §2, §3, §5, §6 in full before writing.
3. `readmodel/standards_spine.json` — the authority for skill ids and verbatim labels.
4. `doctrine/CHALLENGE_BOILERPLATE.md` — the canonical Challenge text. **Insert it from the
   file. Do not retype it from memory.**

## Outputs

```
cases/<id>/
├── case.md            the case study spine, numbers as {{NEEDS_SOURCE: ...}}
├── case.json          SPEC §4 record + pipeline extensions
├── LEARNING_GOALS.md  the bidirectional deliverable ↔ skill matrix
└── FACILITATOR.md     draft: both arguments + 5 Socratic questions + the trap
```

`FACILITATOR.md` is drafted here, not at publish time — you understand the balance better than
anyone downstream will. SPEC §7 requires it; `case-qa` checks it exists and has five questions
and a named trap; `case-publish` renders it into the packet.

`<id>` is the lowercase slug of the title: `Fermenter` → `fermenter`,
`Cold Chain` → `cold-chain`.

---

## Procedure

### 1. Lock the skill list first, before writing prose

Pull the exact ids, labels and kinds you intend to claim. Verbatim labels are needed for the
final appendix; ids are needed for `case.json`.

```bash
cd "$PROJECT" && python3 - <<'PY'
import json
IDS = ["geometry-how-to-find-the-surface-area-of-a-cylinder",
       "geometry-how-to-find-the-volume-of-a-cone"]        # <- your claimed ids
d = json.load(open('readmodel/standards_spine.json'))
by_id = {s['id']:(dom['domain'], g['group'], s)
         for dom in d['domains'] for g in dom['groups'] for s in g['skills']}
for i in IDS:
    if i not in by_id: print("MISSING FROM SPINE:", i); continue
    dm,gp,s = by_id[i]
    print(f"n={s['n']:2d} {s['kind']:7s} | {dm}/{gp} | {s['label']}")
PY
```

- Any id not in the spine is a **hard stop** — fix the id, do not invent a skill.
- Record which claimed skills currently have `n == 0`. That subset is `new_coverage[]`, and
  **it must be non-empty** (SPEC §7). A case that closes nothing has no reason to exist.
- Note the **duplicate-label hazard**: `Congruent`, `Volume`, `Weight`, `Digit` and
  `Line Segment` appear under more than one group. `case.json` disambiguates by id; the final
  appendix prints only the label, which is correct and expected — the join is by id.

### 2. Title block

```
Case Study: Fermenter
MS | Math | Case Study | 2026 | Adventure
```

1–3 words, concrete noun, no colon-subtitle. `Airstrike`. `Cinema`. `Catering`. Never
`A Study of Volumetric Optimization`. Studio is `Adventure` or `Launchpad`.

### 3. Overview — 150–300 words, and zero numbers the student needs

Rules from SPEC §1.2, all of them enforced by QA:

- Present tense. *In medias res* — mid-action, mid-dialogue, or mid-crisis. **Never** open with
  background ("The Riverbend Brewing Company was founded in 2011…" is an instant rewrite).
- A named protagonist with a specific job and something personal at stake.
- Concrete sensory detail. The smell of hot wort. A forklift alarm. A phone face-down on a
  clipboard.
- **Ends at the instant of decision** and stops. The protagonist holding two folders, opening
  the tab, reading the buzzing phone. It does not resolve, hint, or moralize.
- **No load-bearing numbers.** A date on a calendar or "twelve employees" as texture is fine
  only if the student never needs it. If a student could plug it into a calculation, it belongs
  in Background or an appendix. When in doubt, cut the number.

Write the Overview *last*, after the Background exists — you write a better hook when you know
what the constraint set actually is.

### 4. Background — 200–500 words, third person, neutral

- The protagonist's role, authority, and what they are accountable for.
- **Both options named explicitly, with memorable labels** — `Operation Grey Dawn` /
  `Operation Desert Sparrow`, `The Squat Pair` / `The Tall One`. The Dilemma section restates
  these labels; QA checks both appear here.
- Every hard constraint: budget, deadline, capacity, contractual minimum, physical limit. Each
  one as a placeholder: `{{NEEDS_SOURCE: 2026 stainless 304 sheet price, USD per lb}}`.
- **No decorative constraints.** If a constraint never enters a calculation and never rules out
  an option, delete it. (Deliberately *irrelevant appendix data* is allowed and encouraged at T3+
  — that is filtering practice. An unused constraint stated as a rule in Background is different:
  it is noise.)
- Cross-reference every appendix you intend to ship: `(SEE APPENDIX A)`, `(SEE APPENDICES C AND D)`.

### 5. Dilemma — exactly this shape

```
You are Rosa Delgado.
Do you:
A.) Buy two 20-barrel squat fermenters that clear the existing ceiling OR
B.) Buy one 40-barrel tall fermenter and cut the mezzanine
```

Binary, always. No third option, no "or something else", no elaboration paragraph after it.

### 6. Challenges — insert the boilerplate from the doctrine file

```bash
sed -n '/^## BEGIN CANONICAL BLOCK/,/^## END CANONICAL BLOCK/p' \
  "$PROJECT/doctrine/CHALLENGE_BOILERPLATE.md"
```

Paste sections 1, 2, 4, 5 **character-for-character** from that block, including the `1.)` style
numerals, the curly quotes around `"excellent"` and `"how to…"`, and the leading `*` on the
absence clause in section 5. Then author **only** section 3.

Section 3 is a short list — three to six concrete artifacts the pitch must contain. These are
what force the math. Give each one a stable id (`D1`, `D2`, …) because `case.json` and the
learning-goal matrix reference them:

```
3.) Your pitch must include:
    D1. A dimensioned net of each fermenter option, drawn to scale, with every face labeled.
    D2. A surface-area comparison table: total steel area for Option A vs Option B, in square feet.
    D3. A cost-per-barrel-of-capacity calculation for each option, showing your arithmetic.
    D4. A one-year heat-loss estimate for each option, using the jacket area you computed in D2.
```

Write deliverables as **artifacts**, not as instructions. "A cost-per-barrel table" is a
deliverable. "Calculate the cost per barrel" is a homework problem.

### 7. Appendices — stubs now, data later

Letter them `Appendix A`, `Appendix B`, …. At this stage each is a stub with a title, a
statement of what it will hold, and its placeholders:

```markdown
### Appendix C — Fermenter Spec Sheets
| | Option A (20 bbl, ×2) | Option B (40 bbl, ×1) |
|---|---|---|
| Nominal capacity (bbl) | {{NEEDS_SOURCE: manufacturer nominal capacity, Option A}} | {{NEEDS_SOURCE: ..., Option B}} |
| Overall height (in) | {{NEEDS_SOURCE: ...}} | {{NEEDS_SOURCE: ...}} |
| Shell diameter (in) | {{NEEDS_SOURCE: ...}} | {{NEEDS_SOURCE: ...}} |
| Cone angle (deg) | {{NEEDS_SOURCE: ...}} | {{NEEDS_SOURCE: ...}} |
| List price (USD) | {{NEEDS_SOURCE: ...}} | {{NEEDS_SOURCE: ...}} |
```

Rules:
- **Every appendix must be referenced** from Background or Challenges. Orphans are a QA failure.
- External links (Desmos, Google Maps, a live price page) are welcome, but anything load-bearing
  is also reproduced in-document so the case survives the link dying.
- Data may be messy and over-complete. At T3+, include figures the student must decide to
  ignore — filtering is part of the work. Mark none of them as "irrelevant"; that is the point.

### 8. The placeholder discipline

Every figure in the document is one of exactly three things:

| Form | When |
|---|---|
| `{{NEEDS_SOURCE: <precise description, with units>}}` | Default. Everything. |
| A number under a `Modeling Assumptions` heading | Only after `case-research` returns NOT FOUND and a human accepts the assumption. **Never at write time.** |
| A number with an inline citation | Only after `case-research` fills it. |

There is no fourth category. A plausible number is not a true number (SPEC §5).

**The Modeling Assumptions block states WHAT was assumed and WHY — never the RESULT.** A recurring
defect found 2026-08-13 across 9+ cases from two separate authoring passes: a `Sensitivity`/`Why`
column that names the assumption, then goes on to state the case's own `balance_test.margin_pct`,
which option wins, or the exact dollar/percent threshold where SPEC §2's 20% cap breaks. That is
the answer key, handed to the student inside the document they're meant to solve — caught by Tier
2 probe 1's leak check every time, but only after a full case-write pass has to be redone. Write
the assumption's basis and its real-world justification; if you need to note that the assumption is
load-bearing, say "the answer is sensitive to this value" — never the size, direction, or threshold
of that sensitivity. That analysis belongs in `case.json.balance`/`sensitivity_disclosure[]` and
`FACILITATOR.md`, both facilitator-only, never in `case.md`'s student-facing appendices.

Write the description precisely enough that a researcher can act on it without re-reading the
case. Bad: `{{NEEDS_SOURCE: steel price}}`. Good:
`{{NEEDS_SOURCE: 304 stainless sheet price, USD per pound, US spot, 2026 or most recent}}`.

### 9. Final appendix — "How To…" Math Questions To Research

**Mandatory. This is the standards bridge** (SPEC §1.7). Two parts, and every line is a
**verbatim label from the spine** — not paraphrased, not re-cased, not pluralized.

Generate it mechanically. Never type these by hand:

```bash
cd "$PROJECT" && python3 - <<'PY'
import json
IDS = ["geometry-surface-area", "geometry-how-to-find-the-surface-area-of-a-cylinder"]  # claimed ids
d = json.load(open('readmodel/standards_spine.json'))
by_id = {s['id']:s for dom in d['domains'] for g in dom['groups'] for s in g['skills']}
terms  = [by_id[i]['label'] for i in IDS if by_id[i]['kind']=='term']
howtos = [by_id[i]['label'] for i in IDS if by_id[i]['kind']=='how-to']
print("### Appendix Z — \"How To…\" Math Questions To Research\n")
print("**Vocabulary terms**\n")
for t in terms:  print(f"- {t}")
print("\n**\"How to…\" questions**\n")
for h in howtos: print(f"- {h}")
PY
```

Letter it as the last appendix in sequence (if you have appendices A–F, this is G).

### 10. The LEARNING GOAL CHECK — run it, do not skip it

A bidirectional mapping between Challenge-3 deliverables and claimed spine skills. Write it to
`cases/<id>/LEARNING_GOALS.md` as a matrix:

```markdown
| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 dimensioned nets | geometry-how-to-draw-the-net-of-a-3-d-shape, geometry-face, geometry-edge, geometry-how-to-name-a-3-d-shape |
| D2 surface-area table | geometry-surface-area, geometry-how-to-find-the-surface-area-of-a-cylinder |
| D3 cost per barrel | geometry-how-to-find-the-volume-of-a-cylinder, geometry-how-to-find-the-volume-of-a-cone, advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 heat loss | measurement-how-to-convert-an-amount-with-compound-units |
```

Then report **two error classes**, both BLOCKERs:

- **UNMAPPED DELIVERABLE** — a Challenge-3 deliverable with an empty skills column. The artifact
  costs the student time and teaches nothing measurable. Either bind it to a skill or cut it.
- **UNREACHABLE SKILL** — a skill in `standards[]` that no deliverable forces. This is the common
  failure: the author lists a skill because it sounds related. Either add a deliverable that
  genuinely requires it, or remove it from `standards[]`. **An unreachable skill in
  `new_coverage[]` is the worst case — it silently marks a gap closed that the student never
  touched, corrupting the coverage matrix for every future gap query.**

"Forces" has a strict test: *could a competent student produce this deliverable correctly
without ever performing this skill?* If yes, the mapping is fake.

Print both lists explicitly, even when empty:

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 11    new_coverage: 7
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

Do not proceed to `case.json` with either list non-empty. Fix the case.

### 11. Balance argument — draft it now

QA needs it and you understand the case best right now. Draft, in `case.json` and as a section at
the bottom of `case.md` under `<!-- FACILITATOR ONLY -->`:

- The strongest **quantitative** argument for A
- The strongest **quantitative** argument for B
- The expected **margin** on the primary metric

At write time the margin is `{{NEEDS_SOURCE}}`-dependent, so record it as `null` with a
`margin_basis` string explaining how it will be computed once the numbers land. Do not guess a
percentage.

Then write `cases/<id>/FACILITATOR.md` with, at minimum:

- **Argument for A** and **Argument for B** — the quantitative case for each, in facilitator voice.
- **The margin** — how it will be computed, and (after research) what it is.
- **Five Socratic questions**, each ending in a question mark, each answerable only with the
  case's numbers. Not "what did you choose?" — "Your cost-per-barrel favours B by 8%. What would
  the mezzanine quote have to be for that to flip?"
- **The trap** — the plausible reasoning that produces a confident wrong answer. Every good case
  has one; naming it is what lets a discussion lead run the room. ("Heroes will compare total
  price and miss that Option A buys two tanks, so the capacity denominators differ.")
- A **sensitivity note** if SPEC §6 applies.

### 12. Emit `case.json`

SPEC §4 fields, plus additive pipeline extensions (marked). Additive keys are permitted; the
SPEC §4 keys are mandatory and may not be renamed.

```json
{
  "id": "fermenter",
  "title": "Fermenter",
  "tier": "T2",
  "complexity": 2,
  "band": ["MS-core"],
  "primary_metric": "buildout dollars per barrel of annual capacity",
  "options": { "A": "Two 20-bbl squat fermenters under the existing ceiling",
               "B": "One 40-bbl tall fermenter with the mezzanine cut" },
  "margin_pct": null,
  "standards": ["geometry-surface-area", "geometry-how-to-find-the-surface-area-of-a-cylinder"],
  "new_coverage": ["geometry-how-to-find-the-surface-area-of-a-cylinder"],
  "sources": [],

  "_ext": "keys below are pipeline extensions, additive to SPEC §4",
  "status": "draft",
  "studio": "MS Adventure",
  "protagonist": "Rosa Delgado, head brewer",
  "deliverables": [
    {"id": "D1", "text": "A dimensioned net of each fermenter option…",
     "skills": ["geometry-how-to-draw-the-net-of-a-3-d-shape"]}
  ],
  "appendices": [
    {"letter": "A", "title": "Fermenter Spec Sheets", "referenced_from": ["Background"], "kind": "table"}
  ],
  "balance": {
    "argument_a": "…",
    "argument_b": "…",
    "margin_basis": "Compare total buildout cost / annual barrel capacity across A and B once the spec sheets and the mezzanine quote land.",
    "margin_pct": null
  },
  "needs_source": [
    {"token": "{{NEEDS_SOURCE: 304 stainless sheet price, USD per pound, US spot, 2026}}",
     "location": "Appendix C, row 'List price'", "status": "OPEN"}
  ],
  "modeling_assumptions": [],
  "sensitivity_note": null,
  "qa": {"verdict": null, "run_on": null, "blockers_open": null, "case_md_sha256": null},
  "authored_on": "2026-07-31",
  "pipeline_version": "1.0"
}
```

`complexity` (added above, alongside `tier`) is the T1→1/T2→2/T3→4/T4→5 star mapping from §14 —
set it here at write time, not left for a later backfill.

Validate before you finish:

```bash
cd "$PROJECT" && python3 - <<'PY'
import json,re,hashlib,sys
cid = "fermenter"
c = json.load(open(f'cases/{cid}/case.json'))
md = open(f'cases/{cid}/case.md').read()
sp = json.load(open('readmodel/standards_spine.json'))
by_id = {s['id']:s for dom in sp['domains'] for g in dom['groups'] for s in g['skills']}
err=[]
for k in ["id","title","tier","band","primary_metric","options","margin_pct","standards","new_coverage","sources"]:
    if k not in c: err.append(f"case.json missing SPEC §4 key: {k}")
for s in c["standards"]:
    if s not in by_id: err.append(f"standards[] id not in spine: {s}")
for s in c["new_coverage"]:
    if s not in c["standards"]: err.append(f"new_coverage[] not a subset of standards[]: {s}")
    elif by_id[s]["n"] != 0:    err.append(f"new_coverage[] claims a skill already covered (n={by_id[s]['n']}): {s}")
if not c["new_coverage"]: err.append("new_coverage[] is empty — the case has no reason to exist (SPEC §7)")
toks = re.findall(r'\{\{NEEDS_SOURCE:[^}]*\}\}', md)
print(f"placeholders in case.md: {len(toks)}   recorded in needs_source[]: {len(c.get('needs_source',[]))}")
if len(toks) != len(c.get('needs_source',[])): err.append("needs_source[] count != placeholders in case.md")
print("SHA256(case.md) =", hashlib.sha256(md.encode()).hexdigest()[:16])
print("ERRORS:" if err else "VALIDATION CLEAN"); [print(" -",e) for e in err]
PY
```

### 13. Tier check against SPEC §3

Before you hand off, sanity-check the tier you declared against the numeric load you actually
wrote (QA will do this again, harder):

| Tier | Numeric load | Ambiguity |
|---|---|---|
| T1 | arithmetic, percent, single-step unit conversion | one dominant variable |
| T2 | multi-step, rates, ratio, area/volume, weighted comparison | two competing variables that trade off |
| T3 | scientific notation, systems, probability, optimization over a set | 3+ variables, some data deliberately irrelevant |
| T4 | algebraic modeling, functions, statistics with inference, sensitivity | assumptions must be stated and defended; data incomplete by design |

**T4 cases must include at least one quantity the student has to assume**, with the assumption
stated and justified. If you declared T4, name that quantity now.

### 14. Set complexity from tier

Set `case.json["complexity"]` from the tier you just checked, using this fixed mapping (never a
different one, never a guess independent of tier):

| Tier | Complexity (stars) |
|---|---|
| T1 | 1 |
| T2 | 2 |
| T3 | 4 |
| T4 | 5 |

(3 is deliberately skipped — SPEC §3's numeric-load table shows a bigger jump T2→T3 than between
the other adjacent tiers.) This is a normal `case.json` key written alongside `tier`, not a
separate step later — set it now, at write time.

### 15. Report and hand off

Report: case id, tier, deliverable count, claimed/new-coverage skill counts, LEARNING GOAL CHECK
result, placeholder count, and the next step —
`Run case-research on <id> to fill <N> placeholders.`

## Never

- **Never write a number.** Not a "reasonable" price, not a "typical" capacity, not a rounded
  placeholder value. Every figure is `{{NEEDS_SOURCE: …}}` until `case-research` cites it or a
  human accepts it as a stated Modeling Assumption.
- Never retype the Challenge boilerplate from memory — read `doctrine/CHALLENGE_BOILERPLATE.md`.
- Never paraphrase a spine label in the final appendix. Verbatim or it breaks the coverage join.
- Never claim a skill no deliverable forces, and never ship with an unmapped deliverable.
- Never write a three-option dilemma, an Overview containing load-bearing numbers, or an appendix
  nothing references.
- Never set `qa.verdict`. Only `case-qa` writes that. Never publish. Only `case-publish` does.
- Never edit `readmodel/standards_spine.json`. Coverage moves at publish time, not write time.
