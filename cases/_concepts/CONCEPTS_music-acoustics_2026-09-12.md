# Concept sheet — Music, Sound & Acoustics (`music-acoustics`)

**Target and why (one line).** `readmodel/domains.json`'s `music-acoustics` entry is HIGH
authoring priority, MEDIUM data grade, and **0 existing cases** (`existing_cases: []`,
`n_uncovered_signature_skills: 0` against its own signature list) — the domain-level gap this
brief was asked to close.

**Scoring convention used here.** Per this session's spine-wide sweep, zero skills anywhere in
the 437-skill spine are at true `n==0`; I scored against `gap_queue.json`'s thin (`n<=2`)
convention and pulled every `n` live from `readmodel/standards_spine.json` on 2026-09-12 (values
below are current as of that read, not memorized).

**Prior art check — two cases already sit on this domain's math, unlabeled.** `cases_index.json`
lists `Fret Board` (a luthier deciding fret-cutting method, closing
`basic-operations-factor`/`greatest-common-factor`/`how-to-find-the-greatest-common-factor…`,
`advanced-operations-exponent-also-power`/`how-to-evaluate-an-exponential-expression`,
`measurement-ratio`/`how-to-find-equivalent-ratios` — none of which are thin, n=3 to n=8) and
`The Downbeat Split` (a broadcast audio engineer, closing
`fractions-how-to-divide-a-fraction-by-a-fraction` and `fractions-how-to-divide-fractions-and-mixed-numbers`,
both of which **are** thin at n=1/n=2 today — this case is already one of their two covering
cases). Neither is tagged to the `music-acoustics` domain field in its own `case.json` (both read
`"domain": null`), which is consistent with the domain's own `existing_cases: []`, but it means
any new concept here has to actively avoid re-treading their scenarios (fret geometry;
rhythmic-subdivision fraction arithmetic) even though the skill IDs aren't fully claimed. Each
concept below is checked against both.

| # | Concept | Score | Tier | Group(s) closed |
|---|---|---|---|---|
| C1 | The Wolf Interval | **6.2** | T3 | Basic Operations / Factoring (3/3 remaining gap) |
| C2 | The Absorption Call | **1.56** | T2 | Measurement / Units (1/1 remaining gap) |
| C3 | The Comb Filter | **0.96** | T3 | none fully closed |
| C4 | The Property Line | **0.0** | T2 | none |

**Recommendation.** Write **C1, The Wolf Interval** first. It fully closes Basic Operations /
Factoring's entire remaining gap (`prime`, `composite`, `how-to-factor-a-number` — the group's
3-of-6 thin skills) through a genuine number-theory argument (why the Pythagorean comma can never
close to exactly zero), not a bolted-on vocabulary detour, and its core math needs no external
dataset at all — it is the one concept in this sheet whose feasibility is HIGH without caveats.
**C2** is the domain's own headline room-acoustics archetype and is worth writing second even at
a modest score — the score is capped low honestly because it only reaches one thin skill
(`measurement-volume`, the sole remaining gap in Measurement/Units), and Sabine's formula genuinely
needs it. **C4** (Philadelphia's real 70 dB property-line ordinance) has the single most concretely
verified real-world number in this whole sheet but closes zero thin skills — it is a fine breadth
case someday, not a gap-closing one; do not write it under this brief. **Kill C3** for now unless a
trig-branch case is specifically wanted: it deliberately declines to claim `tangent-function` (not
genuinely forced), so it only reaches 2 of the Trig Functions group's 3 thin skills, and its
concrete numbers (mic spacing, source distance) are a stated scenario, not sourced data.

---

### C1 — The Wolf Interval   ·   score 6.2   ·   tier T3

**Protagonist.** Iris Callahan, a harpsichord builder and tuner who tunes each instrument by hand
before it ships and has to pick one temperament before the customer's first lesson.

**The dilemma.** A.) Tune the harpsichord in just intonation — pure, beat-free thirds and fifths
in the instrument's home key, but at least one interval (the "wolf") will sound audibly sour in
distant keys OR B.) tune it in 12-tone equal temperament — every key equally usable, but no
interval anywhere is perfectly pure. (This is `domains.json` music-acoustics's own decision
archetype #1, verbatim.)

**Primary metric.** Fraction of a semitone of mistuning, averaged across all 12 major keys the
instrument must support (a ratio — total mistuning divided by number of keys — not a raw cents
count, because a comma that is huge in one key and zero in eleven others is a different design
problem than one spread evenly).

**Why it's close.** Just intonation makes the home key perfect and every other key worse, in some
cases unplayably so — a real tradeoff if the customer only ever plays in one key, a real problem
if they don't. Equal temperament is the industry default for exactly this reason, but Iris's
customer is a period-performance early-music group that specifically wants the purer home-key
sound. The mathematical heart of the case is *why there has to be a wolf at all*: stack twelve
pure fifths (each a 3/2 frequency ratio) and you should reach seven octaves (each a 2/1 ratio) —
but (3/2)^12 ÷ 2^7 ≈ 1.0136, not 1. That gap, the Pythagorean comma, is provably never zero
because 3 and 2 share no common prime factor — no power of 3 can ever equal a power of 2. That is
a genuine, forced argument from prime factorization, not a decorative label.

**Would close (5 skills, 3 how-to / 2 term):**

| id | kind | label | n |
|---|---|---|---|
| basic-operations-prime | term | Prime | 2 |
| basic-operations-composite | term | Composite | 2 |
| basic-operations-how-to-factor-a-number | how-to | How to factor a number | 2 |
| fractions-how-to-divide-a-fraction-by-a-whole-number | how-to | How to divide a fraction by a whole number | 1 |
| fractions-how-to-divide-a-whole-number-by-a-fraction | how-to | How to divide a whole number by a fraction | 1 |

Group closure: the first three are **all three** of Basic Operations/Factoring's remaining thin
skills (`n_gap` 3/6 in `gap_queue.json`) → full-group bonus. The two division-of-fractions skills
are deliberately the two **not** already used by `The Downbeat Split` (which covers
`divide-a-fraction-by-a-fraction` and `divide-fractions-and-mixed-numbers`); this case adds first
coverage to the other two members of that same still-thin group (octave ratio 2 ÷ fifth-squared
ratio 9/4 = whole-number-by-fraction; the comma fraction ÷ a whole-number octave count =
fraction-by-whole-number) rather than re-treading the two skills that case already forces.

raw = (0.6+0.6) [terms] + (1.0×3) [how-tos] = 4.2 · group_bonus = +2.0 (Factoring, full) · **total
6.2** · availability HIGH (×1.0) → **score 6.2**

**Already-covered skills it also exercises.** `advanced-operations-exponent-also-power` (n=8) and
`advanced-operations-how-to-evaluate-an-exponential-expression` (n=8) — computing (3/2)^12 and 2^7;
`fractions-how-to-multiply-two-fractions` (n=2, thin but not claimed toward score since it's a
supporting step, not a skill the case's own deliverable is built around) — stacking the fifths.

**Data feasibility: HIGH.** The interval math needs no external dataset — it is arithmetic on
defined ratios, exactly as `domains.json`'s own note says ("Interval ratios and equal-temperament
frequencies are mathematics, not data, and need no citation beyond a definition"). Live-checked
this session: Wikipedia's "Piano key frequencies" page and Wikipedia's "12 equal temperament" /
"Twelfth root of two" pages publish the standard A4=440Hz equal-tempered frequency table and the
2^(1/12) derivation — real, stable, citable background for the how-it-differs-from-just-intonation
framing, even though the comma calculation itself doesn't depend on them.
Not confident about: a real, named harpsichord customer or shop — this stays a constructed
scenario (stated as such), which is fine per SPEC since no number in it is fabricated data.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None — 5 skills, one coherent arc (stack ratios → compute the gap → explain why it
can't vanish → apply to the tuning decision).

---

### C2 — The Absorption Call   ·   score 1.56   ·   tier T2

**Protagonist.** Marcus Oyelaran, an acoustic consultant hired by a community theater to fix a
"boomy" black-box space before a run of amplified shows.

**The dilemma.** A.) Treat the rear wall with absorptive panels to kill the echo and shorten
reverberation time, favoring speech clarity OR B.) treat it with diffusive panels that scatter
sound instead of killing it, preserving the room's "liveness" for the unamplified acoustic sets on
the same calendar. (`domains.json` music-acoustics's decision archetype #2, verbatim.)

**Primary metric.** Ratio of achieved RT60 (seconds) to the room's target RT60 for its dominant
use (speech vs. music) — a ratio, not a raw seconds figure, because "1.4 seconds" means something
different in a lecture hall than a black-box theater.

**Why it's close.** Sabine's equation, RT60 = 0.161 V / A (V = room volume in m³, A = total
absorption in metric sabins), makes the tradeoff mechanical once volume is fixed: absorptive
treatment adds sabins fast and shortens RT60, cheaply solving the speech problem — but the same
treatment kills the room for unamplified music, where the theater's other bookings need some
liveness. Diffusive treatment redistributes reflections instead of removing them, keeping RT60
closer to its current value while (a claim the case must qualify, not assert as fact) improving
perceived clarity — the two options are not simply "more treatment vs. less," they trade an easy
number (RT60 via Sabine) against a harder-to-quantify one (subjective liveness), which is exactly
where the Socratic discussion should land.

**Would close (1 skill, 1 term):**

| id | kind | label | n |
|---|---|---|---|
| measurement-volume | term | Volume | 2 |

Group closure: this is Measurement/Units's **only** remaining thin skill (`n_gap` 1/9 in
`gap_queue.json`) → full-group bonus.

raw = 0.6 (term) · group_bonus = +2.0 (Units, full) · total 2.6 · availability **MEDIUM** (×0.6) →
**score 1.56**

**Already-covered skills it also exercises.** Room surface-area skills from
Geometry/Surface Area And Volume (already thickly covered by other cases, not thin);
`measurement-how-to-convert-an-amount-with-compound-units` (n=18, sabins per square meter).

**Data feasibility: MEDIUM — honestly, not HIGH.** Live-checked this session:
`acoustics-engineering.com/html/sabin.html` confirms Sabine's formula publicly (T = 0.161 V/A) but
does **not** itself publish a usable absorption-coefficient table — it links out to
manufacturer-specific downloadable databases (Isover, Rockfon, OWA) in a proprietary
MS-Access-style format, not a simple public table. A ResearchGate paper on Sabine/Eyring equations
does cite specific audience-absorption coefficients (0.56–0.86) but sits behind a paper, not a
clean public page. This matches `domains.json`'s own note exactly: build the case on the formula
with **stated** absorption coefficients drawn from whatever published table `case-research` can
actually pin down (a university acoustics course PDF or a single manufacturer spec sheet is the
likeliest fit), not a promise of one clean government-style dataset. A specific *named* real hall's
published RT60 (e.g., Boston Symphony Hall is widely reported around 1.8–1.9s occupied, mid-band)
is citable as color/context but should not be the case's own room, since the theater in the
dilemma is fictional by necessity — no real theater will have "Option A vs. Option B" pre-computed
for it.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None — narrow, single-skill claim by design.

---

### C3 — The Comb Filter   ·   score 0.96   ·   tier T3

**Protagonist.** Priya Nakamura, a recording engineer tracking a jazz combo live in one room, who
has thirty minutes left in a booked session to commit to a mic setup.

**The dilemma.** A.) Close-mic every instrument separately — clean, isolated tracks, but a dry
sound the mix engineer will have to fake room ambience onto later OR B.) add a spaced pair of room
mics for natural ambience — richer sound, but if the room mics' distances from the source aren't
matched to the close mics within a fraction of a wavelength, summing the signals causes comb-filter
cancellation that can hollow out or kill specific frequencies entirely.

**Primary metric.** Path-length difference between the two mic signals, expressed as a fraction of
the wavelength of the frequency in question (a dimensionless ratio) — because whether that ratio
lands near a whole number (reinforcement) or a half-integer (cancellation) is what actually
determines the sound, not the raw distance in feet.

**Why it's close.** Option A is safe but flat; Option B can sound noticeably better *or* audibly
broken depending on a few centimeters of mic placement, and Priya doesn't have time to solve it by
trial and error for every frequency — she has to reason about which frequency band a given path
difference will damage, using the phase angle (360° × path-difference/wavelength) read off the
unit circle: a whole-cycle phase difference reinforces, a half-cycle difference cancels.

**Would close (2 skills, 1 how-to / 1 term):**

| id | kind | label | n |
|---|---|---|---|
| pre-calculus-unit-circle | term | Unit Circle | 2 |
| pre-calculus-how-to-find-the-sine-cosine-and-tangent-of-an-angle-using-the-unit-circle | how-to | How to find the sine, cosine, and tangent of an angle using the unit circle | 2 |

`pre-calculus-tangent-function` (n=2, also thin, also in this group) is **deliberately not
claimed** — nothing in a phase-cancellation argument forces a tangent value; only the sine/cosine
(amplitude of constructive/destructive interference) matters, and claiming tangent just to
inflate the group closure would be exactly the vocabulary-stuffing the parent skill warns against.
Because of that omission, this does **not** close the remaining Trig Functions gap (2 of its 3
thin skills, not 3 of 3) — no group bonus.

raw = 0.6 (term) + 1.0 (how-to) = 1.6 · no group bonus · availability **MEDIUM** (×0.6) →
**score 0.96**

**Already-covered skills it also exercises.** `pre-calculus-sine-function` / `amplitude` /
`period-of-a-function` (all already-covered, n=3 each) — modeling the waveform itself;
`measurement-how-to-convert-an-amount-with-compound-units` (n=18, converting mic distance and the
speed of sound, ~343 m/s, into a wavelength).

**Data feasibility: MEDIUM.** The speed of sound in air is a stable, uncontested physics constant
needing no citation. But the case's actual numbers (mic distances, which frequency is examined)
have to be a stated recording scenario, not a real dataset — there is no public "session log" to
cite. Feasibility for the underlying physics is HIGH; feasibility for the case's specific numbers
is closer to "modeling assumption," which is why this is graded MEDIUM overall rather than HIGH.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None.

---

### C4 — The Property Line   ·   score 0.0   ·   tier T2

**Protagonist.** Devon Ashworth, the production manager for an outdoor summer concert series,
laying out the stage and delay-tower plan two weeks before a show with a strict municipal noise
permit.

**The dilemma.** A.) Angle the stage and main speaker stacks toward the open field, requiring a
long cable run to the front-of-house mix position OR B.) angle the stage toward the parking lot
side, with a much shorter cable run, but aiming more direct sound energy toward the nearest
residential property line and its decibel limit.

**Primary metric.** Extra cable-run cost per decibel of margin kept under the property-line limit
(dollars per dB) — a ratio that forces comparing a fixed infrastructure cost against a regulatory
cushion, not just "which orientation is cheaper."

**Why it's close.** The short-run option (B) saves real, quantifiable cable and labor cost, but
sound level falls off with distance (each doubling of distance from the source roughly halves
sound intensity), so orienting toward the closer property line eats into the legal margin faster
than intuition suggests; the long-run option (A) costs more upfront but buys a much larger, safer
buffer. Whether the cable savings are worth the shrunk margin is genuinely a judgment call once
both numbers are in front of the reader.

**Would close (0 thin skills).** This concept, honestly scored, closes no skill at `n<=2`. It
exercises `measurement-ratio`/`proportion` (n=27/20), `measurement-how-to-convert-an-amount-with-compound-units`
(n=18), and `geometry-angle` (n=3) — all already well-covered. raw = 0 · **score 0.0**, regardless
of availability grade.

**Data feasibility: HIGH (for what it's worth).** Live-checked this session: Philadelphia's actual
noise ordinance (`phila.gov`, Chapter 10-400, also mirrored at `nonoise.org`) sets a real, specific,
citable 70 dB limit measured at the property boundary for a concert venue over 1,000 seats — one
of the most concretely verifiable real-world numbers checked for this entire brief. That
feasibility strength does not translate into a gap-closing score; it is a good breadth case for a
future non-gap-driven authoring pass, not this brief's target.

**Sensitivity (SPEC §6).** None required.

**Split risk.** N/A — not recommended for this round regardless.
