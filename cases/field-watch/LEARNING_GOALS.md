# Learning Goals — Field Watch

Bidirectional deliverable ↔ skill matrix. `case-write`, 2026-08-12.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — simplify Model A (distribute + combine) | `advanced-operations-distributive-property`, `advanced-operations-like-terms` |
| D2 — simplify Model B (distribute + combine) | `advanced-operations-distributive-property` (reinforced), `advanced-operations-like-terms` (reinforced) |
| D3 — solve Model A for crossing day | `advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-one-side` |
| D4 — solve Model B for crossing day | `advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-one-side` (reinforced) |
| D5 — single expression for the models' disagreement | `advanced-operations-how-to-add-and-subtract-an-expression-with-variables` |
| D6 — safety buffer for each model | `advanced-numbers-how-to-subtract-with-negative-numbers` (already covered) |
| D7 — percentage-margin verdict | `advanced-numbers-how-to-find-the-percent-of-a-number` (already covered) |

## LEARNING GOAL CHECK

```
deliverables: 7    claimed skills: 6    new_coverage: 4
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each new-coverage skill** (*could a competent Hero produce the
deliverable correctly without ever performing this skill?*):

- `distributive-property` — D1/D2's raw model forms (`0.72 − 0.02(day − 3)`) are written
  deliberately unexpanded; there is no route to a usable simplified expression without distributing
  the `−0.02` across `(day − 3)`.
- `like-terms` — After distributing, D1/D2 leave two separate constant terms (e.g. `0.72` and
  `+0.06`) that must be combined into one; skipping this leaves an un-simplified, unusable
  expression.
- `how-to-add-and-subtract-an-expression-with-variables` — D5 explicitly asks for Model A's
  simplified expression *minus* Model B's simplified expression, combined into a single expression
  — there is no other way to produce "how much do they differ, as a function of day" as one clean
  expression.
- `how-to-solve-a-multi-step-equation-with-a-variable-on-one-side` — D3/D4's crossing days (19 and
  18) only come from solving `0.40 = [simplified expression]` for `day`; no other operation
  produces these specific values.

**Deliberately not claimed** (see `cases/_concepts/CONCEPTS_remote-sensing_2026-08-12.md`'s
rescope note): `advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-
sides`. The natural "where do the two models agree" deliverable is mathematically trivial for this
data — both models share the Pass 2 anchor point by construction, so they intersect there exactly,
which is not a genuine variable-on-both-sides problem. No other clean, honestly-motivated
deliverable was found for it without contriving the scenario.

No skill here is claimed on the strength of "the case is about satellites generally" — each one
traces to a specific verb in a specific deliverable, using the exact algebraic operation (distribute
vs. combine vs. solve vs. combine-across-subtraction) each spine skill actually names.
