# Research Log — Speed Climbing

Legacy conversion, 2026-08-20. Unlike a fresh case, almost none of this case's load-bearing data
needed external sourcing: the twelve climbers, their timed trial (Appendix A), their practice/
competition history and six-month progression (Appendix B), and Coach's Notes (Appendix C) are the
case's own given scenario data from the source docx — not real, externally-verifiable people or
events, so SPEC §5's "cited or declared assumption" rule doesn't apply to them any more than it
applies to Family Trip's driving distance being a fact about a fictional-enough family road trip.
(Family Trip *did* need sourcing because it named real airlines, real IRS rates, and a real route.
Speed Climbing's protagonist, gym, and climbers are original to the source and not claimed to be
real.)

What *did* need real-world sourcing: Appendix E, "About Speed Climbing," which makes real,
externally-checkable claims about the actual sport (wall specs, current world records, USA
Climbing's youth program) to ground the case in reality per SPEC's general house practice.

## P01 — IFSC official speed wall height and overhang angle

- Searched: "IFSC speed climbing world record women's 2026 15 meter wall"
- Fetched: `https://en.wikipedia.org/wiki/Speed_climbing_wall`
- Found: 15,000 mm (15 m) tall, continuous 5° overhang, per current IFSC Speed Licence Rules.
- Confidence: HIGH (Wikipedia summarizing the governing body's own published rules; unambiguous
  units; matches the original source's own Guide Notes claim of "15 meters tall").
- Recorded as [S1].

## P02 — Women's speed climbing world record

- Searched: "Emma Hunt 5.99 seconds women's speed climbing world record 2026"
- Fetched: `https://www.nbcsports.com/olympics/news/emma-hunt-speed-climbing-world-record`
- Found: 5.99 seconds, Emma Hunt, July 4, 2026, World Climbing Series Kraków. First sub-6-second
  run by a woman. Previous record 6.03s, Aleksandra Mirosław.
- Confidence: HIGH (reputable sports journalism, dated, unambiguous, directly fetched).
- Recorded as [S2].
- Rejected: `climbing.com`'s own article on this same fact — the URL redirected to an
  authentication/paywall gate (`accounts.outsideonline.com`) rather than serving the article; not
  used as a citation since it was never actually fetched.

## P03 — Men's speed climbing world record

- Searched: "men's speed climbing world record 2026 seconds holder"
- Found two candidate records for the same athlete (Zhao Yicheng) in 2026: 4.58s (Asian Beach
  Games, April 28) and a reported later 4.54s (World Climbing Series Wujiang, ~May 2026).
- Fetched and confirmed only the first: `https://www.lacrux.com/en/klettern/Zhao-Yicheng-shatters-speed-world-record--4.58-seconds/`
  — 4.58 seconds, April 28, 2026, Asian Beach Games, Sanya, China, beating Sam Watson's prior
  4.64s.
- The 4.54s figure was not independently fetched/confirmed (only a search-result summary from
  People's Daily/NBC coverage), so it is **not** cited as the current record — the case cites only
  the directly-confirmed 4.58s figure, with a disclosed note in `case.json.sources[]` that a later,
  faster run was reported but not verified. This is a real-world number used only as texture in
  Appendix E, not load-bearing for any calculation, so the small residual uncertainty about the
  exact current record doesn't affect the case's math.
- Confidence: HIGH (directly fetched, dated, unambiguous).
- Recorded as [S3].

## P04 — USA Climbing Youth Nationals Speed discipline

- Searched: "USA Climbing U18 speed climbing national championships youth category"
- Fetched: `https://usaclimbing.org/compete/youth-national-championships/`
- Found: USA Climbing runs Speed as one of three disciplines (with Boulder and Lead/TR) at Youth
  Nationals; a seeding round establishes time, then a knockout bracket (per the 2025 event page).
  The fetch did **not** confirm USA Climbing's own exact age-division names (e.g., whether "U18" is
  literally one of their division labels).
- Decision: cite only what was confirmed (Speed is a real, currently-run youth discipline) and
  explicitly disclose in case.md that "U18" is this case's own fictional gym's internal division
  name, not asserted to be USA Climbing's own terminology. This avoids an unverifiable overclaim
  while still grounding the case in a real national governing body and a real competitive format.
- Confidence: HIGH for what was confirmed.
- Recorded as [S4].

## NOT FOUND / not pursued

- Exact USA Climbing age-division names and cutoffs — not pursued further since the case doesn't
  need them (The Summit's "U18" is disclosed as the gym's own label).
- A precise, single up-to-the-minute "current" men's world record — see P03; resolved by citing
  only the directly-confirmed figure and disclosing the uncertainty rather than guessing.

## Post-write correction (case-readiness Tier 2 P6, 2026-08-20)

P6's fetch-capable subagent re-fetched all 4 URLs. S1/S2/S3 fully confirmed as cited. S4's page
confirmed Speed is one of three disciplines at USA Climbing Youth Nationals, but could **not**
confirm the "seeding-round-then-bracket format" detail this case originally cited alongside it —
that phrase doesn't appear on the page. Per house doctrine ("a URL that resolves but no longer
carries the figure is worse, because nothing else in the pipeline would ever notice"), the
unconfirmed detail was removed from both `case.md` Appendix E and `case.json.sources[]` S4's
`claim`/`note` — the case now cites only the directly-confirmed fact.

## Summary

| Placeholder | Value | Confidence | Source |
|---|---|---|---|
| P01 | 15,000 mm / 5° | HIGH | Wikipedia / IFSC rules |
| P02 | 5.99 s (Emma Hunt) | HIGH | NBC Sports |
| P03 | 4.58 s (Zhao Yicheng) | HIGH | Lacrux Climbing Magazine |
| P04 | Speed discipline confirmed at USAC Youth Nationals | HIGH | USA Climbing |

Zero `{{NEEDS_SOURCE}}` remain in `case.md`. All four real-world claims in Appendix E are cited;
all core scenario data (Appendices A, B, C, D) is the case's own given data, not requiring external
citation. Next step: `case-readiness` Tier 1 + Tier 2 on `speed-climbing`.
