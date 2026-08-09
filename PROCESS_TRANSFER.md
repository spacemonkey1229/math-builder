# Process Transfer — What HIGH GRADE Taught This Project

**Source:** the *HIGH GRADE — Murder at the Elkhorn Grand* production kit (23 players, v1.5, 165 artifacts)
**Why it transfers:** both are systems for producing a **facilitated group experience from a printed packet**, where the artifact and the facilitation can each fail independently, and where a designer who knows the answer cannot evaluate whether a fresh participant will find it.

---

## The seven patterns adopted

### 1. Canon, and the continuity bug

HIGH GRADE has a **Canon** — one versioned document that is the single source of truth for the world, the killer, the method. Everything else derives from it. When the killer changed from Adelaide to Rourke at v1.2, three documents never got the memo and kept convicting Adelaide. The workplan calls this out as a **continuity bug** and makes fixing it Phase 0, a hard prerequisite: *"everything downstream must encode the Rourke solution, so the stale docs get fixed before we build on them."*

**Adopted as:** `case.md` is the case of record. `FACILITATOR.md`, the workbook and the published `.docx` all derive from it. Tier 1 checks T1-14/15 sweep every number in the Guide Notes and every cell in the `.xlsx` and fail if they disagree with the case.

**It fired immediately.** Cold Chain's workbook was built 22 minutes before the last edit to `case.md`. That is exactly the Adelaide bug, in a spreadsheet.

### 2. Design layer vs. production layer

*"The design is done; the kit is not."* HIGH GRADE separates the creative bible from the stack of paper a host actually prints, and tracks them as different completion states.

**Adopted as:** a case is not done when `case.md` is good. It is done when the packet, the guide notes, the timed Socratic plan, the workbook and the tracker record all exist and agree. The gate states — `DRAFT → TIER1_PASS → TIER2_PASS → PUBLISHED → VERIFIED` — encode the distinction.

### 3. The Cold Solve packet

The strongest single idea in the kit. HIGH GRADE hands fresh readers **only what a player sees** and asks: can they convict Rourke *for the right reasons*, and get past the Adelaide trap?

Note the three-part test. Not "did they get it right" — **right answer, right reasons, past the trap.** A solver who convicts Rourke by coin flip has failed.

**Adopted as:** Tier 2 probe 1. A genuinely fresh subagent, given only the student packet, with no facilitator context.

**It fired immediately.** Three independent fresh readers each derived a *different* in-spec dose total, all defensible, none matching the case's published 7,771 — because two allocation conventions were never written down. The author could not have seen this. Only a cold reader could.

### 4. The tier ladder, and why Tier 3 cannot be skipped

The Beta Host Report opens with the most useful sentence in the entire kit:

> *"This kit has cleared every machine gate we have — all thirteen structural checks and all six simulated-play probes. What no simulation can test is a real room. The last time HIGH GRADE was run live it failed on two things the machine checks called fine."*

**Adopted as:** Tier 1 (structural, machine) → Tier 2 (simulated play) → Tier 3 (human dry-run). A case may be **PUBLISHED** on Tiers 1–2. It may only be **VERIFIED** — and therefore only earn a ✅ in the doctrine ledger — after a guide has run it with real learners and filed a report.

**Current honest state: no case is VERIFIED.** Cold Chain has not been run with learners. That is the largest gap in this project and it is the exact gap HIGH GRADE says matters most.

### 5. Facts first, impressions second

The Beta Host Report demands a release-timing table before it will accept a single opinion, because *"an early leak here explains more about a disappointing night than any opinion about the plot."*

**Adopted as:** `templates/RUN_REPORT.md` opens with timings, cohort size and band, when the twist landed, which anchors were reached, and where the room stalled — all recorded *during* the session, "not from memory." Impressions come after, and are clearly labelled as such.

### 6. The design-vs-delivery attribution problem

HIGH GRADE's post-mortem *"could not tell whether the design or the hosting was at fault, because nobody had written down what actually happened when."*

This is the deepest pattern here. A bad discussion has two possible causes and they call for opposite responses: fix the case, or coach the guide. Conflating them means iterating on the wrong thing forever.

**Adopted as:** RUN_REPORT has an explicit attribution table with three columns — *the case was weak here* / *I lost the room here* / **can't tell**. The third column is the important one. An honest "can't tell" is a signal to instrument that moment better next time.

### 7. Bands

HIGH GRADE scales 23 → 12 players with named bands (19–23 / 16–18 / 12–15) and documented role cuts.

**Adopted as:** cases should declare `cohort_bands[]` — a Socratic discussion built for 14 does not work with 5. Tier 1 currently flags Cold Chain's absence of bands as a GAP. **Not yet designed properly**; see the roadmap.

---

## Two patterns not yet adopted, and worth it

**The engineered herring.** Adelaide is a *deliberately constructed* wrong answer with real supporting evidence — not an accident, a designed trap. Cold Chain has a trap ("optimize total doses and never notice you dropped two villages") but it was noticed during authoring rather than engineered from the start. HIGH GRADE builds the herring first and the truth around it. Worth trying: design the seductive wrong answer *before* the right one.

**Powers and information rights.** Each character booklet specifies what that player knows, may reveal, and must conceal. There is no case-study analogue yet, but there could be: a **jigsaw variant** where different Heroes receive different appendices and must combine them. That turns a solo case into a genuinely collaborative one, and it is the single most interesting unexplored idea in the transfer.

---

## What does *not* transfer

HIGH GRADE is a closed system with a correct answer. A case study is deliberately open — SPEC §2 requires that both options remain defensible, and the Socratic discussion exists precisely because there is no key. So the Cold Solve probe cannot ask *"did they get it right."* It asks **"could a fresh reader reach a defensible position, and did the case give them what they needed to defend it?"**

The failure mode being hunted is inverted, too. HIGH GRADE fails when the mystery is unsolvable. A case study fails when it is **too solvable** — when one option wins by a mile and the room has nothing to argue about.
