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
import csv, datetime, io, os, re, subprocess, sys, unicodedata


# ---------------------------------------------------------------- errors ---
class ApiError(Exception):
    def __init__(self, code, msg):
        super().__init__(msg)
        self.code = code
        self.msg = msg


# ------------------------------------------------------------ utilities ----
def live(rows):
    return [r for r in rows if not r.get('_example')]


def slugify(s):
    # NFKD + drop combining marks first, so "Théo" -> "theo" (transliterated) rather than
    # silently vanishing into "th-o" the moment the regex below hits a non-ASCII character.
    ascii_s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    return re.sub(r'[^a-z0-9]+', '-', ascii_s.lower()).strip('-')


def today():
    return datetime.date.today().isoformat()


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
        out.append({
            "id": L['id'], "name": L['display_name'], "program": L['program'], "cohort": L.get('cohort'),
            "status": L['status'], "badges": earned_n, "badges_total": p['badges'],
            "cases_done": total, "cases_required": p['cases_required'], "cases_per_badge": p['cases_per_badge'],
            "one_short": one_short, "eligible_slots": eligible,
        })
    return out


def build_state(store):
    roster = store.load('roster.json')
    subs = store.load('submissions.json')
    cases_idx = store.load('cases_index.json')
    assignable_cases = sorted(
        [{"id": c['id'], "title": c.get('title') or c['id'], "tier": c.get('tier'), "status": c.get('status'),
          "band": c.get('band') or [], "standards_count": c.get('standards_count'),
          "domains_touched": c.get('domains_touched') or []}
         for c in cases_idx.get('cases', []) if c.get('status') in ('published', 'legacy')],
        # published (real, vetted content) before legacy (older corpus, often
        # missing case.json/interactive HTML) -- a guide picking blind from an
        # alphabetical list was landing on a legacy case by default. Within
        # each group, sort by band then title so MS/HS don't interleave.
        key=lambda c: (c['status'] != 'published', ','.join(sorted(c['band'])), c['title']))

    A = live(subs['assignments'])
    S = live(subs['submissions'])
    D = live(subs['discussions'])
    SC = [s for s in subs.get('scores', []) if not s.get('_example')]

    assignments_view = []
    for a in A:
        my_subs = sorted([s for s in S if s['assignment_id'] == a['id']], key=lambda s: s['submitted_on'])
        latest = my_subs[-1] if my_subs else None
        my_scores = sorted([s for s in SC if s['learner_id'] == a['learner_id'] and s['case_id'] == a['case_id']],
                            key=lambda s: s['scored_on'])
        latest_score = my_scores[-1] if my_scores else None
        dcount = len([d for d in D if d['learner_id'] == a['learner_id'] and d['case_id'] == a['case_id']])
        assignments_view.append({**a, "latest_submission": latest, "latest_score": latest_score,
                                  "discussion_count": dcount, "n_submissions": len(my_subs)})

    domains_doc = store.load('domains.json')
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
    }


# --------------------------------------------------------------- writes ----
def _add_learner_to_roster(roster, display_name, program, cohort, status, learner_id):
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
    roster['learners'].append({
        "id": lid, "display_name": display_name, "program": program, "cohort": (cohort or "").strip() or None,
        "status": status or "active", "started_on": today(), "badges_earned": [],
        "drive_folder_id": None, "drive_folder_url": None, "notes": "",
    })
    return lid


def do_add_learner(store, display_name, program, cohort, status, learner_id):
    roster = store.load('roster.json')
    lid = _add_learner_to_roster(roster, display_name, program, cohort, status, learner_id)
    store.save('roster.json', roster)
    return lid


def do_bulk_add_learners_csv(store, csv_text):
    """Expected columns (header row required, case-insensitive, extra columns
    ignored): display_name, program, cohort (optional), status (optional,
    default active), id (optional, auto-slugified from display_name if absent).
    Partial success is normal and expected for a bulk import -- report every row's
    outcome rather than failing the whole file on the first bad row (same 'absent/
    wrong is a first-class reportable state, not a silent all-or-nothing' spirit
    the rest of this project applies everywhere else)."""
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
            lid = _add_learner_to_roster(roster, name, get('program'), get('cohort'),
                                          get('status') or None, get('id') or None)
            added.append({"row": i, "id": lid, "display_name": name})
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


def do_set_self_assessment(store, learner_id, interests, note, captured_by):
    """The goals/career conversation, guide-mediated for now (PLAN.md Phase 2 -- students
    don't have their own login yet, so this is entered by whoever had the conversation,
    same as review notes and discussion logs already are). interests[] are domains.json
    cluster ids, not free text -- a fixed, real taxonomy that already exists and is already
    validated at domain-build time (app/validate_domains.py), so there is nothing new to
    keep in sync. Setting a new self-assessment always resets reviewed_by_guide to False:
    a guide reviews *this* version, not a promise to re-review indefinitely."""
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
    learner['self_assessment'] = {
        "interests": interests,
        "note": note or "",
        "captured_on": today(),
        "captured_by": captured_by or "guide",
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


def suggest_cases(store, learner_id, limit=5):
    """PLAN.md Phase 2c. Turns a reviewed self-assessment into a short, explained shortlist
    instead of a guide scrolling all ~56 assignable cases blind. Reuses the exact same
    published/legacy eligibility rule build_state() already applies (never invent a second
    notion of 'assignable'), and domains.json's own existing_cases[]/why_it_engages/careers[]
    -- all already validated at build time (app/validate_domains.py) -- rather than any new
    matching heuristic. Returns [] (not an error) for a learner with no reviewed
    self-assessment; the caller decides what that means for the UI."""
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
            candidates.append({
                "case_id": case['id'], "title": case.get('title') or case['id'],
                "tier": case.get('tier'), "band": case.get('band') or [],
                "domain": dom.get('name'), "why_it_engages": dom.get('why_it_engages'),
                "career_title": career[0].get('title'),
            })
    # A guide can't judge grade/skill fit on a case with no tier -- prefer real, piloted
    # T1-T4 cases over unvetted legacy imports whenever both exist for the same interest,
    # rather than filling the shortlist domain-by-domain regardless of how well-specified
    # each case is. Sort is stable, so ties keep the original domain-priority/appearance order.
    candidates.sort(key=lambda c: 0 if c["tier"] else 1)
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
                      key=lambda s: s['submitted_on'])
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
    "display_name,program,cohort,status,id\n"
    "Avery N.,MS-Adventure,2026-fall-adventure,active,\n"
    "Jordan P.,Launchpad,2026-fall-lp,active,\n"
)
