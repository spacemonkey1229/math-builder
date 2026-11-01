# Learning Goals — The Draft Line

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 draft-and-offload calculation | number-sense-depth, measurement-how-to-convert-an-amount-with-compound-units |
| D2 route transit-time comparison | number-sense-distance, measurement-how-to-find-elapsed-time, measurement-how-to-convert-an-amount-with-compound-units |
| D3 net-revenue-per-TEU comparison | measurement-currency, measurement-how-to-convert-an-amount-with-compound-units |
| D4 written recommendation + draft-at-limit edge case | number-sense-depth |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** requires understanding **depth** — the vessel's laden *draft* is exactly a depth measurement (the vertical distance from waterline to keel), and the deliverable's whole arithmetic turns on comparing that depth to the canal's charted limit and reducing it. A student who cannot correctly interpret what "draft exceeds the limit by X meters" means, in depth terms, cannot produce this deliverable. It also requires converting a compound-unit rate (a cm-per-TEU draft-change figure) into a whole-TEU offload count — dividing a depth reduction in meters by a rate given in cm/TEU forces a unit conversion before the division is even valid (m → cm, then cm ÷ cm/TEU = TEU). A student who divides the raw meter figure by the raw cm/TEU rate without converting units gets an answer off by a factor of 100. Genuinely forces `depth` and `how-to-convert-an-amount-with-compound-units`.
- **D2** requires knowing what **distance** means in this context — nautical miles are a real, specific unit of distance, and this deliverable's entire premise is that the two routes differ in distance and that difference is what the student must quantify. It also requires converting a rate (nautical miles ÷ knots, itself nautical-miles-per-hour) into a total transit time, then converting hours to days — a **compound-unit conversion** chained through two steps. Finally, "the schedule difference between the two routes in days" is exactly a **find elapsed time** calculation: computing the duration between two transit-time totals and expressing it as a number of days a real ship would actually spend at sea. A student who reports a raw hour count without converting to days, or who cannot explain why the difference in transit times is itself an elapsed-time quantity, has not performed this skill. Genuinely forces `distance`, `how-to-find-elapsed-time`, and `how-to-convert-an-amount-with-compound-units`.
- **D3** requires computing real dollar totals from several rate inputs — a toll in **currency**, a fuel price in dollars per metric ton multiplied by tons per day multiplied by days (itself a chained **compound-unit conversion**: USD/ton × tons/day × days = USD), and a daily operating cost multiplied by a day count. A student who cannot correctly carry units through that chain (rather than just multiplying digits together and hoping) will produce an internally inconsistent dollar figure. The deliverable's final step — dividing total net revenue by TEU actually carried — is itself a rate built from a currency total, so a student who cannot reason correctly about currency totals cannot produce a defensible net-revenue-per-TEU figure. Genuinely forces `currency` and `how-to-convert-an-amount-with-compound-units`.
- **D4** requires reasoning about the **depth** edge case directly: what happens to the whole comparison if the vessel's draft is exactly at the canal's charted limit, meaning zero TEU need to come off. A student who cannot explain that this removes D1's offload cost entirely (while D2/D3's toll, fuel, and time figures are unaffected) has not actually engaged with what a depth measurement sitting exactly at a limit means for the rest of the case. Genuinely forces `depth`.

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 5    new_coverage: 0 (see case.json.reinforcement_note)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

At case-write time (2026-09-18), `number-sense-depth` was read at `n=2` in
`readmodel/standards_spine.json`, matching the concept sheet's own scoring
(`CONCEPTS_maritime-shipping_2026-09-12.md`, C2). By the time this case reached `case-readiness`
(same day), a fresh spine read found it already at `n=2` with `covered_by=['The Deep End', 'The
Custom Die']` — two sibling cases authored concurrently in this batch closed it first. Per the
reinforcement carve-out (T1-10, `skills/case-readiness/SKILL.md`, "The reinforcement carve-out on
T1-10," added 2026-08-17), `new_coverage[]` is honestly recorded empty rather than padded or falsely
claimed as still-zero — see `case.json.reinforcement_note` for the full record of which adjacent
skills in the Number Sense/Measurement And Data group were checked and found not genuinely forced by
this case's deliverables. `number-sense-depth` remains in `standards[]` because D1 and D4 genuinely
force it (see the forces-test above) — the case still adds real reinforcement value.

The other four claimed skills (`measurement-currency` n=26, `measurement-how-to-find-elapsed-time`
n=12, `measurement-how-to-convert-an-amount-with-compound-units` n=19, `number-sense-distance` n=13)
were checked against the spine and are already well above the n≤2 thin threshold — they are included
in `standards[]` only because the deliverables genuinely force them (see the forces-test above), not
to inflate the skill count. This matches the concept sheet's own explicit call: an earlier draft of
this archetype tried to force coordinate-plane/trig skills onto the same Suez-vs-Cape decision and was
dropped because it could not honestly force any additional thin skill.
