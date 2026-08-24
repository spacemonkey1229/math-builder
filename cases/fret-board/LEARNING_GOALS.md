# Fret Board — Learning Goal Matrix

Bidirectional check between Challenge 3 deliverables and claimed spine skills (`case-write`
SKILL.md §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — fret-position table, Precision Method | `advanced-operations-exponent-also-power`, `advanced-operations-how-to-evaluate-an-exponential-expression` (evaluating the twelfth-root-of-two ratio raised to a rational exponent *n*/12 for each fret) |
| D2 — fret-position table, Rule of Eighteen | `measurement-ratio`, `measurement-how-to-find-equivalent-ratios` (applying a fixed divisor ratio repeatedly to a shrinking remaining length, and comparing that approximated ratio series against the true one) |
| D3 — cents-of-deviation conversion | `advanced-operations-exponent-also-power`, `advanced-operations-how-to-evaluate-an-exponential-expression` (the cents formula is itself an evaluated exponential/logarithmic expression applied to the D1/D2 outputs) |
| D4 — GCF string-length-ratio table | `basic-operations-greatest-common-factor`, `basic-operations-how-to-find-the-greatest-common-factor-of-a-set-of-numbers`, `basic-operations-factor` (reducing each fret's open:fretted length ratio to lowest terms) |
| D5 — recommendation | draws on all of the above; forces no additional skill by itself |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 7    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied:** a competent student cannot produce D1 without evaluating a rational
exponent; cannot produce D2 without applying and comparing ratios; cannot produce D4 without
computing a GCF and reducing a ratio to lowest terms. D3 reuses the same exponent/ratio machinery
from D1/D2 to convert their outputs into cents rather than forcing a new skill class — it is
listed against the same two exponent-family ids rather than invented a separate claim.

## Coverage note

Every claimed skill already has `n >= 1` in `readmodel/standards_spine.json` at the time this
case was written (checked 2026-08-24, see `case.json.reinforcement_note` and the `n` values
recorded there). `new_coverage[]` is therefore genuinely empty — this case was never expected to
close a zero-coverage skill (see `CONCEPTS_formal-logic-vectors-matrices-numbertheory_2026-08-23.md`,
C4: "0 new zero-coverage skills"). Its reason to exist is opening the zero-existing-case
`music-acoustics` domain and feeding the case-starved `number-theory` branch — a domain-opening
case, not a skill-count case. See the `reinforcement_note` field in `case.json` for the full
adjacent-skill check required by the carve-out.
