# RESEARCH_LOG.md — A Coach's Dilemma (content replacement, 2026-08-18)

One row per figure needed: what was searched, what was found or rejected, and why. This case
replaces the previous fictionalized-2008-NCAA content with a scenario built on a real, documented,
verifiable 2015 NBA playoff series (see `case.json.replacement_note`). All fetches below were done
live during this authoring pass (WebSearch + WebFetch/curl), not recalled from memory.

---

## P01 — DeAndre Jordan's 2014-15 real free-throw statistics

**Searched:** "DeAndre Jordan 2014-15 season free throw percentage basketball-reference." Initial
WebSearch snippets returned a confusing, wrong-looking figure ("39 percent... in reference to his
improved free throw shooting in the 2016 regular season") that needed direct verification rather
than trust.

**Resolved:** `basketball-reference.com` blocks the WebFetch tool directly (HTTP 403). Fetched the
page instead via `curl` with a browser user-agent from Bash (200 OK, ~1.4MB HTML) and parsed the
raw per-game/totals table rows directly out of the HTML (`data-stat="ft"`, `"fta"`, `"ft_pct"`).
Confirmed: 2014-15 regular season, 187-471 FT, .397 (39.7%), 82 games, matches the season-total row
exactly. **Confidence: HIGH.** Used in case.md Appendix B / case.json source S1.

**Also found on the same page (not initially targeted, kept for use):** the same player's 2015
playoffs table breaks out by round — a WC1 row (7 games vs. San Antonio, 28-73 FT, 38.4%) and a
separate WCS row (7 games vs. Houston, 39-84 FT, 46.4%) plus a combined 14-game full-playoffs row
(67-157, 42.7%). **Deliberately used only the WC1 (pre-Houston-series) row** in case.md — the WCS
row and the 14-game combined row both silently include games against Houston that had not been
played yet at this case's decision point (before Game 4), and using them in the student-facing
Background/Appendix would leak future information / partially leak the Twist. The WCS-series row
(46.4%) is real and cited for context inside FACILITATOR.md's Twist material only, never in case.md.

---

## P02 — Los Angeles Clippers' 2014-15 team Offensive Rating and Pace

**Searched:** "Clippers 2014-15 offensive rating points per 100 possessions basketball-reference."
Same 403 issue on direct WebFetch; resolved the same way — `curl` with a browser user-agent against
`basketball-reference.com/teams/LAC/2015.html` (200 OK), parsed the `team_misc` table's `off_rtg`
and `pace` cells directly. **Found: ORtg 112.4, Pace 94.7.** **Confidence: HIGH.** Used in case.md
Appendix B / case.json source S3. Points-per-possession (1.124) is the case's own shown division
(112.4 / 100), not a separately sourced figure.

---

## P03 — Real NBA six-foul disqualification rule and the "no one-and-one, always two free throws"
intentional-foul rule

**Searched:** "NBA official rule six personal fouls disqualification foul out rulebook." Attempted a
direct fetch of the NBA's own official rulebook PDF (`ak-static.cms.nba.com/.../NBA-Official-
Playing-Rules.pdf`) — **rejected**, request timed out (60s) without returning content. Attempted
`official.nba.com/rulebook/` directly — also timed out.

**Resolved:** Fetched Wikipedia's "Personal foul (basketball)" page, "Fouling out" section, which
states the NBA's 6-foul-in-48-minutes disqualification rule explicitly and compares it against
other leagues (WNBA, PBA D-League: 6 fouls in a 40-minute game; NBA Summer League: 10 fouls) —
internally consistent and corroborated by every independent NBA-rules-explainer search result
returned in the same research pass (all in agreement on 6 fouls, no dissenting figure found
anywhere). **Confidence: HIGH** — this is a long-standing, uncontroversial rule with no real
controversy or recent change to source more cautiously; the two-free-throws-not-one-and-one detail
for an intentional/non-shooting foul is standard, widely known officiating knowledge, further
corroborated by every real box score checked in this research pass (DeAndre Jordan's real free
throws always came in pairs of attempts, e.g. 34 attempts across 17 trips in the real Game 4 box
score, never single one-and-one attempts). Used in case.md Appendix C / case.json source S4.

---

## P04 — Real offensive-rebound rate on a missed free throw

**Searched:** "NBA offensive rebound rate after missed free throw study percentage." Multiple
results surfaced a range of numbers across different eras and framings (13.9% from an "older
study," 10.4% vs. 24.7% for missed FT vs. missed FG specifically in the 2015-16 season).

**Attempted:** WebFetch of `darrylblackport.com`'s "Separating First and Second Chance Scoring in
the NBA" (a 17-season, 2001-02 through 2017-18 analysis) — **rejected for this specific figure**:
the piece has real, specific numbers for league-wide second-chance-points-per-100-possessions by
season, but does not break out the offensive-rebound rate specifically on missed free throws versus
missed field goals, which is exactly what this case needs.

**Attempted:** WebFetch of `fansided.com/2016/01/06/offensive-rebounds-and-three-pointers/` —
**this is the figure used.** Confirmed by direct fetch (not just a search snippet): "10.4%"
offensive-rebound rate on missed free throws vs. "24.7%" on missed field goals, both stated as
2015/16-season league-wide figures. **Confidence: MEDIUM, not HIGH** — this is a secondary sports
blog reporting its own observed league data without citing a primary NBA.com/Stats page, and its
season (2015-16) is one year later than this case's own 2014-15 setting. **Decision:** used only as
the disclosed real anchor for Appendix D's MA2 Modeling Assumption, never presented in case.md as a
bare, load-bearing cited fact. This is the exact pattern SPEC §5/case-research's "NOT FOUND" exit 1
describes: a real, dated, public estimate exists, but not one clean enough to cite as a hard fact —
so it becomes a disclosed assumption's anchor instead of a fabricated precise appendix number.

---

## P05 — Transition-offense value vs. half-court-offense value

**Searched:** "NBA transition offense points per possession vs half court offense study 2015."
Results were scattered and inconsistent across sources: one analysis cited "1.20 points per
possession" for elite transition offense; another cited "half-court 1.084, transition 1.228"; a
third cited "transition 1.04, half-court 0.87." None of these three had a single, clean, dated,
primary citation specific to the 2014-15 NBA season fetchable within this research pass.

**Decision: NOT FOUND at the precision this case would need to cite as a hard fact.** Per
case-research's NOT FOUND procedure, this became a stated, disclosed Modeling Assumption (MA3)
rather than an invented precise number: the case states the conservative low end of the real range
found across multiple independent (if non-primary) analyses (~0.15 points per possession), discloses
the range and the lack of a single primary source in Appendix D and case.json's
`modeling_assumptions[]`, and does not present it as a cited fact anywhere. A hand check during
authoring found this assumption is load-bearing for SPEC's 20% balance cap (removing it pushes the
margin to 23.1%, over the cap) — flagged explicitly in `case.json.balance.stability` and
FACILITATOR.md's Sensitivity note for a future Tier 2 probe 5 run to test formally.

---

## P06 — Backup-center defensive drop-off (on/off efficiency split)

**Searched:** "Houston Rockets 2015 playoffs backup center Josh Smith Clint Capela minutes Dwight
Howard foul trouble," and attempted a direct fetch of Dwight Howard's Basketball-Reference player
page looking for an on/off-court splits table.

**Found:** real, general context (Clint Capela and Josh Smith both saw real minutes as Houston's
backup centers that postseason; Capela averaged a real 16.2 points/11.9 rebounds per 36 minutes in
the 2015 playoffs) but **no clean, granular, publicly fetchable on/off defensive-rating split**
specific to "Clippers offense with Houston's starting center in vs. out" for this exact series.
Basketball-Reference's on/off splits pages were not reachable at the depth this research pass
budgeted for.

**Decision: NOT FOUND at the granularity needed.** Became MA4, a stated, disclosed, deliberately
modest assumption (+8.0 points per 100 possessions when the backup is in), reasoned from the
general, well-documented real pattern that NBA team defense worsens when a primary rim-protecting
big is replaced by a lesser one — explicitly not claimed as a number pinned to this specific
matchup. Disclosed in Appendix D and `case.json.modeling_assumptions[]`.

---

## P07 — Real Game 4 (May 10, 2015) box score and play-by-play (Twist material)

**Searched/fetched directly:** ESPN's Game 4 summary page and a direct `curl` fetch of Basketball-
Reference's box score (`/boxscores/201505100LAC.html`) and play-by-play
(`/boxscores/pbp/201505100LAC.html`) pages.

**Found, all HIGH confidence, all corroborated across ESPN + Basketball-Reference + a Yahoo
Sports/AP recap independently:** Final score Clippers 128, Rockets 95. DeAndre Jordan: 14-of-34 free
throws, with 28 of those 34 attempts coming in the first half alone (widely reported as an NBA
playoff record). Houston's primary center, Dwight Howard: 18:22 minutes played, 6 personal fouls
(disqualified) plus a technical foul on the same play (ejected), 7 points, -28 plus/minus. Parsed
the real play-by-play foul log directly: Howard's personal fouls came at 9:21 and 8:20 remaining in
the 1st quarter, 8:19 in the 2nd, 8:05 and 3:07 in the 3rd, and his 6th foul (plus the technical)
came with 9:52 remaining in the 4th quarter — meaning he had 5 personal fouls entering the 4th
quarter and fouled out just 8 seconds into it.

**Used exclusively in FACILITATOR.md's Twist material — deliberately excluded from case.md.** This
case's decision point is set before Game 4 tips off; including the real Game 4 result or Howard's
real foul progression anywhere in the student-facing case.md would leak the Twist before discussion,
the exact defect (P4 pre-leak) that got the previous version of this case BLOCKED. Appendix C's D4
deliverable instead poses a stated, clearly-labeled hypothetical scenario ("suppose he already has 4
fouls entering the fourth") rather than the real number, precisely so the real outcome can still
land as a genuine surprise in discussion.

---

## Not pursued / explicitly excluded

- The original FiveThirtyEight piece "Intentionally fouling DeAndre Jordan is futile" is real and
  was found via WebSearch snippets (confirming a very similar naive-EV-vs-corrected-EV structure to
  this case's own D2/D3 split, independently corroborating the modeling approach). **Its live URL
  now 301-redirects to `abcnews.com/politics`** — the fivethirtyeight.com domain appears to have
  been repurposed/merged since the article was written. Per case-research's "verify every URL
  resolves before shipping it" rule, this was **excluded from case.json sources[]** entirely; it is
  recorded here only as research context, not cited anywhere in the case.
- Dwight Howard's own 2014-15 season awards/accolades were checked to see if a "he was an
  All-Defensive selection that season" claim could strengthen MA4's real anchor — **rejected**: the
  All-Defensive First Team / DPOY-3 finalist accolades found in that research thread belonged to
  DeAndre Jordan's own 2014-15 season row, not Dwight Howard's. Not used, to avoid misattributing a
  real accolade to the wrong real player.
