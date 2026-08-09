# SPEC — Anatomy of a Math Case Study

**Version:** 1.0 · **Status:** LOCKED · **Derived from:** 6 exemplar case studies + 15 student work products + the 27-case standards matrix (Acton Academy / Heroes Academy Discovery Studio corpus)

> This is the contract. Every case study produced by this project conforms to it. The `case-qa` skill enforces it mechanically. Deviations require a DOCTRINE_LEDGER row.

---

## 0. What a case study *is*

A math case study is **not** a word problem with a story pasted on top. It is a **decision under constraint** where the math is the only way to defend a position, and where a reasonable person could argue either side.

Modeled on Harvard Business School and Acton MBA cases, with a quantitative lean. The learner (Hero) works 2–3 hours with documentation, then attends a 45–60 minute Socratic discussion where they must defend their choice against peers.

**The load-bearing property is _defensible ambiguity_.** If the math produces one obviously correct answer, there is no discussion, and the case has failed. The numbers must make the choice *close*.

---

## 1. Required structure

Every case is a single document with these sections, in this order.

### 1.1 Title block
```
Case Study: <Short Evocative Noun>
MS | Math | Case Study | <year> | <studio>
```
Title is 1–3 words, concrete, no colon-subtitle. `Airstrike`. `Cinema`. `Catering`. `Family Trip`. Never `A Study of Volumetric Optimization`.

### 1.2 Overview — the hook
- **150–300 words.** Present tense. *In medias res.*
- Opens mid-action, mid-dialogue, or mid-crisis. Never with background.
- A **named protagonist** with a specific job and something personal at stake.
- Concrete sensory detail (the smell of popcorn; a yell echoing across the war room).
- **Ends at the instant of decision** — the protagonist holding two folders, opening the browser tab, reading the buzzing phone. It stops before the choice is made.
- Contains **no numbers the student needs.** Data lives in Background and Appendices. The Overview earns attention; it does not inform.

### 1.3 Background — the constraint set
- **200–500 words.** Third person, neutral, factual.
- Establishes the protagonist's role, authority, and what they are accountable for.
- Names the two options explicitly, ideally with memorable labels (*Operation Grey Dawn* / *Operation Desert Sparrow*).
- States every **hard constraint**: budgets, deadlines, capacities, contractual minimums, physical limits.
- Cross-references appendices: `(SEE APPENDIX A)`, `(SEE APPENDICES D, G and F)`.
- Every constraint stated here must be *needed*. No decorative constraints.

### 1.4 Dilemma — the fork
Exactly this shape, no elaboration:
```
You are <Protagonist Name>.
Do you:
A.) <Option A, one line> OR
B.) <Option B, one line>
```
**Binary. Always binary.** Not "what should they do" — a forced choice between two named, pre-analyzed options. Three options dilutes the Socratic discussion; open-ended kills it.

### 1.5 Challenges — the fixed five
Sections 1–2 and 4–5 are **boilerplate and must appear verbatim** (they are the badge requirements). Only section 3 is case-specific.

1. **Research task.** "Research and find an online resource that answers one of the 'how to…' questions from the case study launch. Post a link to the resource as your submission."
2. **The pitch.** "Post 250 or more 'excellent' words pitching a firm stance to your audience on which you would choose and why." Must include (a) use of the researched how-to, (b) **at least one original visual display** of the data.
3. **Case-specific deliverables.** ← *the only authored part.* A short list of concrete artifacts the pitch must contain: an itinerary, a master schedule, flight paths with distances and times, a cost breakdown, a loading plan. **These are what force the math.** Each deliverable maps to specific standards rows.
4. **Appendix of work.** "An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count."
5. **Discussion.** "Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 'excellent' words on the questions above."

### 1.6 Appendices — the data
Lettered `Appendix A`, `Appendix B`, …

- **Real data only.** Tables, price lists, maps, schedules, spec sheets, calendars, graphs.
- Every appendix must be **referenced from Background or Challenges**. Orphan appendices are a QA failure.
- External links are welcome (Desmos graphs, Google Maps routes, live price sites) — but the case must remain solvable if the link dies. Anything load-bearing gets reproduced in-document.
- Data may be *messy and over-complete*: real cases include figures the student must decide to ignore. This is deliberate — filtering is part of the work.

### 1.7 Final appendix — "How To…" Math Questions To Research
**Mandatory. This is the standards bridge.**

A two-part list:
- **Vocabulary terms** the case exercises (`Probability`, `Event`, `Mean`, `Percents`, `Decimals`)
- **"How to…" procedural skills** (`How to find the mean of a set of data`, `How to convert between units of time`)

Every line in this appendix **must be a verbatim label from `readmodel/standards_spine.json`.** Not paraphrased. This is what lets the coverage matrix update automatically and what the student researches in Challenge 1.

---

## 2. The balance test

A case passes only if **both options are genuinely defensible**. The `case-qa` skill checks this by requiring the author to supply:

- The strongest quantitative argument for A
- The strongest quantitative argument for B
- The **margin**: how close the two come on the primary metric

**Rule: if the better option wins by more than ~20% on the primary metric, the case is unbalanced** and must be retuned by adjusting a constraint — not by hiding data.

The Robotics Engineering exemplar is the gold standard: Route 1 beat Route 2 by **0.09%**, and the student still had to defend it. That is a case that works.

---

## 3. Difficulty tiers

| Tier | Band | Sessions | Numeric load | Ambiguity |
|---|---|---|---|---|
| **T1** | MS entry | 2 h | Arithmetic, percent, single-step unit conversion | One dominant variable |
| **T2** | MS core | 2–3 h | Multi-step, rates, ratio, area/volume, weighted comparison | Two competing variables that trade off |
| **T3** | MS stretch / HS entry | 3 h | Scientific notation, systems, probability, optimization over a set | Three+ variables; some data deliberately irrelevant |
| **T4** | HS | 3 h+ | Algebraic modeling, functions, statistics with inference, sensitivity | Requires stating and defending assumptions; data is incomplete by design |

T4 cases **must** include at least one quantity the student has to assume, with the assumption stated and justified. Modeling under missing data is the HS-band skill.

---

## 4. Standards binding

Each case ships with a `case.json` carrying:

```json
{
  "id": "cold-chain",
  "title": "Cold Chain",
  "tier": "T3",
  "band": ["MS-stretch", "HS-entry"],
  "primary_metric": "doses delivered within spec per dollar",
  "options": { "A": "...", "B": "..." },
  "margin_pct": 12.4,
  "standards": ["geometry-surface-area", "..."],
  "new_coverage": ["geometry-how-to-find-the-surface-area-of-a-rectangular-prism"],
  "sources": [ { "claim": "...", "value": "...", "url": "...", "confidence": "HIGH" } ]
}
```

- `standards[]` — every skill id the case exercises. Must exist in the spine.
- `new_coverage[]` — the subset that had `n == 0` before this case. **This is the reason the case exists.**
- `sources[]` — every externally-sourced number, with a URL and a confidence grade.

---

## 5. Hard lines (this project's own — see `00_SESSION.md` for graduation history)

- **Never fabricate a number.** Every figure in an appendix is either (a) cited to a real source, or (b) explicitly labeled as a stated scenario assumption in a `Modeling Assumptions` block. There is no third category.
- **Absent data is a first-class state.** If a needed figure cannot be sourced, the case either states it as an assumption *in the open* or the case design changes. It is never quietly invented.
- A number that is *plausible* is not the same as a number that is *true*. QA rejects plausible.
- Where a real-world source is contested or conflates categories, the case says so. (See: the "50% of vaccines wasted" figure — widely repeated, poorly sourced, excluded.)
- **A case citing a still-changing real entity states a fixed "as of" cutoff, everywhere.** An active athlete's career stats, a live market price, an ongoing company's headcount — anything real that keeps moving after the case is written is not a fixed number, it's a snapshot. State the cutoff date explicitly (a Modeling Assumption naming it), and freeze *every* number tied to that entity at the same date — not just the one figure that prompted the case, or a partial/incomplete slice of the most recent period. (LeBron vs. Michael originally froze one stat at an undisclosed, incomplete partial season while its accolade counts silently drifted to whatever was true "now" — two different, unstated cutoffs pretending to be one case. See `cases/lebron-vs-michael/case.json.correction_2026_08_04`.)

---

## 6. Sensitivity note on subject matter

The corpus includes a case (`Airstrike`) built on nuclear casualty counts, and others on end-of-life care and life insurance. Real stakes drive real engagement, and that is the point.

**Guidance, not prohibition:** a case may carry genuine weight, but the math must not require students to optimize human death tolls as an abstract quantity. Prefer framings where the stake is *protection* rather than *destruction* — doses delivered rather than casualties inflicted, structures saved rather than targets destroyed. Same rigor, same tension, better room.

Cases touching illness, death, money stress, or family hardship get a one-line facilitator note flagging it for the discussion lead.

---

## 7. The facilitator artifacts

*Derived from 39 Guide Notes documents across Y1–Y3 and the one full Socratic plan (Food Rationing, Y2 S7).*

A case study is **half a document and half a conversation.** The written case is the setup; the Socratic discussion is where the learning lands. Two facilitator artifacts ship with every case.

### 7.1 Guide Notes — the anchor ladder

The corpus converged on a five-anchor structure. Reproduce it.

```
Intro          — frame the format; name the opener
Launch         — video / article / image to set stakes
Anchor 1       — TAKE A STAND AND VOTE. No reasoning yet, just commit.
                 "Is anyone courageous enough to stand with ___?"
Anchor 2       — WHAT IS THE PROBLEM WE'RE SOLVING?
                 "Is this the right question?" · "What do you mean by A?"
                 → deliberately let confusion grow: "Wow, this is a challenging problem."
Anchor 3       — WHAT IS THE PROCESS?
                 "If we go through this process and find the data, how will we decide?"
                 → re-ask: "Is our question still the right question?"
Anchor 4       — WHAT DON'T WE KNOW?
                 "Do we need to make assumptions? Which ones are critical?"
Data Deep Dive — now, and only now, the numbers
Twist          — new information that breaks some models (see 7.2)
Close          — VOTE AGAIN. "Did we ask the right question?"
                 "What math was new to you, and how did you attack it?"
Lessons Learned
Standards Touched On
```

The pedagogical move is that **Anchors 2 and 3 come before the data.** Students want to compute immediately; the guide's job is to make them define the question first. `A Coach's Dilemma` records a discussion that spent 15 minutes before landing on the real question — and the guide treats that as the success, not the delay.

### 7.2 The Twist

At roughly the 15-minute mark, the facilitator introduces information that was withheld. It must **invalidate at least one popular position** without making any position obviously correct.

Food Rationing does this exactly right: a week passes, no rescue ship, two people's health deteriorates, and hidden emergency rations are discovered. Then: *"You now have 60 seconds. Are you changing your plan — or not?"*

The follow-up is the whole point: **"What just broke in your original model? Were you wrong — or just missing information?"** That distinction is the transferable skill.

A twist is **optional but strongly preferred.** Guide Notes may record `Twist: N/A`, and several do — but a case with a well-built twist produces a visibly better discussion. Authors should attempt one.

### 7.3 45-minute Socratic plan

Only one case in the corpus has a full timed plan. It should become standard, because it is the strongest single facilitator artifact in the whole set:

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote — no explanation |
| 3:00–10:00 | Position defense: *"Convince us why it's better, not just fair"* |
| 10:00–15:00 | Pressure-test the models: *"Whose plan is most fragile?"* |
| **15:00** | **DROP THE TWIST** — delivered slowly, with pauses |
| 15:00–20:00 | Immediate recommit: who reverses? *"What just broke?"* |
| 20:00–30:00 | Threaded deep conflict (2–3 named threads, e.g. optimization vs. fairness; probability thinking; role-based obligation) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

**Corpus state:** 40/56 cases have Guide Notes; 2/56 have a timed Socratic plan. Backfilling timed plans onto existing high-use cases is tracked in the gap queue as reconciliation work.

### 7.4 Cohort bands

A Socratic discussion built for 14 does not run the same way with 5, and a guide who has only ever run one cohort size will not know that until it fails live. Every case declares `cohort_bands[]` in `case.json`: named size ranges, with what changes at each.

**Minimum specification per case — three bands, at minimum:**

| Band | Typical size | What changes |
|---|---|---|
| **Full** | the size the case was authored for | the Socratic plan and Anchor timings run as written |
| **Compressed** | roughly half | Anchors 2–3 combine into one pass; the twist still drops but the "deep conflict" threads (§7.3, 20:00–30:00) drop to one thread instead of two or three; total runtime shortens proportionally, not the content |
| **1:1 / pair** | 1–2 learners | there is no vote to take, so Anchor 1 becomes a stated initial position instead; the guide plays devil's advocate directly rather than cold-calling; the twist still lands but "who reverses" becomes "would you reverse, and why" |

A case may declare more bands than this if its discussion genuinely needs finer steps, but three is the floor. **A case with no `cohort_bands[]` is a Tier 1 GAP** — it is being handed to whatever room shows up with no guidance on what to change.

**How a guide finds out the bands are wrong:** the RUN_REPORT (§Tier 3 of `case-readiness`) records the actual cohort size and band used for every dry-run. If a band's stated compression doesn't hold up in the room, that is exactly the kind of finding Tier 3 exists to surface — fix the band definition, not just the one session.

---

## 8. Definition of done

A case is publishable when:

- [ ] All seven structural sections present and conformant
- [ ] Overview contains zero load-bearing numbers
- [ ] Dilemma is binary and both options are named in Background
- [ ] Challenge sections 1, 2, 4, 5 are verbatim boilerplate
- [ ] Every appendix is referenced; no orphans
- [ ] Final appendix lines are all verbatim spine labels
- [ ] Balance test passed, margin recorded, both arguments written
- [ ] Every number cited or declared an assumption
- [ ] `case.json` validates; `new_coverage[]` is non-empty
- [ ] **Guide Notes** written to the §7.1 anchor ladder
- [ ] **Twist** authored, or `N/A` explicitly justified
- [ ] **45-minute Socratic plan** with timed moves (§7.3)
- [ ] **Cohort bands** declared, each with a size range and a note on what changes (§7.4)
- [ ] **Interactive HTML** published alongside the docx/xlsx packets — fresh, and never printing the `balance_test` verdict as a static literal (MCS-37)
- [ ] **Math vocabulary glossary** — every term the case uses is hoverable (plain-English definition) and clickable (a real, fetched-and-confirmed link to an allowlisted educational site), at least 8 terms (MCS-39)
