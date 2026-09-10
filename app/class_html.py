"""app/class_html.py — HTML for the weekly-class lane (see admin_core.py's
"weekly class cases" section). Shared by both servers (app/admin_server.py,
local; app/admin_web/app.py, hosted) the same way admin_html.py and
student_portal_html.py already are -- one render function, two thin routing
shims on top.
"""
import html as _html


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


def render_class_review_html(view, case_id=None):
    """view is admin_core.build_class_review_view()'s return dict:
      rows              -- submission rows (already filtered to case_id if given)
      ordered_case_ids  -- this week's cases first (even at 0 submissions), then
                           any other case with submissions, most recent first
      case_titles       -- {case_id: real title}; a lookup miss falls back to
                           the bare slug in the section header, never hidden
      case_briefs       -- {case_id: facilitator cheat-sheet dict or absent}
      case_open_paths   -- {case_id: /cases/.../Interactive.html path or None}
      weekly_debrief    -- {label, url} for the current debrief-prep page, or None
    Kept as one dict argument (rather than five positional ones) since both
    servers just forward build_class_review_view()'s result straight through."""
    rows, case_titles = view["rows"], view["case_titles"]
    case_briefs, case_open_paths = view["case_briefs"], view["case_open_paths"]
    weekly_debrief, weekly_cases = view["weekly_debrief"], view["weekly_cases"]

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

    cases_banner = (
        '<div style="margin-bottom:18px;padding:12px 16px;border:1px solid var(--rule);border-radius:8px;'
        'background:#fff;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">'
        + (f'<span class="det">This week\'s cases: <strong style="color:var(--ink)">'
           + ', '.join(_html.escape(case_titles.get(c, c)) for c in weekly_cases) + '</strong>'
           '<br>Each one below has its own debrief section -- with or without submissions -- so you can walk '
           'through every case live.</span>'
           if weekly_cases else
           '<span class="det">No weekly case list set -- sections below only show cases with submissions. '
           'Set the list to also see zero-submission cases.</span>')
        + '<a href="#set-cases" style="font-size:12.5px;color:var(--muted);white-space:nowrap" '
          'onclick="document.getElementById(\'cases-form\').style.display=\'flex\';return false;">'
        + ('Change' if weekly_cases else 'Set this week\'s cases') + '</a></div>'
        '<form id="cases-form" style="display:none;gap:8px;margin-bottom:18px;flex-wrap:wrap;align-items:flex-start">'
        '<textarea id="cases-list" placeholder="One case per line -- either the id (roofline-call) or the title" '
        f'style="flex:1;min-width:260px;min-height:70px">{_html.escape(chr(10).join(weekly_cases))}</textarea>'
        '<button type="button" class="btn ghost" id="save-cases-btn">Save</button>'
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

    ordered_case_ids = view["ordered_case_ids"]
    if not ordered_case_ids:
        body = '<p class="det">No submissions yet, and no weekly case list set -- use "Set this week\'s cases" above.</p>'
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

        body = "".join(
            f'<section style="margin-bottom:26px">'
            f'<h2 style="font-size:16px;margin:0 0 8px;padding-bottom:6px;border-bottom:1px solid var(--rule);display:flex;align-items:baseline;justify-content:space-between;gap:10px;flex-wrap:wrap">'
            f'<span>{_html.escape(case_titles.get(cid, cid))} '
            f'<span class="det" style="font-weight:400">&middot; {len(groups.get(cid, []))} submission{"s" if len(groups.get(cid, [])) != 1 else ""}</span></span>'
            f'<span>{_links(cid)}</span></h2>'
            + _brief_html(cid)
            + ("".join(_card(r) for r in groups[cid]) if groups.get(cid) else
               '<p class="det">No submissions yet for this case -- use the reference above to walk through it live.</p>')
            + '</section>'
            for cid in ordered_case_ids
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
