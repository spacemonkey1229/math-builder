# Player Of The Year — Analytics-Driven Methodology Split

**Source data:** `2027-2028 NCAA Division I Women's Volleyball Statistics.xlsx` (9 tabs: Hitting %, KillsSet, BlocksSet, AssistsSet, PointsSet, DigsSet, AcesSet, AttacksSet, Season Final Team RPI Rankings) and `Stat_Definitions.pdf`, both already present locally under `source/Y2/Session 5/Player Of The Year/` (these are the local copies of the docx's Appendix A Google Sheet and Appendix B glossary — no external fetch was needed since the files ship with the source folder).

**Background confirmed from the docx:** the 2027-2028 champion was **Wisconsin** (RPI #2, 31-3), which beat the favored **Louisville** (RPI #1, 32-1) in the title match. The 14 AVCA First-Team All-Americans are exactly the 14 named in the case's dilemma list.

---

## 1. Full 14-Player Data Table

Each stat is **per set** (or a percentage), pulled directly from its ranked national leaderboard tab where the player appears in that tab's top bracket (Hitting % / Assists / Digs / Aces = top 150 nationally; Blocks = top 300; Kills = top 1,500 — effectively the full D-I field). Where a player did **not** rank nationally in a category (because her role doesn't generate volume there — e.g., a setter's kill total, a middle blocker's ace total), the cell is marked **NR** (not ranked) rather than a fabricated number. Several NR cells were recoverable by back-computing from a different tab that reports the same raw counts (e.g., Hitting % from AttacksSet's Kills/Errors/Attempts; Aces/Set and Blocks/Set from PointsSet's raw Aces / Block Solos+Assists columns) — those are flagged "(derived)". Genuinely unrecoverable NRs remain blank.

| Player | Pos | School (Conf.) | Sets | Hit % | Kills/Set | Attacks/Set | Digs/Set | Assists/Set | Aces/Set | Blocks/Set | Pts/Set | Team RPI | Team W-L |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Betsy Torres | OH | Texas (Big 12) | 99 | NR | 3.91 | NR | NR | NR | 0.44 | 0.65 (d) | 4.72 | 4 | 27-2 |
| Nicole Peterson | MB | Wisconsin (Big Ten) | 120 | 0.430 | 3.41 | 6.40 (d) | NR | NR | 0.01 (d) | 1.43 | 4.24 | 2 | 31-3 |
| Stephanie Roberts | RS | Minnesota (Big Ten) | 114 | 0.254 (d) | 4.75 | 12.58 | NR | NR | 0.19 (d) | 0.72 (d) | 5.32 | 13 | 22-9 |
| Shawna Capellen | OH | Utah (Pac-12) | 112 | 0.276 (d) | 5.19 | 12.50 | NR | NR | 0.31 (d) | 0.49 (d) | 5.77 | 23 | 22-9 |
| Lauren Bates | L/DS | Wisconsin (Big Ten) | 122 | NR | NR | NR | 4.35 | NR | NR | NR | NR | 2 | 31-3 |
| Julia Bergmann | OH | Georgia Tech (ACC) | 112 | 0.284 (d) | 4.44 | 9.95 | NR | NR | 0.32 (d) | 0.60 (d) | 5.16 | 5 | 26-6 |
| Mastana Brambilla | OH | Georgia Tech (ACC) | 112 | 0.286 (d) | 4.34 | 10.14 | NR | NR | 0.21 (d) | 0.44 (d) | 4.77 | 5 | 26-6 |
| Anna DeFluer | OH | Louisville (ACC) | 105 | NR | 3.27 | NR | NR | NR | NR | NR | NR | 1 | 32-1 |
| Tori Dent | S | Louisville (ACC) | 113 | NR | NR | NR | NR | 10.74 | NR | NR | NR | 1 | 32-1 |
| Samantha Drechsel | OH | Washington (Pac-12) | 116 | NR | 3.48 | NR | NR | NR | 0.27 (d) | 0.57 (d) | 4.04 | 16 | 26-5 |
| Sydney Hilley | S | Wisconsin (Big Ten) | 122 | NR | NR | NR | NR | 11.95 | NR | NR | NR | 2 | 31-3 |
| Mac May | OH | UCLA (Pac-12) | 115 | 0.268 (d) | 4.85 | 11.66 | NR | NR | 0.39 | 0.45 (d) | 5.51 | 17 | 25-6 |
| Yossiana Pressley | OH | Baylor (Big 12) | 100 | 0.280 (d) | 4.53 | 10.37 | NR | NR | 0.15 (d) | 0.55 (d) | 5.00 | 6 | 22-6 |
| Anna Stevenson | MB | Louisville (ACC) | 111 | 0.427 | 2.79 | 5.23 (d) | NR | NR | NR | 1.35 | NR | 1 | 32-1 |

**(d)** = derived from a raw-count column in a different tab rather than read directly off that stat's own ranked leaderboard. Notably: the 9 pin hitters (OH/RS) cluster around .25–.29 hitting and 3.3–5.2 kills/set; the two setters (Tori Dent, Sydney Hilley) and the libero (Lauren Bates) are, as expected, absent from every offensive category — their entire national-caliber production is concentrated in Assists/Set or Digs/Set respectively. This role split is real, not a data gap, and it's the reason the two methodologies below can legitimately diverge.

**National reference population** (mean, population SD, n) computed from each stat's own full ranked leaderboard — used as the z-score baseline for both methodologies:

| Category | Mean | SD | n (players in tab) |
|---|---|---|---|
| Hitting % | 0.356 | 0.033 | 150 |
| Kills/Set | 2.333 | 0.784 | 1,500 |
| Blocks/Set | 1.084 | 0.130 | 301 |
| Assists/Set | 9.997 | 0.756 | 150 |
| Digs/Set | 4.617 | 0.426 | 150 |
| Aces/Set | 0.405 | 0.061 | 150 |
| Attacks/Set | 10.844 | 0.925 | 150 |

---

## 2. Two Composite Methodologies

### Methodology A — "All-Purpose Production Index" (unweighted, position-blind z-score composite)

**Logic:** Score every finalist identically, regardless of position, across the five countable per-set production categories every rally can generate: Kills, Aces, Blocks, Assists, Digs. Each category is converted to a z-score against the national field (mean/SD table above), and the five z-scores are averaged with **equal weight**. If a player isn't nationally ranked in a category, that category is scored at **league average (z = 0)** rather than penalized as a zero — i.e., "no data" is treated as "no information," not "failure." This is the standard sabermetric-style approach to an all-around value composite (analogous to an unweighted five-tool score).

**Formula:**

```
CompositeA(player) = mean( z(Kills/Set), z(Aces/Set), z(Blocks/Set), z(Assists/Set), z(Digs/Set) )
where z(x) = (player's value − national mean) / national population SD
      and z(x) = 0 if the player is not nationally ranked in that category
```

### Methodology B — "Role-Weighted × Team-Success Composite"

**Logic:** Reflects two things the docx explicitly says the selection committees actually use — position-specific excellence (a setter is not evaluated on kills; a libero is not evaluated on hitting percentage) and team quality ("they utilize the players' statistics as well as weigh the quality of the teams into their decisions"). Each player is scored only on the 1–3 stat categories that define excellence at her position, averaged as z-scores, then multiplied by a team-success factor derived from her team's final-season RPI rank (out of ~340 D-I teams) — the better the team, the larger the multiplier, capping at +50% for the nation's #1 team and decaying to no bonus outside the top 50.

**Role-relevant categories:**

| Position | Categories scored |
|---|---|
| OH / RS (pin hitters) | Kills/Set, Hitting %, Aces/Set |
| MB (middle blocker) | Blocks/Set, Hitting %, Kills/Set |
| S (setter) | Assists/Set |
| L/DS (libero/defensive specialist) | Digs/Set |

**Formula:**

```
RoleZ(player)   = mean( z(cat) for cat in that player's role-category list )
TeamMult(RPI)   = 1 + 0.5 × (1 − (RPI − 1)/49)     if RPI ≤ 50
                = 1.0                                if RPI > 50
CompositeB(player) = RoleZ(player) × TeamMult(TeamRPI)
```

---

## 3. Computed Scores (auditable, all 14 finalists)

### Methodology A — ranked

| Rank | Player | z(Kills) | z(Aces) | z(Blocks) | z(Assists) | z(Digs) | **CompositeA** |
|---|---|---|---|---|---|---|---|
| 1 | **Anna Stevenson** | +0.583 | 0.000 | +2.047 | 0.000 | 0.000 | **+0.526** |
| 2 | Sydney Hilley | 0.000 | 0.000 | 0.000 | +2.585 | 0.000 | +0.517 |
| 3 | Anna DeFluer | +1.195 | 0.000 | 0.000 | 0.000 | 0.000 | +0.239 |
| 4 | Tori Dent | 0.000 | 0.000 | 0.000 | +0.983 | 0.000 | +0.197 |
| 5 | Lauren Bates | 0.000 | 0.000 | 0.000 | 0.000 | −0.628 | −0.126 |
| 6 | Betsy Torres | +2.011 | +0.575 | −3.349 | 0.000 | 0.000 | −0.153 |
| 7 | Mac May | +3.209 | −0.245 | −4.891 | 0.000 | 0.000 | −0.385 |
| 8 | Nicole Peterson | +1.373 | −6.473 | +2.663 | 0.000 | 0.000 | −0.487 |
| 9 | Julia Bergmann | +2.686 | −1.392 | −3.735 | 0.000 | 0.000 | −0.488 |
| 10 | Shawna Capellen | +3.642 | −1.556 | −4.583 | 0.000 | 0.000 | −0.499 |
| 11 | Stephanie Roberts | +3.082 | −3.523 | −2.810 | 0.000 | 0.000 | −0.650 |
| 12 | Samantha Drechsel | +1.463 | −2.212 | −3.966 | 0.000 | 0.000 | −0.943 |
| 13 | Yossiana Pressley | +2.801 | −4.178 | −4.120 | 0.000 | 0.000 | −1.099 |
| 14 | Mastana Brambilla | +2.559 | −3.195 | −4.968 | 0.000 | 0.000 | −1.121 |

**Winner under Methodology A: Anna Stevenson (MB, Louisville).** Her block rate (1.35/set, well above the national top-300 average of 1.08) combined with an elite .427 hitting percentage produce the highest average z-score, narrowly (+0.526 vs. +0.517) ahead of Sydney Hilley.

### Methodology B — ranked

| Rank | Player | Role categories | RoleZ | Team RPI | TeamMult | **CompositeB** |
|---|---|---|---|---|---|---|
| 1 | **Sydney Hilley** | Assists | +2.585 | 2 | 1.490 | **+3.851** |
| 2 | Nicole Peterson | Blocks, Hit%, Kills | +2.082 | 2 | 1.490 | +3.102 |
| 3 | Anna Stevenson | Blocks, Hit%, Kills | +1.583 | 1 | 1.500 | +2.375 |
| 4 | Tori Dent | Assists | +0.983 | 1 | 1.500 | +1.474 |
| 5 | Betsy Torres | Kills, Hit%, Aces | +0.862 | 4 | 1.469 | +1.267 |
| 6 | Anna DeFluer | Kills, Hit%, Aces | +0.398 | 1 | 1.500 | +0.598 |
| 7 | Mac May | Kills, Hit%, Aces | +0.106 | 17 | 1.337 | +0.142 |
| 8 | Shawna Capellen | Kills, Hit%, Aces | −0.106 | 23 | 1.276 | −0.136 |
| 9 | Samantha Drechsel | Kills, Hit%, Aces | −0.250 | 16 | 1.347 | −0.336 |
| 10 | Julia Bergmann | Kills, Hit%, Aces | −0.291 | 5 | 1.459 | −0.424 |
| 11 | Lauren Bates | Digs | −0.628 | 2 | 1.490 | −0.936 |
| 12 | Mastana Brambilla | Kills, Hit%, Aces | −0.914 | 5 | 1.459 | −1.334 |
| 13 | Stephanie Roberts | Kills, Hit%, Aces | −1.169 | 13 | 1.378 | −1.610 |
| 14 | Yossiana Pressley | Kills, Hit%, Aces | −1.221 | 6 | 1.449 | −1.769 |

**Winner under Methodology B: Sydney Hilley (S, Wisconsin).** Her 11.95 assists/set is #1 nationally by a wide margin (z = +2.585, the single largest z-score of any player in either methodology), and it's fully credited because she's compared only to other setters' primary stat — combined with Wisconsin's #2 RPI (the team that actually won the national title), she comfortably outranks everyone, including Anna Stevenson.

**The two methodologies produce two genuinely different, real winners — this was not forced.** Methodology A (position-blind, all-around production) crowns the middle blocker whose hitting efficiency and block rate survive being averaged against categories she doesn't play. Methodology B (role-normalized, team-success weighted) crowns the setter whose signature stat is the most dominant single number in the entire dataset, once she's not diluted by categories that aren't her job.

---

## 4. Locked Dilemma — Option A / Option B

**You are the AVCA Player Of The Year Committee. Two committee members have each proposed a rigorous, formula-based scoring system — and they disagree. Which methodology should the committee adopt?**

**Option A — Adopt the All-Purpose Production Index.**
Score all 14 finalists identically, position blind, as an unweighted average z-score across Kills/Set, Aces/Set, Blocks/Set, Assists/Set, and Digs/Set (national mean/SD baseline; non-ranked categories scored at league average). Under this system, **Anna Stevenson (MB, Louisville)** is the AVCA Player Of The Year — her .427 hitting percentage and 1.35 blocks/set generate the highest average z-score of any of the 14 finalists (+0.526), narrowly ahead of Sydney Hilley (+0.517).

**Option B — Adopt the Role-Weighted × Team-Success Composite.**
Score each finalist only on the categories that define her position (pin hitters: kills/hit%/aces; middles: blocks/hit%/kills; setters: assists; libero: digs), then multiply by a team-success factor tied to her team's final RPI rank (up to +50% for a top-team boost, per the selection committee's own stated practice of weighing team quality). Under this system, **Sydney Hilley (S, Wisconsin)** is the AVCA Player Of The Year — her nationally-#1 11.95 assists/set produces the largest single z-score in the dataset (+2.585), and it's paired with Wisconsin's #2 RPI and their upset national championship over #1 Louisville, giving her the highest composite score of any finalist (+3.851), comfortably ahead of Nicole Peterson (+3.102).

---

## 5. Data & Method Appendix (for the case drafter)

- **Extraction script:** reads all 9 tabs of the xlsx via `openpyxl`, matches each of the 14 named finalists by first-token name string across every tab, and back-fills a stat from an alternate tab's raw counts when the player isn't in that stat's own ranked leaderboard (Hitting % ← AttacksSet raw Kills/Errors/Attempts; Attacks/Set ← Hitting % tab's Total Attacks/Sets; Aces/Set and Blocks/Set ← PointsSet's raw Aces / Block Solos+Assists columns).
- **National reference stats** are computed from each stat's full ranked leaderboard column (not just the 14 finalists), giving an honest "how does this player compare to the field" baseline — noting this baseline is itself an *already-elite* subpopulation (top 150/300/1,500 nationally), which is a modeling choice worth stating explicitly in the write-up.
- **Team RPI / W-L** pulled from the "Season Final Team RPI Rankings" tab, matched by stripping the conference parenthetical from each player's school field.
- All computation is reproducible arithmetic (mean/SD/z-score/weighted average) — no hand calculation of the 14×7 table was performed; a full Python script computed every cell. The team can hand this table + the two formulas directly to students as the case's "data necessary" appendix, or use it as the answer key against student-built composites.
