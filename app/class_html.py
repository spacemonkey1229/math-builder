"""app/class_html.py — HTML for the weekly-class lane (see admin_core.py's
"weekly class cases" section). Shared by both servers (app/admin_server.py,
local; app/admin_web/app.py, hosted) the same way admin_html.py and
student_portal_html.py already are -- one render function, two thin routing
shims on top.
"""
import html as _html
import re as _re


def render_class_case_html(case, err=None):
    open_case_inner = (
        f'<a class="btn" id="open-case-btn" href="{_html.escape(case["interactive_path"])}" target="_blank" '
        'rel="noopener" aria-disabled="true">Open the case &rarr;</a>'
        '<p class="det" style="margin-top:8px">This opens in a <strong>new tab</strong>. Work through it there, '
        'then click the case\'s own <strong>Submit</strong> button (top right) to turn your work into a PDF -- '
        'then come back to <strong>this</strong> tab to upload it below.</p>'
        if case["interactive_path"] else
        '<p class="det">(No interactive page for this case -- work from the printed/shared case sheet.)</p>'
    )
    err_html = f'<div class="err">{_html.escape(err)}</div>' if err else ''
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_html.escape(case['title'])} — Math Builder</title>
<style>
:root{{--paper:#FAF8F4;--ink:#16140F;--muted:#5F594E;--rule:#DED8CC;--accent:#22406B;--flag:#A93A1E;--flag-soft:#F8E7E1;--ok:#2E5E3E}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Arial,sans-serif;background:var(--paper);color:var(--ink);
  display:flex;justify-content:center;padding:28px 16px}}
main{{max-width:560px;width:100%}}
.card{{background:#fff;border:1px solid var(--rule);border-radius:10px;padding:24px;box-shadow:0 4px 14px rgba(24,20,12,.06);margin-bottom:16px;
  transition:opacity .15s}}
.card.locked{{opacity:.45;pointer-events:none}}
.step{{font-size:11px;font-weight:700;letter-spacing:.04em;color:var(--accent);text-transform:uppercase;margin:0 0 6px}}
h1{{font-size:19px;margin:0 0 6px}}
p.sub{{font-size:13px;color:var(--muted);margin:0 0 16px}}
.det{{font-size:12.5px;color:var(--muted)}}
label{{display:block;font-size:12.5px;font-weight:600;margin:14px 0 6px}}
label:first-of-type{{margin-top:0}}
input[type=text],textarea{{width:100%;padding:9px 10px;border:1px solid var(--rule);border-radius:6px;font-size:14px;font-family:inherit}}
textarea{{min-height:80px;resize:vertical}}
input[type=file]{{font-size:13px}}
.btn{{display:inline-block;padding:9px 16px;background:var(--accent);color:#fff;border:none;border-radius:6px;
  cursor:pointer;font-weight:600;font-size:14px;text-decoration:none;margin-top:6px}}
.btn:disabled,.btn[aria-disabled=true]{{opacity:.4;cursor:default;pointer-events:none}}
.err{{color:var(--flag);background:var(--flag-soft);border-radius:6px;padding:8px 10px;font-size:13px;margin-bottom:14px}}
.ok{{color:var(--ok);background:#E7F2EA;border-radius:6px;padding:10px;font-size:13.5px}}
</style></head><body><main>
<div class="card">
  <p class="step">Step 1</p>
  <h1>{_html.escape(case['title'])}</h1>
  <p class="sub">{_html.escape(case.get('primary_metric') or '')}</p>
  <label for="name">Your name</label>
  <input type="text" id="name" placeholder="First and last name" autofocus>
</div>
<div class="card locked" id="open-card">
  <p class="step" id="open-hint">Step 2 &middot; enter your name above first</p>
  {open_case_inner}
</div>
<div class="card locked" id="form-card">
  <p class="step">Step 3</p>
  {err_html}
  <div id="pre-submit">
    <label for="pdf">Upload your submitted PDF</label>
    <input type="file" id="pdf" accept="application/pdf">
    <label for="photo">Photo of extra work (optional)</label>
    <input type="file" id="photo" accept="image/*" capture="environment">
    <label for="answer">Anything you want to add? (optional)</label>
    <textarea id="answer" placeholder="Notes for your guide, or your answer if the PDF didn't work out"></textarea>
    <div><button class="btn" id="submit-btn" type="button">Submit</button></div>
  </div>
  <div id="post-submit" style="display:none" class="ok">Got it -- thanks! You can close this page now.</div>
</div>
</main>
<script>
var nameInput = document.getElementById('name');
var openCard = document.getElementById('open-card');
var formCard = document.getElementById('form-card');
var openBtn = document.getElementById('open-case-btn');
var openHint = document.getElementById('open-hint');
function syncLock() {{
  var has = nameInput.value.trim().length > 0;
  openCard.classList.toggle('locked', !has);
  formCard.classList.toggle('locked', !has);
  openHint.textContent = has ? 'Step 2' : 'Step 2 · enter your name above first';
  if (openBtn) {{
    if (has) openBtn.removeAttribute('aria-disabled'); else openBtn.setAttribute('aria-disabled', 'true');
  }}
}}
nameInput.addEventListener('input', syncLock);
syncLock();

document.getElementById('submit-btn').onclick = async function() {{
  var name = nameInput.value.trim();
  var answer = document.getElementById('answer').value.trim();
  var pdf = document.getElementById('pdf').files[0];
  var photo = document.getElementById('photo').files[0];
  if (!name) {{ alert('Please enter your name at the top first.'); return; }}
  if (!pdf && !answer && !photo) {{ alert('Upload your PDF (or add a photo / note) before submitting.'); return; }}
  var btn = document.getElementById('submit-btn');
  btn.disabled = true; btn.textContent = 'Submitting...';
  var fd = new FormData();
  fd.append('case_id', {case['id']!r});
  fd.append('student_name', name);
  fd.append('answer_text', answer);
  if (pdf) fd.append('pdf', pdf);
  if (photo) fd.append('photo', photo);
  try {{
    var res = await fetch('/api/class-submit', {{method: 'POST', body: fd}});
    var out = await res.json();
    if (!res.ok || out.error) throw new Error(out.error || 'submit failed');
    document.getElementById('pre-submit').style.display = 'none';
    document.getElementById('post-submit').style.display = 'block';
  }} catch (e) {{
    alert('Could not submit: ' + e.message);
    btn.disabled = false; btn.textContent = 'Submit';
  }}
}};
</script>
</body></html>"""


_LEVEL_COLORS = {
    "prealg": ("#A6472A", "#F5E4DC"),
    "alg":    ("#3D5A99", "#E5E9F5"),
    "geo":    ("#2B6E63", "#E4F0EC"),
    "adv":    ("#347F80", "#E1EFEE"),
    "adv2":   ("#1F5F6B", "#DDEBEC"),
    "disc":   ("#96631E", "#F5EADA"),
    "stat":   ("#7A4C9E", "#EFE5F5"),
}
_DEFAULT_LEVEL_COLOR = ("#5F594E", "#EDEAE1")

# One 64x64 illustrative glyph per level_key, inlined per-card exactly like
# the reference design (no shared <symbol>/<use> sprite) -- currentColor so
# each one picks up the card's --gold-ink icon tile color automatically.
_LEVEL_ICONS = {
    "prealg": '<rect x="8" y="26" width="48" height="4" fill="currentColor"/>'
              '<text x="16" y="20" font-family="Georgia,serif" font-size="16" fill="currentColor">3</text>'
              '<text x="16" y="46" font-family="Georgia,serif" font-size="16" fill="currentColor">4</text>',
    "alg":    '<text x="10" y="40" font-family="Georgia,serif" font-size="26" font-style="italic" '
              'fill="currentColor">x=y</text>',
    "geo":    '<polygon points="32,10 54,50 10,50" fill="none" stroke="currentColor" stroke-width="3"/>'
              '<path d="M32,50 A18,18 0 0 1 42,33" fill="none" stroke="currentColor" stroke-width="2" '
              'stroke-dasharray="2,2"/>',
    "adv":    '<path d="M4,32 C14,10 22,10 32,32 C42,54 50,54 60,32" fill="none" stroke="currentColor" '
              'stroke-width="3"/>',
    "adv2":   '<path d="M6,50 C20,50 24,14 40,14 C50,14 54,26 58,26" fill="none" stroke="currentColor" '
              'stroke-width="3"/><line x1="16" y1="46" x2="40" y2="30" stroke="currentColor" stroke-width="1.6" '
              'stroke-dasharray="3,3"/>',
    "disc":   '<circle cx="14" cy="16" r="5" fill="currentColor"/><circle cx="50" cy="16" r="5" fill="currentColor"/>'
              '<circle cx="32" cy="48" r="5" fill="currentColor"/>'
              '<line x1="14" y1="16" x2="50" y2="16" stroke="currentColor" stroke-width="2"/>'
              '<line x1="14" y1="16" x2="32" y2="48" stroke="currentColor" stroke-width="2"/>'
              '<line x1="50" y1="16" x2="32" y2="48" stroke="currentColor" stroke-width="2"/>',
    "stat":   '<rect x="10" y="34" width="10" height="20" fill="currentColor"/>'
              '<rect x="27" y="18" width="10" height="36" fill="currentColor"/>'
              '<rect x="44" y="26" width="10" height="28" fill="currentColor"/>',
}
_DEFAULT_LEVEL_ICON = '<circle cx="32" cy="32" r="18" fill="none" stroke="currentColor" stroke-width="3"/>'


def render_catalog_html(weeks_data):
    """The public, unauthenticated /catalog page -- "Class Cases", a real-time
    card catalog built straight from whatever the guide has configured via
    /class-review's own week-list editor (admin_core.get_public_catalog(),
    which itself reuses do_get_weekly_cases() + the public-safe
    get_case_brief(), never get_case_facilitator_brief()). weeks_data is
    get_public_catalog()'s return: [{"label": "Week 1"|None, "cases": [
    {id, title, interactive_path, class_path, level, level_key, field, role,
    concepts: [...], ask}, ...]}, ...].

    Deliberately shows no margin/percentage figure anywhere -- that data is
    intentionally absent from get_case_brief() and must stay absent here
    too (MCS-45's public/gated boundary). The card's button points at
    class_path (/class/<id>, the same public submission flow /class-review
    itself links students to) -- this page doubles as the student's actual
    entry point for the week, not just a browsing index.

    All weeks render into the page at once as their own <section id="week-N">;
    a sticky row of anchor links jumps between them -- plain in-page
    navigation, no JS required, so a direct link like /catalog#week-3 always
    lands on the right section even with scripts off."""
    has_any = any(w['cases'] for w in weeks_data)

    def _icon(level_key):
        return _LEVEL_ICONS.get(level_key or '', _DEFAULT_LEVEL_ICON)

    def _card(c):
        concepts = c.get('concepts') or []
        concepts_html = _html.escape(', '.join(concepts)) if concepts else '&mdash;'
        btn = (
            f'<a class="btn" href="{_html.escape(c["class_path"])}" target="_blank" rel="noopener">'
            'Open the case &amp; submit &rarr;</a>'
            if c.get('interactive_path') else
            '<span class="btn" style="opacity:.5;cursor:default">Not yet available</span>'
        )
        return (
            '<div class="card">'
            '<div class="card-top">'
            f'<div class="icon"><svg viewBox="0 0 64 64">{_icon(c.get("level_key"))}</svg></div>'
            '<div class="titles">'
            f'<span class="tag">{_html.escape(c.get("level") or "Unrated")}</span>'
            f'<h3>{_html.escape(c["title"])}</h3>'
            '</div></div>'
            f'<p class="ask">{_html.escape(c.get("ask") or "")}</p>'
            '<table class="details">'
            f'<tr><th>Field</th><td>{_html.escape(c.get("field") or "&mdash;")}</td></tr>'
            f'<tr><th>Role</th><td>{_html.escape(c.get("role") or "&mdash;")}</td></tr>'
            f'<tr><th>Concepts</th><td>{concepts_html}</td></tr>'
            '</table>'
            f'{btn}'
            '</div>'
        )

    def _week_section(i, w):
        label = w.get('label') or 'This week'
        cards = "".join(_card(c) for c in w['cases'])
        return (
            f'<h2 class="week-h" id="week-{i}">{_html.escape(label)}</h2>'
            f'<div class="grid">{cards}</div>'
        )

    jump_html = "".join(
        f'<a href="#week-{i}">{_html.escape(w.get("label") or "This week")}</a>'
        for i, w in enumerate(weeks_data)
    ) if len(weeks_data) > 1 else ''

    sections_html = (
        "".join(_week_section(i, w) for i, w in enumerate(weeks_data))
        if has_any else
        '<p class="empty-note">No cases are published to the catalog yet -- check back soon.</p>'
    )

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Class Cases — Math Builder</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Source+Sans+3:wght@400;500;600;700&display=swap">
<style>
:root{{
  color-scheme: light dark;
  --ink:#1a2e44; --ink-soft:#3d5266; --ground:#faf8f4; --surface:#ffffff;
  --line:#e4ded2; --muted:#5f5a50; --gold:#b4802b; --gold-ink:#7a5620; --gold-bg:#f7edd9;
  --btn-bg:#1a2e44; --btn-bg-hover:#7a5620;
  --shadow: 0 1px 2px rgba(26,46,68,.06), 0 6px 20px rgba(26,46,68,.05);
}}
@media (prefers-color-scheme: dark){{
  :root:not([data-theme="light"]){{
    --ink:#eef1f5; --ink-soft:#c3ccd6; --ground:#12161c; --surface:#1a1f27;
    --line:#2b323d; --muted:#a7b0bb; --gold:#e0ab52; --gold-ink:#f3cb84; --gold-bg:#2c2413;
  }}
}}
:root[data-theme="dark"]{{
  --ink:#eef1f5; --ink-soft:#c3ccd6; --ground:#12161c; --surface:#1a1f27;
  --line:#2b323d; --muted:#a7b0bb; --gold:#e0ab52; --gold-ink:#f3cb84; --gold-bg:#2c2413;
}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--ground);color:var(--ink);font-family:"Source Sans 3",-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1180px;margin:0 auto;padding:40px 22px 80px}}
header.page{{padding-bottom:22px;margin-bottom:8px;border-bottom:1px solid var(--line)}}
.eyebrow{{font-size:12.5px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--gold-ink)}}
h1{{font-family:"Fraunces",ui-serif,Georgia,serif;font-weight:600;font-size:clamp(26px,4vw,36px);line-height:1.1;margin:6px 0 6px;text-wrap:balance}}
p.sub{{color:var(--muted);font-size:15px;max-width:66ch;line-height:1.5;margin:0}}
nav.jump{{position:sticky;top:0;z-index:5;display:flex;gap:8px;flex-wrap:wrap;margin:24px -22px 8px;padding:12px 22px;
  background:var(--ground);border-bottom:1px solid var(--line)}}
nav.jump a{{font-size:13px;font-weight:600;color:var(--ink-soft);text-decoration:none;padding:6px 13px;
  border:1px solid var(--line);border-radius:999px;background:var(--surface)}}
nav.jump a:hover{{border-color:var(--gold);color:var(--gold-ink)}}
h2.week-h{{font-family:"Fraunces",ui-serif,serif;font-weight:600;font-size:20px;margin:30px 0 14px;color:var(--ink);
  scroll-margin-top:56px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:16px}}
.card{{background:var(--surface);border:1px solid var(--line);border-radius:14px;box-shadow:var(--shadow);
  display:flex;flex-direction:column;overflow:hidden}}
.card-top{{display:flex;align-items:center;gap:14px;padding:18px 20px 14px}}
.icon{{flex:0 0 auto;width:52px;height:52px;border-radius:10px;background:var(--gold-bg);color:var(--gold-ink);
  display:flex;align-items:center;justify-content:center;padding:10px}}
.icon svg{{width:100%;height:100%}}
.card-top .titles{{min-width:0}}
.card .tag{{font-size:10.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--gold-ink);
  display:block;margin-bottom:3px}}
.card h3{{font-family:"Fraunces",ui-serif,serif;font-weight:600;font-size:19px;margin:0;color:var(--ink)}}
.card .ask{{font-size:13.5px;line-height:1.5;color:var(--ink-soft);margin:0;padding:0 20px 14px}}
table.details{{width:calc(100% - 40px);margin:0 20px 14px;border-collapse:collapse;font-size:12.5px}}
table.details tr{{border-top:1px solid var(--line)}}
table.details th{{text-align:left;font-weight:700;letter-spacing:.03em;text-transform:uppercase;color:var(--muted);
  padding:7px 10px 7px 0;width:78px;vertical-align:top;white-space:nowrap;font-size:10.5px}}
table.details td{{padding:7px 0;color:var(--ink-soft);line-height:1.4}}
.card .btn{{display:flex;align-items:center;justify-content:center;gap:8px;background:var(--btn-bg);color:#fff;
  text-decoration:none;font-size:14px;font-weight:600;padding:13px 18px;margin-top:auto}}
.card .btn:hover{{background:var(--btn-bg-hover)}}
.empty-note{{color:var(--muted);font-size:14.5px}}
</style></head><body>
<div class="wrap">
  <header class="page">
    <span class="eyebrow">Math Builder</span>
    <h1>Class Cases</h1>
    <p class="sub">Every case, grouped by week &mdash; the field it's set in, the role you're stepping into, the dilemma, and the concepts it tests. Open whichever one you're working on and submit your finished notebook there.</p>
  </header>
  {f'<nav class="jump">{jump_html}</nav>' if jump_html else ''}
  {sections_html}
</div>
</body></html>"""


def render_class_review_html(view, case_id=None):
    """view is admin_core.build_class_review_view()'s return dict:
      rows           -- submission rows (already filtered to case_id if given)
      weeks          -- ordered [{"label": "Week 1" or None, "cases": [case_id,...]}, ...] --
                        the guide's own groups, plus a trailing "Other" group for any
                        case_id with submissions that isn't in a group. A case shows up
                        with its own debrief section even at 0 submissions.
      raw_weeks      -- weeks as actually configured (no "Other" group) -- used only
                        to repopulate the edit textarea in its original form.
      case_titles    -- {case_id: real title}; a lookup miss falls back to
                        the bare slug in the section header, never hidden
      case_briefs    -- {case_id: facilitator cheat-sheet dict or absent}
      case_open_paths-- {case_id: /cases/.../Interactive.html path or None}
      weekly_debrief -- {label, url} for the current debrief-prep page, or None
    Kept as one dict argument (rather than several positional ones) since both
    servers just forward build_class_review_view()'s result straight through."""
    rows, case_titles = view["rows"], view["case_titles"]
    case_briefs, case_open_paths = view["case_briefs"], view["case_open_paths"]
    weekly_debrief, weeks, raw_weeks = view["weekly_debrief"], view["weeks"], view["raw_weeks"]

    debrief_banner = (
        '<div style="margin-bottom:10px;padding:12px 16px;border:1px solid var(--rule);border-radius:8px;'
        'background:#EFF4EF;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">'
        + (f'<a href="{_html.escape(weekly_debrief["url"])}" target="_blank" rel="noopener" '
           f'style="font-weight:600;color:var(--accent);text-decoration:none">&#8599; {_html.escape(weekly_debrief["label"])} '
           '<span class="det" style="font-weight:400">(opens the full debrief-prep page in a new tab)</span></a>'
           if weekly_debrief else
           '<span class="det">No debrief-prep link set for this week yet.</span>')
        + '<a href="#set-debrief" style="font-size:12.5px;color:var(--muted)" '
          'onclick="document.getElementById(\'debrief-form\').style.display=\'flex\';return false;">'
        + ('Change' if weekly_debrief else 'Set one') + '</a></div>'
        '<form id="debrief-form" style="display:none;gap:8px;margin-bottom:10px;flex-wrap:wrap;align-items:center">'
        '<input type="text" id="debrief-label" placeholder="Label, e.g. Week 2 Debrief" '
        f'value="{_html.escape(weekly_debrief["label"]) if weekly_debrief else ""}" style="flex:1;min-width:160px">'
        '<input type="url" id="debrief-url" placeholder="https://claude.ai/code/artifact/..." '
        f'value="{_html.escape(weekly_debrief["url"]) if weekly_debrief else ""}" style="flex:2;min-width:240px">'
        '<button type="button" class="btn ghost" id="save-debrief-btn">Save</button>'
        '</form>'
    )

    def _weeks_to_text(weeks_list):
        blocks = []
        for w in weeks_list:
            lines = ([w['label']] if w.get('label') else []) + list(w['cases'])
            blocks.append('\n'.join(lines))
        return '\n\n'.join(blocks)

    cases_summary = ' &middot; '.join(
        f'{_html.escape(w["label"])} ({len(w["cases"])} case{"s" if len(w["cases"]) != 1 else ""})'
        if w.get('label') else
        ', '.join(_html.escape(case_titles.get(c, c)) for c in w['cases'])
        for w in raw_weeks
    )
    cases_banner = (
        '<div style="margin-bottom:18px;padding:12px 16px;border:1px solid var(--rule);border-radius:8px;'
        'background:#fff;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">'
        + (f'<span class="det">This term\'s cases: <strong style="color:var(--ink)">{cases_summary}</strong>'
           '<br>Each one below has its own debrief section -- with or without submissions -- so you can walk '
           'through every case live.</span>'
           if raw_weeks else
           '<span class="det">No case list set -- sections below only show cases with submissions. '
           'Set the list to also see zero-submission cases.</span>')
        + '<a href="#set-cases" style="font-size:12.5px;color:var(--muted);white-space:nowrap" '
          'onclick="document.getElementById(\'cases-form\').style.display=\'flex\';return false;">'
        + ('Change' if raw_weeks else 'Set the case list') + '</a></div>'
        '<form id="cases-form" style="display:none;gap:8px;margin-bottom:18px;flex-wrap:wrap;align-items:flex-start">'
        '<textarea id="cases-list" rows="8" placeholder="Week 1&#10;apron-order&#10;field-watch&#10;&#10;Week 2&#10;feedback" '
        f'style="flex:1;min-width:260px;min-height:120px;font-family:monospace">{_html.escape(_weeks_to_text(raw_weeks))}</textarea>'
        '<button type="button" class="btn ghost" id="save-cases-btn">Save</button>'
        '<p class="det" style="flex-basis:100%;margin:0">One week per block, separated by a blank line -- '
        'first line of each block is its label (e.g. &quot;Week 1&quot;), then one case per line '
        '(id or title). Skip the label line entirely for one unlabeled group.</p>'
        '</form>'
    )

    def _table_html(rows):
        head, *body = rows
        thead = "".join(f'<th>{_html.escape(c)}</th>' for c in head)
        tbody = "".join(
            '<tr>' + "".join(f'<td>{_html.escape(c)}</td>' for c in row) + '</tr>' for row in body
        )
        return f'<table><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table>'

    def _brief_html(cid):
        b = case_briefs.get(cid)
        if not b:
            return ''
        options = b.get('options') or {}
        opt_lines = "".join(
            f'<li><strong>{_html.escape(k)}.</strong> {_html.escape(v)}</li>' for k, v in options.items()
        )
        deliverables = b.get('deliverables') or []
        deliv_lines = "".join(
            f'<li><strong>{_html.escape(d["id"] or "")}</strong> {_html.escape(d["text"])}</li>' for d in deliverables
        )
        open_path = case_open_paths.get(cid)

        # Split the docx's tables into the Socratic pacing plan (its own
        # first row is literally "Time"/"Move") vs. any real worked-numbers
        # tables (per-moment calculations etc.) -- the latter are shown
        # under Step-by-step, the former stays a separate pacing aid so the
        # two don't read as the same kind of thing.
        solution_tables = b.get('solution_tables') or []
        pacing_table = next((t for t in solution_tables if t[0][:2] == ['Time', 'Move']), None)
        data_tables = [t for t in solution_tables if t is not pacing_table]
        steps = b.get('solution_steps') or []

        solution_block = ''
        if steps or data_tables:
            step_items = "".join(f'<li>{_html.escape(s)}</li>' for s in steps)
            tables_html = "".join(_table_html(t) for t in data_tables)
            solution_block = (
                '<div style="margin:14px 0;padding:12px;border:1px solid var(--rule);border-radius:8px;background:#FBFAF6">'
                '<p style="margin:0 0 8px;font-weight:700;color:var(--accent)">&#128209; How to solve it &mdash; step by step</p>'
                + (f'<ol style="margin:0 0 8px;padding-left:18px">{step_items}</ol>' if step_items else '')
                + (f'<div class="case-solution">{tables_html}</div>' if tables_html else '')
                + '</div>'
            )

        pacing_block = (
            '<details style="margin:8px 0"><summary style="cursor:pointer;font-size:12.5px;color:var(--muted)">'
            '&#128337; Suggested discussion pacing</summary>'
            f'<div class="case-solution" style="margin-top:6px">{_table_html(pacing_table)}</div></details>'
            if pacing_table else ''
        )

        return (
            '<details class="brief" style="margin:10px 0 16px;border:1px solid var(--rule);border-radius:8px;background:#fff" open>'
            '<summary style="cursor:pointer;padding:10px 14px;font-weight:600;font-size:13.5px;color:var(--accent)">'
            'Facilitator quick reference</summary>'
            '<div style="padding:0 14px 14px;font-size:13.5px;line-height:1.5">'
            + (f'<p><a class="btn ghost" href="{_html.escape(open_path)}" target="_blank" rel="noopener" '
               'style="font-size:12.5px;padding:4px 10px;display:inline-block">Open the case (student view) &rarr;</a></p>'
               if open_path else '')
            + (f'<p class="det" style="margin:6px 0">{_html.escape(b["protagonist"])} &middot; {_html.escape(b["primary_metric"] or "")}</p>'
               if b.get('protagonist') or b.get('primary_metric') else '')
            + (f'<ul style="margin:8px 0;padding-left:18px">{opt_lines}</ul>' if opt_lines else '')
            + (f'<div class="case-figs">{"".join(b["figures"])}</div>' if b.get('figures') else '')
            + solution_block
            + (f'<p style="margin:8px 0"><strong>Option A\'s case:</strong> {_html.escape(b["argument_a"])}</p>' if b.get('argument_a') else '')
            + (f'<p style="margin:8px 0"><strong>Option B\'s case:</strong> {_html.escape(b["argument_b"])}</p>' if b.get('argument_b') else '')
            + (f'<p style="margin:8px 0" class="det">Real margin: {b["margin_pct"]}%</p>' if b.get('margin_pct') is not None else '')
            + (f'<p style="margin:10px 0 4px"><strong>Deliverables to walk through:</strong></p><ol style="margin:0;padding-left:18px">{deliv_lines}</ol>'
               if deliv_lines else '')
            + pacing_block
            + '</div></details>'
        )

    def _card(r):
        sid = r["id"]
        assessment = (r.get('assessment') or '').strip()
        return (
            f'<div class="sub-panel" style="margin-bottom:10px;padding:10px;border:1px solid var(--rule);border-radius:8px" data-submission="{sid}">'
            f'<div style="display:flex;justify-content:space-between;align-items:baseline;gap:8px">'
            f'<span><strong>{_html.escape(r["student_name"])}</strong> '
            f'<span class="det">&middot; {_html.escape(r["submitted_on"] or "")}</span></span>'
            f'<button class="btn ghost" data-delete="{sid}" '
            'style="font-size:11.5px;padding:3px 8px;border-color:var(--flag);color:var(--flag)" '
            'title="Remove this submission">Delete</button></div>'
            + (f'<p>{_html.escape(r["answer_text"])}</p>' if r.get('answer_text') else '')
            + (f'<p><a href="/class-photo/{_html.escape(r["pdf_path"])}" target="_blank">View PDF</a></p>'
               if r.get('pdf_path') else '')
            + (f'<p><a href="/class-photo/{_html.escape(r["photo_path"])}" target="_blank">View photo</a></p>'
               if r.get('photo_path') else '')
            + (f'<p class="det">Reviewed by {_html.escape(r["reviewed_by"] or "")}: {_html.escape(r["review_note"] or "")}</p>'
               if r.get('reviewed_on') else
               '<div class="row"><input type="text" placeholder="review note" id="note-' + sid + '" style="flex:1;margin-right:6px">'
               '<button class="btn ghost" data-review="' + sid + '">Mark reviewed</button></div>')
            # Assessment: a persisted strengths/opportunities read of the actual
            # work, separate from the reviewed/review-note tracking above --
            # shown once written (by a guide, or pasted in from a Claude
            # conversation that read the export bundle) and always editable.
            + '<div style="margin-top:8px;padding-top:8px;border-top:1px dashed var(--rule)">'
            + (f'<p class="det" style="font-weight:700;color:var(--accent);margin:0 0 3px">ASSESSMENT</p><p style="margin:0 0 6px">{_html.escape(assessment)}</p>'
               if assessment else '<p class="det" style="margin:0 0 6px">No assessment yet.</p>')
            + f'<div class="row"><textarea placeholder="Strengths / opportunities from reading this student\'s work" '
              f'id="assess-{sid}" style="flex:1;min-height:44px;margin-right:6px;padding:6px 8px;border:1px solid var(--rule);border-radius:6px;font:inherit">{_html.escape(assessment)}</textarea>'
            + f'<button class="btn ghost" data-assess="{sid}" style="align-self:flex-end">Save</button></div>'
            + '</div></div>'
        )

    all_case_ids = [cid for w in weeks for cid in w['cases']]
    if not all_case_ids:
        body = '<p class="det">No submissions yet, and no case list set -- use "Set the case list" above.</p>'
    else:
        groups = {}
        for r in rows:
            groups.setdefault(r['case_id'], []).append(r)

        def _links(cid):
            out = (f'<a href="/class-review/export?case_id={_html.escape(cid)}" '
                   f'style="font-size:12.5px;font-weight:600;color:var(--accent);text-decoration:none">'
                   f'&#8595; Export for debrief</a>')
            # Per-case debrief pages built this session anchor each case's own
            # section as #<case_id> (see the Week 2 Debrief Prep artifact) --
            # jump straight to this case's own dilemma/answer-key/concepts
            # instead of the top of a page covering several cases at once.
            if weekly_debrief:
                out = (f'<a href="{_html.escape(weekly_debrief["url"])}#{_html.escape(cid)}" target="_blank" rel="noopener" '
                       f'style="font-size:12.5px;font-weight:600;color:var(--accent);text-decoration:none;margin-right:14px">'
                       f'&#8599; Debrief-prep writeup</a>') + out
            return out

        def _case_section(cid):
            return (
                f'<section style="margin-bottom:26px">'
                f'<h2 style="font-size:16px;margin:0 0 8px;padding-bottom:6px;border-bottom:1px solid var(--rule);display:flex;align-items:baseline;justify-content:space-between;gap:10px;flex-wrap:wrap">'
                f'<span>{_html.escape(case_titles.get(cid, cid))} '
                f'<span class="det" style="font-weight:400">&middot; {len(groups.get(cid, []))} submission{"s" if len(groups.get(cid, [])) != 1 else ""}</span></span>'
                f'<span>{_links(cid)}</span></h2>'
                + _brief_html(cid)
                + ("".join(_card(r) for r in groups[cid]) if groups.get(cid) else
                   '<p class="det">No submissions yet for this case -- use the reference above to walk through it live.</p>')
                + '</section>'
            )

        def _week_counts(case_ids):
            subs = [r for cid in case_ids for r in groups.get(cid, [])]
            unreviewed = sum(1 for r in subs if not r.get('reviewed_on'))
            return len(subs), unreviewed

        # A week gets its own collapsible <details> block (and anchor id)
        # only when it has a label (an unlabeled single group -- the
        # pre-week-grouping shape, or a case_id-filtered drill-down page --
        # renders its cases with no extra wrapper at all, identical to how
        # this page looked before weeks existed). <details>/<summary> gives
        # a native disclosure arrow for free; state is restored/persisted
        # client-side per week (see the script block below) so a guide's
        # open/closed choices survive a reload.
        def _week_block(i, w):
            if not w.get('label'):
                return "".join(_case_section(cid) for cid in w['cases'])
            total, unreviewed = _week_counts(w['cases'])
            badge = (f' &middot; <span class="week-badge">{unreviewed} to review</span>'
                     if unreviewed else '')
            return (
                f'<details class="week-block" id="week-{i}" open>'
                f'<summary><span class="week-title">{_html.escape(w["label"])}</span>'
                f'<span class="week-meta">{total} submission{"s" if total != 1 else ""}{badge}</span>'
                '</summary>'
                f'<div class="week-body">{"".join(_case_section(cid) for cid in w["cases"])}</div>'
                '</details>'
            )

        body = "".join(_week_block(i, w) for i, w in enumerate(weeks))

    # A jump-nav bar across the named weeks, plus expand/collapse-all
    # shortcuts -- only worth showing once there's more than one week to
    # jump between; a single week (or none) has nothing for it to usefully
    # do.
    labeled = [(i, w['label']) for i, w in enumerate(weeks) if w.get('label')]
    week_nav = (
        '<nav class="week-nav" style="position:sticky;top:0;z-index:5;margin:0 -16px 14px;padding:10px 16px;'
        'background:#FAF8F4;border-bottom:1px solid var(--rule);display:flex;gap:14px;flex-wrap:wrap;'
        'align-items:center;font-size:12.5px">'
        + "".join(
            f'<a href="#week-{i}" style="color:var(--accent);font-weight:600;text-decoration:none">{_html.escape(label)}</a>'
            for i, label in labeled
        )
        + '<span style="flex:1"></span>'
        '<button type="button" class="btn ghost" id="week-expand-all" style="font-size:11.5px;padding:3px 8px">Expand all</button>'
        '<button type="button" class="btn ghost" id="week-collapse-all" style="font-size:11.5px;padding:3px 8px">Collapse all</button>'
        '</nav>'
        if len(labeled) > 1 else ''
    )
    return f"""<!doctype html><html><head><meta charset="utf-8">
<title>Class submissions — Math Builder</title>
<style>
:root{{--rule:#DED8CC;--accent:#22406B;--muted:#5F594E}}
body{{font-family:-apple-system,sans-serif;max-width:720px;margin:24px auto;padding:0 16px;background:#FAF8F4;color:#16140F}}
.det{{color:#5F594E;font-size:12.5px}} .row{{display:flex;align-items:center;margin-top:6px}}
input,textarea{{padding:6px 8px;border:1px solid #DED8CC;border-radius:6px;font-family:inherit}}
.btn.ghost{{background:none;border:1px solid #22406B;color:#22406B;padding:5px 10px;border-radius:6px;cursor:pointer}}
summary::-webkit-details-marker{{color:var(--accent)}}
.week-block{{border:1px solid var(--rule);border-radius:8px;margin:20px 0;background:#fff;scroll-margin-top:56px}}
.week-block > summary{{cursor:pointer;list-style:none;padding:12px 14px;display:flex;align-items:baseline;
  justify-content:space-between;gap:10px;flex-wrap:wrap}}
.week-block > summary::-webkit-details-marker{{display:none}}
.week-block > summary::before{{content:"\\25B8";display:inline-block;margin-right:8px;color:var(--accent);
  transition:transform .15s ease}}
.week-block[open] > summary::before{{transform:rotate(90deg)}}
.week-title{{font-size:17px;font-weight:700}}
.week-meta{{font-size:12.5px;font-weight:400;color:var(--muted)}}
.week-badge{{font-weight:600;color:#A93A1E}}
.week-body{{padding:0 14px 14px}}
.case-figs{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:10px 0}}
.case-figs figure{{margin:0;padding:12px;border:1px solid var(--rule);border-radius:8px;background:#fff;text-align:center}}
.case-figs figure svg,.case-figs figure img{{max-width:100%;height:auto;display:block;margin:0 auto}}
.case-figs figcaption{{font-size:11px;color:var(--muted);margin-top:8px;text-align:left;line-height:1.4}}
.case-figs .box-compare{{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;text-align:center}}
.case-figs .box-compare .label{{font-weight:600;font-size:12.5px;margin-top:4px}}
.case-figs .box-compare .sub{{font-size:11px;color:var(--muted)}}
.case-solution{{overflow-x:auto}}
.case-solution table{{width:100%;border-collapse:collapse;margin:8px 0;font-size:12px;font-variant-numeric:tabular-nums}}
.case-solution th,.case-solution td{{border:1px solid var(--rule);padding:5px 8px;text-align:left;white-space:nowrap}}
.case-solution th{{background:#F0EDE3;font-weight:600}}
</style></head><body>
<h1>Class submissions{' — ' + _html.escape(case_titles.get(case_id, case_id)) if case_id else ''}</h1>
{debrief_banner}
{cases_banner if not case_id else ''}
{week_nav if not case_id else ''}
{body}
<script>
document.querySelectorAll('[data-review]').forEach(function(b) {{
  b.onclick = async function() {{
    var id = b.dataset.review;
    var note = document.getElementById('note-' + id).value;
    var res = await fetch('/api/class-review', {{method:'POST', headers:{{'Content-Type':'application/json'}},
      body: JSON.stringify({{submission_id: id, review_note: note}})}});
    if (res.ok) location.reload(); else alert('Failed to save review.');
  }};
}});
document.querySelectorAll('[data-assess]').forEach(function(b) {{
  b.onclick = async function() {{
    var id = b.dataset.assess;
    var assessment = document.getElementById('assess-' + id).value;
    var res = await fetch('/api/class-review/assess', {{method:'POST', headers:{{'Content-Type':'application/json'}},
      body: JSON.stringify({{submission_id: id, assessment: assessment}})}});
    if (res.ok) location.reload(); else alert('Failed to save -- assessment text is required.');
  }};
}});
document.querySelectorAll('[data-delete]').forEach(function(b) {{
  b.onclick = async function() {{
    var id = b.dataset.delete;
    if (!confirm('Delete this submission? This cannot be undone.')) return;
    var res = await fetch('/api/class-review/delete', {{method:'POST', headers:{{'Content-Type':'application/json'}},
      body: JSON.stringify({{submission_id: id}})}});
    if (res.ok) location.reload(); else alert('Failed to delete.');
  }};
}});
var saveDebriefBtn = document.getElementById('save-debrief-btn');
if (saveDebriefBtn) {{
  saveDebriefBtn.onclick = async function() {{
    var label = document.getElementById('debrief-label').value;
    var url = document.getElementById('debrief-url').value;
    var res = await fetch('/api/weekly-debrief', {{method:'POST', headers:{{'Content-Type':'application/json'}},
      body: JSON.stringify({{label: label, url: url}})}});
    if (res.ok) location.reload(); else alert('Failed to save -- check the link starts with http:// or https://');
  }};
}}
document.querySelectorAll('.week-block').forEach(function(d) {{
  var key = 'mb-week-open-' + d.id;
  try {{
    var saved = localStorage.getItem(key);
    if (saved !== null) d.open = saved === '1';
  }} catch (e) {{}}
  d.addEventListener('toggle', function() {{
    try {{ localStorage.setItem(key, d.open ? '1' : '0'); }} catch (e) {{}}
  }});
}});
document.querySelectorAll('.week-nav a[href^="#week-"]').forEach(function(a) {{
  a.addEventListener('click', function() {{
    var target = document.getElementById(a.getAttribute('href').slice(1));
    if (target && target.tagName === 'DETAILS') target.open = true;
  }});
}});
var expandAllBtn = document.getElementById('week-expand-all');
if (expandAllBtn) {{
  expandAllBtn.onclick = function() {{
    document.querySelectorAll('.week-block').forEach(function(d) {{ d.open = true; }});
  }};
}}
var collapseAllBtn = document.getElementById('week-collapse-all');
if (collapseAllBtn) {{
  collapseAllBtn.onclick = function() {{
    document.querySelectorAll('.week-block').forEach(function(d) {{ d.open = false; }});
  }};
}}
var saveCasesBtn = document.getElementById('save-cases-btn');
if (saveCasesBtn) {{
  saveCasesBtn.onclick = async function() {{
    var cases = document.getElementById('cases-list').value;
    var res = await fetch('/api/weekly-cases', {{method:'POST', headers:{{'Content-Type':'application/json'}},
      body: JSON.stringify({{cases: cases}})}});
    if (res.ok) {{ location.reload(); }} else {{
      var out = await res.json().catch(function() {{ return {{}}; }});
      alert('Failed to save -- ' + (out.error || 'check each line is a real case id or title'));
    }}
  }};
}}
</script>
</body></html>"""
