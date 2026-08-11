"""app/admin_html.py — the admin single-page app frontend (HTML/CSS/vanilla JS).

Shared between the local stdlib server (admin_server.py) and the hosted Flask
app (admin_web/app.py) -- the frontend only ever talks to relative /api/...
paths via fetch(), so it does not care which backend is serving it. The one
thing that DOES differ per backend is the masthead badge (local/no-auth vs.
hosted/passcode-protected) -- render_admin_html(hosted=...) fills that in so
the hosted deployment doesn't ship a factually wrong "LOCAL ONLY" claim about
an app sitting on the public internet with real student data behind it.
"""

_BADGE = {
    False: "LOCAL ONLY · 127.0.0.1",
    True: "HOSTED · PASSCODE PROTECTED",
}


def render_admin_html(hosted):
    return _ADMIN_HTML_TEMPLATE.replace("__BADGE__", _BADGE[bool(hosted)])


_ADMIN_HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Math Builder — Admin</title>
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
.wrap{max-width:1180px;margin:0 auto;padding:0 var(--s5)}
header.mast{border-bottom:1px solid var(--rule);background:var(--paper);padding:var(--s5) 0}
.kicker{font-size:10.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
h1.title{font-size:24px;margin-top:2px}
.local-badge{display:inline-block;margin-left:var(--s3);font-family:var(--mono);font-size:10.5px;
  background:var(--warn-soft);color:var(--warn);border:1px solid var(--warn-line);border-radius:4px;padding:2px 7px;vertical-align:2px}
nav.tabs{display:flex;gap:2px;border-bottom:1px solid var(--rule);background:var(--paper-2);padding:0 var(--s5)}
nav.tabs button{background:none;border:none;border-bottom:2px solid transparent;padding:11px 16px;font-size:13px;color:var(--muted)}
nav.tabs button.on{color:var(--accent);border-bottom-color:var(--accent);font-weight:600}
main{padding:var(--s5) 0 var(--s6)}
.card{background:var(--card);border:1px solid var(--rule-2);border-radius:10px;padding:var(--s4);box-shadow:var(--shadow);margin-bottom:var(--s4)}
.row{display:flex;gap:var(--s3);align-items:center;flex-wrap:wrap}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:var(--s4)}
.pill{display:inline-block;font-family:var(--mono);font-size:10.5px;font-weight:700;letter-spacing:.03em;
  border-radius:5px;padding:2px 8px;border:1px solid var(--rule)}
.pill.flag{background:var(--flag-soft);color:var(--flag);border-color:var(--flag-line)}
.pill.warn{background:var(--warn-soft);color:var(--warn);border-color:var(--warn-line)}
.pill.ok{background:var(--ok-soft);color:var(--ok);border-color:var(--ok-line,#bcd8c9)}
.pill.accent{background:var(--accent-soft);color:var(--accent);border-color:var(--accent-line)}
.exc-row{display:flex;align-items:center;gap:var(--s4);padding:10px 12px;border-bottom:1px solid var(--rule-2)}
.exc-row:last-child{border-bottom:none}
.who{font-family:var(--serif);font-size:14.5px}
.det{color:var(--muted);font-size:12.5px;margin-top:2px}
.empty{text-align:center;padding:var(--s6) var(--s4);color:var(--muted)}
.btn{background:var(--accent);color:#fff;border:none;border-radius:6px;padding:7px 13px;font-size:12.5px;font-weight:600}
.btn:hover{background:var(--accent-2)}
.btn.ghost{background:none;border:1px solid var(--rule);color:var(--ink-2)}
.btn.ghost:hover{border-color:var(--accent);color:var(--accent)}
.btn.danger{background:var(--flag)}
.btn:disabled{opacity:.45;cursor:not-allowed}
.field{display:flex;flex-direction:column;gap:3px;margin-bottom:var(--s3)}
.field label{font-size:11.5px;color:var(--muted);font-weight:600}
.msg{border-radius:6px;padding:9px 12px;font-size:12.5px;margin-bottom:var(--s3)}
.msg.err{background:var(--flag-soft);color:var(--flag);border:1px solid var(--flag-line)}
.msg.ok{background:var(--ok-soft);color:var(--ok);border:1px solid #bcd8c9}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;font-size:10.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--faint);
  border-bottom:1px solid var(--rule);padding:6px 8px}
td{padding:8px;border-bottom:1px solid var(--rule-2);vertical-align:top}
.sub-panel{background:var(--paper-2);border:1px solid var(--rule-2);border-radius:8px;padding:var(--s4);margin-top:var(--s3)}
.crit-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:4px;margin:var(--s2) 0}
.crit{text-align:center;border-radius:5px;padding:5px 2px;font-family:var(--mono);font-size:11px;border:1px solid var(--rule)}
.crit.ny{background:var(--flag-soft);color:var(--flag)}
.crit.p{background:var(--ok-soft);color:var(--ok)}
.crit.e{background:var(--accent-soft);color:var(--accent)}
pre.report{white-space:pre-wrap;font-family:var(--mono);font-size:11px;background:#fff;border:1px solid var(--rule);
  border-radius:6px;padding:var(--s3);max-height:340px;overflow:auto}
.rings{display:flex;gap:var(--s4);flex-wrap:wrap}
.ringcard{display:flex;gap:var(--s3);align-items:center;border:1px solid var(--rule-2);border-radius:8px;padding:var(--s3);background:var(--card-2)}
details.learner{border:1px solid var(--rule-2);border-radius:8px;margin-bottom:var(--s3);background:var(--card)}
details.learner>summary{padding:12px 14px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;list-style:none}
details.learner>summary::-webkit-details-marker{display:none}
details.learner .body{padding:0 14px 14px}
</style>
</head>
<body>
<header class="mast"><div class="wrap">
  <div class="kicker">ACTON ACADEMY · HEROES DISCOVERY STUDIO</div>
  <h1 class="title">Math Builder — Admin <span class="local-badge">__BADGE__</span></h1>
  <p style="color:var(--muted);font-size:12.5px;margin-top:6px">
    Every write here follows the exact same rules as <span class="mono">skills/case-track/SKILL.md</span>
    and <span class="mono">skills/submission-score/SKILL.md</span> — nothing is auto-graded, nothing is
    auto-completed, no badge is ever auto-awarded. See <a href="dashboard.html">dashboard.html</a> for the
    read-only curriculum + tracker view.
  </p>
</div></header>

<nav class="tabs wrap" id="tabs">
  <button data-tab="queue" class="on">Exception Queue</button>
  <button data-tab="learners">Learners</button>
  <button data-tab="assign">Assign a Case</button>
  <button data-tab="badges">Badges</button>
</nav>

<main class="wrap">
  <div id="msg"></div>
  <div id="view"></div>
</main>

<script>
let STATE = null;
let TAB = "queue";
// UAT FINDING 2026-08-09: every write re-renders the whole view from scratch (the
// simplest correct way to guarantee the UI never shows stale state), which means
// an open <details> panel snaps shut after every single action -- brutal for the
// real workflow, which is a sequence of actions against the SAME learner (record,
// score, confirm, discuss, complete). Track which learner ids are expanded and
// re-apply it after every render instead of losing it.
const OPEN_LEARNERS = new Set();
// Same class of bug as OPEN_LEARNERS above: refresh() re-renders the whole view from
// scratch, which would wipe out a post-hoc DOM write into #csv-result the instant the
// upload's own refresh() call landed. Persist the last CSV upload's added/skipped rows
// here and have renderLearners() bake them into the HTML string on every render instead.
let LAST_CSV_RESULT = null;

async function api(path, opts) {
  const res = await fetch(path, opts);
  const body = await res.json();
  if (!res.ok || body.error) throw new Error(body.error || ("HTTP " + res.status));
  return body;
}
async function refresh() {
  STATE = await api("/api/state");
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
  } catch (e) {
    flash(e.message, true);
    throw e;
  }
}
function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
}
function val(id) { return document.getElementById(id).value; }

document.getElementById("tabs").addEventListener("click", (e) => {
  const b = e.target.closest("button[data-tab]");
  if (!b) return;
  TAB = b.dataset.tab;
  document.querySelectorAll("#tabs button").forEach((x) => x.classList.toggle("on", x === b));
  render();
});

function render() {
  const v = document.getElementById("view");
  if (TAB === "queue") v.innerHTML = renderQueue();
  else if (TAB === "learners") v.innerHTML = renderLearners();
  else if (TAB === "assign") v.innerHTML = renderAssign();
  else if (TAB === "badges") v.innerHTML = renderBadges();
  wireView();
}

// ---------------------------------------------------------------- queue ---
function renderQueue() {
  const Q = STATE.queue;
  const names = {1:"ACT NOW",2:"NEEDS YOU",3:"CHECK",4:"DRIFTING"};
  const cls = {1:"flag",2:"warn",3:"accent",4:"ghost"};
  if (!Q.length) {
    return '<div class="card empty"><h3>Nothing needs judgment today</h3>' +
      '<p style="font-size:13px">' + STATE.learners.length + " active learner(s) on the roster. " +
      "Check the Learners tab for full history.</p></div>";
  }
  const bySev = {};
  Q.forEach((q) => { (bySev[q.severity] = bySev[q.severity] || []).push(q); });
  return Object.keys(bySev).sort().map((sev) =>
    '<h4 style="margin:14px 0 6px">' + names[sev] + '</h4><div class="card" style="padding:0">' +
    bySev[sev].map((q) =>
      '<div class="exc-row"><span class="pill ' + cls[sev] + '">' + esc(q.kind) + "</span>" +
      '<div style="flex:1"><div class="who">' + esc(q.learner) + (q.case_id ? " &middot; <span class=\"mono\">" + esc(q.case_id) + "</span>" : "") + "</div>" +
      '<div class="det">' + esc(q.detail) + " &middot; " + esc(q.action) + "</div></div></div>"
    ).join("") + "</div>"
  ).join("");
}

// ------------------------------------------------------------- learners ---
function renderCsvResult() {
  if (!LAST_CSV_RESULT) return "";
  const {added, skipped} = LAST_CSV_RESULT;
  let html = '<p style="font-size:12.5px"><strong>' + added.length + " added</strong>" +
    (skipped.length ? ", <strong>" + skipped.length + " skipped</strong>" : "") + "</p>";
  if (added.length) {
    html += '<ul style="font-size:12px;color:var(--ok);margin:0 0 6px 18px">' +
      added.map((a) => "<li>row " + a.row + ": " + esc(a.display_name) + " &rarr; " + esc(a.id) + "</li>").join("") +
      "</ul>";
  }
  if (skipped.length) {
    html += '<ul style="font-size:12px;color:var(--flag);margin:0 0 0 18px">' +
      skipped.map((s) => "<li>row " + s.row + (s.display_name ? " (" + esc(s.display_name) + ")" : "") +
        ": " + esc(s.reason) + "</li>").join("") + "</ul>";
  }
  return html;
}

function renderLearners() {
  const progOpts = Object.keys(STATE.programs).map((p) => '<option value="' + esc(p) + '">' + esc(p) + "</option>").join("");
  let html = '<div class="card"><h3 style="margin-bottom:10px">Add a learner</h3>' +
    '<div class="row">' +
    '<div class="field"><label>Display name</label><input id="new-name" placeholder="Avery N."></div>' +
    '<div class="field"><label>Program</label><select id="new-program">' + progOpts + "</select></div>" +
    '<div class="field"><label>Cohort</label><input id="new-cohort" placeholder="2026-fall-adventure"></div>' +
    '<div class="field"><label>&nbsp;</label><button class="btn" id="add-learner-btn">Add learner</button></div>' +
    "</div></div>";

  html += '<div class="card"><h3 style="margin-bottom:6px">Upload a class (CSV)</h3>' +
    '<p style="font-size:12.5px;color:var(--muted);margin:0 0 10px">Columns: <span class="mono">display_name</span>, ' +
    '<span class="mono">program</span> (required — must match a program below exactly) — plus optional ' +
    '<span class="mono">cohort</span>, <span class="mono">status</span>, <span class="mono">id</span>. ' +
    'Every row is reported back individually: added rows and skipped rows with the exact reason, never a silent ' +
    'all-or-nothing.</p>' +
    '<div class="row">' +
    '<input type="file" id="csv-file" accept=".csv,text/csv">' +
    '<button class="btn" id="csv-upload-btn">Upload class</button>' +
    '<a class="btn ghost" href="/api/learners/csv-template" download>Download CSV template</a>' +
    "</div><div id=\"csv-result\" style=\"margin-top:10px\">" + renderCsvResult() + "</div></div>";

  html += STATE.learners.map((L) => {
    const myA = STATE.assignments.filter((a) => a.learner_id === L.id);
    const badge = STATE.badges.find((b) => b.id === L.id);
    return '<details class="learner" data-learner-id="' + esc(L.id) + '"' + (OPEN_LEARNERS.has(L.id) ? " open" : "") +
      '><summary><div><strong>' + esc(L.display_name) + "</strong> " +
      '<span class="pill ' + (L.status === "active" ? "ok" : "ghost") + '">' + esc(L.status) + "</span> " +
      '<span class="mono" style="font-size:11px;color:var(--muted)">' + esc(L.program) + " &middot; " + esc(L.cohort || "no cohort") + "</span></div>" +
      '<span class="mono" style="font-size:12px;color:var(--muted)">' + (badge ? badge.badges + "/" + badge.badges_total + " badges &middot; " + badge.cases_done + "/" + badge.cases_required + " cases" : "") + "</span>" +
      "</summary><div class=\"body\">" +
      renderLearnerAssignments(L, myA) +
      renderLearnerStatusControls(L) +
      "</div></details>";
  }).join("");
  return html;
}

function renderLearnerStatusControls(L) {
  return '<div class="row" style="margin-top:10px">' +
    '<span style="font-size:11.5px;color:var(--muted)">Set status:</span>' +
    ["active", "paused", "alumni"].map((s) =>
      '<button class="btn ghost set-status" data-learner="' + esc(L.id) + '" data-status="' + s + '" ' +
      (L.status === s ? 'disabled' : '') + '>' + s + "</button>").join("") + "</div>" +
    '<div class="row" style="margin-top:6px">' +
    '<span style="font-size:11.5px;color:var(--muted)">Leaving the program? Use Set status above — ' +
    'active/paused/alumni preserves their full history. Delete below is only for fixing a mistake ' +
    '(duplicate, typo, test data) and is permanent.</span></div>' +
    '<div class="row" style="margin-top:6px">' +
    '<button class="btn ghost danger delete-learner" data-learner="' + esc(L.id) + '" data-name="' + esc(L.display_name) + '">Delete learner (permanent)</button>' +
    "</div>";
}

function renderLearnerAssignments(L, myA) {
  if (!myA.length) return '<p style="font-size:12.5px;color:var(--muted)">No assignments yet.</p>';
  return myA.map((a) => {
    const sub = a.latest_submission;
    const score = a.latest_score;
    let body = '<div class="sub-panel"><div class="row" style="justify-content:space-between">' +
      '<div><strong class="mono">' + esc(a.case_id) + '</strong> <span class="pill accent">' + esc(a.status) + "</span></div>" +
      '<div style="font-size:11.5px;color:var(--muted)">assigned ' + esc(a.assigned_on) + (a.due_on ? " &middot; due " + esc(a.due_on) : "") + " &middot; badge slot " + (a.badge_index == null ? "unallocated" : a.badge_index) + "</div>" +
      "</div>";

    if (a.status === "assigned") {
      body += recordSubmissionForm(a);
    }
    if (sub && !sub.outcome) {
      body += '<div style="margin-top:8px;font-size:12.5px"><strong>Latest submission</strong> (' + esc(sub.submitted_on) + ") &mdash; awaiting review.</div>";
      body += scoreForm(a, sub);
      if (score) body += scoreSummary(score) + guideConfirmForm(a, score);
      body += reviewForm(a, sub);
    } else if (sub && sub.outcome) {
      body += '<div style="margin-top:8px;font-size:12.5px"><strong>Reviewed</strong> ' + esc(sub.reviewed_on) + " by " + esc(sub.reviewed_by) +
        ' &middot; outcome <span class="pill ' + (sub.outcome === "accepted" ? "ok" : sub.outcome === "revise" ? "warn" : "flag") + '">' + esc(sub.outcome) + "</span></div>";
      if (sub.review_note) body += '<div class="det">' + esc(sub.review_note) + "</div>";
      if (score) body += scoreSummary(score);
      if (sub.outcome === "revise") {
        body += '<p style="font-size:12px;color:var(--muted);margin-top:6px">Sent back for revision — record the resubmission below when it comes in.</p>';
        body += recordSubmissionForm(a);
      }
    }

    body += '<div style="margin-top:8px"><strong style="font-size:12.5px">Discussions logged: ' + a.discussion_count + "/2</strong></div>";
    body += discussionForm(a);

    if (a.status === "reviewed" && sub && sub.outcome === "accepted" && a.discussion_count >= 2) {
      body += '<button class="btn" style="margin-top:8px" data-complete="' + esc(a.id) + '" data-badge="' + (a.badge_index == null ? '' : a.badge_index) + '">Mark complete</button>';
    }
    if (a.status !== "complete" && a.status !== "withdrawn") {
      body += '<button class="btn ghost danger" style="margin-top:8px;margin-left:6px" data-withdraw="' + esc(a.id) + '">Withdraw</button>';
    }
    return body + "</div>";
  }).join("");
}

function recordSubmissionForm(a) {
  const uid = a.id + "_" + a.n_submissions;
  return '<div class="sub-panel" style="margin-top:8px">' +
    '<strong style="font-size:12.5px">Record a submission</strong>' +
    '<div class="field"><label>Upload the packet (optional — or paste a link/path below)</label>' +
    '<input type="file" id="file-' + uid + '"><button class="btn ghost" style="margin-top:4px" data-upload="' + uid + '" data-learner="' + esc(a.learner_id) + '" data-case="' + esc(a.case_id) + '">Upload</button>' +
    '<div class="mono" id="uploaded-' + uid + '" style="font-size:11px;color:var(--ok);margin-top:4px"></div></div>' +
    '<div class="grid2">' +
    '<div class="field"><label>Challenge 1 — resource URL</label><input id="c1-' + uid + '"></div>' +
    '<div class="field"><label>Challenge 2 — pitch link/path</label><input id="c2url-' + uid + '"></div>' +
    '<div class="field"><label>Challenge 2 — word count</label><input type="number" id="c2wc-' + uid + '"></div>' +
    '<div class="field"><label>Challenge 2 — original visual?</label><select id="c2vis-' + uid + '"><option value="unknown">unknown</option><option value="true">yes</option><option value="false">no</option></select></div>' +
    '<div class="field"><label>Challenge 3 — deliverables present (comma-separated ids)</label><input id="c3-' + uid + '" placeholder="D1,D2,D3"></div>' +
    '<div class="field"><label>Challenge 4 — appendix link/path</label><input id="c4-' + uid + '"></div>' +
    "</div>" +
    '<button class="btn" data-record="' + uid + '" data-learner="' + esc(a.learner_id) + '" data-case="' + esc(a.case_id) + '">Record submission</button>' +
    "</div>";
}

function scoreForm(a, sub) {
  const uid = a.id + "_score";
  const prefill = sub.artifacts && sub.artifacts.challenge_4_appendix_url ? sub.artifacts.challenge_4_appendix_url : "";
  return '<div class="sub-panel" style="margin-top:8px"><strong style="font-size:12.5px">Run the machine first pass</strong>' +
    '<div class="field"><label>File path(s) to score, one per line — relative to the project root</label>' +
    '<textarea id="paths-' + uid + '" rows="2" style="width:100%">' + esc(prefill) + "</textarea></div>" +
    '<button class="btn" data-score="' + uid + '" data-learner="' + esc(a.learner_id) + '" data-case="' + esc(a.case_id) + '">Score it</button></div>';
}

function scoreSummary(score) {
  const order = ["C1","C2","C3","C4","C5","C6","C7"];
  return '<div class="sub-panel" style="margin-top:8px">' +
    '<div class="row" style="justify-content:space-between">' +
    '<strong style="font-size:12.5px">Score &middot; ' + esc(score.scored_on) + " &middot; " +
    '<span class="pill ' + (score.status === "confirmed" ? "ok" : "warn") + '">' + esc(score.status) + "</span></strong>" +
    '<span class="mono" style="font-size:12px">gate: <strong>' + (score.badge_eligible ? "PASS" : "NOT YET") + "</strong> &middot; growth " + score.growth_score + "</span></div>" +
    '<div class="crit-grid">' + order.map((k) => {
      const c = score.criteria[k];
      if (!c) return '<div class="crit">' + k + "<br>&mdash;</div>";
      const cls = c.level === "Not Yet" ? "ny" : c.level === "Exemplary" ? "e" : "p";
      return '<div class="crit ' + cls + '">' + k + "<br>" + (c.level === "Not Yet" ? "NY" : c.level === "Proficient" ? "P" : "E") + "</div>";
    }).join("") + "</div></div>";
}

function guideConfirmForm(a, score) {
  if (score.status === "confirmed") return "";
  const uid = a.id + "_confirm";
  const order = ["C1","C2","C3","C4","C5","C6","C7"];
  return '<div class="sub-panel" style="margin-top:8px"><strong style="font-size:12.5px">Guide confirm</strong>' +
    '<div class="field"><label>Your name</label><input id="by-' + uid + '"></div>' +
    '<p style="font-size:11.5px;color:var(--muted)">Overriding a criterion? Fill in below — every override needs a reason, and it\'s logged permanently as calibration data.</p>' +
    order.map((k) =>
      '<div class="row" style="margin-bottom:4px"><span class="mono" style="width:26px">' + k + "</span>" +
      '<select id="ovr-' + uid + '-' + k + '"><option value="">(no override)</option><option>Not Yet</option><option>Proficient</option><option>Exemplary</option></select>' +
      '<input id="reason-' + uid + '-' + k + '" placeholder="reason (required if overriding)" style="flex:1"></div>'
    ).join("") +
    '<button class="btn" data-confirm="' + uid + '" data-learner="' + esc(a.learner_id) + '" data-case="' + esc(a.case_id) + '">Confirm</button></div>';
}

function reviewForm(a, sub) {
  const uid = sub.id;
  return '<div class="sub-panel" style="margin-top:8px"><strong style="font-size:12.5px">Set review outcome</strong>' +
    '<div class="row">' +
    '<select id="outcome-' + uid + '"><option value="accepted">accepted</option><option value="revise">revise</option><option value="not-accepted">not-accepted</option></select>' +
    '<input id="reviewer-' + uid + '" placeholder="reviewed by" style="width:140px">' +
    "</div>" +
    '<div class="field"><label>Review note (specific — what to fix, or why it\'s accepted)</label><textarea id="note-' + uid + '" rows="2" style="width:100%"></textarea></div>' +
    '<button class="btn" data-review="' + esc(uid) + '">Save review</button></div>';
}

function discussionForm(a) {
  const uid = a.id + "_disc";
  return '<div class="row" style="margin-top:6px">' +
    '<select id="mode-' + uid + '"><option value="live">live</option><option value="written-500">written-500</option></select>' +
    '<input id="note-' + uid + '" placeholder="note (optional)" style="flex:1">' +
    '<button class="btn ghost" data-discuss="' + uid + '" data-learner="' + esc(a.learner_id) + '" data-case="' + esc(a.case_id) + '">Log participation</button></div>';
}

// --------------------------------------------------------------- assign ---
function caseInfoHTML(c) {
  if (!c) return "";
  const band = c.band && c.band.length ? c.band.join("/") : "band unrecorded";
  const domains = c.domains_touched && c.domains_touched.length ? c.domains_touched.join(", ") : "not recorded";
  const std = c.standards_count != null ? c.standards_count + " standards" : "standards count unrecorded";
  return '<div class="sub-panel" id="a-case-info" style="margin-top:8px">' +
    '<div class="mm">' + esc(c.title) + " &middot; " + esc(c.tier || "tier unrecorded") + " &middot; " + esc(band) +
    (c.status === "legacy" ? ' <span class="pill warn">LEGACY — no case.json/interactive page</span>' : "") + "</div>" +
    '<div style="font-size:12.5px;color:var(--muted);margin-top:4px">Touches: ' + esc(domains) + " &middot; " + esc(std) + "</div>" +
    "</div>";
}
function renderAssign() {
  if (!STATE.learners.length) return '<div class="card empty">Add a learner first, on the Learners tab.</div>';
  const activeLearners = STATE.learners.filter((l) => l.status === "active");
  const learnerOpts = '<option value="" disabled selected>— choose a learner —</option>' +
    activeLearners.map((l) => '<option value="' + esc(l.id) + '">' + esc(l.display_name) + "</option>").join("");
  const caseOpts = '<option value="" disabled selected>— choose a case —</option>' +
    STATE.cases.map((c) => '<option value="' + esc(c.id) + '">' + esc(c.title) + " (" + esc(c.tier || "?") +
      (c.band && c.band.length ? " · " + esc(c.band.join("/")) : "") + ", " + esc(c.status) + ")</option>").join("");
  return '<div class="card"><h3 style="margin-bottom:10px">Assign a case</h3>' +
    '<div class="grid2">' +
    '<div class="field"><label>Learner</label><select id="a-learner">' + learnerOpts + "</select></div>" +
    '<div class="field"><label>Case</label><select id="a-case">' + caseOpts + "</select></div>" +
    '<div class="field"><label>Due date (optional)</label><input type="date" id="a-due"></div>' +
    '<div class="field"><label>Badge slot (optional)</label><input type="number" id="a-badge" min="1"></div>' +
    "</div>" +
    '<div id="a-case-info-wrap"></div>' +
    '<button class="btn" id="do-assign">Assign</button>' +
    '<p style="font-size:11.5px;color:var(--muted);margin-top:8px">Only cases that have passed the publish gate (' +
    '<span class="mono">published</span> or <span class="mono">legacy</span>) are listed — the same rule ' +
    "case-track itself enforces. Published cases are listed first; nothing is pre-selected, so an assignment " +
    "always reflects a deliberate pick, not whatever happened to sort first.</p></div>";
}

// --------------------------------------------------------------- badges ---
function renderBadges() {
  if (!STATE.badges.length) return '<div class="card empty">No learners yet.</div>';
  return '<div class="rings">' + STATE.badges.map((b) => {
    const canAward = b.eligible_slots.length > 0;
    return '<div class="ringcard"><div>' +
      '<div class="who">' + esc(b.name) + "</div>" +
      '<div class="det">' + esc(b.program) + " &middot; " + b.badges + "/" + b.badges_total + " badges &middot; " + b.cases_done + "/" + b.cases_required + " cases</div>" +
      (canAward ? b.eligible_slots.map((slot) =>
        '<button class="btn" style="margin-top:6px" data-award="' + esc(b.id) + '" data-slot="' + slot + '">Confirm award — badge ' + slot + "</button>").join("")
        : (b.one_short ? '<span class="pill warn" style="margin-top:6px;display:inline-block">one case short</span>' : "")) +
      "</div></div>";
  }).join("") + "</div>";
}

// ------------------------------------------------------------- wiring -----
function wireView() {
  const $ = (id) => document.getElementById(id);

  document.querySelectorAll("details.learner").forEach((d) => {
    d.addEventListener("toggle", () => {
      if (d.open) OPEN_LEARNERS.add(d.dataset.learnerId);
      else OPEN_LEARNERS.delete(d.dataset.learnerId);
    });
  });

  const addBtn = document.getElementById("add-learner-btn");
  if (addBtn) addBtn.onclick = () => call("/api/learner/add", {
    display_name: val("new-name"), program: val("new-program"), cohort: val("new-cohort"),
  });

  document.querySelectorAll(".set-status").forEach((b) => b.onclick = () =>
    call("/api/learner/status", {learner_id: b.dataset.learner, status: b.dataset.status}));

  document.querySelectorAll(".delete-learner").forEach((b) => b.onclick = async () => {
    const name = b.dataset.name, lid = b.dataset.learner;
    if (!confirm(
      "Permanently delete " + name + " (" + lid + ")?\n\n" +
      "This removes the learner AND every assignment, submission, discussion, and score record " +
      "tied to them. This cannot be undone from this UI (files are snapshotted on disk first).\n\n" +
      "If this person is leaving the program, cancel this and use Set status → alumni/paused instead " +
      "— that keeps their history. Delete is only for fixing a mistake (duplicate, typo, test data)."
    )) return;
    try {
      const r = await call("/api/learner/delete", {learner_id: lid});
      const c = r.removed || {};
      flash("Deleted " + name + " — removed " + c.assignments + " assignment(s), " +
        c.submissions + " submission(s), " + c.discussions + " discussion(s), " + c.scores + " score row(s).", false);
    } catch (e) { /* call() already flashed the error */ }
  });

  const csvBtn = document.getElementById("csv-upload-btn");
  if (csvBtn) csvBtn.onclick = async () => {
    const fileInput = document.getElementById("csv-file");
    if (!fileInput.files.length) return flash("choose a CSV file first", true);
    const fd = new FormData();
    fd.append("file", fileInput.files[0]);
    try {
      const res = await fetch("/api/learners/bulk-csv", {method: "POST", body: fd});
      const body = await res.json();
      if (!res.ok || body.error) throw new Error(body.error || "upload failed");
      LAST_CSV_RESULT = {added: body.added || [], skipped: body.skipped || []};
      flash("CSV processed: " + LAST_CSV_RESULT.added.length + " added, " + LAST_CSV_RESULT.skipped.length + " skipped.", false);
      await refresh();
    } catch (e) { flash(e.message, true); }
  };

  document.querySelectorAll("[data-upload]").forEach((b) => b.onclick = async () => {
    const uid = b.dataset.upload;
    const fileInput = document.getElementById("file-" + uid);
    if (!fileInput.files.length) return flash("choose a file first", true);
    const fd = new FormData();
    fd.append("learner_id", b.dataset.learner);
    fd.append("case_id", b.dataset.case);
    fd.append("file", fileInput.files[0]);
    try {
      const res = await fetch("/api/upload", {method: "POST", body: fd});
      const body = await res.json();
      if (!res.ok || body.error) throw new Error(body.error);
      document.getElementById("uploaded-" + uid).textContent = "Saved to " + body.path;
      const c2 = document.getElementById("c2url-" + uid), c4 = document.getElementById("c4-" + uid);
      if (c2 && !c2.value) c2.value = body.path;
      if (c4 && !c4.value) c4.value = body.path;
      flash("Uploaded.", false);
    } catch (e) { flash(e.message, true); }
  });

  document.querySelectorAll("[data-record]").forEach((b) => b.onclick = () => {
    const uid = b.dataset.record;
    const visRaw = val("c2vis-" + uid);
    call("/api/submission/record", {
      learner_id: b.dataset.learner, case_id: b.dataset.case,
      artifacts: {
        challenge_1_resource_url: val("c1-" + uid) || null,
        challenge_2_pitch_url: val("c2url-" + uid) || null,
        challenge_2_word_count: val("c2wc-" + uid) ? Number(val("c2wc-" + uid)) : null,
        challenge_2_has_original_visual: visRaw === "unknown" ? null : visRaw === "true",
        challenge_3_deliverables_present: val("c3-" + uid).split(",").map((s) => s.trim()).filter(Boolean),
        challenge_4_appendix_url: val("c4-" + uid) || null,
      },
      source: "facilitator-dictated",
    });
  });

  document.querySelectorAll("[data-score]").forEach((b) => b.onclick = () => {
    const uid = b.dataset.score;
    const paths = val("paths-" + uid).split("\n").map((s) => s.trim()).filter(Boolean);
    call("/api/score", {learner_id: b.dataset.learner, case_id: b.dataset.case, file_paths: paths});
  });

  document.querySelectorAll("[data-confirm]").forEach((b) => b.onclick = () => {
    const uid = b.dataset.confirm;
    const order = ["C1","C2","C3","C4","C5","C6","C7"];
    const overrides = [];
    order.forEach((k) => {
      const level = val("ovr-" + uid + "-" + k);
      if (level) overrides.push({criterion: k, level, reason: val("reason-" + uid + "-" + k)});
    });
    call("/api/guide-confirm", {learner_id: b.dataset.learner, case_id: b.dataset.case, by: val("by-" + uid), overrides});
  });

  document.querySelectorAll("[data-review]").forEach((b) => b.onclick = () => {
    const uid = b.dataset.review;
    call("/api/review", {
      submission_id: uid, outcome: val("outcome-" + uid),
      reviewed_by: val("reviewer-" + uid), review_note: val("note-" + uid),
    });
  });

  document.querySelectorAll("[data-discuss]").forEach((b) => b.onclick = () => {
    const uid = b.dataset.discuss;
    call("/api/discussion/add", {
      learner_id: b.dataset.learner, case_id: b.dataset.case,
      mode: val("mode-" + uid), note: val("note-" + uid),
    });
  });

  document.querySelectorAll("[data-complete]").forEach((b) => b.onclick = () =>
    call("/api/complete", {assignment_id: b.dataset.complete, badge_index: b.dataset.badge ? Number(b.dataset.badge) : null}));

  document.querySelectorAll("[data-withdraw]").forEach((b) => b.onclick = () => {
    if (confirm("Withdraw this assignment?")) call("/api/assign/withdraw", {assignment_id: b.dataset.withdraw});
  });

  const caseSelect = document.getElementById("a-case");
  if (caseSelect) {
    const infoWrap = document.getElementById("a-case-info-wrap");
    const updateCaseInfo = () => {
      const c = STATE.cases.find((x) => x.id === caseSelect.value);
      infoWrap.innerHTML = caseInfoHTML(c);
    };
    caseSelect.addEventListener("change", updateCaseInfo);
    updateCaseInfo();
  }

  const assignBtn = document.getElementById("do-assign");
  if (assignBtn) assignBtn.onclick = () => {
    const learner_id = val("a-learner"), case_id = val("a-case");
    if (!learner_id || !case_id) {
      flash("Pick a learner and a case first — nothing is assigned by default.", true);
      return;
    }
    call("/api/assign", {
      learner_id, case_id,
      due_on: val("a-due") || null, badge_index: val("a-badge") ? Number(val("a-badge")) : null,
    });
  };

  document.querySelectorAll("[data-award]").forEach((b) => b.onclick = () => {
    if (confirm("Confirm badge award for " + b.dataset.award + "?")) call("/api/badge/award", {learner_id: b.dataset.award, badge_index: Number(b.dataset.slot)});
  });
}

refresh().catch((e) => flash(e.message, true));
</script>
</body>
</html>
"""
