# Research Log — downbeat-split

Stage: case-research. 12 open `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md`
(2 in Appendix A, 5 in Appendix B, 2 in Appendix C, 3 in Appendix D).

Before researching, re-read the case narrative closely: Appendix A's own prose already states
*"Larkspur Sound and this specific cue are invented for this case; the broadcast industry's
frame-accurate delivery requirement for ad spots is a real, standard practice this case models."*
That sentence sets the ceiling on what's sourceable here. Only one appendix (C, the AFM rate
card) claims to reproduce real published data. The other three appendices (A, B, D) describe
the specifics of one fictional cue at a fictional studio — a target duration, a phrase length, a
tempo, a subdivision unit, a rehearsal pace. No amount of searching finds "the broadcast slot
duration for Larkspur Sound's cue" because that thing does not exist outside this case. Those
had to be resolved as stated Modeling Assumptions, not as NOT-FOUND-after-search dead ends where
a real search was still owed and performed (see below) before making that call.

## P01/P02 — Appendix C: AFM session rehearsal rate + minimum call length (SOURCED)

**Searched:**
- "AFM Local 802 jingle rate scale 2026 rehearsal per hour"
- "American Federation of Musicians commercial announcement scale wages rehearsal minimum call"

**Found:** The AFM's national **Commercial Announcements Agreement (CAA) Signatory Packet**
(Version 2, 2023-09-29; original term June 2014–June 2017, indefinitely extended), hosted at
`afm47.org` under the AFM President's letterhead — a tier-1 primary-publisher document (the
union's own agreement text, not a third party's summary). Page 5, "Original Sessions / Standard
Recording Rates":

> "For a recording session, there shall be a minimum call session length of one (1) hour...
> Currently, the basic scale wage for an instrumentalist (called a 'Side Musician') for a
> minimum call session is **$133.01**. Each 20 minutes of overtime shall pay an additional
> one-third of the one-hour session fee (**$44.34**)."

- P01 (rehearsal rate): **$133.01 per one-hour minimum call** (Side Musician scale). Confidence
  **HIGH**. Caveat recorded in the source note: the CAA does not publish a distinct
  "rehearsal-only" line item separate from session-call pay — in-studio time (rehearsal and
  recording alike) is billed as one session call under this agreement, which is exactly the
  framing the case's own Appendix C intro uses ("used to anchor the cost side of the decision").
- P02 (minimum call length): **60 minutes (1 hour)**. Confidence **HIGH**, same source.

Rejected as a source: an older 2016 AFM national PDF (afm.org) turned up in search but was not
fetched, since the 2023 packet is the more current indefinitely-extended text and states the
same $133.01/1-hour figures are "currently" in force. A cross-check search for a possibly newer
CBA rate did not surface one; if a newer AFM CAA scale exists post-2023 it would supersede this
figure, so this should be re-verified before this case is reused past ~2027.

## P03–P12 — Appendices A, B, D (ASSUMPTION — 10 placeholders)

Each of these names a property of *this specific invented cue* (its length, tempo, phrase
structure, the client's target duration, the ensemble's subdivision habit, how long one
read-through takes). None of these are publicly documented facts — there is no real "Larkspur
Sound" session to look up. Per the skill's NOT-FOUND procedure this still required a genuine
attempt before concluding that: I ran two framings each for the two placeholders that could
plausibly have had a real-world anchor (target duration, subdivision unit) to make sure I wasn't
missing an actual industry-standard constant hiding in them:

- "standard broadcast commercial spot length seconds 15 30 60" — confirms :15/:30/:60 are the
  standard broadcast ad lengths (this is real and used as the *basis* for MA1's value), but does
  not give *this* client's exact frame-accurate figure, which is a private production spec by
  the case's own admission.
- "eighth note sixteenth note standard subdivision orchestral sight reading default" — confirms
  eighth-note (half-beat) subdivision is the conventional "straight" default in staff notation,
  used as the basis for MA8, but there is no published standard for what a specific ensemble's
  "normal" subdivision is — that is an arrangement-specific fact about this fictional ensemble.

Both came back NOT FOUND as specific figures, as expected, with a usable real-world *basis*
for the assumption. The other eight (session length, measures, phrase length, tempo, repeat
count, D2's fraction, minutes/read-through, minutes remaining) have no real-world anchor to
search for at all — they are pure scenario design — so no search was run for those; searching
"Larkspur Sound session length" would only return zero relevant results for a company invented
for this case.

All 10 are recorded as **Modeling Assumptions MA1–MA10** in Appendix E of `case.md`, each with a
basis and a sensitivity note per SPEC §5 / the skill's Exit 1. They were chosen to be internally
consistent so the case is solvable with exact fraction/mixed-number arithmetic:

- Phrase length 3¾ beats × tempo 1⅓ sec/beat = exactly 5 sec/phrase-repeat (clean mixed-number
  product, no rounding).
- 4 full repeats → Straight Cut's written total = 20 sec.
- D2's fraction 3/8 of the final phrase's 3¾ beats locates the cutoff at 20 + 1⅞ = 21⅞ sec —
  which is therefore MA1's target duration, so D1 and D2 chain together exactly with no residual
  fudge.
- Remaining session time 22½ min ÷ read-through length 2½ min = exactly 9 read-throughs (D4),
  and 2½ min × 9 = 22½ min (D5's Option B rehearsal-minute numerator) ÷ 1⅞ sec of accuracy gained
  = exactly 12 rehearsal-minutes/second — a clean final ratio.

This internal consistency is a case-design convenience, not a claim of realism, and is disclosed
as such in Appendix E. `case-qa` should still re-verify the full D1→D5 arithmetic chain
end-to-end; that reconciliation is a structural check beyond this stage's sourcing job.

## Verification

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources: []
```

## P13 — retune addendum: MA11/MA12 redelivery-risk probabilities (ASSUMPTION)

Added 2026-08-29 during a `case-write`-stage retune (see `QA_REPORT.md`): the original primary
metric ("rehearsal minutes required per second of timing accuracy gained") was structurally
unbalanceable — Option A's rehearsal-minute numerator is exactly zero by the case's own
construction, so any nonzero Option B cost computes to a 100% margin under SPEC §2's formula,
regardless of how the other ten assumptions are tuned. Retuned the primary metric to expected
total studio minutes (rehearsal minutes plus probability-weighted redelivery-risk minutes), which
required two new probability assumptions.

**Searched:**
- "broadcast commercial ad delivery rejected quality control frame accuracy percentage reject rate"
- "AFM recording session re-book re-record commercial jingle cost redo"

**Found:** No published rejection-rate data for broadcast frame-accuracy QC specifically (general
ad-platform rejection rates exist — e.g. Meta's ~8–12% ad-review rejection rate — but that measures
content-policy rejection, not frame-accurate broadcast delivery, and is not a usable analogue).
AFM sources confirm re-use/re-book fee structures exist but do not publish a "cost to redo an
entire session" figure distinct from a standard minimum call. Both searches came back NOT FOUND as
expected — this is the same "invented studio, no real record to look up" ceiling P03–P12 already
hit, extended to a new pair of quantities.

**Resolved as Modeling Assumptions MA11 (1/3) and MA12 (1/20)** — both grounded directly in the
case's own narrative rather than in outside data: MA11 (Straight Cut's rejection probability) is
set in line with the Twist already drafted in `FACILITATOR.md` (this exact type of tempo-compromise
take has already come back rejected once for this client), and MA12 (Downbeat Split's rejection
probability) is set well below MA11 because that option is rehearsed to an exact target across 9
full read-throughs before it is ever recorded, but deliberately not zero, since no live take is risk
free. The re-book session length reuses MA2 (90 minutes) rather than inventing a new figure — a
rejected take has to be re-booked as a full session, not a bare minimum call, per the Twist's own
"re-book the ensemble and re-cut the spot" framing.

## Next step

Run `case-qa` on `downbeat-split`.
