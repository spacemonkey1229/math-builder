# Challenge Boilerplate — canonical text

**Status:** LOCKED · **Authority:** SPEC.md §1.5 · **Version:** 1.0

> This file is the single source of truth for the fixed Challenge sections.
> `case-write` inserts this text. `case-qa` diffs the case against this text.
> Neither skill keeps its own copy. Changing a character here changes every future case
> and requires a DOCTRINE_LEDGER row.

Sections **1, 2, 4 and 5 are boilerplate and must appear verbatim** — they are the badge
requirements. **Only section 3 is authored per case.**

The sentences in double quotes below are quoted verbatim from SPEC.md §1.5 and are
character-locked. The `a.)` / `b.)` sub-lines under Challenge 2 are the house rendering of the
two requirements SPEC.md §1.5 states in prose ("must include (a) use of the researched how-to,
(b) at least one original visual display of the data"); they are locked here so QA can check
them mechanically.

---

## BEGIN CANONICAL BLOCK

```
Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) <CASE-SPECIFIC DELIVERABLES — the only authored section. A short list of concrete artifacts
the pitch must contain. See SPEC.md §1.5 item 3.>

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.
```

## END CANONICAL BLOCK

---

## Notes for QA

- Compare after normalizing: collapse runs of whitespace to a single space, normalize curly
  quotes (`“ ” ‘ ’`) to straight, and normalize the ellipsis character `…` to itself (do **not**
  expand it to `...` — the ellipsis in `"how to…"` is part of the locked text).
- The leading numeral form (`1.)`) is part of the locked text.
- A case that renumbers, merges, splits, softens ("try to participate"), or drops any of
  sections 1, 2, 4, 5 is a **BLOCKER**, not a POLISH note.
- Section 3's heading numeral `3.)` is locked; its contents are free.
