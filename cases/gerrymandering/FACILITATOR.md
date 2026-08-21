# Guide Notes: Gerrymandering

**Case:** Gerrymandering · **Tier:** T3 · **Band:** MS-stretch / HS-entry · **Studio:** Adventure
**Standards:** see `case.json.standards[]` for the exact ids — percent, population/mean,
perimeter/area/circle-area, convex, and ratio/proportion

Legacy conversion, 2026-08-20, built from the original case study docx
(`source/Y3/Additional/Gerrymandering/Case Study_ Gerrymandering.docx`; no separate Guide Notes
document exists for this case — confirmed by directory listing) onto the current 11-anchor ladder.
The real premise (Idaho's incoming third congressional seat, the bipartisan Commission for
Reapportionment, the Treasure Valley's outsized population share, the efficiency-gap challenge) is
preserved from the source. The binary dilemma is not from the source — the original had no named
options at all — and is taken verbatim from the human-approved lock in
`cases/_concepts/LEGACY_DILEMMA_LOCKS_2026-08-20.md`.

**A note on political framing (read this before running the discussion).** An earlier draft of
this case's locked rationale named a specific political party as the beneficiary of one option.
That language was struck at lock-approval and does not appear anywhere in `case.md`, this file, or
`case.json` — both options are argued here in neutral political-geography terms only: compact/
whole-county vs. split-for-balance, and the legal packing/cracking standard. **If a discussion
participant tries to name which party benefits from Plan A or Plan B, redirect to the math:** ask
them to show the packing/cracking or population-deviation evidence for that claim using the case's
own numbers, not asserted priors. The case is legally and mathematically real either way — Idaho's
own redistricting criteria (Appendix A/C) apply regardless of who they're presumed to help.

## Intro

Frame the format: this is a real state's real redistricting choice, made by a commission that is
required by law to be evenly split by party — so the room's own vote, whatever the mix, mirrors
that structure. Name the opener: "Idaho is getting a third congressional seat. Two complete maps
are on the table. Neither map breaks the law on its face — but only one gets recommended tomorrow
at 9 a.m."

## Launch

Read the Overview aloud, then Background's three sentences on the two plans (Whole Valley intact
vs. Balanced Split), with no Appendix numbers shown yet. Ask: "Just from the names of these two
plans — which one sounds more like gerrymandering to you? Why?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who's recommending the Whole Valley Plan? Who's recommending the Balanced Split?" Show of hands,
no discussion yet. Record the count — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'fair'?"**

Push on what "avoiding gerrymandering" actually means here — Idaho's own criteria list four
different things at once (population equality, compactness, county integrity, non-dilution of
race/age/party groups) and the two plans trade off against each other on exactly those four.
"Is anyone courageous enough to say which one of these four criteria matters most — before we've
seen a single number?" Let the room sit in the ambiguity: "Wow, Idaho's own law doesn't rank these
for us either."

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked a working definition of "fair" (or at least ranked the four criteria),
ask them to name the actual steps: population-balance math (D1), compactness math (D2), the
efficiency-gap calculation (D3), and the demographic check (D4). Re-ask: "Given how we just ranked
those four criteria — is that still the right process, or does one deliverable now matter more
than the others?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the Appendix F Modeling Assumption out loud, as a group, before anyone computes anything:
the Balanced Split Plan's exact population-share line through the Treasure Valley is *not* a fixed
fact — it's a constructed dividing line the case-research stage had to state and justify. Ask: "If
that dividing line moved five percentage points, would your recommendation still hold?" (Facilitator
note: this is exactly what the Twist tests — let the room guess first.)

## Data Deep Dive

Now, and only now, the numbers. Walk D1's population-balance table together as a room, then D2's
compactness scores.

**The trap:** most Heroes will treat "compact" and "fair" as the same word — they'll see the Whole
Valley Plan's higher Polsby-Popper score, conclude it's obviously the less-gerrymandered map, and
never actually run the population-deviation math in D1. That's backwards from how courts actually
weigh these criteria: population equality is the *constitutional* requirement for congressional
districts (Appendix C) — compactness is a secondary, traditional-districting-principle factor
courts use as evidence of intent, not a hard rule with its own numeric threshold the way population
equality is. A student who leads with the map that "looks less gerrymandered" and never checks its
population-deviation number against Appendix C's stricter congressional-district standard has
skipped the one criterion the courts actually enforce first. Cold-call on this specifically: "Which
of these two legal tests is Idaho's constitution actually stricter about?"

## Twist — drop this at roughly the 15-minute mark

Deliver slowly, with pauses:

"Whichever plan you picked, go back and check your D3 efficiency-gap number against a neighbor who
picked the *other* plan. Compare them side by side. What do you notice?"

**Facilitator-only.** `case.json.balance.margin_pct` is `0.0` by disclosed design: D3's methodology
uses Modeling Assumption MA2 (every region's two-party vote share is assumed to match the real,
sourced statewide two-party split, since county-level 2020 vote data wasn't reprocessed this
research pass) — and under that assumption, the projected efficiency gap comes out **identical**
under Plan A and Plan B, because it's driven by vote share, not by which population is grouped into
which district. Heroes who did the arithmetic correctly should discover this themselves. This is
the real twist: **the metric they were told to compute (Appendix E) turns out not to distinguish
the two plans at all** — which means whichever plan they already argued for has to stand on D1
(population balance) and D2 (compactness), not on D3. Never reveal this before the room finds it —
ask instead: "If your D3 numbers came out the same for both plans, what does that tell you about
which of your other numbers is actually doing the work in your recommendation?"

Once the room has surfaced this, walk the *real* asymmetry: D1's population-deviation numbers
sharply favor the Balanced Split Plan (the intact Treasure Valley district is a fixed, real 18.44%
over Idaho's statewide ideal district population; a well-chosen split can bring every district
within a percentage point or two of ideal) — the one criterion federal courts scrutinize most
strictly for congressional maps (Appendix C, *Karcher v. Daggett*). D2's compactness numbers
(computed by each Hero from their own measured perimeter) should sharply favor the Whole Valley
Plan instead. Neither plan wins on every axis — that's the real dilemma, not the efficiency gap.

Ask: "You now have 60 seconds. Does this change your
recommendation — or not?" Then, the follow-up that matters more than the vote: **"What just broke
in your original model? Were you wrong about your plan — or just wrong about which of your own
numbers was actually carrying the argument?"**

**Twist soundness check (SPEC §6):** this twist introduces no new figure that contradicts an
earlier one — it names, out loud, a consequence of an assumption that was already disclosed in
`case.json.modeling_assumptions[]` (MA2), and asks the room to discover it by comparing their own
computed numbers. It holds under both a sequential read (Hero computes D3 before ever comparing
notes with someone who picked the other plan) and a simultaneous read (both plans' full numbers
laid out side by side).

## Immediate recommit

Re-vote immediately. "Did realizing D3 doesn't discriminate between the plans change your hand —
or did it just change *which numbers* you're now resting your hand on?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2 — is
'fair' actually one thing, or four things in tension?" And: "What math was new to you today, and
how did you attack it?"

## Lessons Learned

The source case's own framing treats "avoid gerrymandering" as a single instruction with no
worked-out tension inside it. This conversion's central lesson is that Idaho's own stated
redistricting criteria are not one test but (at least) four, and that a compact, whole-county map
and a population-balanced, split-county map can each satisfy some of those criteria while
straining another — "avoid gerrymandering" is not a single number to optimize, it's several
legal tests that do not always point the same direction. A second, transferable lesson: an
assumption that looks like a technical footnote (exactly where a population-split line falls) can
be the single most load-bearing number in the entire recommendation.

## Five Socratic Questions

Use these across Anchors 2–4 and the Data Deep Dive — each is answerable only with this case's own
numbers once `case-research` fills them in, not general opinion.

1. Your D1 population-balance table shows one district furthest from the statewide mean — which plan produces that district, and by how many percentage points does it miss?
2. Your D2 compactness scores favor one plan — does the plan with the higher Polsby-Popper score also win on population balance, or do the two criteria point at different plans?
3. Appendix C describes a stricter population-deviation standard for congressional districts than for state legislative ones — under that stricter standard, does your chosen plan actually pass?
4. Compare your D3 efficiency-gap number against a classmate who picked the other plan — are they actually different, and if not, why not, given the assumption Appendix E's methodology rests on?
5. Appendix A defines "packing" and "cracking" as the two technical forms gerrymandering takes — which of those two, if either, does your non-chosen plan more closely resemble, and what number from your own tables is your evidence?

## Standards Touched On

See `case.json.standards[]` and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: percent and percent-deviation arithmetic, population and mean (the "ideal"
district size), perimeter/area and the area of a circle (the Polsby-Popper compactness benchmark),
convex vs. concave classification, and ratio/proportion (apportioning a split county's votes and
population by the same share).

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** Anchors 2–3 run as written; the room splits into a "compactness/county-integrity"
  faction and a "population-balance" faction before the Twist forces everyone to hold both legal
  standards at once.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; D2's compactness score and D3's
  efficiency-gap calculation are worked as one shared worked example (one plan) instead of every
  Hero building both plans independently.
- **1:1 / pair (1–2):** No vote to take — Anchor 1 becomes a stated initial position instead of a
  cold-call show of hands; the guide plays devil's advocate directly, arguing whichever plan the
  Hero didn't pick.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's the fairer map, not just the less-gerrymandered-looking one" |
| 10:00–15:00 | Pressure-test the models: "Whose plan breaks first if the split-line assumption moves?" |
| **15:00** | **DROP THE TWIST** — the population-share assumption is not a fact, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict — two named threads: (1) compactness/county-integrity vs.
population-balance as competing legal criteria; (2) packing vs. cracking as the two technical forms
of the same underlying accusation, and which plan's shape resembles which |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |
