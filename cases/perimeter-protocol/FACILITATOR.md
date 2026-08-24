# Facilitator Notes — Perimeter Protocol

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices.*

**Status:** Numbers finalized after case-research. On the Traffic Sample (Appendix C, Table C-1):
Rule Set A (p OR q) blocks 10 of the 11 true threats present, at a cost of 6 false positives
(ratio 10/6 = 1.667). Rule Set B (p AND q) blocks 4 of the 11 true threats, at a cost of 2 false
positives (ratio 4/2 = 2.0). Margin on the primary metric = (2.0 − 1.667) / 2.0 = **16.7%,
favoring Rule Set B** — within SPEC §2's 20% cap. Do not reveal these counts to Heroes before
Challenge 3 is submitted; `case.md` deliberately withholds them so students classify the sample
themselves.

## Intro

Frame the format before the numbers: this is a one-shot approval decision under a hard deadline —
"You are Marcus Webb. It's 4:50 p.m. Friday. Two fully-tested firewall rule sets sit open in two
tabs. You have to approve one before tonight's deployment window opens, and it holds through the
weekend." Let that land before Launch.

## Launch

Put the two rule sets side by side with only the headline tradeoff visible: Rule Set A ("Broad
Net") catches more real threats but generates more false alarms; Rule Set B ("Narrow Gate")
generates far fewer false alarms but lets more real threats through. Ask for a gut read: "Same
firewall, same weekend. Which rule set do you approve?" Do not correct an early answer yet — that
instinct is exactly what the case is built to test.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who's with the tighter rule set, Rule Set B?" Show of hands, both options, no discussion. Record
the count for the Close re-vote.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What does 'better' mean here?"**

Let confusion grow here. Heroes will want to just ask which rule set catches more threats, and
stop there. Push: "Marcus isn't being asked which rule set is more aggressive. He's being asked
which rule set actually protects the network without drowning a two-person weekend crew." If the
room arrives at "we need to compare a ratio, not just a raw threat count" on its own, the case is
working.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has the right question, ask them to name the steps before opening Appendix C: build
truth tables for both block conditions (D1), classify every request in the Traffic Sample under
both rule sets (D2), work out the negation of Rule Set A's condition and see what it lets through
(D3), test the conditional statement's converse, inverse, and reversed-negated form against the sample (D4),
and total the triage cost against the analyst-hour pool to get each rule set's ratio (D5). Re-ask:
"Now that we can see the steps — is our question still the right one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the Modeling Assumptions block honestly: MA1 (the 20-analyst-hour weekend pool, a stated
scenario constraint), MA2 (the 20-request Traffic Sample itself, hand-built since no real
per-hospital firewall log could ever be published), and MA3 (15 analyst-minutes per false
positive, anchored to two real Ponemon Institute surveys but not a literal transfer of either
survey's own number). Ask which ones are actually load-bearing for the final recommendation — the
Modeling Assumptions table itself already flags all three "the answer is sensitive to this value."

## Data Deep Dive

Now, and only now, the numbers. Walk D1 (both truth tables) as a room, then split into two desks
for D2 (the classification table) and D3/D4 (negation and the converse/inverse/reversed-negated forms) before
reconvening to compare and for D5's ratio and margin.

**Facilitator-only arithmetic note.**

Rule Set A blocks 10/11 true threats at a cost of 6 false positives (ratio 1.667). Rule Set B
blocks 4/11 true threats at a cost of 2 false positives (ratio 2.0). Total weekend triage time:
Rule Set A costs 90 analyst-minutes (6 × 15), Rule Set B costs 30 analyst-minutes (2 × 15) — both
comfortably inside the 20-hour (1,200-minute) pool at this sample's scale. Margin, computed on
true-threats-blocked-per-false-positive: (2.0 − 1.667) / 2.0 = **16.7%** (`case.json.balance.margin_pct`).

## Twist

**Rule Set A's higher raw threats-blocked count is guaranteed by the logic before any data is even
looked at.** p OR q can never be satisfied less often than p AND q, so a Hero who reasons "A blocks
more threats, therefore A is the better rule" has not yet done any real math — that ranking was
true before the Traffic Sample existed. The twist fires the moment a Hero notices the real
question is not "which rule set blocks more threats" but "which rule set is more efficient per
false positive it costs the weekend crew" — and that this second question can only be answered by
actually classifying the sample and computing the ratio, which is exactly what flips the
recommendation toward the tighter rule set, Rule Set B.

## The trap

The obvious, confident wrong move is treating "catches more threats" and "is the better rule" as
the same claim. Rule Set A's superiority on raw threats-blocked is guaranteed by the OR/AND
structure before any data is even looked at — p OR q is never satisfied less often than p AND q.
Heroes who stop there will confidently recommend A without ever computing the ratio the case
actually asks for.

A second, subtler trap sits in D4: assuming the inverse of the watchlist conditional ("if not
listed, then not a threat") is true is exactly the reasoning that makes Rule Set B feel safer than
its own false-negative rate actually supports — the inverse is not logically guaranteed by the
original conditional, and the Traffic Sample shows at least one row (request 12–14, 17) where it
fails: unlisted IPs that are still genuine threats. A Hero who takes Rule Set B's low false-positive
count as proof it is "safe" without checking whether it is quietly relying on the inverse being
true has found a number, not the answer.

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" A room that voted the same way both times is worth pressing:
did they land on Rule Set B for the real reason — the ratio — or did they just guess right?

## Deep conflict — two threads (20:00–30:00)

1. **Raw threat coverage vs. per-alert efficiency.** Rule Set A guarantees it never misses a
   threat Rule Set B catches. Is a rule set that structurally can't be beaten on raw coverage ever
   the wrong call purely because it costs more analyst time, given the network protects a hospital?
2. **Fixed capacity vs. scaling risk.** Both rule sets fit comfortably inside the 20-hour pool at
   this sample's 20-request scale. Socratic Question 4 asks what happens if real weekend traffic
   volume were 100× larger — does that change which rule set is actually safer to run?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — headline tradeoff only, gut-check vote |
| 3:00–6:00 | Anchor 1 vote recorded |
| 6:00–9:00 | Anchor 2 — pressure-tests "better, measured how?" |
| 9:00–12:00 | Anchor 3 — name the five-deliverable process before opening Appendix C |
| 12:00–15:00 | Anchor 4 — surface MA1–MA3, ask which are load-bearing for the recommendation |
| **~15:00** | **TWIST drops** — Rule Set A's raw-coverage lead is guaranteed by logic, not evidence |
| 15:00–20:00 | Data Deep Dive — D1 (truth tables) worked as a room |
| 20:00–30:00 | Deep conflict — two threads (raw coverage vs. efficiency; fixed capacity vs. scaling risk) |
| 30:00–40:00 | Data Deep Dive continued — D2–D5 in two desks, reconvene for the shared comparison |
| 40:00–45:00 | Close, re-vote, reflection, lessons learned |

## Socratic questions

1. Rule Set A blocked 10 true threats against 6 false positives — Rule Set B blocked 4 against 2. Which ratio is actually better, and does "more threats caught" change your answer once you see the ratio?
2. You just triaged a false positive under D3's negation — Rule Set A let it through untouched. Was that outcome an accident of the rule, or exactly what the negation predicted?
3. In D4 you tested the inverse of "if watchlisted, then a genuine threat" against the Traffic Sample. Was the inverse actually true for every row — and if it wasn't, what is Rule Set B quietly assuming every time it lets an unlisted-but-unpatched request through?
4. Rule Set A's total weekend triage time is 90 minutes; Rule Set B's is 30 — both comfortably inside the 20-hour pool on this 20-request sample. If the real weekend's traffic volume were 100 times larger, which rule set hits the analyst-hour ceiling first, and what would you have to recommend then even if the per-false-positive ratio hadn't changed at all?
5. Rule Set A's true-threats-blocked count is guaranteed to be greater than or equal to Rule Set B's — that's a fact of the OR/AND structure, not something you had to measure. Given that, what quantity actually had to be measured before you could recommend one over the other?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes reached for the raw threats-blocked comparison first, and how much nudging it
  took to get to the ratio in D5.
- Whether the negation exercise (D3) was treated as a real check on Rule Set A's blind spot or as
  a box to tick before D4.
- Whether the converse/inverse/contrapositive analysis (D4) surfaced the inverse's failure on its
  own or needed a direct hint toward requests 12–14 and 17.

## Standards Touched On

Conjunction · Disjunction · Negation · Conditional Statement · Truth Table · Converse · Inverse ·
Contrapositive · How to construct a truth table for a compound statement · How to determine the
converse, inverse, and contrapositive of a conditional statement

## Facilitator note — margin stability (Tier 2 P5)

The recommendation is **not** stable under every plausible reading of the Traffic Sample (MA2).
Flexing any of the six p/q-category true-threat or false-positive counts by ±50% either flips the
winner to Rule Set A or pushes the margin past SPEC §2's 20% cap in Rule Set B's favor — most
notably, a -50% flex on the p-AND-q true-threat count or a +50% flex on its false-positive count
both flip the winner to Rule Set A outright. MA1 (the analyst-hour pool) and MA3 (minutes per
false positive) do not move the ratio at all — they only affect whether either rule set's triage
load fits inside the fixed weekend pool, which it comfortably does on this sample either way. See
`sensitivity_model.py`, `case.json.sensitivity_disclosure[]` (all Category F — genuinely
irreducible unknowns; no real per-hospital firewall log exists or could be published), and the
Tier 2 P5 probe result in `QA_REPORT.md`. This is disclosed, not hidden: the Modeling Assumptions
table already flags MA2 "the answer is sensitive to this value." If a Hero treats the 16.7% margin
as rock-solid, Anchor 4 exists specifically to surface this before the numbers are worked.

## Sensitivity note (SPEC §6)

Hospital/clinical framing (SPEC §6). Keep discussion anchored to the *access-control decision* —
Marcus is choosing between two rule sets, not responding to a breach. No named real hospital, no
real incident, no dwelling on patient harm. If a Hero pushes the framing toward "what if patients
died," redirect: "That's exactly why the false-positive cost matters too — a SOC that's drowning
in false alarms starts missing the real ones. Let's look at the ratio."
