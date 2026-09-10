"""app/admin_core.py — the case-track/submission-score business logic, store-agnostic.

Everything in this file used to live directly inside admin_server.py, coupled to
real files on disk via a `project` path string. It's extracted here and
parameterized on a `store` object instead, so the exact same rules — assignment
eligibility, the assigned -> submitted -> reviewed -> complete state machine,
badge math, the never-auto-award-a-badge / never-auto-complete limits — run
identically whether the caller is the local stdlib server (app/store_local.py,
real files) or the hosted Vercel app (app/store_postgres.py, Neon Postgres).

A `store` duck-types this contract (not enforced via ABC -- matches this
project's minimal-machinery style):
    store.load(name) -> dict                 # name is a readmodel/*.json filename
    store.save(name, data) -> None            # snapshots first, same as before
    store.write_submitted_file(path, learner_id, case_id, content, content_type=None) -> None
    store.materialized_project(file_paths=None) -> context manager yielding a
        real filesystem directory laid out like the project root, for the two
        subprocess-based scoring scripts to operate on. See app/store_postgres.py
        for what this does when there's no real project directory to begin with.

This module does not introduce new policy — same rules as
skills/case-track/SKILL.md and skills/submission-score/SKILL.md documented
before any of this had a UI on top of it.
"""
import csv, datetime, io, json, os, random, re, subprocess, sys, unicodedata

_APP_DIR = os.path.dirname(os.path.abspath(__file__))
_CASES_DIR = os.path.join(os.path.dirname(_APP_DIR), 'cases')


def case_interactive_filename(title):
    return f"{title} - Interactive.html"


def is_student_published_file(case_id, filename):
    """True iff cases/<case_id>/published/<filename> is on this case's own
    MANIFEST.json with audience == "student" -- the boundary the public,
    unauthenticated /cases/<id>/published/<filename> route relies on to
    serve the student-facing Case Study.docx/Data.xlsx/Interactive.html
    while continuing to hard-block Facilitator Guide.docx and Guide Notes.docx
    (audience == "facilitator"), which contain the balance/twist/trap answers
    and must never be reachable without an admin login.

    Reads the manifest fresh every call rather than caching: this is a
    request-time authorization check, and a stale cache here would be a
    security bug, not a performance one -- MANIFEST.json is small and this
    route is not hot enough to need caching.

    Diagnosed 2026-08-21: for months this route accepted *only* an exact
    ' - Interactive.html' suffix, so the dashboard's own "Downloads" panel
    (built from this same MANIFEST.json data) linked to docx/xlsx URLs that
    404'd for every single case in the corpus -- not a case-specific bug.
    """
    manifest_path = os.path.join(_CASES_DIR, case_id, 'published', 'MANIFEST.json')
    if os.path.isfile(manifest_path):
        try:
            with open(manifest_path, encoding='utf-8') as f:
                manifest = json.load(f)
        except (json.JSONDecodeError, OSError):
            return False
        return any(
            entry.get('audience') == 'student' and entry.get('name') == filename
            for entry in manifest.get('files', [])
        )
    # No manifest (a handful of older cases -- see 2026-08-21 fix notes):
    # fall back to a filename-shape allowlist, still with an explicit
    # facilitator-material denylist so a missing manifest can never widen
    # access, only narrow it relative to the manifest path above.
    if re.search(r'facilitator|guide notes', filename, re.IGNORECASE):
        return False
    return bool(re.search(r'[-—] (Interactive\.html|Case Study\.docx|Data\.xlsx)$', filename))


def _case_interactive_info(case_id, title):
    """Whether cases/<id>/published/<title> - Interactive.html exists on disk --
    cases/ ships as static, read-only content in the deployment bundle (never in
    Postgres, see store_postgres.py's own docstring), so a plain filesystem check
    is correct in both local and hosted modes. Many `legacy` cases have no
    interactive page at all (see admin_html.py's own LEGACY pill) -- surfacing
    that here means the student portal can say so instead of linking to a 404."""
    filename = case_interactive_filename(title)
    exists = os.path.isfile(os.path.join(_CASES_DIR, case_id, 'published', filename))
    return filename, exists


# ---------------------------------------------------------------- errors ---
class ApiError(Exception):
    def __init__(self, code, msg):
        super().__init__(msg)
        self.code = code
        self.msg = msg


# ------------------------------------------------------------ utilities ----
def live(rows):
    return [r for r in rows if not r.get('_example')]


def _rating_summary(ratings, case_id):
    rs = [r['stars'] for r in ratings if r['case_id'] == case_id]
    return {"avg_rating": round(sum(rs) / len(rs), 1) if rs else None, "rating_count": len(rs)}


def slugify(s):
    # NFKD + drop combining marks first, so "Théo" -> "theo" (transliterated) rather than
    # silently vanishing into "th-o" the moment the regex below hits a non-ASCII character.
    ascii_s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    return re.sub(r'[^a-z0-9]+', '-', ascii_s.lower()).strip('-')


def today():
    return datetime.date.today().isoformat()


def _gen_passcode(existing):
    """A short numeric code a Hero can type on a shared classroom device -- not a
    real credential (see admin_web/app.py's own passcode-gate docstring for the
    same tradeoff at the guide layer). Excludes anything already in use so two
    learners never collide."""
    while True:
        code = f"{random.randint(0, 9999):04d}"
        if code not in existing:
            return code


_SUB_SEQ_RX = re.compile(r'__sub(\d+)$')


def _submission_sort_key(s):
    # "latest submission" was being decided by submitted_on alone (a date, no time), which
    # ties whenever a learner submits and resubmits the same day -- a common case, not an
    # edge case. Worse, the Postgres-backed store's SELECT has no ORDER BY, so which same-day
    # row a stable sort keeps as "first" is undefined, meaning the wrong submission (e.g. a
    # 'revise' rather than the later 'accepted' one) could silently win on the hosted app even
    # though it never did locally (a plain JSON list preserves real append order). do_record_
    # submission's own ids ("<assignment>__sub<n>", n = count-at-creation-time + 1) are already
    # a reliable, monotonically increasing sequence regardless of same-day collisions or
    # storage backend, so use that as the real tiebreaker instead of trusting row order.
    m = _SUB_SEQ_RX.search(s.get('id', ''))
    return (s.get('submitted_on', ''), int(m.group(1)) if m else -1)


# ------------------------------------------------------- read-side view ----
def compute_queue(roster, subs):
    TODAY = datetime.date.today()
    learners = {l['id']: l for l in live(roster['learners']) if l['status'] == 'active'}
    A = [a for a in live(subs['assignments']) if a['learner_id'] in learners]
    SUB_LATEST = {}
    for s in live(subs['submissions']):
        prev = SUB_LATEST.get(s['assignment_id'])
        if not prev or s['submitted_on'] >= prev['submitted_on']:
            SUB_LATEST[s['assignment_id']] = s
    DISC = {}
    for d in live(subs['discussions']):
        k = (d['learner_id'], d['case_id'])
        DISC[k] = DISC.get(k, 0) + 1
    prog = roster['programs']

    def days(d):
        return (TODAY - datetime.date.fromisoformat(d)).days

    Q = []
    for a in A:
        L = learners[a['learner_id']]
        sub = SUB_LATEST.get(a['id'])
        dc = DISC.get((a['learner_id'], a['case_id']), 0)
        if a['status'] == 'assigned':
            if a.get('due_on') and days(a['due_on']) > 0:
                Q.append({"severity": 1, "kind": "OVERDUE", "learner": L['display_name'],
                          "learner_id": L['id'], "case_id": a['case_id'],
                          "detail": f"due {a['due_on']} ({days(a['due_on'])}d ago), nothing submitted",
                          "action": "check in with the Hero", "assignment_id": a['id']})
            elif days(a['assigned_on']) > 21:
                Q.append({"severity": 4, "kind": "STALE", "learner": L['display_name'],
                          "learner_id": L['id'], "case_id": a['case_id'],
                          "detail": f"assigned {days(a['assigned_on'])}d ago, no due date, no activity",
                          "action": "set a due date or withdraw", "assignment_id": a['id']})
        if a['status'] == 'submitted':
            d = days(sub['submitted_on']) if sub else 0
            Q.append({"severity": 2, "kind": "AWAITING REVIEW", "learner": L['display_name'],
                      "learner_id": L['id'], "case_id": a['case_id'], "detail": f"submitted {d}d ago",
                      "action": "read the pitch and set an outcome", "assignment_id": a['id'],
                      "submission_id": sub['id'] if sub else None})
        # UAT FINDING 2026-08-09: ported faithfully from case-track/SKILL.md's own worked
        # exception-queue example, which gates DISCUSSION SHORT / READY TO COMPLETE on
        # status=='reviewed' alone, never checking the review's own outcome. A 'reviewed'
        # assignment whose outcome is 'revise' (or 'not-accepted') isn't blocked on
        # discussions at all -- it's blocked on a resubmission that hasn't happened yet.
        # Reporting "0/2 discussions logged, schedule participation" there is actively
        # misleading (do_complete() already correctly refuses unless outcome=='accepted';
        # this is a read-side messaging bug, not a write-side gate bug). Split on outcome.
        if a['status'] == 'reviewed' and sub and sub.get('outcome') == 'accepted':
            if dc < 2:
                Q.append({"severity": 3, "kind": "DISCUSSION SHORT", "learner": L['display_name'],
                          "learner_id": L['id'], "case_id": a['case_id'],
                          "detail": f"accepted, {dc}/2 discussions logged",
                          "action": "schedule or log participation", "assignment_id": a['id']})
            else:
                Q.append({"severity": 2, "kind": "READY TO COMPLETE", "learner": L['display_name'],
                          "learner_id": L['id'], "case_id": a['case_id'], "detail": f"accepted + {dc} discussions",
                          "action": "confirm complete and assign a badge slot", "assignment_id": a['id']})
        elif a['status'] == 'reviewed' and sub and sub.get('outcome') in ('revise', 'not-accepted'):
            Q.append({"severity": 2, "kind": "NEEDS RESUBMISSION", "learner": L['display_name'],
                      "learner_id": L['id'], "case_id": a['case_id'],
                      "detail": f"outcome={sub['outcome']} on {sub.get('reviewed_on')}",
                      "action": "record the Hero's resubmission when it comes in", "assignment_id": a['id']})

    for lid, L in learners.items():
        p = prog[L['program']]
        per = p['cases_per_badge']
        done = [a for a in A if a['learner_id'] == lid and a['status'] == 'complete']
        byslot = {}
        for a in done:
            byslot[a.get('badge_index')] = byslot.get(a.get('badge_index'), 0) + 1
        earned = {b['badge_index'] for b in L.get('badges_earned', [])}
        for slot, n in byslot.items():
            if slot is None:
                Q.append({"severity": 3, "kind": "UNALLOCATED COMPLETION", "learner": L['display_name'],
                          "learner_id": lid, "detail": f"{n} complete case(s) with no badge_index",
                          "action": "assign them to a badge slot"})
                continue
            if n >= per and slot not in earned:
                Q.append({"severity": 1, "kind": "BADGE ELIGIBLE", "learner": L['display_name'],
                          "learner_id": lid, "detail": f"badge {slot}: {n}/{per} complete",
                          "action": "CONFIRM AWARD", "badge_index": slot})
            elif n == per - 1:
                Q.append({"severity": 2, "kind": "ONE CASE SHORT", "learner": L['display_name'],
                          "learner_id": lid, "detail": f"badge {slot}: {n}/{per} complete",
                          "action": "assign the last case"})
        if not [a for a in A if a['learner_id'] == lid and a['status'] in ('assigned', 'submitted', 'reviewed')]:
            Q.append({"severity": 3, "kind": "NO OPEN WORK", "learner": L['display_name'], "learner_id": lid,
                      "detail": "active learner with no open assignment", "action": "assign a case"})
    Q.sort(key=lambda q: q['severity'])
    return Q


def compute_badge_rows(roster, subs):
    prog = roster['programs']
    A = live(subs['assignments'])
    out = []
    for L in live(roster['learners']):
        p = prog[L['program']]
        done = [a for a in A if a['learner_id'] == L['id'] and a['status'] == 'complete']
        total = len(done)
        earned_n = len(L.get('badges_earned', []))
        byslot = {}
        for a in done:
            byslot[a.get('badge_index')] = byslot.get(a.get('badge_index'), 0) + 1
        earned_slots = {b['badge_index'] for b in L.get('badges_earned', [])}
        one_short = any(n == p['cases_per_badge'] - 1 for slot, n in byslot.items() if slot not in earned_slots)
        eligible = [slot for slot, n in byslot.items()
                    if slot is not None and n >= p['cases_per_badge'] and slot not in earned_slots]
        names = p.get('badge_names') or []
        slots = []
        for i in range(p['badges']):
            if i in earned_slots:
                st = 'earned'
            elif i in eligible:
                st = 'eligible'
            else:
                st = 'in_progress'
            slots.append({
                "index": i, "name": names[i] if i < len(names) else None, "status": st,
                "cases_done": byslot.get(i, 0), "cases_per_badge": p['cases_per_badge'],
            })
        out.append({
            "id": L['id'], "name": L['display_name'], "program": L['program'], "cohort": L.get('cohort'),
            "status": L['status'], "badges": earned_n, "badges_total": p['badges'],
            "cases_done": total, "cases_required": p['cases_required'], "cases_per_badge": p['cases_per_badge'],
            "one_short": one_short, "eligible_slots": eligible, "slots": slots,
        })
    return out


def build_state(store):
    roster = store.load('roster.json')
    subs = store.load('submissions.json')
    cases_idx = store.load('cases_index.json')
    def _case_view(c):
        title = c.get('title') or c['id']
        filename, has_interactive = _case_interactive_info(c['id'], title)
        return {"id": c['id'], "title": title, "tier": c.get('tier'), "complexity": c.get('complexity'),
                "status": c.get('status'),
                "band": c.get('band') or [], "standards_count": c.get('standards_count'),
                "domains_touched": c.get('domains_touched') or [],
                "interactive_file": filename, "has_interactive": has_interactive}

    assignable_cases = sorted(
        [_case_view(c) for c in cases_idx.get('cases', []) if c.get('status') in ('published', 'legacy')],
        # published (real, vetted content) before legacy (older corpus, often
        # missing case.json/interactive HTML) -- a guide picking blind from an
        # alphabetical list was landing on a legacy case by default. Within
        # each group, sort by band then title so MS/HS don't interleave.
        key=lambda c: (c['status'] != 'published', ','.join(sorted(c['band'])), c['title']))

    ratings = subs.get('ratings', [])
    for c in assignable_cases:
        c.update(_rating_summary(ratings, c['id']))

    A = live(subs['assignments'])
    S = live(subs['submissions'])
    D = live(subs['discussions'])
    SC = [s for s in subs.get('scores', []) if not s.get('_example')]
    cases_by_id = {c['id']: c for c in assignable_cases}

    assignments_view = []
    for a in A:
        my_subs = sorted([s for s in S if s['assignment_id'] == a['id']], key=_submission_sort_key)
        latest = my_subs[-1] if my_subs else None
        my_scores = sorted([s for s in SC if s['learner_id'] == a['learner_id'] and s['case_id'] == a['case_id']],
                            key=lambda s: s['scored_on'])
        latest_score = my_scores[-1] if my_scores else None
        dcount = len([d for d in D if d['learner_id'] == a['learner_id'] and d['case_id'] == a['case_id']])
        c = cases_by_id.get(a['case_id'])
        assignments_view.append({**a, "latest_submission": latest, "latest_score": latest_score,
                                  "discussion_count": dcount, "n_submissions": len(my_subs),
                                  "case_title": c['title'] if c else a['case_id'],
                                  "interactive_file": c['interactive_file'] if c else None,
                                  "has_interactive": bool(c and c['has_interactive']),
                                  "complexity": c.get('complexity') if c else None,
                                  "avg_rating": c.get('avg_rating') if c else None,
                                  "rating_count": c.get('rating_count') if c else 0,
                                  "my_rating": next((r['stars'] for r in ratings
                                                      if r['learner_id'] == a['learner_id']
                                                      and r['case_id'] == a['case_id']), None)})

    domains_doc = store.load('domains.json')
    tree_doc = store.load('curriculum_tree.json')
    return {
        "today": today(),
        "programs": roster['programs'],
        "learners": live(roster['learners']),
        "cases": assignable_cases,
        "assignments": assignments_view,
        "discussions": D,
        "queue": compute_queue(roster, subs),
        "badges": compute_badge_rows(roster, subs),
        # Phase 2 (goals/career self-assessment): the fixed tag list a guide picks from is
        # domains.json's own real clusters, not a new taxonomy -- see do_set_self_assessment.
        "interest_clusters": [{"id": c['id'], "name": c['name']} for c in domains_doc.get('clusters', [])],
        # Same idea for "what course are they in" -- reuse curriculum_tree.json's 10 real
        # branches (the same ones dashboard.html's Tree of Thought already renders) rather
        # than invent a second course taxonomy.
        "curriculum_branches": [{"id": b['id'], "branch": b['branch'], "band": b['band']}
                                 for b in tree_doc.get('branches', [])],
    }


# --------------------------------------------------------------- writes ----
def _add_learner_to_roster(roster, display_name, program, cohort, status, learner_id, goals=None):
    """Pure mutation on an already-loaded roster dict -- shared by the single-add
    endpoint and the CSV bulk-add path, so bulk upload does one load+save for the
    whole file instead of one round-trip (and one snapshot) per row."""
    if not display_name or not display_name.strip():
        raise ApiError(400, "display_name is required")
    display_name = display_name.strip()
    if program not in roster['programs']:
        raise ApiError(400, f"unknown program {program!r} -- must be one of {list(roster['programs'])}")
    lid = (learner_id or slugify(display_name)).strip()
    if not lid:
        raise ApiError(400, "could not derive a learner id from that name")
    if any(l['id'] == lid for l in roster['learners']):
        raise ApiError(409, f"learner id {lid!r} already exists")
    if status and status not in ('active', 'paused', 'alumni'):
        raise ApiError(400, f"status must be active/paused/alumni, got {status!r}")
    existing_codes = {l.get('passcode') for l in roster['learners'] if l.get('passcode')}
    passcode = _gen_passcode(existing_codes)
    roster['learners'].append({
        "id": lid, "display_name": display_name, "program": program, "cohort": (cohort or "").strip() or None,
        "status": status or "active", "started_on": today(), "badges_earned": [],
        "drive_folder_id": None, "drive_folder_url": None, "notes": "",
        "goals": (goals or "").strip(), "passcode": passcode,
    })
    return lid, passcode


def do_add_learner(store, display_name, program, cohort, status, learner_id, goals=None):
    roster = store.load('roster.json')
    lid, passcode = _add_learner_to_roster(roster, display_name, program, cohort, status, learner_id, goals)
    store.save('roster.json', roster)
    return lid, passcode


def do_set_learner_goals(store, learner_id, goals):
    roster = store.load('roster.json')
    learner = next((l for l in roster['learners'] if l['id'] == learner_id), None)
    if not learner:
        raise ApiError(404, f"learner {learner_id} not found")
    learner['goals'] = (goals or "").strip()
    store.save('roster.json', roster)


def do_reset_passcode(store, learner_id):
    roster = store.load('roster.json')
    learner = next((l for l in roster['learners'] if l['id'] == learner_id), None)
    if not learner:
        raise ApiError(404, f"learner {learner_id} not found")
    existing = {l.get('passcode') for l in roster['learners'] if l.get('passcode')}
    learner['passcode'] = _gen_passcode(existing)
    store.save('roster.json', roster)
    return learner['passcode']


def do_bulk_add_learners_csv(store, csv_text):
    """Expected columns (header row required, case-insensitive, extra columns
    ignored): display_name, program, cohort (optional), status (optional,
    default active), id (optional, auto-slugified from display_name if absent),
    goals (optional, free text). Partial success is normal and expected for a
    bulk import -- report every row's outcome rather than failing the whole file
    on the first bad row (same 'absent/wrong is a first-class reportable state,
    not a silent all-or-nothing' spirit the rest of this project applies
    everywhere else)."""
    reader = csv.DictReader(io.StringIO(csv_text))
    if not reader.fieldnames:
        raise ApiError(400, "empty CSV -- no header row found")
    norm_fields = {f.strip().lower(): f for f in reader.fieldnames}
    if 'display_name' not in norm_fields or 'program' not in norm_fields:
        raise ApiError(400, f"CSV header must include display_name and program columns "
                            f"(found: {list(reader.fieldnames)})")

    roster = store.load('roster.json')
    added, skipped = [], []
    for i, row in enumerate(reader, start=2):  # header is row 1
        def get(col):
            key = norm_fields.get(col)
            return (row.get(key) or '').strip() if key else ''
        name = get('display_name')
        if not name:
            skipped.append({"row": i, "reason": "blank display_name"})
            continue
        try:
            lid, passcode = _add_learner_to_roster(roster, name, get('program'), get('cohort'),
                                                     get('status') or None, get('id') or None, get('goals'))
            added.append({"row": i, "id": lid, "display_name": name, "passcode": passcode})
        except ApiError as e:
            skipped.append({"row": i, "display_name": name, "reason": e.msg})
    if added:
        store.save('roster.json', roster)
    return added, skipped


def do_set_learner_status(store, learner_id, status):
    if status not in ('active', 'paused', 'alumni'):
        raise ApiError(400, "status must be active/paused/alumni")
    roster = store.load('roster.json')
    learner = next((l for l in roster['learners'] if l['id'] == learner_id), None)
    if not learner:
        raise ApiError(404, f"learner {learner_id} not found")
    learner['status'] = status
    store.save('roster.json', roster)


VALID_GRADE_LEVELS = set(range(6, 13))  # 6-12, matches curriculum_tree.json's MS-through-HS span


def do_set_self_assessment(store, learner_id, interests, note, captured_by, grade_level=None, current_branch=None):
    """The goals/career conversation, guide-mediated for now (PLAN.md Phase 2 -- students
    don't have their own login yet, so this is entered by whoever had the conversation,
    same as review notes and discussion logs already are). interests[] are domains.json
    cluster ids, not free text -- a fixed, real taxonomy that already exists and is already
    validated at domain-build time (app/validate_domains.py), so there is nothing new to
    keep in sync. grade_level/current_branch are optional -- feeding suggest_cases() a real
    match score, not a hard requirement for capturing interests at all. current_branch is
    one of curriculum_tree.json's 10 real branch ids (the same taxonomy dashboard.html's own
    Tree of Thought uses), not a new course list invented for this feature. Setting a new
    self-assessment always resets reviewed_by_guide to False: a guide reviews *this* version,
    not a promise to re-review indefinitely."""
    roster = store.load('roster.json')
    learner = next((l for l in roster['learners'] if l['id'] == learner_id), None)
    if not learner:
        raise ApiError(404, f"learner {learner_id} not found")
    if not interests:
        raise ApiError(400, "pick at least one interest cluster")
    domains = store.load('domains.json')
    valid = {c['id'] for c in domains.get('clusters', [])}
    bad = [i for i in interests if i not in valid]
    if bad:
        raise ApiError(400, f"unknown interest cluster id(s): {bad} -- must be one of {sorted(valid)}")
    if grade_level is not None and grade_level not in VALID_GRADE_LEVELS:
        raise ApiError(400, f"grade_level must be one of {sorted(VALID_GRADE_LEVELS)} or omitted")
    if current_branch is not None:
        tree = store.load('curriculum_tree.json')
        valid_branches = {b['id'] for b in tree.get('branches', [])}
        if current_branch not in valid_branches:
            raise ApiError(400, f"unknown current_branch {current_branch!r} -- must be one of {sorted(valid_branches)}")
    learner['self_assessment'] = {
        "interests": interests,
        "note": note or "",
        "captured_on": today(),
        "captured_by": captured_by or "guide",
        "grade_level": grade_level,
        "current_branch": current_branch,
        "reviewed_by_guide": False,
        "reviewed_on": None,
        "reviewed_by": None,
    }
    store.save('roster.json', roster)


def do_review_self_assessment(store, learner_id, reviewed_by):
    roster = store.load('roster.json')
    learner = next((l for l in roster['learners'] if l['id'] == learner_id), None)
    if not learner:
        raise ApiError(404, f"learner {learner_id} not found")
    sa = learner.get('self_assessment')
    if not sa:
        raise ApiError(400, f"{learner['display_name']} has no self-assessment on file yet")
    sa['reviewed_by_guide'] = True
    sa['reviewed_on'] = today()
    sa['reviewed_by'] = reviewed_by or 'guide'
    store.save('roster.json', roster)


# Coarse, explicitly-a-heuristic mapping from grade level to the tier SPEC.md's own
# difficulty table (section 3) says that grade is ready for -- T1 "MS entry" through
# T4 "HS". Not calibrated against real outcomes yet; a reasonable starting point, not
# a claim of precision. Tune here if a cohort's actual fit says otherwise.
GRADE_TO_TIER = {6: 1, 7: 1, 8: 2, 9: 2, 10: 3, 11: 3, 12: 4}
TIER_NUM = {"T1": 1, "T2": 2, "T3": 3, "T4": 4}


def _match_score(case, dom_priority, learner_branch_domains, grade_level):
    """Returns (score 0-100, breakdown dict of label -> points) for one candidate case
    against one learner. Three components, each capped so no single signal can dominate
    the other two:
      - domain fit (0-30): how strongly the matched interest domain is prioritized for
        authoring (domains.json's own authoring_priority -- a real, existing signal for
        "this domain has a well-thought-through case pipeline behind it", not a guess).
      - skills overlap (0-30): how many of the case's domains_touched land in the spine
        domains the learner's current course (curriculum_tree.json's acton_domains for
        their current_branch) actually feeds -- i.e. is this case teaching what they're
        learning in class right now, not just a topic they said they like.
      - tier/grade fit (0-40): distance between the case's real T1-T4 tier and the tier
        GRADE_TO_TIER expects for their grade. Weighted heaviest, on purpose -- a case a
        student can't realistically do yet (or that's beneath them) is the failure mode
        a guide most needs the shortlist to catch. An unknown (legacy) tier or unset
        grade_level score low/neutral rather than being excluded -- absent data is
        surfaced as a real cost, never guessed away.
    """
    breakdown = {}
    domain_pts = {"HIGH": 30, "MEDIUM": 20, "LOW": 10}.get(dom_priority, 10)
    breakdown["Matches a priority interest area"] = domain_pts

    touched = set(case.get('domains_touched') or [])
    overlap = len(touched & learner_branch_domains) if learner_branch_domains else 0
    skills_pts = min(30, overlap * 10) if learner_branch_domains else 15
    breakdown["Overlaps their current course" if learner_branch_domains else "Current course not on file"] = skills_pts

    tier = case.get('tier')
    tier_num = TIER_NUM.get(tier)
    if tier_num and grade_level and grade_level in GRADE_TO_TIER:
        dist = abs(tier_num - GRADE_TO_TIER[grade_level])
        tier_pts = {0: 40, 1: 20, 2: 5}.get(dist, 0)
        breakdown[f"{tier} fits grade {grade_level}" if dist == 0 else f"{tier} vs. expected tier for grade {grade_level}"] = tier_pts
    elif tier_num:
        tier_pts = 20
        breakdown[f"{tier}, real difficulty rating (grade not on file to check fit)"] = tier_pts
    else:
        tier_pts = 5
        breakdown["No tier yet — older, unvetted case"] = tier_pts

    return domain_pts + skills_pts + tier_pts, breakdown


def suggest_cases(store, learner_id, limit=5):
    """PLAN.md Phase 2c/2e. Turns a reviewed self-assessment into a short, explained,
    *ranked* shortlist instead of a guide scrolling all ~56 assignable cases blind.
    Reuses the exact same published/legacy eligibility rule build_state() already
    applies (never invent a second notion of 'assignable'), domains.json's own
    existing_cases[]/why_it_engages[]/careers[]/authoring_priority (already validated
    at build time by app/validate_domains.py), and curriculum_tree.json's real 10-branch
    course taxonomy (the same one dashboard.html's Tree of Thought renders) for the
    grade/course match -- no new taxonomy invented anywhere in this function. Returns []
    (not an error) for a learner with no reviewed self-assessment; the caller decides
    what that means for the UI."""
    roster = store.load('roster.json')
    learner = next((l for l in roster['learners'] if l['id'] == learner_id), None)
    if not learner:
        raise ApiError(404, f"learner {learner_id} not found")
    sa = learner.get('self_assessment')
    if not sa or not sa.get('reviewed_by_guide') or not sa.get('interests'):
        return []

    domains_doc = store.load('domains.json')
    id_to_name = {c['id']: c['name'] for c in domains_doc.get('clusters', [])}
    wanted_cluster_names = {id_to_name[i] for i in sa['interests'] if i in id_to_name}

    cases_idx = store.load('cases_index.json')
    by_title = {c.get('title'): c for c in cases_idx.get('cases', []) if c.get('status') in ('published', 'legacy')}

    subs = store.load('submissions.json')
    already = {a['case_id'] for a in live(subs['assignments']) if a['learner_id'] == learner_id}

    learner_branch_domains = set()
    if sa.get('current_branch'):
        tree = store.load('curriculum_tree.json')
        branch = next((b for b in tree.get('branches', []) if b['id'] == sa['current_branch']), None)
        if branch:
            learner_branch_domains = set(branch.get('acton_domains') or [])
    grade_level = sa.get('grade_level')

    priority_rank = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    seen_case_ids, candidates = set(), []
    matching_domains = [d for d in domains_doc.get('domains', []) if d.get('cluster') in wanted_cluster_names]
    matching_domains.sort(key=lambda d: priority_rank.get(d.get('authoring_priority'), 3))
    for dom in matching_domains:
        for title in dom.get('existing_cases', []):
            case = by_title.get(title)
            if not case or case['id'] in already or case['id'] in seen_case_ids:
                continue
            seen_case_ids.add(case['id'])
            career = dom.get('careers') or [{}]
            score, breakdown = _match_score(case, dom.get('authoring_priority'), learner_branch_domains, grade_level)
            candidates.append({
                "case_id": case['id'], "title": case.get('title') or case['id'],
                "tier": case.get('tier'), "band": case.get('band') or [],
                "domain": dom.get('name'), "why_it_engages": dom.get('why_it_engages'),
                "career_title": career[0].get('title'),
                # Case-specific, not the domain-level why_it_engages above -- multiple
                # suggestions can share a domain (and so share that sentence verbatim),
                # but domains_touched/standards_count/primary_metric are per-case, from
                # cases_index.json, so they're what actually differentiate one suggestion
                # from another instead of reading like repeated, broken copy.
                "domains_touched": case.get('domains_touched') or [],
                "standards_count": case.get('standards_count'),
                "primary_metric": case.get('primary_metric'),
                "match_score": score, "match_breakdown": breakdown,
            })
    # Real, explained ranking now (see _match_score) instead of a bare tier-known-first
    # sort -- that was a reasonable stopgap but couldn't account for grade fit or what
    # the learner is actually taking in class right now.
    candidates.sort(key=lambda c: -c["match_score"])
    return candidates[:limit]


def do_delete_learner(store, learner_id):
    """HARD delete -- deliberately NOT what skills/case-track/SKILL.md's own 'Never
    delete a learner' rule describes. That rule protects a real student's real
    history from being erased; the reason it says 'set status instead' is exactly
    that erasure risk. This exists for the different, narrower case the doctrine
    doesn't cover: correcting a mistake (a duplicate, a typo, test/fixture data --
    e.g. this project's own UAT pass added and then needed to remove a throwaway
    'Priya Nair' test learner by hand before this endpoint existed). Snapshotted
    first like every other write here, so it is recoverable from
    readmodel/_snapshots/ even though there's no in-app undo. Cascades: removes
    every assignment/submission/discussion/score row referencing this learner,
    not just the roster entry, so no orphaned rows are left pointing at a learner
    id that no longer exists."""
    roster = store.load('roster.json')
    learner = next((l for l in roster['learners'] if l['id'] == learner_id), None)
    if not learner:
        raise ApiError(404, f"learner {learner_id} not found")
    subs = store.load('submissions.json')
    counts = {
        "assignments": len([a for a in subs['assignments'] if a.get('learner_id') == learner_id]),
        "submissions": len([s for s in subs['submissions'] if s.get('learner_id') == learner_id]),
        "discussions": len([d for d in subs['discussions'] if d.get('learner_id') == learner_id]),
        "scores": len([s for s in subs.get('scores', []) if s.get('learner_id') == learner_id]),
    }
    roster['learners'] = [l for l in roster['learners'] if l['id'] != learner_id]
    subs['assignments'] = [a for a in subs['assignments'] if a.get('learner_id') != learner_id]
    subs['submissions'] = [s for s in subs['submissions'] if s.get('learner_id') != learner_id]
    subs['discussions'] = [d for d in subs['discussions'] if d.get('learner_id') != learner_id]
    if 'scores' in subs:
        subs['scores'] = [s for s in subs['scores'] if s.get('learner_id') != learner_id]
    store.save('roster.json', roster)
    store.save('submissions.json', subs)
    try:
        ov = store.load('score_overrides.json')
    except FileNotFoundError:
        ov = None
    if ov is not None:
        before = len(ov.get('overrides', []))
        ov['overrides'] = [o for o in ov.get('overrides', []) if o.get('learner_id') != learner_id]
        if len(ov['overrides']) != before:
            store.save('score_overrides.json', ov)
    return counts


def do_assign(store, learner_id, case_id, due_on, badge_index, assigned_by):
    roster = store.load('roster.json')
    subs = store.load('submissions.json')
    cases_idx = store.load('cases_index.json')

    learner = next((l for l in roster['learners'] if l['id'] == learner_id and not l.get('_example')), None)
    if not learner:
        raise ApiError(404, f"learner {learner_id} not found")
    if learner['status'] != 'active':
        raise ApiError(400, f"{learner['display_name']} is not active (status={learner['status']})")

    case = next((c for c in cases_idx.get('cases', []) if c.get('id') == case_id), None)
    if not case:
        raise ApiError(404, f"case {case_id} not found in cases_index.json")
    if case.get('status') not in ('published', 'legacy'):
        raise ApiError(400, f"{case_id} has not passed the gate (status={case.get('status')!r}); "
                            f"run case-publish first, or pick a published/legacy case")

    live_asg = live(subs['assignments'])
    if any(a['learner_id'] == learner_id and a['case_id'] == case_id and a['status'] in ('assigned', 'submitted', 'reviewed')
           for a in live_asg):
        raise ApiError(409, f"{learner['display_name']} already has an open assignment for {case_id}")
    if any(a['learner_id'] == learner_id and a['case_id'] == case_id and a['status'] == 'complete'
           for a in live_asg):
        raise ApiError(409, f"{learner['display_name']} has already completed {case_id}")

    aid = f"{learner_id}__{case_id}__{today()}"
    subs['assignments'].append({
        "id": aid, "learner_id": learner_id, "case_id": case_id, "assigned_on": today(),
        "due_on": due_on or None, "assigned_by": assigned_by or "facilitator",
        "badge_index": badge_index, "status": "assigned", "notes": "",
    })
    store.save('submissions.json', subs)
    return aid


def do_withdraw(store, assignment_id):
    subs = store.load('submissions.json')
    asg = next((a for a in subs['assignments'] if a['id'] == assignment_id), None)
    if not asg:
        raise ApiError(404, "assignment not found")
    asg['status'] = 'withdrawn'
    store.save('submissions.json', subs)


def do_record_submission(store, learner_id, case_id, artifacts, source):
    subs = store.load('submissions.json')
    live_asg = live(subs['assignments'])
    asg = next((a for a in live_asg if a['learner_id'] == learner_id and a['case_id'] == case_id
                and a['status'] in ('assigned', 'submitted', 'reviewed')), None)
    if not asg:
        raise ApiError(404, "no open assignment found for this learner and case")
    n = len([s for s in subs['submissions'] if s['assignment_id'] == asg['id']]) + 1
    sid = f"{asg['id']}__sub{n}"
    subs['submissions'].append({
        "id": sid, "assignment_id": asg['id'], "learner_id": learner_id, "case_id": case_id,
        "submitted_on": today(), "artifacts": artifacts, "source": source or "facilitator-dictated",
        "drive_artifacts": None, "reviewed_on": None, "reviewed_by": None, "review_note": None, "outcome": None,
    })
    asg['status'] = 'submitted'
    store.save('submissions.json', subs)
    return sid


def do_add_discussion(store, learner_id, case_id, date, mode, recorded_by, note):
    if mode not in ('live', 'written-500'):
        raise ApiError(400, "mode must be live or written-500")
    subs = store.load('submissions.json')
    n = len([d for d in live(subs['discussions']) if d['learner_id'] == learner_id and d['case_id'] == case_id]) + 1
    did = f"{learner_id}__{case_id}__d{n}"
    subs['discussions'].append({
        "id": did, "learner_id": learner_id, "case_id": case_id, "date": date or today(),
        "mode": mode, "recorded_by": recorded_by or "guide", "note": note or None,
    })
    store.save('submissions.json', subs)
    return did, n


def do_rate_case(store, learner_id, case_id, stars, note=None):
    if not isinstance(stars, int) or not (1 <= stars <= 5):
        raise ApiError(400, "stars must be an integer 1-5")
    subs = store.load('submissions.json')
    subs.setdefault('ratings', [])
    live_asg = live(subs['assignments'])
    asg = next((a for a in live_asg if a['learner_id'] == learner_id and a['case_id'] == case_id
                and a['status'] in ('submitted', 'reviewed', 'complete')), None)
    if not asg:
        raise ApiError(400, "rate a case only after submitting work for it")
    existing = next((r for r in subs['ratings'] if r['learner_id'] == learner_id and r['case_id'] == case_id), None)
    if existing:
        existing['stars'], existing['note'], existing['rated_on'] = stars, note or None, today()
        rid = existing['id']
    else:
        rid = f"{learner_id}__{case_id}__rating"
        subs['ratings'].append({"id": rid, "learner_id": learner_id, "case_id": case_id,
                                 "stars": stars, "note": note or None, "rated_on": today()})
    store.save('submissions.json', subs)
    return rid


def do_review(store, submission_id, outcome, review_note, reviewed_by):
    if outcome not in ('accepted', 'revise', 'not-accepted'):
        raise ApiError(400, "outcome must be accepted / revise / not-accepted")
    subs = store.load('submissions.json')
    sub = next((s for s in subs['submissions'] if s['id'] == submission_id), None)
    if not sub:
        raise ApiError(404, "submission not found")
    sub['reviewed_on'] = today()
    sub['reviewed_by'] = reviewed_by or 'guide'
    sub['review_note'] = review_note or None
    sub['outcome'] = outcome
    asg = next((a for a in subs['assignments'] if a['id'] == sub['assignment_id']), None)
    if asg and asg['status'] == 'submitted':
        asg['status'] = 'reviewed'
    store.save('submissions.json', subs)


def do_complete(store, assignment_id, badge_index):
    subs = store.load('submissions.json')
    asg = next((a for a in subs['assignments'] if a['id'] == assignment_id), None)
    if not asg:
        raise ApiError(404, "assignment not found")
    my_subs = sorted([s for s in subs['submissions'] if s['assignment_id'] == assignment_id],
                      key=_submission_sort_key)
    latest = my_subs[-1] if my_subs else None
    if not latest or latest.get('outcome') != 'accepted':
        raise ApiError(400, "the latest submission is not outcome=accepted yet")
    dcount = len([d for d in live(subs['discussions'])
                  if d['learner_id'] == asg['learner_id'] and d['case_id'] == asg['case_id']])
    if dcount < 2:
        raise ApiError(400, f"only {dcount}/2 discussions logged (SPEC Challenge 5)")
    if badge_index is not None:
        asg['badge_index'] = badge_index
    if asg.get('badge_index') is None:
        raise ApiError(400, "badge_index is required to mark complete -- an unallocated completion is a real "
                            "gap in the record, not a detail (case-track/SKILL.md)")
    asg['status'] = 'complete'
    store.save('submissions.json', subs)


def do_score(store, learner_id, case_id, file_paths, note):
    if not file_paths:
        raise ApiError(400, "at least one file path is required")
    with store.materialized_project(file_paths=file_paths) as project:
        script = os.path.join(project, 'skills', 'submission-score', 'scripts', 'score_submission.py')
        cmd = [sys.executable, script, '--learner', learner_id, '--case', case_id, '--project', project, '--write']
        for fp in file_paths:
            cmd += ['--file', fp]
        if note:
            cmd += ['--note', note]
        res = subprocess.run(cmd, capture_output=True, text=True, cwd=project)
        if res.returncode != 0:
            raise ApiError(500, f"score_submission.py exited {res.returncode}:\n{res.stderr[-4000:]}")
        return res.stdout


def do_guide_confirm(store, learner_id, case_id, by, overrides, scored_on):
    if not by:
        raise ApiError(400, "a name is required to confirm (guide_confirm.py --by)")
    with store.materialized_project() as project:
        script = os.path.join(project, 'skills', 'submission-score', 'scripts', 'guide_confirm.py')
        cmd = [sys.executable, script, '--learner', learner_id, '--case', case_id, '--by', by,
               '--project', project, '--write']
        if scored_on:
            cmd += ['--scored-on', scored_on]
        for ov in (overrides or []):
            if not ov.get('criterion') or not ov.get('level') or not ov.get('reason'):
                raise ApiError(400, "every override needs a criterion, a level, and a reason")
            cmd += ['--override', f"{ov['criterion']}={ov['level']}", '--reason', ov['reason']]
        res = subprocess.run(cmd, capture_output=True, text=True, cwd=project)
        if res.returncode != 0:
            raise ApiError(500, f"guide_confirm.py exited {res.returncode}:\n{res.stderr[-4000:]}")
        return res.stdout


def do_award_badge(store, learner_id, badge_index, awarded_by):
    roster = store.load('roster.json')
    subs = store.load('submissions.json')
    learner = next((l for l in roster['learners'] if l['id'] == learner_id and not l.get('_example')), None)
    if not learner:
        raise ApiError(404, "learner not found")
    prog = roster['programs'][learner['program']]
    done = [a for a in live(subs['assignments'])
            if a['learner_id'] == learner_id and a['status'] == 'complete' and a.get('badge_index') == badge_index]
    if len(done) < prog['cases_per_badge']:
        raise ApiError(400, f"only {len(done)}/{prog['cases_per_badge']} complete for badge {badge_index}")
    already = {b['badge_index'] for b in learner.get('badges_earned', [])}
    if badge_index in already:
        raise ApiError(409, f"badge {badge_index} already awarded")
    learner.setdefault('badges_earned', []).append({
        "badge_index": badge_index, "awarded_on": today(), "awarded_by": awarded_by or "facilitator",
        "cases": [a['case_id'] for a in done],
    })
    store.save('roster.json', roster)


# --------------------------------------------------------- student portal --
def do_student_login(store, learner_id, passcode):
    roster = store.load('roster.json')
    learner = next((l for l in live(roster['learners']) if l['id'] == learner_id), None)
    if not learner or not learner.get('passcode') or learner['passcode'] != (passcode or '').strip():
        raise ApiError(401, "wrong learner or passcode")
    if learner['status'] != 'active':
        raise ApiError(403, f"{learner['display_name']}'s account is {learner['status']}, not active -- ask your guide")
    return learner


def build_student_state(store, learner_id):
    """The live student portal's whole-page state -- deliberately just the slice
    of build_state() this one learner is allowed to see: their own record, their
    own assignments (feedback included), their own badge progress. No roster,
    no other learner's data, ever."""
    full = build_state(store)
    learner = next((l for l in full['learners'] if l['id'] == learner_id), None)
    if not learner:
        raise ApiError(404, f"learner {learner_id} not found")
    my_assignments = [a for a in full['assignments'] if a['learner_id'] == learner_id]
    my_badges = next((b for b in full['badges'] if b['id'] == learner_id), None)
    try:
        suggestions = suggest_cases(store, learner_id)
    except ApiError:
        suggestions = []
    return {
        "today": full['today'], "learner": learner, "assignments": my_assignments, "badges": my_badges,
        "interest_clusters": full['interest_clusters'], "curriculum_branches": full['curriculum_branches'],
        "suggestions": suggestions,
    }


def build_class_dashboard(store):
    """PLAN.md-style aggregate the guide asked for: what the class as a whole is
    into, what's working, what's not -- to help match students to cases, not a
    per-learner drill-down (that's the Learners tab). Every number here is
    derived live from roster.json + submissions.json + cases_index.json, same
    as build_state(), never a second cached copy."""
    roster = store.load('roster.json')
    subs = store.load('submissions.json')
    cases_idx = store.load('cases_index.json')
    domains_doc = store.load('domains.json')
    tree_doc = store.load('curriculum_tree.json')

    learners = live(roster['learners'])
    active = [l for l in learners if l['status'] == 'active']
    cases_by_id = {c['id']: c for c in cases_idx.get('cases', [])}
    branch_by_id = {b['id']: b for b in tree_doc.get('branches', [])}
    cluster_by_id = {c['id']: c for c in domains_doc.get('clusters', [])}
    domain_by_name = {d['name']: d for d in domains_doc.get('domains', [])}

    # Topics being considered -- current_branch on each learner's self-assessment.
    topic_counts = {}
    for l in active:
        sa = l.get('self_assessment')
        b = sa and sa.get('current_branch')
        if not b:
            continue
        entry = topic_counts.setdefault(b, {"branch_id": b, "branch": branch_by_id.get(b, {}).get('branch', b),
                                             "learners": []})
        entry['learners'].append(l['display_name'])
    topics = sorted(topic_counts.values(), key=lambda t: -len(t['learners']))

    # Careers of interest -- each learner's interest cluster ids -> that cluster's
    # domains -> each domain's named careers[] (domains.json), same taxonomy
    # suggest_cases() already uses, no new one invented here.
    career_counts = {}
    for l in active:
        sa = l.get('self_assessment')
        if not sa or not sa.get('interests'):
            continue
        cluster_names = {cluster_by_id[i]['name'] for i in sa['interests'] if i in cluster_by_id}
        seen_titles = set()
        for dom in domains_doc.get('domains', []):
            if dom.get('cluster') not in cluster_names:
                continue
            for career in (dom.get('careers') or []):
                title = career.get('title')
                if not title or title in seen_titles:
                    continue
                seen_titles.add(title)
                entry = career_counts.setdefault(title, {"title": title, "learners": []})
                entry['learners'].append(l['display_name'])
    careers = sorted(career_counts.values(), key=lambda c: -len(c['learners']))[:15]

    # Strength / difficulty -- reviewed submissions grouped by the domains the
    # case touches (cases_index.json domains_touched), split on outcome. A
    # domain with many 'accepted' outcomes and few 'revise'/'not-accepted' ones
    # is a class strength; the reverse is a difficulty.
    domain_stats = {}
    for s in live(subs['submissions']):
        if not s.get('outcome'):
            continue
        case = cases_by_id.get(s['case_id'])
        touched = (case or {}).get('domains_touched') or []
        for d in touched:
            entry = domain_stats.setdefault(d, {"domain": d, "accepted": 0, "revise": 0, "not_accepted": 0})
            if s['outcome'] == 'accepted':
                entry['accepted'] += 1
            elif s['outcome'] == 'revise':
                entry['revise'] += 1
            elif s['outcome'] == 'not-accepted':
                entry['not_accepted'] += 1
    scored = []
    for d in domain_stats.values():
        total = d['accepted'] + d['revise'] + d['not_accepted']
        d['total'] = total
        d['accept_rate'] = round(100 * d['accepted'] / total) if total else None
        scored.append(d)
    strengths = sorted([d for d in scored if d['total'] >= 1], key=lambda d: (-d['accept_rate'], -d['total']))[:8]
    difficulties = sorted([d for d in scored if d['total'] >= 1], key=lambda d: (d['accept_rate'], -d['total']))[:8]

    # Learners with no self-assessment / no active work at all -- a guide can't
    # match a case to a Hero it has nothing on file about.
    no_self_assessment = [l['display_name'] for l in active if not l.get('self_assessment')]
    queue = compute_queue(roster, subs)
    needs_resubmission = [q for q in queue if q['kind'] == 'NEEDS RESUBMISSION']
    overdue = [q for q in queue if q['kind'] in ('OVERDUE', 'STALE')]

    return {
        "learner_count": len(active), "topics": topics, "careers": careers,
        "strengths": strengths, "difficulties": difficulties,
        "no_self_assessment": no_self_assessment,
        "needs_resubmission": needs_resubmission, "overdue": overdue,
    }


# ------------------------------------------------------------- uploads -----
def parse_multipart(body, content_type):
    m = re.search(r'boundary=(?:"([^"]+)"|([^;]+))', content_type or '')
    if not m:
        raise ApiError(400, "missing multipart boundary")
    boundary = (m.group(1) or m.group(2)).strip()
    delim = b'--' + boundary.encode()
    fields, files = {}, []
    for part in body.split(delim):
        part = part.strip(b'\r\n')
        if not part or part == b'--':
            continue
        if b'\r\n\r\n' not in part:
            continue
        head, data = part.split(b'\r\n\r\n', 1)
        data = data[:-2] if data.endswith(b'\r\n') else data
        headers = head.decode('utf-8', 'replace')
        nm = re.search(r'name="([^"]+)"', headers)
        if not nm:
            continue
        name = nm.group(1)
        fn = re.search(r'filename="([^"]*)"', headers)
        if fn and fn.group(1):
            files.append((name, fn.group(1), data))
        else:
            fields[name] = data.decode('utf-8', 'replace')
    return fields, files


def do_upload(store, fields, files):
    if not files:
        raise ApiError(400, "no file in upload")
    _, filename, data = files[0]
    learner_id = fields.get('learner_id') or 'unknown'
    case_id = fields.get('case_id') or 'unknown'
    safe_name = re.sub(r'[^A-Za-z0-9 ._-]', '_', filename) or 'upload.bin'
    rel_path = f"student_work/{learner_id}/{case_id}/submitted/{safe_name}"
    store.write_submitted_file(rel_path, learner_id, case_id, data)
    return rel_path


CSV_TEMPLATE = (
    "display_name,program,cohort,status,id,goals\n"
    "Avery N.,MS-Adventure,2026-fall-adventure,active,,build confidence with ratios\n"
    "Jordan P.,Launchpad,2026-fall-lp,active,,explore engineering careers\n"
)


# ---------------------------------------------------- weekly class cases ---
# A deliberately separate, lighter-weight lane from the roster/assignment/
# submission machinery above: one shared link per case, a walk-up student
# types their name and goes through the case, no pre-registered learner id
# or passcode. Built for a live, facilitator-run weekly session with a small
# group (2-8 students) discussed together afterward -- not the self-directed,
# multi-week C1-C7 research-capstone flow the rest of this file supports.
def get_case_brief(case_id):
    """Public info for the /class/<case_id> landing page: title, the
    dilemma's framing, and its published Interactive.html filename if one
    exists. Reads cases_index.json directly off disk (bundled, read-only
    content in both local and hosted modes -- see store docstrings) rather
    than through store.load(), since this page has to work before any store
    is even relevant (it's unauthenticated)."""
    idx_path = os.path.join(os.path.dirname(_CASES_DIR), 'readmodel', 'cases_index.json')
    with open(idx_path, encoding='utf-8') as f:
        idx = json.load(f)
    case = next((c for c in idx['cases'] if c['id'] == case_id and c['status'] in ('published', 'legacy')), None)
    if not case:
        raise ApiError(404, f"case {case_id} not found or not published")
    filename, exists = _case_interactive_info(case_id, case['title'])
    return {
        "id": case['id'], "title": case['title'], "primary_metric": case.get('primary_metric'),
        "options": case.get('options', {}),
        "interactive_path": f"/cases/{case_id}/published/{filename}" if exists else None,
    }


def _save_class_file(store, case_id, sid, student_name, kind, file_tuple, default_name):
    """file_tuple is (filename, bytes) or None. kind ('pdf'/'photo') just
    keeps the two uploads from colliding in student_work/... paths."""
    if not file_tuple:
        return None
    filename, data = file_tuple
    safe_name = re.sub(r'[^A-Za-z0-9 ._-]', '_', filename) or default_name
    path = f"class_work/{case_id}/{sid}__{kind}__{safe_name}"
    store.write_submitted_file(path, f"class:{slugify(student_name)}", case_id, data)
    return path


def do_class_submit(store, case_id, group_label, student_name, answer_text, photo_file, pdf_file=None):
    """photo_file/pdf_file are each (filename, bytes) or None. pdf_file is the
    expected main artifact -- the case's own "Submit" toolbar button packages
    the student's filled-in notebook into a print-to-PDF document -- but
    nothing here hard-requires it: a device where print-to-PDF misbehaves
    mid-class shouldn't block a student from submitting *something*. Looks
    the case up first so a bad/typo'd case_id in a hand-typed link fails
    clearly instead of writing an orphaned submission."""
    case = get_case_brief(case_id)  # raises ApiError(404) if unknown
    student_name = (student_name or "").strip()
    if not student_name:
        raise ApiError(400, "name is required")
    answer_text = (answer_text or "").strip()
    if not answer_text and not photo_file and not pdf_file:
        raise ApiError(400, "submit your PDF, a photo, a note, or some combination")
    sid = f"class__{case_id}__{slugify(student_name) or 'student'}__{datetime.datetime.now().strftime('%Y%m%dT%H%M%S%f')}"
    pdf_path = _save_class_file(store, case_id, sid, student_name, 'pdf', pdf_file, 'submission.pdf')
    photo_path = _save_class_file(store, case_id, sid, student_name, 'photo', photo_file, 'photo.jpg')
    store.add_class_submission({
        "id": sid, "case_id": case_id, "group_label": (group_label or case['title']).strip(),
        "student_name": student_name, "answer_text": answer_text or None,
        "pdf_path": pdf_path, "photo_path": photo_path,
    })
    return sid


def do_list_class_submissions(store, case_id=None):
    return store.list_class_submissions(case_id)


def do_review_class_submission(store, submission_id, review_note, reviewed_by):
    store.review_class_submission(submission_id, review_note, reviewed_by)


def do_set_submission_assessment(store, submission_id, assessment):
    """A persisted strengths/opportunities note per submission -- distinct
    from review_note/reviewed_on, which just track "a guide looked at this."
    This is meant for the actual read of the work (what's well understood,
    where the gaps are), written once (by a guide, or pasted in from a
    Claude conversation that read the exported bundle) and then visible on
    the review page from then on, not re-derived every time."""
    assessment = (assessment or "").strip()
    if not assessment:
        raise ApiError(400, "assessment text is required")
    store.set_submission_assessment(submission_id, assessment)


def do_delete_class_submission(store, submission_id):
    store.delete_class_submission(submission_id)


_WEEKLY_DEBRIEF_KEY = "weekly_debrief"


def do_get_weekly_debrief(store):
    """{label, url} for the current week's debrief-prep page, or None if
    nothing has been set yet. Stored as one JSON string under a single
    settings key -- see get_setting()/set_setting() on each store."""
    raw = store.get_setting(_WEEKLY_DEBRIEF_KEY)
    return json.loads(raw) if raw else None


def do_set_weekly_debrief(store, label, url):
    label, url = (label or "").strip(), (url or "").strip()
    if not url:
        raise ApiError(400, "a link is required")
    if not (url.startswith("http://") or url.startswith("https://")):
        raise ApiError(400, "link must start with http:// or https://")
    store.set_setting(_WEEKLY_DEBRIEF_KEY, json.dumps({"label": label or "This week's debrief", "url": url}))


_WEEKLY_CASES_KEY = "weekly_cases"


def do_get_weekly_cases(store):
    """Ordered list of case_ids the guide has marked as 'this week's set'.
    A case on this list shows up on /class-review with its own debrief
    section whether or not any student has submitted to it yet -- a
    zero-submission case still needs to be walked through live, and before
    this it was simply invisible on the page (indistinguishable from
    broken)."""
    raw = store.get_setting(_WEEKLY_CASES_KEY)
    return json.loads(raw) if raw else []


def do_set_weekly_cases(store, raw_text):
    """raw_text is freeform, comma- or newline-separated -- a guide can type
    either the case_id (the slug from its /class/<id> link) or the plain
    title; both resolve against cases_index.json. Raises on the first token
    that matches neither, naming it, rather than silently dropping it."""
    tokens = [t.strip() for t in re.split(r'[,\n]+', raw_text or '') if t.strip()]
    idx_path = os.path.join(os.path.dirname(_CASES_DIR), 'readmodel', 'cases_index.json')
    with open(idx_path, encoding='utf-8') as f:
        idx = json.load(f)
    live = [c for c in idx['cases'] if c['status'] in ('published', 'legacy')]
    by_id = {c['id'] for c in live}
    by_title_slug = {slugify(c['title']): c['id'] for c in live}
    case_ids = []
    for t in tokens:
        cid = t if t in by_id else by_title_slug.get(slugify(t))
        if not cid:
            raise ApiError(400, f"case not found: {t!r}")
        if cid not in case_ids:
            case_ids.append(cid)
    store.set_setting(_WEEKLY_CASES_KEY, json.dumps(case_ids))
    return case_ids


def get_case_facilitator_brief(case_id):
    """Facilitator-only cheat sheet for a live class debrief: the actual
    dilemma, both options, each side's real argument, the margin, and the
    deliverable list -- read straight off the case's own case.json. Unlike
    get_case_brief() (which backs the public, unauthenticated /class/<id>
    page), this surfaces the same balance/answer-key content the
    Facilitator Guide docx carries, so it must only ever be called from the
    passcode-gated /class-review page. Returns None if case.json is
    missing (a bad/typo'd case_id in the weekly-cases list)."""
    case_path = os.path.join(_CASES_DIR, case_id, 'case.json')
    if not os.path.isfile(case_path):
        return None
    with open(case_path, encoding='utf-8') as f:
        case = json.load(f)
    balance = case.get('balance') or {}
    deliverables = [
        {"id": d.get("id"), "text": d.get("text")}
        for d in (case.get('deliverables') or []) if d.get("text")
    ]
    return {
        "id": case_id,
        "title": case.get('title', case_id),
        "protagonist": case.get('protagonist'),
        "primary_metric": case.get('primary_metric'),
        "options": case.get('options') or {},
        "argument_a": balance.get('argument_a'),
        "argument_b": balance.get('argument_b'),
        "margin_pct": balance.get('margin_pct'),
        "deliverables": deliverables,
        "figures": _extract_case_figures(case_id, case.get('title', case_id)),
    }


_FIGURE_RE = re.compile(r'<figure\b.*?</figure>', re.DOTALL | re.IGNORECASE)


def _extract_case_figures(case_id, title):
    """Pulls the real <figure>...</figure> diagrams/photos straight out of
    the case's own published Interactive.html -- the same enrichment pass
    that added story glossaries to the corpus also added labeled SVG
    diagrams and sourced photos inside <figure>/<figcaption> blocks, one per
    visual concept. Returning the raw markup (not a description of it) is
    what actually answers "we're also visual learners": the guide sees the
    identical diagram a student sees, not a text summary of one. Capped at
    6 so one very visual case can't blow out the whole review page; trusted
    project content, never user-supplied, so no escaping is needed."""
    filename, exists = _case_interactive_info(case_id, title)
    if not exists:
        return []
    path = os.path.join(_CASES_DIR, case_id, 'published', filename)
    with open(path, encoding='utf-8') as f:
        html_src = f.read()
    return _FIGURE_RE.findall(html_src)[:6]


def build_class_review_view(store, case_id_filter=None):
    """Assembles everything /class-review needs in one place, so the two
    servers (admin_web/app.py, admin_server.py) share this instead of each
    re-deriving it and risking drift. Sections cover the union of: this
    week's case list (do_get_weekly_cases, shown even with 0 submissions)
    and any case_id that actually has submissions -- so an old case that
    fell off the weekly list is still reachable, never silently hidden."""
    rows = do_list_class_submissions(store, case_id_filter)
    weekly_cases = do_get_weekly_cases(store)
    if case_id_filter:
        ordered_case_ids = [case_id_filter]
    else:
        ordered_case_ids = list(weekly_cases)
        extra = sorted(
            {r['case_id'] for r in rows if r['case_id'] not in ordered_case_ids},
            key=lambda cid: max(r['submitted_on'] or '' for r in rows if r['case_id'] == cid),
            reverse=True,
        )
        ordered_case_ids += extra
    case_titles, case_briefs, case_open_paths = {}, {}, {}
    for cid in ordered_case_ids:
        try:
            brief_public = get_case_brief(cid)
            case_titles[cid] = brief_public['title']
            case_open_paths[cid] = brief_public['interactive_path']
        except ApiError:
            pass
        brief = get_case_facilitator_brief(cid)
        if brief:
            case_briefs[cid] = brief
    return {
        "rows": rows,
        "ordered_case_ids": ordered_case_ids,
        "weekly_cases": weekly_cases,
        "case_titles": case_titles,
        "case_briefs": case_briefs,
        "case_open_paths": case_open_paths,
        "weekly_debrief": do_get_weekly_debrief(store),
    }


def _extract_pdf_text(pdf_bytes):
    """Best-effort text extraction from a submitted PDF. The "Submit" button
    produces these via the browser's own print-to-PDF on the student's typed
    Working Notebook, so the text layer is normally real and selectable, not
    a scanned image -- but a student's own screenshots/handwriting pasted
    into the notebook, or a device whose print-to-PDF behaves oddly, can
    still yield a PDF with little or no extractable text. Never raises: a
    bad/unusual PDF degrades to an empty string with a note, so one broken
    submission can't take down the whole class's export."""
    try:
        import pypdf
        reader = pypdf.PdfReader(io.BytesIO(pdf_bytes))
        pages = [(p.extract_text() or "").strip() for p in reader.pages]
        text = "\n\n".join(p for p in pages if p)
        return text or "(PDF has no extractable text -- likely a scanned image or photo; open the PDF directly to read it.)"
    except Exception as e:
        return f"(Could not read this PDF automatically: {type(e).__name__}. Open it directly to read it.)"


def do_export_case_debrief_bundle(store, case_id):
    """One plain-text bundle of every submission for a case: real extracted
    PDF text plus any typed answer/note, per student -- built so a guide can
    download it once and hand it to a reader (human or Claude) instead of
    opening submissions one at a time. Never touches review status; this is
    read-only, same spirit as do_list_class_submissions."""
    case = get_case_brief(case_id)
    rows = store.list_class_submissions(case_id)
    lines = [f"# {case['title']} — submission bundle for debrief prep",
             f"# {len(rows)} submission(s), exported {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
             ""]
    for r in sorted(rows, key=lambda r: r['submitted_on'] or ''):
        lines.append(f"## {r['student_name']}  ({r['submitted_on'] or 'no timestamp'})")
        if r.get('pdf_path'):
            pdf_bytes = store.get_submitted_file(r['pdf_path'])
            lines.append(_extract_pdf_text(pdf_bytes) if pdf_bytes else
                         "(PDF was recorded but the file itself is missing from storage.)")
        else:
            lines.append("(No PDF submitted.)")
        if r.get('answer_text'):
            lines.append(f"\n**Their own typed note/answer:** {r['answer_text']}")
        if r.get('reviewed_on'):
            lines.append(f"\n_Already reviewed by {r.get('reviewed_by') or 'guide'}: {r.get('review_note') or ''}_")
        lines.append("\n---\n")
    return "\n".join(lines)
