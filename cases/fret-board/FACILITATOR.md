# Fret Board — Facilitator Notes (draft, stage 2)

**Status:** draft at `case-write` time. Margin and cents figures below are placeholders until
`case-research` fills `case.md`'s `{{NEEDS_SOURCE}}` tokens; this file's job is to record the
*shape* of the argument now, while the balance is freshest in the writer's head, and be updated
in stage 3 with real numbers.

## Argument for A — the Precision Method

The Precision Method is definitionally exact: it *is* equal temperament, not an approximation of
it. At fret 12 — the octave point, where the string should stop at exactly half its open length —
the Precision Method lands there by construction. Its argument is that "close enough" is not a
luthiers' standard when a client's ear (and tuner) will notice drift compounding toward the
12th fret and above. A shop that wants every build to intonate cleanly across the whole neck,
including upper frets rarely used but always audible when they are, has a hard case for A
regardless of the extra time it costs at the bench.

## Argument for B — the Rule of Eighteen

The Rule of Eighteen is faster to mark by hand — a single division per fret against a shrinking
remaining length, no calculator required for four-decimal precision, no risk of a keystroke error
compounding across twelve entries. It is also the method that generations of working luthiers
actually used, on instruments that intonated well enough to be played professionally for
decades. Its argument is that the *actual* deviation it introduces, once converted to cents, may
sit well inside what any human ear (or even a clip-on tuner) can detect — in which case the
Precision Method's extra bench time buys accuracy nobody will ever hear, on a build with a real
five-day deadline.

## The margin

**Margin basis:** the 12th-fret cents-of-deviation figure from `case.md` Appendix D, compared
against the acceptable-intonation-tolerance figure in the same appendix (now filled by
`case-research`; see `RESEARCH_LOG.md` and `case.json.sources`/`modeling_assumptions`).

- Cents of deviation, Rule of Eighteen vs. true equal temperament at fret 12: **≈12.5 cents flat**
  (derived from Appendix B vs. Appendix C's 12th-fret lengths — 12.7500 in vs. 12.6573 in,
  25.5 in scale).
- Acceptable tolerance: **5 cents** (Modeling Assumption MA1 — no single hard published
  professional standard exists; 5 cents is a stated mid-point of the ~2–6 cent range that
  guitar-tech/luthier consensus and general pitch-JND research converge on).
- Verdict on whether B's drift crosses the tolerance line: **it does, by roughly 2.5×**, under
  MA1 as stated.

**This margin is NOT the close SPEC §2 race the case-write draft hoped for**, and that is worth
naming plainly rather than smoothing over: on the primary metric alone, once real numbers landed,
Option A wins decisively, not narrowly. Research turned up a real, important complication that
softens this without erasing it: the source establishing the historical rule-of-18 divisor (=18,
not the modern 17.817 refinement) also notes that working luthiers' *built* instruments have
historically intonated well "within human musical pitch discrimination" ranges in practice —
because bridge-saddle compensation, done at final setup regardless of which fret-marking method
was used, corrects for a chunk of this kind of systematic error. The case does not model bridge
compensation (that would be a redesign, not a research-stage fix), so the honest state of this
case is: **the primary metric alone is not close, but the real-world practice that makes Option B
survivable is genuinely more nuanced than the primary metric captures.** Flag this for
`case-qa`/human review before this case proceeds — either the case needs a redesign that makes the
metric itself closer (e.g., asking for deviation at an earlier fret, where the two methods are
closer together), or the case is reframed to make explicit that the dilemma's real tension is cost
and deadline against a *known, named, larger* accuracy cost, not a coin-flip on accuracy. Either is
legitimate; picking one is a `case-qa`-stage judgment call, not a `case-research`-stage one.

## Five Socratic questions

1. Your D3 cents-of-deviation figure at fret 12 — is that number bigger or smaller than you
   expected before you calculated it, and what does that tell you about why the Rule of Eighteen
   survived as a real shop method for so long?
2. If the Rule of Eighteen's drift crosses the acceptable-tolerance line in Appendix D, does it
   cross it at fret 12, or does your D1/D2 comparison show it crossing earlier — and if earlier,
   why does the case's primary metric only ask about fret 12?
3. Your D4 table shows some frets reducing to clean small-whole-number ratios and others not —
   what does a "nice" ratio actually correspond to on the instrument, and why would a luthier
   care about that independently of the cents-of-deviation question?
4. A week of unpaid rework is the cost of being wrong. How many extra minutes would the Precision
   Method have to cost Yuki, per fret, before that time cost alone would flip your recommendation
   toward Option B — even if B's cents-of-deviation were otherwise borderline?
5. The "Rule of Eighteen" is named for a whole number, but the real divisor luthiers use is not
   exactly 18. Why would a trade keep using a rounded nickname for over a century instead of
   correcting the name to match the number they actually use?

## The trap

The plausible wrong answer is treating "small rounding error" as automatically negligible because
the words "small" and "traditional" both sound reassuring. Heroes will be tempted to eyeball the
Rule of Eighteen's fret-position numbers, see they're close to the Precision Method's, and declare
B safe without ever computing the cents conversion in D3 — missing that cents is a logarithmic
(multiplicative) scale, not a linear one, so a length difference that looks tiny in inches can
still represent a musically audible number of cents, or conversely can look like "more error" in
raw inches at fret 12 than at fret 1 while actually representing the *same* proportional drift.
The case forces D3 specifically so no one can skip straight from "the numbers look close" to "the
methods are equivalent."

## Sensitivity note (SPEC §6)

None declared by the concept sheet, and the case as drafted does not introduce one: no quantity
here is contested in the way a wasted-vaccine statistic or a frozen athlete's stat line would be.
The one figure genuinely at risk of drifting between draft and research — the acceptable
intonation tolerance in cents — is flagged in Appendix D as likely to need a stated Modeling
Assumption rather than a single hard citation (per the concept sheet's own MEDIUM
data-feasibility call); if `case-research` cannot source it, state it as an assumption in the
open per SPEC §5, not as a fabricated tolerance.
