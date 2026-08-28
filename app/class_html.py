"""app/class_html.py — HTML for the weekly-class lane (see admin_core.py's
"weekly class cases" section). Shared by both servers (app/admin_server.py,
local; app/admin_web/app.py, hosted) the same way admin_html.py and
student_portal_html.py already are -- one render function, two thin routing
shims on top.
"""
import html as _html


def render_class_case_html(case, err=None):
    open_case = (
        f'<a class="btn" href="{_html.escape(case["interactive_path"])}" target="_blank" rel="noopener">'
        'Open the case &rarr;</a>'
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
.card{{background:#fff;border:1px solid var(--rule);border-radius:10px;padding:24px;box-shadow:0 4px 14px rgba(24,20,12,.06);margin-bottom:16px}}
h1{{font-size:19px;margin:0 0 6px}}
p.sub{{font-size:13px;color:var(--muted);margin:0 0 16px}}
.det{{font-size:12.5px;color:var(--muted)}}
label{{display:block;font-size:12.5px;font-weight:600;margin:14px 0 6px}}
input[type=text],textarea{{width:100%;padding:9px 10px;border:1px solid var(--rule);border-radius:6px;font-size:14px;font-family:inherit}}
textarea{{min-height:110px;resize:vertical}}
input[type=file]{{font-size:13px}}
.btn{{display:inline-block;padding:9px 16px;background:var(--accent);color:#fff;border:none;border-radius:6px;
  cursor:pointer;font-weight:600;font-size:14px;text-decoration:none;margin-top:6px}}
.btn:disabled{{opacity:.6;cursor:default}}
.err{{color:var(--flag);background:var(--flag-soft);border-radius:6px;padding:8px 10px;font-size:13px;margin-bottom:14px}}
.ok{{color:var(--ok);background:#E7F2EA;border-radius:6px;padding:10px;font-size:13.5px}}
</style></head><body><main>
<div class="card">
  <h1>{_html.escape(case['title'])}</h1>
  <p class="sub">{_html.escape(case.get('primary_metric') or '')}</p>
  {open_case}
</div>
<div class="card" id="form-card">
  {err_html}
  <div id="pre-submit">
    <label for="name">Your name</label>
    <input type="text" id="name" placeholder="First and last name">
    <label for="answer">Your answer &amp; reasoning</label>
    <textarea id="answer" placeholder="What did you decide, and how did you work it out?"></textarea>
    <label for="photo">Photo of your work (optional)</label>
    <input type="file" id="photo" accept="image/*" capture="environment">
    <div><button class="btn" id="submit-btn" type="button">Submit</button></div>
  </div>
  <div id="post-submit" style="display:none" class="ok">Got it -- thanks! You can close this page now.</div>
</div>
</main>
<script>
document.getElementById('submit-btn').onclick = async function() {{
  var name = document.getElementById('name').value.trim();
  var answer = document.getElementById('answer').value.trim();
  var photo = document.getElementById('photo').files[0];
  if (!name) {{ alert('Please enter your name.'); return; }}
  if (!answer && !photo) {{ alert('Add an answer, a photo, or both.'); return; }}
  var btn = document.getElementById('submit-btn');
  btn.disabled = true; btn.textContent = 'Submitting...';
  var fd = new FormData();
  fd.append('case_id', {case['id']!r});
  fd.append('student_name', name);
  fd.append('answer_text', answer);
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


def render_class_review_html(rows, case_id=None):
    body = "".join(
        '<div class="sub-panel" style="margin-bottom:10px;padding:10px;border:1px solid var(--rule);border-radius:8px">'
        f'<strong>{_html.escape(r["student_name"])}</strong> '
        f'<span class="det">&middot; {_html.escape(r["case_id"])} &middot; {_html.escape(r["submitted_on"] or "")}</span>'
        + (f'<p>{_html.escape(r["answer_text"])}</p>' if r.get('answer_text') else '')
        + (f'<p><a href="/class-photo/{_html.escape(r["photo_path"])}" target="_blank">View photo</a></p>'
           if r.get('photo_path') else '')
        + (f'<p class="det">Reviewed by {_html.escape(r["reviewed_by"] or "")}: {_html.escape(r["review_note"] or "")}</p>'
           if r.get('reviewed_on') else
           '<div class="row"><input type="text" placeholder="review note" id="note-' + r["id"] + '" style="flex:1;margin-right:6px">'
           '<button class="btn ghost" data-review="' + r["id"] + '">Mark reviewed</button></div>')
        + '</div>'
        for r in rows
    ) or '<p class="det">No submissions yet.</p>'
    return f"""<!doctype html><html><head><meta charset="utf-8">
<title>Class submissions — Math Builder</title>
<style>
body{{font-family:-apple-system,sans-serif;max-width:720px;margin:24px auto;padding:0 16px;background:#FAF8F4;color:#16140F}}
.det{{color:#5F594E;font-size:12.5px}} .row{{display:flex;align-items:center;margin-top:6px}}
input{{padding:6px 8px;border:1px solid #DED8CC;border-radius:6px}}
.btn.ghost{{background:none;border:1px solid #22406B;color:#22406B;padding:5px 10px;border-radius:6px;cursor:pointer}}
</style></head><body>
<h1>Class submissions{' — ' + _html.escape(case_id) if case_id else ''}</h1>
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
</script>
</body></html>"""
