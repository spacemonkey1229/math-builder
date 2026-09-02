# Guide Notes: The Contrapositive Claim

**Case:** The Contrapositive Claim · **Tier:** T2 · **Band:** MS-core · **Studio:** Adventure
**Standards:** Conjunction / Disjunction / Negation / Conditional Statement / Truth Table / How to
construct a truth table for a compound statement / How to determine the converse, inverse, and
contrapositive of a conditional statement — see `case.json.standards[]` for the exact ids.

**Facilitator-only. Do not distribute to students.** The balance argument, the margin, and the
room's likely misstep live here and in `case.json`'s `balance` object — never in `case.md`.

**Balance flag, read before you facilitate.** Research is complete. `margin_pct = 16.7`, **Option
B (the Mirror-Image Standard) wins.** Appendix E's 14-row constructed log (Modeling Assumption
MA2): the Plain-Text Standard catches 6 of 14 wrongly-denied rows (42.9 per 100 appeals reviewed);
the Mirror-Image Standard catches 7 of 14 (50.0 per 100) — the one extra catch is the log's row 1
(the windstorm/roof-breach scenario lifted straight from this case's own Overview), where only the
Mirror-Image Standard's explicit non-flood-cause check catches an adjuster who labeled the loss
"flood" without addressing the wind-created opening in the reported facts. margin_pct =
100*(50.0-42.9)/42.9 = 16.7%, comfortably inside SPEC §2's ~20% cap. Full derivation in
`case.json` → `balance.margin_note`; full retune history (an earlier draft log produced a 100%
margin before Appendix E was expanded to 14 rows and rebalanced) in `RESEARCH_LOG.md` and
`case.json` → `modeling_assumptions[MA2].sensitivity`. **This margin is real but modest — do not
oversell Option B in the room; the two standards agree on 13 of Appendix E's 14 rows.**

## Argument for A — The Plain-Text Standard

The clause as written is a conditional the company itself filed and underwrote; applying it
literally requires no retraining, no new review step, and denies coverage in exactly the cases
where the stated antecedent (flood caused the damage) is actually true. Every claim it denies is
one the clause, read forward, plainly covers. Its exposure is entirely on the miss side: if an
adjuster reasoned from the clause's converse rather than its contrapositive, the Plain-Text
Standard's own audit rule has no mechanism to catch that error on appeal — it re-applies the same
literal rule the original adjuster already applied, so a converse-shaped denial that was wrong the
first time stays wrong on review too.

## Argument for B — The Mirror-Image Standard

A conditional and its contrapositive are logically equivalent — they share every row of a truth
table (D2) — so switching to the Mirror-Image Standard denies coverage in exactly the same true
cases as the Plain-Text Standard, while additionally re-examining every appeal through the one
logical form that is guaranteed not to smuggle in the converse error. If any meaningful share of
Appendix E's log reflects an adjuster reasoning "coverage was denied, so it must have been flood"
(the converse) rather than "flood caused the damage, so deny coverage" (the original clause), only
the Mirror-Image Standard's audit rule is structurally positioned to catch it on appeal. Its cost
is retraining time and a heavier per-file review burden — real, but bounded, and it buys down real
downstream legal exposure (Appendix D, CACI No. 2332 / *Hangarter v. Provident*) if a pattern of
wrongful denials would otherwise have gone uncaught.

## Five Socratic questions

1. Your D1 sheet gives you four rules built from the same p and q — the original clause, its converse, its inverse, and its contrapositive. Which two of those four are guaranteed to agree on every single appeal file, no matter what the file says, and how does D2 prove that without your having to check every row by hand?
2. Suppose an adjuster's stated reasoning is "coverage was denied, so it must have been flood." Which of D1's four rules is that adjuster actually applying — and is it the same rule as the one written in Appendix A?
3. Your D5 count treats every appeal in Appendix E the same way under whichever standard you're testing. Is there a row in that log where the Plain-Text Standard and the Mirror-Image Standard would classify the file identically — and if so, does that row tell you anything about which standard is really doing the work?
4. If Marisol picks the Mirror-Image Standard, does that change what the appeals team is allowed to conclude about a file where the reported facts are genuinely ambiguous — or does it only change which of the four D1 rules gets applied to the same facts?
5. D3 asks you to negate each of the four rules' conclusions. If negating the original clause gave you the same statement as its inverse, what would that tell you about the clause's antecedent and consequent — and is that ever actually true for a real conditional?

## The trap

Heroes will treat "the contrapositive" and "the opposite of the clause" as the same idea, and
conclude that switching standards means the appeals team starts approving claims it used to deny
(or vice versa) across the board. That is wrong on the logic: a conditional and its true
contrapositive are equivalent, not opposite — D2's truth table should show the Plain-Text Standard
and Mirror-Image Standard columns matching on every row where a hero built the contrapositive
correctly. The real, useful reframe is not "does switching flip decisions," it's "does switching
catch an adjuster who was silently applying the *converse* instead" — a different rule, built from
the same p and q, that is not equivalent to the original clause at all. A hero who conflates
"contrapositive" with "opposite" will misread D4's classification memo and may misclassify
Appendix E rows in exactly the direction the case is built to expose.

## Anchor ladder (SPEC §7.1)

### Intro

Frame the format: a real audit-standard memo Marisol has to send before her afternoon call, not a
worksheet. Name the opener: "You are Marisol Aguon. Two drafts of the standard sit open. Your
manager wants your call before the call."

### Launch

Read the Overview's closing lines aloud — "the clock in the corner of her screen just ticked
forward another minute" — and cold-call for a gut read on A vs. B, no truth tables yet: "Just from
that framing, which draft would you send?"

### Anchor 1 — Take a stand and vote

"Is anyone courageous enough to stand with the Plain-Text Standard — no retraining, no new
review step?" Count hands. "And the Mirror-Image Standard — logically equivalent, but a heavier
review?" Count hands. Record the split.

### Anchor 2 — What is the problem we're solving?

Let confusion grow. Heroes will want to jump to "which standard is more careful" — push instead:
"Is this actually about which rule is stricter, or about which rule can even detect a specific kind
of reasoning error?" The room should arrive at "we need to know whether the contrapositive and the
converse are the same thing" before Anchor 3.

### Anchor 3 — What is the process?

Walk the room toward: write the clause and its three logical relatives symbolically (D1), build one
truth table covering all four (D2), negate each rule's conclusion (D3), classify real appeal
scenarios against the table (D4), then count wrongly-denied claims caught per 100 appeals under
each standard (D5).

### Anchor 4 — What don't we know?

Surface honestly: MA0 (that adjusters have actually made this specific converse/contrapositive
error) is a stated scenario premise, not a documented finding — what's real is that the underlying
fallacies have formal legal names (Appendix D). Appendix E's entire 14-row log (MA2) is a
constructed dataset, not real appeal records. Ask: "Which of these, if untrue, would change your
Anchor 1 vote?"

### Data Deep Dive

Walk D1 through D5 together. Reveal Appendix E's real classification: Plain-Text catches 6 of 14
wrongly-denied rows (42.9 per 100), Mirror-Image catches 7 of 14 (50.0 per 100), a 16.7% margin.
Cold-call specifically for row 1 (the one row only Mirror-Image catches) and row 14 (the twist,
below) — a Hero who cannot explain *why* those two rows differ from the other 12 has not actually
understood the mechanism, just counted rows.

## Twist

**Appendix E, row 14.** Water staining is found inside an exterior wall shortly after a regional
storm — no active leak, opening, or standing water visible anywhere at the time of the appeal
review, and the reported facts name no specific point of entry. It looks, on its face, like
exactly the kind of file the Mirror-Image Standard's "actively check for a competing cause" habit
should catch. It doesn't: the true cause (a slow, unrelated plumbing pinhole leak) is only
discovered months later, during an unrelated remodel that happens to open the same wall — nothing
in the file available at review time disclosed it. Drop this after the room has convinced itself
Option B is simply "the more careful standard": row 14 shows that logical equivalence and an
explicit non-flood-cause checklist protect against the *converse/inverse reasoning error*
specifically (row 1's failure mode), not against every possible misjudgment on appeal. A file can
be genuinely ambiguous at review time regardless of which standard the reviewer was trained on —
neither Plain-Text nor Mirror-Image can classify a fact that is not yet in the file.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read the Overview's closing lines, cold-call for a gut read on A vs. B, no truth tables yet |
| 3:00–10:00 | Position defense — *"Convince us Marisol's team can trust your standard, not just that it feels more careful"* |
| 10:00–15:00 | Pressure-test the models — *"Whose standard is most fragile if the appeals log looked different?"* |
| 15:00 | Drop the twist once authored (see above) |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (equivalence vs. opposite; what a truth table proves vs. what a real file's ambiguity can't resolve) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?"

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Conjunction · Disjunction · Negation · Conditional Statement · Truth Table · How to construct a
truth table for a compound statement · How to determine the converse, inverse, and contrapositive
of a conditional statement

## Facilitator note — sensitivity (SPEC §6)

Mildly sensitive: this case turns on insurance claim denial, which touches a policyholder's home
and money. Keep the discussion on the audit-standard decision and the logic itself — never let it
drift into treating any specific real carrier named in Appendix B as having actually made this
error, and never frame the discussion around a real claimant's hardship. The scenario is
property/homeowners, deliberately not health or life, per the concept sheet's own sensitivity
guidance. Appendix D's adjacent-industry reference (health-insurance claim-review litigation) is
there only as real-world stakes context for why getting an audit standard right matters — do not
let the room conflate that separate, real litigation with anything alleged about Marisol's own
company.

## Facilitator note — the confusion premise is a stated assumption, not a documented fact

`case.json.modeling_assumptions[MA0]` records this explicitly: no documented real insurance
incident of an adjuster confusing a conditional's converse with its contrapositive was found in
research. What is real and citable is the underlying reasoning errors' formal names — "affirming
the consequent" and "denying the antecedent" — used in real appellate opinions. If a sharp Hero
asks "did this actually happen at a real insurer," the honest answer is no — this is a modeled
scenario built on a real, formally recognized category of reasoning error, not a reported incident.
Say so directly if asked; it does not weaken the case's math, which does not depend on the premise
being historically documented, only on it being logically well-formed.
