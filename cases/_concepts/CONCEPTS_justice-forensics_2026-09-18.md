# Concepts — Law, Forensics & Criminal Justice — 2026-09-18

Target picked: **Statistics And Probability / Probability** (`independent-event` n=2, `permutation`
n=2, its how-to n=2, `how-to-determine-the-number-of-outcomes-of-a-combination` n=2) plus
**Statistics And Probability / Sampling And Experiments** (`multistage-sampling` n=2,
`convenience-sampling` n=3). Cross-checked against `readmodel/domains.json`'s `justice-forensics`
entry: every one of its 12 listed `signature_skills` already sits at `n>=2` in the live spine (not
`n=0` as the domain sheet's own `uncovered_signature_skills` field suggests at a glance — that
field is empty, meaning the *signature* list is fully covered, but several adjacent
**Probability**-group skills the signature list doesn't name are still genuinely thin). A live
spine query (`n==0` across the whole 322-skill spine) returned **zero** skills — the corpus has no
true zero-coverage skill left as of this run, so per `skills/case-readiness/SKILL.md`'s
"reinforcement carve-out," any freshly-authored case today legitimately records an empty
`new_coverage[]` with a `reinforcement_note`, provided the case genuinely forces thin (`n<=3`)
skills rather than padding already-saturated ones. Rank below reflects that reality.

| Concept | Score | Tier | Thin skills forced (n<=3) |
|---|---|---|---|
| **C1 — The Cold Hit** | 7.4 | T3 | 6 |
| C2 — The Overtime Sweep | 5.1 | T2 | 3 |
| C3 — The Ballistics Backlog | 4.6 | T2 | 2 |

**Recommendation:** write **C1 — The Cold Hit**. It is the only concept that closes the full
Probability-group thin cluster (`independent-event`, `permutation` + its how-to,
`how-to-determine-the-number-of-outcomes-of-a-combination`) *and* the Sampling-group cluster
(`multistage-sampling`, `convenience-sampling`) with every one of those six skills genuinely forced
by a deliverable — not just plausible-sounding. It also maps directly onto
`domains.json`'s own decision archetype #1 ("Charge on the DNA database hit alone, or hold for
corroborating evidence, given the database size"), so the protagonist's job and stakes are the
domain's own framing, not an invented analogy. Kill C3 (Ballistics Backlog) — its combinatorics
use (ordering which of 4 backlogged case types to run first) turned out to be decorative once
sketched; the case doesn't actually need it to reach its decision, which is the "coverage inflation"
trap this file's scoring rubric warns against.

---

### C1 — The Cold Hit   ·   score 7.4   ·   tier T3

**Protagonist.** Dana Osei, forensic statistician at a state crime laboratory's DNA unit. She
signs the report that goes to the district attorney's office; her name is the one a defense
expert cross-examines if the case goes to trial.

**The dilemma.** A.) Refer the case for charging as soon as the offender-database search returns
a cold hit whose random-match probability clears the lab's stated reporting threshold (fast — the
case moves to the DA immediately) OR B.) Hold the referral until at least one independent
corroborating step (a second, non-DNA evidentiary check) closes, which consumes detective-hours
but essentially eliminates the risk of referring on database coincidence alone.

**Primary metric.** Correctly-resolved cold-hit cases per detective-hour of lab-and-investigator
time (a case that is later kicked back for insufficient corroboration burns far more hours in
rework than the corroboration step itself would have cost up front — that's what makes the ratio,
not the raw count, the real quantity Dana is optimizing).

**Why it's close.** Option A clears cases fastest per case *when the database is small enough*
that a coincidental match is rare — every hour spent on mandatory corroboration is an hour not
spent clearing the next case in the backlog. But the expected number of coincidental
(non-contributor) matches in a database search scales with database size × the profile's random
match probability — that's a direct multiplication-of-independent-events calculation — and a
crime lab's searchable database has grown by orders of magnitude over the CODIS program's
history, which is real, citable, and directly changes which option wins. The two options trade
detective-hours (B's fixed cost per case) against rework-hours (A's cost only when a referred hit
turns out to be a coincidence) — genuinely close once real database-size and rework-time figures
are found.

**Would close (6 skills, 4 how-to / 2 term, all n<=2-3):**

| id | kind | label | n |
|---|---|---|---|
| statistics-and-probability-independent-event | term | Independent Event | 2 |
| statistics-and-probability-permutation | term | Permutation | 2 |
| statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation | how-to | How to determine the number of outcomes of a permutation | 2 |
| statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination | how-to | How to determine the number of outcomes of a combination | 2 |
| statistics-and-probability-multistage-sampling | term | Multistage Sampling | 2 |
| statistics-and-probability-convenience-sampling | term | Convenience Sampling | 3 |

**Already-covered skills it also exercises (reinforcing, not scored):**
`statistics-and-probability-conditional-probability`,
`statistics-and-probability-how-to-determine-the-probability-of-conditional-events`,
`statistics-and-probability-how-to-determine-the-probability-of-a-compound-event`,
`statistics-and-probability-population`, `statistics-and-probability-sample`,
`statistics-and-probability-random`, `advanced-numbers-how-to-find-the-percent-of-a-number`.

**Data feasibility: HIGH.** Named sources I expect to exist: FBI CODIS program's own published
"CODIS-NDIS Statistics" page (offender/arrestee profile counts by year — a real, live, growing
number); the FBI's 2017 core-loci expansion notice (13→20 CODIS core loci, a real, citable
policy change that is the honest basis for a permutation-vs-combination deliverable: "how many
distinct 10-of-20-loci subsets exist, and why is that a combination problem, not a permutation
one?"); published random-match-probability orders-of-magnitude from peer-reviewed forensic
genetics literature (these are usually given as illustrative ranges, e.g. "rarer than 1 in a
billion for unrelated individuals," rather than one clean number — the case should treat the
specific RMP figure honestly as a scenario input if no single citable number fits the panel
size chosen). Not confident about: detective rework-hours per false referral (almost certainly
becomes a disclosed Modeling Assumption); the lab's own reporting-threshold policy (department-
specific, not public — assumption).

**Sensitivity (SPEC §6).** This case touches wrongful accusation, which is real stakes but not a
death/illness/family-hardship stake per SPEC §6's list — still gets a one-line facilitator flag
per SPEC §6's general guidance ("cases touching illness, death, money stress, or family hardship"
— wrongful accusation is adjacent enough to flag, not to avoid). Framed as *protection* (avoiding
wrongful referral) rather than *punishment*, consistent with SPEC §6's protection-over-destruction
guidance.

**Split risk.** NONE — 6 scored skills plus reinforcing is well within the 8–15-skill honest range
for a single T3 case.

---

### C2 — The Overtime Sweep   ·   score 5.1   ·   tier T2

**Protagonist.** Marcus Whitfield, crime analyst deciding whether to deploy a single extra patrol
overtime shift to a historic crime hotspot or spread the same hours evenly across a precinct.

**The dilemma.** A.) Concentrate the overtime shift on the historic hotspot block OR B.) Spread
the same total overtime hours evenly across all patrol sectors.

**Primary metric.** Incidents prevented per overtime-dollar, judged against displacement (whether
concentrating patrol just pushes incidents to the next block over).

**Why it's close.** Hotspot concentration wins if displacement is low; even spread wins if
displacement is high enough that hotspot suppression just relocates the problem — genuinely an
empirical question a real crime-analysis literature addresses.

**Would close (3 skills, 2 how-to / 1 term):** `statistics-and-probability-multistage-sampling`,
`statistics-and-probability-random`, `statistics-and-probability-how-to-determine-the-probability-of-a-compound-event`.

**Data feasibility: MEDIUM.** FBI Crime Data Explorer gives real incident counts by agency, not
by hotspot block — block-level would require a specific city's open incident-with-coordinates
file (data.gov lists several), not guaranteed to be searchable in a way that supports "before/
after" hotspot analysis cleanly. Displacement effect size: MEDIUM, published criminology studies
exist but figures vary widely by study.

**Sensitivity (SPEC §6).** NONE beyond ordinary policing-policy weight.

**Split risk.** NONE, but thin-skill count (3) is lower than C1's (6) — weaker on the "which gap
does this actually close" test.

---

### C3 — The Ballistics Backlog   ·   score 4.6   ·   tier T2

**Protagonist.** A firearms-examination unit supervisor deciding whether to process backlogged
ballistics cases in the order they arrived (FIFO) or triaged by case severity/court-date urgency.

**The dilemma.** A.) FIFO processing OR B.) Severity-triaged processing.

**Primary metric.** Cases cleared before their court deadline, per examiner-month.

**Why it's close.** FIFO is fair and simple; triage clears the highest-stakes cases faster but
risks starving low-severity cases past their own deadlines — a genuine queuing tradeoff.

**Would close (2 skills):** `statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation` (ordering backlog processing sequences), `statistics-and-probability-random`.

**Data feasibility: MEDIUM.** Backlog sizes are published by some state crime labs' annual
reports (real but scattered, not one clean federal source); court-deadline timing would likely
need to be a disclosed scenario assumption.

**Sensitivity (SPEC §6).** NONE.

**Split risk.** On inspection, the permutation use here (ordering a small backlog for processing)
turned out to be decorative — a real supervisor doesn't need to enumerate all *orderings* to
decide FIFO vs. triage, just to rank by one criterion. Flagged and killed for this reason.
