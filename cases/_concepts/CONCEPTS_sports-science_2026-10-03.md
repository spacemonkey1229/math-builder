# Concepts — Sports Analytics (Sports Science wave) — 2026-10-03, round 4

Source foundation: `Sports_Science_Math_Case_Studies_Bundle_2026.zip` (whitepaper + 10 CSVs). Round 1 blocked the nine-case
slate. Rounds 2 and 3 (R1a BLOCK on C1/C4 in round 3; R1b and R1c conditional APPROVE) are folded in below. Cases 4-8 of the
original slate are HELD (bottom). Domain: `sports-analytics` (Culture, Play & Performance).

**Wave cap: 4 cases, four stories** (swimming, football-stats, cycling, football-history). The release plan (bottom of this file) names
four paired non-sports slots from domains with no concept file yet (hard gate, per R1c). The sports cases are staggered,
never consecutive, and the two football cases are non-adjacent. No leftover picks from over-mined concept files.

Evidence tags: **[R1b-CONFIRMED]** sourced by R1b on the web; **[DERIVED]** computed by us, recomputed by R1a;
**[ASSUMPTION]** disclosed with a sensitivity table; **[UNVERIFIED]** research task, cut or disclosed if still open at drafting.
Every case ships a teacher-facing note on sensitivity and a "what the model leaves out" step that is graded, not a closing remark.

| Concept | Story | Math | Tier guess |
|---|---|---|---|
| **C1 The Hundredth** | 2008 Olympic 100 m butterfly | Rates, units, measurement uncertainty, tie rule | T2 |
| **C2 The Trophy and the Table** | Tottenham 2024/25 | Scatter, line of best fit, residuals, leave-one-out | T2 |
| **C3 The Eight-Second Tour** | 1989 Tour, stage 21 | Power law (v^3), break-even, model limits | T3 |
| **C4 The Gijon Rule** | 1982 World Cup, WG-Austria | Tables, tie-breaks, scenario enumeration, rule design | T2 |

---

## C1 — The Hundredth

**Protagonist.** The chief judge ruling on the protest (a role, not a named person). The decision point is **constructed**:
the case says plainly that the real referee reviewed high-speed video and upheld the result. Students reason about the evidence he faced.

**Facts [R1b-CONFIRMED].** Phelps 50.58 (Olympic record), Cavic 50.59, 16 Aug 2008. Serbia protested. Referee Ben Ekumbo, per
secondary reports, said "One was stroking and one was gliding" and that Cavic touched second; FINA said it was convinced Phelps
reached the wall first (ABC, 16 Aug 2008). **First contact is contested:** Omega's Berthaud (single source, one spelling) and Cavic
himself have said Cavic touched first without triggering the pad; the case attributes "gliding" to Ekumbo only and presents both
claims as claims. FINA technical rules (2023 edition, wording confirmed; **2008-edition rule numbers [UNVERIFIED]**): SW 13.1 gives
automatic equipment precedence; SW 13.4.2 treats equal official times as ties. Official resolution is hundredths.
Cut: "Serbia accepted the footage" (unsourced).

**Binary dilemma (R1a fix).** Which instrument decides when the pad and the eye could disagree?
- **Option A: the pad ranks** (equipment precedence, the rule as written: 50.58 beats 50.59).
- **Option B: first contact on high-speed video ranks** (what the swimmers' hands did, not when the pad registered).
Both are defensible: A is objective, resolved to 0.001 s, and applied identically to every race; B measures what the sport is
meant to reward, but a video call is a human judgment. The case does **not** offer a shared gold: the official times are not equal,
and SW 13.4.2 makes a dead heat require equal times, so the rule, not the pad's precision, is what rules it out (students see why).

**Math [DERIVED].**
- Average speed 100/50.58 = 1.977 m/s, so 0.01 s is about **2.0 cm** (an average-speed approximation; finishing speed differs and
  a gliding hand is slower).
- A pad lag common to both swimmers cancels. **Only a differential lag greater than 0.01 s (about 2 cm of glide) could make the pad
  and first contact disagree.** That differential is the graded, open question: students compute it, state the lag range
  they consider plausible and justify it, with the stroking-vs-gliding asymmetry on one side and Berthaud's touch-vs-push point on the other.
- Video band by frame rate: 30 fps 6.6 cm, 60 fps 3.3 cm, 240 fps 0.82 cm, 1000 fps 0.20 cm: why broadcast video could not decide
  this and high-speed footage could.

**[ASSUMPTION].** The lag range: no published figure was found; a 1.5-2.5 kg pad activation force appears only in industry write-ups
(secondary); no lag number is attributed to Omega or FINA. Student-facing text says **"plausible range, not measured"** and carries a
sensitivity table. **[UNVERIFIED].** 2008-edition rounding wording; the camera used in 2008.

**Neutral register.** Cavic is described by his race and protest only. FINA's ruling stands; the case never implies it was wrong.

**Data/images.** Results from Olympedia/Wikipedia. No press-agency finish photo (copyright). Any image needs a Wikimedia licence check.
The bundle's Douglass 512 Hz study is not used.

---

## C2 — The Trophy and the Table

**Protagonist.** A member of the club board (unnamed; public record only, no motive speculation).
**Teacher note (required).** Students are judging a model, not a person; the case is not a verdict on the manager.

**Facts [R1b-CONFIRMED].** Postecoglou dismissed 6 Jun 2025, 16 days after Spurs beat Manchester United 1-0 in the Europa League
final (21 May 2025, San Mames, Bilbao). Spurs finished 17th: 38 pts, W11 D5 L22, GF 64, GA 65, GD -1; lowest finish in 48 years.
The club cited poor league form. The case explains the Europa League in one paragraph for US students.

**Binary dilemma.** Keep the manager who won a trophy, or replace him after a 17th-place league finish.

**Math [DERIVED, recomputed by R1a].**
- 20-club fit: points = 52.35 + 0.666 x GD, R^2 = 0.941, residual SD 4.63.
- Spurs: predicted 51.7, actual 38, residual **-13.68** (about -2.95 SD). Next worst is Bournemouth at **-4.35** (write "-4.3 to -4.4"
  or the exact value).
- **Leave-one-out:** points = 53.07 + 0.665 x GD, R^2 = 0.970, Spurs residual **-14.40**; against the other 19 clubs' residual SD
  (3.34) Spurs sits about **-4.3 SD** out. Outlier lesson.
- **Graded step: what the model leaves out.** n = 20, one season, GD and points are mechanically linked (description, not causation),
  a residual cannot separate luck from management. Injuries: the Premier League reported a centre-back injury crisis
  (premierleague.com/en/news/4208927); injury counts from fan sites are not used as fact.

**Data terms [R1b].** Football-Data.co.uk says data is for private use only and not for commercial or automated-bot use:
**link to it and have students download it themselves; never bundle the CSV**. The 20-row table is from the official final table
(matches Wikipedia). StatsBomb open data requires attribution plus logo and is non-commercial; Understat has no published terms: both
are **optional extensions only**, not on the required path. FBref xG is discontinued (Opta, 20 Jan 2026): never cited.
The bundle CSV is the case's table; the regression outputs stay labelled derived.

---

## C3 — The Eight-Second Tour

**Protagonist.** The sports director of LeMond's team on the evening before stage 21 (a role; no invented quotes).
**Framing disclosure.** This is a **hindsight scenario**: the 50 s target is the real deficit; Fignon's real 27:55 stands in for the
rival's expected time. The case states that the director would not have known Fignon's time, and assumes LeMond's conventional-position
speed equals Fignon's.

**Facts [R1b-CONFIRMED].** Stage 21, 23 Jul 1989, 24.5 km, Versailles to Champs-Elysees. LeMond 26:57 (54.545 km/h), Fignon +58 s.
LeMond trailed by 50 s going in and won the Tour by 8 s, the closest ever. LeMond: aero (triathlon) bars, aero helmet,
rear disc; Fignon: no aero bars, no helmet, front and rear discs. Fignon's saddle sores, ponytail and poor sleep are contested
context and stay **out of the math**. Never state "LeMond gained X seconds from the bars"; the "about a minute" figure is unsourced and cut.

**Binary dilemma.** Commit to the aero-bar position (less drag, less sustainable power) or ride the conventional position at full power.

**Math [DERIVED, algebra corrected after R1a].**
- Needed speed ratio = 1675 / 1625 = **1.0308** (+3.1%); cubed = **1.0952** (+9.5% power at fixed drag).
- Cube-law break-even for CdA cut x and power loss y: (1 - y) / (1 - x) >= 1.0952, so y <= 1 - 1.0952(1 - x).
- Full model (bundle parameters: 78 kg, Crr 0.004, rho 1.225, CdA 0.32, includes rolling resistance, about 6% of power) breaks even sooner:

| CdA cut x | Cube-law y (max power loss) | Full-model y |
|---|---|---|
| 10% | 1.4% | 1.1% |
| 14% | 5.8% | 5.2% |
| 15% | 6.9% | 6.2% |
| 20% | 12.4% | 11.3% |

The gap between columns is the model-limits lesson. **What the literature does and does not give [R1b-CONFIRMED, honest limits]:**
Garcia-Lopez et al. 2008 (J Sports Sci 26(3):277-286): position changes among time-trial positions cut drag about 14% in 5 professionals
(wind tunnel). Fintelman et al. 2014 (J Biomech, "Optimal cycling time trial position models"): peak power fell about 14% between a
24-degree and a flat torso (confirmed from a search summary; cite "per the abstract" after a human check), and its abstract reportedly
says the aero gain outweighs the power loss above about **46 km/h**, while LeMond averaged 54.5 km/h. **Neither paper compares aero bars
with a conventional position**, and the two 14% figures come from different comparisons. So students treat x = 10-15% and y = 3-14% as
a **sensitivity range, not a measurement**; the 3% lower bound is our assumption. The case says openly that at race speed the
literature leans toward aero, and the honest tension is how large a power loss the position tolerates, not a coin flip.
Popular "15-25%" CdA figures are not peer reviewed and are cited as indicative only.

**Model-does-not-match disclosure [DERIVED].** The bundle parameters imply about **728 W** to ride 24.5 km in 26:57, not credible
for 27 minutes. The model does not reproduce LeMond's observed speed (course, wind or parameters differ). The case uses **ratios
only** and never implies LeMond produced those watts. The v^3 form is the aero-only approximation.

**Image.** "Greg LeMond 1989 Tour de France stage 21 TT.jpg", CC BY 2.0, credit Benjamin Werner (Flickr user bw94) exactly as on the Commons page; the photo shows the start, so caption it that way.
Stage results from Wikipedia (ProCyclingStats is not openly licensed).

---

## C4 — The Gijon Rule

**Protagonist.** A member of a FIFA rules committee choosing the final-round rule for the next World Cup (a role). **The scene is
constructed**: no source documents how or when the 1986 rule was decided, and the 1994 three-point rule came later for other reasons.
The case teaches the group rules and Algeria's side from scratch. **Framing:** an incentive-structure story, not an accusation; FIFA ruled
no rule was broken and the case never alleges match-fixing.

**Facts [R1b-CONFIRMED, secondary sources].** Results from the Wikipedia group pages (raw wikitext). 1982 Group 2: WG 1-2 Algeria;
Chile 0-1 Austria; WG 4-1 Chile; Algeria 0-2 Austria; Algeria 3-2 Chile; WG 1-0 Austria (25 Jun, Hrubesch 10th minute). Final table: WG
4 pts GD +3, Austria 4 GD +2, Algeria 4 GD 0. Two points per win; **tie-break ladder 1982: points, goal difference, goals scored [UNVERIFIED: no URL found for the 1982 regulation text; cite the FIFA 1982 regulations or Wikipedia before drafting, or drop the ladder-dependent counts].** Since 1986
the final pair of group matches kick off simultaneously (secondary: Wikipedia, goalswithoutborders.com). Three points for a win: first
used at the 1994 World Cup.

**Binary dilemma (R1a fix: the options are now differently shaped).**
- **Option A: simultaneous kickoffs only** (1982 tie-break ladder unchanged).
- **Option B: simultaneous kickoffs plus goals scored before goal difference** as the first tie-break.
Students first test the tempting fix, the **3-point rule, and find it changes nothing** (same advancing pairs, all scorelines to 6 goals).

**Math [DERIVED; recomputed by R1a and R1c].** "Safe" = a West Germany-Austria scoreline that sends both through for certain.
- 1982 as played (Algeria-Chile known, 3-2): WG wins by 1 or 2 are safe (1-0, 2-0, 2-1, 3-1, ...). Larger margins usually send WG and Algeria,
  with exceptions students find (5-2 leaves Austria and Algeria level on goal difference and goals scored; 6-3 sends Austria through).
- **Worst-case reasoning (A):** with Algeria-Chile unplayed, **no scoreline is safe against every Algeria-Chile result**. But a risk-tolerant
  pair can still gamble. Over Algeria-Chile results of 0-6 goals each (49 cells, illustrative count, not probabilities), a 1-0 WG win still sends both
  through in **39 of 49** cells (all 28 where Algeria draws or loses, 11 of the 21 where Algeria wins). A shrinks certain collusion to a gamble.
- **Option B:** the same 1-0 survives in only **29 of 49** cells (all 28 where Algeria draws or loses, 1 of 21 where Algeria wins); high-scoring wins
  needing Austria on 5+ goals stay safe against more results. For low-margin scorelines like 1-0, B sharply cuts the gamble but does not abolish it (the best scoreline, 6-5, is safe in 45 of 49 cells under B versus 42 under A).
- **The cost side (B), sourced [R1b, derived from group pages]:** applying B to the other five 1982 first-round groups changes the advancing pair
  in exactly **one** (Group 6: Scotland, GF 8, replaces USSR, GF 6, who went through on goal difference); Groups 1, 3, 4 and 5 are unchanged.
  So B rewrites a real result in 1 of 5 other groups. Students weigh a bigger fix against rewriting history.
- A's own cost (a broadcast slot, fan access) has **no source: not claimed.** The tension rests on B's computed side effect and on A
  leaving a gamble open.
- **A forward-looking cost of B (R1c).** Goals-first does not remove collusion, it relocates it: the safe region becomes high-scoring wins
  (3-2, 4-2, 5-3, ...), so two teams that both profit could cooperate on a **goal-fest** instead of coasting. B also changes every future
  group, for every team: a side protecting a lead gains nothing from goal difference, and attacking play is rewarded whether or not it
  wins the game. Students weigh a rule that fixes 1982 against one that creates a new cooperative scoreline.
- Coasting is individually rational for both teams; the case says so: a rule, not exhortation, changes incentives.
- **Open ending (required).** The case does not tell students which option FIFA "should" have chosen. Option A is what FIFA actually did
  and the case says so; the debrief asks whether that makes it the better rule or only the one history picked.

**Data.** Group pages en.wikipedia.org/wiki/1982_FIFA_World_Cup_Group_1 to _Group_6 (use raw wikitext; do not use summaries of the main
tournament page). The bundle's K6 round-robin CSV is not used. Any match image needs a licence check.

---

## Release plan (the diversity hard gate, made checkable)

Slots, in this order, so no two sports cases are adjacent and the football cases are separated. The non-sports slots are the **thinnest
domains in the corpus**: a keyword scan of every `case.md` (2026-10-03, rough; `case-brainstorm` re-checks against `cases_index.json`) found
**zero** archaeology and **zero** linguistics hits (the whole Deep Time & Language cluster is untouched), about 4 nuclear-energy hits
(mostly `nuclear-waste`) and about 7 hydrology/flood hits. Domains with existing cases or concept mentions (insurance, elections,
clinical-medicine, agriculture) were deliberately **not** used. Working directions below are placeholders for a fresh brainstorm, not
approved concepts; each needs its own R1a/b/c pass.

| Slot | Case | Domain (cluster) | Working direction (to be brainstormed) |
|---|---|---|---|
| 1 | C1 The Hundredth | sports-analytics | n/a |
| 2 | NON-SPORTS A | archaeology (Deep Time & Language) | dating-a-find decision using radiocarbon decay |
| 3 | C3 The Eight-Second Tour | sports-analytics | n/a |
| 4 | NON-SPORTS B | hydrology-water (Earth, Climate & Environment) | flood-frequency / return-period call from public gauge data |
| 5 | C2 The Trophy and the Table | sports-analytics | n/a |
| 6 | NON-SPORTS C | linguistics (Deep Time & Language) | word-frequency / dialect-split decision from open corpora |
| 7 | C4 The Gijon Rule | sports-analytics | n/a |
| 8 | NON-SPORTS D | nuclear-energy (Food, Energy & Resources) | decay/shielding or outage-scheduling decision (not waste storage; `nuclear-waste` exists) |

Gate: a sports case is promoted only after its paired slot holds an R1-approved concept.

---

## Held (not dropped)

| Concept | Why held | What would unblock it |
|---|---|---|
| Beijing Slowdown (Bolt) | No official Beijing splits; an estimate, not a decision | Official/peer-reviewed splits plus a pre-race pacing decision |
| Rest Day Fine (Popovich/Kawhi) | ACWR evidence is rugby/youth football; real injury, controversy | One story, a named NBA dataset with terms, no ACWR-justifies-resting claim |
| Mid-Range Question (Curry/Morey) | Mid-range ~0.8 vs 1.08 pts is not close; overlaps `a-coachs-dilemma` | Close-call framing and a licensed per-zone source |
| Judge's 62 | Not a real decision; Statcast terms unchecked | Swing-change trade-off with real Statcast bins, terms checked |
| Shot from the Wing (Messi) | No real dilemma; StatsBomb attribution/logo terms | Real decision plus a 7.32 m goal recompute |
| Goalball | Source claim fails geometry | Not needed |
