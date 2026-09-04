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


def render_class_review_html(rows, case_id=None, case_titles=None, weekly_debrief=None):
    """case_titles: optional {case_id: title} map so groups can show a real
    title instead of the bare slug. A case_id missing from the map (e.g. a
    since-unpublished case) falls back to the slug itself -- never hidden.
    weekly_debrief: optional {label, url} for the current debrief-prep page,
    surfaced as a banner at the top so it's one click from the review list
    instead of something the guide has to go dig up from chat history."""
    case_titles = case_titles or {}

    debrief_banner = (
        '<div style="margin-bottom:18px;padding:12px 16px;border:1px solid var(--rule);border-radius:8px;'
        'background:#EFF4EF;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">'
        + (f'<a href="{_html.escape(weekly_debrief["url"])}" target="_blank" rel="noopener" '
           f'style="font-weight:600;color:var(--accent);text-decoration:none">&#8599; {_html.escape(weekly_debrief["label"])}</a>'
           if weekly_debrief else
           '<span class="det">No debrief link set for this week yet.</span>')
        + '<a href="#set-debrief" style="font-size:12.5px;color:var(--muted)" '
          'onclick="document.getElementById(\'debrief-form\').style.display=\'flex\';return false;">'
        + ('Change' if weekly_debrief else 'Set one') + '</a></div>'
        '<form id="debrief-form" style="display:none;gap:8px;margin-bottom:18px;flex-wrap:wrap;align-items:center">'
        '<input type="text" id="debrief-label" placeholder="Label, e.g. Week 2 Debrief" '
        f'value="{_html.escape(weekly_debrief["label"]) if weekly_debrief else ""}" style="flex:1;min-width:160px">'
        '<input type="url" id="debrief-url" placeholder="https://claude.ai/code/artifact/..." '
        f'value="{_html.escape(weekly_debrief["url"]) if weekly_debrief else ""}" style="flex:2;min-width:240px">'
        '<button type="button" class="btn ghost" id="save-debrief-btn">Save</button>'
        '</form>'
    )

    def _card(r):
        return (
            '<div class="sub-panel" style="margin-bottom:10px;padding:10px;border:1px solid var(--rule);border-radius:8px">'
            f'<strong>{_html.escape(r["student_name"])}</strong> '
            f'<span class="det">&middot; {_html.escape(r["submitted_on"] or "")}</span>'
            + (f'<p>{_html.escape(r["answer_text"])}</p>' if r.get('answer_text') else '')
            + (f'<p><a href="/class-photo/{_html.escape(r["pdf_path"])}" target="_blank">View PDF</a></p>'
               if r.get('pdf_path') else '')
            + (f'<p><a href="/class-photo/{_html.escape(r["photo_path"])}" target="_blank">View photo</a></p>'
               if r.get('photo_path') else '')
            + (f'<p class="det">Reviewed by {_html.escape(r["reviewed_by"] or "")}: {_html.escape(r["review_note"] or "")}</p>'
               if r.get('reviewed_on') else
               '<div class="row"><input type="text" placeholder="review note" id="note-' + r["id"] + '" style="flex:1;margin-right:6px">'
               '<button class="btn ghost" data-review="' + r["id"] + '">Mark reviewed</button></div>')
            + '</div>'
        )

    if not rows:
        body = '<p class="det">No submissions yet.</p>'
    else:
        groups = {}
        for r in rows:
            groups.setdefault(r['case_id'], []).append(r)
        # Sort groups by each group's most recent submission (newest case
        # activity first), same "what needs attention" ordering the rest of
        # this project's dashboards use -- not alphabetical by slug.
        ordered = sorted(groups.items(),
                          key=lambda kv: max((row['submitted_on'] or '') for row in kv[1]),
                          reverse=True)
        body = "".join(
            f'<section style="margin-bottom:22px">'
            f'<h2 style="font-size:16px;margin:0 0 8px;padding-bottom:6px;border-bottom:1px solid var(--rule);display:flex;align-items:baseline;justify-content:space-between;gap:10px;flex-wrap:wrap">'
            f'<span>{_html.escape(case_titles.get(cid, cid))} '
            f'<span class="det" style="font-weight:400">&middot; {len(group_rows)} submission{"s" if len(group_rows) != 1 else ""}</span></span>'
            f'<a href="/class-review/export?case_id={_html.escape(cid)}" '
            f'style="font-size:12.5px;font-weight:600;color:var(--accent);text-decoration:none">'
            f'&#8595; Export for debrief</a></h2>'
            + "".join(_card(r) for r in group_rows)
            + '</section>'
            for cid, group_rows in ordered
        )
    return f"""<!doctype html><html><head><meta charset="utf-8">
<title>Class submissions — Math Builder</title>
<style>
:root{{--rule:#DED8CC;--accent:#22406B;--muted:#5F594E}}
body{{font-family:-apple-system,sans-serif;max-width:720px;margin:24px auto;padding:0 16px;background:#FAF8F4;color:#16140F}}
.det{{color:#5F594E;font-size:12.5px}} .row{{display:flex;align-items:center;margin-top:6px}}
input{{padding:6px 8px;border:1px solid #DED8CC;border-radius:6px}}
.btn.ghost{{background:none;border:1px solid #22406B;color:#22406B;padding:5px 10px;border-radius:6px;cursor:pointer}}
</style></head><body>
<h1>Class submissions{' — ' + _html.escape(case_titles.get(case_id, case_id)) if case_id else ''}</h1>
{debrief_banner}
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
</script>
</body></html>"""
