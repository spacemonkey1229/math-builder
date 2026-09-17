#!/usr/bin/env python3
"""
render_context.py — case.json's context_glossary[] is the source of truth; the published
Interactive HTML's STORY_GLOSSARY object, .sterm CSS, storyGlossaryCard, and
autoLinkStoryTerms() selector list are GENERATED from it. Closes the "Known gap" documented
in skills/case-context/SKILL.md: that scaffolding used to be hand-authored per case.

Modes:
  --case <id>              render case.json -> published HTML (the normal, forward direction)
  --case <id> --check      dry-run: report whether the HTML would change, exit 1 if so
  --case <id> --extract    reverse direction, ONE-TIME BACKFILL: read the existing
                            hand-authored STORY_GLOSSARY out of the HTML and write it into
                            case.json.context_glossary[], so a case authored before this
                            script existed doesn't regress on first --case run.

Usage:
    python3 skills/case-publish/scripts/render_context.py --case gerrymandering
    python3 skills/case-publish/scripts/render_context.py --case gerrymandering --check
    python3 skills/case-publish/scripts/render_context.py --case gerrymandering --extract

Idempotent: re-running --case with an unchanged context_glossary[] produces a byte-identical
file (the whole point — case.json drives the HTML, not the other way around, from here on).

What this script does NOT do: place images/<figure> blocks (real photo sourcing and captioning
still needs editorial judgment — see skills/case-context/SKILL.md's visual-sourcing section)
or write the .gterm math glossary (case-agnostic, from templates/INTERACTIVE_HTML_CONTRACT.md).
It only owns the STORY_GLOSSARY/.sterm layer.
"""
import argparse
import glob
import json
import os
import re
import sys

BEGIN_CSS = "/* BEGIN case-context AUTO-GENERATED CSS — edit case.json, not this block; see skills/case-publish/scripts/render_context.py */"
END_CSS = "/* END case-context AUTO-GENERATED CSS */"
BEGIN_JS = "/* BEGIN case-context AUTO-GENERATED STORY_GLOSSARY — edit case.json.context_glossary[], not this block; see skills/case-publish/scripts/render_context.py */"
END_JS = "/* END case-context AUTO-GENERATED STORY_GLOSSARY */"

STERM_CSS = """.sterm{position:relative;color:var(--navy-dk);text-decoration:none;border-bottom:1.5px dotted var(--ok);cursor:help;font-weight:600}
  .sterm:hover, .sterm:focus{background:var(--ok-bg)}
  .sterm .tip{visibility:hidden;opacity:0;position:absolute;left:50%;bottom:135%;transform:translateX(-50%);
    width:230px;background:var(--navy-dk);color:#fff;font-family:var(--sans);font-weight:400;font-size:.76rem;
    line-height:1.4;padding:9px 11px;border-radius:7px;box-shadow:0 4px 14px rgba(0,0,0,.25);transition:opacity .12s;z-index:30}
  .sterm .tip .go{display:block;margin-top:6px;color:var(--ok);font-weight:700}
  .sterm .tip:after{content:"";position:absolute;top:100%;left:50%;transform:translateX(-50%);border:6px solid transparent;border-top-color:var(--navy-dk)}
  .sterm:hover .tip, .sterm:focus .tip{visibility:visible;opacity:1}
  .glossary-grid .sterm{display:inline-block;background:#fff;border:1px solid var(--line);border-bottom:1.5px dotted var(--ok);
    border-radius:999px;padding:5px 12px;font-family:var(--sans);font-size:.82rem}
  .glossary-grid{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 16px}"""

DEFAULT_SELECTORS = ['#overview', '#background', '#dilemma', '#challenges', '#appendices', '#notebook', '#twist']

RENDER_JS = r"""function stermHTML(label, textOverride){
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
}"""


def js_str(s):
    """Render a Python string as a double-quoted JS string literal."""
    out = s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
    return f'"{out}"'


def find_html(project, cid):
    matches = glob.glob(os.path.join(project, 'cases', cid, 'published', '*Interactive.html'))
    if not matches:
        raise SystemExit(f"no published Interactive.html found for case '{cid}'")
    if len(matches) > 1:
        raise SystemExit(f"ambiguous: multiple Interactive.html files for '{cid}': {matches}")
    return matches[0]


def build_glossary_js(entries):
    lines = [BEGIN_JS, "const STORY_GLOSSARY = {"]
    for i, e in enumerate(entries):
        comma = "," if i < len(entries) - 1 else ""
        lines.append(f'  {js_str(e["term"])}: {{desc: {js_str(e["desc"])},')
        lines.append(f'    link: {js_str(e["link"])}}}{comma}')
    lines.append("};")
    lines.append(END_JS)
    return "\n".join(lines)


def build_card_html(domain_label):
    return (
        f'<div class="card" id="storyGlossaryCard">\n'
        f'  <strong>{domain_label} Vocabulary</strong>\n'
        f'  <p class="side-note" style="margin-top:6px">Hover any underlined term below (or in the prose\n'
        f'    above) for a plain-English definition; click to open a real source on it. This is separate\n'
        f'    from the math vocabulary in Appendix H &mdash; these are the {domain_label.lower()} words the story\n'
        f'    itself is told in.</p>\n'
        f'  <div class="glossary-grid" id="storyGlossaryGrid"></div>\n'
        f'</div>'
    )


def extract_existing_glossary(html):
    """Best-effort parse of a hand-authored STORY_GLOSSARY object into [{term,desc,link}]."""
    m = re.search(r'const STORY_GLOSSARY\s*=\s*\{(.*?)\n\};', html, re.S)
    if not m:
        return []
    body = m.group(1)
    entries = []
    for em in re.finditer(
        r'"((?:[^"\\]|\\.)*)"\s*:\s*\{\s*desc:\s*"((?:[^"\\]|\\.)*)"\s*,\s*link:\s*"((?:[^"\\]|\\.)*)"\s*\}',
        body, re.S,
    ):
        term, desc, link = em.groups()
        unesc = lambda s: s.replace('\\"', '"').replace('\\n', ' ').replace('\\\\', '\\')
        entries.append({"term": unesc(term), "desc": unesc(desc), "link": unesc(link)})
    return entries


def do_extract(project, cid):
    html_path = find_html(project, cid)
    html = open(html_path, encoding='utf-8').read()
    entries = extract_existing_glossary(html)
    if not entries:
        print(f"{cid}: no existing STORY_GLOSSARY found in HTML, nothing to extract")
        return
    case_json_path = os.path.join(project, 'cases', cid, 'case.json')
    d = json.load(open(case_json_path))
    if d.get("context_glossary"):
        print(f"{cid}: case.json.context_glossary[] already has {len(d['context_glossary'])} "
              f"entries — refusing to overwrite. Delete it first if you really want to re-extract.")
        return
    d["context_glossary"] = entries
    json.dump(d, open(case_json_path, 'w'), indent=2, ensure_ascii=False)
    print(f"{cid}: extracted {len(entries)} entries from HTML into case.json.context_glossary[]")


def render(project, cid, check_only):
    html_path = find_html(project, cid)
    html = open(html_path, encoding='utf-8').read()
    case_json_path = os.path.join(project, 'cases', cid, 'case.json')
    d = json.load(open(case_json_path))
    entries = d.get("context_glossary") or []
    if not entries:
        print(f"{cid}: case.json.context_glossary[] is empty — nothing to render. "
              f"Run --extract first if this case has a hand-authored STORY_GLOSSARY to migrate, "
              f"or run case-context to source real entries.")
        return False
    domain_label = d.get("context_domain_label", "Real-World")
    selectors = d.get("context_selectors") or DEFAULT_SELECTORS

    new_css_block = f"{BEGIN_CSS}\n  {STERM_CSS}\n  {END_CSS}"
    new_js_block = build_glossary_js(entries)
    new_autolink_call = (
        "autoLinkStoryTerms([" + ", ".join(js_str(s) for s in selectors) + "]);"
    )

    out = html
    changed = False

    # NOTE: every re.sub below uses a lambda/function replacement, never a plain string. re.sub
    # treats a STRING replacement's backslashes as backreference syntax (\1, \\, ...) and will
    # silently corrupt any literal backslash in the injected JS (e.g. the auto-linker's own
    # regex-escaping code) -- caught live 2026-09-16 when a generated file failed `node --check`.
    # A function replacement's return value is used verbatim, no escape processing.

    # 1. CSS block: replace if markers present, else insert before </style> if .sterm missing entirely.
    if BEGIN_CSS in out:
        out2 = re.sub(re.escape(BEGIN_CSS) + r'.*?' + re.escape(END_CSS),
                       lambda m: new_css_block, out, flags=re.S)
        changed = changed or (out2 != out)
        out = out2
    elif '.sterm{' not in out and '.sterm {' not in out:
        out2 = out.replace('</style>', f'  {new_css_block}\n</style>', 1)
        changed = changed or (out2 != out)
        out = out2
    # else: .sterm CSS already present but un-marked (hand-authored, pre-existing case) — leave it,
    # don't risk mangling hand-tuned CSS we can't safely locate the boundaries of.

    # 2. STORY_GLOSSARY JS object: replace if markers present; replace bare object if found un-marked;
    #    else insert before the first </script>'s closing (end of case-specific script section).
    if BEGIN_JS in out:
        out2 = re.sub(re.escape(BEGIN_JS) + r'.*?' + re.escape(END_JS),
                       lambda m: new_js_block, out, flags=re.S)
        changed = changed or (out2 != out)
        out = out2
    elif re.search(r'const STORY_GLOSSARY\s*=\s*\{.*?\n\};', out, re.S):
        out2 = re.sub(r'const STORY_GLOSSARY\s*=\s*\{.*?\n\};',
                       lambda m: new_js_block, out, count=1, flags=re.S)
        changed = changed or (out2 != out)
        out = out2
    else:
        # Fresh scaffold: also need renderStoryGlossary/autoLinkStoryTerms and the card.
        insertion = (
            f"\n{new_js_block}\n{RENDER_JS}\n{new_autolink_call}\n"
        )
        out2 = re.sub(r'(</script>\s*)$', lambda m: insertion + m.group(1), out, count=1, flags=re.M)
        if out2 == out:
            raise SystemExit(f"{cid}: could not find an insertion point (no closing </script>) — "
                              f"manual scaffold needed")
        changed = True
        out = out2
        if 'id="storyGlossaryCard"' not in out:
            card = build_card_html(domain_label)
            out2 = re.sub(r'(<section id="background">)', lambda m: m.group(1) + '\n' + card,
                           out, count=1)
            if out2 == out:
                print(f"{cid}: WARNING — no #background section found to insert storyGlossaryCard into; "
                      f"add it by hand.")
            else:
                out = out2
        # Fresh scaffold already emitted its own autoLinkStoryTerms call above; skip step 3.
        if check_only:
            print(f"{cid}: WOULD CHANGE (fresh scaffold)")
            return True
        open(html_path, 'w', encoding='utf-8').write(out)
        print(f"{cid}: scaffolded STORY_GLOSSARY + card + auto-link from scratch "
              f"({len(entries)} entries)")
        return True

    # 3. autoLinkStoryTerms(...) call: replace the existing call's argument list.
    out2 = re.sub(r'autoLinkStoryTerms\(\[[^\]]*\]\);', lambda m: new_autolink_call, out, count=1)
    changed = changed or (out2 != out)
    out = out2

    if check_only:
        if changed:
            print(f"{cid}: WOULD CHANGE")
        else:
            print(f"{cid}: up to date")
        return changed

    if changed:
        open(html_path, 'w', encoding='utf-8').write(out)
        print(f"{cid}: rendered {len(entries)} glossary entries into {os.path.basename(html_path)}")
    else:
        print(f"{cid}: already up to date, no write")
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--case', required=True)
    ap.add_argument('--project', default=os.getcwd())
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--extract', action='store_true')
    args = ap.parse_args()

    if args.extract:
        do_extract(args.project, args.case)
        return
    changed = render(args.project, args.case, args.check)
    if args.check and changed:
        sys.exit(1)


if __name__ == '__main__':
    main()
