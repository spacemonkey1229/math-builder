---
name: case-qa
description: "Gate a math case study against the SPEC.md §7 Definition of Done and the §2 balance test before it can be published. Use when the user says \"QA the case\", \"run the gate\", \"is this case ready\", \"check the Fermenter case\", \"review the case study against the spec\", \"can we publish this\", or after case-research reports all placeholders closed. Runs a mechanical checklist — seven structural sections, verbatim Challenge boilerplate, no orphan appendices, final-appendix lines are verbatim spine labels, every number cited or declared an assumption, no load-bearing numbers in the Overview, difficulty tier matches the numeric load — plus the balance test (both options defensible, margin ≤ ~20% on the primary metric, both arguments written out). Emits a BLOCKER / GAP / POLISH verdict to cases/<id>/QA_REPORT.md. This skill CANNOT publish. It only gates, and every BLOCKER must be resolved before publish."
---

# case-qa — the gate

Stage four. The only skill in the pipeline whose output is a **verdict**. It gates and nothing
else: it does not fix, does not source, does not publish. If it finds problems it names them and
hands the case back.

> House doctrine: *The critique pass is not optional. BLOCKER/GAP/POLISH before any build begins.*
> Here it is before any publish begins. **Every BLOCKER must be resolved. No exceptions.**

## Verdict vocabulary

| Level | Definition | Effect |
|---|---|---|
| **BLOCKER** | Violates SPEC §7, §5 or §2. The case is not publishable and would damage the corpus or mislead a Hero. | `case-publish` refuses. Non-negotiable. |
| **GAP** | Something real is missing but the case still functions. A thin appendix, a dead external link with the data reproduced in-document, a facilitator guide missing one Socratic question. | Publishable only with an explicit human waiver recorded in the report. |
| **POLISH** | Quality, not correctness. Wording, a weak sensory detail, table formatting. | Never blocks. |

Verdict is `PASS` when `blockers == 0`. Otherwise `BLOCKED`.

## Inputs

`cases/<id>/case.md`, `cases/<id>/case.json`, `cases/<id>/LEARNING_GOALS.md`,
`SPEC.md`, `doctrine/CHALLENGE_BOILERPLATE.md`, `readmodel/standards_spine.json`.

---

## The mechanical pass — run the script

Everything below that can be checked by a machine, is. Run this first; then do the judgment pass
by hand. The script never rewrites the case.

```bash
cd "$PROJECT" && python3 - <<'PY'
import json,re,hashlib,unicodedata,sys
CID = "fermenter"                      # <- set this
md   = open(f'cases/{CID}/case.md').read()
c    = json.load(open(f'cases/{CID}/case.json'))
sp   = json.load(open('readmodel/standards_spine.json'))
bp   = open('doctrine/CHALLENGE_BOILERPLATE.md').read()
B, G, P = [], [], []

def norm(s):
    s = s.replace('“','"').replace('”','"').replace('‘',"'").replace('’',"'")
    return re.sub(r'\s+',' ', s).strip()

labels = {}       # label -> [ids]
by_id  = {}
for dom in sp['domains']:
    for g in dom['groups']:
        for s in g['skills']:
            by_id[s['id']] = s
            labels.setdefault(s['label'], []).append(s['id'])

# --- 1. structural sections -------------------------------------------------
for name, pat in [("Title block", r'Case Study:\s*\S'),
                  ("MS banner",   r'MS\s*\|\s*Math\s*\|\s*Case Study'),
                  ("Overview",    r'(?im)^#+\s*Overview'),
                  ("Background",  r'(?im)^#+\s*Background'),
                  ("Dilemma",     r'(?im)^#+\s*(The )?Dilemma'),
                  ("Challenges",  r'(?im)^#+\s*Challenges'),
                  ("Appendices",  r'(?im)^#+\s*Appendix\s+A')]:
    if not re.search(pat, md): B.append(f"SPEC §1 — missing section: {name}")

# --- 2. Overview: length + no load-bearing numbers --------------------------
ov = re.search(r'(?is)^#+\s*Overview\s*(.*?)(?=^#+\s)', md, re.M)
if ov:
    words = len(ov.group(1).split())
    if not 150 <= words <= 300: G.append(f"SPEC §1.2 — Overview is {words} words, spec says 150–300")
    nums = re.findall(r'(?<![\w$])\d[\d,]*\.?\d*\s*(?:%|lb|ft|in|mi|km|kg|bbl|gal|hr|hours|minutes|\$)?', ov.group(1))
    nums = [n.strip() for n in nums if n.strip()]
    if nums: B.append(f"SPEC §1.2 — Overview contains numerals {nums[:6]}; confirm none are load-bearing "
                      f"(a year or a staff count as texture is a POLISH note, a quantity a student could use is a BLOCKER)")

# --- 3. Dilemma is binary ---------------------------------------------------
dl = re.search(r'(?is)^#+\s*(?:The )?Dilemma\s*(.*?)(?=^#+\s)', md, re.M)
if dl:
    d = dl.group(1)
    if not re.search(r'(?m)^\s*A\.\)', d) or not re.search(r'(?m)^\s*B\.\)', d):
        B.append("SPEC §1.4 — Dilemma must use the A.) / B.) form")
    if re.search(r'(?m)^\s*C\.\)', d): B.append("SPEC §1.4 — Dilemma is not binary (found option C)")
    if not re.search(r'(?i)you are\s+\S', d): B.append("SPEC §1.4 — Dilemma must open 'You are <Protagonist>.'")
    for k in ("A","B"):
        opt = (c.get('options') or {}).get(k) or ""
        if opt:
            key = norm(opt).split()[:4]
            bgm = re.search(r'(?is)^#+\s*Background\s*(.*?)(?=^#+\s)', md, re.M)
            if bgm and not any(w.lower() in norm(bgm.group(1)).lower() for w in key if len(w)>4):
                G.append(f"SPEC §1.3 — Option {k} may not be named in Background; check its label appears there")

# --- 4. Challenge boilerplate, verbatim -------------------------------------
canon = re.search(r'## BEGIN CANONICAL BLOCK(.*?)## END CANONICAL BLOCK', bp, re.S).group(1)
canon = re.search(r'```(.*?)```', canon, re.S).group(1)
locked = {}
for n in (1,2,4,5):
    m = re.search(rf'(?ms)^{n}\.\)\s(.*?)(?=^\d\.\)|\Z)', canon)
    if m: locked[n] = norm(m.group(1))
ch = re.search(r'(?is)^#+\s*Challenges\s*(.*?)(?=^#+\s*Appendix|\Z)', md, re.M)
if not ch:
    B.append("SPEC §1.5 — Challenges section not found")
else:
    have = ch.group(1)
    for n, text in locked.items():
        m = re.search(rf'(?ms)^\s*{n}\.\)\s(.*?)(?=^\s*\d\.\)|\Z)', have)
        if not m:
            B.append(f"SPEC §1.5 — Challenge {n} missing")
        elif norm(m.group(1)) != text:
            got = norm(m.group(1))
            i = next((k for k in range(min(len(text),len(got))) if text[k]!=got[k]), min(len(text),len(got)))
            a, b = max(0,i-40), i+70          # window around the first divergence
            B.append(f"SPEC §1.5 — Challenge {n} is NOT verbatim boilerplate (diverges at char {i}).\n"
                     f"      expected: …{text[a:b]}…\n      found:    …{got[a:b]}…")
    if not re.search(r'(?ms)^\s*3\.\)', have): B.append("SPEC §1.5 — Challenge 3 (case-specific deliverables) missing")

# --- 5. appendices: lettered, referenced, no orphans ------------------------
apps = re.findall(r'(?im)^#+\s*Appendix\s+([A-Z])\s*[—\-–:]\s*(.+)$', md)
letters = [a for a,_ in apps]
if letters != sorted(letters):        G.append(f"Appendices out of order: {letters}")
if len(letters) != len(set(letters)): B.append(f"Duplicate appendix letters: {letters}")
body_wo_apps = re.split(r'(?im)^#+\s*Appendix\s+A\b', md)[0]
for L,title in apps:
    # the final "How To…" standards appendix is referenced by Challenge 1 by construction, not by letter
    if re.search(r'(?i)how\s*to', title): continue
    if not re.search(rf'(?i)APPENDI(?:X|CES)[^.\n]*\b{L}\b', body_wo_apps):
        B.append(f"SPEC §1.6 — Appendix {L} ({title.strip()}) is an ORPHAN: never referenced from Background or Challenges")

# --- 6. final appendix lines are verbatim spine labels ----------------------
fin = re.search(r'(?is)^#+\s*Appendix\s+[A-Z]\s*[—\-–:]\s*.{0,10}How To.*?$(.*)\Z', md, re.M)
if not fin:
    B.append('SPEC §1.7 — mandatory final appendix ("How To…" Math Questions To Research) missing')
else:
    lines = [norm(l)[2:].strip() for l in fin.group(1).splitlines() if l.strip().startswith(('- ','* '))]
    if not lines: B.append("SPEC §1.7 — final appendix has no skill lines")
    bad  = [l for l in lines if l not in labels]
    if bad: B.append(f"SPEC §1.7 — final-appendix lines are NOT verbatim spine labels: {bad}")
    claimed_labels = {by_id[i]['label'] for i in c.get('standards',[]) if i in by_id}
    miss = sorted(claimed_labels - set(lines)); extra = sorted(set(lines) - claimed_labels - set(bad))
    if miss:  G.append(f"standards[] claims skills absent from the final appendix: {miss}")
    if extra: G.append(f"final appendix lists skills absent from standards[]: {extra}")
    if not re.search(r'(?i)vocabulary', fin.group(1)) or not re.search(r'how to', fin.group(1), re.I):
        G.append("SPEC §1.7 — final appendix should be a two-part list (Vocabulary terms / \"How to…\" questions)")

# --- 7. every number cited or declared ---------------------------------------
left = re.findall(r'\{\{NEEDS_SOURCE:[^}]*\}\}', md)
if left: B.append(f"SPEC §5 — {len(left)} unresolved {{{{NEEDS_SOURCE}}}} placeholder(s) remain")
ma = re.search(r'(?is)^#+\s*Modeling Assumptions\s*(.*?)(?=^#+\s|\Z)', md, re.M)
ma_txt = ma.group(1) if ma else ""
src_ids = {s.get('id') for s in c.get('sources',[])}
marks   = set(re.findall(r'\[(S\d+)\]', md))
if marks - src_ids: B.append(f"SPEC §5 — citation markers with no sources[] row: {sorted(marks-src_ids)}")
if src_ids - marks: G.append(f"sources[] rows never cited in the document: {sorted(src_ids-marks)}")
for s in c.get('sources',[]):
    miss=[k for k in ("claim","value","org","title","url","accessed","confidence") if not s.get(k)]
    if miss: B.append(f"SPEC §5 — source {s.get('id')} incomplete, missing {miss}")
    if s.get('confidence') not in ("HIGH","MEDIUM","LOW"): B.append(f"source {s.get('id')} has no valid confidence grade")
if [s for s in c.get('sources',[]) if s.get('confidence')=='LOW']:
    G.append("LOW-confidence sources present — confirm none carries a constraint or a dilemma-flipping quantity")
if c.get('modeling_assumptions') and not ma:
    B.append("SPEC §5 — case.json declares modeling assumptions but case.md has no visible 'Modeling Assumptions' block")

# --- 8. balance test (SPEC §2) ----------------------------------------------
bal = c.get('balance') or {}
if not (bal.get('argument_a') or '').strip(): B.append("SPEC §2 — strongest quantitative argument for A not written")
if not (bal.get('argument_b') or '').strip(): B.append("SPEC §2 — strongest quantitative argument for B not written")
mp = c.get('margin_pct', bal.get('margin_pct'))
if mp is None:      B.append("SPEC §2 — margin_pct not recorded")
elif mp > 20:       B.append(f"SPEC §2 — UNBALANCED: margin is {mp}% on '{c.get('primary_metric')}' (cap ~20%). "
                             f"Retune a constraint. Do NOT fix this by hiding data.")
elif mp > 15:       G.append(f"margin {mp}% is inside the cap but wide; the discussion will be one-sided")
if not (c.get('primary_metric') or '').strip(): B.append("SPEC §2/§4 — primary_metric not stated")

# --- 9. standards binding (SPEC §4) -----------------------------------------
for k in ("id","title","tier","band","primary_metric","options","margin_pct","standards","new_coverage","sources"):
    if k not in c: B.append(f"SPEC §4 — case.json missing key: {k}")
for s in c.get('standards',[]):
    if s not in by_id: B.append(f"SPEC §4 — standards[] id not in spine: {s}")
for s in c.get('new_coverage',[]):
    if s not in c.get('standards',[]): B.append(f"new_coverage[] not a subset of standards[]: {s}")
    elif by_id.get(s,{}).get('n',0) != 0:
        B.append(f"new_coverage[] claims '{s}' but the spine shows n={by_id[s]['n']} — already covered")
if not c.get('new_coverage'): B.append("SPEC §7 — new_coverage[] is empty; the case closes no gap")

# --- 10. learning-goal integrity --------------------------------------------
mapped = {sk for d in c.get('deliverables',[]) for sk in d.get('skills',[])}
unmapped = [d['id'] for d in c.get('deliverables',[]) if not d.get('skills')]
unreach  = sorted(set(c.get('standards',[])) - mapped)
if unmapped: B.append(f"LEARNING GOAL — deliverables mapped to no skill: {unmapped}")
if unreach:
    lvl = B if set(unreach) & set(c.get('new_coverage',[])) else G
    lvl.append(f"LEARNING GOAL — skills no deliverable forces: {unreach}"
               + (" (includes new_coverage — this would falsely close a gap)" if lvl is B else ""))

# --- 11. tier vs numeric load (SPEC §3) -------------------------------------
tier = c.get('tier')
load = {"pct": bool(re.search(r'\d\s*%', md)), "ratio": bool(re.search(r'(?i)per\s+\w+', md)),
        "sci":  bool(re.search(r'\d\s*[x×]\s*10\^?\d|e[+-]\d\d', md)),
        "prob": bool(re.search(r'(?i)probabilit|likelihood|odds', md)),
        "assume": bool(ma_txt.strip())}
nvars = len(c.get('deliverables',[]))
if tier == "T4" and not load["assume"]:
    B.append("SPEC §3 — T4 requires at least one quantity the student must assume, stated and justified; "
             "no Modeling Assumptions block found")
if tier == "T1" and (load["sci"] or load["prob"] or nvars > 3):
    G.append("SPEC §3 — declared T1 but the numeric load looks T2+; re-tier")
if tier in ("T3","T4") and nvars <= 2 and not (load["sci"] or load["prob"]):
    G.append(f"SPEC §3 — declared {tier} but only {nvars} deliverables and no advanced operations; may be T2")
if tier not in ("T1","T2","T3","T4"): B.append("SPEC §3 — tier must be T1–T4")

# --- 12. facilitator guide + sensitivity ------------------------------------
import os
if not os.path.exists(f'cases/{CID}/FACILITATOR.md'):
    B.append("SPEC §7 — facilitator guide missing (both arguments + 5 Socratic questions + the trap)")
else:
    f = open(f'cases/{CID}/FACILITATOR.md').read()
    qs = len(re.findall(r'(?m)^\s*(?:\d+[.)]|[-*])\s.*\?', f))
    if qs < 5: G.append(f"facilitator guide has {qs} Socratic questions, spec asks for 5")
    if not re.search(r'(?i)trap', f): G.append("facilitator guide does not name 'the trap'")
if re.search(r'(?i)\b(death|dying|cancer|casualt|foreclos|evict|bankrupt|terminal|hospice|layoff)\w*', md) \
   and not c.get('sensitivity_note'):
    B.append("SPEC §6 — case touches illness/death/money stress/family hardship but has no one-line "
             "facilitator sensitivity note")

# --- report -----------------------------------------------------------------
print(f"case: {CID}   sha256(case.md)={hashlib.sha256(md.encode()).hexdigest()[:16]}")
for lvl,items in (("BLOCKER",B),("GAP",G),("POLISH",P)):
    print(f"\n=== {lvl} ({len(items)}) ===")
    for i in items: print(" •", i)
print(f"\nVERDICT: {'PASS' if not B else 'BLOCKED'}  ({len(B)} blockers, {len(G)} gaps)")
PY
```

Two script behaviours are intentional and must be resolved by hand, not suppressed:

- **Overview numerals** are raised as a BLOCKER for *confirmation*. A year, a staff count, or a
  street number used as texture downgrades to POLISH once you have read it and confirmed no
  student needs it. A quantity that could enter a calculation stays a BLOCKER. Write which it was
  in the report.
- **Option-named-in-Background** uses a fuzzy word match and will occasionally misfire. Read the
  Background and clear it or keep it deliberately.

---

## The judgment pass — what the script cannot check

Do these by hand, after the script, and write findings into the same report.

1. **Is the balance real?** `margin_pct ≤ 20` is arithmetic; *defensibility* is judgment. Read
   both arguments in `case.json`. If argument B is "B is cheaper but worse in every other way",
   the case is unbalanced regardless of the number — a Hero cannot defend it in front of peers.
   The Robotics Engineering exemplar is the standard: Route 1 beat Route 2 by **0.09%** and the
   student still had to defend the choice.
2. **Does the Overview stop at the instant of decision?** Any sentence that resolves, hints, or
   moralizes is a BLOCKER. So is opening with background.
3. **Are the deliverables artifacts or homework?** "A cost-per-barrel table" passes. "Calculate
   the cost per barrel" is a word problem wearing a case's clothes.
4. **Is the data honestly messy?** At T3+, if every appendix number is used, the case does not
   teach filtering. That is a GAP.
5. **Would a Hero need the math?** The test from SPEC §0: could a student pick a side and defend
   it persuasively **without doing the arithmetic**? If yes, the case has failed at its purpose —
   BLOCKER, and it needs a redesign, not a fix.
6. **Sensitivity read (SPEC §6).** Does the math require optimizing human death tolls as an
   abstract quantity? Prefer protection framings. If the case carries weight, confirm the
   one-line facilitator note exists and is actually useful.

---

## Write the report

`cases/<id>/QA_REPORT.md`:

```markdown
# QA Report — <Title>
**Case:** `<id>` · **Run:** 2026-07-31 · **Against:** SPEC.md v1.0
**case.md sha256:** `a1b2c3d4…`   ← case-publish refuses if the file changes after this
**VERDICT: BLOCKED** — 2 BLOCKER · 3 GAP · 4 POLISH

## SPEC §7 Definition of Done
| # | Check | Result | Note |
|---|---|---|---|
| 1 | All seven structural sections present and conformant | PASS | |
| 2 | Overview contains zero load-bearing numbers | PASS | "twelve employees" is texture, confirmed unused |
| 3 | Dilemma binary; both options named in Background | PASS | |
| 4 | Challenge sections 1, 2, 4, 5 verbatim boilerplate | **FAIL** | §2 sub-line b.) reworded — BLOCKER 1 |
| 5 | Every appendix referenced; no orphans | PASS | |
| 6 | Final appendix lines all verbatim spine labels | PASS | 11/11 matched |
| 7 | Balance test passed, margin recorded, both arguments written | PASS | 8.3% on $/bbl |
| 8 | Every number cited or declared an assumption | **FAIL** | Appendix D row 4 uncited — BLOCKER 2 |
| 9 | case.json validates; new_coverage[] non-empty | PASS | 7 new |
| 10 | Facilitator guide written | PASS | 5 questions + trap |

## BLOCKER (must be resolved before publish)
**B1 — Challenge 2 is not verbatim.** …what it says, what it must say, exact fix.
**B2 — …**

## GAP (publishable only with a recorded waiver)
**G1 — …** · waiver: <granted by / declined>

## POLISH
**P1 — …**

## Balance read
Primary metric: … · Margin: 8.3% · Argument A: … · Argument B: …
Judgment: both defensible / A is a trap / unbalanced because …

## Re-run required after fixes
Yes — the sha256 changes on any edit, which invalidates this report.
```

Then set in `case.json`:
`qa: {"verdict": "PASS"|"BLOCKED", "run_on": "<date>", "blockers_open": <n>, "gaps_open": <n>, "case_md_sha256": "<hash>"}`
and `status: "qa"`. **Nothing else in `case.json` may be modified by this skill.**

## Report back

Verdict line, the BLOCKER list verbatim, the report path, and the next step: either
`Fix the N blockers and re-run case-qa` or `Run case-publish on <id>.`

## Never

- **Never fix the case.** QA that edits its own subject cannot be trusted. Name the defect and
  the exact fix; let `case-write` or `case-research` apply it.
- Never publish, never touch `readmodel/`, never write `cases_index.json`.
- Never downgrade a BLOCKER to a GAP to get a case out the door. The margin cap, the verbatim
  boilerplate, the fabricated-number rule and the empty-`new_coverage` rule are absolute.
- Never mark PASS with a stale hash. Any edit after the run invalidates the report; re-run.
- Never accept "the number is plausible". SPEC §5: QA rejects plausible.
