"""app/student_portal_html.py — the live student-portal single-page app.

Separate from app/admin_html.py on purpose: a learner signed in at /student-login
sees only their own slice of the data (admin_core.build_student_state), never the
whole roster, and every write here goes through /api/student/* routes that force
learner_id from the session -- a student can only ever act as themselves. Visual
language matches the admin app (same CSS custom properties) so the two feel like
one product, not two.
"""

STUDENT_PORTAL_HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Math Builder — My Cases</title>
<style>
:root{
  --paper:#FAF8F4; --paper-2:#F2EEE6; --card:#FFFFFF; --card-2:#FCFBF8;
  --ink:#16140F; --ink-2:#38342C; --muted:#5F594E; --faint:#6E675C;
  --rule:#DED8CC; --rule-2:#EBE6DC;
  --accent:#22406B; --accent-2:#325C93; --accent-soft:#E8EEF6; --accent-line:#B9C9DD;
  --flag:#A93A1E; --flag-soft:#F8E7E1; --flag-line:#E4B7A8;
  --warn:#7E5310; --warn-soft:#F8EFD9; --warn-line:#E0CB9A;
  --ok:#2A5C45; --ok-soft:#E4EFE8;
  --s1:4px; --s2:8px; --s3:12px; --s4:16px; --s5:24px; --s6:32px;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,"Helvetica Neue",Arial,sans-serif;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
  --shadow:0 1px 2px rgba(24,20,12,.05),0 4px 14px rgba(24,20,12,.05);
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:14px;line-height:1.55}
h1,h2,h3,h4{font-family:var(--serif);font-weight:600;letter-spacing:-.01em;margin:0}
a{color:var(--accent)}
button{font:inherit;cursor:pointer}
input,select,textarea{font:inherit;padding:7px 9px;border:1px solid var(--rule);border-radius:6px;background:#fff;color:var(--ink)}
.mono{font-family:var(--mono);font-variant-numeric:tabular-nums}
.wrap{max-width:840px;margin:0 auto;padding:0 var(--s5)}
header.mast{border-bottom:1px solid var(--rule);background:var(--paper);padding:var(--s5) 0}
.kicker{font-size:10.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
h1.title{font-size:24px;margin-top:2px}
main{padding:var(--s5) 0 var(--s6)}
.card{background:var(--card);border:1px solid var(--rule-2);border-radius:10px;padding:var(--s4);box-shadow:var(--shadow);margin-bottom:var(--s4)}
.row{display:flex;gap:var(--s3);align-items:center;flex-wrap:wrap}
.pill{display:inline-block;font-family:var(--mono);font-size:10.5px;font-weight:700;letter-spacing:.03em;
  border-radius:5px;padding:2px 8px;border:1px solid var(--rule)}
.pill.flag{background:var(--flag-soft);color:var(--flag);border-color:var(--flag-line)}
.pill.warn{background:var(--warn-soft);color:var(--warn);border-color:var(--warn-line)}
.pill.ok{background:var(--ok-soft);color:var(--ok);border-color:var(--ok-line,#bcd8c9)}
.pill.accent{background:var(--accent-soft);color:var(--accent);border-color:var(--accent-line)}
.who{font-family:var(--serif);font-size:14.5px}
.det{color:var(--muted);font-size:12.5px;margin-top:2px}
.empty{text-align:center;padding:var(--s6) var(--s4);color:var(--muted)}
.btn{background:var(--accent);color:#fff;border:none;border-radius:6px;padding:7px 13px;font-size:12.5px;font-weight:600}
.btn:hover{background:var(--accent-2)}
.btn.ghost{background:none;border:1px solid var(--rule);color:var(--ink-2)}
.btn.ghost:hover{border-color:var(--accent);color:var(--accent)}
.field{display:flex;flex-direction:column;gap:3px;margin-bottom:var(--s3)}
.field label{font-size:11.5px;color:var(--muted);font-weight:600}
.msg{border-radius:6px;padding:9px 12px;font-size:12.5px;margin-bottom:var(--s3)}
.msg.err{background:var(--flag-soft);color:var(--flag);border:1px solid var(--flag-line)}
.msg.ok{background:var(--ok-soft);color:var(--ok);border:1px solid #bcd8c9}
.sub-panel{background:var(--paper-2);border:1px solid var(--rule-2);border-radius:8px;padding:var(--s4);margin-top:var(--s3)}
.ring{display:flex;flex-direction:column;gap:4px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:var(--s4)}
@media (max-width:560px){.grid2{grid-template-columns:1fr}}
.casecard{border:1px solid var(--rule-2);border-radius:8px;margin-bottom:var(--s3);background:var(--card)}
.casecard>.hd{padding:12px 14px;display:flex;justify-content:space-between;align-items:center;gap:var(--s3);flex-wrap:wrap}
.casecard>.body{padding:0 14px 14px}
</style>
</head>
<body>
<header class="mast"><div class="wrap">
  <div class="kicker">ACTON ACADEMY · HEROES DISCOVERY STUDIO</div>
  <div class="row" style="justify-content:space-between">
    <h1 class="title" id="hdr-name">My Cases</h1>
    <form method="post" action="/student-logout"><button class="btn ghost" type="submit">Log out</button></form>
  </div>
</div></header>

<main class="wrap">
  <div id="msg"></div>
  <div id="view"><div class="card empty">Loading…</div></div>
</main>

<script>
let STATE = null;
const FIELD_VALUES = {};
function restoreFieldValues() {
  for (const id in FIELD_VALUES) {
    const el = document.getElementById(id);
    if (el) el.value = FIELD_VALUES[id];
  }
}
async function api(path, opts) {
  const res = await fetch(path, opts);
  const body = await res.json();
  if (!res.ok || body.error) throw new Error(body.error || ("HTTP " + res.status));
  return body;
}
async function refresh() {
  STATE = await api("/api/student/state");
  document.getElementById("hdr-name").textContent = STATE.learner.display_name + " — My Cases";
  render();
}
function flash(text, isErr) {
  const m = document.getElementById("msg");
  m.innerHTML = '<div class="msg ' + (isErr ? "err" : "ok") + '">' + esc(text) + "</div>";
  setTimeout(() => { if (m.firstChild) m.innerHTML = ""; }, 6000);
}
async function call(path, payload) {
  try {
    const r = await api(path, {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(payload || {})});
    flash("Done.", false);
    await refresh();
    return r;
  } catch (e) { flash(e.message, true); throw e; }
}
function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
}
function val(id) { const el = document.getElementById(id); return el ? el.value : ""; }
function caseHref(caseId, filename) {
  return "/cases/" + encodeURIComponent(caseId) + "/published/" + encodeURIComponent(filename);
}

function render() {
  const v = document.getElementById("view");
  v.innerHTML = renderBadgeProgress() + renderGoals() + renderSuggestions() + renderAssignments();
  wireView();
  restoreFieldValues();
}

function renderBadgeProgress() {
  const b = STATE.badges;
  if (!b) return "";
  const slots = (b.slots || []).map((s) => {
    const label = s.name || ("Badge " + (s.index + 1));
    const cls = s.status === "earned" ? "ok" : s.status === "eligible" ? "accent" : "warn";
    return '<span class="pill ' + cls + '" style="margin-right:6px;margin-bottom:6px" title="' + s.cases_done + "/" + s.cases_per_badge + ' cases">' +
      esc(label) + (s.status === "earned" ? " ✓" : " " + s.cases_done + "/" + s.cases_per_badge) + "</span>";
  }).join("");
  return '<div class="card"><h3 style="margin-bottom:8px">Badge progress</h3>' +
    '<div class="det" style="margin-bottom:8px">' + b.badges + "/" + b.badges_total + " badges earned &middot; " +
    b.cases_done + "/" + b.cases_required + " cases complete</div><div>" + slots + "</div></div>";
}

function renderGoals() {
  const L = STATE.learner, sa = L.self_assessment;
  const clusters = STATE.interest_clusters || [];
  const checked = new Set((sa && sa.interests) || []);
  const picker = '<div class="row" style="flex-wrap:wrap;gap:6px;margin-top:6px">' +
    clusters.map((c) =>
      '<label style="font-size:12px;border:1px solid var(--rule-2);border-radius:6px;padding:3px 8px;cursor:pointer">' +
      '<input type="checkbox" value="' + esc(c.id) + '" data-interest' + (checked.has(c.id) ? " checked" : "") +
      ' style="margin-right:4px">' + esc(c.name) + "</label>"
    ).join("") + "</div>";
  const branches = STATE.curriculum_branches || [];
  const curGrade = sa && sa.grade_level, curBranch = sa && sa.current_branch;
  const gradeOpts = '<option value="">grade — not set</option>' +
    [6,7,8,9,10,11,12].map((g) => '<option value="' + g + '"' + (curGrade === g ? " selected" : "") + ">Grade " + g + "</option>").join("");
  const branchOpts = '<option value="">current course — not set</option>' +
    branches.map((b) => '<option value="' + esc(b.id) + '"' + (curBranch === b.id ? " selected" : "") + ">" + esc(b.branch) + "</option>").join("");
  let html = '<div class="card"><h3 style="margin-bottom:4px">Your goals</h3>' +
    '<p class="det" style="margin-bottom:8px">' + (L.goals ? esc(L.goals) : "No goals on file yet — ask your guide to add them, or tell them what you're curious about.") + "</p>";
  html += '<div class="sub-panel"><strong style="font-size:12.5px">What are you into?</strong>' +
    (sa && sa.reviewed_by_guide
      ? '<div class="det" style="margin-top:4px"><span class="pill ok">reviewed by your guide</span> — case suggestions below are based on this.</div>'
      : '<div class="det" style="margin-top:4px"><span class="pill warn">not yet reviewed</span> — your guide will look this over soon.</div>') +
    picker +
    '<div class="row" style="margin-top:6px"><select id="sa-grade">' + gradeOpts + '</select><select id="sa-branch">' + branchOpts + "</select></div>" +
    '<div class="field" style="margin-top:6px"><label>Anything else you want your guide to know?</label>' +
    '<textarea id="sa-note" rows="2" style="width:100%">' + esc((sa && sa.note) || "") + "</textarea></div>" +
    '<button class="btn" id="save-sa-btn">Save</button></div></div>';
  return html;
}

function renderSuggestions() {
  const s = STATE.suggestions || [];
  if (!s.length) return "";
  return '<div class="card"><h3 style="margin-bottom:8px">Cases that might be a good fit</h3>' +
    s.map((c) => '<div class="sub-panel" style="margin-top:8px"><div class="who">' + esc(c.title) + '</div>' +
      '<div class="det">' + esc(c.domain || "") + (c.career_title ? " &middot; " + esc(c.career_title) : "") + "</div>" +
      (c.why_it_engages ? '<div class="det" style="margin-top:4px">' + esc(c.why_it_engages) + "</div>" : "") +
      "</div>").join("") +
    '<p class="det" style="margin-top:8px">Ask your guide to assign one of these on Assign a Case.</p></div>';
}

function renderAssignments() {
  const A = STATE.assignments || [];
  if (!A.length) return '<div class="card empty">No cases assigned yet — check with your guide.</div>';
  return '<h3 style="margin:var(--s5) 0 var(--s3)">Your cases</h3>' + A.map((a) => {
    const sub = a.latest_submission;
    let body = '<div class="hd"><div><div class="who">' + esc(a.case_title) + '</div>' +
      '<div class="det">' + (a.due_on ? "due " + esc(a.due_on) + " &middot; " : "") + "assigned " + esc(a.assigned_on) + "</div></div>" +
      '<span class="pill accent">' + esc(a.status) + "</span></div><div class=\"body\">";

    if (a.has_interactive) {
      body += '<a class="btn ghost" target="_blank" href="' + caseHref(a.case_id, a.interactive_file) + '">Open case</a>';
    } else {
      body += '<p class="det">Ask your guide for this case\'s materials.</p>';
    }

    if (sub && sub.outcome) {
      const cls = sub.outcome === "accepted" ? "ok" : sub.outcome === "revise" ? "warn" : "flag";
      body += '<div class="sub-panel" style="margin-top:10px"><strong style="font-size:12.5px">Feedback from your guide</strong> ' +
        '<span class="pill ' + cls + '" style="margin-left:4px">' + esc(sub.outcome) + "</span>" +
        (sub.review_note ? '<div class="det" style="margin-top:6px">' + esc(sub.review_note) + "</div>" : "") + "</div>";
    }

    if (a.status !== "complete" && a.status !== "withdrawn" && !(sub && sub.outcome === "accepted" && a.status === "reviewed")) {
      const label = sub && sub.outcome === "revise" ? "Resubmit"
        : sub && sub.outcome === "not-accepted" ? "Try again" : "Submit your work";
      body += submitForm(a, label);
    }
    return '<div class="casecard">' + body + "</div></div>";
  }).join("");
}

function submitForm(a, label) {
  const uid = a.id;
  return '<div class="sub-panel" style="margin-top:10px"><strong style="font-size:12.5px">' + esc(label) + "</strong>" +
    '<div class="field"><label>Your pitch — link or path to your write-up</label><input id="c2url-' + uid + '"></div>' +
    '<div class="field"><label>Research resource — the "how to" link you used</label><input id="c1-' + uid + '"></div>' +
    '<div class="field"><label>Deliverables you\'re turning in (comma-separated)</label><input id="c3-' + uid + '" placeholder="D1,D2,D3"></div>' +
    '<div class="field"><label>Appendix / visual — link or path (optional)</label><input id="c4-' + uid + '"></div>' +
    '<button class="btn" data-submit="' + uid + '" data-case="' + esc(a.case_id) + '">' + esc(label) + "</button></div>";
}

function wireView() {
  const saBtn = document.getElementById("save-sa-btn");
  if (saBtn) saBtn.onclick = () => {
    const interests = Array.from(document.querySelectorAll("[data-interest]:checked")).map((c) => c.value);
    if (!interests.length) return flash("Pick at least one — what are you into?", true);
    const gradeRaw = val("sa-grade"), branchRaw = val("sa-branch");
    call("/api/student/self-assessment", {
      interests, note: val("sa-note"),
      grade_level: gradeRaw ? parseInt(gradeRaw, 10) : null, current_branch: branchRaw || null,
    });
  };
  document.querySelectorAll("[data-submit]").forEach((b) => b.onclick = () => {
    const uid = b.dataset.submit;
    call("/api/student/submit", {
      case_id: b.dataset.case,
      artifacts: {
        challenge_1_resource_url: val("c1-" + uid) || null,
        challenge_2_pitch_url: val("c2url-" + uid) || null,
        challenge_3_deliverables_present: val("c3-" + uid).split(",").map((s) => s.trim()).filter(Boolean),
        challenge_4_appendix_url: val("c4-" + uid) || null,
      },
    });
  });
}

document.getElementById("view").addEventListener("input", (e) => {
  const t = e.target;
  if (t.id && (t.tagName === "INPUT" || t.tagName === "TEXTAREA")) FIELD_VALUES[t.id] = t.value;
});

refresh().catch((e) => flash(e.message, true));
</script>
</body>
</html>
"""


def render_student_portal_html():
    return STUDENT_PORTAL_HTML
