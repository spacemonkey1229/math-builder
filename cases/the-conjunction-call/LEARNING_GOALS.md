# Learning Goals — Conjunction Call

Bidirectional deliverable ↔ skill matrix, per `skills/case-write/SKILL.md` §10.

## Deliverable → Skills

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — conjunction-count table (factorial-based combination formula) | `advanced-operations-factorial`, `advanced-operations-how-to-evaluate-a-factorial-expression` |
| D2 — probability-notation screening table (scientific ↔ standard notation, absolute-value margin) | `advanced-operations-scientific-notation`, `advanced-operations-standard-notation`, `advanced-operations-how-to-write-a-number-in-standard-notation-given-its-scientific-notation`, `advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation`, `advanced-operations-absolute-value` |
| D3 — propellant-budget table (Isp → exhaust velocity → kg per m/s, compound-unit conversion) | `measurement-how-to-convert-an-amount-with-compound-units` |
| D4 — decision memo (final ratio/comparison, restated in appropriate notation and units) | `advanced-operations-scientific-notation`, `measurement-how-to-convert-an-amount-with-compound-units` |

## Skills → Deliverable (reverse check)

| Skill (spine id) | n (live) | Reached by |
|---|---|---|
| `advanced-operations-standard-notation` | 2 | D2 |
| `advanced-operations-factorial` | 2 | D1 |
| `advanced-operations-absolute-value` | 2 | D2 |
| `advanced-operations-how-to-write-a-number-in-standard-notation-given-its-scientific-notation` | 2 | D2 |
| `advanced-operations-how-to-evaluate-a-factorial-expression` | 2 | D1 |
| `advanced-operations-scientific-notation` | 5 | D2, D4 |
| `advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation` | 5 | D2 |
| `measurement-how-to-convert-an-amount-with-compound-units` | 19 | D3, D4 |

## Forces test

Applied strictly: *could a competent student produce this deliverable correctly without ever
performing this skill?*

- **D1** cannot be produced without evaluating a factorial-based combination expression
  (`36! / (2! · 34!)`) and simplifying it by cancellation — the group size (36) is too large to
  expand literally, which is exactly why the how-to skill (recognizing the cancellation) is
  forced rather than decorative.
- **D2** cannot be produced without converting a probability given in scientific notation into
  standard (decimal) notation to do the subtraction, and re-expressing the resulting margin in
  scientific notation — both directions of the conversion are genuinely used, not just one.
  Absolute value is forced because the margin can be computed either above or below the
  threshold; the deliverable explicitly asks for the size of that margin, not its sign.
- **D3** cannot be produced without treating "kilograms of propellant per meter/second of
  delta-v" as a compound unit and converting it against a given delta-v in meters/second to
  reach a mass in kilograms.
- **D4** restates the D1–D3 outputs in a final comparison, which forces at least one more
  genuine round of notation and unit-conversion work (the final propellant totals must be
  presented in a directly comparable form to the stated reserve figures).

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 8    new_coverage: 0 (reinforcement carve-out — see case.json.reinforcement_note)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

Every claimed skill in `standards[]` is reached by at least one deliverable above (right-hand
column, "Skills → Deliverable"). Every deliverable in `Deliverable → Skills` has a non-empty
skills column. No skill is claimed that the case's actual math does not force.
