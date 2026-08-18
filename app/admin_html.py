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
abbr.gloss{text-decoration:none;border-bottom:1px dotted var(--muted);cursor:help}
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
  <button data-tab="class">Class Dashboard</button>
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
// Same class of bug again, for free-text/number inputs (e.g. "Your name" on Guide
// confirm, "reviewed by" on Set review outcome): they're uncontrolled DOM nodes with no
// backing JS state, so a re-render from ANY other button click in the view (not just
// their own) wipes out whatever was typed. Capture every keystroke into this map, keyed
// by element id, and re-apply it after every render — same fix shape as OPEN_LEARNERS.
const FIELD_VALUES = {};
// Roster filters (Learners + Badges tabs) -- client-side only, /api/state already
// returns every learner, so slicing the view doesn't need a round-trip. "" means
// no filter on that dimension.
const ROSTER_FILTER = {program: "", cohort: "", status: "active"};
function filteredLearners() {
  return STATE.learners.filter((l) =>
    (!ROSTER_FILTER.program || l.program === ROSTER_FILTER.program) &&
    (!ROSTER_FILTER.cohort || l.cohort === ROSTER_FILTER.cohort) &&
    (!ROSTER_FILTER.status || l.status === ROSTER_FILTER.status));
}
function rosterFilterHTML() {
  const cohorts = Array.from(new Set(STATE.learners.map((l) => l.cohort).filter(Boolean))).sort();
  const progOpts = '<option value="">all levels/programs</option>' +
    Object.keys(STATE.programs).map((p) => '<option value="' + esc(p) + '"' + (ROSTER_FILTER.program === p ? " selected" : "") + ">" + esc(p) + "</option>").join("");
  const cohortOpts = '<option value="">all organizations/cohorts</option>' +
    cohorts.map((c) => '<option value="' + esc(c) + '"' + (ROSTER_FILTER.cohort === c ? " selected" : "") + ">" + esc(c) + "</option>").join("");
  const statusOpts = ["", "active", "paused", "alumni"].map((s) =>
    '<option value="' + s + '"' + (ROSTER_FILTER.status === s ? " selected" : "") + ">" + (s || "all statuses") + "</option>").join("");
  return '<div class="card" style="padding:10px 14px"><div class="row">' +
    '<span style="font-size:11.5px;color:var(--muted);font-weight:600">Filter:</span>' +
    '<select id="filter-program">' + progOpts + "</select>" +
    '<select id="filter-cohort">' + cohortOpts + "</select>" +
    '<select id="filter-status">' + statusOpts + "</select>" +
    '<span style="font-size:11.5px;color:var(--muted)" id="filter-count"></span>' +
    "</div></div>";
}
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
  STATE = await api("/api/state");
  CLASS_DASH = null;
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
function starStr(n) { n = n || 0; return "★".repeat(n) + "☆".repeat(5 - n); }

// Definitions sourced from RUBRIC.md's "The seven criteria" + "Scoring" sections and
// skills/submission-score/SKILL.md, kept short enough for a hover tooltip. If the rubric's
// wording changes, update here too -- this is a paraphrase, not a live pull, so it can drift
// if edited only in one place.
const GLOSSARY = {
  C1: "Research — the “how to” resource. Did the Hero find and cite a real resource that " +
      "teaches the underlying math, independent of the case's own built-in glossary?",
  C2: "The pitch — a firm stance, defended. Did the Hero pick a side and argue for it? Correct " +
      "numbers with no conclusion is Not Yet on C2 even though C3 (below) is fine.",
  C3: "Mathematical correctness. Are the Hero's own numbers right, recomputed against the case's " +
      "appendix data?",
  C4: "Required deliverables. Did the Hero turn in everything the case asks for (per case.json's " +
      "deliverables list)?",
  C5: "Visual display and appendix of work. Is there a chart/image, and is its data original " +
      "(the Hero's own work) rather than copied straight from the case appendix?",
  C6: "Socratic participation. Did the Hero actually take part in the discussion (live or async), " +
      "not just submit and disappear?",
  C7: "Framing the question. Did the Hero notice or question whether the case is even asking the " +
      "right thing — the hardest criterion; a machine pass can never mark this Exemplary.",
  gate: "Badge-eligibility gate. PASS only when all seven criteria (C1–C7) are at least " +
        "Proficient. One Not Yet blocks the badge even if the growth score is high.",
  growth: "Growth score. A weighted 0–100 score across all seven criteria — separate from the " +
          "gate above. A case can score high on growth and still fail the gate (badge) on one weak criterion.",
  NY: "Not Yet — this criterion isn't there yet. Blocks the badge gate regardless of the other six.",
  P: "Proficient — meets the bar for this criterion.",
  E: "Exemplary — exceeds the bar. Machine scoring may never mark C7 Exemplary; that always needs a human read.",
  badge_slot: "Badge slot. Which of the program's badge positions this case's completion fills " +
              "(programs require a fixed number of cases per badge — see the program's cases_per_badge).",
  machine_first_pass: "Machine first-pass. An automated draft score — never final. A guide must " +
                       "confirm (or override, with a reason) before it counts.",
  T1: "Tier 1 — MS entry. ~2 hours. Arithmetic, percent, single-step unit conversion. One dominant variable.",
  T2: "Tier 2 — MS core. ~2–3 hours. Multi-step, rates, ratio, area/volume, weighted comparison. Two competing variables that trade off.",
  T3: "Tier 3 — MS stretch / HS entry. ~3 hours. Scientific notation, systems, probability, optimization over a set. Three+ variables, some deliberately irrelevant.",
  T4: "Tier 4 — HS. ~3+ hours. Algebraic modeling, functions, statistics with inference, sensitivity. Requires stating and defending an assumption; data is incomplete by design.",
  tier_unknown: "No tier assigned yet. This is an older, imported case that hasn't been through the difficulty-tiering pass the newer T1–T4 cases have — a guide should sanity-check it fits the learner's level before assigning.",
};
function gloss(label, term) {
  const def = GLOSSARY[term];
  return def ? '<abbr class="gloss" title="' + esc(def) + '">' + esc(label) + "</abbr>" : esc(label);
}
function badgeSlotLabel(L, badgeIndex) {
  if (badgeIndex == null) return "unallocated";
  const names = (STATE.programs[L.program] || {}).badge_names || [];
  const name = names[badgeIndex];
  return name ? esc(name) + " (badge " + (badgeIndex + 1) + ")" : String(badgeIndex);
}

document.getElementById("tabs").addEventListener("click", async (e) => {
  const b = e.target.closest("button[data-tab]");
  if (!b) return;
  TAB = b.dataset.tab;
  document.querySelectorAll("#tabs button").forEach((x) => x.classList.toggle("on", x === b));
  if (TAB === "class" && !CLASS_DASH) await loadClassDashboard();
  render();
});

// Fetched lazily (not part of /api/state) since it's a heavier aggregate query a
// guide may never open in a given session -- loaded once per page load, then
// cached here; refresh() (called after every write) invalidates it so a change
// made elsewhere (e.g. a new self-assessment) shows up next time the tab opens.
let CLASS_DASH = null;
async function loadClassDashboard() {
  try { CLASS_DASH = await api("/api/class-dashboard"); }
  catch (e) { CLASS_DASH = {error: e.message}; }
}

function render() {
  const v = document.getElementById("view");
  if (TAB === "queue") v.innerHTML = renderQueue();
  else if (TAB === "learners") v.innerHTML = renderLearners();
  else if (TAB === "assign") v.innerHTML = renderAssign();
  else if (TAB === "badges") v.innerHTML = renderBadges();
  else if (TAB === "class") v.innerHTML = renderClassDashboard();
  wireView();
  restoreFieldValues();
}
// Delegated on #view once, at load, not inside render() — a listener attached to a node
// that innerHTML just replaced would itself be gone. Bubbling from a child input/textarea/
// select still reaches this one, permanent listener regardless of how many times the
// children underneath get rebuilt.
document.getElementById("view").addEventListener("input", (e) => {
  const t = e.target;
  if (t.id && (t.tagName === "INPUT" || t.tagName === "TEXTAREA")) FIELD_VALUES[t.id] = t.value;
});

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
      added.map((a) => "<li>row " + a.row + ": " + esc(a.display_name) + " &rarr; " + esc(a.id) +
        (a.passcode ? " &middot; passcode <strong class=\"mono\">" + esc(a.passcode) + "</strong>" : "") + "</li>").join("") +
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
    '<div class="field"><label>Program (level)</label><select id="new-program">' + progOpts + "</select></div>" +
    '<div class="field"><label>Cohort (organization/class)</label><input id="new-cohort" placeholder="2026-fall-adventure"></div>' +
    "</div>" +
    '<div class="field" style="margin-top:2px"><label>Goals — what this Hero is here to work on</label>' +
    '<textarea id="new-goals" rows="2" style="width:100%" placeholder="e.g. build confidence with ratios; wants to explore engineering careers"></textarea></div>' +
    '<button class="btn" id="add-learner-btn">Add learner</button>' +
    '<div id="new-learner-result" style="margin-top:8px"></div></div>';

  html += '<div class="card"><h3 style="margin-bottom:6px">Upload a class (CSV)</h3>' +
    '<p style="font-size:12.5px;color:var(--muted);margin:0 0 10px">Columns: <span class="mono">display_name</span>, ' +
    '<span class="mono">program</span> (required — must match a program below exactly) — plus optional ' +
    '<span class="mono">cohort</span>, <span class="mono">status</span>, <span class="mono">id</span>, ' +
    '<span class="mono">goals</span>. ' +
    'Every row is reported back individually: added rows and skipped rows with the exact reason, never a silent ' +
    'all-or-nothing. Each added Hero gets their own student-portal passcode, shown in the result below.</p>' +
    '<div class="row">' +
    '<input type="file" id="csv-file" accept=".csv,text/csv">' +
    '<button class="btn" id="csv-upload-btn">Upload class</button>' +
    '<a class="btn ghost" href="/api/learners/csv-template" download>Download CSV template</a>' +
    "</div><div id=\"csv-result\" style=\"margin-top:10px\">" + renderCsvResult() + "</div></div>";

  html += rosterFilterHTML();
  const shown = filteredLearners();
  html += '<p style="font-size:11.5px;color:var(--muted);margin:0 0 8px">Showing ' + shown.length + " of " + STATE.learners.length + " learners.</p>";

  html += shown.map((L) => {
    const myA = STATE.assignments.filter((a) => a.learner_id === L.id);
    const badge = STATE.badges.find((b) => b.id === L.id);
    return '<details class="learner" data-learner-id="' + esc(L.id) + '"' + (OPEN_LEARNERS.has(L.id) ? " open" : "") +
      '><summary><div><strong>' + esc(L.display_name) + "</strong> " +
      '<span class="pill ' + (L.status === "active" ? "ok" : "ghost") + '">' + esc(L.status) + "</span> " +
      '<span class="mono" style="font-size:11px;color:var(--muted)">' + esc(L.program) + " &middot; " + esc(L.cohort || "no cohort") + "</span></div>" +
      '<span class="mono" style="font-size:12px;color:var(--muted)">' + (badge ? badge.badges + "/" + badge.badges_total + " badges &middot; " + badge.cases_done + "/" + badge.cases_required + " cases" : "") + "</span>" +
      "</summary><div class=\"body\">" +
      renderProfile(L) +
      renderSelfAssessment(L) +
      renderLearnerAssignments(L, myA) +
      renderLearnerStatusControls(L) +
      "</div></details>";
  }).join("");
  return html;
}

// Student-portal identity + free-text goals, both settable by a guide/admin at
// add-learner time or edited later here. Separate from the structured self-
// assessment below (interests[]/grade/branch) -- goals is the plain-language
// version of "why this Hero signed up," always visible even before a guide has
// had the fuller conversation.
function renderProfile(L) {
  return '<div class="sub-panel"><strong style="font-size:12.5px">Profile</strong>' +
    '<div class="field" style="margin-top:6px"><label>Goals</label>' +
    '<textarea id="goals-' + esc(L.id) + '" rows="2" style="width:100%">' + esc(L.goals || "") + "</textarea></div>" +
    '<div class="row" style="margin-top:4px">' +
    '<button class="btn ghost" data-save-goals="' + esc(L.id) + '">Save goals</button>' +
    '<span class="mono" style="font-size:12px;color:var(--muted)">Student portal passcode: <strong>' + esc(L.passcode || "—") + '</strong></span>' +
    '<button class="btn ghost" data-reset-passcode="' + esc(L.id) + '" data-name="' + esc(L.display_name) + '">Reset passcode</button>' +
    "</div>" +
    '<p style="font-size:11px;color:var(--muted);margin:4px 0 0">Give the Hero their id (<span class="mono">' +
    esc(L.id) + '</span>) and passcode to sign into <a href="/student-login" target="_blank">the student portal</a> ' +
    "themselves — open cases, submit, revise, and check badge progress.</p>" +
    "</div>";
}

// PLAN.md Phase 2b — the goals/career conversation, guide-mediated for now (see
// admin_core.do_set_self_assessment's own docstring for why: students don't have their
// own login yet). Sits in "draft" (reviewed_by_guide: false) until a guide explicitly
// reviews it, same spirit as machine-first-pass never counting toward a badge until
// guide-confirm promotes it -- nothing here suggests cases on its own.
function renderSelfAssessment(L) {
  const sa = L.self_assessment;
  const clusters = STATE.interest_clusters || [];
  const checked = new Set((sa && sa.interests) || []);
  const picker = '<div class="row" style="flex-wrap:wrap;gap:6px;margin-top:6px">' +
    clusters.map((c) =>
      '<label style="font-size:12px;border:1px solid var(--rule-2);border-radius:6px;padding:3px 8px;cursor:pointer">' +
      '<input type="checkbox" value="' + esc(c.id) + '" data-interest-tag="' + esc(L.id) + '"' +
      (checked.has(c.id) ? " checked" : "") + " style=\"margin-right:4px\">" + esc(c.name) + "</label>"
    ).join("") + "</div>";

  const branches = STATE.curriculum_branches || [];
  const curGrade = sa && sa.grade_level;
  const curBranch = sa && sa.current_branch;
  const gradeOpts = '<option value="">grade — not set</option>' +
    [6, 7, 8, 9, 10, 11, 12].map((g) => '<option value="' + g + '"' + (curGrade === g ? " selected" : "") + ">Grade " + g + "</option>").join("");
  const branchOpts = '<option value="">current course — not set</option>' +
    branches.map((b) => '<option value="' + esc(b.id) + '"' + (curBranch === b.id ? " selected" : "") + ">" + esc(b.branch) + " (" + esc(b.band) + ")</option>").join("");
  const branchName = curBranch ? (branches.find((b) => b.id === curBranch) || {}).branch : null;

  let html = '<div class="sub-panel"><strong style="font-size:12.5px">Goals & career self-assessment</strong>';
  if (sa) {
    html += '<div style="font-size:11.5px;color:var(--muted);margin-top:4px">Captured ' + esc(sa.captured_on) +
      " by " + esc(sa.captured_by) +
      (curGrade ? " &middot; grade " + curGrade : "") +
      (branchName ? " &middot; currently in " + esc(branchName) : "") +
      (sa.reviewed_by_guide
        ? ' &middot; <span class="pill ok">reviewed</span> ' + esc(sa.reviewed_on) + " by " + esc(sa.reviewed_by)
        : ' &middot; <span class="pill warn">not yet reviewed — suggestions won\'t show until it is</span>') +
      "</div>";
  } else {
    html += '<div style="font-size:11.5px;color:var(--muted);margin-top:4px">Nothing on file yet. Have the ' +
      "conversation, then capture what the Hero is curious about below.</div>";
  }
  html += picker;
  html += '<div class="row" style="margin-top:6px">' +
    '<select id="sa-grade-' + esc(L.id) + '">' + gradeOpts + "</select>" +
    '<select id="sa-branch-' + esc(L.id) + '">' + branchOpts + "</select>" +
    '</div><p style="font-size:11px;color:var(--muted);margin:4px 0 0">Grade and current course sharpen the ' +
    "suggested-cases match score on Assign a Case — optional, but the more a guide fills in, the better the shortlist.</p>";
  html += '<div class="field" style="margin-top:6px"><label>Note (what they said, in their words)</label>' +
    '<textarea id="sa-note-' + esc(L.id) + '" rows="2" style="width:100%">' + esc((sa && sa.note) || "") + "</textarea></div>";
  html += '<div class="row" style="margin-top:6px">' +
    '<input id="sa-by-' + esc(L.id) + '" placeholder="captured by" style="width:140px">' +
    '<button class="btn" data-save-sa="' + esc(L.id) + '">Save self-assessment</button>';
  if (sa && !sa.reviewed_by_guide) {
    html += '<input id="sa-reviewer-' + esc(L.id) + '" placeholder="reviewed by" style="width:140px">' +
      '<button class="btn ghost" data-review-sa="' + esc(L.id) + '">Mark reviewed</button>';
  }
  html += "</div></div>";
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
      '<div style="font-size:11.5px;color:var(--muted)">assigned ' + esc(a.assigned_on) + (a.due_on ? " &middot; due " + esc(a.due_on) : "") + " &middot; " + gloss("badge slot", "badge_slot") + " " + badgeSlotLabel(L, a.badge_index) + "</div>" +
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
      if (a.badge_index == null) {
        // No badge slot was picked at assignment time. Rather than fail here with no way
        // to recover (the old behavior — see PLAN.md Phase 1b), ask for it right where the
        // guide needs it, matching the Exception Queue's own copy ("confirm complete and
        // assign a badge slot"). /api/complete already accepts badge_index and applies it
        // (admin_core.do_complete) -- this was always a frontend gap, not a backend one.
        body += '<div class="sub-panel" style="margin-top:8px">' +
          '<strong style="font-size:12.5px">Confirm complete and assign a badge slot</strong>' +
          '<div class="row" style="margin-top:6px">' +
          '<input type="number" min="0" id="badge-' + esc(a.id) + '" placeholder="badge slot #" style="width:120px">' +
          '<button class="btn" data-complete="' + esc(a.id) + '" data-badge="">Mark complete</button>' +
          "</div></div>";
      } else {
        body += '<button class="btn" style="margin-top:8px" data-complete="' + esc(a.id) + '" data-badge="' + a.badge_index + '">Mark complete</button>';
      }
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
    '<span class="pill ' + (score.status === "confirmed" ? "ok" : "warn") + '">' +
    (score.status === "machine-first-pass" ? gloss(score.status, "machine_first_pass") : esc(score.status)) +
    "</span></strong>" +
    '<span class="mono" style="font-size:12px">' + gloss("gate", "gate") + ": <strong>" +
    (score.badge_eligible ? "PASS" : "NOT YET") + "</strong> &middot; " + gloss("growth", "growth") + " " +
    score.growth_score + "</span></div>" +
    '<div class="crit-grid">' + order.map((k) => {
      const c = score.criteria[k];
      if (!c) return '<div class="crit">' + gloss(k, k) + "<br>&mdash;</div>";
      const cls = c.level === "Not Yet" ? "ny" : c.level === "Exemplary" ? "e" : "p";
      const letter = c.level === "Not Yet" ? "NY" : c.level === "Proficient" ? "P" : "E";
      return '<div class="crit ' + cls + '">' + gloss(k, k) + "<br>" + gloss(letter, letter) + "</div>";
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
      '<div class="row" style="margin-bottom:4px"><span class="mono" style="width:26px">' + gloss(k, k) + "</span>" +
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
  const complexity = c.complexity != null ? starStr(c.complexity) : "not yet rated";
  const rating = c.rating_count > 0 ? c.avg_rating + "★ from " + c.rating_count + " student" + (c.rating_count === 1 ? "" : "s") : "not yet rated by students";
  return '<div class="sub-panel" id="a-case-info" style="margin-top:8px">' +
    '<div class="mm">' + esc(c.title) + " &middot; " + esc(c.tier || "tier unrecorded") + " &middot; " + esc(band) +
    (c.status === "legacy" ? ' <span class="pill warn">LEGACY — no case.json/interactive page</span>' : "") + "</div>" +
    '<div style="font-size:12.5px;color:var(--muted);margin-top:4px">Touches: ' + esc(domains) + " &middot; " + esc(std) + "</div>" +
    '<div style="font-size:12.5px;color:var(--muted);margin-top:4px">Complexity: ' + esc(complexity) + " &middot; Student rating: " + esc(rating) + "</div>" +
    "</div>";
}
// PLAN.md Phase 2d. Cards built from admin_core.suggest_cases()'s own rationale fields
// (why_it_engages, career_title) -- narrows the search, never gates it: the plain
// dropdown right below stays exactly as it was for every learner, suggested or not.
function suggestionCardsHTML(suggestions, reviewedNoMatch) {
  if (!suggestions.length) {
    if (!reviewedNoMatch) return "";
    // Distinguish "hasn't done a self-assessment" (silence is correct — nothing to show)
    // from "did the self-assessment, reviewed it, and we genuinely have nothing that fits
    // their interests yet" (silence here reads as broken, not as "no signal").
    return '<div class="sub-panel" style="margin-top:8px">' +
      '<strong style="font-size:12.5px">Suggested, based on their self-assessment</strong>' +
      '<p style="font-size:12px;color:var(--muted);margin:6px 0 0">No published or legacy case ' +
      "matches their interests yet. Browse the full list below instead.</p></div>";
  }
  return '<div class="sub-panel" style="margin-top:8px">' +
    '<strong style="font-size:12.5px">Suggested, based on their self-assessment</strong>' +
    suggestions.map((s) => {
      const tierBadge = s.tier ? gloss(s.tier, s.tier) : gloss("?", "tier_unknown");
      const teaches = (s.domains_touched && s.domains_touched.length)
        ? esc(s.domains_touched.join(", ")) + (s.standards_count ? " (" + s.standards_count + " spine skills)" : "")
        : null;
      const scoreTitle = s.match_breakdown
        ? Object.entries(s.match_breakdown).map(([k, v]) => k + ": " + v + " pts").join("\n")
        : null;
      const scorePill = (s.match_score != null)
        ? '<abbr class="gloss" style="border:1px solid var(--rule);border-radius:5px;padding:1px 6px;' +
          'font-family:var(--mono);font-size:11px;font-weight:700' +
          (s.match_score >= 70 ? ";background:var(--ok-soft);color:var(--ok)" : s.match_score >= 40 ? "" : ";color:var(--muted)") +
          '"' + (scoreTitle ? ' title="' + esc(scoreTitle) + '"' : "") + ">" + s.match_score + "% match</abbr>"
        : "";
      return '<div class="row" style="justify-content:space-between;margin-top:8px;align-items:flex-start">' +
        '<div style="flex:1"><div><strong>' + esc(s.title) + "</strong> " +
        '<span class="mono" style="font-size:11px;color:var(--muted)">' + tierBadge +
        (s.band && s.band.length ? " · " + esc(s.band.join("/")) : "") + "</span> " + scorePill + "</div>" +
        (s.primary_metric ? '<div style="font-size:12px;margin-top:3px">The real question: ' + esc(s.primary_metric) + "</div>" : "") +
        (teaches ? '<div style="font-size:12px;color:var(--muted);margin-top:2px">Teaches: ' + teaches + "</div>" : "") +
        '<div style="font-size:12px;color:var(--muted);margin-top:2px">Matches their interest in ' + esc(s.domain || "this domain") +
        (s.why_it_engages ? ": " + esc(s.why_it_engages) : "") +
        (s.career_title ? " &mdash; a real path here: " + esc(s.career_title) : "") + "</div></div>" +
        '<button class="btn ghost" data-use-suggestion="' + esc(s.case_id) + '">Use this</button>' +
        "</div>";
    }).join("") + "</div>";
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
    '<div id="a-suggest-wrap"></div>' +
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
  const shown = STATE.badges.filter((b) =>
    (!ROSTER_FILTER.program || b.program === ROSTER_FILTER.program) &&
    (!ROSTER_FILTER.cohort || b.cohort === ROSTER_FILTER.cohort) &&
    (!ROSTER_FILTER.status || b.status === ROSTER_FILTER.status));
  return rosterFilterHTML() + '<div class="rings">' + shown.map((b) => {
    return '<div class="ringcard"><div style="width:100%">' +
      '<div class="who">' + esc(b.name) + "</div>" +
      '<div class="det">' + esc(b.program) + " &middot; " + b.badges + "/" + b.badges_total + " badges &middot; " + b.cases_done + "/" + b.cases_required + " cases</div>" +
      '<div style="margin-top:8px;display:flex;flex-direction:column;gap:4px">' +
      (b.slots || []).map((s) => {
        const label = s.name || ("Badge " + (s.index + 1));
        if (s.status === 'earned') {
          return '<div style="font-size:12px"><span class="pill ok" style="margin-right:6px">earned</span>' + esc(label) + "</div>";
        }
        if (s.status === 'eligible') {
          return '<div style="font-size:12px">' + esc(label) + " &mdash; " + s.cases_done + "/" + s.cases_per_badge + " cases " +
            '<button class="btn" style="margin-left:6px;padding:3px 9px" data-award="' + esc(b.id) + '" data-slot="' + s.index + '">Confirm award</button></div>';
        }
        return '<div style="font-size:12px;color:var(--muted)">' + esc(label) + " &mdash; " + s.cases_done + "/" + s.cases_per_badge + " cases" +
          (s.cases_done === s.cases_per_badge - 1 ? ' <span class="pill warn">one case short</span>' : "") + "</div>";
      }).join("") +
      "</div></div></div>";
  }).join("") + "</div>";
}

// ---------------------------------------------------------- class dash ----
function renderClassDashboard() {
  if (!CLASS_DASH) return '<div class="card empty">Loading…</div>';
  if (CLASS_DASH.error) return '<div class="card empty">' + esc(CLASS_DASH.error) + "</div>";
  const d = CLASS_DASH;
  let html = '<p style="font-size:12.5px;color:var(--muted);margin-bottom:14px">Live aggregate across ' +
    d.learner_count + ' active learners — what the class is into, what\'s working, and where they\'re stuck, ' +
    "to help match Heroes to their next case. Every number here is derived live, same as the rest of this app.</p>";

  html += '<div class="grid2">';
  html += '<div class="card"><h3 style="margin-bottom:8px;font-size:15px">Topics being considered</h3>' +
    (d.topics.length
      ? d.topics.map((t) => '<div class="row" style="justify-content:space-between;padding:5px 0;border-bottom:1px solid var(--rule-2)">' +
          '<span>' + esc(t.branch) + '</span><span class="pill accent">' + t.learners.length + "</span></div>").join("")
      : '<p style="font-size:12.5px;color:var(--muted)">No current-course data on file yet — set it on a learner\'s self-assessment.</p>') +
    "</div>";
  html += '<div class="card"><h3 style="margin-bottom:8px;font-size:15px">Careers of interest</h3>' +
    (d.careers.length
      ? d.careers.map((c) => '<div class="row" style="justify-content:space-between;padding:5px 0;border-bottom:1px solid var(--rule-2)">' +
          '<span>' + esc(c.title) + '</span><span class="pill accent">' + c.learners.length + "</span></div>").join("")
      : '<p style="font-size:12.5px;color:var(--muted)">No interests on file yet.</p>') +
    "</div></div>";

  html += '<div class="grid2">';
  html += '<div class="card"><h3 style="margin-bottom:4px;font-size:15px">Areas of strength</h3>' +
    '<p style="font-size:11.5px;color:var(--muted);margin:0 0 8px">Highest accept-rate domains across reviewed submissions.</p>' +
    (d.strengths.length
      ? d.strengths.map((s) => '<div class="row" style="justify-content:space-between;padding:5px 0;border-bottom:1px solid var(--rule-2)">' +
          '<span>' + esc(s.domain) + '</span><span class="mono" style="font-size:12px">' + s.accept_rate + "% (" + s.total + ")</span></div>").join("")
      : '<p style="font-size:12.5px;color:var(--muted)">No reviewed submissions yet.</p>') +
    "</div>";
  html += '<div class="card"><h3 style="margin-bottom:4px;font-size:15px">Areas of difficulty</h3>' +
    '<p style="font-size:11.5px;color:var(--muted);margin:0 0 8px">Lowest accept-rate domains — candidates for a check-in or a different case.</p>' +
    (d.difficulties.length
      ? d.difficulties.map((s) => '<div class="row" style="justify-content:space-between;padding:5px 0;border-bottom:1px solid var(--rule-2)">' +
          '<span>' + esc(s.domain) + '</span><span class="mono" style="font-size:12px">' + s.accept_rate + "% (" + s.total + ")</span></div>").join("")
      : '<p style="font-size:12.5px;color:var(--muted)">No reviewed submissions yet.</p>') +
    "</div></div>";

  if (d.overdue.length || d.needs_resubmission.length) {
    html += '<div class="card"><h3 style="margin-bottom:8px;font-size:15px">Needs attention right now</h3>' +
      d.overdue.concat(d.needs_resubmission).map((q) =>
        '<div class="exc-row"><div style="flex:1"><div class="who">' + esc(q.learner) + '</div>' +
        '<div class="det">' + esc(q.kind) + " — " + esc(q.detail) + "</div></div></div>").join("") +
      "</div>";
  }
  if (d.no_self_assessment.length) {
    html += '<div class="card"><h3 style="margin-bottom:6px;font-size:15px">No goals/interests on file</h3>' +
      '<p style="font-size:12.5px;color:var(--muted)">' + d.no_self_assessment.map(esc).join(", ") + "</p></div>";
  }
  return html;
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
  if (addBtn) addBtn.onclick = async () => {
    try {
      const r = await call("/api/learner/add", {
        display_name: val("new-name"), program: val("new-program"), cohort: val("new-cohort"),
        goals: val("new-goals"),
      });
      const box = document.getElementById("new-learner-result");
      if (box) box.innerHTML = '<div class="msg ok">Added <strong>' + esc(r.id) + '</strong> — student portal passcode: <strong class="mono">' + esc(r.passcode) + "</strong>. Give this to the Hero to sign in at /student-login.</div>";
      const nameEl = document.getElementById("new-name");
      if (nameEl) { nameEl.value = ""; document.getElementById("new-goals").value = ""; document.getElementById("new-cohort").value = ""; }
    } catch (e) { /* call() already flashed the error */ }
  };

  document.querySelectorAll("[data-save-goals]").forEach((b) => b.onclick = () =>
    call("/api/learner/goals", {learner_id: b.dataset.saveGoals, goals: val("goals-" + b.dataset.saveGoals)}));

  document.querySelectorAll("[data-reset-passcode]").forEach((b) => b.onclick = () => {
    if (!confirm("Reset the student portal passcode for " + b.dataset.name + "? Their old passcode will stop working immediately.")) return;
    call("/api/learner/passcode/reset", {learner_id: b.dataset.resetPasscode});
  });

  ["program", "cohort", "status"].forEach((dim) => {
    const sel = document.getElementById("filter-" + dim);
    if (sel) sel.onchange = () => { ROSTER_FILTER[dim] = sel.value; render(); };
  });

  document.querySelectorAll(".set-status").forEach((b) => b.onclick = () =>
    call("/api/learner/status", {learner_id: b.dataset.learner, status: b.dataset.status}));

  document.querySelectorAll("[data-save-sa]").forEach((b) => b.onclick = () => {
    const lid = b.dataset.saveSa;
    const interests = Array.from(document.querySelectorAll('[data-interest-tag="' + lid + '"]:checked')).map((c) => c.value);
    if (!interests.length) return flash("Pick at least one interest tag first.", true);
    const gradeRaw = val("sa-grade-" + lid);
    const branchRaw = val("sa-branch-" + lid);
    call("/api/learner/self-assessment", {
      learner_id: lid, interests, note: val("sa-note-" + lid), captured_by: val("sa-by-" + lid),
      grade_level: gradeRaw ? parseInt(gradeRaw, 10) : null,
      current_branch: branchRaw || null,
    });
  });

  document.querySelectorAll("[data-review-sa]").forEach((b) => b.onclick = () => {
    const lid = b.dataset.reviewSa;
    call("/api/learner/self-assessment/review", {learner_id: lid, reviewed_by: val("sa-reviewer-" + lid)});
  });

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

  document.querySelectorAll("[data-complete]").forEach((b) => b.onclick = () => {
    let badgeIndex = b.dataset.badge ? Number(b.dataset.badge) : null;
    if (badgeIndex === null) {
      const inline = document.getElementById("badge-" + b.dataset.complete);
      if (inline && inline.value !== "") badgeIndex = Number(inline.value);
      else return flash("Pick a badge slot first — that's what the number field is for.", true);
    }
    call("/api/complete", {assignment_id: b.dataset.complete, badge_index: badgeIndex});
  });

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

  const learnerSelect = document.getElementById("a-learner");
  const suggestWrap = document.getElementById("a-suggest-wrap");
  if (learnerSelect && suggestWrap) {
    const updateSuggestions = async () => {
      if (!learnerSelect.value) { suggestWrap.innerHTML = ""; return; }
      try {
        const r = await api("/api/suggest-cases?learner_id=" + encodeURIComponent(learnerSelect.value));
        const learner = STATE.learners.find((l) => l.id === learnerSelect.value);
        const reviewed = !!(learner && learner.self_assessment && learner.self_assessment.reviewed_by_guide);
        suggestWrap.innerHTML = suggestionCardsHTML(r.suggestions || [], reviewed);
        suggestWrap.querySelectorAll("[data-use-suggestion]").forEach((b) => b.onclick = () => {
          caseSelect.value = b.dataset.useSuggestion;
          caseSelect.dispatchEvent(new Event("change"));
        });
      } catch (e) { suggestWrap.innerHTML = ""; }  // no self-assessment yet is not an error state
    };
    learnerSelect.addEventListener("change", updateSuggestions);
    updateSuggestions();
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
