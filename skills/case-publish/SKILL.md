---
name: case-publish
description: "Package a QA-passed math case study into the student-facing packet and update the coverage read-model. Use when the user says \"publish the case\", \"ship it\", \"build the packet\", \"make the docx for the Fermenter case\", \"generate the student handout\", \"push the case to Drive\", \"update the coverage matrix\", or after case-qa returns a PASS verdict with 0 BLOCKERs. Produces cases/<id>/published/ containing a .docx case study, an optional .xlsx data workbook when the case has tabular appendix data, and a facilitator guide; then appends the case to readmodel/cases_index.json and updates covered_by[]/n in readmodel/standards_spine.json for every skill the case closes; then OFFERS to upload the packet to Google Drive. Refuses to run on any case that is not PASS with a matching QA hash. Both the read-model write and the Drive upload are explicit human confirm steps, never automatic."
---

# case-publish — packet + coverage promotion

Stage five, and the only skill that writes the read-model. Everything upstream drafts; this is
where a human promotes. Per house doctrine the source of record is frozen and nothing enters it
without an explicit sign-off — so this skill **asks twice**: once before mutating
`readmodel/`, once before touching Google Drive.

## The gate — check it first, refuse loudly

```bash
cd "$PROJECT" && python3 - <<'PY'
import json,hashlib,sys
CID="fermenter"
c=json.load(open(f'cases/{CID}/case.json'))
q=c.get('qa') or {}
md=open(f'cases/{CID}/case.md','rb').read()
h=hashlib.sha256(md).hexdigest()
fail=[]
if q.get('state')!="TIER2_PASS":        fail.append(f"qa.state is {q.get('state')!r}, must be 'TIER2_PASS' — "
                                                    "Tier 1 alone (mechanical/structural) is NOT enough to "
                                                    "publish; case-readiness's own ladder requires all six "
                                                    "Tier 2 probes recorded with 0 FAIL first. A case that is "
                                                    "internally consistent can still contain fabricated or "
                                                    "stale real-world data — Tier 1 cannot see that, only "
                                                    "Tier 2 (P1-P6) can.")
if q.get('verdict')!="PASS":            fail.append(f"qa.verdict is {q.get('verdict')!r}, must be 'PASS'")
if (q.get('blockers_open') or 0) != 0:  fail.append(f"{q.get('blockers_open')} BLOCKER(s) still open")
if q.get('case_md_sha256') != h:        fail.append("QA is STALE: case.md changed since the QA run "
                                                    f"(qa hash {str(q.get('case_md_sha256'))[:12]}…, now {h[:12]}…)")
if not c.get('new_coverage'):           fail.append("new_coverage[] empty — nothing to promote")
print("GATE FAIL:" if fail else "GATE OPEN"); [print(" -",f) for f in fail]
sys.exit(1 if fail else 0)
PY
```

**Why this changed (2026-08-04):** all 10 legacy-conversion cases in this project's first wave reached
`published` on a `TIER1_PASS`-only QA state — the gate above used to check the generic `qa.verdict`
field, which a case-readiness run sets to `"PASS"` the moment Tier 1 clears, well before Tier 2 ever
runs. Tier 1 is purely mechanical: it proves a case is *internally consistent*, not that its
real-world claims are *true*. Two of the four cases fact-checked in a later QA pass turned out to
have fabricated or stale real-world data (a wrong clinical trial's mortality table cited under the
real trial's name; a still-active athlete's career stats frozen at a partial, incomplete season) —
Tier 1 was clean on both. **Never gate `case-publish` on Tier 1 alone again.** If a case-readiness run
genuinely cannot reach `TIER2_PASS` (e.g. P5 has no `sensitivity_model.py`, or P6 has no web-connected
subagent available), that is a real, nameable reason to hold the case at `TIER1_PASS`/`PUBLISHED`-pending,
not a reason to weaken this gate.

If the gate fails, **stop and report**. Do not build a packet "so it's ready". A packet for an
unpublishable case will be sent to a student by someone who did not read the caveat.

Open GAPs are allowed through only if `QA_REPORT.md` records an explicit human waiver for each.
If any GAP lacks a waiver, ask before continuing.

---

## 1. Build the packet

Output to `cases/<id>/published/`:

```
published/
├── <Title> — Case Study.docx        student-facing
├── <Title> — Data.xlsx              optional; only when tabular appendix data exists
├── <Title> — Facilitator Guide.docx facilitator-only
└── MANIFEST.json                    what was built, from which hash, when
```

### 1a. The `.docx` case study

**Read `/sessions/<session>/mnt/.claude/skills/docx/SKILL.md` first** and follow it — the
footguns there are real. The essentials for this packet:

- Build with the `docx` npm package (preinstalled; do not `npm install`).
- **US Letter:** `page: { size: { width: 12240, height: 15840 } }`. The default is A4.
- **Tables need dual widths:** `columnWidths` on the table AND `width` on every cell, both
  `WidthType.DXA`. Percentages break in Google Docs, which is where these get read.
- **Table shading:** `ShadingType.CLEAR`, never `SOLID`.
- **Lists:** a `numbering` config with `LevelFormat.BULLET`. Never a literal `•`.
- Never `\n` — one `Paragraph` per line. `PageBreak` goes inside a `Paragraph`.

Document structure, in order — it mirrors `case.md` exactly, because the docx is the student's
only artifact:

1. Title block (`Case Study: <Title>` / `MS | Math | Case Study | <year> | <studio>`)
2. Overview
3. Background (appendix cross-references intact)
4. Dilemma — the `You are …` / `A.) … OR` / `B.) …` block, kept tight
5. Challenges 1–5, verbatim boilerplate + the authored section 3
6. Appendices A…, each with its tables reproduced in-document; external links as real hyperlinks
7. `Modeling Assumptions` block if the case has one — **keep it visibly labeled**, do not fold it
   into a data table
8. Sources appendix
9. The final `"How To…" Math Questions To Research` appendix

**Strip the `<!-- FACILITATOR ONLY -->` section.** Anything after that marker in `case.md` —
the balance arguments, the trap — must not reach the student docx. Check for it explicitly:
shipping the answer key inside the case is the single worst failure this skill can produce.

Verify by rendering and looking at it:

```bash
python scripts/office/soffice.py --headless --convert-to pdf "published/<Title> — Case Study.docx"
pdftoppm -jpeg -r 100 "<Title> — Case Study.pdf" page && ls page-*.jpg
```

Then Read the images. Check: tables not clipped, the Dilemma readable at a glance, no stray
`{{`, no facilitator content.

### 1b. The `.xlsx` data workbook — only when it earns its place

Build one when the case has appendix data a student would realistically want to compute over:
a price list, a schedule, a spec-comparison table, a time series, a route table. Skip it for a
case whose appendices are maps and prose — an empty workbook is clutter.

**Read the `xlsx` skill** at `/sessions/<session>/mnt/.claude/skills/xlsx/SKILL.md`. Essentials:

- `openpyxl`, preinstalled. Professional font throughout (Arial).
- One sheet per appendix table, named for the appendix: `Appendix C — Spec Sheets`.
- A `README` sheet first: what the workbook is, which case, which appendix each sheet maps to,
  and the source citation for each table.
- **Give the student the data, not the answer.** Ship raw values and a clearly-marked empty
  work area. Never pre-compute the comparison the case asks them to produce — that is the
  assignment.
- Cite each table's source in a cell adjacent to it, matching the `[S<n>]` id from `case.json`.
- If you do include any formula (e.g. a units-conversion helper in the work area), you must run
  `python scripts/recalc.py <file>` and get a clean `status: success`.

### 1c. The facilitator guide

Render `cases/<id>/FACILITATOR.md` to `.docx`, adding a publish-time run-of-show:

- The two arguments and the margin (now a real number).
- The five Socratic questions.
- **The trap.**
- The SPEC §6 sensitivity note if present, at the top, boxed.
- A short "what a strong defense sounds like" paragraph — not an answer key; a description of
  reasoning quality, because the case has no single right answer.
- The skills the case exercises, so the facilitator can name them in debrief.

### 1d. The interactive HTML (MCS-37/MCS-39) — build from the shared shell

`case-readiness` Tier 1 (`T1-18`, `T1-19`) already gates on `published/*.html` existing, fresh,
leak-free, and glossary-complete — but building it from scratch per case is exactly what made
Cold Chain's the only one that exists. Start from `templates/interactive_shell.html`, not a blank
file; the contract for filling it in (including a verified starter glossary you can reuse
verbatim) is `templates/INTERACTIVE_HTML_CONTRACT.md`. This is authored before `case-publish`
runs — the same as the docx/xlsx — not generated by this skill; `case-publish` just confirms it's
present, fresh, and gate-clean before including it in the manifest below.

### 1e. `MANIFEST.json`

```json
{"case_id":"fermenter","built_on":"2026-07-31","case_md_sha256":"a1b2…",
 "qa_report":"cases/fermenter/QA_REPORT.md","qa_verdict":"PASS","waived_gaps":[],
 "files":[{"name":"Fermenter — Case Study.docx","bytes":48211,"audience":"student"},
          {"name":"Fermenter - Interactive.html","bytes":51230,"audience":"student"}],
 "drive":{"pushed":false,"folder_id":null,"urls":[]}}
```

---

## 2. Promote to the read-model — ask first

**Stop and ask the user to confirm** before this step, showing exactly what will change:

```
About to promote 'Fermenter' into the read-model:
  cases_index.json   + 1 case (status: published)
  standards_spine.json
      cases[]        + "Fermenter"   (27 → 28)
      covered_by[]   + "Fermenter" on 11 skills
      n              +1 on those 11
      uncovered      100 → 93   (7 skills close: geometry-how-to-find-the-surface-area-of-a-cylinder, …)
      thin_1_2        80 → 84
  gap_queue.json     regenerated from the updated spine
Snapshot will be written to readmodel/_snapshots/ first. Proceed? (yes/no)
```

Then run it. Snapshot before write, single script, idempotent:

```bash
cd "$PROJECT" && python3 - <<'PY'
import json,shutil,os,datetime
CID="fermenter"
ts=datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
os.makedirs('readmodel/_snapshots',exist_ok=True)
for f in ('standards_spine.json','cases_index.json','gap_queue.json'):
    shutil.copy2(f'readmodel/{f}', f'readmodel/_snapshots/{f.replace(".json","")}.{ts}.json')

c=json.load(open(f'cases/{CID}/case.json')); TITLE=c['title']
sp=json.load(open('readmodel/standards_spine.json'))

if TITLE in sp['cases']:
    print(f"IDEMPOTENT STOP: '{TITLE}' already in spine cases[]. Nothing written."); raise SystemExit(0)
sp['cases'].append(TITLE)

claimed=set(c['standards']); touched=0
for dom in sp['domains']:
    for g in dom['groups']:
        for s in g['skills']:
            if s['id'] in claimed and TITLE not in s['covered_by']:
                s['covered_by'].append(TITLE); s['n']=len(s['covered_by']); touched+=1
allsk=[s for dom in sp['domains'] for g in dom['groups'] for s in g['skills']]
sp['totals']={"skills":len(allsk),"cases":len(sp['cases']),
              "uncovered":sum(1 for s in allsk if s['n']==0),
              "thin_1_2":sum(1 for s in allsk if s['n'] in (1,2))}
json.dump(sp,open('readmodel/standards_spine.json','w'),indent=1,ensure_ascii=False)

# gap_queue regenerated from the spine so the two can never disagree
gq=[]
for dom in sp['domains']:
    for g in dom['groups']:
        # n_gap counts THIN skills (n <= 2), matching the seeded gap_queue.json convention
        gaps=[{"label":s['label'],"n":s['n']} for s in g['skills'] if s['n']<=2]
        if gaps: gq.append({"domain":dom['domain'],"group":g['group'],
                            "n_gap":len(gaps),"n_total":len(g['skills']),"skills":gaps})
gq.sort(key=lambda x:-x['n_gap'])
json.dump(gq,open('readmodel/gap_queue.json','w'),indent=1,ensure_ascii=False)

idx=json.load(open('readmodel/cases_index.json'))
idx['cases']=[x for x in idx['cases'] if x['id']!=c['id']]
idx['cases'].append({
  "id":c['id'],"title":TITLE,"status":"published","source":"pipeline","tier":c['tier'],
  "band":c.get('band',[]),"studio":c.get('studio'),"primary_metric":c['primary_metric'],
  "options":c['options'],"margin_pct":c['margin_pct'],"standards_count":len(c['standards']),
  "domains_touched":sorted({dom['domain'] for dom in sp['domains'] for g in dom['groups']
                            for s in g['skills'] if s['id'] in claimed}),
  "new_coverage_count":len(c['new_coverage']),"authored_on":c.get('authored_on'),
  "published_on":datetime.date.today().isoformat(),"qa_verdict":"PASS",
  "paths":{"case_md":f"cases/{c['id']}/case.md","case_json":f"cases/{c['id']}/case.json",
           "published_dir":f"cases/{c['id']}/published/","drive_url":None},
  "notes":""})
json.dump(idx,open('readmodel/cases_index.json','w'),indent=2,ensure_ascii=False)

c['status']="published"; c['published_on']=datetime.date.today().isoformat()
json.dump(c,open(f'cases/{CID}/case.json','w'),indent=2,ensure_ascii=False)
print(f"promoted '{TITLE}': {touched} skill rows updated; totals -> {sp['totals']}; snapshot ts={ts}")
PY
```

Guarantees this script gives you, and you must preserve if you edit it:

- **Snapshot before write.** Recovery is `cp readmodel/_snapshots/<file>.<ts>.json readmodel/<file>.json`.
- **Idempotent.** Re-running does nothing rather than double-counting `n`.
- **`n` is recomputed from `len(covered_by)`**, never incremented blindly. The list is the truth.
- **`gap_queue.json` is derived, never hand-edited.** It is regenerated from the spine every
  promotion so the two cannot drift.
- **Title is the join key.** `standards_spine.json cases[]`, `covered_by[]` entries and
  `cases_index.json.title` must be the same string, character for character.

Verify after:

```bash
cd "$PROJECT" && python3 -c "
import json;sp=json.load(open('readmodel/standards_spine.json'))
a=[s for d in sp['domains'] for g in d['groups'] for s in g['skills']]
print(sp['totals']); print('n==len(covered_by) everywhere:', all(s['n']==len(s['covered_by']) for s in a))
print('cases[] unique:', len(sp['cases'])==len(set(sp['cases'])))"
```

---

## 3. Google Drive — offer, never assume

The user has a Google Drive MCP connected. Its tools are deferred; load them first:

```
ToolSearch  query: "select:mcp__7b221fd7-b7a0-4223-93e1-329e59ca4cc0__create_file,mcp__7b221fd7-b7a0-4223-93e1-329e59ca4cc0__search_files"
```

Then **ask**:

> Packet built and coverage promoted. Push these 3 files to Google Drive? (yes/no)
> `Fermenter — Case Study.docx` · `Fermenter — Data.xlsx` · `Fermenter — Facilitator Guide.docx`
> Target folder: `Math Builder / Published / Fermenter` — or tell me a different one.

On yes: locate or create the destination with `search_files`, upload with `create_file`, then
record the resulting URLs in `MANIFEST.json` `drive.urls[]` and in `cases_index.json`
`paths.drive_url`. On no: say the packet is on disk and can be pushed later; write
`drive.pushed: false`.

**Never upload without the confirm**, and flag the facilitator guide explicitly if the target
folder is shared with students — it contains the trap and both arguments.

## 4. Report

Files built with sizes · coverage delta (`uncovered 100 → 93`, naming the skills closed) ·
snapshot timestamp · Drive status · next step:
`Run case-track to assign <Title> to a learner or cohort.`

## Never

- Never run on a case that is not `PASS` with a matching hash. A stale hash means the case was
  edited after QA and QA no longer describes it.
- Never write the read-model without the confirm prompt and without a snapshot.
- Never mark a skill covered that the case does not genuinely exercise. `covered_by` is what
  every future gap query reads; a false entry silently hides a real hole forever.
- Never ship facilitator content, the trap, or the balance arguments in the student docx.
- Never pre-compute the student's answer inside the xlsx.
- Never upload to Drive without an explicit yes.
- Never hand-edit `gap_queue.json` — regenerate it.
