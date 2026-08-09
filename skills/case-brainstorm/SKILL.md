---
name: case-brainstorm
description: "Propose new math case study CONCEPTS that close standards-coverage gaps in the Acton/Heroes math corpus. Use when the user says \"brainstorm a case study\", \"what case should we write next\", \"we need a geometry case\", \"give me case ideas for transformations\", \"close the surface area gap\", \"what's in the gap queue\", \"pitch me 5 case concepts\", or names an uncovered skill group (Transformations, Surface Area And Volume, Factoring, Division Of Fractions, Systems Of Equations) and asks for a case that would teach it. Reads readmodel/gap_queue.json and standards_spine.json, emits 3-5 ranked concept sheets to cases/_concepts/ — each with protagonist, binary dilemma, primary metric, the exact spine skills it would close, and an honest feasibility note on whether real sourceable data exists. Ranks by skills-closed x data-availability. NEVER writes a full case study and never invents a data source it has not checked."
---

# case-brainstorm — gap-driven case concept generation

The first stage of the case pipeline. Turns "Geometry/Transformations is 20/20 uncovered" into
3–5 concrete, rankable case study concepts a human can pick from. **It produces concepts only.**
Writing the case is `case-write`; sourcing the numbers is `case-research`.

## Project paths

Resolve the project root once and reuse it. On macOS it is
`/Users/<user>/Documents/Claude/Projects/Math Builder`. In the workspace shell it is mounted
under `/sessions/<session>/mnt/Projects/Math Builder` — find it with
`ls -d /sessions/*/mnt/Projects/"Math Builder"`.

| Path | Role |
|---|---|
| `SPEC.md` | The contract. Read §0, §1.4, §2, §3 before proposing anything. |
| `readmodel/gap_queue.json` | Thin coverage by domain/group, sorted by `n_gap`. **Read this first.** Note the convention: `n_gap` counts skills with `n <= 2` (uncovered *and* thin), out of `n_total` in the group. The per-skill `n` tells you which are truly zero. It is a derived view — regenerated from the spine on every publish, never hand-edited. |
| `readmodel/standards_spine.json` | All 322 skills with `id`, `label`, `kind`, `covered_by[]`, `n`. The authority for skill ids and labels. |
| `readmodel/cases_index.json` | Existing corpus — 27 legacy cases. Read it to avoid re-proposing an existing case. |
| `cases/_concepts/` | **The only place this skill writes.** |

## Procedure

### 1. Establish the target

If the user named a gap (a domain, group, or specific skill), use it. If they named nothing, pick
the target yourself. Rank by **zero-coverage count first** (a skill at `n == 0` is a hole; a skill
at `n == 2` is merely thin), then by the fraction of the group that is thin:

```bash
cd "$PROJECT" && python3 -c "
import json
q=json.load(open('readmodel/gap_queue.json'))
rows=[(sum(1 for s in g['skills'] if s['n']==0), g['n_gap'], g['n_total'], g['domain'], g['group']) for g in q]
for z,ng,nt,d,gr in sorted(rows, key=lambda r:(-r[0], -(r[1]/r[2])))[:8]:
    print(f\"zero {z:3d} | thin {ng:3d}/{nt:<3d} | {d} / {gr}\")
"
```

As of the seed read-model the top of that list is:

```
zero  20 | thin  20/20  | Geometry / Transformations
zero  17 | thin  19/22  | Geometry / Quadrilaterals And Polygons
zero  14 | thin  19/24  | Geometry / Fundamentals Of Geometry
zero   8 | thin  10/11  | Geometry / Visual Perceptibility
zero   6 | thin   6/6   | Basic Operations / Factoring
zero   5 | thin   9/9   | Statistics And Probability / Algebra
zero   5 | thin   7/11  | Advanced Operations / Variables
zero   4 | thin  10/10  | Geometry / Surface Area And Volume
```

100 of 322 skills have zero coverage and **Geometry is the corpus's big hole** — the top four
groups are all Geometry. Surface Area And Volume ranks lower on zeros but is 10/10 thin: every
skill in it sits at n ≤ 1, so one case there both closes gaps *and* thickens the whole group. A
concept that hits Transformations plus Visual Perceptibility is the highest-value target
available today.

Tell the user which target you picked and why, in one line, before you generate anything.

### 2. Pull the exact uncovered skills for the target

Never work from memory or from the gap queue's abbreviated labels. Pull ids, labels and kinds
from the spine, because `case-write` will need the ids and the verbatim labels:

```bash
cd "$PROJECT" && python3 -c "
import json,sys
target_group='Transformations'   # <- set this
d=json.load(open('readmodel/standards_spine.json'))
for dom in d['domains']:
    for g in dom['groups']:
        if g['group']!=target_group: continue
        for s in g['skills']:
            if s['n']==0:
                print(f\"{s['kind']:7s} | {s['id']:70s} | {s['label']}\")
"
```

**Watch for duplicate labels across groups.** `Congruent` exists in both
Geometry/Transformations and Geometry/Fundamentals Of Geometry; `Volume` exists in both
Geometry/Surface Area And Volume and Measurement/Units; `Digit` exists in two Number Sense
groups. Always carry the **id**, not just the label. A concept that claims "Congruent" without
saying which id is ambiguous and `case-qa` will reject it downstream.

### 3. Generate 3–5 concepts

Each concept must satisfy SPEC §0: **a decision under constraint where the math is the only way
to defend a position, and where a reasonable person could argue either side.** Not a word problem
with a story on top.

Generation heuristics that actually work for this corpus:

- **Start from the skill, find the job.** Who gets *paid* to do this math? Surface area of a
  cylinder → a brewery choosing a fermentation tank; a rocket team choosing a fuel tank; a city
  choosing a water tower. Transformations → a stadium seating-bowl designer; a warehouse robot
  path planner; a quilt/tile manufacturer nesting a pattern; a satellite imaging analyst
  registering two photos of the same ground.
- **The binary is the hard part.** Two named, pre-analyzed options (SPEC §1.4). "Which tank?" is
  weak. "Tank A: the squat 12-ft cylinder from the domestic supplier, delivered in 3 weeks —
  or Tank B: the tall 8-ft cylinder from the import supplier, delivered in 9" is a case.
- **Pick a primary metric that is a ratio, not a total.** `cost per delivered dose`,
  `square feet of steel per gallon held`, `minutes of robot travel per pallet`. Ratios make the
  two options come close; totals make one obviously win.
- **Aim the margin at 5–15%.** SPEC §2 caps it at ~20%. You cannot know the true margin before
  research, but you can tell whether the two options are structurally comparable. If one option
  is obviously twice as good, say so and change a constraint now.
- **Follow SPEC §6 on subject matter.** Prefer protection over destruction — doses delivered,
  structures saved, acres protected — same stakes, better room.

### 4. Score the feasibility of the data — honestly

This is the step that decides whether the case survives `case-research`. For each concept, name
the **specific** sources you believe exist, and grade:

| Grade | Factor | Means |
|---|---|---|
| HIGH | 1.0 | You can name a specific public dataset, published price list, government table, or manufacturer spec sheet **and** you are confident it is online and free. Example: USDA food price data, USGS streamflow, a published tank manufacturer's PDF spec sheet, an airline's published baggage fee table. |
| MEDIUM | 0.6 | The category of source exists and is usually public, but you have not identified the specific document, or it may require assembling several sources. |
| LOW | 0.25 | You are guessing that data exists. Likely to come back NOT FOUND from `case-research` and force Modeling Assumptions. |

**Do not web-search during brainstorm** unless the user asks for a verified concept sheet. The
grade is an honest prior, and it is allowed to be wrong — `case-research` is the arbiter. What is
**not** allowed is writing "HIGH — data readily available" with no named source. If you cannot
name the source, it is MEDIUM at best.

### 5. Rank

```
weight(skill)      = 1.0 if kind == "how-to", 0.6 if kind == "term"
raw                = sum of weight over the uncovered skills the concept would close
group_bonus        = +2.0 if the concept closes every remaining gap in one spine group
score              = (raw + group_bonus) * availability_factor
```

How-tos outweigh terms deliberately: vocabulary is cheap to claim and cheap to fake. A concept
that closes twelve terms and no how-tos is vocabulary stuffing.

**Coverage-inflation guard:** a single 2–3 hour case honestly exercises roughly 8–15 skills. If a
concept claims more than 15 new skills, flag it — either it is inflated, or it should be split
into two cases. Say which.

**Calibration point — the score is bounded by the target group's size, not by concept quality,
and Cold Chain proves it.** Recomputed under this exact formula (2026-08-01): Cold Chain's own
`new_coverage[]` (`advanced-operations-absolute-value`, `advanced-operations-how-to-evaluate-an-absolute-value-expression`,
`geometry-prism`) scores **raw 2.2, +2.0 group bonus** (it happened to close the last two
zero-coverage skills in Advanced Operations/Scientific Notation-Factorial-Absolute-Value) **× HIGH
= 4.2.** That is *lower* than several concepts in `cases/_concepts/CONCEPTS_precalc-calculus-discrete_2026-08-01.md`
that never got written. The lesson: a concept targeting a spine group with only 5–8 total skills
(most of Discrete Mathematics's own groups, by construction — see B2) has a hard ceiling around
5–8 even at perfect HIGH feasibility and a full-group bonus; that is not the concept being weak,
it is the group being small. **Do not chase a higher number by claiming skills the case doesn't
genuinely force** (see the "Never" list) — if two honestly-scoped concepts each undershoot a
target because they split a small group cleanly between them (no overlap, both HIGH), evaluate
them as a pair against the threshold, not each alone. When in doubt about whether a concept is
"good enough," a real shipped case is a better calibration anchor than an abstract number — ask
whether it clears Cold Chain's own 4.2, not whether it hits some larger score that assumes a
bigger group than the one it's actually targeting.

### 6. Write the concept sheet

One file per run, all concepts in it:
`cases/_concepts/CONCEPTS_<target-slug>_<YYYY-MM-DD>.md`.

Use exactly this template per concept:

```markdown
### C1 — <Title>   ·   score <n.n>   ·   tier <T1-T4>
**Protagonist.** <Name>, <specific job title> at <specific org type>. Personally at stake: <one clause>.
**The dilemma.** A.) <one line> OR B.) <one line>
**Primary metric.** <a ratio, with units>
**Why it's close.** <2-3 sentences: what makes A win on one axis and B win on another. This is
the balance argument in embryo.>
**Would close (<k> skills, <h> how-to / <t> term):**
| id | kind | label |
|---|---|---|
| geometry-how-to-find-the-surface-area-of-a-cylinder | how-to | How to find the surface area of a cylinder |
| ... | | |
**Already-covered skills it also exercises.** <ids, brief — these do not score but they show the case is well-rounded>
**Data feasibility: HIGH/MEDIUM/LOW.** Named sources I expect to exist:
- <org + document + what number it gives>
- <...>
Sources I am NOT confident about: <the honest gaps — these become `{{NEEDS_SOURCE}}` risks>
**Sensitivity (SPEC §6).** <NONE, or the one-line facilitator flag this case would need>
**Split risk.** <NONE, or: claims N skills, recommend splitting into X and Y>
```

Head the file with a short table ranking all concepts by score, and a one-paragraph
**Recommendation** naming the concept you would write and the one you would kill, with reasons.

### 7. Hand off

End your reply with: the ranked list, the recommendation, the path to the concept sheet, and the
literal next step — `Approve a concept, then run case-write on it.` Nothing is written to
`cases/<id>/` until a human picks one.

## Worked example (abbreviated)

Target picked: **Geometry / Surface Area And Volume — 10/10 uncovered**, plus
**Geometry / Visual Perceptibility — 10/11**.

> ### C1 — Fermenter · score 5.8 · tier T2
> *(raw = 4 how-to × 1.0 + 3 terms × 0.6 = 5.8; no group bonus, the group has 10 skills;
> availability HIGH × 1.0 → 5.8)*
> **Protagonist.** Rosa Delgado, head brewer at a 12-employee regional brewery, who signed the
> distribution contract herself and has to make the tank fit the room.
> **The dilemma.** A.) Buy two squat 20-bbl cylindrical fermenters that fit under the existing
> ceiling OR B.) Buy one tall 40-bbl fermenter and cut a hole in the mezzanine.
> **Primary metric.** Dollars of steel-and-buildout cost per barrel of annual capacity.
> **Why it's close.** One 40-bbl tank has less surface area per unit volume than two 20-bbl
> tanks, so it is cheaper in steel and loses less heat — but it needs the mezzanine cut, and it
> cannot run two beers at once, which costs Rosa a contract term. The volumes are equal by
> construction; the case turns on surface area and schedule.
> **Would close (7 skills, 4 how-to / 3 term):** `geometry-how-to-find-the-surface-area-of-a-cylinder`,
> `geometry-how-to-find-the-volume-of-a-cone` (conical bottom), `geometry-how-to-draw-the-net-of-a-3-d-shape`,
> `geometry-how-to-name-a-3-d-shape`, `geometry-face`, `geometry-edge`, `geometry-prism`
> **Data feasibility: HIGH.** Named sources: published fermenter spec sheets from tank
> manufacturers (dimensions, capacity, jacket area); Brewers Association published barrel/cost
> figures; commodity stainless sheet pricing. Not confident about: regional mezzanine
> construction cost — that will likely be a stated Modeling Assumption.

## Never

- Never write a full case study, a Background, or an appendix. Concepts only.
- Never claim a skill the concept does not genuinely force a student to use. `case-write` runs a
  bidirectional LEARNING GOAL CHECK and will surface the lie as an unreachable skill.
- Never grade data feasibility HIGH without naming a specific source document.
- Never propose a concept whose title collides with a case already in `cases_index.json`.
- Never invent a number in a concept sheet. Ranges and orders of magnitude in the "why it's
  close" narrative must be written as reasoning ("one large tank has less surface area per unit
  volume than two small ones"), never as fake data ("saves $14,200").
- Never propose a three-way or open-ended dilemma. Binary always (SPEC §1.4).
