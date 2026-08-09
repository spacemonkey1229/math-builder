---
name: case-track
description: "Run the student side of the math case-study program: assign a case to a Hero or a whole cohort, record a submission, mark discussion participation (2x required per case), and compute badge progress (MS Adventure = 4 badges x 5 cases; Launchpad = 3 badges x 10 cases). Use when the user says \"assign Fermenter to Avery\", \"assign this case to the fall cohort\", \"log a submission\", \"mark discussion participation\", \"who's behind\", \"what needs review\", \"badge progress\", \"who's one case short\", \"show me the exception queue\", \"what needs my attention today\", or asks about a learner's standing. Operates on readmodel/roster.json and readmodel/submissions.json. The default view is an EXCEPTION QUEUE — overdue assignments, submissions awaiting review, learners one case short of a badge — not a dashboard. NEVER auto-grades and never awards a badge: it tracks state and flags what needs human judgment."
---

# case-track — assignments, submissions, badges, and the exception queue

Stage six, and the only skill that touches student data. It records state and computes what is
derivable from it. It has no opinion about the quality of a Hero's work, and it never forms one.

> House doctrine: **the home screen is an exception queue.** Not a dashboard, not a database.
> What needs judgment today. Default output of this skill is the queue, always.

## Data

| File | Written by | Contents |
|---|---|---|
| `readmodel/roster.json` | this skill only | `programs{}` (badge structure), `learners[]` (incl. each learner's `drive_folder_id`/`drive_folder_url` — Roadmap C3, see **Drive intake** below) |
| `readmodel/submissions.json` | this skill only | `assignments[]`, `submissions[]`, `discussions[]` |
| `readmodel/cases_index.json` | `case-publish` | the assignable catalogue. **Read-only here.** |

Read each file's `_schema` block before writing to it — the field semantics are documented there
and they are the contract. Records with `"_example": true` are seed data for the app to render;
exclude them from every count unless the user asks to include them.

**Nothing in `submissions.json` is computed on write.** Overdue, badge progress and the queue are
all derived at read time. That way a change to the rules never leaves stale numbers behind.

---

## The state machine

```
assigned ──submit──▶ submitted ──human review──▶ reviewed ──2 discussions + confirm──▶ complete
    │                                                                                     │
    └────────────────────────── withdrawn ◀───────────────────────────────────────────────┘
```

- `submitted` → `reviewed` requires a human `outcome` (`accepted` / `revise` / `not-accepted`).
  This skill records the human's word; it never decides it.
- `reviewed` → `complete` requires `outcome == "accepted"` **and** `discussion_count >= 2`
  (SPEC Challenge 5) **and** an explicit confirm from the facilitator.
- **Only `complete` cases count toward a badge.**
- Resubmission: add a new `submissions[]` record with `__subN`; never overwrite the prior one.

---

## Operations

### Assign

To one learner, or to a cohort. Before writing, check:
1. The case exists in `cases_index.json` and its `status` is `published` or `legacy`.
   Refuse `concept` / `draft` / `researched` / `qa` — that case has not passed the gate.
2. The learner is `active`.
3. No open (`assigned`/`submitted`/`reviewed`) assignment already exists for that learner+case.
   A duplicate assignment is almost always a mistake; report it and ask.
4. The learner has not already completed that case.

Then append to `assignments[]` with `id = "<learner_id>__<case_id>__<assigned_on>"`,
a `due_on` (ask if not given — an assignment with `due_on: null` can never be flagged OVERDUE,
only STALE), and a `badge_index` if the facilitator specified one.

### Record a submission

Append to `submissions[]`. Capture the Challenge artifacts as they map to SPEC §1.5 — the
Challenge-1 resource link, the Challenge-2 pitch link with its word count and whether it carries
an original visual, which Challenge-3 deliverable ids are present, the Challenge-4 appendix link.

**Unknown is not zero.** If the facilitator did not say whether the pitch has a visual, write
`null`, not `false`. The queue reports `null` as *not recorded* and asks; it never treats it as a
failure. Set the assignment `status` to `submitted`.

The word count and deliverable list are **flags for the human, not a grade**. Report
"pitch is 212 words — Challenge 2 asks for 250+" and stop there. Do not reject, do not score.

### Drive intake — detect a submission instead of waiting on dictation (Roadmap C3)

The path above (`source: "facilitator-dictated"`) requires a human to read the Hero's actual
posts and tell case-track the Challenge links directly. This operation is the alternative: a Hero
drops their packet into a Drive folder, and case-track finds it. It is a **detection** shortcut,
not a review shortcut — it still ends at the same explicit human confirm before anything is
written, and it never sets `reviewed_on`/`outcome` itself (MCS-40). A file arriving in Drive is
evidence something was submitted, not evidence it was any good.

**Folder convention:** one folder per learner, subfoldered per case —
`Math Builder / Submissions / <learner display_name> / <case_id>/`. This mirrors `case-publish`'s
own `Math Builder / Published / <Case Title>` convention (`skills/case-publish/SKILL.md` §3) so
the whole project uses one Drive layout, not two.

**Tools** — same connected MCP server `case-publish` already uses for its outbound push, used here
for read/download instead. Load before use:

```
ToolSearch  query: "select:mcp__7b221fd7-b7a0-4223-93e1-329e59ca4cc0__search_files,mcp__7b221fd7-b7a0-4223-93e1-329e59ca4cc0__list_recent_files,mcp__7b221fd7-b7a0-4223-93e1-329e59ca4cc0__download_file_content,mcp__7b221fd7-b7a0-4223-93e1-329e59ca4cc0__get_file_metadata"
```

**Procedure:**

1. **Locate or create the learner's folder.** If `roster.json` already has `drive_folder_id` for
   this learner, use it. If not, `search_files` for `Math Builder / Submissions / <display_name>`;
   if it doesn't exist, **ask before creating it** (same confirm bar as case-publish's Drive push):
   *"No Drive submissions folder exists yet for Avery N. — create `Math Builder / Submissions /
   Avery N.`?"* On yes, record the new `drive_folder_id`/`drive_folder_url` in `roster.json`
   (snapshot first, MCS-22). On no, stop — dictated intake still works without this.
2. **List what's there.** `list_recent_files` (or `search_files`) scoped to the case's
   subfolder. Compare each file's Drive id against every `drive_artifacts.files[].drive_file_id`
   already recorded for that learner+case in `submissions.json` — a file whose id isn't already
   recorded is new.
3. **Report what's new, don't write yet.** *"Found 3 new files in Avery N.'s `fermenter/` folder:
   `Fermenter - Pitch.docx`, `Fermenter - Appendix.pdf`, `Fermenter - Workbook.xlsx`. Record this
   as a submission?"* This is the confirm gate — identical in spirit to case-publish's two-confirm
   step, applied here because this skill is writing a new `submissions[]` record, same as the
   dictated path already does.
4. **On yes:** `download_file_content` each matched file to
   `student_work/<learner_id>/<case_id>/submitted/<original filename>` (create the directory if
   needed) so a local copy exists — **Drive is the intake channel, never the artifact's only
   copy**; `submission-score --file` and every other downstream tool expect a local path. Append
   to `submissions[]` with `source: "drive-intake"` and `drive_artifacts: {folder_id, files: [...]}`
   populated with each file's id, name, `modified_time`, and the `local_path` it landed at. Set
   `artifacts.*` fields the same way the dictated path would if the file names or content make a
   Challenge mapping obvious (e.g. a file literally named `Challenge 1 - Resource Link.txt`); leave
   anything genuinely unclear as `null` — **do not guess a word count or infer a visual is present
   from a file existing.** Set the assignment `status` to `submitted`, same as dictated intake.
5. Everything after this point — review, `outcome`, discussion participation, completion — is
   identical to the dictated path. Drive intake only replaces step zero (a human noticing a
   submission exists); it does not shorten the human-judgment steps that follow.

**Honest status:** this mechanism is fully specified and uses a live, connected MCP server, but —
same caveat as `case-publish`'s own Drive push (ROADMAP.md D1) — **it has never been executed
against a real account.** No learner has a real `drive_folder_id` yet; no real submission has ever
been recorded this way. Treat the first real run as a first run, not a known-working path: check
that `search_files`/`list_recent_files` return what you expect before trusting the diff logic in
step 2.

### Mark discussion participation

Append to `discussions[]`: learner, case, date, `mode` (`live`, or `written-500` for the SPEC
absence substitute of 500 excellent words), who recorded it. Two records per learner per case
satisfy Challenge 5. Report the new count and whether the case is now completable.

### Complete a case

Only on explicit instruction, and only when review outcome is `accepted` and
`discussion_count >= 2`. Set `status: "complete"`. If `badge_index` is null, ask which badge slot
it fills — an unallocated completion is a real gap in the record, not a detail.

### Award a badge

**This skill does not award badges.** It reports eligibility. When a learner reaches
`cases_per_badge` complete cases in a slot, it says so and asks the facilitator to confirm; only
then does it append to `roster.json` `learners[].badges_earned[]`, recording `awarded_by` and the
case ids that satisfied it. Machines draft, humans finalize.

---

## Badge math

```
MS-Adventure : 4 badges × 5  cases = 20 cases
Launchpad    : 3 badges × 10 cases = 30 cases
```

Read the structure from `roster.json` `programs{}`, never hardcode it. A completed case counts
once, toward exactly one badge slot.

---

## The exception queue — the default output

```bash
cd "$PROJECT" && python3 - <<'PY'
import json, datetime, collections
TODAY = datetime.date.today()
R = json.load(open('readmodel/roster.json')); S = json.load(open('readmodel/submissions.json'))
def live(rows): return [r for r in rows if not r.get('_example')]
learners = {l['id']: l for l in live(R['learners']) if l['status']=='active'}
A = [a for a in live(S['assignments']) if a['learner_id'] in learners]
SUB = {s['assignment_id']: s for s in live(S['submissions'])}
DISC = collections.Counter((d['learner_id'], d['case_id']) for d in live(S['discussions']))
prog = R['programs']
def days(d): return (TODAY - datetime.date.fromisoformat(d)).days

Q = []   # (severity, kind, learner, detail, action)
for a in A:
    L = learners[a['learner_id']]; sub = SUB.get(a['id']); dc = DISC[(a['learner_id'], a['case_id'])]
    if a['status'] == 'assigned':
        if a.get('due_on') and days(a['due_on']) > 0:
            Q.append((1,'OVERDUE',L['display_name'],
                      f"{a['case_id']} due {a['due_on']} ({days(a['due_on'])}d ago), nothing submitted",
                      "check in with the Hero"))
        elif days(a['assigned_on']) > 21:
            Q.append((4,'STALE',L['display_name'],
                      f"{a['case_id']} assigned {days(a['assigned_on'])}d ago, no due date, no activity",
                      "set a due date or withdraw"))
    if a['status'] == 'submitted':
        d = days(sub['submitted_on']) if sub else 0
        Q.append((2,'AWAITING REVIEW',L['display_name'],
                  f"{a['case_id']} submitted {d}d ago", "read the pitch and set an outcome"))
        if sub:
            ar = sub.get('artifacts', {})
            wc = ar.get('challenge_2_word_count')
            if wc is not None and wc < 250:
                Q.append((3,'CHALLENGE 2 SHORT',L['display_name'],
                          f"{a['case_id']} pitch is {wc} words (Challenge 2 asks 250+)","facilitator judgment"))
            if ar.get('challenge_2_has_original_visual') is False:
                Q.append((3,'NO ORIGINAL VISUAL',L['display_name'],
                          f"{a['case_id']} pitch has no original visual display","facilitator judgment"))
            unknown = [k for k,v in ar.items() if v is None]
            if unknown:
                Q.append((5,'NOT RECORDED',L['display_name'],
                          f"{a['case_id']} artifacts unknown: {', '.join(unknown)}","record or confirm absent"))
    if a['status'] == 'reviewed' and dc < 2:
        Q.append((3,'DISCUSSION SHORT',L['display_name'],
                  f"{a['case_id']} reviewed, {dc}/2 discussions logged","schedule or log participation"))
    if a['status'] == 'reviewed' and dc >= 2:
        Q.append((2,'READY TO COMPLETE',L['display_name'],
                  f"{a['case_id']} reviewed + {dc} discussions","confirm complete and assign a badge slot"))

# badge progress + one-short
for lid, L in learners.items():
    p = prog[L['program']]; per = p['cases_per_badge']
    done = [a for a in A if a['learner_id']==lid and a['status']=='complete']
    byslot = collections.Counter(a.get('badge_index') for a in done)
    earned = {b['badge_index'] for b in L.get('badges_earned',[])}
    for slot, n in byslot.items():
        if slot is None:
            Q.append((3,'UNALLOCATED COMPLETION',L['display_name'],
                      f"{n} complete case(s) with no badge_index","assign them to a badge slot")); continue
        if n >= per and slot not in earned:
            Q.append((1,'BADGE ELIGIBLE',L['display_name'],
                      f"badge {slot}: {n}/{per} complete","CONFIRM AWARD — human act, never automatic"))
        elif n == per - 1:
            Q.append((2,'ONE CASE SHORT',L['display_name'],
                      f"badge {slot}: {n}/{per} complete","assign the last case"))
    if not [a for a in A if a['learner_id']==lid and a['status'] in ('assigned','submitted','reviewed')]:
        Q.append((3,'NO OPEN WORK',L['display_name'],"active learner with no open assignment","assign a case"))

names = {1:'ACT NOW',2:'NEEDS YOU',3:'CHECK',4:'DRIFTING',5:'MISSING DATA'}
print(f"EXCEPTION QUEUE — {TODAY}   ({len(Q)} items, {len(learners)} active learners)\n")
if not Q: print("  Nothing needs judgment today.")
for sev in sorted({q[0] for q in Q}):
    print(f"── {names[sev]} ──")
    for _,kind,who,detail,action in sorted([q for q in Q if q[0]==sev], key=lambda x:x[2]):
        print(f"  [{kind}] {who}: {detail}\n        → {action}")
    print()
PY
```

Severity ladder, and why each row exists:

| Sev | Kinds | Why it is in the queue |
|---|---|---|
| 1 ACT NOW | `OVERDUE`, `BADGE ELIGIBLE` | A Hero is stuck, or has earned something and is waiting on a human. |
| 2 NEEDS YOU | `AWAITING REVIEW`, `READY TO COMPLETE`, `ONE CASE SHORT` | Work is sitting on the facilitator's desk. |
| 3 CHECK | `DISCUSSION SHORT`, `CHALLENGE 2 SHORT`, `NO ORIGINAL VISUAL`, `UNALLOCATED COMPLETION`, `NO OPEN WORK` | A requirement is unmet or a record is incoherent. Judgment, not enforcement. |
| 4 DRIFTING | `STALE` | Quietly rotting. Nobody notices these without a queue. |
| 5 MISSING DATA | `NOT RECORDED` | Absent data is a first-class state — surfaced, never inferred. |

Only show a full roster table when the user explicitly asks for one ("show me everyone",
"badge progress for the cohort"). The default answer to "how are we doing" is the queue.

---

## Worked example

> **User:** assign the Fermenter case to the fall adventure cohort, due Nov 14

1. Look up `fermenter` in `cases_index.json` — `status: published`. Good. If it were `qa`,
   refuse: *"Fermenter has not passed the gate; run case-publish first."*
2. Select active learners with `cohort == "2026-fall-adventure"`. Report the count and the names
   before writing — a bulk assign is easy to aim at the wrong cohort.
3. Skip anyone with an open or completed Fermenter assignment, listing who and why.
4. Append one `assignments[]` row per learner, `due_on: "2026-11-14"`, `badge_index` asked for if
   not given.
5. Re-run the exception queue and report the delta: *"6 assigned. `NO OPEN WORK` cleared for 4
   learners. 1 `OVERDUE` remains: Jordan P. on `heist`, 3 days over."*

> **User:** Avery participated twice in the Catering discussion today

Append two `discussions[]` records (`mode: "live"`), report `2/2 — Challenge 5 satisfied`, and
because the Catering assignment is `reviewed` with `outcome: accepted`, surface it:
*"Catering is ready to complete. Confirm, and tell me which badge slot it fills."*

---

## Never

- **Never grade.** No score field exists in the schema, by design. Report facts — word count,
  artifacts present, discussion count — and hand the judgment to the facilitator.
- **Never auto-award a badge.** Report eligibility, ask, then record with `awarded_by`.
- **Never auto-complete** an assignment. `complete` is a human confirm.
- Never assign a case whose `cases_index.json` status is not `published` or `legacy`.
- Never overwrite a submission — resubmissions are new records; the prior one is retained.
- Never treat a `null` artifact field as a failure. `null` means not recorded; it goes to the
  MISSING DATA tier and gets asked about.
- Never write `cases_index.json`, `standards_spine.json` or `gap_queue.json`. Those belong to
  `case-publish`.
- Never delete a learner. Set `status: "alumni"` or `"paused"`.
- Never render a dashboard when the user asked how things are going. Render the queue.
- **Never let a Drive file's presence alone set `reviewed_on` or `outcome` (MCS-40).** Drive
  intake automates noticing a submission arrived, not judging it — a downloaded file still needs
  a human to read it and record an outcome, exactly like a dictated one.
- Never record a `drive-intake` submission without downloading a local copy first
  (`student_work/<learner>/<case>/submitted/`). Drive is the channel, not the copy of record.
- Never create a learner's Drive submissions folder without asking first — same confirm bar as
  `case-publish`'s Drive push.
