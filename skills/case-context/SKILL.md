---
name: case-context
description: "The repository of this project's standard for real-world explanation: sourced glossary terms with hover tooltips AND click-through hyperlinks, images/diagrams with citations, and per-deliverable why-notes — what to include (the 'fit' test) and the exact copy-paste CSS/JS/HTML implementation (the .sterm hover+hyperlink mechanism, STORY_GLOSSARY object, autoLinkStoryTerms wiring, <figure> pattern). Use when the user says \"add context to the case\", \"add hovers and hyperlinks\", \"source some background material\", \"this case needs explaining\", \"find an image for the case\", \"the terms aren't explained\", \"wire up the glossary\", or after case-research reports all numeric placeholders closed. Runs after case-research, before case-readiness. Never touches a load-bearing numeric figure — that stays case-research's job."
---

# case-context — real-world explanation, sourced like everything else

Stage between `case-research` and `case-readiness`. `case-research` sources every number the case's
*math* needs. This skill sources everything the case's *setting* needs — the vocabulary, the
picture, the "why this order of operations" reasoning — so a student with no background in
harbor piloting, contact tracing, or hardwood milling can still follow the story. Tier 2's P7
probe (MCS-48) checks the result; this skill is what produces it, so authoring stops relying on a
QA probe catching an absence a month after publish.

> The corpus-wide fix this project's own QA history keeps re-discovering (STORY_GLOSSARY on
> apron-order, then retrofitted onto lebron-vs-michael, tide-window, six-degrees-of-exposure,
> the-special-order, flow-state, gerrymandering — six separate after-the-fact repairs in one
> project) is proof this needs to be a pipeline stage, not a QA finding.

## Inputs

- `cases/<id>/case.md` and `cases/<id>/case.json` with `sources[]`/`needs_source[]` closed by
  `case-research`.
- Tools: `WebSearch` and `WebFetch` (load via ToolSearch if deferred).

## Outputs

- `cases/<id>/case.json` — `sources[]` gains 2-4 new context/visual entries (same schema as a
  data source: `id`, `claim`, `org`, `title`, `url`, `accessed`, `confidence`, `note`), plus a new
  `context_glossary[]` array: `[{term, desc, link, source_id}]`.
- `cases/<id>/case.md` — the chosen terms appear, in-context, somewhere in Overview/Background/
  Dilemma/Challenges/Appendices (not invented as a standalone vocabulary list divorced from the
  narrative), and a short "Context Sources" note naming what was added and why.
- The published HTML's `STORY_GLOSSARY` object, its `.sterm` wiring, and any `<figure>` — hand-
  placed to match `case.json.context_glossary[]`/`sources[]` until a templated generator exists
  (there isn't one yet; see "Known gap" below).

---

## The implementation standard — hovers AND hyperlinks, copy-paste ready

This is the part that was missing: not just *what* to source, but the exact mechanism that turns
a sourced term into something a student actually sees — a dotted-underline term that shows a
plain-English tooltip on hover/focus, and is *also* a real `<a href>` a student can click through
to the source. Every one of this corpus's compliant cases (`apron-order`, then retrofitted onto
`lebron-vs-michael`, `tide-window`, `six-degrees-of-exposure`, `the-special-order`, `flow-state`,
`gerrymandering`) uses this identical mechanism. Copy it verbatim; only the glossary content and
selector list change per case.

**Two separate, parallel layers — never merge them:**

| | Math vocabulary | Story/domain vocabulary |
|---|---|---|
| JS object | `GLOSSARY` | `STORY_GLOSSARY` |
| CSS class | `.gterm` | `.sterm` |
| Field names | `{def, url}` | `{desc, link}` — deliberately different keys so the two can never collide |
| Render fn | `termHTML()` / `renderGlossary()` | `stermHTML()` / `renderStoryGlossary()` |
| Auto-link fn | `autoLinkGlossaryTerms()` | `autoLinkStoryTerms()` |
| Card container | `#glossaryVocab` (Appendix G, SPEC §1.7, case-agnostic) | `#storyGlossaryCard` / `#storyGlossaryGrid` |
| Accent color | gold/amber | green (`--ok`) |

They share one hover-tooltip CSS mechanism (`.tip`), just with different accent tokens, so the two
layers are visually distinguishable at a glance without looking like two different systems.

### 1. CSS — add once per case, alongside the existing `.gterm` rules

```css
/* ---- story/domain-vocabulary hover + hyperlink terms -- a SEPARATE
       layer from .gterm (math vocabulary). Same tooltip mechanism,
       different accent color (ok-green instead of gold) so the two
       layers are visually distinguishable at a glance. ---- */
.sterm{position:relative;color:var(--navy-dk);text-decoration:none;border-bottom:1.5px dotted var(--ok);cursor:help;font-weight:600}
.sterm:hover, .sterm:focus{background:var(--ok-bg)}
.sterm .tip{visibility:hidden;opacity:0;position:absolute;left:50%;bottom:135%;transform:translateX(-50%);
  width:230px;background:var(--navy-dk);color:#fff;font-family:var(--sans);font-weight:400;font-size:.76rem;
  line-height:1.4;padding:9px 11px;border-radius:7px;box-shadow:0 4px 14px rgba(0,0,0,.25);transition:opacity .12s;z-index:30}
.sterm .tip .go{display:block;margin-top:6px;color:var(--ok);font-weight:700}
.sterm .tip:after{content:"";position:absolute;top:100%;left:50%;transform:translateX(-50%);border:6px solid transparent;border-top-color:var(--navy-dk)}
.sterm:hover .tip, .sterm:focus .tip{visibility:visible;opacity:1}
.glossary-grid .sterm{display:inline-block;background:#fff;border:1px solid var(--line);border-bottom:1.5px dotted var(--ok);
  border-radius:999px;padding:5px 12px;font-family:var(--sans);font-size:.82rem}
.glossary-grid{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 16px}
```

Requires the shared design tokens already in every case's `:root` (`--navy-dk`, `--ok`,
`--ok-bg`, `--line`, `--card`, `--sans`) — if a case's palette uses different token names, map
these to the equivalent, don't hardcode colors.

### 2. HTML — the glossary card, placed in Background (or wherever the terms cluster)

```html
<div class="card" id="storyGlossaryCard">
  <strong>{{DOMAIN}} Vocabulary</strong>
  <p class="side-note" style="margin-top:6px">Hover any underlined term below (or in the prose
    above) for a plain-English definition; click to open a real source on it. This is separate
    from the math vocabulary in Appendix H &mdash; these are the {{DOMAIN}} words the story
    itself is told in.</p>
  <div class="glossary-grid" id="storyGlossaryGrid"></div>
</div>
```

`{{DOMAIN}}` is the case's own setting in plain words — "Cutting-Room," "Sports-Media,"
"Maritime," "Public-Health," "Shop" — not a generic label.

### 3. JS — the data object, render function, and auto-linker (end of the case-specific `<script>` block)

```javascript
/* ================================================================
   CASE-SPECIFIC -- story/domain-vocabulary glossary (separate layer
   from GLOSSARY/gterm above, which stays math-only and untouched).
   Same render + auto-link mechanism, ported to the .sterm class so
   the two layers never collide in T1-19's math-glossary count. Every
   url is a real, live, freely-accessible page, verified {{DATE}}.
   ================================================================ */
const STORY_GLOSSARY = {
  "{{Term}}": {desc: "Plain-English definition, 1-2 sentences, tied to how this case actually uses the term -- not a dictionary-style generic definition.",
    link: "https://real-source-for-this-term"},
  // ...2-4 entries total, per the "fit" test above
};
function stermHTML(label, textOverride){
  const g = STORY_GLOSSARY[label];
  if(!g) return textOverride || label;
  const text = textOverride || label;
  return `<a class="sterm" data-sterm="${label}" href="${g.link}" target="_blank" rel="noopener">${text}<span class="tip">${g.desc}<span class="go">Open a real source on this &rarr;</span></span></a>`;
}
function renderStoryGlossary(){
  const el = document.getElementById('storyGlossaryGrid');
  if(!el) return;
  el.innerHTML = Object.keys(STORY_GLOSSARY).map(k => stermHTML(k)).join('');
}
renderStoryGlossary();

function autoLinkStoryTerms(containerSelectors){
  const linked = new Set();
  document.querySelectorAll('.sterm[data-sterm]').forEach(a => {
    if(!a.closest('#storyGlossaryCard')) linked.add(a.dataset.sterm);
  });
  const terms = Object.keys(STORY_GLOSSARY).sort((a, b) => b.length - a.length);
  if(!terms.length) return;
  const esc = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const master = new RegExp('\\b(' + terms.map(t => esc(t) + 's?').join('|') + ')\\b', 'gi');
  const keyFor = raw => terms.find(t => raw.toLowerCase() === t.toLowerCase() || raw.toLowerCase() === (t + 's').toLowerCase());
  const skip = 'script, style, .gterm, .sterm, #apx-glossary, #storyGlossaryCard, button, input, select, textarea, label';
  const roots = [];
  containerSelectors.forEach(sel => document.querySelectorAll(sel).forEach(el => roots.push(el)));
  roots.forEach(root => {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode(node){
        if(!node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        const p = node.parentElement;
        if(!p || p.closest(skip)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    const nodes = [];
    let n; while((n = walker.nextNode())) nodes.push(n);
    nodes.forEach(node => {
      const text = node.nodeValue;
      master.lastIndex = 0;
      let m, lastEnd = 0, frag = null;
      while((m = master.exec(text))){
        const key = keyFor(m[0]);
        if(!key || linked.has(key)) continue;
        linked.add(key);
        if(!frag) frag = document.createDocumentFragment();
        if(m.index > lastEnd) frag.appendChild(document.createTextNode(text.slice(lastEnd, m.index)));
        const span = document.createElement('span');
        span.innerHTML = stermHTML(key, m[0]);
        frag.appendChild(span.firstChild);
        lastEnd = m.index + m[0].length;
      }
      if(frag){
        if(lastEnd < text.length) frag.appendChild(document.createTextNode(text.slice(lastEnd)));
        node.parentNode.replaceChild(frag, node);
      }
    });
  });
}
// MUST include every section id where a story term could appear, including
// appendices -- the single most common real defect this corpus has shipped
// (5 of 6 Week 4 cases, 2026-09-15 Tier 2 P7 audit) is scoping this to only
// #overview/#background/#dilemma/#challenges and missing the appendix
// tables, where a lot of real-world vocabulary actually first shows up.
autoLinkStoryTerms(['#overview', '#background', '#dilemma', '#challenges', '#appendices', '#notebook', '#twist']);
```

`autoLinkStoryTerms` does first-occurrence-wins auto-linking (longest term first, so a compound
term like "charter-party" is matched before the shorter "charter" inside it), skips anything
already inside `.gterm`/`.sterm`/the glossary cards themselves, and matches a trailing plural `s`
automatically. Running it is what turns a term merely *defined in the card* into a term that's
*also underlined and hoverable the first time it appears in the actual prose* — both halves
("hovers and hyperlinks") only exist together if this call runs with the right selector list.

### 4. Images — the same `<figure>` pattern, real or hand-drawn

```html
<figure>
  <img src="https://upload.wikimedia.org/wikipedia/commons/..." alt="Descriptive alt text" style="max-width:100%;height:auto;border-radius:6px;display:block;margin:0 auto">
  <figcaption>What this shows and why it's here. Photo/Diagram: Creator Name, Wikimedia Commons, LICENSE.</figcaption>
</figure>
```

For a hand-drawn SVG in place of `<img>`, keep the same `<figure>`/`<figcaption>` wrapper — the
figcaption still needs to say what's real data vs. an invented illustrative example (see
`cases/gerrymandering/`'s Appendix B chart caption for the pattern: real axis values, explicitly
labeled as this case's own real figures, not a stock illustration).

---

## Confidence tiers — reuse case-research's rubric, don't invent a stricter one

This was a real, live mistake (caught 2026-09-16): treating "reputable outlet republishes an
image with a named attribution" as *disqualifying* rather than as exactly what
`skills/case-research/SKILL.md`'s own Tier 3 = MEDIUM already covers. **The rubric is the same
one case-research already uses** — there is no separate, stricter bar for context/visual
material:

| Tier | Source class | Grade | Usable for context/visual? |
|---|---|---|---|
| 1-2 | Primary publisher, or an institution republishing it with attribution | HIGH | Yes |
| 3 | Reputable journalism/outlet naming a real source (incl. Wikimedia Commons with a real uploader and file history) | MEDIUM | **Yes** — this is the normal case, not an edge case |
| 4 | Undated blog/forum/AI-summary with no traceable provenance | LOW | Only as explicitly-labeled decorative noise; never for a claim a student is meant to rely on |

The one real distinction that matters: **is this material load-bearing for the graded math, or
is it illustrative/explanatory?** A LOW-confidence figure may never carry a constraint or a
dilemma-flipping quantity (case-research's rule, unchanged). A MEDIUM-confidence *image or
glossary term* is completely normal — most of this corpus's existing STORY_GLOSSARY links are
MEDIUM-tier Wikipedia pages, and that's fine, because nothing about "a term is explained" is a
graded quantity. Don't apply data-figure strictness to a sentence that just tells a 14-year-old
what a "kerf" is.

## The "fit" test — which 2-4 terms/visuals actually make the cut

Sourcing something real is necessary but not sufficient. A glossary of correct-but-irrelevant
trivia is as useless as no glossary. A candidate term or image is a **fit** only if it clears all
four:

1. **It's already in the case.** The term appears verbatim somewhere in `case.md`'s own
   Overview/Background/Dilemma/Challenges/Appendices, or a visual would illustrate a scene,
   object, or mechanism the case's own narrative describes. Do not import a generic "fun fact"
   about the setting that the case never actually mentions — that's decoration, not
   accessibility.
2. **It would stop a genuinely fresh reader.** Ask, term by term: would someone with zero
   background in this setting (not zero math background — zero *setting* background) need to
   look this up to follow the sentence it's in? If a plainer synonym already sits next to it in
   the sentence, or context makes the meaning obvious, it doesn't need a glossary entry — adding
   one anyway just clutters the card. This is literally Tier 2 P7's own test
   (`skills/case-readiness/scripts/tier2_probes.py`, `probe_accessibility`); running that probe's
   prompt yourself, in character as a zero-context reader, before publishing is the actual
   fit-check, not a proxy for it.
3. **It doesn't leak the case.** No context term, image caption, or diagram may state or imply a
   verdict, margin, or computed result — same no-answer-leak rule that already governs every other
   part of the case.
4. **It's real and cited**, at minimum MEDIUM confidence per the table above. Never fabricate a
   definition or invent a citation to clear the 2-4 minimum — an honest 1 beats a padded 3.

If fewer than 2 terms clear all four bars, ship fewer than 2 and say so in the Context Sources
note — the same "an honest hole beats a fabricated fill" principle `case-research` already
applies to numeric placeholders. If a case's setting is already fully self-explanatory (rare, but
real — a case set in a school cafeteria needs no glossary), record that explicitly rather than
padding.

## Visual sourcing, specifically

Prefer, in order:

1. A real photo or diagram with traceable provenance (a named photographer/creator, a real
   institution, or Wikimedia Commons with real file history and an explicit license) —
   Tier 1-3/HIGH-MEDIUM per the table above. Embed as `<figure><img src="..."><figcaption>...
   credit + license...</figcaption></figure>`, matching the pattern already in
   `cases/tide-window/published/` and `cases/lebron-vs-michael/published/`.
2. A hand-drawn, self-contained inline SVG when no real image clears the bar for this specific
   case, or when a diagram needs to show this case's own invented numbers (which a real photo
   obviously can't) — matching `cases/roofline-call/` and `cases/the-trailer-return/`'s
   convention. An invented illustrative example (not this case's real numbers) is fine and should
   say so in a caption, same as `cases/gerrymandering/`'s Appendix B population chart.
3. Nothing, with a note explaining why (a genuinely abstract topic with no natural visual) — never
   force a decorative image that adds nothing.

A found real image with the *wrong* license (all-rights-reserved stock photography, a paywalled
outlet's own uncredited graphic) is not usable regardless of how well it illustrates the point —
license is a hard gate the confidence tier does not override.

## The generator — `case.json` is the source of truth, the HTML is generated

As of 2026-09-16 this gap is closed: `skills/case-publish/scripts/render_context.py` renders
`case.json.context_glossary[]` (an array of `{term, desc, link}`) into the published HTML's
`STORY_GLOSSARY` object, `.sterm` CSS, `#storyGlossaryCard`, and the `autoLinkStoryTerms([...])`
call — the same mechanism documented above, now generated instead of hand-typed per case.

```bash
python3 skills/case-publish/scripts/render_context.py --case <id>            # render case.json -> HTML
python3 skills/case-publish/scripts/render_context.py --case <id> --check    # dry-run, exit 1 if stale
python3 skills/case-publish/scripts/render_context.py --case <id> --extract  # one-time backfill: pull an
                                                                              # existing hand-authored
                                                                              # STORY_GLOSSARY OUT of the
                                                                              # HTML into case.json (use
                                                                              # this once per case authored
                                                                              # before this script existed)
```

This skill's actual workflow is now: source the 2-4 terms per the fit test above, write them into
`case.json.context_glossary[]` (plus an optional `context_domain_label`, e.g. `"Cutting-Room"`,
and `context_selectors` if a case needs a non-default section list), then run the script — no
hand-editing HTML. It's idempotent (re-running with an unchanged `context_glossary[]` produces a
byte-identical file) and handles three cases: a case with markers already present (replaces
between them), a case with a hand-authored-but-unmarked `STORY_GLOSSARY` (upgrades it in place,
wrapping it in markers so future runs are safe), and a case with no `STORY_GLOSSARY` at all
(scaffolds the full CSS/card/JS from scratch). Regression-tested:
`skills/case-publish/scripts/selftest_render_context.py` — run it after any edit to
`render_context.py`, the same discipline `tier1_structural.py`/`selftest_tier1.py` already follow.

**What it still does not do:** place `<figure>`/`<img>` visual blocks. Real image sourcing,
captioning, and placement decisions still need editorial judgment (see "Visual sourcing,
specifically" above) — this generator only owns the glossary/hover/hyperlink layer.
