# Learning Goals — The Marginal Detection

Bidirectional deliverable ↔ skill matrix, run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 scatter plot of all 20 points | `statistics-and-probability-scatter-plot`, `statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data` |
| D2 line of best fit + correlation judgment + non-linear call | `statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data`, `statistics-and-probability-correlation`, `statistics-and-probability-how-to-identify-correlation-given-a-scatter-plot-or-set-of-data`, `statistics-and-probability-non-linear` |
| D3 naive significance ratio (residual-based) | `statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data` |
| D4 box-and-whisker + quartiles + outlier check | `statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data`, `statistics-and-probability-quartiles`, `statistics-and-probability-outlier` |
| D5 written recommendation comparing both reads | `statistics-and-probability-non-linear`, `statistics-and-probability-outlier`, `statistics-and-probability-quartiles` |

## LEARNING GOAL CHECK

```
  deliverables: 5    claimed skills: 9    new_coverage: 0 (reinforcement carve-out — see case.json.reinforcement_note)
  UNMAPPED DELIVERABLES: none — every deliverable (D1-D5) maps to at least one claimed skill
  UNREACHABLE SKILLS: none — every claimed skill is forced by at least one deliverable:
     - non-linear: D2 (identify why the drift isn't straight), D5 (explain the disagreement)
     - line-of-best-fit how-to: D2 (fit it), D3 (use its residuals)
     - box-and-whisker how-to: D4 (build it)
     - outlier: D4 (1.5xIQR check), D5 (reference it in the written call)
     - scatter plot / how-to: D1
     - correlation / how-to: D2
     - quartiles: D4 (five-number summary), D5 (reference it)
  RESULT: PASS
```

"Forces" test applied: a student cannot produce D3's significance ratio without having actually
fit a line and computed residual standard deviation; cannot produce D4's ratio without actually
building the five-number summary and IQR; cannot write a defensible D5 without having both
numbers and being able to explain non-linearity in plain terms. No deliverable is decorative.

Next step: `Run case-research on the-marginal-detection to fill open placeholders.` (Already run
in the same authoring pass — see `RESEARCH_LOG.md`.)
