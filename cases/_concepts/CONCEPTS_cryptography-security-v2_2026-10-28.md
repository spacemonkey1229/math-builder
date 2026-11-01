# Concept sheet v2 — Cryptography & Cybersecurity (`cryptography-security`), 2026-10-28 (post-R1 revision of the 2026-10-27 sheet)

**Chosen:** option (iii), the sheet's old C2, reworked and renamed **The Thursday Window**. Nothing written under `cases/<id>/`.
All figures below were recomputed in Python on 2026-10-28 from the live CISA KEV feed (catalogVersion 2026.10.27,
dateReleased 2026-10-27T19:00:02Z, 1,760 entries, 1,760 unique CVE ids). Margin convention, stated once and used everywhere:
**margin = (winner's value - loser's value) / winner's value.**

## Why this option (and not the other two)

| Option | Verdict | Reason |
|---|---|---|
| (i) rework C1 Range Query | Rejected | With caching the API wins at every volume (a request-count break-even of 16^5 cancels the response size), so a non-GB metric would still have one option dominating. Not "both genuinely win". |
| (ii) C3 Lock Screen | Rejected for this wave (kept in reserve) | The entry-time gap is now sourced (see below) but the honest numbers make the case unbalanced or force a composite "keyspace per second" metric that is the same non-stake R1c rejected. A uniform-guess model makes the stranger-guess risk ~1 in 10^5, so security stops mattering and the pattern wins on time by roughly 3x; with a 4-digit PIN the keyspace is 10^4 vs 380k. No clean metric found. |
| (iii) C2 Three-Day Clock | **Chosen** | All decision inputs are live, student-checkable public data; the stake is an org's exposure window; the shape is a two-parameter boundary curve with a vertical asymptote (not a one-parameter break-even) plus a window-day sweep; margin 2.8%. Cost: closes no n<=2 skill (it thickens n=2 "Non-linear" to n=3). |

Evidence kept for a future C3 (fetched 2026-10-28): Harbach, De Luca, Egelman, "The Anatomy of Smartphone Unlocking: A Field
Study of Android Lock Screens", CHI 2016 (N=134, 160,746 unlock sessions). Mean successful unlock: pattern 910 ms, 4-digit-class
PIN 1,963 ms; regression y = -53 + 147x ms per pattern cell (x = cells); error rate per attempt pattern 12.1%, PIN 3.1%;
daily unlock time similar (pattern 64.1 s vs PIN 58.3 s). Mean PIN length in the study was 4.25 digits; no 6-digit timings
exist, so any 6-digit-PIN comparison needs a labeled scaling assumption.
URL: `https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/44675.pdf`.

Also settled (R1b on C1): fetched `https://haveibeenpwned.com/Passwords` on 2026-10-28. The page offers **no bulk file or torrent**;
it says the API is "the best way to get the most up-to-date passwords" and points to the free open-source Pwned Passwords
downloader (`github.com/HaveIBeenPwned/PwnedPasswordsDownloader`) to "take the entire corpus offline"; it states no file sizes,
formats, hash counts or dates. So v1's "Option B = mirror" was approximately right in kind, but its 81.2 GB size was computed, not published (UNVERIFIED), and caching made A dominant. C1 is dropped.

---

## C — The Thursday Window   ·   tier T3   ·   metric margin 2.84% (B wins at the operating point)

**Protagonist.** Rafael Quintero (constructed; "Rafael" and "Quintero" each return 0 hits in `cases/` as of 2026-10-28), IT operations lead
for fictional Tallgrass County. His team is three people. The county uses the federal CISA KEV list as its patch trigger
voluntarily; BOD 26-04 itself binds only federal civilian agencies (disclose).

**Story seed (Overview ends at the instant of decision; not the phone-buzz ending).** Wednesday, 7:40 a.m., the county's change-advisory board has not yet convened. Rafael stands in front of the
operations-room wall calendar with a dry-erase marker, two colors of weekly pattern half-drawn: a Thursday square repeated down
the page in blue, and a thin green line through every weekday. Behind him the sheriff's dispatch screens refresh; on the table
sits the county's patch log, three people's initials in the margins. The board wants a standing policy, not a one-off. He
takes the cap off the marker with his teeth and has to decide which pattern gets drawn on the calendar for the next year.
(No numbers in the Overview; counts live in the Appendices.)

**The dilemma (binary, SPEC 1.4).**
You are Rafael Quintero. Do you:
A.) Run **Daily Triage**: check the KEV feed every county business day and patch each applicable entry the same business day it is seen, OR
B.) Run **The Thursday Window**: check the feed once a week and patch every applicable entry in one standing Thursday window (the change board's fixed slot)

**Primary metric.** KEV deadlines met per staff-hour over the frozen study period (higher wins).

**What makes it close (all recomputed).**
Frozen period: dateAdded 2026-06-10 (BOD 26-04 issue date) through 2026-10-27 inclusive (140 calendar days).
Scope: the 10 vendors in the county's constructed inventory (Microsoft, Cisco, Fortinet, Citrix, Adobe, Google, SonicWall,
Oracle, Apple, Palo Alto Networks): **N = 52 entries** (Microsoft 13, Cisco 10, Fortinet 6, Citrix 5, Adobe 4, Google 4,
SonicWall 4, Oracle 3, Apple 2, Palo Alto Networks 1). Feed dueDate minus dateAdded: **41 entries have a 3-day clock, 11 have a
14-day clock**; no entry is a duplicate CVE id.

Rules (stated in the case, so the Hero can reproduce): clocks are calendar days and run from dateAdded (BOD 26-04 Appendix A:
"Days are calendar days"; timelines begin when CISA adds the vulnerability); an entry is **met** if the patch date <= dueDate.
A: first county business day strictly after dateAdded; B: first Thursday strictly after dateAdded.
County closed on the four U.S. federal holidays in the period (Juneteenth Fri 2026-06-19; Independence Day observed Fri
2026-07-03; Labor Day Mon 2026-09-07; Columbus Day Mon 2026-10-12): labeled assumption. **A meets 52/52 with or without
the holidays.** **B (Thursday) meets 40/52 = 76.9%**; the 12 misses are all 3-day items added Thu (6), Fri (3) and Sun (3).
The 11 fourteen-day items are met 11/11 by B.

Counts by weekday added x clock (appendix table, A = all met):

| Added | 3-day | 14-day | Total | B (Thu) met |
|---|---|---|---|---|
| Mon | 3 | 2 | 5 | 5 |
| Tue | 10 | 7 | 17 | 17 |
| Wed | 16 | 1 | 17 | 17 |
| Thu | 6 | 0 | 6 | 0 |
| Fri | 3 | 1 | 4 | 1 |
| Sat | 0 | 0 | 0 | 0 |
| Sun | 3 | 0 | 3 | 0 |
| **All** | **41** | **11** | **52** | **40** |

Hours model (Modeling Assumptions, all labeled): business days in period BD = 96 (100 weekdays minus 4 holidays);
Thursdays W = 20; triage 1.0 staff-hr per business day (A); one window costs 2.0 staff-hr of triage and change-board prep (B);
every one of the 52 entries needs e staff-hours of patch work whichever option; **B's batching saves a fraction d of that
patch work** (shared reboots, testing, tickets). Over the period:

- A hours = 96 + 52e; A yield = 52 / (96 + 52e)
- B hours = 40 + 52e(1 - d); B yield = 40 / (40 + 52e(1 - d))   (B patches all 52; only 40 are on time)

**Operating point e = 4.0 h, d = 0.10:** A = 52/304 = 0.17105 per hour; B = 40/227.2 = 0.17606 per hour.
**B wins by (0.17606 - 0.17105)/0.17606 = 2.84%.** Hours: A 304, B 227.2.

Both options genuinely win: at e = 6.0, d = 0.10, A = 0.12745 vs B = 0.12469, **A wins by 2.17%**; at e = 3.0, B wins by 6.94%; at
e = 2.0, B wins by 13.16%; at e = 5.0, A wins by 0.06% (essentially tied).

**The boundary is a curve, not a point.** Setting A = B and solving for e:
e*(d) = 1760 / (624 - 2704 d)  (equivalently 1760 / (52 (12 - 52 d))), with the d = 0 case e* = 2.82 h.

| d | e* (h) |
|---|---|
| 0.00 | 2.82 |
| 0.05 | 3.60 |
| 0.10 | 4.98 |
| 0.15 | 8.06 |
| 0.20 | 21.15 |
| 0.22 | 60.44 |
| 3/13 = 0.2308 | no finite e*: B always wins |

Rule of thumb that falls out and is checkable by hand: B wins for every e once d >= 1 - 40/52 = 3/13 (B patches the same 52 items
but meets only 40 deadlines, so batching must save at least 12/52 of patch work to beat A's perfect record); below that, a break-even e* exists and
grows non-linearly. This is the real argument: "how much does batching actually save, and how many hours is a KEV patch?"

**Window-day sweep (decision lever the Hero may argue, same e, d).** B's on-time count by window weekday (first such day
strictly after dateAdded): Mon 17, Tue 17, Wed 27, **Thu 40**, **Fri 43**, Sat 36, Sun 20. At e = 4, d = 0.10 a Friday window
would beat A by 9.62% on the same metric (and Thursday by 2.84%), but a Friday window leaves the weekend exposed if a patch
fails; the case fixes Thursday because the change board meets Wednesday, and treats Friday as the Hero's counter-proposal.

**Deliverables (map to rows; each forces math).**
- D1. Clock table: split the 52 entries by clock (3-day vs 14-day) and weekday added; percent of entries that are 3-day (78.8%, 41/52).
- D2. Window rule: write the "met" test for B as a compound statement (added < window AND window <= due), apply it to every weekday x clock cell, and report 40/52 and 76.9%; date arithmetic for each cell (elapsed time).
- D3. Hours and yield: A and B staff-hours at the operating point, the deadlines-per-staff-hour ratio, and the margin using the stated convention.
- D4. Break-even: solve for e at d = 0.10 (variable on both sides), then build a table of e* for at least five values of d, state whether e* is linear or non-linear in d with evidence from the table, and find the d above which B wins for any e.
- D5. Bar chart of on-time count by window weekday (original visual), and a one-paragraph defense of staying with Thursday or asking the board for Friday.

**Forced spine skills (all 8 ids verified to exist in `readmodel/standards_spine.json`; n = current covered_by count):**

| Skill id | n | Forced by |
|---|---|---|
| `measurement-ratio` | 30 | deadlines per staff-hour (D3) |
| `discrete-mathematics-logical-statement` | 3 | D2 "met" test |
| `discrete-mathematics-conjunction` | 3 | D2: added < window AND window <= due |
| `measurement-how-to-find-elapsed-time` | 12 | D2 calendar day counts |
| `advanced-numbers-how-to-convert-numbers-to-percents` | 44 | 76.9%, 78.8% |
| `advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides` | 3 | D4 break-even in e |
| `statistics-and-probability-non-linear` | 2 | D4 e*(d) |
| `number-sense-bar-graph` | 47 | D5 |

No n<=2 skill is newly closed; "Non-linear" goes 2 -> 3 (still thin). The old "digit" claim is dropped (no longer forced).
`discrete-mathematics-logical-statement` and `-conjunction` also appear in Perimeter Protocol (p AND q); see Overlap below.

**Tier T3.** Three+ variables (e, d, window day), some data deliberately irrelevant (vendors outside the inventory,
pre-BOD entries with 21/181-day clocks, the `forensicTriage` flag: 34 of the 41 three-day items carry "Yes", 0 of the
11 fourteen-day items; forensic-triage hours are not modeled and the case says so). Not T4: no inference.

**Data feasibility: HIGH (counts) / assumptions labeled (hours).** Fetched 2026-10-28:
- `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` (catalogVersion 2026.10.27, 1,760 entries; fields cveID, vendorProject, dateAdded, dueDate, forensicTriage). Confidence HIGH. The page, though, is a moving catalog, so the case freezes **as-of 2026-10-27 (feed catalogVersion 2026.10.27)** for every number, and the Hero should be told that entries and dueDates can be edited later.
- `https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk` (issued June 10, 2026; "Days are calendar days"; "timelines ... begin when either (1) CISA adds the vulnerability to the KEV Catalog"; Table 1 is an image, so the 3/14-day tiers are read from the feed's dueDate, not the table). HIGH for dates and rule text; tier values from the feed.
- Student-explorable: the JSON opens in a browser; filtering by dateAdded and vendor reproduces N = 52 in a spreadsheet.

**Modeling Assumptions (not sourced; stated openly).** MA1 inventory = the 10 named vendors. MA2 daily triage 1.0 staff-hr per
business day. MA3 weekly window 2.0 staff-hr. MA4 patch effort e = 4.0 staff-hr per entry (sensitivity: e* 4.98 at d = 0.10). MA5 batching saving d = 0.10 (sensitivity above: this is the most load-bearing dial; asymptote at d = 3/13). MA6 county closed on four federal-holiday dates. MA7 an entry seen on a business day is patched that same day (A) and on window day (B). MA8 county uses BOD 26-04 clocks voluntarily.

**Sensitivity (SPEC 6).** NONE (no real people or incidents; fictional county). Facilitator note: staffing-hours framing; no one is harmed in the case. **Split risk.** NONE.

**Overlap check.** Same upstream data family as `perimeter-protocol` (CISA KEV) but a different premise and math: there it is boolean rule logic on traffic
(p AND q vs p OR q); here it is calendar-window coverage and a staffing break-even curve. Different from `the-keyspace-decision`
(password length vs 2FA) and from Key Length / Codebreaker. R1c may still judge the KEV domain overlap; the alternative is held in reserve (C3 with Harbach data).
Protagonist grep: "Rafael" 0 hits, "Quintero" 0 hits in `cases/`; avoids Priya, Mara, Okafor, Raman.

---

## Fixes applied (R1 round 1 -> v2)

| Finding | Fix |
|---|---|
| R1a: with caching, API transfers less than the full mirror at every volume (N(1-e^(-c/N))) and break-even is the constant 16^5, so response size cancels | C1 dropped; in v2 the break-even is recomputed from live data and depends on two disclosed parameters, not a cancelling constant. |
| R1b: HIBP may offer a bulk file; add as-of date | Fetched 2026-10-28: no bulk file/torrent on the page; downloader on GitHub; no sizes. 81.2 GB was computed, not published. C1 dropped; v2 carries as-of 2026-10-27 on every number. |
| R1c: GB/yr is no stake; same domain as the-keyspace-decision | v2 metric is deadlines met per staff-hour for a county's patch team (org stake); different artifact (KEV calendar) than a password policy. |
| v1 C2: 47 entries / 36 met / e* 3.28 from ten different vendors | Recomputed with an explicit 10-vendor inventory: N = 52, B meets 40, e* = 2.82 at d = 0, 4.98 at d = 0.10. |
| v1 C2: duplicate CVE (CVE-2026-109618 listed twice) | Not reproducible: 1,760 entries and 1,760 unique ids in the 2026.10.27 feed; CVE-2026-109618 appears once (added 2026-10-26, due 2026-10-29). The case still instructs a unique-id check. |
| v1 margins 3-4% on mixed conventions | One convention (gap / winner's value); operating-point margin 2.84% (B), 2.17% (A at e = 6). |
| v1 one-parameter break-even | Two parameters (e, d) so the boundary is a hyperbola e*(d) = 1760/(624 - 2704 d) with asymptote d = 3/13; plus a window-day sweep. |
| Brief: names, endings, as-of dates | Rafael Quintero (0 hits); marker-cap ending; as-of 2026-10-27 stated everywhere. |
| Brief: claim no unforced spine id | 8 ids claimed, each tied to a deliverable; "digit" dropped. |

## Still open (UNVERIFIED / for later reviewers)

1. **Staff-hours (MA2-MA5) are constructed.** No public per-patch hour figure was sourced; d = 0.10 is the single most load-bearing guess (e* explodes toward d = 3/13). R1b may want a cited patch-effort or batching study, or accept it as a labeled assumption.
2. **BOD 26-04 Table 1 is an image**; tiers are inferred from feed dueDates (3 and 14 days observed post-issue; before issue, 21/181-day gaps). The case does not state Table 1's exposure/automation logic; whether a county asset "has a 3-day clock" depends on exposure, which the case simplifies by using the feed's date for all.
3. **Holiday dates** (MA6) are calendar-derived and not fetched from OPM (the OPM page returned an error/blocked response). Results are unchanged without holidays (A 52/52), but business-day count BD would be 100 not 96, shifting the margin slightly. Recompute if kept.
4. **KEV feed is mutable**; the frozen snapshot is not archived in the repo. Before build, save the JSON and record a SHA-256 in `sources[]`.
5. **Voluntary use of a federal directive** (MA8) should be a Background disclosure, not just here.
6. **Closes no n<=2 skill.** If the wave must reduce thin skills, hold C3 (Lock Screen: `statistics-and-probability-permutation`, `...how-to-determine-the-number-of-outcomes-of-a-permutation`, both n=2) in reserve with the Harbach figures above; open problem there is a non-composite metric and a 6-digit PIN timing (none published; patterns of 4-9 dots total 389,112, length>=6 380,336 by enumeration).
7. **Overlap with Perimeter Protocol** (same data family, same logic skills) is R1c's call.

## Reproduction notes (Python, scratchpad `kev/calc.py`)
Filter `dateAdded` in [2026-06-10, 2026-10-27] and vendorProject in the inventory -> 52 rows; gap = dueDate - dateAdded (days) -> {3: 41, 14: 11};
A date = next business day (Mon-Fri minus 4 holidays) after dateAdded; B date = next Thursday after dateAdded; met = date <= dueDate;
BD = 96, W = 20; yields and margins as above; e*(d) = (mB*BD*tA - mA*W*tB) / (n*(mA*(1-d) - mB)) with mA = 52, mB = 40, tA = 1, tB = 2, n = 52.
