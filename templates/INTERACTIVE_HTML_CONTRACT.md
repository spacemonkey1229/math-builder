# Interactive HTML — contract for `templates/interactive_shell.html`

**Roadmap A7.** Cold Chain's `published/*.html` was hand-built end to end; this doc plus the
shell template are the promised scaffold so case #2 doesn't repeat that from a blank file. This
does **not** change Cold Chain itself — it stays exactly as published. Nothing here is a new
DOCTRINE_LEDGER rule; MCS-37 and MCS-39 already specify the requirements this template exists to
satisfy without hand-transcription. See `skills/case-readiness/scripts/tier1_structural.py`
(`T1-18`, `T1-19`) for the actual enforcement — this document explains how to pass it on the
first try instead of by iteration.

---

## 1. How to use the shell

1. Copy `templates/interactive_shell.html` to `cases/<id>/published/<Title> - Interactive.html`.
2. Fill every `{{PLACEHOLDER}}` token. Grep the file for `{{` before you consider it done — an
   unfilled placeholder is invisible in a browser (it just renders as literal text) and will not
   fail any existing check, so it is easy to ship by accident.
3. Do not rename: the `--navy`/`--gold`/... CSS custom properties, the `.gterm`/`.tip`/
   `.glossary-grid` classes, the `gtermHTML`/`renderGlossary` function names, the `#glossaryVocab`/
   `#glossaryHowto` element ids, or `id="ha-logo"`. `T1-19` and the WCAG contrast pairs in
   `app/build_dashboard.py` (MCS-35 — if this HTML is ever surfaced there) assume this vocabulary
   holds across cases.
4. Everything else — banner art, appendix diagrams, the notebook's step count and check logic,
   the twist narrative — is genuinely case-specific. The shell gives you the frame and the
   generic mechanics (checklist, dilemma-pick, tab nav, glossary render); it cannot write your
   case's own arithmetic for you.
5. Run `case-readiness` Tier 1 (`T1-18`, `T1-19`) against the finished file before calling it
   done — the shell reduces mistakes, it does not replace the gate.

---

## 2. The `sensitivity_model.py` ↔ JS-port contract

Cold Chain's `cases/cold-chain/sensitivity_model.py` is the reference shape (see it for the full
implementation). A case's Working Notebook should call into a client-side port of the **same**
four names, so the printed page, the live calculator, and Tier 2 probe 5's sensitivity check can
never quietly diverge:

```python
PARAMS: dict[str, number]        # every dial the case states as an assumption
FLEX: list[str]                  # subset of PARAMS keys Tier 2 probe 5 perturbs ±50%
def evaluate(params, detour_h=0.0) -> dict     # {"A": metric, "B": metric}; higher is better
def evaluate_twist(params) -> dict             # same shape, with the twist's own perturbation applied
```

The JS port (in the shell's `{{CASE_JS_DATA_BLOCK}}`) should expose the same surface:

```js
const PARAMS = { /* same keys/values as the Python PARAMS, kept in sync by hand */ };
const FLEX = [ /* same keys as Python FLEX — drives which values the notebook lets a student flex */ ];
function evaluate(params, detourH = 0) { /* same arithmetic as the Python evaluate() */ return {A, B}; }
function evaluate_twist(params) { /* same arithmetic as the Python evaluate_twist() */ return {A, B}; }
```

**Why this matters, concretely:** Cold Chain did *not* do this — its JS `evaluate(openingCostH,
detourH)` (line ~708) is a hand-derived parallel implementation of the Python model, not a port
of it. That's how the two are able to silently drift; nothing currently checks they agree. For
case #2 onward, write the JS port first (or generate it from the Python file's arithmetic
directly) and have every Working Notebook `check*()` function call `evaluate()`/`evaluate_twist()`
rather than re-deriving the tally inline. This is a code-quality improvement Tier 1/Tier 2 do not
yet mechanically check — treat it as required by this contract, not just by convention, until a
future `T1` check exists to catch drift the way `T1-18`'s staleness sweep catches a stale build.

**Hard line, restated (MCS-37):** the notebook computes; it never prints the answer. Nothing in
the shell or a case's fill-in may render `balance_test.A_in_spec_doses`, `B_in_spec_doses`, or
`margin_pct` as a literal number anywhere outside a `<script>` tag's *computation* — not in a
comment, not in a "for teachers" aside, not pre-rendered into a table cell. `T1-18`'s leak check
is a boundary-aware literal-number regex over the **whole file**, not just prose — a number that
happens to also be a step in an intermediate calculation is fine; the *verdict itself*, printed
anywhere a reader could just read off the page without running the calculator, is a BLOCKER.

---

## 3. The starter glossary — what's genuinely reusable and what isn't

MCS-21 ("no URL from memory") applies to glossary links exactly as it applies to case data
sources. **A URL fetched and confirmed for one case is a legitimate source for the same term
reused verbatim in a different case** — that's not fabrication, it's citing a source you already
verified. **A new term, or a URL you haven't personally fetched for this case, is not** — fetch
and confirm it before shipping, every time, per MCS-39.

The 14 terms below are Cold Chain's own `GLOSSARY` object, verified live on `khanacademy.org` on
2026-08-01 (`cases/cold-chain/published/Cold Chain - Interactive.html`, lines 833–864). They are
general numeracy/measurement vocabulary, not Cold Chain-specific — almost any T1–T3 case will
touch several of them. Copy the ones your case actually uses verbatim (object shape and all);
do not re-verify them again unless a case gate later flags one as dead (MCS-28's re-verification
at gate time covers case data sources today, not glossary links — treat a dead glossary link the
same way if you find one: replace it, verify the replacement, don't leave it).

```js
const STARTER_GLOSSARY = {
  "Volume": {def: "The amount of three-dimensional space a shape encloses.",
    url: "https://www.khanacademy.org/math/geometry-home/geometry-volume-surface-area"},
  "Surface Area": {def: "The total area of every outside face of a 3-D shape, added together.",
    url: "https://www.khanacademy.org/math/geometry-home/geometry-volume-surface-area"},
  "Prism": {def: "A solid with two parallel, congruent polygon bases joined by rectangular side faces.",
    url: "https://www.khanacademy.org/math/geometry-home/geometry-volume-surface-area"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Unit": {def: "A defined quantity -- a centimeter, an hour, a liter -- used as a standard for measuring.",
    url: "https://www.khanacademy.org/math/cc-fifth-grade-math/imp-measurement-and-data-3"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \"per hundred.\"",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Decimal": {def: "A number written with place value to the right of a decimal point, e.g. 0.34.",
    url: "https://www.khanacademy.org/math/arithmetic/arith-decimals"},
  "Absolute Value": {def: "How far a number is from zero on the number line -- always zero or positive.",
    url: "https://www.khanacademy.org/math/algebra-home/alg-absolute-value"},
  "Scientific Notation": {def: "A compact way to write very large or very small numbers: a number from 1-10 times a power of 10.",
    url: "https://www.khanacademy.org/math/8th-grade-illustrative-math/unit-7-exponents-and-scientific-notation"},
  "Measurement": {def: "Assigning a number to a physical quantity -- length, time, mass -- using a chosen unit.",
    url: "https://www.khanacademy.org/math/cc-fifth-grade-math/imp-measurement-and-data-3"},
  "Distance": {def: "How far apart two points or places are.",
    url: "https://www.khanacademy.org/math/cc-fifth-grade-math/imp-measurement-and-data-3"},
  "Weight": {def: "A measure of how heavy something is.",
    url: "https://www.khanacademy.org/math/cc-fifth-grade-math/imp-measurement-and-data-3"},
  "Data": {def: "Facts or numbers collected for reference or analysis.",
    url: "https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-data-statistics"},
  "Bar Graph": {def: "A chart that uses rectangular bars to compare values across categories.",
    url: "https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-data-statistics"},
  "Mean": {def: "The \"average\": add up every value in a data set, then divide by how many values there are.",
    url: "https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/a/mean-median-and-mode-review"},
};
```

**This is a starter, not a ceiling.** MCS-39 requires ≥8 real terms; these 14 clear that floor
by themselves, but a case whose vocabulary is mostly *this* list rather than its own domain
content is thin — pull the case's own new-coverage skills (its `case.json.new_coverage[]`) into
the glossary too, fetching and confirming fresh links for each. The allowlist is fixed at
`khanacademy.org`, `mathsisfun.com`, `cuemath.com`, `purplemath.com`, `ck12.org`, `nctm.org`,
`openstax.org` (`tier1_structural.py`'s `ALLOWLIST_DOMAINS`) — a link to any other domain, however
good, is a `T1-19` BLOCKER.

---

## 4. Auto-linking — concepts get hover+hyperlink wherever they're actually used

MCS-39's own text asks for hover+hyperlink treatment on "any concepts that need explanation" —
not just a standalone list at the bottom of the page. Appendix G (§3 above) satisfies `T1-19`'s
letter (≥8 terms, allowlisted, hoverable, clickable), but by itself it doesn't put the explanation
anywhere near where a reader actually meets the term in the Overview, Background, Appendices, or
Working Notebook prose. The shell closes that gap itself, automatically — **an author does not
need to hand-wrap every mention.**

After `renderGlossary()` builds the Appendix G list, `autoLinkGlossaryTerms()` walks the
case-specific content sections (`#overview`, `#background`, `#dilemma`, `#challenges`,
`#appendices`, `#notebook`, `#twist`) and wraps the **first plain-text mention** of each `GLOSSARY`
key — case-insensitive, tolerating a simple trailing "s" the same way `case-reconcile`'s own term
matcher does — in the identical `gtermHTML()` hover+hyperlink treatment Appendix G uses. Write your
prose in normal English; if "Volume" is a glossary term and it appears in your Background
paragraph, it gets linked there automatically, once, the first time it's said. It is never
double-linked on a second or third mention in the same document — later repeats stay plain text on
purpose, so the page doesn't turn into a wall of dotted underlines.

**What it deliberately does not touch:** the Appendix G glossary block itself
(`id="apx-glossary"` — it's already the reference list, not a "mention" to auto-link over),
anything already inside a `.gterm` (no double-wrapping), and form controls
(`button`/`input`/`select`/`textarea`/`label`) where wrapping text would break interaction.

**Forcing a specific occurrence.** The auto-linker always takes the *first* mention in document
order. If a term should link somewhere other than its literal first appearance (e.g. it appears in
passing early on but the pedagogically right place is a later table), hand-author that one
occurrence as a static anchor with `data-term="Label"`:
```html
<span class="gterm-placeholder" data-term="Volume">…</span> <!-- filled by gtermHTML('Volume') at build/author time -->
```
or simply call `gtermHTML('Volume', 'volume')` inline when generating that spot. The auto-linker
seeds its "already linked" set from every hand-placed `.gterm[data-term]` **outside** Appendix G
before it scans, so it will skip that term everywhere else, including its literal first mention.
Get this wrong in either direction and it fails safe, not silently: forget the `data-term`
attribute and the auto-linker just links the first mention instead (no double-link, no broken
anchor) — the failure mode is "the obvious place" not "nothing happens."

**Verified against a filled fixture** (2026-08-01, this session): built a throwaway case with
"Volume" mentioned in both Overview and twice in Background, "Ratio" and "Surface Area" each
mentioned once. Confirmed by DOM inspection: `Volume` linked once (its first, Overview,
occurrence — not its Background repeats), `Ratio` and `Surface Area` linked once each at their
own first mention, Appendix G's own list still complete and independent (7 total `.gterm` anchors:
3 auto-linked in prose + 3 in the Appendix G grid + 1 in its how-to list). Zero console errors.
**Caught and fixed a real bug during that verification**: the first draft seeded `linked` from
*every* `.gterm[data-term]` on the page, including Appendix G's own — since Appendix G lists every
term by design, that pre-marked every single term as "already linked" before the scanner ever
looked at the prose, so nothing outside Appendix G ever got wrapped. Fixed to exclude
`#apx-glossary` from the seeding step, not just the scanning step.

---

## 5. CSV export — every appendix data table gets a download button, automatically

Every case must let a student pull any data table into Google Sheets/Excel, not just read it on
the page. The shell now does this for free — **an author does not need to hand-wire anything.**

**How it works.** Three pieces, all in the shell template already:

- CSS: `.csv-row` / `.csvbtn` (a small right-aligned button under each table).
- JS helpers, defined once near the top of the script block: `tableToCSV(table)` (serializes a
  `<table>` element's rows to RFC-4180-ish CSV — quotes any cell containing a comma, quote, or
  newline, doubles embedded quotes) and `downloadCSV(tableId, filename)` (builds a `Blob` with a
  UTF-8 BOM, so Excel opens it without mangling special characters, and triggers a browser
  download via a throwaway `<a download>` click).
- `autoAddCSVButtons(caseId)`, called once at the end of the script block (right after
  `autoLinkGlossaryTerms(...)`, alongside it): walks every `<table>` inside `#appendices`,
  assigns it an `id` if it doesn't already have one, derives a filename from `CASE_ID` plus the
  enclosing `<details>`'s `<summary>` text (stripped of a leading "Appendix X" label, slugified),
  and inserts a "⬇ Download CSV" button immediately after the table. It marks each table with
  `dataset.csvWired` so it's idempotent — safe to call more than once, safe if a case's own script
  also touches the DOM after load.

**What this means for you as an author:** write your appendix tables as normal `<table>` markup
inside `#appendices` (which every case already does — `T1-19`'s glossary grid and every worked
example lives there too). You get a working, correctly-named CSV download button on each one for
free. You do not need to give tables an `id`, write a button, or call any function yourself.

**If you want a specific filename or button placement** — e.g. two tables share a `<details>` and
you want distinct names — give the `<table>` an explicit `id="myTableId"` yourself;
`autoAddCSVButtons` respects an existing `id` rather than generating one, but still derives the
filename from the enclosing summary text, so distinct filenames still require either distinct
summaries or a manual `downloadCSV('myTableId', 'exact-name.csv')` button of your own instead of
relying on the auto-inserted one.

**Retrofit note (2026-08-01, this session):** all cases published before this feature existed
(Cold Chain, Baseball Lineup, and the six other legacy conversions in flight at the time) were
retrofitted with the same CSS/JS/button pattern by a one-off script, since they predate the shell
change and won't pick up `autoAddCSVButtons` just by being reloaded — the shell only affects files
copied from it *after* the change. Nuclear Waste's Appendix A–C had been written as prose `<p>`
tags rather than tables (the only case doing this) and were converted to real two-column
`<table>` markup first, specifically so the retrofit — and every future edit — has an actual table
to attach a button to. All nine retrofitted files were re-verified with `tier1_structural.py`
afterward: same `TIER1_PASS` status and GAP counts as before the retrofit, confirming the change
is additive (new buttons + CSS + JS helpers) and doesn't disturb anything Tier 1 checks.

---

## 6. The top-right toolbar — copy, whole-case PDF, per-table PDF, submission packet

Every case ships a small fixed toolbar in the top-right corner with three actions, plus a PDF
option next to every CSV button. All four are zero-dependency — no external library, no server,
nothing that can go stale or need a CDN allowlist entry. Everything leans on capabilities the
browser already has: `navigator.clipboard`, `document.execCommand('copy')` as a fallback, and
`window.print()` (the same mechanism a reader would reach for with Cmd/Ctrl+P).

**Copy.** `copyShareInfo()` builds a plain-text block — case title, a one-line program credit, the
footer's own `Sources` list, and the page's URL — and writes it to the clipboard. **Always has a
fallback path**: `navigator.clipboard.writeText()` is the primary route, but it can reject with
`NotAllowedError` in perfectly ordinary situations (no secure context, no recent user gesture by
the time the promise resolves, a strict permissions policy) — this is not a hypothetical, it is
what happened on the very first real test of this feature in this session. The `.catch()` falls
back to the classic hidden-`<textarea>` + `document.execCommand('copy')` pattern, which works
synchronously inside the same click handler. Don't remove the fallback branch to "simplify" this
function — it is the difference between the button working and silently doing nothing.

**Export PDF.** `exportCasePDF()` force-opens every `<details>` in `#appendices` (so nothing a
reader collapsed is missing from the printout) and calls `window.print()`. The student picks
"Save as PDF" in the OS print dialog — there is no separate PDF-generation code path to maintain.
A `@media print` block hides the toolbar itself, the nav tabs, every button, and the `.csv-row`
wrappers, and forces `details .inner` visible regardless of the `[open]` attribute — so a reader
who prints directly (Cmd/Ctrl+P, bypassing the button entirely) still gets a clean, complete
document, not a page full of interactive chrome and collapsed sections.

**Per-table PDF.** `autoAddCSVButtons()` (§5) now adds a second button next to every CSV button —
`printTable(tableId, title)` opens a new window containing just that one table, styled minimally,
and prints it. `printHTMLDoc(title, bodyHTML)` is the shared helper both `printTable()` and
`exportSubmissionPacket()` build on: it owns the popup-window boilerplate (inline stylesheet, no
external assets) so there is exactly one place that knows how a printable document is shaped.

**Submit.** `exportSubmissionPacket()` is explicitly **not** a live upload — case-track's real
intake is a per-learner Google Drive folder (see `skills/submission-score/SKILL.md`), and wiring a
live Drive API call from a static, credential-less HTML file is a different, much bigger piece of
work this button does not attempt. What it does: reads this Hero's own state back out of
`localStorage` — their dilemma pick, every Working Notebook field's current value and ✓/✗ status,
every deliverable checklist box and its note — and lays it out as a printable packet via the same
`printHTMLDoc()` helper. The Hero saves it as a PDF and drops it in their Drive submission folder
alongside their write-up. It reads the DOM generically (`#notebook .fieldrow`, the case's own
`DELIVERABLES` array) rather than hardcoding step ids, so it needs zero per-case wiring — the same
"case-agnostic in mechanism, case-specific only in content" shape as the checklist renderer in §1.

**Retrofit note (2026-08-02, this session):** the toolbar was added to the shell after 11 cases
already existed. Two of them (Cardiology, LeBron Vs. Michael) were built from the updated shell
directly. The other nine — including Cold Chain, the original hand-built case — were retrofitted
by a one-off script for the same reason the CSV retrofit needed one (§5): they predate the change
and don't pick it up just by being reloaded. All eleven were re-verified with `tier1_structural.py`
afterward with unchanged `TIER1_PASS` status and GAP counts — the toolbar is pure UI chrome with no
new case data, so it cannot trip `T1-18`'s number-continuity sweep any more than the CSV buttons
did.

---

## 7. `T1-18` / `T1-19` gotchas the shell exists to prevent

- **The balance-test leak check is boundary-aware but file-wide**, not scoped to prose. It
  matches comma-formatted, plain, and stringified-int forms of `A_in_spec_doses`,
  `B_in_spec_doses`, and `margin_pct` anywhere in the file, `<script>` tags included. A
  case-specific JS data block that accidentally hardcodes the *final* tally rather than the raw
  inputs the tally is computed from will trip this. Keep `{{CASE_JS_DATA_BLOCK}}` to raw given
  data (dimensions, prices, schedules) — never a pre-computed verdict.
- **The glossary check's JS-data-object detection is exact-shape.** Its regex is
  `"[A-Za-z][A-Za-z \-]*":\s*\{def:\s*"...",\s*url:\s*"(https://...)"` — double-quoted label keys,
  unquoted `def:`/`url:` property names, in that order, `https://` only. **If a JS data object is
  present at all, it becomes the sole source of truth for both the term count and URL validation
  — co-occurring static `<a class="gterm">` anchors are ignored**, specifically to avoid double
  counting an unrendered template literal (this bit Cold Chain's own first draft — see
  DOCTRINE_LEDGER MCS-39's change-log entry). Don't leave template placeholder text that looks
  like a `gterm` anchor sitting next to a real JS object; the checker will not merge them the way
  you might expect, and a real bad domain could hide next to an unresolved placeholder.
- **Staleness (`T1-18`) is mtime-based.** The `.html` file's modification time must be ≥
  `case.md`'s. If you're iterating on the shell fill-in after `case.md` was last edited, you're
  fine; if you edit `case.md` afterward (a late wording fix, a corrected figure), touch/resave the
  `.html` too or the gate will flag it stale even though the content might still agree.
- **Numbers outside `<script>` must trace to the case's own number universe** (`case.md`/
  `case.json`). Prose and table content in the placeholder sections is swept for orphan numbers;
  CSS/SVG decimals (opacity, stroke-width, viewBox coordinates) are the accepted false-positive
  class (Cold Chain's baseline: 110 accepted GAPs of exactly this kind) — don't spend time trying
  to eliminate those, but don't add new *data-shaped* numbers to markup without sourcing them.
- **`MANIFEST.json`'s `files[]` array doesn't currently list the interactive `.html`** — a
  documentation gap, not a gate failure (case-publish doesn't build or verify this file, it just
  leaves it in place). If you touch `skills/case-publish/SKILL.md`'s manifest template, add it.
- **The auto-linker (§4) is invisible to both static sweeps, and that's correct, not a loophole.**
  It runs client-side against the DOM, so the `.gterm` anchors it generates in prose never exist as
  literal text in the file `T1-18`/`T1-19` read — only the `GLOSSARY` object does, which is already
  T1-19's actual source of truth (§3 above). Nothing new to check; the count and URL validation are
  unaffected by whether or where a term happens to get auto-linked in prose.

---

## 8. What this doesn't solve yet

The shell templates the *mechanics*. It does not generate a case's diagrams, its narrative, or
its Working Notebook's specific check logic — those still take real authoring time per case,
same as `case.md` itself does. What it removes is re-deriving the CSS design system, the
checklist/localStorage plumbing, the dilemma-pick widget, and the glossary renderer from scratch
each time, and the drift risk of a hand-copied version of those subtly changing between cases.
