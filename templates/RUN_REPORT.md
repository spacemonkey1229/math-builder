# RUN REPORT — Tier 3 human dry-run gate

**Case:** ______________________  ·  **Template v1.0**
**Fill this in DURING the session and in the ten minutes after it. Not from memory.**

> **FACTS FIRST, IMPRESSIONS SECOND.**
> Sections 1–6 are facts. Sections 7–9 are opinion. Do them in that order, and do not skip
> ahead — an anchor that ran ten minutes late explains more about a flat discussion than any
> opinion about the case.

> **Return this even if the session went perfectly.** A clean run is the only evidence we have
> that the gate works. This case has cleared every machine check we own — seventeen structural
> checks and six simulated-play probes. What no simulation can test is a real room. Tier 3 exists
> because a kit in the sibling project passed all thirteen of its structural checks and all six of
> its simulated-play probes and *still* failed live, and the post-mortem could not tell whether
> the artifact or the facilitation was at fault. Section 8 is how we stop that happening here.

---

## 1 — The run

| | |
|---|---|
| Guide | |
| Date | |
| Case + tier | |
| Learners present | |
| **Cohort band used** (from `case.json.cohort_bands[]`) | |
| Planned length | |
| Actual length | |
| Anything you cut for time | |
| First time running this case? | Y / N |

---

## 2 — Execution fidelity (the important one)

Write the **real** clock time each move happened. If a move slipped, ran early, or got skipped,
say so. Do not write the planned time in the actual column.

| Planned | Move | **Actual** | Skipped / changed? |
|---|---|---|---|
| 0:00–3:00 | Launch + cold call | | |
| ~0:02 | **Anchor 1** — take a stand and vote (no reasoning) | | |
| 0:03–0:10 | **Anchor 2** — what is the problem we're solving? | | |
| | *Did you let the confusion grow, or rescue them?* | | |
| 0:10–0:15 | **Anchor 3** — what is the process? | | |
| | **Anchor 4** — what don't we know? | | |
| | **Data Deep Dive** — the numbers, and not before | | |
| **0:15** | **THE TWIST** | | |
| 0:15–0:20 | Immediate recommit — "what just broke?" | | |
| 0:20–0:30 | Deep conflict threads | | |
| 0:30–0:45 | Close, re-vote, lessons learned | | |

**Did the numbers reach the room before Anchor 2 and Anchor 3 were done?**  Y / N
If yes, say when and how — a data leak before the question is framed is the single most common
way this format fails, and it explains a disappointing session better than any critique of the
case.

**Which anchors did you actually reach?** Circle: 1 · 2 · 3 · 4 · Deep Dive · Twist · Close
**Which did you skip, and why (time / room / you judged it unnecessary)?**

---

## 3 — Solve clarity

| | |
|---|---|
| Anchor 1 vote (A / B / undecided) | ____ / ____ / ____ |
| Closing vote (A / B / undecided) | ____ / ____ / ____ |
| How many learners **moved**? | |
| First time anyone named the real question aloud | T+____ |
| Did anyone reach a defensible position **without doing the arithmetic**? | Y / N — who, and how |
| Did anyone walk into the trap the Guide Notes name? | Y / N — how many |
| Did anyone find a trap the Guide Notes do **not** name? | Y / N — what was it |
| Did any learner's number disagree with the Guide Notes? | Y / N — which number, whose was right |

> That last row is load-bearing. If a learner's arithmetic disagreed with the guide and the
> learner was right, that is a Tier 1/Tier 2 escape and it goes straight back to `case-readiness`.

---

## 4 — The twist

| | |
|---|---|
| Time dropped | T+____ |
| Was it a genuine surprise? | Y / N |
| How many learners changed position? | ____ of ____ |
| Did anyone change position and **say why**? | Y / N |
| Did the twist invalidate a position someone actually held? | Y / N — whose |
| Did anyone argue the twist doesn't change anything — and were they right? | |

If the twist landed flat, say which of these it was: delivered too fast · dropped too late ·
the room had already reached the conclusion it was supposed to break · the arithmetic didn't
actually move · nobody held the position it invalidates.

---

## 5 — Engagement

Mark each learner **A** (active — spoke with a reason), **T** (thin — spoke, didn't reason),
or **I** (idle — did not speak). This is the same measurement the simulated-play probes make,
so your answers sit directly against their predictions.

| Learner | Pre-twist (0–15) | Post-twist (15–30) | Close (30–45) | Note |
|---|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

**How many learners never spoke?** ____ of ____
**Did the same 2–3 voices carry the room?** Y / N

---

## 6 — Where the room stalled

| Moment | How long | What was happening |
|---|---|---|
| | | |
| | | |

**Where did it drag?**
**Where did it rush?**
**Was 45 minutes right for this case at this cohort size?** too short / right / too long

---

## 7 — What broke, and what you improvised

Every improvisation is a gap in the artifact that we would rather fix than have the next guide
reinvent. List what you had to make up on the spot.

1.
2.
3.

---

## 8 — DESIGN vs DELIVERY (do not skip this)

This section exists because a post-mortem in the sibling project could not tell whether the
artifact or the facilitation had failed, and so nothing could be fixed. Separate them here, while
it is fresh. **Being honest in the right-hand column is more useful than being right.**

| # | What went wrong | **The case was weak here** (artifact) | **I lost the room here** (delivery) | Can't tell |
|---|---|---|---|---|
| 1 | | ☐ | ☐ | ☐ |
| 2 | | ☐ | ☐ | ☐ |
| 3 | | ☐ | ☐ | ☐ |

For every row you marked **artifact**: what specifically would you change in the case document,
the appendices, or the Guide Notes?

For every row you marked **delivery**: what would you do differently next time you run it?

For every **can't tell**: what would you need to observe to decide? (This is the most valuable
row on the form. A "can't tell" that nobody writes down becomes a confident wrong attribution
three months later.)

**Would a different guide have had the same problem?** Y / N / don't know — and why.

---

## 9 — The three questions

- **Would you run this case again?** Y / N — and what would you change first?
- **Which single deliverable (D1…Dn) would you cut or rewrite?**
- **What did a learner say that stuck with you?**

---

## Filing

Save as `cases/<id>/runs/RUN_<YYYY-MM-DD>_<guide>.md`.

A filed RUN_REPORT is what moves a case from `PUBLISHED` to `VERIFIED`. Until one exists, the
case may be taught, but it **may not be marked ✅ in `DOCTRINE_LEDGER.md`** — per the ledger's own
rule, no ✅ without a QA report naming the case it was verified against, and Tier 3 is the only
tier that produces evidence from a real room.

**Sections 3, 4 and 8 feed back into `case-readiness`.** A trap the guide didn't name, a twist
that didn't fire, or a learner's arithmetic that beat the guide's is a Tier 1/Tier 2 escape and
re-opens the gate.
