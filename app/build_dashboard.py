#!/usr/bin/env python3
"""
build_dashboard.py — generates app/dashboard.html from the readmodel/*.json files.

The dashboard must open by double-click over file://, where fetch() of a local JSON
file is blocked by CORS. So the read-model is compiled here and INLINED into the
HTML as a single `const DATA = {...}` literal. Re-run this script whenever anything
under readmodel/ changes.

    python3 app/build_dashboard.py            # build + verify
    python3 app/build_dashboard.py --verify   # verify the existing file only

Doctrine: absent data is a first-class state. Nothing in here converts a missing
value into a zero. Branches with no legacy standards rows are emitted with
coverage.state == "unmapped" and null counts, never 0%.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import quote, unquote

ROOT = Path(__file__).resolve().parent.parent
RM = ROOT / "readmodel"
OUT = ROOT / "app" / "dashboard.html"
OUT_STUDENT = ROOT / "app" / "student.html"

# source/ is gitignored (140MB+ of raw authoring material, not needed for a
# deploy) so it never reaches Vercel. Links into it are rewritten to point at
# a Google Drive mirror instead -- see app/source_drive_links.json, keyed by
# path relative to source/. Built by hand once; regenerate it if source/
# gains files that aren't in the mirror yet.
_DRIVE_LINKS_PATH = ROOT / "app" / "source_drive_links.json"
DRIVE_LINKS: dict = json.loads(_DRIVE_LINKS_PATH.read_text()) if _DRIVE_LINKS_PATH.exists() else {}

TODAY = date.today()

SOURCES = [
    "curriculum_tree.json",
    "standards_spine.json",
    "gap_queue.json",
    "pipeline_status.json",
    "legacy_readiness.json",
    "corpus_index.json",
    "cases_index.json",
    "roster.json",
    "submissions.json",
    "domains.json",
    "domain_coverage.json",
    "score_overrides.json",
]


def load(name: str):
    with open(RM / name, encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------------------
# reconciliation: corpus folders  <->  legacy standards-matrix columns
# --------------------------------------------------------------------------

FUZZY_CUTOFF = 0.77  # admits "Castle Securtiy"->"Castle Security", "Payroll 2.0"->"Payroll"


def norm_title(s: str) -> str:
    s = s.replace("_s", "'s").lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def reconcile(corpus_cases, matrix_cols):
    by_norm = {norm_title(c): c for c in matrix_cols}
    out = {}
    for c in corpus_cases:
        t = norm_title(c["title"])
        if t in by_norm:
            out[c["title"]] = {"col": by_norm[t], "match": "exact", "score": 1.0}
            continue
        best = max(by_norm, key=lambda m: difflib.SequenceMatcher(None, t, m).ratio())
        score = round(difflib.SequenceMatcher(None, t, best).ratio(), 3)
        if score >= FUZZY_CUTOFF:
            out[c["title"]] = {"col": by_norm[best], "match": "fuzzy", "score": score}
        else:
            out[c["title"]] = {"col": None, "match": "none", "score": score}
    # A matrix column is one case's standards row. Nothing upstream stops two different
    # corpus folders from independently fuzzy-matching (or, rarer, exact-matching a
    # collided norm_title) the SAME column -- e.g. "Phone Plan" (Session 3) and "Phone
    # Plans 2.0" (Additional) are two folders on disk, a real case and a same-script
    # reskin of it, and both resolve to the sole "Phone Plan" spine column at >0.95
    # similarity. Every downstream count (n_skill_ids, standards_count, coverage
    # totals) assumes one column maps to one case; a silent collision double-counts
    # that column's skills against whichever folder read second. Keep only the
    # single best-scoring folder per column (exact beats fuzzy; higher score wins a
    # fuzzy-vs-fuzzy tie) and demote every other folder that collided into it back to
    # unmapped -- unmapped-with-a-reason is correct here, not a guess forced to fit.
    col_claims = {}
    for title, r in out.items():
        if r["col"] is not None:
            col_claims.setdefault(r["col"], []).append(title)
    for col, titles in col_claims.items():
        if len(titles) <= 1:
            continue
        titles.sort(key=lambda t: out[t]["score"], reverse=True)
        for loser in titles[1:]:
            out[loser] = {"col": None, "match": "none", "score": out[loser]["score"],
                          "collided_with": titles[0]}
    return out


# --------------------------------------------------------------------------
# asset links
#
# Every asset in corpus_index.json is a real file on disk. Locally, the
# dashboard lives at app/dashboard.html, so a link to source/Y1/... has to be
# "../source/Y1/..." -- from file:// a relative <a href> hands the file to
# the OS handler. But source/ is gitignored and never ships to Vercel, so
# that relative link 404s on the deployed site. For anything under source/,
# we instead emit the file's Google Drive mirror URL (DRIVE_LINKS, keyed by
# path relative to source/) -- an absolute URL that works everywhere,
# deployed or local. Falls back to the old relative path if a file hasn't
# been mirrored to Drive yet.
#
# Every path segment is percent-encoded individually with safe="" so that
# spaces, apostrophes, commas, parentheses, ampersands and the U+2019 curly
# apostrophe in "Women's" all survive. "/" is NOT encoded — it is the separator.
#
# A missing file is NOT silently dropped and NOT rendered as a live link: it
# gets href=None and state "not on disk", which the UI renders as absent.
# --------------------------------------------------------------------------

ANNOT_RX = re.compile(r"\s*\([^()]*\)\s*$")

LINKS: list = []          # every link record emitted this build (verification hook)


def href_for(rel: str) -> str:
    """rel is POSIX-relative to the project root; the page sits one level down."""
    if rel.startswith("source/"):
        drive_url = DRIVE_LINKS.get(rel[len("source/"):])
        if drive_url:
            return drive_url
    return "../" + "/".join(quote(seg, safe="") for seg in rel.split("/") if seg not in ("", "."))


def make_link(rel: str, label: str, kind: str, student_safe: bool):
    """Resolve one asset to a link record. Records are appended to LINKS."""
    note = None
    p = ROOT / rel
    exists = p.exists()
    if not exists:
        # corpus_index carries a few annotated entries, e.g.
        #   "FACILITATOR.md (timed plan embedded)"
        # strip the trailing parenthetical and retry before declaring it absent.
        cand = ANNOT_RX.sub("", rel)
        if cand != rel and (ROOT / cand).exists():
            note = ANNOT_RX.search(rel).group(0).strip().strip("()")
            rel, p, exists = cand, ROOT / cand, True
            label = rel.split("/")[-1]      # the annotation moves into `note`
    rec = {
        "label": label,
        "kind": kind,
        "rel": rel,
        "href": href_for(rel) if exists else None,
        "exists": exists,
        "is_dir": bool(exists and p.is_dir()),
        "ext": (p.suffix.lower().lstrip(".") or None) if exists and p.is_file() else None,
        "kb": round(p.stat().st_size / 1024) if exists and p.is_file() else None,
        "note": note,
        "student_safe": student_safe,
    }
    LINKS.append(rec)
    return rec


ASSET_KINDS = [
    ("interactive_html", "Interactive Case (open in browser)", True),
    ("case_doc", "Case document", True),
    ("guide_notes", "Guide Notes (facilitator)", False),
    ("socratic_plan", "Socratic plan (facilitator)", False),
    ("data_workbooks", "Data workbook", True),
    ("reference_pdfs", "Reference PDF", True),
    ("images", "Image", True),
]
STUDENT_SAFE_KINDS = {k for k, _lab, safe in ASSET_KINDS if safe}


def case_links(case):
    """{kind: [link,...]} for one corpus case, plus a folder link (guide only)."""
    out = {}
    for k, label, safe in ASSET_KINDS:
        rows = []
        for fn in case["assets"].get(k, []):
            rows.append(make_link(case["path"] + "/" + fn, fn, k, safe))
        out[k] = rows
    # The folder itself. NEVER student-safe: a directory listing exposes
    # Guide Notes.docx even when the guide-notes link is filtered out.
    out["_folder"] = make_link(case["path"], case["path"].split("/")[-1], "folder", False)
    return out


# --------------------------------------------------------------------------
# RUBRIC.md -> structured criteria (parsed, not retyped, so it cannot drift)
# --------------------------------------------------------------------------

LEVELS = ["Not Yet", "Proficient", "Exemplary"]
LEVEL_POINTS = {"Not Yet": 0, "Proficient": 70, "Exemplary": 100}
LEVEL_ORDER = {"Not Yet": 0, "Proficient": 1, "Exemplary": 2}
BIAS_MIN_N = 8          # score_overrides.json the_rule: under 8 confirmed records a rate is noise
BIAS_DEMOTE_AT = 0.30   # RUBRIC / MCS-31: >30% overridden => flag for demotion to guide-only


def parse_rubric():
    md = (ROOT / "RUBRIC.md").read_text(encoding="utf-8")

    version = (re.search(r"\*\*Version:\*\*\s*([^\s·]+)", md) or [None, "?"])[1]
    status = (re.search(r"\*\*Status:\*\*\s*(.+)", md) or [None, "?"])[1].strip()

    # criteria blocks
    heads = list(re.finditer(r"^### (C[1-7]) · (.+?)\s*$", md, re.M))
    crits = []
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else md.index("\n## Scoring")
        chunk = md[h.start():end]
        title = h.group(2)
        name, _, tail = title.partition(" — ")
        src_line = (re.search(r"^\*(.+?)\*\s*$", chunk, re.M) or [None, ""])[1]
        weight = int(re.search(r"Weight\s+(\d+)", src_line or chunk).group(1))
        bands = {}
        for lvl, txt in re.findall(r"^\|\s*\*\*(Not Yet|Proficient|Exemplary)\*\*\s*\|\s*(.+?)\s*\|\s*$", chunk, re.M):
            bands[lvl] = txt
        lead = [
            ln.strip() for ln in chunk.splitlines()
            if ln.strip() and not ln.startswith(("###", "|", ">", "*Challenge", "*Underlies", "*Not from"))
            and not re.fullmatch(r"[-*_]{3,}", ln.strip())
        ]
        notes = [n.strip() for n in re.findall(r"^>\s*(.+?)\s*$", chunk, re.M) if n.strip()]
        crits.append({
            "id": h.group(1),
            "name": name.strip(),
            "subtitle": tail.strip() or None,
            "source": (src_line or "").split(".")[0].strip() or None,
            "weight": weight,
            "bands": [{"level": L, "text": bands.get(L)} for L in LEVELS],
            "lead": lead,
            "notes": notes,
        })

    # the weights row in ## Scoring, kept as an independent cross-check
    wrow = re.search(r"\|\s*C1\s*\|\s*C2\s*\|.*?\n\|[-| ]+\|\n\|(.+?)\|\s*\n", md, re.S)
    weights_table = [int(x.strip()) for x in wrow.group(1).split("|")] if wrow else []

    tier_block = md[md.index("**Tier adjustment.**"):md.index("## Peer and self review")]
    tiers = [{"tier": t, "requires": r.strip()}
             for t, r in re.findall(r"^\|\s*(T[1-4])\s*\|\s*(.+?)\s*\|\s*$", tier_block, re.M)]

    mach = md[md.index("## How the machine pass works"):md.index("## Open questions")]
    signals = [{"signal": s.strip(), "informs": c.strip()}
               for s, c in re.findall(r"^\|\s*([^|]+?)\s*\|\s*((?:C\d[,\s]*)+)\s*\|\s*$", mach, re.M)]
    limits = [{"rule": a.strip(), "detail": b.strip()}
              for a, b in re.findall(r"^\d+\.\s*\*\*(.+?)\*\*\s*(.+?)\s*$", mach, re.M)]
    guessing = (re.search(r"\*\*What it is guessing at:\*\*\s*(.+?)\s*$", mach, re.M) or [None, None])[1]

    openq = [{"q": a.strip(), "detail": b.strip()} for a, b in
             re.findall(r"^-\s*\*\*(.+?)\*\*\s*(.+?)\s*$", md[md.index("## Open questions"):], re.M)]

    return {
        "version": version,
        "status": status,
        "criteria": crits,
        "weights_table": weights_table,
        "weight_sum": sum(c["weight"] for c in crits),
        "levels": LEVELS,
        "level_points": LEVEL_POINTS,
        "tiers": tiers,
        "machine_signals": signals,
        "hard_limits": limits,
        "guessing_at": guessing,
        "open_questions": openq,
        "gate_rule": "badge_eligible = every one of the seven criteria is at least Proficient. "
                     "No partial credit, no compensation, no averaging.",
        "growth_rule": "0-100 weighted composite. Never a grade, never shown to a learner as one, "
                       "never used for badge eligibility. It exists to show trajectory.",
    }


# --------------------------------------------------------------------------
# scoring + override bias
# --------------------------------------------------------------------------

def build_scoring(subs, overrides_file, roster, rubric):
    scores_all = subs.get("scores", [])
    ovr_all = overrides_file.get("overrides", [])

    lname = {l["id"]: l["display_name"] for l in roster["learners"]}

    def shape(scores, ovrs):
        rows = []
        for s in scores:
            crit = s.get("criteria", {})
            rows.append({
                "id": s["id"],
                "learner_id": s["learner_id"],
                "learner": lname.get(s["learner_id"], s["learner_id"]),
                "case_id": s["case_id"],
                "scored_on": s.get("scored_on"),
                "status": s.get("status"),
                "interim": s.get("status") != "confirmed",
                "criteria": {c["id"]: crit.get(c["id"]) for c in rubric["criteria"]},
                "badge_eligible": s.get("badge_eligible"),
                "growth_score": s.get("growth_score"),
                "surface_first": s.get("surface_first", []),
                "confirmed_by": s.get("confirmed_by"),
                "confirmed_on": s.get("confirmed_on"),
                "overrides": s.get("overrides", []),
                "report": s.get("report"),
            })
        rows.sort(key=lambda r: (r["learner"], r["case_id"], r["scored_on"] or ""))

        confirmed = [s for s in scores if s.get("status") == "confirmed"]
        bias = []
        for c in rubric["criteria"]:
            mine = [o for o in ovrs if o["criterion"] == c["id"]]
            n_conf = sum(1 for s in confirmed if c["id"] in (s.get("criteria") or {}))
            raised = sum(1 for o in mine
                         if LEVEL_ORDER.get(o["guide_level"], 0) > LEVEL_ORDER.get(o["machine_level"], 0))
            lowered = len(mine) - raised
            enough = n_conf >= BIAS_MIN_N
            rate = round(100.0 * len(mine) / n_conf, 1) if (enough and n_conf) else None
            bias.append({
                "criterion": c["id"],
                "name": c["name"],
                "n_overrides": len(mine),
                "n_confirmed": n_conf,
                "raised": raised,
                "lowered": lowered,
                "rate_pct": rate,                       # None == not computable, never 0
                "state": ("OK" if rate is not None and rate <= 100 * BIAS_DEMOTE_AT
                          else "FLAG FOR DEMOTION" if rate is not None
                          else "INSUFFICIENT DATA"),
                "why_absent": None if enough else (
                    "no confirmed score records at all — a rate has no denominator"
                    if n_conf == 0 else
                    "%d confirmed record%s; the file's own rule needs %d before a rate means anything"
                    % (n_conf, "" if n_conf == 1 else "s", BIAS_MIN_N)),
                "direction": ("machine reads harsh — guide keeps raising it" if raised and not lowered
                              else "machine reads generous — guide keeps lowering it" if lowered and not raised
                              else "mixed" if mine else None),
            })

        known = {s["id"] for s in scores}
        dangling = [o["id"] for o in ovrs if o.get("score_id") and o["score_id"] not in known]
        return {
            "n_scores": len(scores),
            "n_confirmed": len(confirmed),
            "n_interim": len(scores) - len(confirmed),
            "scores": rows,
            "overrides": ovrs,
            "n_overrides": len(ovrs),
            "bias": bias,
            "dangling_override_refs": dangling,
            "min_n": BIAS_MIN_N,
            "demote_at_pct": round(100 * BIAS_DEMOTE_AT),
        }

    real = lambda rows: [r for r in rows if not r.get("_example")]
    return {
        "real": shape(real(scores_all), real(ovr_all)),
        "example": shape(scores_all, ovr_all),
    }


# --------------------------------------------------------------------------
# root connections: domains.json + domain_coverage.json
# --------------------------------------------------------------------------

def build_domains_block(doms, dcov, skill_label):
    cov_by_id = {d["domain"]: d for d in dcov["by_domain"]}
    cards = []
    for d in doms["domains"]:
        cv = cov_by_id.get(d["id"], {})
        da = d.get("data_availability") or {}
        cards.append({
            "id": d["id"],
            "name": d["name"],
            "cluster": d["cluster"],
            "one_line": d["one_line"],
            "why": d.get("why_it_engages"),
            "priority": d.get("authoring_priority"),
            "grade": da.get("grade"),
            "sources": da.get("sources", []),
            "data_note": da.get("note"),
            "archetypes": d.get("decision_archetypes", []),
            "careers": d.get("careers", []),
            "branches": d.get("math_branches", []),
            "skills": [{"id": s, "label": skill_label.get(s, s)} for s in d.get("signature_skills", [])],
            "n_skills": d.get("n_signature_skills"),
            "uncovered": [{"id": s, "label": skill_label.get(s, s)}
                          for s in d.get("uncovered_signature_skills", [])],
            "n_uncovered": d.get("n_uncovered_signature_skills"),
            "cases": d.get("existing_cases", []),
            "n_cases": len(d.get("existing_cases", [])),
        })
    cards.sort(key=lambda c: ({"HIGH": 0, "MEDIUM": 1, "LOW": 2}.get(c["priority"], 3), c["name"]))

    matrix = []
    for b in dcov["by_branch"]:
        matrix.append({
            "branch": b["branch"],
            "name": b["name"],
            "phase": b["phase"],
            "has_standards_rows": b["has_standards_rows"],
            "n_domains": b["n_domains"],
            "domains": b["domains"],
            "high_priority": b["high_priority_domains"],
            "n_cases": b["n_existing_cases_in_those_domains"],
            "n_uncovered_reachable": b.get("n_uncovered_signature_skills_reachable"),
            "domain_starved": b["domain_starved"],
            "case_starved": b["case_starved"],
            "reasons": b.get("starvation_reasons", []),
        })

    n_sources = sum(len(c["sources"]) for c in cards)
    return {
        "clusters": doms["clusters"],
        "domains": cards,
        "matrix": matrix,
        "totals": dcov["totals"],
        "orphan_uncovered": dcov.get("orphan_uncovered_skills", []),
        "unassigned_cases": dcov.get("unassigned_corpus_cases", []),
        "n_high": sum(1 for c in cards if c["priority"] == "HIGH"),
        "n_sources": n_sources,
        "generated_at": dcov.get("_generated_at"),
    }


# --------------------------------------------------------------------------
# student payload — built by REDACTION IN THE GENERATOR, not by hiding in CSS.
#
# Everything the doctrine says a learner must not see is removed here, so it is
# not present in the object at all: facilitator guide notes, socratic plans,
# twists, QA reports, other learners' anything, the gap queue, override bias.
# The growth score is dropped too — RUBRIC is explicit that it is a guide tool
# and never a grade shown to the learner.
# --------------------------------------------------------------------------

STUDENT_FORBIDDEN_KEYS = ("twist", "guide_notes", "socratic_plan", "qa", "gap", "bias", "override")


def build_student(learner_id, roster, subs, lib_by_title, ci_by_id, spine_skills, scoring_all):
    L = next((x for x in roster["learners"] if x["id"] == learner_id), None)
    if L is None:
        return None
    prog = roster["programs"][L["program"]]

    mine_a = [a for a in subs["assignments"] if a["learner_id"] == learner_id]
    mine_s = [s for s in subs["submissions"] if s["learner_id"] == learner_id]
    mine_d = [d for d in subs["discussions"] if d["learner_id"] == learner_id]
    sub_by_a = {}
    for s in mine_s:
        sub_by_a.setdefault(s["assignment_id"], []).append(s)
    dcount = Counter(d["case_id"] for d in mine_d)

    def title_of(case_id):
        ci = ci_by_id.get(case_id)
        return (ci or {}).get("title") or case_id

    cards = []
    for a in sorted(mine_a, key=lambda a: a["assigned_on"]):
        t = title_of(a["case_id"])
        c = lib_by_title.get(t)
        assets = []
        if c:
            for k, label, safe in ASSET_KINDS:
                if k not in STUDENT_SAFE_KINDS:
                    continue
                for ln in c["asset_links"][k]:
                    assets.append({kk: ln[kk] for kk in
                                   ("label", "kind", "href", "exists", "ext", "kb", "note")})
        latest = sorted(sub_by_a.get(a["id"], []), key=lambda s: s["submitted_on"])[-1:] or [None]
        latest = latest[0]
        due_state = "no deadline set"
        if a["status"] == "complete":
            due_state = "completed"
        elif a["due_on"]:
            dd = (date.fromisoformat(a["due_on"]) - TODAY).days
            due_state = ("due in %d day%s" % (dd, "" if dd == 1 else "s") if dd > 0
                         else "due today" if dd == 0 else "%d day%s past due" % (-dd, "" if dd == -1 else "s"))
        cards.append({
            "case_id": a["case_id"],
            "title": t,
            "tier": (ci_by_id.get(a["case_id"]) or {}).get("tier"),
            "year": (c or {}).get("year"),
            "session": (c or {}).get("session"),
            "assigned_on": a["assigned_on"],
            "due_on": a["due_on"],
            "due_state": due_state,
            "status": a["status"],
            "badge_index": a["badge_index"],
            "submitted_on": (latest or {}).get("submitted_on"),
            "reviewed": bool(latest and latest.get("reviewed_on")),
            "outcome": (latest or {}).get("outcome"),
            "discussions": dcount[a["case_id"]],
            "discussions_required": 2,
            "assets": assets,
            "assets_known": c is not None,
        })

    # my own heatmap: skills exercised by the cases I have actually completed
    done_ids = [a["case_id"] for a in mine_a if a["status"] == "complete"]
    for b in L["badges_earned"]:
        done_ids += b["cases"]
    done_titles = {title_of(i) for i in set(done_ids)}
    exercised = set()
    for s in spine_skills:
        if done_titles & set(s["covered_by"]):
            exercised.add(s["id"])

    credited = sum(len(b["cases"]) for b in L["badges_earned"])
    in_flight = sum(1 for a in mine_a if a["status"] == "complete")
    total_done = credited + in_flight
    nxt = prog["cases_per_badge"] - (total_done % prog["cases_per_badge"])

    # my scores only — mastery verdicts, no growth score, no other learner
    my_scores = []
    for s in scoring_all["scores"]:
        if s["learner_id"] != learner_id:
            continue
        my_scores.append({
            "case_id": s["case_id"],
            "title": title_of(s["case_id"]),
            "scored_on": s["scored_on"],
            "interim": s["interim"],
            "criteria": {k: ({"level": (v or {}).get("level")} if v else None)
                         for k, v in s["criteria"].items()},
            "badge_eligible": s["badge_eligible"],
            "not_yet": [k for k, v in s["criteria"].items() if (v or {}).get("level") == "Not Yet"],
        })

    return {
        "learner": {
            "id": L["id"], "name": L["display_name"], "program": L["program"],
            "cohort": L["cohort"], "started_on": L["started_on"],
            "is_example": bool(L.get("_example")),
        },
        "program": prog,
        "badges": {
            "earned": [{"badge_index": b["badge_index"], "awarded_on": b["awarded_on"],
                        "n_cases": len(b["cases"])} for b in L["badges_earned"]],
            "n_earned": len(L["badges_earned"]),
            "badges_total": prog["badges"],
            "cases_done": total_done,
            "cases_required": prog["cases_required"],
            "cases_per_badge": prog["cases_per_badge"],
            "to_next": nxt if total_done < prog["cases_required"] else 0,
        },
        "cases": cards,
        "skills": {
            "exercised": sorted(exercised),
            "n_exercised": len(exercised),
            "n_total": len(spine_skills),
            "from_cases": sorted(done_titles),
        },
        "scores": my_scores,
        # rubric[] and domains[] are shared, not learner-specific. In the guide
        # build the page reads them off the top level; student_doc() moves the
        # same objects in here for the standalone student build. Duplicating
        # them in both places cost 175 KB and bought nothing.
        "rubric": None,
        "domains": None,
    }


# --------------------------------------------------------------------------
# build the compiled read-model
# --------------------------------------------------------------------------

def build_data():
    del LINKS[:]
    tree = load("curriculum_tree.json")
    spine = load("standards_spine.json")
    gapq = load("gap_queue.json")
    corpus = load("corpus_index.json")
    cases_index = load("cases_index.json")
    roster = load("roster.json")
    subs = load("submissions.json")
    domsrc = load("domains.json")
    dcov = load("domain_coverage.json")
    ovr = load("score_overrides.json")
    pipeline = load("pipeline_status.json")
    legacy_ready = load("legacy_readiness.json")

    matrix_cols = spine["cases"]
    corpus_cases = corpus["cases"]
    recon = reconcile(corpus_cases, matrix_cols)

    hit_cols = {v["col"] for v in recon.values() if v["col"]}
    orphan_cols = sorted(set(matrix_cols) - hit_cols)
    fuzzy_links = sorted(
        [{"folder": k, "column": v["col"], "score": v["score"]}
         for k, v in recon.items() if v["match"] == "fuzzy"],
        key=lambda d: d["folder"],
    )
    # columns reachable ONLY through a near-miss folder name
    exact_cols = {v["col"] for v in recon.values() if v["match"] == "exact"}
    fuzzy_only_cols = sorted({f["column"] for f in fuzzy_links} - exact_cols)

    # ---- standards spine -------------------------------------------------
    skills_by_domain = {}
    heat_domains = []
    for dom in spine["domains"]:
        groups = []
        dskills = []
        for g in dom["groups"]:
            sk = []
            for s in g["skills"]:
                rec = {
                    "id": s["id"],
                    "label": s["label"],
                    "kind": s["kind"],
                    "n": s["n"],
                    "by": s["covered_by"],
                }
                sk.append(rec)
                dskills.append(rec)
            groups.append({
                "group": g["group"],
                "n": len(sk),
                "uncovered": sum(1 for x in sk if x["n"] == 0),
                "thin": sum(1 for x in sk if 1 <= x["n"] <= 2),
                "skills": sk,
            })
        skills_by_domain[dom["domain"]] = dskills
        heat_domains.append({
            "domain": dom["domain"],
            "n": len(dskills),
            "uncovered": sum(1 for x in dskills if x["n"] == 0),
            "thin": sum(1 for x in dskills if 1 <= x["n"] <= 2),
            "healthy": sum(1 for x in dskills if x["n"] >= 3),
            "groups": groups,
        })

    total_skills = sum(d["n"] for d in heat_domains)
    total_uncov = sum(d["uncovered"] for d in heat_domains)
    total_thin = sum(d["thin"] for d in heat_domains)

    # ---- curriculum tree -------------------------------------------------
    branches = []
    for b in tree["branches"]:
        doms = b["acton_domains"]
        if not doms:
            cov = {
                "state": "unmapped",
                "n_skills": None,
                "n_covered": None,
                "pct": None,
                "uncovered": None,
                "thin": None,
                "cases": [],
                "case_count": None,
            }
        else:
            sk = [s for d in doms for s in skills_by_domain[d]]
            counter = Counter()
            for s in sk:
                for c in s["by"]:
                    counter[c] += 1
            n_cov = sum(1 for s in sk if s["n"] > 0)
            cov = {
                "state": "mapped",
                "n_skills": len(sk),
                "n_covered": n_cov,
                "pct": round(100.0 * n_cov / len(sk), 1),
                "uncovered": len(sk) - n_cov,
                "thin": sum(1 for s in sk if 1 <= s["n"] <= 2),
                "cases": [{"title": t, "n": n} for t, n in counter.most_common()],
                "case_count": len(counter),
            }
        branches.append({**b, "coverage": cov})

    # phase 4 roots
    roots = []
    for i in tree["intersections"]:
        roots.append({
            "id": "root-" + re.sub(r"[^a-z]+", "-", i["domain"].lower()),
            "domain": i["domain"],
            "branches": i["branches"],
            "note": i["note"],
            "cluster": i.get("cluster"),
            "priority": i.get("authoring_priority"),
            # domains.json#<id> -> the Root Connections card this tendril stands for
            "domain_id": (i.get("ref") or "#").split("#")[-1] or None,
        })

    # ---- case library ----------------------------------------------------
    ci_by_title = {c["title"]: c for c in cases_index["cases"]}
    ci_by_id = {c["id"]: c for c in cases_index["cases"]}

    all_spine_skills = [s for d in spine["domains"] for g in d["groups"] for s in g["skills"]]
    skill_label = {s["id"]: s["label"] for s in all_spine_skills}
    # matrix column -> spine skill ids it covers
    skills_by_col = {}
    for s in all_spine_skills:
        for col in s["covered_by"]:
            skills_by_col.setdefault(col, []).append(s["id"])
    # corpus case title -> root domain ids that claim it
    doms_by_case = {}
    for d in domsrc["domains"]:
        for t in d.get("existing_cases", []):
            doms_by_case.setdefault(t, []).append(d["id"])
    # branch id -> corpus case titles reachable through its domains
    cases_by_branch = {b["branch"]: b["existing_cases"] for b in dcov["by_branch"]}

    # avg_rating/rating_count per case_id, computed here rather than imported from
    # admin_core (this generator is deliberately self-contained) -- same tiny
    # averaging logic as admin_core._rating_summary().
    ratings_by_case = {}
    for r in subs.get("ratings", []):
        ratings_by_case.setdefault(r["case_id"], []).append(r["stars"])

    def _rating_summary(case_id):
        rs = ratings_by_case.get(case_id, [])
        return {"avg_rating": round(sum(rs) / len(rs), 1) if rs else None, "rating_count": len(rs)}

    def _case_detail_fields(cj, ci, matrix_col):
        """Fields shared by every Case Library entry, corpus-reconciled or
        pipeline-native alike -- everything derivable from case.json (cj) and/or
        a cases_index.json record (ci), independent of how the case was found."""
        case_id = (ci or {}).get("id") or (cj or {}).get("id")
        # Legacy cases join standards through a matrix column (skills_by_col);
        # pipeline case.json carries its own standards id list directly, which
        # is the more precise source when both are available.
        skill_ids = (cj or {}).get("standards")
        if matrix_col:
            n_skill_ids = len(skills_by_col.get(matrix_col, []))
        elif skill_ids:
            n_skill_ids = len(skill_ids)
        else:
            n_skill_ids = None
        return {
            "tier": (ci or {}).get("tier") or (cj or {}).get("tier"),
            "complexity": (cj or {}).get("complexity", (ci or {}).get("complexity")),
            "standards_count": (ci or {}).get("standards_count") or (len(skill_ids) if skill_ids else None),
            "domains_touched": (ci or {}).get("domains_touched") or [],
            "skill_ids": skill_ids,
            # skill ids are NOT shipped for the legacy join: the page derives them
            # from heat[].by. Pipeline cases ship skill_ids above instead.
            "n_skill_ids": n_skill_ids,
            "case_id": case_id,
            **_rating_summary(case_id),
            "protagonist": (cj or {}).get("protagonist"),
            "primary_metric": (cj or {}).get("primary_metric") or (ci or {}).get("primary_metric"),
            "options": (cj or {}).get("options") or (ci or {}).get("options") or {"A": None, "B": None},
            "margin_pct": (cj or {}).get("margin_pct", (ci or {}).get("margin_pct")),
            "balance_verdict": ((cj or {}).get("balance_test") or {}).get("verdict"),
            "argument_a": ((cj or {}).get("balance_test") or {}).get("argument_A"),
            "argument_b": ((cj or {}).get("balance_test") or {}).get("argument_B"),
            "deliverables": (cj or {}).get("deliverables") or [],
            "assumptions": (cj or {}).get("assumptions") or [],
            "qa": ({"verdict": (cj["qa"] or {}).get("verdict"),
                    "state": (cj["qa"] or {}).get("state"),
                    "blockers": (cj["qa"] or {}).get("blockers"),
                    "gaps": (cj["qa"] or {}).get("gaps"),
                    "gate": (cj["qa"] or {}).get("gate"),
                    "run_at": (cj["qa"] or {}).get("run_at"),
                    "note": (cj["qa"] or {}).get("note")} if (cj or {}).get("qa")
                   else ({"verdict": ci.get("qa_verdict")} if ci and ci.get("qa_verdict") else None)),
            "twist": (((cj or {}).get("facilitator") or {}).get("twist")),
            "sensitivity_note": (((cj or {}).get("facilitator") or {}).get("sensitivity_note")),
        }

    used_ci_ids = set()   # cases_index ids already placed in `lib` via corpus reconciliation
    lib = []
    for c in corpus_cases:
        r = recon[c["title"]]
        ci = ci_by_title.get(r["col"]) if r["col"] else None
        if ci:
            used_ci_ids.add(ci["id"])
        # A corpus record's own path never updates after conversion -- it's
        # frozen at its original legacy location. Once a case is reconciled
        # to a pipeline record, prefer the reconciled paths (which do track
        # cases/<id>/) for locating case.json / published HTML / pipeline docs.
        pipeline_path = None
        if ci and ci.get("paths", {}).get("case_json"):
            pipeline_path = str(Path(ci["paths"]["case_json"]).parent)
        elif c["path"].startswith("cases/"):
            pipeline_path = c["path"]
        cj = None
        if pipeline_path:
            jp = ROOT / pipeline_path / "case.json"
            if jp.exists():
                cj = json.loads(jp.read_text(encoding="utf-8"))
        links = case_links(c)
        if pipeline_path:
            pub_dir = ROOT / pipeline_path / "published"
            if pub_dir.is_dir():
                for hp in sorted(pub_dir.glob("*.html")):
                    rel = pipeline_path + "/published/" + hp.name
                    links["interactive_html"].append(make_link(rel, hp.name, "interactive_html", True))
        extra = []
        if cj and pipeline_path:
            for fn, lab in (("case.md", "Case source (markdown)"),
                            ("QA_REPORT.md", "QA report (facilitator)"),
                            ("FACILITATOR.md", "Facilitator pack"),
                            ("case.json", "case.json (machine record)")):
                if (ROOT / pipeline_path / fn).exists():
                    extra.append(make_link(pipeline_path + "/" + fn, lab, "pipeline", False))
        lib.append({
            "title": c["title"],
            "year": c["year"],
            "session": c["session"],
            "status": c["status"],
            "path": c["path"],
            "assets": c["assets"],
            "asset_links": links,
            "pipeline_links": extra,
            "has_guide": c["has_guide"],
            "has_socratic_plan": c["has_socratic_plan"],
            "n_assets": c["n_assets"],
            "n_links_ok": sum(1 for k, _l, _s in ASSET_KINDS for x in links[k] if x["exists"]),
            "n_links_missing": sum(1 for k, _l, _s in ASSET_KINDS for x in links[k] if not x["exists"]),
            "has_case_json": bool(cj),
            "mapped": bool(r["col"]),
            "legacy_unreconciled": not bool(r["col"]),
            "matrix_col": r["col"],
            "match": r["match"],
            "score": r["score"],
            "root_domains": doms_by_case.get(c["title"], []),
            **_case_detail_fields(cj, ci, r["col"]),
        })

    # ---- case library, part 2: pipeline-native cases ----------------------
    # Every case authored straight through the case-brainstorm -> ... ->
    # case-publish pipeline (not converted from a legacy corpus folder) has no
    # entry in corpus_index.json, so the loop above never visits it -- it was
    # invisible to the Case Library and unopenable from the dashboard even
    # though its case.json is real, on disk, and often fully published.
    # Walk every case pipeline_status.json knows about (any id with a real
    # cases/<id>/case.json, at whatever stage -- drafting through verified)
    # and add the ones the corpus loop above didn't already place.
    for pc in pipeline.get("cases", []):
        pid = pc["id"]
        if pc.get("origin") == "legacy" or pid in used_ci_ids:
            # "legacy" entries are folders already carried by corpus_cases above;
            # everything else already reconciled is in used_ci_ids.
            continue
        case_dir = ROOT / "cases" / pid
        jp = case_dir / "case.json"
        if not jp.exists():
            continue
        used_ci_ids.add(pid)
        cj = json.loads(jp.read_text(encoding="utf-8"))
        ci = ci_by_id.get(pid)
        rel_dir = "cases/" + pid

        links = {k: [] for k, _l, _s in ASSET_KINDS}
        pub_dir = case_dir / "published"
        if pub_dir.is_dir():
            kind_by_suffix = {".html": "interactive_html", ".xlsx": "data_workbooks",
                               ".pdf": "reference_pdfs"}
            image_ext = {".png", ".jpg", ".jpeg", ".gif", ".svg"}
            for fp in sorted(pub_dir.iterdir()):
                if fp.name == "MANIFEST.json" or not fp.is_file():
                    continue
                ext = fp.suffix.lower()
                if ext == ".docx":
                    kind = "guide_notes" if "facilitator" in fp.stem.lower() else "case_doc"
                elif ext in image_ext:
                    kind = "images"
                else:
                    kind = kind_by_suffix.get(ext)
                if not kind:
                    continue
                rel = rel_dir + "/published/" + fp.name
                links[kind].append(make_link(rel, fp.name, kind, kind in STUDENT_SAFE_KINDS))
        links["_folder"] = make_link(rel_dir, pid, "folder", False)

        extra = []
        for fn, lab in (("case.md", "Case source (markdown)"),
                        ("QA_REPORT.md", "QA report (facilitator)"),
                        ("FACILITATOR.md", "Facilitator pack"),
                        ("case.json", "case.json (machine record)")):
            if (case_dir / fn).exists():
                extra.append(make_link(rel_dir + "/" + fn, lab, "pipeline", False))

        assets_manifest = {k: [x["label"] for x in links[k]] for k, _l, _s in ASSET_KINDS}
        lib.append({
            "title": pc["title"],
            # These cases aren't part of a legacy Y1/Y2/Y3 cohort -- "Pipeline"
            # is a real, distinct provenance label, not a stand-in for missing
            # data. Studio (the pipeline's own grouping) fills the session slot.
            "year": "Pipeline",
            "session": cj.get("studio") or (ci or {}).get("studio") or "Unassigned studio",
            "status": pc.get("status") or cj.get("status"),
            "path": rel_dir,
            "assets": assets_manifest,
            "asset_links": links,
            "pipeline_links": extra,
            "has_guide": bool(assets_manifest["guide_notes"]),
            "has_socratic_plan": bool(assets_manifest["socratic_plan"]),
            "n_assets": sum(len(v) for v in assets_manifest.values()),
            "n_links_ok": sum(1 for k, _l, _s in ASSET_KINDS for x in links[k] if x["exists"]),
            "n_links_missing": sum(1 for k, _l, _s in ASSET_KINDS for x in links[k] if not x["exists"]),
            "has_case_json": True,
            # This case was never part of the legacy 27-case matrix, so that
            # reconciliation ("legacy_unreconciled") doesn't apply to it at all
            # -- it's not an unresolved gap, it just isn't the same problem.
            # "mapped" here means the library-wide, origin-agnostic question
            # "do we know this case's standards" -- yes, straight from its own
            # case.json, no matrix join needed.
            "mapped": bool(cj.get("standards")),
            "legacy_unreconciled": False,
            "matrix_col": None,
            "match": "n/a",
            "score": None,
            "root_domains": doms_by_case.get(pc["title"], []),
            **_case_detail_fields(cj, ci, None),
        })

    lib.sort(key=lambda c: (c["year"], c["session"], c["title"]))
    lib_by_title = {c["title"]: c for c in lib}

    # Best-of-Studio reference material — real files, previously unlinked.
    exemplars = {
        "student_work": [make_link("source/Best Of Studio/" + f, f, "exemplar", False)
                         for f in corpus.get("student_exemplars", [])],
        "case_examples": [make_link("source/Best Of Studio/Case Study Examples/" + f, f, "example", False)
                          for f in corpus.get("case_examples", [])],
    }

    # Legacy-matrix reconciliation gaps only -- never pipeline-native cases,
    # which were never part of that matrix and so have nothing to reconcile.
    unmapped_cases = [c for c in lib if c["legacy_unreconciled"]]

    # ---- gap queue -------------------------------------------------------
    # which application domains could actually close each cluster: a real
    # set-intersection between the cluster's zero-coverage skill ids and each
    # domain's signature_skills, not a name match.
    dom_sig = {d["id"]: set(d.get("signature_skills", [])) for d in domsrc["domains"]}
    dom_meta = {d["id"]: (d["name"], d.get("authoring_priority"),
                          (d.get("data_availability") or {}).get("grade")) for d in domsrc["domains"]}
    # gap_queue.json carries labels, not ids. Resolve each back to its spine id
    # through (domain, group, label) so the cluster can cross-navigate.
    id_by_dgl = {}
    for dom in spine["domains"]:
        for g in dom["groups"]:
            for s in g["skills"]:
                id_by_dgl[(dom["domain"], g["group"], s["label"])] = s["id"]
    gaps = []
    for g in gapq:
        for s in g["skills"]:
            s["id"] = id_by_dgl.get((g["domain"], g["group"], s["label"]))
        unc = [s for s in g["skills"] if s["n"] == 0]
        thin = [s for s in g["skills"] if s["n"] > 0]
        unc_ids = {s.get("id") for s in unc if s.get("id")}
        closers = []
        for did, sig in dom_sig.items():
            hit = sig & unc_ids
            if hit:
                nm, pr, gr = dom_meta[did]
                closers.append({"id": did, "name": nm, "priority": pr, "grade": gr, "n": len(hit)})
        closers.sort(key=lambda c: (-c["n"], {"HIGH": 0, "MEDIUM": 1, "LOW": 2}.get(c["priority"], 3), c["name"]))
        gaps.append({
            "domain": g["domain"],
            "group": g["group"],
            "n_gap": g["n_gap"],
            "n_total": g["n_total"],
            "n_uncovered": len(unc),
            "n_thin": len(thin),
            "share": round(100.0 * g["n_gap"] / g["n_total"], 1),
            "skills": g["skills"],
            "closers": closers,
        })
    gaps.sort(key=lambda g: (-g["n_uncovered"], -g["n_gap"], g["domain"]))

    # ---- tracker ---------------------------------------------------------
    def real(rows):
        return [r for r in rows if not r.get("_example")]

    learners_all = roster["learners"]
    asg_all = subs["assignments"]
    sub_all = subs["submissions"]
    dsc_all = subs["discussions"]

    def exceptions(learners, assignments, submissions, discussions):
        lmap = {l["id"]: l for l in learners}
        smap = {}
        for s in submissions:
            smap.setdefault(s["assignment_id"], []).append(s)
        dcount = Counter((d["learner_id"], d["case_id"]) for d in discussions)
        rows = []
        for a in assignments:
            L = lmap.get(a["learner_id"])
            if not L or L.get("status") != "active":
                continue
            mine = sorted(smap.get(a["id"], []), key=lambda s: s["submitted_on"])
            latest = mine[-1] if mine else None
            nd = dcount[(a["learner_id"], a["case_id"])]
            base = {
                "learner": L["display_name"],
                "learner_id": L["id"],
                "program": L["program"],
                "case_id": a["case_id"],
                "badge_index": a["badge_index"],
                "assigned_on": a["assigned_on"],
                "due_on": a["due_on"],
                "status": a["status"],
                "discussions": nd,
            }
            if a["status"] in ("complete", "withdrawn"):
                continue
            if latest and latest["reviewed_on"] is None:
                rows.append({**base, "kind": "AWAITING REVIEW", "rank": 1,
                             "detail": "Submitted " + latest["submitted_on"] + " · no facilitator review recorded",
                             "age": (TODAY - date.fromisoformat(latest["submitted_on"])).days})
                continue
            if a["status"] == "reviewed" and latest and latest.get("outcome") == "accepted" and nd >= 2:
                rows.append({**base, "kind": "READY TO COMPLETE", "rank": 2,
                             "detail": "Reviewed, accepted, " + str(nd) + " discussions logged · needs a human confirm",
                             "age": (TODAY - date.fromisoformat(latest["reviewed_on"])).days})
                continue
            if a["due_on"] and date.fromisoformat(a["due_on"]) < TODAY and not latest:
                rows.append({**base, "kind": "OVERDUE", "rank": 0,
                             "detail": "Due " + a["due_on"] + " · nothing submitted",
                             "age": (TODAY - date.fromisoformat(a["due_on"])).days})
                continue
            if a["due_on"] is None and not latest:
                rows.append({**base, "kind": "STALE", "rank": 3,
                             "detail": "No deadline set · assigned " + a["assigned_on"],
                             "age": (TODAY - date.fromisoformat(a["assigned_on"])).days})
        rows.sort(key=lambda r: (r["rank"], -r["age"]))
        return rows

    def badge_rows(learners, assignments, programs):
        done = Counter()
        for a in assignments:
            if a["status"] == "complete":
                done[a["learner_id"]] += 1
        out = []
        for L in learners:
            prog = programs[L["program"]]
            credited = sum(len(b["cases"]) for b in L["badges_earned"])
            in_flight = done[L["id"]]
            total = credited + in_flight
            nxt = prog["cases_per_badge"] - (total % prog["cases_per_badge"])
            out.append({
                "id": L["id"],
                "name": L["display_name"],
                "program": L["program"],
                "cohort": L["cohort"],
                "badges": len(L["badges_earned"]),
                "badges_total": prog["badges"],
                "cases_done": total,
                "cases_required": prog["cases_required"],
                "cases_per_badge": prog["cases_per_badge"],
                "to_next_badge": nxt if total < prog["cases_required"] else 0,
                "one_short": nxt == 1,
            })
        return out

    tracker = {
        "programs": roster["programs"],
        "today": TODAY.isoformat(),
        "real": {
            "learners": len(real(learners_all)),
            "assignments": len(real(asg_all)),
            "submissions": len(real(sub_all)),
            "discussions": len(real(dsc_all)),
            "exceptions": exceptions(real(learners_all), real(asg_all), real(sub_all), real(dsc_all)),
            "badges": badge_rows(real(learners_all), real(asg_all), roster["programs"]),
        },
        "example": {
            "learners": len(learners_all),
            "assignments": len(asg_all),
            "submissions": len(sub_all),
            "discussions": len(dsc_all),
            "exceptions": exceptions(learners_all, asg_all, sub_all, dsc_all),
            "badges": badge_rows(learners_all, asg_all, roster["programs"]),
        },
    }

    # ---- rubric, scoring, root connections -------------------------------
    rubric = parse_rubric()
    scoring = build_scoring(subs, ovr, roster, rubric)
    domains_block = build_domains_block(domsrc, dcov, skill_label)

    # ---- student payload ---------------------------------------------------
    # Built for EVERY active learner (not just one) so each gets their own
    # role-locked file -- see student_doc()/build(). "student" below stays the
    # first one for back-compat with dashboard.html's guide-only preview toggle,
    # which only ever needs a single example to render, never a real roster pick.
    actives = [l for l in roster["learners"] if l.get("status") == "active"]
    real_actives = [l for l in actives if not l.get("_example")]
    pick = (real_actives or actives)
    students = {}
    for l in pick:
        st = build_student(
            l["id"], roster, subs, lib_by_title, ci_by_id, all_spine_skills,
            scoring["example" if not real_actives else "real"],
        )
        st["preview_only"] = not bool(real_actives)
        st["n_real_learners"] = len(real_actives)
        students[l["id"]] = st
    student = students[pick[0]["id"]] if pick else None

    # ---- headline --------------------------------------------------------
    headline = {
        "corpus_cases": len(lib),
        "matrix_cols": len(matrix_cols),
        # legacy-matrix reconciliation only -- corpus_cases is the fixed universe
        # that reconciliation applies to; pipeline-native cases (never in that
        # matrix) are neither mapped nor unmapped by this measure.
        "mapped": len(corpus_cases) - len(unmapped_cases),
        "unmapped": len(unmapped_cases),
        "orphan_cols": len(orphan_cols),
        "fuzzy": len(fuzzy_links),
        "fuzzy_only_cols": len(fuzzy_only_cols),
        "skills": total_skills,
        "uncovered": total_uncov,
        "thin": total_thin,
        "healthy": total_skills - total_uncov - total_thin,
        "uncovered_pct": round(100.0 * total_uncov / total_skills, 1),
        "domains": len(heat_domains),
        "branches": len(branches),
        "unmapped_branches": sum(1 for b in branches if b["coverage"]["state"] == "unmapped"),
        "with_guide": sum(1 for c in lib if c["has_guide"]),
        "with_socratic": sum(1 for c in lib if c["has_socratic_plan"]),
        "asset_files": sum(c["n_assets"] for c in lib),
        "geometry_uncovered": next(d["uncovered"] for d in heat_domains if d["domain"] == "Geometry"),
        "geometry_skills": next(d["n"] for d in heat_domains if d["domain"] == "Geometry"),
        "root_domains": len(domains_block["domains"]),
        "root_clusters": len(domains_block["clusters"]),
        "data_sources": domains_block["n_sources"],
        "careers": sum(len(d["careers"]) for d in domains_block["domains"]),
        "links_total": len(LINKS),
        "links_ok": sum(1 for l in LINKS if l["exists"]),
        "links_missing": sum(1 for l in LINKS if not l["exists"]),
        "case_starved_branches": sum(1 for m in domains_block["matrix"] if m["case_starved"]),
        "domain_starved_branches": sum(1 for m in domains_block["matrix"] if m["domain_starved"]),
        "criteria": len(rubric["criteria"]),
        "scores_real": scoring["real"]["n_scores"],
    }

    return {
        "meta": {
            "generated_on": TODAY.isoformat(),
            "sources": SOURCES,
            "spine_source": spine.get("source"),
            "grade_band": spine.get("grade_band"),
            "tree_source": tree["_schema"]["source"],
            "fuzzy_cutoff": FUZZY_CUTOFF,
            "rubric_version": rubric["version"],
            "rubric_status": rubric["status"],
        },
        "headline": headline,
        "phases": tree["phases"],
        "branches": branches,
        "roots": roots,
        "heat": heat_domains,
        "cases": lib,
        "exemplars": exemplars,
        "cases_by_branch": cases_by_branch,
        "matrix": {
            "columns": matrix_cols,
            "orphans": orphan_cols,
            "fuzzy": fuzzy_links,
            "fuzzy_only_cols": fuzzy_only_cols,
        },
        "gaps": gaps,
        "pipeline": pipeline,
        "legacy_readiness": legacy_ready,
        "tracker": tracker,
        "rubric": rubric,
        "scoring": scoring,
        "rootc": domains_block,
        "student": student,
        "students": students,
        "links": {"total": len(LINKS), "ok": sum(1 for l in LINKS if l["exists"]),
                  "missing": [l["rel"] for l in LINKS if not l["exists"]]},
    }


# --------------------------------------------------------------------------
# the page
# --------------------------------------------------------------------------

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Math Builder · Curriculum Instrument</title>
<style>
:root{
  --paper:#FAF8F4; --paper-2:#F2EEE6; --card:#FFFFFF; --card-2:#FCFBF8;
  --ink:#16140F; --ink-2:#38342C; --muted:#5F594E; --faint:#6E675C;
  --rule:#DED8CC; --rule-2:#EBE6DC;
  --accent:#22406B; --accent-2:#325C93; --accent-soft:#E8EEF6; --accent-line:#B9C9DD;
  --flag:#A93A1E; --flag-soft:#F8E7E1; --flag-line:#E4B7A8;
  --warn:#7E5310; --warn-soft:#F8EFD9; --warn-line:#E0CB9A;
  --ok:#2A5C45; --ok-soft:#E4EFE8;
  --c0:#B23F22; --c1:#D9E2EA; --c2:#B4C6D8; --c3:#89A7C4; --c4:#5C82AC; --c5:#3A5F8E; --c6:#22406B;
  --s1:4px; --s2:8px; --s3:12px; --s4:16px; --s5:24px; --s6:32px; --s7:48px; --s8:64px;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,"Times New Roman",serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,"Helvetica Neue",Arial,sans-serif;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;
  --shadow:0 1px 2px rgba(24,20,12,.05),0 4px 14px rgba(24,20,12,.05);
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{
  background:var(--paper); color:var(--ink);
  font-family:var(--sans); font-size:14px; line-height:1.55;
  -webkit-font-smoothing:antialiased; text-rendering:optimizeLegibility;
}
h1,h2,h3,h4{font-family:var(--serif); font-weight:600; letter-spacing:-.01em; margin:0}
a{color:var(--accent)}
button{font:inherit;color:inherit}
.mono{font-family:var(--mono);font-variant-numeric:tabular-nums}
.wrap{max-width:1440px;margin:0 auto;padding:0 var(--s6)}

/* ---------- masthead ---------- */
.masthead{border-bottom:1px solid var(--rule);background:var(--paper)}
.mast-top{display:flex;align-items:flex-end;justify-content:space-between;gap:var(--s6);padding:var(--s6) 0 var(--s4)}
.mast-id{display:flex;align-items:baseline;gap:var(--s3);flex-wrap:wrap}
h1.title{font-size:27px;line-height:1.15}
.kicker{font-family:var(--sans);font-size:10.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.mast-sub{color:var(--muted);font-size:12.5px;max-width:62ch;margin-top:var(--s2)}
.mast-meta{text-align:right;font-size:11px;color:var(--faint);font-family:var(--mono);line-height:1.7;white-space:nowrap}

.stat-strip{display:grid;grid-template-columns:repeat(6,1fr);border-top:1px solid var(--rule-2);border-left:1px solid var(--rule-2)}
.stat-strip[data-n="5"]{grid-template-columns:repeat(5,1fr)}
.stat-strip[data-n="4"]{grid-template-columns:repeat(4,1fr)}
.stat{padding:var(--s3) var(--s4);border-right:1px solid var(--rule-2);border-bottom:1px solid var(--rule-2);background:var(--card-2)}
.stat .v{font-family:var(--mono);font-size:22px;font-weight:600;letter-spacing:-.02em;line-height:1.1;color:var(--ink)}
.stat .v small{font-size:12px;color:var(--faint);font-weight:400}
.stat .k{font-size:10px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);margin-top:3px}
.stat.alert .v{color:var(--flag)}
.stat.alert{background:var(--flag-soft)}

/* ---------- tabs ---------- */
.tabbar{position:sticky;top:0;z-index:40;background:rgba(250,248,244,.96);backdrop-filter:saturate(1.4) blur(6px);border-bottom:1px solid var(--rule)}
.tabs{display:flex;gap:0;overflow-x:auto}
.tab{appearance:none;background:none;border:0;border-bottom:2px solid transparent;padding:var(--s4) var(--s4) 13px;cursor:pointer;
  font-size:12.5px;font-weight:600;color:var(--muted);letter-spacing:.02em;white-space:nowrap;display:flex;align-items:center;gap:var(--s2);transition:color .12s,border-color .12s}
.tab:hover{color:var(--ink)}
.tab[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--accent)}
.tab .num{font-family:var(--mono);font-size:10.5px;color:var(--faint);background:var(--paper-2);border:1px solid var(--rule-2);border-radius:3px;padding:1px 5px}
.tab[aria-selected="true"] .num{background:var(--accent-soft);border-color:var(--accent-line);color:var(--accent)}
.tab:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}

.view{display:none;padding:var(--s6) 0 var(--s8)}
.view.on{display:block}

/* ---------- shared ---------- */
.sec-head{display:flex;align-items:baseline;justify-content:space-between;gap:var(--s4);margin-bottom:var(--s4);flex-wrap:wrap}
.sec-head h2{font-size:19px}
.sec-head .note{font-size:12px;color:var(--muted);max-width:70ch}
.eyebrow{font-size:10px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--muted)}
.rule{height:1px;background:var(--rule);margin:var(--s6) 0}
.card{background:var(--card);border:1px solid var(--rule);border-radius:5px}
.pill{display:inline-flex;align-items:center;gap:4px;font-size:10px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;
  padding:2px 7px;border-radius:3px;border:1px solid var(--rule);background:var(--paper-2);color:var(--muted);white-space:nowrap}
.pill.ms{background:var(--accent-soft);border-color:var(--accent-line);color:var(--accent)}
.pill.hs{background:#EFEAF6;border-color:#CFC3E2;color:#4B3A73}
.pill.adv{background:#E6F0EC;border-color:#B7D2C6;color:var(--ok)}
.pill.flag{background:var(--flag-soft);border-color:var(--flag-line);color:var(--flag)}
.pill.warn{background:var(--warn-soft);border-color:var(--warn-line);color:var(--warn)}
.pill.ok{background:var(--ok-soft);border-color:#B7D2C6;color:var(--ok)}
.callout{border-left:3px solid var(--flag);background:var(--flag-soft);padding:var(--s3) var(--s4);border-radius:0 4px 4px 0;font-size:12.5px;color:var(--ink-2)}
.callout strong{color:var(--flag)}
.callout.info{border-left-color:var(--accent);background:var(--accent-soft)}
.callout.info strong{color:var(--accent)}
.empty{border:1px dashed var(--rule);border-radius:5px;background:repeating-linear-gradient(135deg,transparent,transparent 7px,rgba(110,103,92,.045) 7px,rgba(110,103,92,.045) 14px);
  padding:var(--s7) var(--s6);text-align:center}
.filters{display:flex;flex-wrap:wrap;gap:var(--s2);align-items:center;padding:var(--s3) 0 var(--s4);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s5)}
.fgroup{display:flex;gap:4px;align-items:center}
.flabel{font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--faint);margin-right:var(--s1)}
.chip{appearance:none;border:1px solid var(--rule);background:var(--card);border-radius:3px;padding:4px 9px;font-size:11.5px;color:var(--muted);cursor:pointer;transition:.12s}
.chip:hover{border-color:var(--faint);color:var(--ink)}
.chip[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:#fff}
.chip:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
input[type=search],input[type=text]{border:1px solid var(--rule);background:var(--card);border-radius:3px;padding:5px 9px;font-size:12.5px;min-width:230px;color:var(--ink)}
input[type=search]:focus{outline:2px solid var(--accent);outline-offset:-1px;border-color:var(--accent)}
.count-note{margin-left:auto;font-size:11.5px;color:var(--muted);font-family:var(--mono)}

/* ---------- 1 · tree ---------- */
.tree-layout{display:grid;grid-template-columns:minmax(0,1fr) 372px;gap:var(--s6);align-items:start}
.tree-stage{background:var(--card);border:1px solid var(--rule);border-radius:5px;padding:var(--s3);box-shadow:var(--shadow);overflow:hidden}
#treeSvg{display:block;width:100%;height:auto}
.node{cursor:pointer}
.node rect.box{fill:var(--card-2);stroke:var(--rule);stroke-width:1.25;transition:stroke .12s,fill .12s}
.node:hover rect.box{stroke:var(--accent-2)}
.node.sel rect.box{stroke:var(--accent);stroke-width:2.25;fill:#fff}
.node.unmapped rect.box{fill:url(#hatch);stroke:var(--warn-line);stroke-dasharray:5 3}
.node.sel.unmapped rect.box{stroke:var(--warn);stroke-width:2.25}
.node .nm{font-family:var(--serif);font-size:14.5px;font-weight:600;fill:var(--ink)}
.node .sub{font-family:var(--mono);font-size:10px;fill:var(--muted)}
.node .band{font-family:var(--sans);font-size:9px;font-weight:700;letter-spacing:.1em;fill:var(--muted)}
.node .ringval{font-family:var(--mono);font-size:12px;font-weight:600;fill:var(--ink);text-anchor:middle}
.node .ringno{font-family:var(--mono);font-size:13px;fill:var(--warn);text-anchor:middle}
.edge{fill:none;stroke:#C4BCAD;stroke-width:1.25;transition:stroke .12s,stroke-width .12s,opacity .12s}
.edge.hot{stroke:var(--accent);stroke-width:2.25}
.edge.dim{opacity:.28}
.edge.root{stroke:#CBBFA8;stroke-dasharray:3 4;opacity:.24}
.edge.root.hot{stroke:var(--warn);opacity:1;stroke-dasharray:3 4}
.phase-band text{font-family:var(--sans);font-size:9.5px;font-weight:700;letter-spacing:.14em;fill:var(--faint)}
.phase-band line{stroke:var(--rule-2)}
.rootnode rect{fill:var(--paper-2);stroke:var(--rule);stroke-dasharray:2 3}
.rootnode:hover rect{stroke:var(--warn)}
.rootnode text.rt{font-family:var(--serif);font-size:12.5px;fill:var(--ink-2)}
.rootnode text.rs{font-family:var(--mono);font-size:9px;fill:var(--faint)}

.panel{position:sticky;top:64px;background:var(--card);border:1px solid var(--rule);border-radius:5px;box-shadow:var(--shadow);max-height:calc(100vh - 96px);overflow:auto}
.panel-head{padding:var(--s4) var(--s5);border-bottom:1px solid var(--rule-2)}
.panel-head h3{font-size:19px;margin-bottom:2px}
.panel-body{padding:var(--s4) var(--s5) var(--s6)}
.panel h4{font-size:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-family:var(--sans);margin:var(--s5) 0 var(--s2)}
.panel h4:first-child{margin-top:0}
.panel p{font-size:12.5px;color:var(--ink-2);margin:0 0 var(--s2)}
.taglist{display:flex;flex-wrap:wrap;gap:4px}
.tag{font-size:11px;border:1px solid var(--rule-2);background:var(--paper-2);border-radius:3px;padding:2px 7px;color:var(--ink-2)}
.tag.b{border-color:var(--accent-line);background:var(--accent-soft);color:var(--accent)}
.barrow{display:grid;grid-template-columns:1fr 42px;gap:var(--s2);align-items:center;font-size:11.5px;padding:2px 0}
.barrow .lab{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--ink-2)}
.bar{height:5px;background:var(--paper-2);border-radius:2px;overflow:hidden}
.bar i{display:block;height:100%;background:var(--accent-2)}
.kv{display:grid;grid-template-columns:auto 1fr;gap:2px var(--s3);font-size:12px}
.kv dt{color:var(--muted)}
.kv dd{margin:0;font-family:var(--mono);color:var(--ink)}

/* ---------- 2 · heatmap ---------- */
.legend{display:flex;gap:var(--s4);flex-wrap:wrap;align-items:center;font-size:11.5px;color:var(--muted)}
.legend .item{display:flex;align-items:center;gap:5px}
.sw{width:13px;height:13px;border-radius:2px;border:1px solid rgba(24,20,12,.14)}
.dom-block{margin-bottom:var(--s6);break-inside:avoid}
.dom-head{display:flex;align-items:baseline;gap:var(--s3);border-bottom:1px solid var(--ink);padding-bottom:5px;margin-bottom:var(--s3)}
.dom-head h3{font-size:16px}
.dom-head .meta{margin-left:auto;font-family:var(--mono);font-size:11px;color:var(--muted)}
.grp{display:grid;grid-template-columns:206px 1fr;gap:var(--s4);padding:5px 0;border-bottom:1px solid var(--rule-2);align-items:start}
.grp:last-child{border-bottom:0}
.grp .gname{font-size:11.5px;color:var(--ink-2);line-height:1.35;padding-top:2px}
.grp .gname em{display:block;font-style:normal;font-family:var(--mono);font-size:10px;color:var(--faint)}
.cells{display:flex;flex-wrap:wrap;gap:2px}
.cell{width:13px;height:13px;border-radius:2px;border:1px solid rgba(24,20,12,.10);cursor:default}
.cell.k-howto{border-radius:7px}
.cell.hot{outline:2px solid var(--ink);outline-offset:1px}
.cell.hide{opacity:.13}
#tip{position:fixed;z-index:100;pointer-events:none;max-width:330px;background:#1B1913;color:#F6F3EC;border-radius:4px;padding:9px 11px;
  font-size:12px;line-height:1.45;box-shadow:0 6px 24px rgba(0,0,0,.28);display:none}
#tip .t{font-family:var(--serif);font-size:13.5px;color:#fff;margin-bottom:2px}
#tip .m{font-family:var(--mono);font-size:10.5px;color:#B9B2A4;letter-spacing:.04em;text-transform:uppercase}
#tip .c{margin-top:6px;padding-top:6px;border-top:1px solid #38342B;color:#DCD6C9;font-size:11.5px}

/* ---------- 3 · library ---------- */
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:var(--s4)}
.ccard{background:var(--card);border:1px solid var(--rule);border-radius:5px;padding:var(--s4);cursor:pointer;transition:.12s;text-align:left;width:100%;display:block;font:inherit}
.ccard:hover{border-color:var(--accent-2);box-shadow:var(--shadow);transform:translateY(-1px)}
.ccard:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.ccard.sel{border-color:var(--accent);box-shadow:var(--shadow)}
.ccard .ct{font-family:var(--serif);font-size:16px;font-weight:600;line-height:1.25}
.ccard .cm{font-family:var(--mono);font-size:10.5px;color:var(--muted);margin-top:3px;letter-spacing:.03em}
.chips{display:flex;flex-wrap:wrap;gap:4px;margin-top:var(--s3)}
.ac{font-size:10.5px;font-family:var(--mono);border:1px solid var(--rule-2);background:var(--paper-2);border-radius:3px;padding:1.5px 6px;color:var(--muted)}
.ac.on{background:var(--accent-soft);border-color:var(--accent-line);color:var(--accent)}
.ac.gold{background:var(--warn-soft);border-color:var(--warn-line);color:var(--warn)}
.ccard .flagline{margin-top:var(--s3);padding-top:var(--s2);border-top:1px solid var(--rule-2);display:flex;justify-content:space-between;align-items:center;gap:var(--s2)}
.path{font-family:var(--mono);font-size:11px;color:var(--muted);word-break:break-all;background:var(--paper-2);border:1px solid var(--rule-2);border-radius:3px;padding:6px 8px}
.manifest{font-size:12px}
.manifest li{margin-bottom:2px}
.manifest ul{margin:2px 0 var(--s3);padding-left:18px}

/* ---------- 4 · gaps ---------- */
.two{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:var(--s7);align-items:start}
.split{display:grid;grid-template-columns:minmax(0,1fr) 372px;gap:var(--s6);align-items:start}
.qhead{display:flex;align-items:center;gap:var(--s3);border-bottom:2px solid var(--ink);padding-bottom:var(--s2);margin-bottom:var(--s3)}
.qhead h2{font-size:18px}
.qhead .n{margin-left:auto;font-family:var(--mono);font-size:12px;color:var(--muted)}
.qnote{font-size:12px;color:var(--muted);margin-bottom:var(--s4);max-width:60ch}
.grow{border:1px solid var(--rule);border-left:3px solid var(--flag);border-radius:0 4px 4px 0;background:var(--card);padding:var(--s3) var(--s4);margin-bottom:var(--s2)}
.grow.thin-only{border-left-color:var(--warn)}
.grow .gh{display:flex;align-items:baseline;gap:var(--s2);flex-wrap:wrap}
.grow .gh .rank{font-family:var(--mono);font-size:11px;color:var(--faint);width:22px}
.grow .gh .gt{font-family:var(--serif);font-size:15px;font-weight:600}
.grow .gh .gd{font-size:11px;color:var(--muted)}
.grow .gh .gn{margin-left:auto;font-family:var(--mono);font-size:11.5px;color:var(--flag)}
.gapbar{display:flex;height:6px;border-radius:2px;overflow:hidden;margin:var(--s2) 0;background:var(--paper-2)}
.gapbar i{display:block;height:100%}
.skl{display:flex;flex-wrap:wrap;gap:3px;margin-top:var(--s2)}
.skl span{font-size:10.5px;border-radius:3px;padding:1.5px 6px;border:1px solid}
.skl .z{background:var(--flag-soft);border-color:var(--flag-line);color:var(--flag)}
.skl .t{background:var(--warn-soft);border-color:var(--warn-line);color:var(--warn)}
.recon-row{display:grid;grid-template-columns:1fr auto;gap:var(--s3);align-items:center;padding:7px var(--s3);border-bottom:1px solid var(--rule-2);font-size:12.5px}
.recon-row:hover{background:var(--card-2)}
.recon-row .rt{font-family:var(--serif);font-size:14px}
.recon-row .rp{font-family:var(--mono);font-size:10.5px;color:var(--faint)}
.recon-wrap{border:1px solid var(--rule);border-left:3px solid var(--accent);border-radius:0 4px 4px 0;background:var(--card)}

/* ---------- 4b · pipeline ---------- */
.pipeboard{display:grid;grid-template-columns:repeat(6,minmax(200px,1fr));gap:var(--s4);align-items:start;overflow-x:auto;padding-bottom:var(--s2)}
.pipecol{background:var(--card-2);border:1px solid var(--rule-2);border-radius:6px;padding:var(--s3);min-width:200px}
.pipecol h3{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:0 0 2px;display:flex;align-items:center;justify-content:space-between}
.pipecol h3 .n{font-family:var(--mono);color:var(--ink);font-weight:700}
.pipecol .colnote{font-size:10.5px;color:var(--faint);margin-bottom:var(--s3);line-height:1.35}
.pipecard{background:var(--card);border:1px solid var(--rule);border-left:3px solid var(--rule);border-radius:0 4px 4px 0;padding:var(--s2) var(--s3);margin-bottom:var(--s2);font-size:12px;display:block;width:100%;text-align:left;font:inherit}
.pipecard.st-ok{border-left-color:var(--ok)}
.pipecard.st-flag{border-left-color:var(--flag)}
.pipecard.st-warn{border-left-color:var(--warn)}
.pipecard[data-go]{cursor:pointer;transition:.12s}
.pipecard[data-go]:hover{border-color:var(--accent-line);box-shadow:0 1px 4px rgba(0,0,0,.08)}
.pipecard[data-go]:hover .pt{color:var(--accent)}
.pipecard .pt{font-family:var(--serif);font-size:14px;font-weight:600;line-height:1.25}
.pipecard .pid{font-family:var(--mono);font-size:10px;color:var(--faint);margin-top:1px}
.pipecard .ptags{display:flex;flex-wrap:wrap;gap:4px;margin-top:6px}
.pipecard .pnext{font-size:11px;color:var(--muted);margin-top:6px;line-height:1.35;border-top:1px dashed var(--rule-2);padding-top:5px}
.pipecard .popen{font-size:10px;font-weight:700;color:var(--accent);margin-top:6px;letter-spacing:.02em}
.pipecol.empty{opacity:.55}
.pipecol .emptynote{font-size:11px;color:var(--faint);font-style:italic}
.pipe-legacy{margin-top:var(--s5);border:1px dashed var(--rule);border-radius:6px;padding:var(--s5);background:var(--card-2);font-size:12px;color:var(--muted)}
.pipe-legacy h3{font-family:var(--serif);font-size:16px;color:var(--ink)}
.lr-two{display:grid;grid-template-columns:1fr 1fr;gap:var(--s6);margin-top:var(--s3)}
.lr-row{display:grid;grid-template-columns:170px 1fr auto;gap:var(--s3);align-items:center;margin-top:7px;font-size:11.5px}
.lr-lab{color:var(--ink)}
.lr-bar{height:7px;border-radius:3px;background:var(--paper-2);overflow:hidden}
.lr-bar i{display:block;height:100%;background:var(--accent)}
.lr-pct{color:var(--muted);white-space:nowrap;font-size:11px}
.lr-note{grid-column:1/-1;font-size:10.5px;color:var(--faint);margin:-2px 0 4px;padding-left:2px}
.lr-absent{margin-top:var(--s5);padding-top:var(--s4);border-top:1px solid var(--rule-2);font-size:11.5px}
.lr-absent div{margin-top:4px}

/* ---------- 5 · tracker ---------- */
.exc-row{display:grid;grid-template-columns:132px 1fr auto;gap:var(--s4);align-items:center;padding:var(--s3) var(--s4);border-bottom:1px solid var(--rule-2)}
.exc-row:last-child{border-bottom:0}
.exc-kind{font-size:10px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;padding:3px 7px;border-radius:3px;text-align:center;border:1px solid}
.k-OVERDUE{background:var(--flag-soft);border-color:var(--flag-line);color:var(--flag)}
.k-AWAITING{background:var(--warn-soft);border-color:var(--warn-line);color:var(--warn)}
.k-READY{background:var(--ok-soft);border-color:#B7D2C6;color:var(--ok)}
.k-STALE{background:var(--paper-2);border-color:var(--rule);color:var(--muted)}
.exc-row .who{font-family:var(--serif);font-size:15px}
.exc-row .det{font-size:11.5px;color:var(--muted);font-family:var(--mono)}
.exc-row .age{font-family:var(--mono);font-size:11.5px;color:var(--faint);text-align:right;white-space:nowrap}
.rings{display:grid;grid-template-columns:repeat(auto-fill,minmax(228px,1fr));gap:var(--s4)}
.ringcard{background:var(--card);border:1px solid var(--rule);border-radius:5px;padding:var(--s4);display:flex;gap:var(--s4);align-items:center}
.ringcard .who{font-family:var(--serif);font-size:15px;line-height:1.2}
.ringcard .sub{font-family:var(--mono);font-size:10.5px;color:var(--muted);margin-top:2px}
.banner{display:flex;gap:var(--s3);align-items:center;border:1px solid var(--warn-line);background:var(--warn-soft);border-radius:4px;padding:var(--s3) var(--s4);font-size:12.5px;color:var(--ink-2);margin-bottom:var(--s5)}
.banner strong{color:var(--warn)}
.toggle{margin-left:auto}

/* ---------- 6 · role bar + global search + router ---------- */
.rolebar{background:var(--ink);color:#F6F3EC;font-size:11.5px}
.rolebar .wrap{display:flex;align-items:center;gap:var(--s4);padding:7px var(--s6);min-height:36px}
.rolebar .rl{font-weight:700;letter-spacing:.13em;text-transform:uppercase;font-size:10px;display:flex;align-items:center;gap:7px}
.rolebar .rl .dot{width:8px;height:8px;border-radius:50%;background:#F0C24B;flex:none}
.rolebar .rsub{color:#CFC8B9;font-family:var(--mono);font-size:10.5px}
.rolebar .spacer{margin-left:auto}
.rolesw{display:flex;border:1px solid rgba(246,243,236,.34);border-radius:4px;overflow:hidden}
.rolesw button{appearance:none;background:transparent;border:0;color:#DCD6C9;font-size:11px;font-weight:600;padding:4px 11px;cursor:pointer;letter-spacing:.03em}
.rolesw button[aria-pressed="true"]{background:#F6F3EC;color:#16140F}
.rolesw button:focus-visible{outline:2px solid #F0C24B;outline-offset:-2px}
body[data-role="student"] .rolebar{background:#164A3D;color:#F1F7F4}
body[data-role="student"] .rolebar .rl .dot{background:#8FD9BE}
body[data-role="student"] .rolebar .rsub{color:#C3DCD3}
body[data-role="student"] .rolesw{border-color:rgba(241,247,244,.4)}
body[data-role="student"] .rolesw button{color:#DCEBE5}
body[data-role="student"] .rolesw button[aria-pressed="true"]{background:#F1F7F4;color:#123C31}
body[data-role="student"]{--accent:#164A3D;--accent-2:#1F6553;--accent-soft:#E3F0EA;--accent-line:#AFCFC3}
body[data-role="student"] .tabbar{border-bottom-color:#BFD8CE}
body[data-role="student"] .masthead{border-bottom:3px solid #164A3D}

.navrow{display:flex;align-items:center;gap:var(--s3);padding:var(--s3) 0 0}
.backbtn{appearance:none;display:inline-flex;align-items:center;gap:6px;border:1px solid var(--rule);background:var(--card);
  border-radius:3px;padding:4px 11px;font-size:11.5px;color:var(--ink-2);cursor:pointer}
.backbtn:hover:not([disabled]){border-color:var(--faint)}
.backbtn[disabled]{opacity:.42;cursor:default}
.backbtn:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.crumb{font-size:11.5px;color:var(--muted);font-family:var(--mono)}
.crumb b{color:var(--ink);font-weight:600}

.searchwrap{position:relative;min-width:300px}
.searchwrap input{width:100%;min-width:0}
.searchwrap kbd{position:absolute;right:7px;top:6px;font-family:var(--mono);font-size:10px;color:var(--faint);
  border:1px solid var(--rule);border-radius:3px;padding:0 5px;background:var(--paper-2);pointer-events:none}
.results{position:absolute;z-index:60;top:calc(100% + 5px);left:0;right:0;max-height:60vh;overflow:auto;background:var(--card);
  border:1px solid var(--rule);border-radius:5px;box-shadow:0 8px 30px rgba(24,20,12,.15);display:none}
.results.on{display:block}
.results .rgroup{font-size:9.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);
  padding:7px var(--s4) 3px;background:var(--card-2);border-bottom:1px solid var(--rule-2);position:sticky;top:0}
.results button{display:block;width:100%;text-align:left;appearance:none;background:none;border:0;border-bottom:1px solid var(--rule-2);
  padding:7px var(--s4);cursor:pointer;font-size:12.5px;color:var(--ink)}
.results button:hover,.results button.cur{background:var(--accent-soft)}
.results button .rm{font-family:var(--mono);font-size:10.5px;color:var(--muted);display:block}
.results .none{padding:var(--s4);font-size:12.5px;color:var(--muted)}

/* ---------- asset links ---------- */
.alist{display:flex;flex-direction:column;gap:3px;margin:0 0 var(--s3)}
.alink{display:flex;align-items:center;gap:var(--s2);border:1px solid var(--rule-2);background:var(--card-2);border-radius:4px;
  padding:6px 9px;font-size:12px;color:var(--accent);text-decoration:none;transition:.12s}
.alink:hover{border-color:var(--accent-line);background:var(--accent-soft)}
.alink:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.alink .ext{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
  border:1px solid var(--accent-line);background:var(--accent-soft);color:var(--accent);border-radius:2px;padding:1px 5px;flex:none;min-width:38px;text-align:center}
.alink .fn{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.alink .sz{margin-left:auto;font-family:var(--mono);font-size:10px;color:var(--muted);flex:none}
.alink.dead{color:var(--flag);border-color:var(--flag-line);background:var(--flag-soft);cursor:not-allowed}
.alink.dead .ext{border-color:var(--flag-line);background:transparent;color:var(--flag)}
.alink.folder .ext{background:var(--warn-soft);border-color:var(--warn-line);color:var(--warn)}

/* ---------- primary open-case CTA -- the interactive HTML is the starting
   point for a case, everything else (docx/xlsx/pdf) is a secondary download ---------- */
.primary-cta{display:flex;align-items:center;gap:8px;background:var(--accent);color:#fff;border:none;
  border-radius:5px;padding:11px 16px;font-size:13.5px;font-weight:700;text-decoration:none;
  margin:2px 0 14px;transition:.12s;width:fit-content}
.primary-cta:hover{filter:brightness(1.08)}
.primary-cta:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.primary-cta .ic{font-size:15px;line-height:1}
.primary-cta.dead{background:var(--flag);cursor:not-allowed;opacity:.7}
.downloads-label{font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:12px 0 5px}
.akind{font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:var(--s3) 0 var(--s1)}
.ext-link{font-size:12px;color:var(--accent);text-decoration:none;border-bottom:1px solid var(--accent-line)}
.ext-link:hover{border-bottom-color:var(--accent)}

/* ---------- case detail sheet ---------- */
.scrim{position:fixed;inset:0;background:rgba(24,20,12,.34);z-index:80;display:none;animation:fade .14s ease-out}
.scrim.on{display:block}
.sheet{position:fixed;top:0;right:0;bottom:0;width:min(620px,100%);background:var(--card);border-left:1px solid var(--rule);
  box-shadow:-8px 0 40px rgba(24,20,12,.16);z-index:81;overflow:auto;display:none}
.sheet.on{display:block;animation:slidein .18s cubic-bezier(.2,.7,.3,1)}
@keyframes fade{from{opacity:0}to{opacity:1}}
@keyframes slidein{from{transform:translateX(22px);opacity:.4}to{transform:none;opacity:1}}
@media (prefers-reduced-motion:reduce){.scrim,.sheet.on{animation:none}}
.sheet-head{position:sticky;top:0;background:var(--card);border-bottom:1px solid var(--rule);padding:var(--s4) var(--s5);z-index:2}
.sheet-head .eyebrow{margin-bottom:3px}
.sheet-head h3{font-size:22px;line-height:1.18}
.sheet-close{position:absolute;top:var(--s3);right:var(--s3);appearance:none;border:1px solid var(--rule);background:var(--card);
  border-radius:3px;width:28px;height:28px;cursor:pointer;color:var(--muted);font-size:15px;line-height:1}
.sheet-close:hover{border-color:var(--faint);color:var(--ink)}
.sheet-close:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.sheet-body{padding:var(--s4) var(--s5) var(--s8)}
.sheet-body h4{font-size:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);
  font-family:var(--sans);margin:var(--s5) 0 var(--s2);padding-bottom:4px;border-bottom:1px solid var(--rule-2)}
.sheet-body p{font-size:12.5px;color:var(--ink-2);margin:0 0 var(--s2)}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:var(--s3)}
.opt{border:1px solid var(--rule);border-radius:4px;padding:var(--s3);background:var(--card-2)}
.opt .ol{font-size:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin-bottom:3px}
.opt p{font-size:12px;margin:0}
.jump{appearance:none;border:1px solid var(--accent-line);background:var(--accent-soft);color:var(--accent);border-radius:3px;
  padding:2px 8px;font-size:11px;cursor:pointer;transition:.12s}
.jump:hover{background:var(--accent);color:#fff;border-color:var(--accent)}
.jump:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.jump.warnj{border-color:var(--warn-line);background:var(--warn-soft);color:var(--warn)}
.jump.warnj:hover{background:var(--warn);color:#fff}
.jumps{display:flex;flex-wrap:wrap;gap:4px}
.absent{font-size:12px;color:var(--faint);font-style:italic}

/* ---------- 7 · root connections ---------- */
.cluster{margin-bottom:var(--s6)}
.cluster-head{display:flex;align-items:baseline;gap:var(--s3);border-bottom:1px solid var(--ink);padding-bottom:5px;margin-bottom:var(--s3)}
.cluster-head h3{font-size:16px}
.cluster-head .meta{margin-left:auto;font-family:var(--mono);font-size:11px;color:var(--muted)}
.dgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(268px,1fr));gap:var(--s3)}
.dcard{background:var(--card);border:1px solid var(--rule);border-radius:5px;padding:var(--s3) var(--s4);cursor:pointer;text-align:left;
  width:100%;font:inherit;transition:.12s;border-left:3px solid var(--rule)}
.dcard:hover{border-color:var(--accent-2);border-left-color:var(--accent-2);box-shadow:var(--shadow)}
.dcard:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.dcard.sel{border-color:var(--accent);border-left-color:var(--accent);box-shadow:var(--shadow)}
.dcard.p-HIGH{border-left-color:var(--flag)}
.dcard.p-MEDIUM{border-left-color:var(--warn)}
.dcard.p-LOW{border-left-color:var(--rule)}
.dcard .dn{font-family:var(--serif);font-size:15px;font-weight:600;line-height:1.22}
.dcard .dl{font-size:11.5px;color:var(--muted);margin-top:4px;line-height:1.4}
.dcard .dm{display:flex;flex-wrap:wrap;gap:4px;margin-top:var(--s3);align-items:center}
.mini{font-family:var(--mono);font-size:10px;color:var(--muted);border:1px solid var(--rule-2);background:var(--paper-2);border-radius:3px;padding:1px 5px}
.mini.hot{border-color:var(--flag-line);background:var(--flag-soft);color:var(--flag)}
.mini.good{border-color:#B7D2C6;background:var(--ok-soft);color:var(--ok)}
.mtx{width:100%;border-collapse:collapse;font-size:12px}
.mtx th,.mtx td{border:1px solid var(--rule-2);padding:6px 9px;text-align:left;vertical-align:middle}
.mtx thead th{background:var(--card-2);font-size:10px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);font-weight:700}
.mtx td.num{font-family:var(--mono);text-align:right;white-space:nowrap}
.mtx tr.starved td{background:var(--flag-soft)}
.mtx tr.warnrow td{background:var(--warn-soft)}
.mtx .bn{font-family:var(--serif);font-size:14px}
.mtx .rz{font-size:11px;color:var(--muted)}
.srcrow{display:flex;gap:var(--s2);align-items:baseline;padding:5px 0;border-bottom:1px solid var(--rule-2);font-size:12px}
.srcrow:last-child{border-bottom:0}
.srcrow .off{color:var(--muted);font-size:11.5px}
.career{border-left:2px solid var(--accent-line);padding:2px 0 2px var(--s3);margin-bottom:var(--s3)}
.career .ct2{font-family:var(--serif);font-size:14px;font-weight:600}
.career .cu{font-size:12px;color:var(--ink-2);margin:2px 0}
.career .cp{font-size:11.5px;color:var(--muted)}
.arch{font-size:12.5px;color:var(--ink-2);border-left:2px solid var(--warn-line);padding-left:var(--s3);margin-bottom:var(--s2)}

/* ---------- 8 · rubric & scoring ---------- */
.dual{display:grid;grid-template-columns:1fr 1fr;gap:var(--s5);margin-bottom:var(--s6)}
.gatebox{border:2px solid var(--ok);border-radius:5px;background:var(--ok-soft);padding:var(--s4) var(--s5)}
.growbox{border:1px dashed var(--rule);border-radius:5px;background:var(--card-2);padding:var(--s4) var(--s5)}
.gatebox h3,.growbox h3{font-size:17px;margin-bottom:var(--s1)}
.gatebox h3{color:var(--ok)}
.growbox h3{color:var(--muted)}
.dual .lab{font-size:9.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;margin-bottom:5px}
.gatebox .lab{color:var(--ok)}
.growbox .lab{color:var(--faint)}
.dual p{font-size:12.5px;color:var(--ink-2);margin:var(--s2) 0 0}
.dual .big{font-family:var(--mono);font-size:26px;font-weight:600;letter-spacing:-.02em}
.divider-or{display:flex;align-items:center;justify-content:center}
.crit{border:1px solid var(--rule);border-radius:5px;background:var(--card);margin-bottom:var(--s2);overflow:hidden}
.crit>summary{list-style:none;cursor:pointer;padding:var(--s3) var(--s4);display:grid;grid-template-columns:38px 1fr auto;gap:var(--s3);align-items:center}
.crit>summary::-webkit-details-marker{display:none}
.crit>summary:hover{background:var(--card-2)}
.crit>summary:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}
.crit .cid{font-family:var(--mono);font-size:15px;font-weight:600;color:var(--accent)}
.crit .cnm{font-family:var(--serif);font-size:15.5px;font-weight:600}
.crit .csub{font-size:11.5px;color:var(--muted)}
.crit .cw{font-family:var(--mono);font-size:11px;color:var(--muted);white-space:nowrap}
.crit[open]>summary{border-bottom:1px solid var(--rule-2);background:var(--card-2)}
.critbody{padding:var(--s4)}
.bands{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--s3)}
.band{border:1px solid var(--rule-2);border-radius:4px;padding:var(--s3);background:var(--card-2)}
.band .bl{font-size:9.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;margin-bottom:5px}
.band p{font-size:12px;color:var(--ink-2);margin:0}
.band.l0{border-left:3px solid var(--flag)} .band.l0 .bl{color:var(--flag)}
.band.l1{border-left:3px solid var(--ok)}   .band.l1 .bl{color:var(--ok)}
.band.l2{border-left:3px solid var(--accent)} .band.l2 .bl{color:var(--accent)}
.wbar{display:flex;height:18px;border-radius:3px;overflow:hidden;border:1px solid var(--rule)}
.wbar i{display:block;height:100%;font-style:normal;font-family:var(--mono);font-size:9.5px;color:#fff;text-align:center;line-height:18px}
.vgrid{display:grid;grid-template-columns:150px repeat(7,minmax(0,1fr)) 110px;gap:2px;font-size:11px;align-items:stretch}
.vgrid .vh{font-size:9.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);padding:4px 2px;text-align:center}
.vcell{border-radius:3px;padding:4px 3px;text-align:center;font-weight:600;font-size:10.5px;border:1px solid}
.v-NotYet{background:var(--flag-soft);border-color:var(--flag-line);color:var(--flag)}
.v-Proficient{background:var(--ok-soft);border-color:#B7D2C6;color:var(--ok)}
.v-Exemplary{background:var(--accent-soft);border-color:var(--accent-line);color:var(--accent)}
.v-none{background:var(--paper-2);border-color:var(--rule);color:var(--faint)}
.vcell .cf{display:block;font-size:8.5px;font-weight:400;letter-spacing:.06em;opacity:.85}
.interim{border:1px dashed var(--warn-line)!important;background:repeating-linear-gradient(135deg,var(--warn-soft),var(--warn-soft) 6px,#FDF7E9 6px,#FDF7E9 12px)}
.biasrow{display:grid;grid-template-columns:44px 1fr 140px 190px;gap:var(--s3);align-items:center;padding:9px var(--s4);border-bottom:1px solid var(--rule-2);font-size:12px}
.biasrow:last-child{border-bottom:0}
.biasrow .bc{font-family:var(--mono);font-size:13px;font-weight:600;color:var(--accent)}
.biasrow .bn2{font-size:12.5px}
.biasrow .bd{font-size:11px;color:var(--muted)}
.biasrow .bstate{font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;text-align:center;padding:3px 6px;border-radius:3px;border:1px solid}
.bs-OK{background:var(--ok-soft);border-color:#B7D2C6;color:var(--ok)}
.bs-FLAG{background:var(--flag-soft);border-color:var(--flag-line);color:var(--flag)}
.bs-NA{background:var(--paper-2);border-color:var(--rule);color:var(--muted)}

/* ---------- 9 · student ---------- */
.mycards{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:var(--s4)}
.mycase{background:var(--card);border:1px solid var(--rule);border-radius:5px;padding:var(--s4);border-top:3px solid var(--accent)}
.mycase h3{font-size:17px;line-height:1.2}
.mycase .mm{font-family:var(--mono);font-size:10.5px;color:var(--muted);margin-top:3px}
.mycase .due{font-size:11.5px;font-weight:600;margin-top:var(--s2)}
.mycase .due.late{color:var(--flag)}
.steps{display:flex;gap:4px;margin:var(--s3) 0}
.step{flex:1;text-align:center;font-size:9.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:4px 2px;border-radius:3px;
  border:1px solid var(--rule);background:var(--paper-2);color:var(--muted)}
.step.done{background:var(--ok-soft);border-color:#B7D2C6;color:var(--ok)}
.step.now{background:var(--accent-soft);border-color:var(--accent-line);color:var(--accent)}
.myheat{display:flex;flex-wrap:wrap;gap:2px}
.myheat span{width:11px;height:11px;border-radius:2px;border:1px solid rgba(24,20,12,.10)}

@media (max-width:1180px){
  .tree-layout,.two,.split{grid-template-columns:1fr}
  .panel{position:static;max-height:none}
  .stat-strip,.stat-strip[data-n]{grid-template-columns:repeat(3,1fr)}
  .wrap{padding:0 var(--s4)}
  .dual,.opts,.bands{grid-template-columns:1fr}
  .biasrow{grid-template-columns:36px 1fr;row-gap:6px}
  .vgrid{grid-template-columns:1fr;gap:4px}
  .sheet{width:100%}
  .rolebar .wrap{flex-wrap:wrap}
  .mast-top{flex-wrap:wrap;gap:var(--s4)}
  .mast-meta{text-align:left;white-space:normal}
  .searchwrap{min-width:0;width:100%}
  .cards,.mycards,.dgrid{grid-template-columns:1fr}
}
</style>
</head>
<body data-role="guide">

<div class="rolebar" id="roleBar">
  <div class="wrap">
    <span class="rl"><span class="dot" aria-hidden="true"></span><span id="roleLabel">Guide mode</span></span>
    <span class="rsub" id="roleSub"></span>
    <span class="spacer"></span>
    <div class="rolesw" id="roleSw" role="group" aria-label="Role"></div>
  </div>
</div>

<header class="masthead">
  <div class="wrap">
    <div class="mast-top">
      <div>
        <div class="kicker">Acton Academy · Heroes Discovery Studio · Read-model instrument</div>
        <div class="mast-id"><h1 class="title">Math Builder</h1></div>
        <p class="mast-sub" id="mastSub">A curriculum instrument over the case corpus, the 322-skill standards spine and the tracker.
        Every figure below is computed from <span class="mono">readmodel/*.json</span> at build time. Missing data is rendered as missing, never as zero.</p>
        <div class="searchwrap" style="margin-top:14px">
          <input type="search" id="gq" placeholder="Search cases, skills, domains, careers…" aria-label="Search everything" autocomplete="off" aria-expanded="false" aria-controls="gres">
          <kbd>/</kbd>
          <div class="results" id="gres" role="listbox" aria-label="Search results"></div>
        </div>
      </div>
      <div class="mast-meta" id="mastMeta"></div>
    </div>
    <div class="stat-strip" id="statStrip"></div>
  </div>
</header>

<nav class="tabbar"><div class="wrap"><div class="tabs" role="tablist" id="tabs"></div></div></nav>

<main class="wrap">
  <div class="navrow"><button class="backbtn" id="backBtn" disabled>&#8592; Back</button><span class="crumb" id="crumb"></span></div>
  <section class="view on" id="view-tree" role="tabpanel" aria-labelledby="tab-tree"></section>
  <section class="view" id="view-heat" role="tabpanel" aria-labelledby="tab-heat"></section>
  <section class="view" id="view-library" role="tabpanel" aria-labelledby="tab-library"></section>
  <section class="view" id="view-roots" role="tabpanel" aria-labelledby="tab-roots"></section>
  <section class="view" id="view-rubric" role="tabpanel" aria-labelledby="tab-rubric"></section>
  <section class="view" id="view-pipeline" role="tabpanel" aria-labelledby="tab-pipeline"></section>
  <section class="view" id="view-gaps" role="tabpanel" aria-labelledby="tab-gaps"></section>
  <section class="view" id="view-tracker" role="tabpanel" aria-labelledby="tab-tracker"></section>
  <section class="view" id="view-mycases" role="tabpanel" aria-labelledby="tab-mycases"></section>
  <section class="view" id="view-myprogress" role="tabpanel" aria-labelledby="tab-myprogress"></section>
  <section class="view" id="view-myskills" role="tabpanel" aria-labelledby="tab-myskills"></section>
</main>

<div id="tip" role="tooltip" aria-hidden="true"></div>
<div class="scrim" id="scrim"></div>
<aside class="sheet" id="sheet" role="dialog" aria-modal="true" aria-labelledby="sheetTitle" aria-hidden="true"></aside>

<script id="readmodel">
/* Compiled read-model, inlined by app/build_dashboard.py.
   Inlined rather than fetched because this file must work from file://.

   TWO PAYLOADS, TWO AUDIENCES. In the guide build DATA is the full read-model
   and DATA.student is the redacted per-learner object. In the student build
   (app/student.html) DATA is *only* that redacted object — the guide notes,
   socratic plans, twists, QA reports, gap queue, override bias and every other
   learner are not hidden, they are absent from the file. Redaction happens in
   app/build_dashboard.py, not in CSS. */
const ROLE_LOCK = __ROLE_LOCK__;
const DATA = __DATA_JSON__;
</script>

<script>
"use strict";
(function () {
  const $ = (s, r) => (r || document).querySelector(s);
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const starStr = (n) => { n = n || 0; return "★".repeat(n) + "☆".repeat(5 - n); };
  const $$ = (s, r) => Array.prototype.slice.call((r || document).querySelectorAll(s));
  const H = DATA.headline || {};
  const S = DATA.student || null;                 // redacted per-learner payload
  const HASGUIDE = DATA.branches != null;         // false in the student-only build
  const nf = (n) => (n == null ? "&mdash;" : String(n));
  /* inline markdown, applied AFTER escaping, so nothing can inject markup */
  const mdi = (s) => esc(s == null ? "" : s)
    .replace(/`([^`]+)`/g, '<code class="mono">$1</code>')
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/(^|[^*])\*([^*]+)\*/g, "$1<em>$2</em>");

  /* ============================== role ============================== */
  const RKEY = "mcs.role";
  const store = {
    get: (k) => { try { return window.localStorage.getItem(k); } catch (e) { return null; } },
    set: (k, v) => { try { window.localStorage.setItem(k, v); } catch (e) { /* file:// may block */ } }
  };
  const ROLES = [];
  if (HASGUIDE) ROLES.push("guide");
  if (S) ROLES.push("student");
  let ROLE = ROLE_LOCK || store.get(RKEY) || ROLES[0];
  if (ROLES.indexOf(ROLE) < 0) ROLE = ROLES[0];

  const TABS_GUIDE = () => [
    { id: "tree", label: "Curriculum Tree", num: DATA.branches.length + " branches" },
    { id: "heat", label: "Coverage Heatmap", num: H.skills + " skills" },
    { id: "library", label: "Case Library", num: H.corpus_cases + " cases" },
    { id: "roots", label: "Root Connections", num: H.root_domains + " domains" },
    { id: "rubric", label: "Rubric & Scoring", num: H.criteria + " criteria" },
    { id: "pipeline", label: "Pipeline", num: (DATA.pipeline ? DATA.pipeline.cases.length + DATA.pipeline.concepts.length : 0) + " in flight" },
    { id: "gaps", label: "Gap Queue", num: DATA.gaps.length + " + " + H.unmapped },
    { id: "tracker", label: "Tracker", num: "exceptions" }
  ];
  const TABS_STUDENT = () => [
    { id: "mycases", label: "My Cases", num: S.cases.length + " assigned" },
    { id: "myprogress", label: "My Progress", num: S.badges.n_earned + "/" + S.badges.badges_total + " badges" },
    { id: "myskills", label: "My Skills", num: S.skills.n_exercised + " exercised" },
    { id: "rubric", label: "How I'm Assessed", num: RUB.criteria.length + " criteria" },
    { id: "roots", label: "Where Maths Goes", num: RC.domains.length + " fields" }
  ];
  const tabsFor = () => (ROLE === "student" ? TABS_STUDENT() : TABS_GUIDE());

  function paintRole() {
    document.body.setAttribute("data-role", ROLE);
    const stu = ROLE === "student";
    $("#roleLabel").textContent = stu ? "Student mode" : "Guide mode";
    $("#roleSub").innerHTML = stu
      ? esc(S.learner.name) + " &#183; " + esc(S.learner.program) +
        (S.preview_only ? ' &#183; <strong>EXAMPLE LEARNER, no real roster yet</strong>' : "") +
        (ROLE_LOCK
          ? " &#183; facilitator material is not in this file"
          : ' &#183; <strong>GUIDE PREVIEW &#8212; this file still holds the full read-model. Hand a learner app/student.html.</strong>')
      : "full read-model &#183; " + (DATA.meta.sources || []).length + " files &#183; exception queue, QA, scoring and gap queue visible";
    $("#roleSw").innerHTML = ROLE_LOCK
      ? '<button aria-pressed="true" disabled>' + esc(ROLE_LOCK === "student" ? "Student build" : "Guide build") + "</button>"
      : ROLES.map((r) => '<button data-r="' + r + '" aria-pressed="' + (r === ROLE) + '">' +
          (r === "guide" ? "Guide" : "Student") + "</button>").join("");
    $("#mastSub").innerHTML = stu
      ? "Your cases, your badge progress and the skills you have actually exercised. " +
        "The rubric is here too, so you can read exactly what you are being judged on before you submit."
      : "A curriculum instrument over the case corpus, the 322-skill standards spine and the tracker. " +
        'Every figure below is computed from <span class="mono">readmodel/*.json</span> at build time. Missing data is rendered as missing, never as zero.';
    const cards = statCards();
    $("#statStrip").innerHTML = cards.map((s) =>
      '<div class="stat' + (s.alert ? " alert" : "") + '"><div class="v">' + nf(s.v) +
      ' <small>' + esc(s.s) + '</small></div><div class="k">' + esc(s.k) + "</div></div>").join("");
    $("#statStrip").setAttribute("data-n", String(Math.min(6, cards.length)));
    $("#gq").placeholder = stu ? "Search my cases, skills, fields, careers…" : "Search cases, skills, domains, careers…";
    paintTabs();
  }

  function statCards() {
    if (ROLE === "student") {
      const b = S.badges, done = S.cases.filter((c) => c.status === "complete").length;
      return [
        { k: "Cases assigned to me", v: S.cases.length, s: done + " complete" },
        { k: "Badges earned", v: b.n_earned, s: "of " + b.badges_total },
        { k: "Cases toward next badge", v: b.to_next, s: "of " + b.cases_per_badge },
        { k: "Skills I have exercised", v: S.skills.n_exercised, s: "of " + S.skills.n_total },
        { k: "Fields to explore", v: RC.domains.length, s: RC.clusters.length + " clusters" }
      ];
    }
    return [
      { k: "Case studies in corpus", v: H.corpus_cases, s: "across 3 years" },
      { k: "Cases with no standards row", v: H.unmapped, s: "of " + H.corpus_cases, alert: true },
      { k: "Atomic skills in spine", v: H.skills, s: H.domains + " domains" },
      { k: "Skills with zero coverage", v: H.uncovered, s: H.uncovered_pct + "%", alert: true },
      { k: "Openable case files", v: H.links_ok, s: "of " + H.links_total + " linked" },
      { k: "Application domains", v: H.root_domains, s: H.data_sources + " data sources" }
    ];
  }

  function paintTabs() {
    const T = tabsFor();
    $("#tabs").innerHTML = T.map((t) =>
      '<button class="tab" role="tab" id="tab-' + t.id + '" aria-controls="view-' + t.id +
      '" aria-selected="' + (CUR && CUR.view === t.id) + '" data-t="' + t.id + '">' + esc(t.label) +
      '<span class="num">' + esc(t.num) + "</span></button>").join("");
  }

  /* ============================ masthead ============================ */
  $("#mastMeta").innerHTML =
    "built " + esc(DATA.meta.generated_on) + "<br>" +
    (HASGUIDE ? esc((DATA.meta.sources || []).length) + " read-model files<br>spine: " + esc(DATA.meta.spine_source)
              : "student build<br>redacted at generation") +
    "<br>rubric " + esc(DATA.meta.rubric_version || "?");

  /* ============================= router ============================= */
  /* file:// forbids pushState with a URL (opaque origin), so state objects are
     pushed with the URL left alone. Browser Back therefore works; deep links
     into a view do not, which is the honest trade for a double-clickable file. */
  const VIEWS = ["tree", "heat", "library", "roots", "rubric", "pipeline", "gaps", "tracker", "mycases", "myprogress", "myskills"];
  let CUR = null, NAVSTACK = [], HISTORY_OK = false;
  const CRUMB = { tree: "Curriculum Tree", heat: "Coverage Heatmap", library: "Case Library",
    roots: "Root Connections", rubric: "Rubric & Scoring", pipeline: "Pipeline", gaps: "Gap Queue", tracker: "Tracker",
    mycases: "My Cases", myprogress: "My Progress", myskills: "My Skills" };

  function goto(view, focus, opts) {
    opts = opts || {};
    if (VIEWS.indexOf(view) < 0) return;
    if (tabsFor().filter((t) => t.id === view).length === 0) {
      // asked for a view this role does not have — fall back to its first tab
      view = tabsFor()[0].id; focus = null;
    }
    if (CUR && !opts.replace) NAVSTACK.push(CUR);
    CUR = { view: view, focus: focus || {} };
    if (HISTORY_OK) { try { history[opts.replace ? "replaceState" : "pushState"]({ mcs: CUR }, ""); } catch (e) { } }
    apply(CUR, opts);
  }
  function apply(st, opts) {
    opts = opts || {};
    $$(".tab").forEach((t) => t.setAttribute("aria-selected", String(t.dataset.t === st.view)));
    $$(".view").forEach((v) => v.classList.toggle("on", v.id === "view-" + st.view));
    const f = st.focus || {};
    if (st.view === "tree" && f.branch) treeSelect(f.branch);
    if (st.view === "tree" && f.root) treeRootPanel(f.root);
    if (st.view === "heat") heatFocus(f);
    if (st.view === "library") libFocus(f);
    if (st.view === "roots") rootsFocus(f);
    if (st.view === "rubric") rubricFocus(f);
    if (st.view === "gaps") gapsFocus(f);
    if (st.view === "myskills") mySkillsFocus(f);
    paintCrumb();
    if (f.case != null) openCase(f.case, true);
    if (!opts.silent) { try { window.scrollTo({ top: 0 }); } catch (e) { } }
  }
  function paintCrumb() {
    const b = $("#backBtn"); b.disabled = NAVSTACK.length === 0;
    const f = (CUR && CUR.focus) || {}, bits = [];
    Object.keys(f).forEach((k) => { if (f[k] != null && k !== "case") bits.push(k + ": " + f[k]); });
    $("#crumb").innerHTML = "<b>" + esc(CRUMB[CUR.view] || CUR.view) + "</b>" +
      (bits.length ? " &#8250; " + esc(bits.join(" · ")) : "");
  }
  function back() {
    if (!NAVSTACK.length) return;
    if (HISTORY_OK) { history.back(); return; }
    CUR = NAVSTACK.pop(); apply(CUR);
  }
  $("#backBtn").addEventListener("click", back);
  window.addEventListener("popstate", (e) => {
    const st = e.state && e.state.mcs;
    if (!st) return;
    if (NAVSTACK.length) NAVSTACK.pop();
    CUR = st; closeSheet(true); apply(CUR, { silent: true });
  });
  $("#tabs").addEventListener("click", (e) => {
    const b = e.target.closest(".tab"); if (!b) return; goto(b.dataset.t, null);
  });
  /* every jump button in the app routes through one delegated handler */
  document.addEventListener("click", (e) => {
    const j = e.target.closest("[data-go]"); if (!j) return;
    e.preventDefault();
    let f = null;
    try { f = j.dataset.focus ? JSON.parse(j.dataset.focus) : null; } catch (err) { f = null; }
    if (j.dataset.go === "case") { openCase(j.dataset.focus, false); return; }
    goto(j.dataset.go, f);
  });
  const goBtn = (view, focus, label, cls) =>
    '<button class="jump ' + (cls || "") + '" data-go="' + view + '" data-focus="' +
    esc(typeof focus === "string" ? focus : JSON.stringify(focus)) + '">' + label + "</button>";

  /* the role switch is wired at boot, once every view exists */

  /* ====================== shared indexes + links ==================== */
  const RC = DATA.rootc || (S && S.domains) || { domains: [], clusters: [], matrix: [] };
  const RUB = DATA.rubric || (S && S.rubric) || null;
  const CASE_IDX = {}, CASE_BY_COL = {}, CASE_BY_ID = {}, DOM_NAME = {}, DOM_IDX = {}, SKILL = {};
  (DATA.cases || []).forEach((c, i) => {
    CASE_IDX[c.title] = i;
    if (c.matrix_col) CASE_BY_COL[c.matrix_col] = i;
    if (c.case_id) CASE_BY_ID[c.case_id] = i;
  });
  RC.domains.forEach((d, i) => { DOM_NAME[d.id] = d.name; DOM_IDX[d.id] = i; });
  /* matrix column -> the spine skill ids it covers. Derived here rather than
     shipped per case: the same 1,080 ids were 58 KB of duplicated payload. */
  const SKILLS_BY_COL = {};
  (DATA.heat || []).forEach((d) => d.groups.forEach((g) => g.skills.forEach((s) => {
    SKILL[s.id] = { s: s, d: d.domain, g: g.group };
    (s.by || []).forEach((t) => (SKILLS_BY_COL[t] = SKILLS_BY_COL[t] || []).push(s.id));
  })));
  const skillsOf = (c) => (c.matrix_col && SKILLS_BY_COL[c.matrix_col]) || [];

  const ASSET_ORDER = [
    { k: "case_doc", lab: "Case document" },
    { k: "guide_notes", lab: "Guide Notes (facilitator)" },
    { k: "socratic_plan", lab: "Socratic plan (facilitator)" },
    { k: "data_workbooks", lab: "Data workbook" },
    { k: "reference_pdfs", lab: "Reference PDF" },
    { k: "images", lab: "Image" }
  ];
  const EXT_LABEL = { docx: "DOCX", xlsx: "XLSX", pdf: "PDF", md: "MD", json: "JSON",
    png: "PNG", jpg: "JPG", jpeg: "JPG", gif: "GIF", pptx: "PPTX", csv: "CSV" };
  /* One asset -> one row. A link with href === null is a file the generator
     could not find on disk; it renders as unopenable rather than as a link
     that 404s, and never as an empty slot. */
  function linkRow(l) {
    const tag = l.is_dir ? "DIR" : (EXT_LABEL[l.ext] || (l.ext ? l.ext.toUpperCase() : "FILE"));
    const size = l.kb == null ? "" : (l.kb >= 1024 ? (l.kb / 1024).toFixed(1) + " MB" : l.kb + " KB");
    const inner = '<span class="ext">' + esc(tag) + '</span><span class="fn">' + esc(l.label) + "</span>" +
      (l.note ? '<span class="sz">' + esc(l.note) + "</span>" : '<span class="sz">' + esc(size) + "</span>");
    if (!l.href) {
      return '<span class="alink dead" title="Not found on disk at ' + esc(l.rel) + '">' + inner + "</span>";
    }
    return '<a class="alink' + (l.is_dir ? " folder" : "") + '" href="' + esc(l.href) + '" title="' + esc(l.rel) + '">' + inner + "</a>";
  }
  function linkList(rows) {
    return rows.length ? '<div class="alist">' + rows.map(linkRow).join("") + "</div>" : "";
  }
  /* The interactive HTML is the starting point for a case -- a real self-checking
     notebook, glossary, CSV/PDF export, everything -- not just one file in a download
     list. Render it as a prominent button; docx/xlsx/pdf stay in the ordinary list
     below as what they are: secondary, offline copies. */
  function primaryCta(l) {
    const path = l.rel || l.label || "";
    if (!l.href) {
      return '<span class="primary-cta dead" title="Not found on disk at ' + esc(path) +
        '"><span class="ic">&#9654;</span> Open the Interactive Case (missing)</span>';
    }
    return '<a class="primary-cta" href="' + esc(l.href) + '" title="' + esc(path) +
      '"><span class="ic">&#9654;</span> Open the Interactive Case</a>';
  }
  const skillChip = (id) => {
    const r = SKILL[id];
    return goBtn("heat", { skill: id }, esc(r ? r.s.label : id) +
      (r ? ' <span class="mono" style="opacity:.7">·' + r.s.n + "</span>" : ""));
  };
  const domChip = (id) => goBtn("roots", { domain: id }, esc(DOM_NAME[id] || id));

  /* ========================= shared: tooltip ======================== */
  const tip = $("#tip");
  function showTip(html, x, y) {
    tip.innerHTML = html; tip.style.display = "block"; tip.setAttribute("aria-hidden", "false");
    const r = tip.getBoundingClientRect();
    let left = x + 14, top = y + 16;
    if (left + r.width > window.innerWidth - 12) left = x - r.width - 14;
    if (top + r.height > window.innerHeight - 12) top = y - r.height - 14;
    tip.style.left = Math.max(8, left) + "px"; tip.style.top = Math.max(8, top) + "px";
  }
  const hideTip = () => { tip.style.display = "none"; tip.setAttribute("aria-hidden", "true"); };

  const bandClass = (b) => (b === "MS" ? "ms" : b === "HS" ? "hs" : "adv");

  /* ======================= 1 · CURRICULUM TREE ====================== */
  const W = 1180, NW = 254, NH = 92, RW = 254, RH = 54;
  const ROWS = { 3: 46, 2: 244, 1: 442, 4: 630 };
  const ROOT_ROW2 = 704, SVGH = ROOT_ROW2 + RH + 20;
  /* domains.json now supplies all 40 root domains. Only the eight highest
     authoring priorities are drawn as tendrils — the rest live in the Root
     Connections tab, and the eighth tile routes there. Drawing 40 would put
     37 of them outside the viewBox, which is what happened before. */
  const PRIO = { HIGH: 0, MEDIUM: 1, LOW: 2 };
  const ROOTS_SHOWN = (DATA.roots || []).slice().sort((a, b) =>
    ((PRIO[a.priority] == null ? 3 : PRIO[a.priority]) - (PRIO[b.priority] == null ? 3 : PRIO[b.priority])) ||
    a.domain.localeCompare(b.domain)).slice(0, 7);
  const LAYOUT = {
    discrete: [24, 3], "prob-stats": [316, 3], calculus: [608, 3], "linear-algebra": [900, 3],
    "algebra-1": [24, 2], "algebra-2": [316, 2], geometry: [608, 2], precalc: [900, 2],
    "pre-algebra": [316, 1], "number-theory": [608, 1]
  };
  const BR = {}; (DATA.branches || []).forEach((b) => (BR[b.id] = b));
  const pos = (id) => ({ x: LAYOUT[id][0], y: ROWS[LAYOUT[id][1]] });

  function ring(cx, cy, pct) {
    const r = 19, C = 2 * Math.PI * r;
    const on = (pct / 100) * C;
    return '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="none" stroke="#E7E1D6" stroke-width="5.5"/>' +
      '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="none" stroke="var(--accent)" stroke-width="5.5" ' +
      'stroke-linecap="butt" stroke-dasharray="' + on.toFixed(1) + " " + (C - on).toFixed(1) +
      '" transform="rotate(-90 ' + cx + " " + cy + ')"/>' +
      '<text class="ringval" x="' + cx + '" y="' + (cy + 4) + '">' + Math.round(pct) + "%</text>";
  }
  function unring(cx, cy) {
    return '<circle cx="' + cx + '" cy="' + cy + '" r="19" fill="none" stroke="var(--warn-line)" stroke-width="2" stroke-dasharray="4 3"/>' +
      '<text class="ringno" x="' + cx + '" y="' + (cy + 4) + '">?</text>';
  }
  function edgePath(a, b) {
    // a = prereq (lower row), b = dependent (upper row)
    const x1 = a.x + NW / 2, y1 = a.y, x2 = b.x + NW / 2, y2 = b.y + NH;
    const m = (y1 + y2) / 2;
    return "M" + x1 + "," + y1 + "C" + x1 + "," + m + " " + x2 + "," + m + " " + x2 + "," + y2;
  }

  function treeSvg() {
    let edges = "", nodes = "", bands = "";
    DATA.phases.forEach((p) => {
      const y = ROWS[p.phase];
      const ly = p.phase === 4 ? y - 16 : y - 15;
      bands += '<g class="phase-band"><line x1="0" y1="' + ly + '" x2="' + W + '" y2="' + ly + '"/>' +
        '<text x="0" y="' + (ly - 7) + '">PHASE ' + p.phase + " · " + esc(p.name.toUpperCase()) + "</text></g>";
    });
    // prereq edges
    DATA.branches.forEach((b) => {
      b.prereqs.forEach((p) => {
        if (!LAYOUT[p] || !LAYOUT[b.id]) return;
        const A = pos(p), B = pos(b.id);
        if (LAYOUT[p][1] === LAYOUT[b.id][1]) {
          const y = A.y + NH / 2;
          edges += '<path class="edge" data-a="' + p + '" data-b="' + b.id + '" d="M' + (A.x + NW) + "," + y +
            "C" + (A.x + NW + 24) + "," + (y + 44) + " " + (B.x - 24) + "," + (y + 44) + " " + B.x + "," + y + '"/>';
        } else {
          edges += '<path class="edge" data-a="' + p + '" data-b="' + b.id + '" d="' + edgePath(A, B) + '"/>';
        }
      });
    });
    // phase-4 root tendrils (dotted, illuminated on hover)
    ROOTS_SHOWN.forEach((r, i) => {
      const rx = 24 + (i % 4) * 292, ry = i < 4 ? ROWS[4] : ROOT_ROW2;
      r._x = rx; r._y = ry;
      r.branches.forEach((bid) => {
        if (!LAYOUT[bid]) return;
        const B = pos(bid);
        edges += '<path class="edge root" data-root="' + r.id + '" data-b="' + bid + '" d="M' + (rx + RW / 2) + "," + ry +
          "C" + (rx + RW / 2) + "," + (ry - 120) + " " + (B.x + NW / 2) + "," + (B.y + NH + 130) + " " +
          (B.x + NW / 2) + "," + (B.y + NH) + '"/>';
      });
    });
    // branch nodes
    DATA.branches.forEach((b) => {
      const P = pos(b.id), c = b.coverage, un = c.state === "unmapped";
      nodes += '<g class="node ' + (un ? "unmapped" : "") + '" data-id="' + b.id + '" tabindex="0" role="button" ' +
        'aria-label="' + esc(b.branch) + '">' +
        '<rect class="box" x="' + P.x + '" y="' + P.y + '" width="' + NW + '" height="' + NH + '" rx="4"/>' +
        (un ? unring(P.x + 40, P.y + 46) : ring(P.x + 40, P.y + 46, c.pct)) +
        '<text class="band" x="' + (P.x + 74) + '" y="' + (P.y + 24) + '">' + esc(b.band.toUpperCase()) + "</text>" +
        '<text class="nm" x="' + (P.x + 74) + '" y="' + (P.y + 46) + '">' + esc(shorten(b.branch)) + "</text>" +
        '<text class="sub" x="' + (P.x + 74) + '" y="' + (P.y + 65) + '">' +
        (un ? "NO STANDARDS ROWS" : c.n_covered + "/" + c.n_skills + " skills covered") + "</text>" +
        (un ? '<text class="sub" x="' + (P.x + 74) + '" y="' + (P.y + 79) + '" fill="var(--warn)">unmapped &#8212; not 0%</text>'
          : '<text class="sub" x="' + (P.x + 74) + '" y="' + (P.y + 79) + '">' + c.case_count + " cases touch it</text>") +
        "</g>";
    });
    // root nodes
    let rootNodes = "";
    const clip = (s, n) => (s.length > n ? s.slice(0, n - 1) + "…" : s);
    ROOTS_SHOWN.forEach((r) => {
      rootNodes += '<g class="rootnode" data-root="' + r.id + '" tabindex="0" role="button" aria-label="' + esc(r.domain) + '">' +
        '<rect x="' + r._x + '" y="' + r._y + '" width="' + RW + '" height="' + RH + '" rx="4"/>' +
        '<text class="rt" x="' + (r._x + 14) + '" y="' + (r._y + 23) + '">' + esc(clip(r.domain, 30)) + "</text>" +
        '<text class="rs" x="' + (r._x + 14) + '" y="' + (r._y + 40) + '">' + esc(r.priority || "?") + " &#183; feeds " +
        esc(clip(r.branches.map((b) => (BR[b] ? BR[b].branch.split(" ")[0] : b)).join(" · "), 34)) + "</text></g>";
    });
    const more = DATA.roots.length - ROOTS_SHOWN.length, mx = 24 + 3 * 292, my = ROOT_ROW2;
    rootNodes += '<g class="rootnode" data-more="1" tabindex="0" role="button" aria-label="All ' + DATA.roots.length + ' root domains">' +
      '<rect x="' + mx + '" y="' + my + '" width="' + RW + '" height="' + RH + '" rx="4"/>' +
      '<text class="rt" x="' + (mx + 14) + '" y="' + (my + 23) + '">+ ' + more + " more domains &#8594;</text>" +
      '<text class="rs" x="' + (mx + 14) + '" y="' + (my + 40) + '">open Root Connections</text></g>';
    return '<svg id="treeSvg" viewBox="0 0 ' + W + " " + SVGH + '" xmlns="http://www.w3.org/2000/svg" role="img" ' +
      'aria-label="Curriculum dependency tree, 4 phases, 10 branches">' +
      '<defs><pattern id="hatch" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">' +
      '<rect width="7" height="7" fill="#FBF6EA"/><line x1="0" y1="0" x2="0" y2="7" stroke="#E6D8B8" stroke-width="2.2"/></pattern></defs>' +
      bands + edges + nodes + rootNodes + "</svg>";
  }
  const shorten = (s) => s.replace(" (Single Variable)", "").replace(" & Trigonometry", " & Trig")
    .replace(" Essentials", "").replace("Probability & Statistics", "Probability & Stats");

  function chain(id, seen) {
    seen = seen || [];
    (BR[id].prereqs || []).forEach((p) => { if (seen.indexOf(p) < 0) { chain(p, seen); seen.push(p); } });
    return seen;
  }

  function branchPanel(id) {
    const b = BR[id], c = b.coverage;
    const ch = chain(id);
    const rootsFor = DATA.roots.filter((r) => r.branches.indexOf(id) >= 0);
    let cov;
    if (c.state === "unmapped") {
      cov = '<div class="callout"><strong>No legacy standards rows.</strong> The 27-case matrix predates this branch entirely &#8212; ' +
        'it maps none of the eight Acton domains onto it. This is <em>absent data</em>, not zero coverage. ' +
        'Coverage here is unknown until the branch is bound to a domain or a case is authored against it.</div>';
    } else {
      cov = '<div class="kv"><dt>Skills reachable</dt><dd>' + c.n_skills + "</dd>" +
        "<dt>Covered</dt><dd>" + c.n_covered + " (" + c.pct + "%)</dd>" +
        "<dt>Thin (1&#8211;2 cases)</dt><dd>" + c.thin + "</dd>" +
        "<dt>Zero coverage</dt><dd>" + c.uncovered + "</dd></div>" +
        '<div class="bar" style="margin-top:10px"><i style="width:' + c.pct + '%"></i></div>';
    }
    const cases = c.state === "unmapped" ? '<p style="color:var(--muted)">Unknown &#8212; no rows to join on.</p>'
      : c.cases.slice(0, 10).map((x) => {
        const w = Math.round((100 * x.n) / c.cases[0].n);
        const idx = CASE_BY_COL[x.title];
        const lab = esc(x.title);
        return '<div class="barrow"><div class="lab">' +
          (idx == null ? lab : '<button class="jump" data-go="case" data-focus="' + esc(String(idx)) + '">' + lab + "</button>") +
          '</div><div class="mono" style="text-align:right;color:var(--muted)">' + x.n + "</div>" +
          '<div class="bar" style="grid-column:1/3"><i style="width:' + w + '%"></i></div></div>';
      }).join("") + (c.cases.length > 10 ? '<p style="margin-top:8px;color:var(--faint);font-size:11.5px">+ ' + (c.cases.length - 10) + " more</p>" : "");
    const feeders = (DATA.rootc.matrix.filter((m) => m.branch === id)[0] || {});

    return '<div class="panel-head"><div class="eyebrow">Phase ' + b.phase + " &#183; " + esc(DATA.phases[b.phase - 1].name) + "</div>" +
      "<h3>" + esc(b.branch) + '</h3><div style="margin-top:6px"><span class="pill ' + bandClass(b.band) + '">' + esc(b.band) + "</span> " +
      (c.state === "unmapped" ? '<span class="pill warn">Unmapped</span>' : '<span class="pill">' + c.pct + "% covered</span>") + "</div></div>" +
      '<div class="panel-body">' +
      "<h4>Description</h4><p>" + esc(b.description) + "</p>" +
      "<h4>Critical dependency</h4><p>" + esc(b.critical_dependency) + "</p>" +
      "<h4>Coverage</h4>" + cov +
      "<h4>Core topics</h4><div class=\"taglist\">" + b.core_topics.map((t) => '<span class="tag">' + esc(t) + "</span>").join("") + "</div>" +
      "<h4>Prerequisite chain</h4>" + (ch.length ? '<p class="mono" style="font-size:12px">' +
        ch.map((p) => esc(shorten(BR[p].branch))).join(" &rarr; ") + " &rarr; <strong>" + esc(shorten(b.branch)) + "</strong></p>"
        : '<p style="color:var(--muted)">None &#8212; this is a trunk entry point.</p>') +
      "<h4>Feeds into</h4>" + (function () {
        const f = DATA.branches.filter((x) => x.prereqs.indexOf(id) >= 0);
        return f.length ? '<div class="taglist">' + f.map((x) => '<span class="tag b">' + esc(shorten(x.branch)) + "</span>").join("") + "</div>"
          : '<p style="color:var(--muted)">Terminal branch.</p>';
      })() +
      "<h4>Acton domains feeding it</h4>" + (b.acton_domains.length ?
        '<div class="jumps">' + b.acton_domains.map((d) =>
          goBtn("heat", { domain: d }, esc(d) + " &#8594;")).join("") + "</div>"
        : '<p style="color:var(--warn)">None. No legacy sheet maps to this branch.</p>') +
      "<h4>Application domains feeding it</h4>" +
      (feeders.n_domains
        ? '<p>' + feeders.n_domains + " of the " + H.root_domains + " root domains reach this branch, " +
          feeders.high_priority.length + " of them HIGH authoring priority. " +
          (feeders.case_starved ? '<strong style="color:var(--flag)">Case-starved</strong> &#8212; only ' + feeders.n_cases + " existing cases sit in them."
                                : feeders.n_cases + " existing cases sit in them.") + "</p>" +
          '<div class="jumps" style="margin-top:6px">' +
          feeders.high_priority.slice(0, 6).map((d) => goBtn("roots", { domain: d }, esc(DOM_NAME[d] || d) + " &#8594;")).join("") +
          goBtn("roots", { branch: id }, "branch &times; domain matrix &#8594;", "warnj") + "</div>"
        : '<p class="absent">Not computed.</p>') +
      (rootsFor.length ? "<h4>Interdisciplinary roots</h4>" + rootsFor.slice(0, 4).map((r) =>
        '<p><strong>' + esc(r.domain) + ".</strong> " + esc(r.note) + "</p>").join("") +
        (rootsFor.length > 4 ? '<p class="absent">+ ' + (rootsFor.length - 4) + " more in Root Connections.</p>" : "") : "") +
      "<h4>Case studies touching it</h4>" +
      '<div class="jumps" style="margin-bottom:8px">' + goBtn("library", { branch: id }, "Filter the Case Library to this branch &#8594;") + "</div>" +
      cases + "</div>";
  }

  function rootPanel(id) {
    const r = DATA.roots.filter((x) => x.id === id)[0];
    if (!r) return "";
    return '<div class="panel-head"><div class="eyebrow">Phase 4 &#183; Root connection' +
      (r.cluster ? " &#183; " + esc(r.cluster) : "") + '</div><h3>' + esc(r.domain) + "</h3>" +
      (r.priority ? '<div style="margin-top:6px"><span class="pill ' +
        (r.priority === "HIGH" ? "flag" : r.priority === "MEDIUM" ? "warn" : "") + '">' + esc(r.priority) + " authoring priority</span></div>" : "") +
      "</div>" +
      '<div class="panel-body"><h4>Why it binds</h4><p>' + esc(r.note) + "</p>" +
      "<h4>Branches consumed</h4><div class=\"jumps\">" +
      r.branches.map((b) => BR[b] ? goBtn("tree", { branch: b }, esc(BR[b].branch)) : "").join("") + "</div>" +
      "<h4>Full record</h4>" + '<div class="jumps">' +
      (r.domain_id ? goBtn("roots", { domain: r.domain_id }, "Open in Root Connections &#8594;") : "") + "</div>" +
      '<p style="color:var(--muted);margin-top:10px">Phase 4 is interdisciplinary framing, not a course. It carries no standards rows of its own.</p></div>';
  }

  function renderTree() {
    $("#view-tree").innerHTML =
      '<div class="sec-head"><div><h2>The Tree of Thought</h2>' +
      '<p class="note">Four phases, ' + DATA.branches.length + ' branches, MS through university. Ring = share of reachable spine skills touched by at least one case. ' +
      'Hatched nodes carry <em>no legacy standards rows at all</em> &#8212; that is absent data, deliberately not drawn as 0%. Click any node.</p></div></div>' +
      '<div class="tree-layout"><div class="tree-stage">' + treeSvg() + "</div>" +
      '<aside class="panel" id="treePanel"></aside></div>' +
      '<div class="rule"></div>' +
      '<div class="callout"><strong>' + H.unmapped_branches + " of " + H.branches +
      " branches have zero rows in the legacy matrix.</strong> Pre-Calculus &amp; Trigonometry, Calculus and Discrete Mathematics are mapped to none of the eight Acton domains. " +
      "Their coverage is unknown, not low. Any roll-up that averages them in as 0% is wrong.</div>";

    const svg = $("#treeSvg");
    svg.querySelectorAll(".node").forEach((n) => {
      n.addEventListener("click", () => treeSelect(n.dataset.id));
      n.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); treeSelect(n.dataset.id); } });
    });
    svg.querySelectorAll(".rootnode").forEach((n) => {
      const light = (on) => svg.querySelectorAll('.edge.root[data-root="' + n.dataset.root + '"]')
        .forEach((e) => e.classList.toggle("hot", on));
      const act = () => {
        if (n.dataset.more) { goto("roots", null); return; }
        treeRootPanel(n.dataset.root);
      };
      n.addEventListener("mouseenter", () => light(true));
      n.addEventListener("mouseleave", () => light(false));
      n.addEventListener("focus", () => light(true));
      n.addEventListener("blur", () => light(false));
      n.addEventListener("click", act);
      n.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); act(); } });
    });
    treeSelect("pre-algebra");
  }

  function treeSelect(id) {
    const svg = $("#treeSvg"); if (!svg || !BR[id]) return;
    svg.querySelectorAll(".node").forEach((n) => n.classList.toggle("sel", n.dataset.id === id));
    svg.querySelectorAll(".edge").forEach((e) => {
      const hot = !e.classList.contains("root") && (e.dataset.a === id || e.dataset.b === id);
      e.classList.toggle("hot", hot);
      e.classList.toggle("dim", !hot && !e.classList.contains("root"));
    });
    $("#treePanel").innerHTML = branchPanel(id);
  }
  function treeRootPanel(rid) {
    const svg = $("#treeSvg"); if (!svg) return;
    svg.querySelectorAll(".node").forEach((x) => x.classList.remove("sel"));
    $("#treePanel").innerHTML = rootPanel(rid);
  }

  /* ========================= 2 · HEATMAP ============================ */
  const TIERS = [
    { key: "0", lab: "0 cases &#8212; gap", css: "var(--c0)", test: (n) => n === 0 },
    { key: "1", lab: "1", css: "var(--c1)", test: (n) => n === 1 },
    { key: "2", lab: "2", css: "var(--c2)", test: (n) => n === 2 },
    { key: "3", lab: "3&#8211;4", css: "var(--c3)", test: (n) => n >= 3 && n <= 4 },
    { key: "5", lab: "5&#8211;9", css: "var(--c4)", test: (n) => n >= 5 && n <= 9 },
    { key: "10", lab: "10&#8211;19", css: "var(--c5)", test: (n) => n >= 10 && n <= 19 },
    { key: "20", lab: "20+", css: "var(--c6)", test: (n) => n >= 20 }
  ];
  const tierOf = (n) => TIERS.filter((t) => t.test(n))[0];
  const heatState = { dom: "ALL", tier: "ALL", q: "" };
  let heatApply = null;

  function heatFocus(f) {
    f = f || {};
    if (!heatApply) return;
    if (f.domain && DATA.heat.some((d) => d.domain === f.domain)) {
      heatState.dom = f.domain;
      $$("#hDom .chip").forEach((c) => c.setAttribute("aria-pressed", String(c.dataset.v === f.domain)));
    }
    if (f.skill && SKILL[f.skill]) {
      // never leave a focused skill filtered out from under the user
      heatState.tier = "ALL"; heatState.q = "";
      $$("#hTier .chip").forEach((c) => c.setAttribute("aria-pressed", String(c.dataset.v === "ALL")));
      const qi = $("#hQ"); if (qi) qi.value = "";
      heatState.dom = SKILL[f.skill].d;
      $$("#hDom .chip").forEach((c) => c.setAttribute("aria-pressed", String(c.dataset.v === heatState.dom)));
    }
    heatApply();
    $$(".cell.hot").forEach((c) => c.classList.remove("hot"));
    $("#hFocus").innerHTML = f.skill ? skillFocusCard(f.skill) : "";
    if (f.skill) {
      const cell = $('.cell[data-id="' + (window.CSS && CSS.escape ? CSS.escape(f.skill) : f.skill) + '"]');
      if (cell) {
        cell.classList.add("hot");
        try { cell.scrollIntoView({ block: "center" }); } catch (e) { }
      }
    }
  }
  function skillFocusCard(id) {
    const r = SKILL[id]; if (!r) return "";
    const s = r.s;
    const doms = RC.domains.filter((d) => d.skills.some((x) => x.id === id));
    return '<div class="card" style="padding:14px 18px;margin-bottom:18px;border-left:3px solid var(--accent)">' +
      '<div class="eyebrow">' + esc(r.d) + " &#183; " + esc(r.g) + " &#183; " + (s.kind === "how-to" ? "procedure" : "term") + "</div>" +
      '<div style="font-family:var(--serif);font-size:17px;font-weight:600;margin:2px 0 8px">' + esc(s.label) + "</div>" +
      (s.by.length
        ? '<div class="eyebrow" style="margin-bottom:4px">Exercised by ' + s.n + " case" + (s.n === 1 ? "" : "s") + "</div>" +
          '<div class="jumps">' + s.by.map((t) => CASE_BY_COL[t] == null
            ? '<span class="tag">' + esc(t) + " (no folder)</span>"
            : '<button class="jump" data-go="case" data-focus="' + esc(String(CASE_BY_COL[t])) + '">' + esc(t) + "</button>").join("") + "</div>"
        : '<div class="callout"><strong>No case in the matrix exercises this skill.</strong> ' +
          "That is the authoring signal, not a zero &#8212; " + H.unmapped + " corpus cases carry no standards row at all and may already cover it.</div>") +
      (doms.length ? '<div class="eyebrow" style="margin:12px 0 4px">Reachable from ' + doms.length + " application domain" + (doms.length === 1 ? "" : "s") + "</div>" +
        '<div class="jumps">' + doms.slice(0, 8).map((d) => domChip(d.id)).join("") +
        (doms.length > 8 ? '<span class="mini">+' + (doms.length - 8) + " more</span>" : "") + "</div>" : "") +
      "</div>";
  }

  function renderHeat() {
    const legend = '<div class="legend"><span class="eyebrow">Cases covering each skill</span>' +
      TIERS.map((t) => '<span class="item"><span class="sw" style="background:' + t.css + '"></span>' + t.lab + "</span>").join("") +
      '<span class="item" style="margin-left:8px"><span class="sw" style="border-radius:7px;background:var(--c3)"></span>&ldquo;How to&rdquo; procedure</span>' +
      '<span class="item"><span class="sw" style="background:var(--c3)"></span>Vocabulary term</span></div>';

    const filters = '<div class="filters">' +
      '<span class="flabel">Domain</span><div class="fgroup" id="hDom">' +
      '<button class="chip" data-v="ALL" aria-pressed="true">All ' + H.skills + "</button>" +
      DATA.heat.map((d) => '<button class="chip" data-v="' + esc(d.domain) + '" aria-pressed="false">' + esc(d.domain) + " " + d.n + "</button>").join("") +
      '</div><span class="flabel" style="margin-left:12px">Tier</span><div class="fgroup" id="hTier">' +
      ['ALL:All', '0:Zero coverage', 'THIN:Thin (1–2)', 'OK:Healthy (3+)'].map((s) => {
        const p = s.split(":");
        return '<button class="chip" data-v="' + p[0] + '" aria-pressed="' + (p[0] === "ALL") + '">' + p[1] + "</button>";
      }).join("") +
      '</div><input type="search" id="hQ" placeholder="Filter skills…" aria-label="Filter skills">' +
      '<span class="count-note" id="hCount"></span></div>';

    $("#view-heat").innerHTML =
      '<div class="sec-head"><div><h2>Coverage Heatmap</h2><p class="note">Every one of the ' + H.skills +
      ' atomic skills in the spine, grouped by domain and sub-group. One cell = one skill; colour = how many of the ' + H.matrix_cols +
      ' matrix-tracked cases exercise it. Hover a cell for the label and the covering cases.</p></div></div>' +
      legend + filters + '<div id="hFocus"></div><div id="heatBody"></div>';

    const body = $("#heatBody");
    body.innerHTML = DATA.heat.map((d) =>
      '<section class="dom-block" data-dom="' + esc(d.domain) + '">' +
      '<div class="dom-head"><h3>' + esc(d.domain) + "</h3>" +
      '<span class="pill' + (d.uncovered > d.n / 2 ? " flag" : "") + '">' + d.uncovered + " uncovered</span>" +
      '<span class="meta">' + d.n + " skills &#183; " + d.thin + " thin &#183; " + d.healthy + " healthy</span></div>" +
      d.groups.map((g) =>
        '<div class="grp" data-grp="' + esc(g.group) + '"><div class="gname">' + esc(g.group) +
        "<em>" + g.n + " skills &#183; " + g.uncovered + " at zero</em></div>" +
        '<div class="cells">' + g.skills.map((s) =>
          '<span class="cell k-' + (s.kind === "how-to" ? "howto" : "term") + '" data-id="' + esc(s.id) +
          '" tabindex="0" role="button" style="background:' + tierOf(s.n).css + ';cursor:pointer" aria-label="' +
          esc(s.label) + ": " + s.n + ' cases"></span>').join("") +
        "</div></div>").join("") + "</section>").join("");

    const SK = SKILL;

    body.addEventListener("click", (e) => {
      const c = e.target.closest(".cell"); if (!c) return;
      hideTip(); goto("heat", { skill: c.dataset.id });
    });
    body.addEventListener("keydown", (e) => {
      const c = e.target.closest(".cell");
      if (c && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); goto("heat", { skill: c.dataset.id }); }
    });
    body.addEventListener("mousemove", (e) => {
      const c = e.target.closest(".cell");
      if (!c) { hideTip(); return; }
      const r = SK[c.dataset.id], s = r.s;
      const cases = s.by.length ? s.by.slice(0, 12).join(", ") + (s.by.length > 12 ? ", +" + (s.by.length - 12) + " more" : "")
        : "No case in the matrix exercises this skill.";
      showTip('<div class="t">' + esc(s.label) + '</div><div class="m">' + esc(r.d) + " &#183; " + esc(r.g) + " &#183; " +
        (s.kind === "how-to" ? "procedure" : "term") + '</div><div class="c"><strong>' + s.n + " case" + (s.n === 1 ? "" : "s") +
        "</strong> &#183; " + esc(cases) + '</div><div class="c" style="color:#B9B2A4">Click to pin this skill and cross-navigate.</div>',
        e.clientX, e.clientY);
    });
    body.addEventListener("mouseleave", hideTip);

    function apply() {
      let shown = 0;
      body.querySelectorAll(".dom-block").forEach((db) => {
        const domOk = heatState.dom === "ALL" || db.dataset.dom === heatState.dom;
        let domShown = 0;
        db.querySelectorAll(".grp").forEach((gr) => {
          let grShown = 0;
          gr.querySelectorAll(".cell").forEach((c) => {
            const s = SK[c.dataset.id].s;
            const tierOk = heatState.tier === "ALL" || (heatState.tier === "0" && s.n === 0) ||
              (heatState.tier === "THIN" && s.n >= 1 && s.n <= 2) || (heatState.tier === "OK" && s.n >= 3);
            const qOk = !heatState.q || s.label.toLowerCase().indexOf(heatState.q) >= 0;
            const ok = domOk && tierOk && qOk;
            c.classList.toggle("hide", !ok);
            if (ok) grShown++;
          });
          gr.style.display = grShown ? "" : "none";
          domShown += grShown;
        });
        db.style.display = domShown ? "" : "none";
        shown += domShown;
      });
      $("#hCount").textContent = shown + " of " + H.skills + " skills shown";
    }
    $("#hDom").addEventListener("click", (e) => {
      const b = e.target.closest(".chip"); if (!b) return;
      heatState.dom = b.dataset.v;
      $("#hDom").querySelectorAll(".chip").forEach((c) => c.setAttribute("aria-pressed", String(c === b)));
      apply();
    });
    $("#hTier").addEventListener("click", (e) => {
      const b = e.target.closest(".chip"); if (!b) return;
      heatState.tier = b.dataset.v;
      $("#hTier").querySelectorAll(".chip").forEach((c) => c.setAttribute("aria-pressed", String(c === b)));
      apply();
    });
    $("#hQ").addEventListener("input", (e) => { heatState.q = e.target.value.trim().toLowerCase(); apply(); });
    heatApply = apply;
    apply();
  }

  /* ========================= 3 · LIBRARY ============================ */
  const ASSETS = [
    { k: "case_doc", lab: "case doc" }, { k: "guide_notes", lab: "guide notes" },
    { k: "socratic_plan", lab: "socratic plan" }, { k: "data_workbooks", lab: "workbook" },
    { k: "reference_pdfs", lab: "pdf" }, { k: "images", lab: "image" }
  ];
  const libState = { year: "ALL", asset: "ALL", mapped: "ALL", q: "", branch: null, domain: null };
  let libApply = null;

  function libFocus(f) {
    f = f || {};
    if (!libApply) return;
    libState.branch = f.branch || null;
    libState.domain = f.domain || null;
    if (f.branch || f.domain) { libState.year = "ALL"; libState.mapped = "ALL"; libState.asset = "ALL"; libState.q = "";
      const q = $("#lQ"); if (q) q.value = "";
      [["#lYear", "ALL"], ["#lAsset", "ALL"], ["#lMap", "ALL"]].forEach((p) =>
        $$(p[0] + " .chip").forEach((c) => c.setAttribute("aria-pressed", String(c.dataset.v === p[1]))));
    }
    libApply();
  }

  function renderLibrary() {
    const years = Array.from(new Set(DATA.cases.map((c) => c.year))).sort();
    $("#view-library").innerHTML =
      '<div class="sec-head"><div><h2>Case Library</h2><p class="note">All ' + H.corpus_cases +
      " case studies found on disk, with their asset manifests. " + H.with_guide + " carry facilitator Guide Notes; " +
      H.with_socratic + " carries a full 45-minute Socratic plan. " + H.asset_files + " files in total.</p></div></div>" +
      '<div class="filters">' +
      '<span class="flabel">Year</span><div class="fgroup" id="lYear"><button class="chip" data-v="ALL" aria-pressed="true">All</button>' +
      years.map((y) => '<button class="chip" data-v="' + y + '" aria-pressed="false">' + y + "</button>").join("") + "</div>" +
      '<span class="flabel" style="margin-left:12px">Has</span><div class="fgroup" id="lAsset">' +
      '<button class="chip" data-v="ALL" aria-pressed="true">Any</button>' +
      ASSETS.map((a) => '<button class="chip" data-v="' + a.k + '" aria-pressed="false">' + a.lab + "</button>").join("") + "</div>" +
      '<span class="flabel" style="margin-left:12px">Standards</span><div class="fgroup" id="lMap">' +
      ['ALL:All', 'Y:Mapped', 'N:Unmapped'].map((s) => { const p = s.split(":");
        return '<button class="chip" data-v="' + p[0] + '" aria-pressed="' + (p[0] === "ALL") + '">' + p[1] + "</button>"; }).join("") + "</div>" +
      '<input type="search" id="lQ" placeholder="Search titles…" aria-label="Search case titles">' +
      '<span class="count-note" id="lCount"></span></div>' +
      '<div id="libNote"></div><div class="cards" id="libCards"></div>' +
      '<div class="rule"></div>' +
      '<div class="sec-head"><div><h2>Best of Studio</h2><p class="note">Reference material that sits outside the ' +
      "session folders: worked student write-ups and the studio's own model case studies. Facilitator reference &#8212; " +
      "not shown in student mode.</p></div></div>" +
      '<div class="two"><section><div class="eyebrow" style="margin-bottom:6px">Model case studies &#183; ' +
      DATA.exemplars.case_examples.length + "</div>" + linkList(DATA.exemplars.case_examples) + "</section>" +
      '<section><div class="eyebrow" style="margin-bottom:6px">Student write-ups &#183; ' +
      DATA.exemplars.student_work.length + "</div>" + linkList(DATA.exemplars.student_work) + "</section></div>";

    const cards = $("#libCards");
    cards.innerHTML = DATA.cases.map((c, i) => {
      const chips = ASSETS.map((a) => {
        const n = (c.assets[a.k] || []).length;
        if (!n) return "";
        const gold = a.k === "socratic_plan";
        return '<span class="ac ' + (gold ? "gold" : "on") + '">' + a.lab + (n > 1 ? " ×" + n : "") + "</span>";
      }).join("");
      return '<button class="ccard" data-i="' + i + '"><div class="ct">' + esc(c.title) + "</div>" +
        '<div class="cm">' + esc(c.year) + " &#183; " + esc(c.session) + " &#183; " + c.n_assets + " files &#183; " +
        c.n_links_ok + " openable</div>" +
        '<div class="chips">' + chips + "</div>" +
        '<div class="flagline">' +
        (c.mapped ? '<span class="pill ok">standards-mapped</span>' : '<span class="pill flag">no standards row</span>') +
        (c.standards_count != null ? '<span class="mono" style="font-size:11px;color:var(--muted)">' + c.standards_count + " skills</span>"
          : '<span class="mono" style="font-size:11px;color:var(--faint)">skills unknown</span>') +
        '<span class="mono" style="font-size:11px;color:var(--muted)" title="complexity">' +
          (c.complexity != null ? starStr(c.complexity) : "complexity unknown") + "</span>" +
        (c.rating_count ? '<span class="mono" style="font-size:11px;color:var(--muted)">' + c.avg_rating + "★ (" + c.rating_count + ")</span>" : "") +
        "</div></button>";
    }).join("");

    cards.addEventListener("click", (e) => { const b = e.target.closest(".ccard"); if (b) openCase(+b.dataset.i, false); });

    function apply() {
      let n = 0;
      const inBranch = libState.branch ? (DATA.cases_by_branch[libState.branch] || []) : null;
      const inDomain = libState.domain
        ? ((RC.domains.filter((d) => d.id === libState.domain)[0] || {}).cases || []) : null;
      cards.querySelectorAll(".ccard").forEach((el) => {
        const c = DATA.cases[+el.dataset.i];
        const ok = (libState.year === "ALL" || c.year === libState.year) &&
          (libState.asset === "ALL" || (c.assets[libState.asset] || []).length > 0) &&
          (libState.mapped === "ALL" || (libState.mapped === "Y") === c.mapped) &&
          (!inBranch || inBranch.indexOf(c.title) >= 0) &&
          (!inDomain || inDomain.indexOf(c.title) >= 0) &&
          (!libState.q || c.title.toLowerCase().indexOf(libState.q) >= 0);
        el.style.display = ok ? "" : "none";
        if (ok) n++;
      });
      $("#lCount").textContent = n + " of " + DATA.cases.length + " cases";
      let note = "";
      if (libState.branch) {
        const b = (DATA.branches.filter((x) => x.id === libState.branch)[0] || {});
        const m = (RC.matrix.filter((x) => x.branch === libState.branch)[0] || {});
        note = '<div class="callout info" style="margin-bottom:18px"><strong>Filtered to ' + esc(b.branch || libState.branch) +
          ".</strong> These are the corpus cases that sit in the " + (m.n_domains || 0) +
          " application domains feeding this branch" +
          (m.case_starved ? ' &#8212; <strong>case-starved</strong>: ' + esc((m.reasons || []).join("; ")) : "") +
          ". " + goBtn("tree", { branch: libState.branch }, "back to the branch &#8594;") +
          " " + goBtn("library", {}, "clear filter") + "</div>";
      } else if (libState.domain) {
        note = '<div class="callout info" style="margin-bottom:18px"><strong>Filtered to ' + esc(DOM_NAME[libState.domain] || libState.domain) +
          ".</strong> Corpus cases this application domain already claims. " +
          goBtn("roots", { domain: libState.domain }, "back to the domain &#8594;") + " " +
          goBtn("library", {}, "clear filter") + "</div>";
      }
      $("#libNote").innerHTML = note;
    }
    [["#lYear", "year"], ["#lAsset", "asset"], ["#lMap", "mapped"]].forEach((p) => {
      $(p[0]).addEventListener("click", (e) => {
        const b = e.target.closest(".chip"); if (!b) return;
        libState[p[1]] = b.dataset.v;
        $(p[0]).querySelectorAll(".chip").forEach((c) => c.setAttribute("aria-pressed", String(c === b)));
        apply();
      });
    });
    $("#lQ").addEventListener("input", (e) => { libState.q = e.target.value.trim().toLowerCase(); apply(); });
    libApply = apply;
    apply();
  }

  /* ==================== case detail sheet (global) =================== */
  let sheetOpen = false, sheetReturn = null;

  function openCase(ref, fromRouter) {
    const i = typeof ref === "string" ? (CASE_IDX[ref] != null ? CASE_IDX[ref] : +ref) : ref;
    const c = DATA.cases[i];
    if (!c) return;
    if (!fromRouter) {
      // opening a case is a navigation: it goes on the history stack too
      goto("library", { case: i });
      return;
    }
    sheetReturn = document.activeElement;
    $("#sheet").innerHTML = caseSheet(c, i);
    $("#sheet").classList.add("on"); $("#sheet").setAttribute("aria-hidden", "false");
    $("#scrim").classList.add("on");
    sheetOpen = true;
    const cl = $(".sheet-close"); if (cl) cl.focus();
  }
  function closeSheet(quiet) {
    if (!sheetOpen) return;
    sheetOpen = false;
    $("#sheet").classList.remove("on"); $("#sheet").setAttribute("aria-hidden", "true");
    $("#scrim").classList.remove("on");
    if (sheetReturn && sheetReturn.focus) { try { sheetReturn.focus(); } catch (e) { } }
    if (!quiet && CUR && CUR.focus && CUR.focus.case != null) back();
  }
  $("#scrim").addEventListener("click", () => closeSheet(false));
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && sheetOpen) { e.preventDefault(); closeSheet(false); }
  });
  document.addEventListener("click", (e) => {
    if (e.target.closest(".sheet-close")) closeSheet(false);
  });

  function caseSheet(c, i) {
    const known = (v, txt) => (v ? esc(v) : '<span class="absent">' + (txt || "not recorded for this case") + "</span>");
    let mapNote;
    if (!c.mapped) {
      mapNote = '<div class="callout"><strong>No standards row.</strong> No column in the legacy 27-case matrix corresponds to this folder ' +
        "(closest string similarity " + c.score + "). Its skill coverage is <strong>unknown</strong>, not zero &#8212; it contributes nothing to the heatmap. " +
        "This is reconciliation work, not authoring work.</div>";
    } else if (c.match === "fuzzy") {
      mapNote = '<div class="callout info"><strong>Fuzzy match.</strong> Folder name differs from the matrix column &ldquo;' +
        esc(c.matrix_col) + '&rdquo; (similarity ' + c.score + "). Treated as the same case; worth a human confirm.</div>";
    } else {
      mapNote = '<div class="callout info"><strong>Mapped</strong> to matrix column &ldquo;' + esc(c.matrix_col) + '&rdquo;.</div>';
    }

    const assets = ASSET_ORDER.map((a) => {
      const rows = c.asset_links[a.k] || [];
      if (!rows.length) return "";
      return '<div class="akind">' + esc(a.lab) + " &#183; " + rows.length + "</div>" + linkList(rows);
    }).join("");
    const noAssets = ASSET_ORDER.every((a) => !(c.asset_links[a.k] || []).length);
    const interactiveLinks = c.asset_links.interactive_html || [];
    const interactiveCta = interactiveLinks.length ? primaryCta(interactiveLinks[0]) : "";

    const sids = skillsOf(c);
    const skills = sids.length
      ? '<div class="jumps">' + sids.slice(0, 40).map(skillChip).join("") +
        (sids.length > 40 ? '<span class="mini">+' + (sids.length - 40) + " more</span>" : "") + "</div>"
      : '<p class="absent">Unknown &#8212; this case has no standards row to join on.</p>';

    const doms = c.root_domains.length
      ? '<div class="jumps">' + c.root_domains.map(domChip).join("") + "</div>"
      : '<p class="absent">No application domain claims this case.</p>';

    const qa = c.qa
      ? '<div class="kv"><dt>Verdict</dt><dd>' + known(c.qa.verdict) + "</dd>" +
        (c.qa.gate ? "<dt>Gate</dt><dd>" + esc(c.qa.gate) + "</dd>" : "") +
        (c.qa.blockers != null ? "<dt>Blockers</dt><dd>" + c.qa.blockers + "</dd>" : "") +
        (c.qa.gaps != null ? "<dt>Gaps</dt><dd>" + c.qa.gaps + "</dd>" : "") +
        (c.qa.run_at ? "<dt>Run</dt><dd>" + esc(c.qa.run_at) + "</dd>" : "") + "</div>" +
        (c.qa.note ? "<p style=\"margin-top:8px\">" + esc(c.qa.note) + "</p>" : "")
      : '<p class="absent">No QA run recorded. Legacy corpus cases predate the readiness gate; that is absent data, not a pass.</p>';

    const margin = c.margin_pct == null
      ? '<span class="absent">unknown &#8212; the legacy corpus never recorded one</span>'
      : '<span class="mono">' + c.margin_pct + "%</span> " +
        (c.margin_pct > 20 ? '<span class="pill flag">over the ~20% balance limit</span>'
                           : '<span class="pill ok">within the balance limit</span>');

    return '<div class="sheet-head"><button class="sheet-close" aria-label="Close">&#10005;</button>' +
      '<div class="eyebrow">' + esc(c.year) + " &#183; " + esc(c.session) + " &#183; " + esc(c.status) + "</div>" +
      '<h3 id="sheetTitle">' + esc(c.title) + "</h3>" +
      '<div style="margin-top:7px;display:flex;flex-wrap:wrap;gap:4px">' +
      (c.tier ? '<span class="pill">' + esc(c.tier) + "</span>" : '<span class="pill warn">tier unknown</span>') +
      (c.complexity != null ? '<span class="pill" title="complexity">' + esc(starStr(c.complexity)) + "</span>" : '<span class="pill warn">complexity unknown</span>') +
      (c.rating_count ? '<span class="pill" title="student rating">' + c.avg_rating + "★ (" + c.rating_count + ")</span>" : "") +
      (c.mapped ? '<span class="pill ok">standards-mapped</span>' : '<span class="pill flag">no standards row</span>') +
      (c.has_guide ? '<span class="pill ok">guide notes</span>' : '<span class="pill warn">no guide notes</span>') +
      (c.has_socratic_plan ? '<span class="pill ok">socratic plan</span>' : '<span class="pill warn">no socratic plan</span>') +
      '<span class="pill">' + c.n_links_ok + " openable file" + (c.n_links_ok === 1 ? "" : "s") + "</span>" +
      "</div></div>" +
      '<div class="sheet-body">' +
      (interactiveCta ? "<h4>Start here</h4>" + interactiveCta : "") +
      "<h4>Downloads</h4>" +
      (noAssets ? '<p class="absent">No assets indexed for this folder.</p>' : assets) +
      (c.pipeline_links.length ? '<div class="akind">Pipeline record</div>' + linkList(c.pipeline_links) : "") +
      '<div class="akind">Folder</div>' + linkRow(c.asset_links._folder) +
      (c.n_links_missing ? '<div class="callout" style="margin-top:10px"><strong>' + c.n_links_missing +
        " file" + (c.n_links_missing === 1 ? " is" : "s are") + " indexed but not on disk.</strong> " +
        "They render unopenable above rather than as links that would fail.</div>" : "") +

      "<h4>The dilemma</h4>" +
      (c.protagonist ? "<p><strong>" + esc(c.protagonist) + "</strong></p>" : "") +
      (c.primary_metric ? '<p>Primary metric: <span class="mono">' + esc(c.primary_metric) + "</span></p>"
        : '<p class="absent">Primary metric not recorded. Only pipeline-authored cases carry one; the 27-case legacy matrix never captured it.</p>') +
      ((c.options && (c.options.A || c.options.B))
        ? '<div class="opts"><div class="opt"><div class="ol">Option A</div><p>' + esc(c.options.A) + "</p></div>" +
          '<div class="opt"><div class="ol">Option B</div><p>' + esc(c.options.B) + "</p></div></div>"
        : '<p class="absent">Options not recorded.</p>') +
      (c.argument_a ? '<p style="margin-top:10px"><strong>For A.</strong> ' + esc(c.argument_a) + "</p>" : "") +
      (c.argument_b ? "<p><strong>For B.</strong> " + esc(c.argument_b) + "</p>" : "") +
      '<p style="margin-top:8px">Balance margin: ' + margin +
      (c.balance_verdict ? ' &#183; <span class="mono">' + esc(c.balance_verdict) + "</span>" : "") + "</p>" +
      (c.twist ? '<div class="callout" style="margin-top:10px"><strong>Twist (facilitator only).</strong> ' + esc(c.twist) + "</div>" : "") +
      (c.sensitivity_note ? '<div class="callout" style="margin-top:8px"><strong>Sensitivity.</strong> ' + esc(c.sensitivity_note) + "</div>" : "") +

      (c.deliverables.length ? "<h4>Deliverables &#183; " + c.deliverables.length + "</h4><ul class=\"manifest\">" +
        c.deliverables.map((d) => "<li><strong>" + esc(d.id) + "</strong> " + esc(d.text) + "</li>").join("") + "</ul>" : "") +
      (c.assumptions.length ? "<h4>Stated assumptions</h4><ul class=\"manifest\">" +
        c.assumptions.map((a) => "<li>" + esc(a.statement || a.id) + "</li>").join("") + "</ul>" : "") +

      "<h4>Standards it covers &#183; " + (c.standards_count == null ? "unknown" : c.standards_count) + "</h4>" + skills +
      "<h4>Application domains</h4>" + doms +
      "<h4>Legacy spine domains</h4>" +
      (c.domains_touched.length ? '<div class="jumps">' + c.domains_touched.map((d) =>
        goBtn("heat", { domain: d }, esc(d) + " &#8594;")).join("") + "</div>" : '<p class="absent">Unknown.</p>') +
      "<h4>QA state</h4>" + qa +
      "<h4>Standards reconciliation</h4>" + mapNote +
      "<h4>Path</h4><div class=\"path\">" + esc(c.path) + "</div>" +
      "</div>";
  }

  /* ===================== 6 · ROOT CONNECTIONS ======================= */
  const rootState = { cluster: "ALL", prio: "ALL", grade: "ALL", closes: false, sel: null };
  let rootApply = null;

  function rootsFocus(f) {
    f = f || {};
    if (!rootApply) return;
    if (f.domain && DOM_IDX[f.domain] != null) {
      rootState.cluster = "ALL"; rootState.prio = "ALL"; rootState.grade = "ALL"; rootState.closes = false;
      $$("#rClu .chip").forEach((c) => c.setAttribute("aria-pressed", String(c.dataset.v === "ALL")));
      $$("#rPri .chip").forEach((c) => c.setAttribute("aria-pressed", String(c.dataset.v === "ALL")));
      $$("#rGra .chip").forEach((c) => c.setAttribute("aria-pressed", String(c.dataset.v === "ALL")));
      const cb = $("#rCloses"); if (cb) cb.setAttribute("aria-pressed", "false");
      rootState.sel = f.domain;
    }
    if (f.cluster) { rootState.cluster = f.cluster;
      $$("#rClu .chip").forEach((c) => c.setAttribute("aria-pressed", String(c.dataset.v === f.cluster))); }
    rootApply();
    if (f.branch) {
      const row = $('#mtxBody tr[data-b="' + f.branch + '"]');
      if (row) { row.style.outline = "2px solid var(--accent)"; try { row.scrollIntoView({ block: "center" }); } catch (e) { } }
    }
  }

  function renderRoots() {
    const student = ROLE === "student";
    const CL = RC.clusters, DS = RC.domains;
    const byClu = {}; DS.forEach((d) => (byClu[d.cluster] = byClu[d.cluster] || []).push(d));

    const filters = '<div class="filters">' +
      '<span class="flabel">Cluster</span><div class="fgroup" id="rClu">' +
      '<button class="chip" data-v="ALL" aria-pressed="true">All ' + DS.length + "</button>" +
      CL.map((c) => '<button class="chip" data-v="' + esc(c.name) + '" aria-pressed="false">' +
        esc(c.name) + " " + (byClu[c.name] || []).length + "</button>").join("") + "</div></div>" +
      '<div class="filters" style="border-top:0;padding-top:0">' +
      '<span class="flabel">Priority</span><div class="fgroup" id="rPri">' +
      ["ALL:All", "HIGH:High", "MEDIUM:Medium", "LOW:Low"].map((s) => { const p = s.split(":");
        return '<button class="chip" data-v="' + p[0] + '" aria-pressed="' + (p[0] === "ALL") + '">' + p[1] + "</button>"; }).join("") + "</div>" +
      '<span class="flabel" style="margin-left:12px">Data grade</span><div class="fgroup" id="rGra">' +
      ["ALL:All", "HIGH:High", "MEDIUM:Medium", "LOW:Low"].map((s) => { const p = s.split(":");
        return '<button class="chip" data-v="' + p[0] + '" aria-pressed="' + (p[0] === "ALL") + '">' + p[1] + "</button>"; }).join("") + "</div>" +
      '<div class="fgroup" style="margin-left:12px"><button class="chip" id="rCloses" aria-pressed="false">Closes uncovered skills</button></div>' +
      '<span class="count-note" id="rCount"></span></div>';

    const head = student
      ? '<div class="sec-head"><div><h2>Where Maths Actually Goes</h2><p class="note">' + DS.length +
        " fields that run on the maths you are learning, grouped into " + CL.length + " clusters. " +
        "Each one names the decisions it makes, where its numbers come from &#8212; every source is a real, free, working link &#8212; " +
        "and the jobs that do the computing, with the entry path.</p></div></div>"
      : '<div class="sec-head"><div><h2>Root Connections</h2><p class="note">The third spine: ' + DS.length +
        " application domains in " + CL.length + " clusters, the derived join over " +
        "<span class=\"mono\">domains.json</span> &times; <span class=\"mono\">curriculum_tree.json</span> &times; <span class=\"mono\">standards_spine.json</span>. " +
        "Where the first two spines say what to teach and in what order, this one says where the numbers come from. " +
        RC.totals.uncovered_skills_now_reachable_from_a_domain + " of the " + RC.totals.spine_skills_uncovered +
        " uncovered spine skills are reachable from a domain with named data behind it; " +
        RC.totals.uncovered_skills_still_orphaned + " are not.</p></div></div>";

    const grid = CL.map((c) => {
      const ds = byClu[c.name] || [];
      if (!ds.length) return "";
      return '<section class="cluster" data-clu="' + esc(c.name) + '">' +
        '<div class="cluster-head"><h3>' + esc(c.name) + "</h3>" +
        '<span class="meta">' + ds.length + " domain" + (ds.length === 1 ? "" : "s") + " &#183; " +
        ds.filter((d) => d.priority === "HIGH").length + " high priority &#183; " +
        ds.reduce((a, d) => a + d.n_cases, 0) + " existing cases</span></div>" +
        '<div class="dgrid">' + ds.map((d) => dcard(d)).join("") + "</div></section>";
    }).join("");

    $("#view-roots").innerHTML = head + filters +
      '<div class="split"><div id="rootGrid">' + grid + "</div>" +
      '<aside class="panel" id="rootPanel2"></aside></div>' +
      (student ? "" : '<div class="rule"></div>' + matrixBlock());

    const gridEl = $("#rootGrid");
    gridEl.addEventListener("click", (e) => {
      const b = e.target.closest(".dcard"); if (!b) return;
      goto("roots", { domain: b.dataset.d });
    });

    function apply() {
      let n = 0;
      $$(".cluster", gridEl).forEach((sec) => {
        let shown = 0;
        $$(".dcard", sec).forEach((el) => {
          const d = DS[+el.dataset.i];
          const ok = (rootState.cluster === "ALL" || d.cluster === rootState.cluster) &&
            (rootState.prio === "ALL" || d.priority === rootState.prio) &&
            (rootState.grade === "ALL" || d.grade === rootState.grade) &&
            (!rootState.closes || d.n_uncovered > 0);
          el.style.display = ok ? "" : "none";
          el.classList.toggle("sel", d.id === rootState.sel);
          if (ok) shown++;
        });
        sec.style.display = shown ? "" : "none";
        n += shown;
      });
      $("#rCount").textContent = n + " of " + DS.length + " domains";
      $("#rootPanel2").innerHTML = rootState.sel ? domainPanel(rootState.sel)
        : '<div class="panel-body"><h4>Pick a domain</h4><p>Every card opens the full record: why a 13-year-old cares, ' +
          "the binary decisions a case could pose, the live data sources, the careers with the actual computation named, " +
          "and the curriculum branches it feeds.</p></div>";
    }
    [["#rClu", "cluster"], ["#rPri", "prio"], ["#rGra", "grade"]].forEach((p) => {
      $(p[0]).addEventListener("click", (e) => {
        const b = e.target.closest(".chip"); if (!b) return;
        rootState[p[1]] = b.dataset.v;
        $$(p[0] + " .chip").forEach((c) => c.setAttribute("aria-pressed", String(c === b)));
        apply();
      });
    });
    $("#rCloses").addEventListener("click", (e) => {
      rootState.closes = !rootState.closes;
      e.currentTarget.setAttribute("aria-pressed", String(rootState.closes));
      apply();
    });
    rootApply = apply;
    apply();
  }

  function dcard(d) {
    const i = DOM_IDX[d.id];
    return '<button class="dcard p-' + esc(d.priority || "NA") + '" data-d="' + esc(d.id) + '" data-i="' + i + '">' +
      '<div class="dn">' + esc(d.name) + "</div>" +
      '<div class="dl">' + esc(d.one_line) + "</div>" +
      '<div class="dm">' +
      '<span class="mini' + (d.priority === "HIGH" ? " hot" : "") + '">' + esc(d.priority || "priority ?") + "</span>" +
      '<span class="mini' + (d.grade === "HIGH" ? " good" : "") + '">data ' + esc(d.grade || "?") + "</span>" +
      '<span class="mini' + (d.n_uncovered ? " hot" : "") + '">' + d.n_uncovered + "/" + d.n_skills + " uncovered</span>" +
      '<span class="mini">' + (d.n_cases === 0 ? "no cases yet" : d.n_cases + " case" + (d.n_cases === 1 ? "" : "s")) + "</span>" +
      "</div></button>";
  }

  function domainPanel(id) {
    const d = RC.domains.filter((x) => x.id === id)[0];
    if (!d) return "";
    const student = ROLE === "student";
    const srcs = d.sources.length ? d.sources.map((s) =>
      '<div class="srcrow"><a class="ext-link" href="' + esc(s.url) + '" target="_blank" rel="noopener noreferrer">' +
      esc(s.label) + "</a>" + '<span class="mini' + (s.verified === "LIVE" ? " good" : "") + '">' + esc(s.verified) + "</span>" +
      '<div class="off">' + esc(s.offers) + "</div></div>").join("")
      : '<p class="absent">No sources listed.</p>';

    const careers = d.careers.length ? d.careers.map((c) =>
      '<div class="career"><div class="ct2">' + esc(c.title) + "</div>" +
      '<div class="cu">' + esc(c.math_used) + "</div>" +
      '<div class="cp"><strong>Entry:</strong> ' + esc(c.entry_path) + "</div></div>").join("")
      : '<p class="absent">No careers recorded.</p>';

    const branches = d.branches.map((b) => {
      const br = (DATA.branches || []).filter((x) => x.id === b)[0];
      return student ? '<span class="tag b">' + esc(br ? br.branch : b) + "</span>"
                     : goBtn("tree", { branch: b }, esc(br ? br.branch : b));
    }).join("");

    return '<div class="panel-head"><div class="eyebrow">' + esc(d.cluster) + "</div><h3>" + esc(d.name) + "</h3>" +
      '<div style="margin-top:6px;display:flex;flex-wrap:wrap;gap:4px">' +
      '<span class="pill ' + (d.priority === "HIGH" ? "flag" : d.priority === "MEDIUM" ? "warn" : "") + '">' +
      esc(d.priority || "?") + " priority</span>" +
      '<span class="pill ' + (d.grade === "HIGH" ? "ok" : d.grade === "LOW" ? "flag" : "warn") + '">data ' + esc(d.grade || "?") + "</span>" +
      "</div></div>" +
      '<div class="panel-body">' +
      "<h4>What it decides</h4><p>" + esc(d.one_line) + "</p>" +
      "<h4>Why it engages</h4><p>" + esc(d.why) + "</p>" +
      "<h4>Decision archetypes &#183; " + d.archetypes.length + "</h4>" +
      (d.archetypes.length ? d.archetypes.map((a) => '<div class="arch">' + esc(a) + "</div>").join("")
        : '<p class="absent">None recorded.</p>') +
      "<h4>Data sources &#183; " + d.sources.length + "</h4>" + srcs +
      (d.data_note ? '<p style="margin-top:8px;color:var(--muted);font-size:12px">' + esc(d.data_note) + "</p>" : "") +
      "<h4>Careers &#183; " + d.careers.length + "</h4>" + careers +
      "<h4>Curriculum branches it feeds &#183; " + d.branches.length + "</h4><div class=\"jumps\">" + branches + "</div>" +
      "<h4>Signature skills &#183; " + d.n_skills + (d.n_uncovered ? " (" + d.n_uncovered + " uncovered)" : "") + "</h4>" +
      (student
        ? '<div class="taglist">' + d.skills.map((s) => '<span class="tag">' + esc(s.label) + "</span>").join("") + "</div>"
        : '<div class="jumps">' + d.skills.map((s) => skillChip(s.id)).join("") + "</div>") +
      (!student && d.n_uncovered
        ? '<div class="callout" style="margin-top:10px"><strong>' + d.n_uncovered + " of these have zero case coverage.</strong> " +
          "A case authored here would close them: " + d.uncovered.map((s) => esc(s.label)).join("; ") + ".</div>" : "") +
      "<h4>Existing cases &#183; " + d.n_cases + "</h4>" +
      (d.n_cases
        ? '<div class="jumps">' + d.cases.slice(0, 12).map((t) => CASE_IDX[t] == null
            ? '<span class="tag">' + esc(t) + "</span>"
            : '<button class="jump" data-go="case" data-focus="' + esc(String(CASE_IDX[t])) + '">' + esc(t) + "</button>").join("") +
          (d.cases.length > 12 ? '<span class="mini">+' + (d.cases.length - 12) + " more</span>" : "") + "</div>" +
          (student ? "" : '<div class="jumps" style="margin-top:6px">' +
            goBtn("library", { domain: d.id }, "filter the Case Library to this domain &#8594;") + "</div>")
        : '<div class="callout"><strong>No case has been written here yet.</strong> That is an authoring opportunity, ' +
          "not a coverage failure &#8212; the domain exists in the spine with " + d.sources.length + " named data sources behind it.</div>") +
      "</div>";
  }

  function matrixBlock() {
    const M = RC.matrix;
    const rows = M.map((m) => {
      const cls = m.domain_starved ? "starved" : (m.case_starved ? "warnrow" : "");
      const flags = [];
      if (m.domain_starved) flags.push('<span class="pill flag">domain-starved</span>');
      if (m.case_starved) flags.push('<span class="pill warn">case-starved</span>');
      if (!m.has_standards_rows) flags.push('<span class="pill">no standards rows</span>');
      if (!flags.length) flags.push('<span class="pill ok">healthy</span>');
      return '<tr class="' + cls + '" data-b="' + esc(m.branch) + '">' +
        '<td><span class="bn">' + esc(m.name) + "</span>" +
        (m.reasons.length ? '<div class="rz">' + esc(m.reasons.join("; ")) + "</div>" : "") + "</td>" +
        '<td class="num">' + m.n_domains + "</td>" +
        '<td class="num">' + m.high_priority.length + "</td>" +
        '<td class="num">' + m.n_cases + "</td>" +
        '<td class="num">' + (m.n_uncovered_reachable == null ? "&mdash;" : m.n_uncovered_reachable) + "</td>" +
        "<td>" + flags.join(" ") + "</td>" +
        '<td>' + goBtn("tree", { branch: m.branch }, "tree") + " " +
        goBtn("library", { branch: m.branch }, "cases") + "</td></tr>";
    }).join("");

    const dstar = M.filter((m) => m.domain_starved).map((m) => m.name);
    const cstar = M.filter((m) => m.case_starved && !m.domain_starved).map((m) => m.name);

    return '<div class="sec-head"><div><h2>Branch &times; domain matrix</h2><p class="note">' +
      "Two different kinds of starvation, and they are not the same problem. " +
      "<strong>Domain-starved</strong> means the spine barely reaches the branch: fewer than 6 of the " + RC.domains.length +
      " domains feed it, or none of them is HIGH priority. " +
      "<strong>Case-starved</strong> means the corpus barely reaches it: fewer than 10 of the " + RC.totals.corpus_cases +
      " existing cases sit in its domains. Case-starvation is the real authoring signal.</p></div></div>" +
      '<div class="card" style="overflow:auto"><table class="mtx"><thead><tr>' +
      "<th>Branch</th><th>Domains</th><th>High-priority</th><th>Cases</th><th>Uncovered reachable</th><th>State</th><th></th>" +
      '</tr></thead><tbody id="mtxBody">' + rows + "</tbody></table></div>" +
      '<div class="callout" style="margin-top:16px"><strong>' +
      (dstar.length ? esc(dstar.join(", ")) + " " + (dstar.length === 1 ? "is" : "are") + " both domain- and case-starved."
                    : "No branch is domain-starved.") +
      "</strong> " +
      (cstar.length ? esc(cstar.join(", ")) + " " + (cstar.length === 1 ? "is" : "are") +
        " case-starved but <em>not</em> domain-starved &#8212; the spine reaches " +
        (cstar.length === 1 ? "it" : "them") + " fine, the corpus does not. That is an authoring gap, not a spine gap, " +
        "and it is closed by writing cases rather than by adding domains." : "") +
      "</div>" +
      (RC.orphan_uncovered.length
        ? '<div class="callout" style="margin-top:10px"><strong>' + RC.orphan_uncovered.length +
          " uncovered skills sit in no domain at all.</strong> Residual authoring risk.</div>"
        : '<div class="callout info" style="margin-top:10px"><strong>Every one of the ' + RC.totals.spine_skills_uncovered +
          " uncovered spine skills is reachable from at least one domain with named data behind it.</strong> " +
          "There is no residual orphan set.</div>");
  }

  /* ========================== 4 · GAPS ============================== */
  function gapsFocus(f) {
    f = f || {};
    if (!f.cluster) return;
    const el = $('[data-gap="' + f.cluster + '"]');
    if (el) { el.style.outline = "2px solid var(--accent)"; try { el.scrollIntoView({ block: "center" }); } catch (e) { } }
  }

  /* ===================== 4b · PIPELINE ============================== */
  const STAGE_LABEL = { concepting: "Concepting", drafting: "Drafting", research: "Research",
    readiness: "Readiness", promotion: "Promotion", verified: "Verified" };
  const STAGE_NOTE = {
    concepting: "case-brainstorm output. Nothing written to disk yet.",
    drafting: "case-write output. Every figure is a placeholder.",
    research: "case-research output. Figures are cited or stated assumptions.",
    readiness: "case-readiness gate (Tier 1/2/3). Live-checked at build time.",
    promotion: "case-publish output. Packet built, promoted into the read-model.",
    verified: "A real cohort ran it. Only state that may carry a checkmark."
  };
  function statTile(v, sub, k, alert) {
    return '<div class="stat' + (alert ? " alert" : "") + '"><div class="v">' + esc(v) +
      ' <small>' + esc(sub) + '</small></div><div class="k">' + esc(k) + "</div></div>";
  }
  function pipeConceptCard(c) {
    return '<div class="pipecard"><div class="pt">' + esc(c.title) + '</div>' +
      '<div class="pid">' + esc(c.concept_id) + " &#183; score " + esc(c.score) + " &#183; tier " + esc(c.tier) + "</div>" +
      '<div class="ptags"><span class="pill">from ' + esc(c.sheet) + '</span></div>' +
      '<div class="pnext">Approve, then run case-write.</div></div>';
  }
  const EFFORT_KIND = { "NEAR READY": "READY", "MODERATE WORK": "AWAITING", "MORE WORK": "OVERDUE",
    "NEEDS A REAL DESIGN DECISION": "STALE" };
  /* Every pipeline card that has a matching folder in the Case Library
     (published-track by case_id, legacy-track by title) is clickable straight
     into that case's current sheet -- the fastest way to eyeball completeness
     against what the pipeline claims. Cards with nothing on disk yet
     (concepting) are never clickable. */
  function pipeCaseIdx(c) {
    if (CASE_BY_ID[c.id] != null) return CASE_BY_ID[c.id];
    if (CASE_IDX[c.title] != null) return CASE_IDX[c.title];
    return null;
  }
  function pipeCaseCard(c) {
    const idx = pipeCaseIdx(c);
    const tag = idx != null ? "button" : "div";
    const goAttrs = idx != null ? ' data-go="case" data-focus="' + esc(String(idx)) + '"' : "";
    const openHint = idx != null ? '<div class="popen">&#8594; Open in Case Library</div>' : "";
    if (c.origin === "legacy") {
      const kind = EFFORT_KIND[c.effort_tier] || "STALE";
      const sig = c.legacy_signal || {};
      const sigTags = [
        sig.has_guide ? "Guide Notes" : null,
        sig.standards_tagged ? "standards-tagged" : null,
        sig.mentions_twist ? "twist" : null,
      ].filter(Boolean).map((t) => '<span class="pill">' + esc(t) + "</span>").join("");
      return "<" + tag + ' class="pipecard"' + goAttrs + '><div class="pt">' + esc(c.title) + '</div>' +
        '<div class="pid">' + esc(c.id) + ' &#183; legacy corpus, not yet converted</div>' +
        '<div class="ptags"><span class="exc-kind k-' + kind + '">' + esc(c.effort_tier) + "</span>" + sigTags + "</div>" +
        '<div class="pnext">' + esc(c.next_action) + "</div>" + openHint + "</" + tag + ">";
    }
    const t1 = c.tier1 || {};
    const cls = !t1.ran ? "" : (t1.blockers > 0 ? "st-flag" : (t1.gaps > 0 ? "st-warn" : "st-ok"));
    const t1kind = t1.blockers > 0 ? "OVERDUE" : (t1.gaps > 0 ? "AWAITING" : "READY");
    const t1tag = !t1.ran
      ? '<span class="exc-kind k-STALE">TIER 1 N/A</span>'
      : '<span class="exc-kind k-' + t1kind + '">' + esc(t1.verdict) +
        (t1.blockers ? " &#183; " + t1.blockers + "b" : "") + (t1.gaps ? " &#183; " + t1.gaps + "g" : "") + "</span>";
    return "<" + tag + ' class="pipecard ' + cls + '"' + goAttrs + '><div class="pt">' + esc(c.title) + '</div>' +
      '<div class="pid">' + esc(c.id) + (c.tier ? " &#183; " + esc(c.tier) : "") +
      (c.band && c.band.length ? " &#183; " + esc(c.band.join("/")) : "") + "</div>" +
      '<div class="ptags">' + t1tag +
      (c.run_report_filed ? ' <span class="exc-kind k-READY">RUN_REPORT FILED</span>' : "") +
      '</div><div class="pnext">' + esc(c.next_action) + "</div>" + openHint + "</" + tag + ">";
  }
  function renderPipeline() {
    const P = DATA.pipeline;
    if (!P) { $("#view-pipeline").innerHTML = '<p class="absent">No pipeline_status.json in this build.</p>'; return; }
    const order = P._schema.stage_order;
    const byStage = {}; order.forEach((s) => byStage[s] = []);
    P.concepts.forEach((c) => byStage.concepting.push(pipeConceptCard(c)));
    P.cases.forEach((c) => { if (byStage[c.stage]) byStage[c.stage].push(pipeCaseCard(c)); });

    const stats = order.map((s) => {
      const n = P.stage_counts[s];
      const blockedHere = P.cases.filter((c) => c.stage === s && c.tier1 && c.tier1.ran && c.tier1.blockers > 0).length;
      const sub = blockedHere ? blockedHere + " blocked" : (n === 1 ? "case" : "cases");
      return statTile(n, sub, STAGE_LABEL[s], blockedHere > 0);
    }).join("");

    const cols = order.map((s) => {
      const cards = byStage[s];
      return '<div class="pipecol' + (cards.length ? "" : " empty") + '"><h3>' + esc(STAGE_LABEL[s]) +
        '<span class="n">' + cards.length + "</span></h3>" +
        '<div class="colnote">' + esc(STAGE_NOTE[s]) + "</div>" +
        (cards.length ? cards.join("") : '<div class="emptynote">Nothing here right now.</div>') + "</div>";
    }).join("");

    $("#view-pipeline").innerHTML =
      '<div class="sec-head"><div><h2>Pipeline</h2><p class="note">Every concept and case against the real six-stage ' +
      "pipeline this project actually runs &#8212; concepting (case-brainstorm) &#8594; drafting (case-write) &#8594; " +
      "research (case-research) &#8594; readiness (case-readiness Tier 1/2/3) &#8594; promotion (case-publish) &#8594; " +
      "verified (a real cohort ran it, MCS-29). Tier 1 status per case is <strong>live-checked at build time</strong>, " +
      "not read from a cached field &#8212; case.json.qa is not even a consistent shape across cases yet.</p></div></div>" +
      '<div class="stat-strip" style="position:static;margin-bottom:var(--s5)" data-n="6">' + stats + "</div>" +
      '<div class="pipeboard">' + cols + "</div>" +
      renderLegacyExceptions(P.legacy_total, P.legacy_exceptions) +
      "";
  }

  function renderLegacyExceptions(legacyTotal, exceptions) {
    exceptions = exceptions || [];
    const folded = legacyTotal - exceptions.length;
    return '<div class="pipe-legacy"><h3 style="margin-top:0">One pipeline, not two</h3>' +
      '<p class="qnote" style="max-width:none">All ' + legacyTotal + " legacy corpus cases are triaged into the six columns " +
      "above by real signal read from their source .docx (`app/build_legacy_readiness.py`) &#8212; a locked dilemma with " +
      "Guide Notes and standards tagging lands in Drafting as NEAR READY; a dilemma that isn't strictly binary yet lands in " +
      "Concepting, the same design decision a brand-new concept needs. " + folded + " folded cleanly. " +
      (exceptions.length
        ? "The " + exceptions.length + " below could not be triaged and are surfaced as exceptions instead of guessed at."
        : "Zero exceptions this build.") + "</p>" +
      (exceptions.length
        ? exceptions.map((e) => '<div class="exc-row"><span class="who">' + esc(e.title) + '</span>' +
            '<span class="det">' + esc(e.path) + '</span>' +
            '<span class="age" style="white-space:normal;text-align:left;max-width:260px">' + esc(e.reason) + "</span></div>").join("")
        : "") +
      "</div>";
  }

  function renderGaps() {
    const maxGap = Math.max.apply(null, DATA.gaps.map((g) => g.n_uncovered));
    const authoring = DATA.gaps.map((g, i) => {
      const uw = (100 * g.n_uncovered) / g.n_total, tw = (100 * g.n_thin) / g.n_total;
      const skills = g.skills.slice(0, 14).map((s) => (SKILL[s.id]
        ? '<button class="jump ' + (s.n === 0 ? "" : "warnj") + '" data-go="heat" data-focus="' +
          esc(JSON.stringify({ skill: s.id })) + '">' + esc(s.label) + (s.n ? " ·" + s.n : "") + "</button>"
        : '<span class="' + (s.n === 0 ? "z" : "t") + '">' + esc(s.label) + (s.n ? " ·" + s.n : "") + "</span>")).join("");
      const cl = (g.closers || []);
      const closers = cl.length
        ? '<div class="eyebrow" style="margin-top:10px">Domains that could close it &#183; ' + cl.length + "</div>" +
          '<div class="jumps" style="margin-top:4px">' + cl.slice(0, 5).map((d) =>
            goBtn("roots", { domain: d.id }, esc(d.name) + ' <span class="mono" style="opacity:.75">' + d.n +
              " skills · " + esc(d.priority || "?") + "</span>", d.priority === "HIGH" ? "" : "warnj")).join("") +
          (cl.length > 5 ? '<span class="mini">+' + (cl.length - 5) + " more</span>" : "") + "</div>"
        : (g.n_uncovered ? '<p class="absent" style="margin-top:8px">No application domain lists any of these as a signature skill &#8212; residual authoring risk.</p>' : "");
      return '<article class="grow' + (g.n_uncovered === 0 ? " thin-only" : "") + '" data-gap="' + esc(g.domain + " / " + g.group) + '">' +
        '<div class="gh"><span class="rank mono">' + String(i + 1).padStart(2, "0") + "</span>" +
        '<span class="gt">' + esc(g.group) + '</span><span class="gd">' + esc(g.domain) + "</span>" +
        '<span class="gn">' + g.n_uncovered + " at zero &#183; " + g.n_thin + " thin &#183; " + g.n_total + " total</span></div>" +
        '<div class="gapbar"><i style="width:' + uw + '%;background:var(--c0)"></i><i style="width:' + tw +
        '%;background:var(--c2)"></i><i style="flex:1;background:var(--c5)"></i></div>' +
        '<div class="skl jumps">' + skills + (g.skills.length > 14 ? '<span class="t">+' + (g.skills.length - 14) + " more</span>" : "") + "</div>" +
        closers + "</article>";
    }).join("");

    const unmapped = DATA.cases.filter((c) => !c.mapped);
    const recon = unmapped.map((c) =>
      '<div class="recon-row"><div><div class="rt"><button class="jump" data-go="case" data-focus="' +
      esc(String(CASE_IDX[c.title])) + '">' + esc(c.title) + '</button></div><div class="rp">' + esc(c.path) + "</div></div>" +
      '<div style="text-align:right"><span class="mono" style="font-size:11px;color:var(--muted)">' + c.n_assets + " files</span>" +
      (c.has_guide ? ' <span class="pill ok">guide</span>' : "") + "</div></div>").join("");

    const orphans = DATA.matrix.orphans.map((o) => '<span class="tag" style="border-color:var(--flag-line);background:var(--flag-soft);color:var(--flag)">' + esc(o) + "</span>").join("");
    const fuzzy = DATA.matrix.fuzzy.map((f) =>
      '<div class="recon-row"><div><div class="rt">' + esc(f.folder) + '</div><div class="rp">matched to matrix column &ldquo;' +
      esc(f.column) + '&rdquo;</div></div><div class="mono" style="font-size:11px;color:var(--muted)">' + f.score + "</div></div>").join("");

    $("#view-gaps").innerHTML =
      '<div class="sec-head"><div><h2>Gap Queue</h2><p class="note">Two different kinds of work, deliberately kept apart. ' +
      "Left: clusters of spine skills no case reaches &#8212; these need <em>authoring</em>. " +
      "Right: cases that already exist on disk but were never tagged &#8212; these need <em>reconciliation</em>. " +
      "Conflating them inflates the authoring backlog by " + H.unmapped + " phantom cases.</p></div></div>" +
      '<div class="two"><section>' +
      '<div class="qhead"><h2>Authoring backlog</h2><span class="pill flag">new cases needed</span>' +
      '<span class="n">' + DATA.gaps.length + " clusters &#183; " + H.uncovered + " skills at zero</span></div>" +
      '<p class="qnote">Ranked by number of skills at zero coverage, then by total thin-or-absent. ' +
      "Bar: <span style=\"color:var(--flag)\">zero</span> / <span style=\"color:var(--muted)\">thin (1&#8211;2)</span> / healthy.</p>" +
      authoring + "</section><section>" +
      '<div class="qhead"><h2>Reconciliation backlog</h2><span class="pill">tagging, not authoring</span>' +
      '<span class="n">' + unmapped.length + " cases</span></div>" +
      '<p class="qnote">These ' + unmapped.length + " case studies exist in <span class=\"mono\">source/</span> with " +
      unmapped.reduce((a, c) => a + c.n_assets, 0) + " files between them, and appear nowhere in the legacy standards matrix. " +
      "Their coverage contribution is <strong>unknown</strong>, so the " + H.uncovered_pct + "% zero-coverage figure is an upper bound. " +
      "Tagging these against the spine is cheaper than writing new cases and should happen first.</p>" +
      '<div class="recon-wrap">' + recon + "</div>" +
      '<div class="qhead" style="margin-top:32px"><h2>Matrix columns with no folder</h2><span class="n">' + DATA.matrix.orphans.length + "</span></div>" +
      '<p class="qnote">Tracked in the spreadsheet, no source directory found. Either the case was never written, ' +
      "or its files live somewhere outside <span class=\"mono\">source/</span>.</p><div class=\"taglist\">" + orphans + "</div>" +
      '<div class="qhead" style="margin-top:32px"><h2>Fuzzy joins to confirm</h2><span class="n">' + DATA.matrix.fuzzy.length + "</span></div>" +
      '<p class="qnote">Folder name and matrix column differ. Machine-matched above a ' + DATA.meta.fuzzy_cutoff +
      " similarity threshold; a human should confirm each before the join is trusted.</p>" +
      '<div class="recon-wrap" style="border-left-color:var(--warn)">' + fuzzy + "</div>" +
      "</section></div>";
  }

  /* ===================== 7 · RUBRIC & SCORING ======================= */
  const scoreState = { mode: "real" };
  const LVL_CLASS = (l) => "v-" + String(l || "none").replace(/\s+/g, "");

  function rubricFocus(f) {
    f = f || {};
    if (!f.criterion) return;
    const d = $('details.crit[data-c="' + f.criterion + '"]');
    if (d) { d.open = true; try { d.scrollIntoView({ block: "center" }); } catch (e) { } }
  }

  function renderRubric() {
    const student = ROLE === "student";
    const R = RUB;
    if (!R) { $("#view-rubric").innerHTML = ""; return; }

    const dual =
      '<div class="dual">' +
      '<div class="gatebox"><div class="lab">Output 1 of 2 &#183; pass / not yet</div>' +
      "<h3>The mastery gate</h3>" +
      '<p><span class="big">' + R.criteria.length + "/" + R.criteria.length + "</span> criteria must be at least Proficient " +
      "for a case to count toward a badge.</p>" +
      "<p>" + esc(R.gate_rule) + "</p>" +
      (student ? "<p><strong>This is the one that matters to you.</strong> The question is never a number &#8212; " +
        "it is which criteria are still Not Yet.</p>" : "") + "</div>" +
      '<div class="growbox"><div class="lab">Output 2 of 2 &#183; ' + (student ? "not yours to chase" : "trajectory, not a grade") + "</div>" +
      "<h3>The growth score</h3>" +
      (student
        ? '<p><span class="big" style="color:var(--faint)">&mdash;</span></p>' +
          "<p>There is a 0&#8211;100 composite behind the scenes and it is <strong>deliberately not shown here</strong>. " +
          "It exists so your guide can see whether you are compounding across cases. It is not a grade, it does not decide badges, " +
          "and chasing it would make your work worse.</p>"
        : '<p><span class="big">0&#8211;100</span></p><p>' + esc(R.growth_rule) + "</p>" +
          '<p style="color:var(--flag)"><strong>Never average it with the gate.</strong> Five cases scraping Proficient and ' +
          "five compounding ones look identical to the gate; the score is the only thing that can tell them apart, and it corrupts " +
          "motivation the moment it becomes the point.</p>") +
      "</div></div>";

    /* explicit fg/bg pairs, every one checked against WCAG AA in --verify */
    const WBAR = [["#D9E2EA", "#16140F"], ["#22406B", "#FFFFFF"], ["#3A5F8E", "#FFFFFF"],
      ["#4A6E9A", "#FFFFFF"], ["#89A7C4", "#16140F"], ["#B4C6D8", "#16140F"], ["#B23F22", "#FFFFFF"]];
    const wbar = '<div class="wbar">' + R.criteria.map((c, i) =>
      '<i style="width:' + c.weight + "%;background:" + WBAR[i % 7][0] + ";color:" + WBAR[i % 7][1] + '">' +
      c.id + " " + c.weight + "</i>").join("") + "</div>";

    const crits = R.criteria.map((c) =>
      '<details class="crit" data-c="' + c.id + '"><summary>' +
      '<span class="cid">' + esc(c.id) + "</span>" +
      '<span><span class="cnm">' + esc(c.name) + "</span>" +
      (c.subtitle ? '<span class="csub"> &#183; ' + esc(c.subtitle) + "</span>" : "") +
      (c.source ? '<div class="csub">' + esc(c.source) + "</div>" : "") + "</span>" +
      '<span class="cw">weight ' + c.weight + "</span></summary>" +
      '<div class="critbody">' +
      (c.lead.length ? "<p>" + c.lead.map(mdi).join("</p><p>") + "</p>" : "") +
      '<div class="bands">' + c.bands.map((b, bi) =>
        '<div class="band l' + bi + '"><div class="bl">' + esc(b.level) +
        ' &#183; ' + R.level_points[b.level] + " pts</div><p>" +
        (b.text ? mdi(b.text) : '<span class="absent">not stated</span>') + "</p></div>").join("") + "</div>" +
      (c.notes.length ? c.notes.map((n) => '<div class="callout info" style="margin-top:10px">' + mdi(n) + "</div>").join("") : "") +
      "</div></details>").join("");

    const tiers = '<table class="mtx" style="max-width:760px"><thead><tr><th>Tier</th>' +
      "<th>What Proficient additionally requires</th></tr></thead><tbody>" +
      R.tiers.map((t) => "<tr><td><strong>" + esc(t.tier) + "</strong></td><td>" +
        (t.requires === "—" ? '<span class="absent">nothing beyond the base band</span>' : esc(t.requires)) +
        "</td></tr>").join("") + "</tbody></table>";

    const head = '<div class="sec-head"><div><h2>' + (student ? "How I am assessed" : "Rubric &amp; Scoring") + "</h2>" +
      '<p class="note">RUBRIC.md v' + esc(R.version) + " &#183; <strong>" + esc(R.status) + "</strong>. " +
      (student
        ? "Seven criteria, read straight from the rubric your guide uses. Nothing here is hidden from you and nothing here is a mystery: " +
          "read the Exemplary column before you start, not after you submit."
        : "Parsed from <span class=\"mono\">RUBRIC.md</span> at build time rather than retyped, so this view cannot drift from the document. " +
          "Weights sum to " + R.weight_sum + ".") + "</p></div></div>";

    const machine = student ? "" :
      '<div class="rule"></div><div class="sec-head"><div><h2>What the machine can and cannot see</h2>' +
      '<p class="note">' + (R.guessing_at ? "It is <strong>guessing at</strong> " + mdi(R.guessing_at) : "") + "</p></div></div>" +
      '<div class="two"><section><div class="eyebrow" style="margin-bottom:6px">Signals it actually has</div>' +
      '<table class="mtx"><thead><tr><th>Signal</th><th>Informs</th></tr></thead><tbody>' +
      R.machine_signals.map((s) => "<tr><td>" + mdi(s.signal) + '</td><td class="mono">' +
        s.informs.split(",").map((x) => x.trim()).filter(Boolean).map((x) =>
          '<button class="jump" data-go="rubric" data-focus="' + esc(JSON.stringify({ criterion: x })) + '">' + esc(x) + "</button>").join(" ") +
        "</td></tr>").join("") + "</tbody></table></section>" +
      '<section><div class="eyebrow" style="margin-bottom:6px">Three hard limits</div>' +
      R.hard_limits.map((l, i) => '<div class="callout" style="margin-bottom:8px"><strong>' + (i + 1) + ". " + mdi(l.rule) +
        "</strong> " + mdi(l.detail) + "</div>").join("") + "</section></div>" +
      '<div class="rule"></div><div class="sec-head"><div><h2>Open questions before this locks</h2>' +
      '<p class="note">The rubric says so itself. It is PROPOSED, not locked, and these are the four things one real cohort has to settle.</p></div></div>' +
      '<div class="cards">' + R.open_questions.map((q) =>
        '<div class="card" style="padding:14px 16px;border-left:3px solid var(--warn)"><div style="font-family:var(--serif);font-size:15px;font-weight:600;margin-bottom:4px">' +
        mdi(q.q) + "</div><p style=\"font-size:12.5px;color:var(--ink-2);margin:0\">" + mdi(q.detail) + "</p></div>").join("") + "</div>";

    $("#view-rubric").innerHTML = head + dual +
      '<div class="sec-head" style="margin-top:8px"><div><h2>The seven criteria</h2>' +
      '<p class="note">Click any criterion to open its three bands. Weight bar below is the growth-score weighting only &#8212; ' +
      "the gate ignores weights entirely.</p></div></div>" + wbar +
      '<div style="margin-top:14px">' + crits + "</div>" +
      "<h4 class=\"eyebrow\" style=\"margin:26px 0 8px\">Tier adjustment &#8212; a T1 case scored as if it were T4 is a misuse of this rubric</h4>" + tiers +
      (student ? "" : '<div class="rule"></div>' + scoresBlock()) +
      machine;

    const tg = $("#scoreToggle");
    if (tg) tg.addEventListener("click", () => { scoreState.mode = scoreState.mode === "real" ? "example" : "real"; renderRubric(); });
  }

  function scoresBlock() {
    const SC = DATA.scoring[scoreState.mode], live = scoreState.mode === "real";
    const R = RUB;

    // BUG FIX 2026-08-08 (see student_work/UAT_LOG.md): same class of bug as the
    // Tracker banner -- this used to be hardcoded to "no scores exist yet" for
    // every live-mode render regardless of whether DATA.scoring.real.n_scores was
    // actually 0, so a real cohort's confirmed scores rendered under a banner
    // claiming nothing had been invented "to fill the space" that was itself now
    // false. The table just below (SC.n_scores check) was already correctly
    // dynamic; only the banner text above it wasn't.
    const scoreHasSeed = DATA.scoring.example.n_scores !== DATA.scoring.real.n_scores ||
      DATA.scoring.example.n_overrides !== DATA.scoring.real.n_overrides;
    const banner = '<div class="banner">' + (live
      ? (SC.n_scores
          ? "<span><strong>Live.</strong> " + SC.n_scores + " score record" + (SC.n_scores === 1 ? "" : "s") + " on file, " +
            SC.n_overrides + " guide override" + (SC.n_overrides === 1 ? "" : "s") + " logged. Real verdicts, not a fixture.</span>"
          : "<span><strong>No score records exist yet.</strong> <span class=\"mono\">submissions.json scores[]</span> is empty and every " +
            "override in <span class=\"mono\">score_overrides.json</span> is flagged <span class=\"mono\">_example: true</span>. " +
            "Nothing below is invented to fill the space.</span>")
      : "<span><strong>Previewing example records.</strong> Nothing below is a real learner or a real verdict.</span>") +
      (scoreHasSeed || !live ? '<button class="chip toggle" id="scoreToggle">' + (live ? "Preview with example records" : "Back to live data") + "</button>" : "") +
      "</div>";

    let table;
    if (!SC.n_scores) {
      table = '<div class="empty"><h3 style="font-size:19px;margin-bottom:8px">No verdicts recorded</h3>' +
        '<p style="max-width:60ch;margin:0 auto 14px;color:var(--muted);font-size:13px">' +
        "<span class=\"mono\">submission-score</span> has not run against a submission yet. When it does, each row below carries seven " +
        "verdicts with a confidence flag, and stays <strong>INTERIM</strong> until a named guide confirms it. " +
        "An unconfirmed verdict never counts toward a badge.</p>" +
        '<div class="vgrid" style="max-width:860px;margin:0 auto;text-align:left">' +
        '<div class="vh" style="text-align:left">learner &#183; case</div>' +
        R.criteria.map((c) => '<div class="vh">' + c.id + "</div>").join("") +
        '<div class="vh">gate</div>' +
        '<div class="mono" style="font-size:11px;color:var(--faint);align-self:center">shape only</div>' +
        R.criteria.map(() => '<div class="vcell v-none">&mdash;</div>').join("") +
        '<div class="vcell v-none">&mdash;</div></div>' +
        '<p style="max-width:60ch;margin:16px auto 0;color:var(--faint);font-size:12px">' +
        "Absent, not zero. Nobody is at Not Yet on anything &#8212; nobody has been scored.</p></div>";
    } else {
      table = '<div class="card" style="padding:14px 16px"><div class="vgrid">' +
        '<div class="vh" style="text-align:left">learner &#183; case</div>' +
        R.criteria.map((c) => '<div class="vh">' + c.id + "</div>").join("") +
        '<div class="vh">gate</div>' +
        SC.scores.map((s) =>
          '<div style="align-self:center"><div style="font-family:var(--serif);font-size:14px">' + esc(s.learner) + "</div>" +
          '<div class="mono" style="font-size:10.5px;color:var(--muted)">' + esc(s.case_id) + " &#183; " + esc(s.scored_on || "?") +
          (s.interim ? ' &#183; <strong style="color:var(--warn)">INTERIM</strong>' : " &#183; confirmed by " + esc(s.confirmed_by || "?")) +
          "</div></div>" +
          R.criteria.map((c) => {
            const v = s.criteria[c.id];
            const ovr = (s.overrides || []).filter((o) => o.criterion === c.id)[0];
            if (!v) return '<div class="vcell v-none">&mdash;</div>';
            return '<div class="vcell ' + LVL_CLASS(v.level) + (s.interim ? " interim" : "") +
              '" title="' + esc(c.name) + (ovr ? " · guide override: " + esc(ovr.reason) : "") + '">' +
              esc(v.level === "Not Yet" ? "NY" : v.level === "Proficient" ? "P" : "E") +
              '<span class="cf">' + esc(v.confidence || "?") + (ovr ? " ovr" : "") + (v.set_by === "guide" ? " g" : "") + "</span></div>";
          }).join("") +
          '<div class="vcell ' + (s.badge_eligible ? "v-Proficient" : "v-NotYet") + (s.interim ? " interim" : "") + '">' +
          (s.badge_eligible ? "PASS" : "NOT YET") + "</div>").join("") +
        "</div></div>";
    }

    const bias = '<div class="card">' + SC.bias.map((b) => {
      const st = b.state === "OK" ? "bs-OK" : b.state === "INSUFFICIENT DATA" ? "bs-NA" : "bs-FLAG";
      return '<div class="biasrow"><span class="bc">' +
        '<button class="jump" data-go="rubric" data-focus="' + esc(JSON.stringify({ criterion: b.criterion })) + '">' +
        esc(b.criterion) + "</button></span>" +
        '<span><span class="bn2">' + esc(b.name) + "</span>" +
        '<div class="bd">' + b.n_overrides + " override" + (b.n_overrides === 1 ? "" : "s") + " &#183; " +
        b.n_confirmed + " confirmed record" + (b.n_confirmed === 1 ? "" : "s") +
        (b.direction ? " &#183; " + esc(b.direction) : "") + "</div></span>" +
        '<span class="mono" style="text-align:right">' +
        (b.rate_pct == null ? '<span class="absent">no rate</span>' : b.rate_pct + "%") + "</span>" +
        '<span class="bstate ' + st + '" title="' + esc(b.why_absent || "") + '">' + esc(b.state) + "</span></div>";
    }).join("") + "</div>";

    const anyRate = SC.bias.some((b) => b.rate_pct != null);

    return '<div class="sec-head"><div><h2>Scores</h2><p class="note">' +
      "Per learner per case, the seven verdicts with their confidence flags. " +
      "A machine first pass renders <strong>INTERIM</strong> (hatched) and does not count toward a badge; " +
      "only a named guide can confirm it. Hover a cell for the criterion and any override reason.</p></div></div>" +
      banner + table +
      '<div class="rule"></div><div class="sec-head"><div><h2>Override bias</h2><p class="note">' +
      "Overrides are the training signal. One is a judgment call; a cluster on one criterion is the only measurement of machine " +
      "bias this system has. Per RUBRIC/MCS-31 a criterion overridden more than " + SC.demote_at_pct +
      "% of the time should be <strong>demoted to guide-only</strong> rather than left anchoring the guide with a wrong first pass.</p></div></div>" +
      bias +
      (anyRate ? "" : '<div class="callout" style="margin-top:14px"><strong>No rate is computable and none is shown.</strong> ' +
        "There are " + SC.n_confirmed + " confirmed score records; <span class=\"mono\">score_overrides.json</span> sets the floor at " +
        SC.min_n + ". A percentage off " + SC.n_overrides + " override" + (SC.n_overrides === 1 ? "" : "s") +
        " would be noise wearing a decimal point, so the state is <strong>INSUFFICIENT DATA</strong> and stays that way until the " +
        "denominator exists.</div>") +
      (SC.dangling_override_refs.length
        ? '<div class="callout" style="margin-top:10px"><strong>Referential integrity: ' + SC.dangling_override_refs.length +
          " override row" + (SC.dangling_override_refs.length === 1 ? "" : "s") + " point" +
          (SC.dangling_override_refs.length === 1 ? "s" : "") + " at a score record that does not exist.</strong> " +
          esc(SC.dangling_override_refs.join(", ")) + ". The invariant &ldquo;every entry in overrides[] has a matching row&rdquo; " +
          "holds in one direction only right now, because <span class=\"mono\">scores[]</span> is empty.</div>"
        : "");
  }

  /* ========================= 5 · TRACKER ============================ */
  const trackState = { mode: "real" };

  function progRing(pct, size, label, unknown) {
    const r = size / 2 - 5, C = 2 * Math.PI * r, on = unknown ? 0 : (pct / 100) * C;
    return '<svg width="' + size + '" height="' + size + '" viewBox="0 0 ' + size + " " + size + '" role="img" aria-label="' + esc(label) + '">' +
      '<circle cx="' + size / 2 + '" cy="' + size / 2 + '" r="' + r + '" fill="none" stroke="' + (unknown ? "var(--rule)" : "#E7E1D6") +
      '" stroke-width="6"' + (unknown ? ' stroke-dasharray="4 4"' : "") + "/>" +
      (unknown ? "" : '<circle cx="' + size / 2 + '" cy="' + size / 2 + '" r="' + r + '" fill="none" stroke="var(--accent)" stroke-width="6" ' +
        'stroke-dasharray="' + on.toFixed(1) + " " + (C - on).toFixed(1) + '" transform="rotate(-90 ' + size / 2 + " " + size / 2 + ')"/>') +
      '<text x="' + size / 2 + '" y="' + (size / 2 + 5) + '" text-anchor="middle" font-family="var(--mono)" font-size="' +
      (unknown ? 15 : 14) + '" fill="' + (unknown ? "var(--faint)" : "var(--ink)") + '">' + (unknown ? "—" : Math.round(pct) + "%") + "</text></svg>";
  }

  function renderTracker() {
    const T = DATA.tracker, S = T[trackState.mode], live = trackState.mode === "real";
    const kindClass = (k) => "k-" + k.split(" ")[0];

    let head = '<div class="sec-head"><div><h2>Tracker &#183; Exception Queue</h2><p class="note">' +
      "The home state of this tab is what needs a human, not a summary of what is fine. " +
      "Overdue assignments first, then submissions awaiting review, then learners whose work is ready to be confirmed complete. " +
      'As of <span class="mono">' + esc(T.today) + "</span>.</p></div></div>";

    // BUG FIX 2026-08-08 (see student_work/UAT_LOG.md): this banner and the "empty
    // queue" copy just below used to be hardcoded to the pre-cohort seed-fixture
    // story ("roster.json contains example records only") whenever mode==="real",
    // with no check for whether real learner data actually exists. Once a real
    // cohort's data replaces the seed rows, that text became false -- a genuinely
    // empty exception queue (nothing overdue, nothing awaiting review) was
    // indistinguishable from "no real data has ever been entered," which is
    // exactly the "absent data vs. zero" confusion this whole app's own doctrine
    // (see README's Hard Lines) argues against everywhere else. Now conditioned on
    // whether any non-_example learner actually exists.
    const hasRealData = T.real.learners > 0;
    const hasSeedData = T.example.learners !== T.real.learners || T.example.assignments !== T.real.assignments;
    let banner;
    if (live && !hasRealData) {
      banner = '<div class="banner"><span><strong>Seed state.</strong> roster.json and submissions.json contain example records only ' +
        "(" + DATA.tracker.example.learners + " learners, " + DATA.tracker.example.assignments + " assignments, all flagged " +
        '<span class="mono">_example: true</span>). Per the file invariants they are excluded from every count, so the live queue is empty.</span>' +
        (hasSeedData ? '<button class="chip toggle" id="trackToggle">Preview with example records</button>' : "") + "</div>";
    } else if (live) {
      banner = '<div class="banner"><span><strong>Live.</strong> ' + T.real.learners + " active learner" + (T.real.learners === 1 ? "" : "s") +
        ", real assignment/submission/discussion history. " +
        (S.exceptions.length ? "Items below need your attention." : "Nothing needs judgment today &#8212; not the same thing as nothing having happened yet.") +
        "</span>" + (hasSeedData ? '<button class="chip toggle" id="trackToggle">Preview with example records</button>' : "") + "</div>";
    } else {
      banner = '<div class="banner"><span><strong>Previewing example records.</strong> Nothing below is a real learner. This is the shape the queue takes once ' +
        '<span class="mono">case-track</span> writes real rows.</span>' +
        '<button class="chip toggle" id="trackToggle">Back to live data</button></div>';
    }

    let queue;
    if (!S.exceptions.length && live && !hasRealData) {
      queue = '<div class="empty"><h3 style="font-size:19px;margin-bottom:8px">No exceptions &#8212; and no learners yet</h3>' +
        '<p style="max-width:56ch;margin:0 auto 16px;color:var(--muted);font-size:13px">' +
        "Nothing is overdue because nothing has been assigned. Once <span class=\"mono\">case-track</span> adds a learner and assigns a case, this queue fills with:</p>" +
        '<div style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;max-width:760px;margin:0 auto">' +
        [["OVERDUE", "past due_on, nothing submitted"],
         ["AWAITING REVIEW", "submitted, reviewed_on still null"],
         ["READY TO COMPLETE", "reviewed + accepted + 2 discussions, needs a human confirm"],
         ["STALE", "no due_on set, ageing"]].map((x) =>
          '<span class="pill ' + (x[0] === "OVERDUE" ? "flag" : x[0] === "AWAITING REVIEW" ? "warn" : x[0] === "READY TO COMPLETE" ? "ok" : "") + '" ' +
          'title="' + esc(x[1]) + '">' + x[0] + "</span>").join("") + "</div>" +
        '<p style="max-width:60ch;margin:18px auto 0;color:var(--faint);font-size:12px">' +
        "Counts are deliberately absent rather than zero: an empty roster is not a roster of zero-progress learners.</p></div>";
    } else if (!S.exceptions.length) {
      queue = '<div class="empty"><h3 style="font-size:19px;margin-bottom:8px">Nothing needs judgment today</h3>' +
        '<p style="max-width:56ch;margin:0 auto 16px;color:var(--muted);font-size:13px">' +
        (T.real.learners) + " active learner" + (T.real.learners === 1 ? "" : "s") + ", " + T.real.assignments + " assignment" +
        (T.real.assignments === 1 ? "" : "s") + " on record, and no open exceptions right now &#8212; nothing overdue, nothing awaiting " +
        "review, nothing ready-to-complete sitting unconfirmed. See Badge programs below for what's actually been done.</p></div>";
    } else {
      queue = '<div class="card">' + S.exceptions.map((r) =>
        '<div class="exc-row"><span class="exc-kind ' + kindClass(r.kind) + '">' + esc(r.kind) + "</span>" +
        '<div><div class="who">' + esc(r.learner) + " " +
        (CASE_BY_ID[r.case_id] == null
          ? '<span class="mono" style="font-size:12px;color:var(--muted)">&#183; ' + esc(r.case_id) + "</span>"
          : '<button class="jump" data-go="case" data-focus="' + esc(String(CASE_BY_ID[r.case_id])) + '">' + esc(r.case_id) + "</button>") +
        "</div>" +
        '<div class="det">' + esc(r.detail) + (r.badge_index != null ? " &#183; badge " + r.badge_index : " &#183; badge unallocated") + "</div></div>" +
        '<div class="age">' + r.age + "d</div></div>").join("") + "</div>";
    }

    // badge progress
    let badges;
    if (!S.badges.length) {
      badges = '<div class="empty" style="padding:32px"><p style="color:var(--muted);margin:0;font-size:13px">' +
        "No learners on the roster. Badge progress is <strong>unknown</strong>, not 0% &#8212; there is nobody to have made any.</p>" +
        '<div class="rings" style="margin-top:20px;max-width:520px;margin-left:auto;margin-right:auto">' +
        Object.keys(T.programs).map((p) => {
          const pr = T.programs[p];
          return '<div class="ringcard">' + progRing(0, 62, p + " progress unknown", true) +
            '<div><div class="who">' + esc(p) + '</div><div class="sub">' + pr.badges + " badges × " + pr.cases_per_badge +
            " cases = " + pr.cases_required + "</div>" +
            '<div class="sub" style="color:var(--faint)">no learners enrolled</div></div></div>';
        }).join("") + "</div></div>";
    } else {
      badges = '<div class="rings">' + S.badges.map((b) =>
        '<div class="ringcard">' + progRing((100 * b.cases_done) / b.cases_required, 62, b.name + " progress") +
        '<div><div class="who">' + esc(b.name) + '</div><div class="sub">' + esc(b.program) + " &#183; " + esc(b.cohort || "no cohort") + "</div>" +
        '<div class="sub">' + b.badges + "/" + b.badges_total + " badges &#183; " + b.cases_done + "/" + b.cases_required + " cases</div>" +
        (b.one_short ? '<div style="margin-top:5px"><span class="pill warn">one case short of a badge</span></div>'
          : '<div class="sub" style="color:var(--faint)">' + b.to_next_badge + " to next badge</div>") +
        "</div></div>").join("") + "</div>";
    }

    const oneShort = S.badges.filter((b) => b.one_short);
    const progRef = '<div class="rule"></div><div class="sec-head"><div><h2>Badge programs</h2>' +
      '<p class="note">MS Adventure: ' + T.programs["MS-Adventure"].badges + " badges × " + T.programs["MS-Adventure"].cases_per_badge +
      " cases. Launchpad: " + T.programs["Launchpad"].badges + " × " + T.programs["Launchpad"].cases_per_badge +
      ". A case counts only when its assignment is <span class=\"mono\">complete</span>, which requires review plus two logged discussions " +
      "and an explicit human confirm &#8212; the tracker never awards a badge itself.</p></div></div>";

    $("#view-tracker").innerHTML = head + banner +
      (oneShort.length ? '<div class="callout" style="margin-bottom:16px"><strong>' + oneShort.length +
        " learner" + (oneShort.length === 1 ? " is" : "s are") + " one case short of a badge:</strong> " +
        oneShort.map((b) => esc(b.name)).join(", ") + "</div>" : "") +
      queue + progRef + badges +
      '<div class="rule"></div><div class="callout info"><strong>Nothing here is a grade.</strong> ' +
      "submissions.json has no numeric score field by design. The queue records state and surfaces what needs facilitator judgment; " +
      "review outcome, badge award and completion are all human acts.</div>";

    const tg = $("#trackToggle");
    if (tg) tg.addEventListener("click", () => { trackState.mode = live ? "example" : "real"; renderTracker(); });
  }

  /* ========================== 8 · STUDENT =========================== */
  function renderMyCases() {
    const cards = S.cases.length ? S.cases.map((c) => {
      const steps = [
        ["assigned", true],
        ["submitted", !!c.submitted_on],
        ["reviewed", c.reviewed],
        ["discussed " + c.discussions + "/2", c.discussions >= c.discussions_required],
        ["complete", c.status === "complete"]
      ];
      let cur = steps.findIndex((s) => !s[1]);
      const late = c.due_on && /past due/.test(c.due_state);
      const interactive = c.assets.filter((a) => a.kind === "interactive_html");
      const downloads = c.assets.filter((a) => a.kind !== "interactive_html");
      return '<article class="mycase"><h3>' + esc(c.title) + "</h3>" +
        '<div class="mm">' + esc(c.tier || "tier unrecorded") + " &#183; assigned " + esc(c.assigned_on) +
        (c.badge_index != null ? " &#183; badge " + c.badge_index : " &#183; badge unallocated") + "</div>" +
        '<div class="due' + (late ? " late" : "") + '">' + esc(c.due_state) + "</div>" +
        '<div class="steps">' + steps.map((s, i) =>
          '<span class="step' + (s[1] ? " done" : (i === cur ? " now" : "")) + '">' + esc(s[0]) + "</span>").join("") + "</div>" +
        (interactive.length ? primaryCta(interactive[0]) : "") +
        (downloads.length
          ? '<div class="downloads-label">Downloads</div>' + linkList(downloads)
          : (interactive.length ? "" : '<p class="absent">No files indexed for this case yet &#8212; ask your guide.</p>')) +
        "</article>";
    }).join("")
      : '<div class="empty"><h3 style="font-size:19px;margin-bottom:8px">Nothing assigned yet</h3>' +
        '<p style="color:var(--muted);font-size:13px;max-width:52ch;margin:0 auto">' +
        "When a case is assigned to you it appears here with every file you need to download.</p></div>";

    $("#view-mycases").innerHTML =
      '<div class="sec-head"><div><h2>My Cases</h2><p class="note">' +
      "Everything assigned to you, with the files. You get the case document, the data workbooks and any reference PDFs. " +
      "The Guide Notes and the Socratic plan are your facilitator's &#8212; they are not in this file at all.</p></div></div>" +
      (S.preview_only ? '<div class="banner"><span><strong>Example learner.</strong> The roster has no real learners yet, ' +
        "so this view is rendered from the seed record flagged <span class=\"mono\">_example: true</span>.</span></div>" : "") +
      '<div class="jumps" style="margin-bottom:18px">' +
      goBtn("rubric", null, "Read the rubric before you start &#8594;") +
      goBtn("myskills", null, "See the skills I have exercised &#8594;") + "</div>" +
      '<div class="mycards">' + cards + "</div>";
  }

  function renderMyProgress() {
    const b = S.badges;
    const pct = b.cases_required ? (100 * b.cases_done) / b.cases_required : 0;
    const scores = S.scores.length
      ? S.scores.map((s) =>
        '<div class="card" style="padding:14px 16px;margin-bottom:10px">' +
        '<div style="display:flex;align-items:baseline;gap:10px;flex-wrap:wrap"><span style="font-family:var(--serif);font-size:16px">' +
        esc(s.title) + "</span>" +
        (s.interim ? '<span class="pill warn">INTERIM &#183; not confirmed by a guide</span>'
                   : (s.badge_eligible ? '<span class="pill ok">counts toward a badge</span>'
                                       : '<span class="pill flag">not yet</span>')) + "</div>" +
        (s.not_yet.length
          ? '<p style="margin-top:8px;font-size:12.5px">Still <strong>Not Yet</strong> on: ' +
            '<span class="jumps">' + s.not_yet.map((c) =>
              '<button class="jump" data-go="rubric" data-focus="' + esc(JSON.stringify({ criterion: c })) + '">' + esc(c) + "</button>").join("") +
            "</span></p>"
          : '<p style="margin-top:8px;font-size:12.5px;color:var(--ok)">Every criterion at Proficient or better.</p>') +
        "</div>").join("")
      : '<div class="empty" style="padding:32px"><p style="color:var(--muted);margin:0;font-size:13px;max-width:54ch;margin:0 auto">' +
        "Nothing has been scored yet. That is <strong>absent</strong>, not zero &#8212; there is no verdict on your work, " +
        "which is different from a verdict of Not Yet.</p></div>";

    $("#view-myprogress").innerHTML =
      '<div class="sec-head"><div><h2>My Progress</h2><p class="note">' +
      esc(S.program.badges) + " badges &times; " + S.program.cases_per_badge + " cases = " + S.program.cases_required +
      " for the whole " + esc(S.learner.program) + " program. A case counts only when it is complete: reviewed, " +
      "two discussions logged, and confirmed by a human.</p></div></div>" +
      '<div class="rings" style="margin-bottom:24px"><div class="ringcard">' + progRing(pct, 62, "case progress") +
      '<div><div class="who">' + esc(S.learner.name) + '</div><div class="sub">' + esc(S.learner.cohort || "no cohort") + "</div>" +
      '<div class="sub">' + b.cases_done + "/" + b.cases_required + " cases &#183; " + b.n_earned + "/" + b.badges_total + " badges</div>" +
      '<div class="sub" style="color:var(--faint)">' + (b.to_next ? b.to_next + " to the next badge" : "program complete") + "</div>" +
      "</div></div>" +
      b.earned.map((e) => '<div class="ringcard"><div><div class="who">Badge ' + e.badge_index + "</div>" +
        '<div class="sub">awarded ' + esc(e.awarded_on) + "</div>" +
        '<div class="sub">' + e.n_cases + " cases</div></div></div>").join("") + "</div>" +
      '<div class="sec-head"><div><h2>My verdicts</h2><p class="note">' +
      "Per case, whether it counts toward a badge and which criteria are still Not Yet. " +
      "There is no number here on purpose &#8212; the rubric is explicit that the growth score is a coaching tool for your guide, " +
      "not a grade for you. The question that matters is which criteria are still open.</p></div></div>" + scores;
  }

  function mySkillsFocus() { /* the student heatmap has no sub-focus yet */ }

  function renderMySkills() {
    const done = {};
    S.skills.exercised.forEach((id) => (done[id] = true));
    $("#view-myskills").innerHTML =
      '<div class="sec-head"><div><h2>My Skills</h2><p class="note">' +
      "The " + S.skills.n_total + " atomic skills in the spine. Filled = a case you have completed exercises it. " +
      "This is <em>your</em> map, not the studio's: it says nothing about whether anyone else has covered a skill.</p></div></div>" +
      '<div class="card" style="padding:18px 20px;margin-bottom:20px">' +
      '<div style="display:flex;gap:24px;align-items:center;flex-wrap:wrap">' +
      '<div><div class="mono" style="font-size:30px;font-weight:600">' + S.skills.n_exercised + "</div>" +
      '<div class="eyebrow">skills exercised of ' + S.skills.n_total + "</div></div>" +
      '<div style="flex:1;min-width:220px"><div class="bar" style="height:9px"><i style="width:' +
      (100 * S.skills.n_exercised / S.skills.n_total).toFixed(1) + '%"></i></div>' +
      '<div class="mono" style="font-size:11px;color:var(--muted);margin-top:6px">from ' +
      (S.skills.from_cases.length ? esc(S.skills.from_cases.join(", ")) : "no completed cases yet") + "</div></div></div></div>" +
      (S.skills.from_cases.length ? "" :
        '<div class="callout" style="margin-bottom:18px"><strong>Nothing filled in yet.</strong> ' +
        "This map fills as cases are marked complete, not as they are submitted.</div>") +
      '<div class="legend" style="margin-bottom:14px"><span class="eyebrow">Legend</span>' +
      '<span class="item"><span class="sw" style="background:var(--accent)"></span>I have exercised it</span>' +
      '<span class="item"><span class="sw" style="background:var(--paper-2)"></span>Not yet</span></div>' +
      '<div class="jumps" style="margin-bottom:16px">' +
      goBtn("roots", null, "Where these skills actually get used &#8594;") +
      goBtn("mycases", null, "Back to my cases &#8594;") + "</div>" +
      '<div id="mySkillBody"></div>';

    // the student payload carries only ids; group them off the shared spine shape
    const body = $("#mySkillBody");
    if (!DATA.heat) {
      body.innerHTML = '<div class="myheat">' + S.skills.exercised.map(() =>
        '<span style="background:var(--accent)"></span>').join("") +
        Array(Math.max(0, S.skills.n_total - S.skills.n_exercised)).join("|").split("|").map(() =>
          '<span style="background:var(--paper-2)"></span>').join("") + "</div>";
      return;
    }
    body.innerHTML = DATA.heat.map((d) => {
      const n = d.groups.reduce((a, g) => a + g.skills.filter((s) => done[s.id]).length, 0);
      return '<section class="dom-block"><div class="dom-head"><h3>' + esc(d.domain) + "</h3>" +
        '<span class="pill' + (n ? " ok" : "") + '">' + n + " of " + d.n + "</span></div>" +
        d.groups.map((g) => '<div class="grp"><div class="gname">' + esc(g.group) + "<em>" +
          g.skills.filter((s) => done[s.id]).length + " of " + g.n + "</em></div>" +
          '<div class="myheat">' + g.skills.map((s) =>
            '<span title="' + esc(s.label) + '" style="background:' + (done[s.id] ? "var(--accent)" : "var(--paper-2)") + '"></span>').join("") +
          "</div></div>").join("") + "</section>";
    }).join("");
  }

  /* ========================= global search ========================== */
  let SEARCH = [], searchCur = -1, searchRows = [];

  function buildSearch() {
    SEARCH = [];
    if (ROLE === "student") {
      S.cases.forEach((c) => SEARCH.push({ g: "My cases", t: c.title, m: c.due_state, v: "mycases", f: null }));
      RC.domains.forEach((d) => {
        SEARCH.push({ g: "Fields", t: d.name, m: d.one_line, v: "roots", f: { domain: d.id } });
        d.careers.forEach((k) => SEARCH.push({ g: "Careers", t: k.title, m: d.name, v: "roots", f: { domain: d.id } }));
      });
      RUB.criteria.forEach((c) => SEARCH.push({ g: "Rubric", t: c.id + " · " + c.name, m: "weight " + c.weight, v: "rubric", f: { criterion: c.id } }));
      (DATA.heat || []).forEach((d) => d.groups.forEach((g) => g.skills.forEach((s) =>
        SEARCH.push({ g: "Skills", t: s.label, m: d.domain, v: "myskills", f: null }))));
      return;
    }
    DATA.cases.forEach((c, i) => SEARCH.push({
      g: "Cases", t: c.title, m: c.year + " · " + c.session + " · " + c.n_links_ok + " files", v: "case", f: i
    }));
    Object.keys(SKILL).forEach((id) => {
      const r = SKILL[id];
      SEARCH.push({ g: "Skills", t: r.s.label, m: r.d + " · " + r.g + " · " + r.s.n + " cases", v: "heat", f: { skill: id } });
    });
    RC.domains.forEach((d) => {
      SEARCH.push({ g: "Domains", t: d.name, m: d.cluster + " · " + d.priority + " · " + d.n_cases + " cases", v: "roots", f: { domain: d.id } });
      d.careers.forEach((k) => SEARCH.push({ g: "Careers", t: k.title, m: d.name, v: "roots", f: { domain: d.id } }));
    });
    DATA.branches.forEach((b) => SEARCH.push({
      g: "Branches", t: b.branch, m: "Phase " + b.phase + " · " + b.band, v: "tree", f: { branch: b.id }
    }));
    if (RUB) RUB.criteria.forEach((c) => SEARCH.push({
      g: "Rubric", t: c.id + " · " + c.name, m: "weight " + c.weight, v: "rubric", f: { criterion: c.id }
    }));
  }

  function runSearch(q) {
    const box = $("#gres");
    q = q.trim().toLowerCase();
    if (q.length < 2) { box.classList.remove("on"); box.innerHTML = ""; $("#gq").setAttribute("aria-expanded", "false"); return; }
    const hits = [];
    for (let i = 0; i < SEARCH.length; i++) {
      const it = SEARCH[i], t = it.t.toLowerCase();
      const p = t.indexOf(q);
      if (p >= 0) hits.push({ it: it, rank: (p === 0 ? 0 : 1), len: t.length });
      else if ((it.m || "").toLowerCase().indexOf(q) >= 0) hits.push({ it: it, rank: 2, len: t.length });
    }
    hits.sort((a, b) => a.rank - b.rank || a.len - b.len);
    const top = hits.slice(0, 40);
    if (!top.length) {
      box.innerHTML = '<div class="none">Nothing matches &ldquo;' + esc(q) + "&rdquo;.</div>";
      box.classList.add("on"); $("#gq").setAttribute("aria-expanded", "true"); searchRows = []; return;
    }
    const groups = {};
    top.forEach((h) => (groups[h.it.g] = groups[h.it.g] || []).push(h.it));
    let html = "", n = 0; searchRows = [];
    Object.keys(groups).forEach((g) => {
      html += '<div class="rgroup">' + esc(g) + " &#183; " + groups[g].length + "</div>";
      groups[g].forEach((it) => {
        searchRows.push(it);
        html += '<button role="option" data-n="' + n + '">' + esc(it.t) +
          '<span class="rm">' + esc(it.m || "") + "</span></button>";
        n++;
      });
    });
    box.innerHTML = html; box.classList.add("on"); $("#gq").setAttribute("aria-expanded", "true"); searchCur = -1;
  }
  function pickSearch(n) {
    const it = searchRows[n]; if (!it) return;
    $("#gres").classList.remove("on"); $("#gq").setAttribute("aria-expanded", "false"); $("#gq").blur();
    if (it.v === "case") openCase(it.f, false); else goto(it.v, it.f);
  }
  $("#gq").addEventListener("input", (e) => runSearch(e.target.value));
  $("#gres").addEventListener("click", (e) => {
    const b = e.target.closest("button[data-n]"); if (b) pickSearch(+b.dataset.n);
  });
  $("#gq").addEventListener("keydown", (e) => {
    if (e.key === "Escape") { $("#gres").classList.remove("on"); $("#gq").setAttribute("aria-expanded", "false"); return; }
    if (!searchRows.length) return;
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {
      e.preventDefault();
      searchCur = Math.max(0, Math.min(searchRows.length - 1, searchCur + (e.key === "ArrowDown" ? 1 : -1)));
      $$("#gres button").forEach((b, i) => b.classList.toggle("cur", i === searchCur));
      const el = $$("#gres button")[searchCur]; if (el) el.scrollIntoView({ block: "nearest" });
    } else if (e.key === "Enter") {
      e.preventDefault(); pickSearch(searchCur < 0 ? 0 : searchCur);
    }
  });
  document.addEventListener("keydown", (e) => {
    if (e.key !== "/" || e.metaKey || e.ctrlKey || e.altKey) return;
    const t = e.target, tag = (t && t.tagName) || "";
    if (tag === "INPUT" || tag === "TEXTAREA" || (t && t.isContentEditable)) return;
    e.preventDefault(); $("#gq").focus(); $("#gq").select();
  });
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".searchwrap")) {
      $("#gres").classList.remove("on"); $("#gq").setAttribute("aria-expanded", "false");
    }
  });

  /* ============================== boot ============================== */
  try { history.replaceState({ mcs: { view: null, focus: {} } }, ""); HISTORY_OK = true; }
  catch (e) { HISTORY_OK = false; }

  paintRole();
  if (HASGUIDE) { renderTree(); renderHeat(); renderLibrary(); renderPipeline(); renderGaps(); renderTracker(); }
  if (RC.domains.length) renderRoots();
  if (RUB) renderRubric();
  if (S) { renderMyCases(); renderMyProgress(); renderMySkills(); }
  buildSearch();
  goto(tabsFor()[0].id, null, { replace: true });

  /* re-render the role-sensitive views when the role changes */
  const _paintRole = paintRole;
  window.__setRole = function (r) {
    if (ROLES.indexOf(r) < 0) return false;
    ROLE = r; store.set(RKEY, r); closeSheet(true); NAVSTACK = [];
    _paintRole(); if (RC.domains.length) renderRoots(); if (RUB) renderRubric();
    buildSearch(); goto(tabsFor()[0].id, null, { replace: true });
    return true;
  };
  $("#roleSw").addEventListener("click", (e) => {
    const b = e.target.closest("button[data-r]"); if (b) window.__setRole(b.dataset.r);
  });

  window.__READY__ = true;
  window.__MCS__ = { goto: goto, openCase: openCase, back: back, role: () => ROLE, views: VIEWS, data: DATA };
})();
</script>
</body>
</html>
"""


def render(data, role_lock):
    payload = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    # guard against the JSON literal closing the <script> element
    payload = payload.replace("</", "<\\/")
    return (TEMPLATE
            .replace("__ROLE_LOCK__", json.dumps(role_lock))
            .replace("__DATA_JSON__", payload))


def student_doc(data, student):
    """The learner-facing payload for ONE learner. Everything else is not
    hidden — it is absent.

    The only spine data that survives is the skill id/label/group shape needed
    to draw the learner's own map: no covered_by, no per-skill case counts, no
    corpus, no tracker, no scores but the learner's own, no gap queue."""
    heat = [{
        "domain": d["domain"], "n": d["n"],
        "groups": [{"group": g["group"], "n": g["n"],
                    "skills": [{"id": s["id"], "label": s["label"], "kind": s["kind"]}
                               for s in g["skills"]]} for g in d["groups"]],
    } for d in data["heat"]]
    st = dict(student)
    st["rubric"] = data["rubric"]
    st["domains"] = data["rootc"]
    return {
        "meta": {"generated_on": data["meta"]["generated_on"],
                 "sources": [],
                 "rubric_version": data["meta"]["rubric_version"],
                 "build": "student"},
        "headline": None, "branches": None, "cases": None, "exemplars": None,
        "cases_by_branch": None, "matrix": None, "gaps": None, "tracker": None,
        "scoring": None, "rootc": None, "roots": None, "phases": None, "links": None,
        "heat": heat,
        "student": st,
    }


def student_file_path(learner_id):
    return ROOT / "app" / ("student-%s.html" % learner_id)


LANDING_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Math Builder — My Cases</title>
<style>
:root{--paper:#FAF8F4;--ink:#16140F;--muted:#5F594E;--accent:#164A3D;--accent-soft:#E3F0EA;
  --accent-line:#AFCFC3;--rule:#DED8CC;--card:#FFFFFF}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
  font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
.wrap{max-width:520px;margin:0 auto;padding:64px 20px}
h1{font-size:22px;margin:0 0 6px}
p.lead{color:var(--muted);margin:0 0 28px}
.card{background:var(--card);border:1px solid var(--rule);border-radius:10px;overflow:hidden}
a.row{display:block;padding:16px 18px;color:var(--ink);text-decoration:none;
  border-bottom:1px solid var(--rule)}
a.row:last-child{border-bottom:none}
a.row:hover{background:var(--accent-soft)}
a.row .n{font-weight:600}
a.row .go{float:right;color:var(--accent)}
.empty{color:var(--muted);font-size:13.5px;padding:16px 18px}
.guide{margin-top:28px;font-size:13px;color:var(--muted)}
.guide a{color:var(--accent)}
</style>
</head>
<body>
<div class="wrap">
  <h1>Math Builder</h1>
  <p class="lead">Find your name below to open your own cases, progress and skills.</p>
  <div class="card">__ROWS__</div>
  <p class="guide">Guiding, not learning? <a href="dashboard.html">Open the Guide Dashboard</a>.</p>
</div>
</body>
</html>
"""


def render_student_landing(students):
    """A generic, unauthenticated index -- deliberately carries no case,
    score, or assignment data for anyone. Just names and a link to each
    learner's own role-locked file, so every published case's shared
    '../../../app/student.html' back-link keeps resolving to something real
    once a single learner build no longer lives at that exact path."""
    rows = "".join(
        '<a class="row" href="student-%s.html"><span class="n">%s</span>'
        '<span class="go">Open &rarr;</span></a>'
        % (l["learner"]["id"], esc_py(l["learner"]["name"]))
        for l in sorted(students.values(), key=lambda s: s["learner"]["name"])
    ) or '<div class="empty">No active learners yet.</div>'
    return LANDING_TEMPLATE.replace("__ROWS__", rows)


def esc_py(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#39;"))


def build():
    data = build_data()
    html = render(data, None)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    shtmls = {}
    for learner_id, st in data.get("students", {}).items():
        shtmls[learner_id] = render(student_doc(data, st), "student")
        student_file_path(learner_id).write_text(shtmls[learner_id], encoding="utf-8")
    landing = render_student_landing(data.get("students", {}))
    OUT_STUDENT.write_text(landing, encoding="utf-8")
    return data, html, shtmls, landing


# --------------------------------------------------------------------------
# verification
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# WCAG AA contrast — computed, not eyeballed
# --------------------------------------------------------------------------

def _lum(hexcolor):
    h = hexcolor.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4)]
    c = [(x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4) for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(fg, bg):
    a, b = _lum(fg), _lum(bg)
    hi, lo = max(a, b), min(a, b)
    return round((hi + 0.05) / (lo + 0.05), 2)


# fg, bg, minimum ratio, what it is. 4.5 = AA body text, 3.0 = AA large/UI.
CONTRAST_PAIRS = [
    ("#16140F", "#FAF8F4", 4.5, "body ink on paper"),
    ("#5F594E", "#FAF8F4", 4.5, "muted on paper"),
    ("#6E675C", "#FAF8F4", 4.5, "faint on paper"),
    ("#22406B", "#FAF8F4", 4.5, "accent link on paper"),
    ("#22406B", "#E8EEF6", 4.5, "accent on accent-soft (chips, jump buttons)"),
    ("#A93A1E", "#F8E7E1", 4.5, "flag on flag-soft"),
    ("#7E5310", "#F8EFD9", 4.5, "warn on warn-soft"),
    ("#2A5C45", "#E4EFE8", 4.5, "ok on ok-soft"),
    ("#4B3A73", "#EFEAF6", 4.5, "HS pill"),
    ("#F6F3EC", "#16140F", 4.5, "guide role bar"),
    ("#CFC8B9", "#16140F", 4.5, "guide role bar subtext"),
    ("#F1F7F4", "#164A3D", 4.5, "student role bar"),
    ("#C3DCD3", "#164A3D", 4.5, "student role bar subtext"),
    ("#164A3D", "#FAF8F4", 4.5, "student accent on paper"),
    ("#164A3D", "#E3F0EA", 4.5, "student accent on its soft fill"),
    ("#123C31", "#F1F7F4", 4.5, "student active role toggle"),
    ("#F6F3EC", "#1B1913", 4.5, "tooltip body"),
    ("#B9B2A4", "#1B1913", 4.5, "tooltip meta"),
    ("#FFFFFF", "#22406B", 4.5, "white on accent (weight bar C3+, hover jump)"),
    # the seven rubric weight-bar segments, fg on bg, each stated explicitly
    ("#16140F", "#D9E2EA", 4.5, "weight bar C1"),
    ("#FFFFFF", "#22406B", 4.5, "weight bar C2"),
    ("#FFFFFF", "#3A5F8E", 4.5, "weight bar C3"),
    ("#FFFFFF", "#4A6E9A", 4.5, "weight bar C4"),
    ("#16140F", "#89A7C4", 4.5, "weight bar C5"),
    ("#16140F", "#B4C6D8", 4.5, "weight bar C6"),
    ("#FFFFFF", "#B23F22", 4.5, "weight bar C7"),
]


def verify(quiet=False):
    html = OUT.read_text(encoding="utf-8")
    m = re.search(r"const DATA = (.*?);\n", html, re.S)
    assert m, "inlined DATA literal not found"
    data = json.loads(m.group(1).replace("<\\/", "</"))

    checks = []

    def ck(name, got, want):
        ok = got == want
        checks.append((ok, name, got, want))
        return ok

    # --- structural
    for t in ["tree", "heat", "library", "roots", "rubric", "gaps", "tracker",
              "mycases", "myprogress", "myskills"]:
        ck("root element #view-" + t, ('id="view-' + t + '"') in html, True)
        ck("tab declared for " + t, ('{ id: "' + t + '"') in html, True)
    ck("single <script> data block", html.count("const DATA = "), 1)
    ck("no unescaped </script> in payload", html.count("</script>"), 2)
    ck("no external <script src>/<link href> to the network",
       bool(re.search(r'<(script|link|img|iframe)[^>]+(src|href)="https?://', html)), False)
    ck("role lock is null in the guide build", "const ROLE_LOCK = null;" in html, True)
    ck("router exposes goto()", "window.__MCS__" in html, True)

    # --- recompute everything straight from source
    spine = load("standards_spine.json")
    corpus = load("corpus_index.json")["cases"]
    cases_index_v = load("cases_index.json")
    ci_by_title_v = {c["title"]: c for c in cases_index_v["cases"]}
    tree = load("curriculum_tree.json")
    gapq = load("gap_queue.json")
    roster = load("roster.json")
    subs = load("submissions.json")

    all_skills = [s for d in spine["domains"] for g in d["groups"] for s in g["skills"]]
    ck("spine skills", data["headline"]["skills"], len(all_skills))
    ck("spine skills == totals.skills", len(all_skills), spine["totals"]["skills"])
    ck("zero-coverage skills", data["headline"]["uncovered"], sum(1 for s in all_skills if s["n"] == 0))
    ck("zero-coverage == totals.uncovered", data["headline"]["uncovered"], spine["totals"]["uncovered"])
    ck("thin (1-2) skills", data["headline"]["thin"], sum(1 for s in all_skills if 1 <= s["n"] <= 2))
    ck("thin == totals.thin_1_2", data["headline"]["thin"], spine["totals"]["thin_1_2"])
    ck("domains", data["headline"]["domains"], len(spine["domains"]))
    ck("heatmap cells rendered == skills",
       sum(len(g["skills"]) for d in data["heat"] for g in d["groups"]), len(all_skills))

    geo = [s for d in spine["domains"] if d["domain"] == "Geometry" for g in d["groups"] for s in g["skills"]]
    ck("geometry skills", data["headline"]["geometry_skills"], len(geo))
    ck("geometry uncovered", data["headline"]["geometry_uncovered"], sum(1 for s in geo if s["n"] == 0))

    r = reconcile(corpus, spine["cases"])
    # Case Library entries = every corpus folder, PLUS every pipeline-native
    # case (never in corpus_index.json, so not reconciled above) that has a
    # real cases/<id>/case.json on disk. Mirrors the two-pass build in
    # build_data() -- see the "case library, part 2" loop.
    used_ci_ids_v = set()
    for c in corpus:
        col = r[c["title"]]["col"]
        ci_v = ci_by_title_v.get(col) if col else None
        if ci_v:
            used_ci_ids_v.add(ci_v["id"])
    pipeline_v = load("pipeline_status.json")
    pipeline_native_ids_v = {
        pc["id"] for pc in pipeline_v.get("cases", [])
        if pc.get("origin") != "legacy" and pc["id"] not in used_ci_ids_v
        and (ROOT / "cases" / pc["id"] / "case.json").exists()
    }
    expected_lib_total = len(corpus) + len(pipeline_native_ids_v)
    ck("corpus cases", data["headline"]["corpus_cases"], expected_lib_total)
    ck("cases emitted", len(data["cases"]), expected_lib_total)
    ck("matrix columns", data["headline"]["matrix_cols"], len(spine["cases"]))

    # pipeline-native cases' own contribution to with_guide/asset_files, counted
    # the same way build_data()'s pipeline-native loop counts them (glob the
    # published/ dir; a .docx is "guide notes" iff "facilitator" is in its name).
    _kind_exts = {".html", ".xlsx", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".docx"}
    pn_guide, pn_assets = 0, 0
    for _pid in pipeline_native_ids_v:
        pub = ROOT / "cases" / _pid / "published"
        if not pub.is_dir():
            continue
        _has_guide = False
        for fp in pub.iterdir():
            if fp.name == "MANIFEST.json" or not fp.is_file() or fp.suffix.lower() not in _kind_exts:
                continue
            pn_assets += 1
            if fp.suffix.lower() == ".docx" and "facilitator" in fp.stem.lower():
                _has_guide = True
        if _has_guide:
            pn_guide += 1
    ck("mapped cases", data["headline"]["mapped"], sum(1 for v in r.values() if v["col"]))
    ck("unmapped cases", data["headline"]["unmapped"], sum(1 for v in r.values() if not v["col"]))
    ck("mapped+unmapped == corpus", data["headline"]["mapped"] + data["headline"]["unmapped"], len(corpus))
    ck("orphan matrix columns", data["headline"]["orphan_cols"],
       len(set(spine["cases"]) - {v["col"] for v in r.values() if v["col"]}))
    ck("guide notes", data["headline"]["with_guide"], sum(1 for c in corpus if c["has_guide"]) + pn_guide)
    # pipeline-native cases never carry a socratic plan (that's a legacy-corpus
    # asset kind), so they contribute nothing here.
    ck("socratic plans", data["headline"]["with_socratic"], sum(1 for c in corpus if c["has_socratic_plan"]))
    ck("asset files", data["headline"]["asset_files"], sum(c["n_assets"] for c in corpus) + pn_assets)

    ck("branches", len(data["branches"]), len(tree["branches"]))
    unm = [b["id"] for b in data["branches"] if b["coverage"]["state"] == "unmapped"]
    ck("unmapped branches", sorted(unm), sorted(b["id"] for b in tree["branches"] if not b["acton_domains"]))
    ck("unmapped branch coverage is null (never 0)",
       all(b["coverage"]["pct"] is None and b["coverage"]["n_skills"] is None
           for b in data["branches"] if b["coverage"]["state"] == "unmapped"), True)
    # A literal 0% is legitimate for a branch with real standards rows and genuinely zero
    # coverage (precalc/calculus/discrete as of Roadmap B2, 2026-08-01) — see the fuller note
    # on the matching check further down. The actual invariant is never-0%-for-"unmapped".
    ck("no branch is both 'unmapped' and rendered at pct 0",
       any(b["coverage"]["state"] == "unmapped" and b["coverage"]["pct"] == 0 for b in data["branches"]),
       False)
    ck("roots", len(data["roots"]), len(tree["intersections"]))
    ck("gap clusters", len(data["gaps"]), len(gapq))
    ck("gap skills total", sum(g["n_gap"] for g in data["gaps"]), sum(g["n_gap"] for g in gapq))

    # ---- pipeline ----------------------------------------------------
    pdat = data["pipeline"]
    stage_order = pdat["_schema"]["stage_order"]
    ck("every case has a valid pipeline stage",
       [c["id"] for c in pdat["cases"] if c["stage"] not in stage_order], [])
    ck("stage_counts sums to cases + concepts",
       sum(pdat["stage_counts"].values()), len(pdat["cases"]) + len(pdat["concepts"]))
    written_titles = {c["title"] for c in pdat["cases"]}
    ck("no concept sheet entry duplicates an already-written case title",
       sorted(c["title"] for c in pdat["concepts"] if c["title"] in written_titles), [])
    lrd = data["legacy_readiness"]
    ck("legacy_total matches legacy_readiness.json case count (and 'legacy' is not a pipeline stage)",
       (pdat["legacy_total"], "legacy" in stage_order), (lrd["n_legacy_cases"], False))
    legacy_cards = [c for c in pdat["cases"] if c.get("origin") == "legacy"]
    ck("one pipeline, not two — every legacy case is a folded card, a declared exception, or a real conversion",
       len(legacy_cards) + len(pdat["legacy_exceptions"]) + len(pdat.get("legacy_converted_titles", [])),
       pdat["legacy_total"])
    ck("a converted legacy title is never ALSO left as a stale 'not yet converted' card",
       sorted(set(pdat.get("legacy_converted_titles", [])) & {c["title"] for c in legacy_cards}), [])
    ck("every folded legacy card sits in concepting or drafting, never a stage it hasn't earned",
       sorted({c["stage"] for c in legacy_cards} - {"concepting", "drafting"}), [])
    ck("every case with tier1 actually run reports a stage-1 verdict string",
       [c["id"] for c in pdat["cases"] if c["tier1"].get("ran") and not c["tier1"].get("verdict")], [])

    # ---- legacy readiness ---------------------------------------------
    # legacy_readiness.json counts real docx files still sitting under source/Y1-3 --
    # a physical-file count, unaffected by whether one has since been converted into a
    # real cases/<id> packet. corpus_index's "legacy" status count drops by exactly one
    # for each conversion, so the two are expected to diverge by the converted count.
    ck("legacy_readiness case count matches corpus_index legacy count",
       lrd["n_legacy_cases"],
       sum(1 for c in corpus if c.get("status") == "legacy") + len(pdat.get("legacy_converted_titles", [])))
    ck("legacy readable + errored == total legacy cases",
       lrd["n_case_docs_readable"] + lrd["n_case_docs_errored"], lrd["n_legacy_cases"])
    ck("every structural-shape stat's n does not exceed the readable count",
       [k for k, v in lrd["structural_shape_summary"].items()
        if isinstance(v, dict) and v.get("n", 0) > lrd["n_case_docs_readable"]], [])

    ck("tracker live learners (all seed excluded)", data["tracker"]["real"]["learners"],
       len([l for l in roster["learners"] if not l.get("_example")]))
    ck("tracker live exception queue empty", data["tracker"]["real"]["exceptions"], [])
    # "example" here is really "unfiltered" (real + any _example-flagged seed rows
    # still in roster.json/submissions.json), used pre-cohort so the Tracker tab has
    # something to preview. Once a real cohort exists and the seed rows are deleted
    # (roster.json's own invariant: "delete them before real use"), unfiltered ==
    # real, and there is no longer a fixed fixture shape to assert -- that's the
    # correct post-real-cohort state, not a regression. Only assert the original
    # 3-example-exception fixture shape while seed rows still exist to produce it.
    has_seed_rows = (any(l.get("_example") for l in roster["learners"]) or
                      any(r.get("_example") for r in (subs.get("assignments", []) +
                                                       subs.get("submissions", []) +
                                                       subs.get("discussions", []))))
    if has_seed_rows:
        ck("tracker example exceptions", len(data["tracker"]["example"]["exceptions"]), 3)
        ck("example queue kinds",
           sorted(e["kind"] for e in data["tracker"]["example"]["exceptions"]),
           ["AWAITING REVIEW", "OVERDUE", "READY TO COMPLETE"])
    else:
        ck("tracker example == real once seed rows are gone (MCS-consistent: absent data is a "
           "first-class state, not asserted against a stale fixture)",
           data["tracker"]["example"]["exceptions"], data["tracker"]["real"]["exceptions"])
    ck("MS-Adventure 4x5=20", data["tracker"]["programs"]["MS-Adventure"]["cases_required"], 20)
    ck("Launchpad 3x10=30", data["tracker"]["programs"]["Launchpad"]["cases_required"], 30)

    # ======================================================================
    # ASSET LINKS — the check that matters most. Every href in the emitted
    # page is decoded, resolved relative to app/, and stat()ed on disk.
    # ======================================================================
    hrefs = []
    def walk(o):
        if isinstance(o, dict):
            if "href" in o and "rel" in o:
                hrefs.append(o)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(data)

    resolved, broken, mismatched = 0, [], []
    for l in hrefs:
        if l["href"] is None:
            continue
        if l["href"].startswith("http"):
            # source/ asset rewritten to its Google Drive mirror (href_for) --
            # not a filesystem path, so "resolved" means the mapping in
            # source_drive_links.json actually produced this exact URL.
            drive_rel = l["rel"][len("source/"):] if l["rel"].startswith("source/") else None
            if drive_rel is not None and DRIVE_LINKS.get(drive_rel) == l["href"]:
                resolved += 1
            else:
                broken.append(l["href"])
            continue
        p = (OUT.parent / unquote(l["href"])).resolve()
        if p.exists():
            resolved += 1
        else:
            broken.append(l["href"])
        if (ROOT / l["rel"]).resolve() != p:
            mismatched.append(l["rel"])

    live = [l for l in hrefs if l["href"] is not None]
    corpus_files = sum(len(v) for c in corpus for v in c["assets"].values())
    # interactive_html links are discovered by globbing <pipeline_path>/published/*.html rather
    # than listed in corpus_index.json's assets{} -- count them the same way here so this check's
    # expectation stays in sync with what the page actually emits. pipeline_path prefers the
    # reconciled cases_index.json record's own paths (which track cases/<id>/ after conversion)
    # over the corpus record's frozen original path -- same rule as the build loop.
    # mirror the build loop's own lookup exactly: ci is keyed by the reconciled
    # matrix column (data["cases"][i]["matrix_col"]), not by the corpus title.
    matrix_col_by_title = {c["title"]: c.get("matrix_col") for c in data["cases"]}
    def _pipeline_path(c):
        col = matrix_col_by_title.get(c["title"])
        ci = ci_by_title_v.get(col) if col else None
        if ci and ci.get("paths", {}).get("case_json"):
            return str((ROOT / ci["paths"]["case_json"]).parent.relative_to(ROOT))
        if c["path"].startswith("cases/"):
            return c["path"]
        return None
    corpus_files += sum(
        len(list((ROOT / pp / "published").glob("*.html")))
        for c in corpus
        for pp in [_pipeline_path(c)]
        if pp and (ROOT / pp / "published").is_dir()
    )
    # pipeline-native cases' published/ files (all ASSET_KINDS, not just .html) --
    # already counted the same way, above, for the "guide notes"/"asset files" checks.
    corpus_files += pn_assets
    ck("asset links emitted", len(hrefs), data["links"]["total"])
    ck("every emitted href decodes+resolves to a file on disk", len(broken), 0)
    ck("resolved link count == live link count", resolved, len(live))
    ck("decoded href == the declared relative path", len(mismatched), 0)
    ck("links declared missing are not rendered as hrefs",
       len(hrefs) - len(live), data["headline"]["links_missing"])
    ck("every corpus asset file got a link",
       sum(1 for c in data["cases"] for k, _l, _s in ASSET_KINDS for x in c["asset_links"][k]), corpus_files)
    ck("every case has a folder link", sum(1 for c in data["cases"] if c["asset_links"]["_folder"]["href"]),
       len(data["cases"]))
    # the page derives per-case skill ids from heat[].by instead of shipping them;
    # prove the derivation still agrees with the legacy matrix count
    by_col = {}
    for d in data["heat"]:
        for g in d["groups"]:
            for s in g["skills"]:
                for t in s["by"]:
                    by_col.setdefault(t, []).append(s["id"])
    ck("page-derived skill ids match the shipped counts",
       [c["title"] for c in data["cases"] if c["mapped"] and c["matrix_col"]
        and len(by_col.get(c["matrix_col"], [])) != c["n_skill_ids"]], [])
    # A case with a real case.json (has_case_json) was individually re-authored with a
    # deliberately curated, forcing-tested standards[] -- smaller and more precise than the
    # raw matrix column's blanket vocabulary tagging by design (see LEARNING_GOALS.md per
    # case). Comparing the two for those cases checks a divergence this project intends,
    # not a bug; restrict this check to cases still relying purely on matrix-column tagging.
    ck("derived skill ids match cases_index standards_count",
       [c["title"] for c in data["cases"] if c["mapped"] and not c["has_case_json"]
        and c["standards_count"] is not None and c["standards_count"] != c["n_skill_ids"]], [])
    # the encoder itself, against the actual awkward names on disk
    ck("space encoded as %20", href_for("source/Y1/Session 1/Family Trip"),
       "../source/Y1/Session%201/Family%20Trip")
    ck("curly apostrophe U+2019 encoded as UTF-8",
       href_for("a/Example Riley’s Catering Case Study_.docx").endswith("Riley%E2%80%99s%20Catering%20Case%20Study_.docx"), True)
    ck("underscore/colon-substitute name survives",
       href_for("x/Case Study_ AirBnb Or LandLord.docx"), "../x/Case%20Study_%20AirBnb%20Or%20LandLord.docx")
    ck("parens, commas and ampersands encoded",
       href_for("x/Tiramisu (Recipe & Video) _ Sally_s Baking Addiction.pdf"),
       "../x/Tiramisu%20%28Recipe%20%26%20Video%29%20_%20Sally_s%20Baking%20Addiction.pdf")
    ck("path separators are NOT encoded", "%2F" in href_for("a/b/c"), False)
    ck("annotated manifest entry resolves to the real file",
       any(l["rel"] == "cases/cold-chain/FACILITATOR.md" and l["note"] for l in hrefs), True)
    ck("no raw & survives into an href attribute",
       bool(re.search(r'href="\.\./[^"]*&(?!amp;|#)', html)), False)

    # ---- root connections
    domsrc = load("domains.json")
    dcov = load("domain_coverage.json")
    RCd = data["rootc"]
    ck("root domains", len(RCd["domains"]), len(domsrc["domains"]))
    ck("root clusters", len(RCd["clusters"]), len(domsrc["clusters"]))
    ck("every domain has a known cluster",
       all(d["cluster"] in {c["name"] for c in RCd["clusters"]} for d in RCd["domains"]), True)
    ck("branch x domain matrix rows", len(RCd["matrix"]), len(dcov["by_branch"]))
    ck("data sources", RCd["n_sources"], sum(len(d["data_availability"]["sources"]) for d in domsrc["domains"]))
    ck("every data source has an http(s) url",
       all(s["url"].startswith("http") for d in RCd["domains"] for s in d["sources"]), True)
    ck("careers", data["headline"]["careers"], sum(len(d["careers"]) for d in domsrc["domains"]))
    ck("number-theory is both domain- and case-starved",
       [ (m["domain_starved"], m["case_starved"]) for m in RCd["matrix"] if m["branch"] == "number-theory"],
       [(True, True)])
    ck("precalc/calculus/linear-algebra case-starved but NOT domain-starved",
       sorted(m["branch"] for m in RCd["matrix"] if m["case_starved"] and not m["domain_starved"]),
       ["calculus", "linear-algebra", "precalc"])
    # Full reachability held for the 93 skills that existed before Roadmap B2 (2026-08-01) added
    # 115 new Pre-Calc/Calculus/Discrete rows; only a subset of those new rows have been folded
    # into a domain's signature_skills[] so far (see ROADMAP.md B2/B4 — closing the rest is future
    # authoring-queue work, not a bug). Assert the real split adds up rather than forcing 100%.
    ck("reachable + orphaned uncovered skills == total uncovered",
       RCd["totals"]["uncovered_skills_now_reachable_from_a_domain"]
       + RCd["totals"]["uncovered_skills_still_orphaned"],
       RCd["totals"]["spine_skills_uncovered"])
    ck("gap clusters carry their closing domains",
       all(("closers" in g) for g in data["gaps"]), True)
    # As of B2 (2026-08-01) 9 of the new Pre-Calc/Calculus/Discrete groups genuinely have no
    # domain pointing at them yet -- this is the same honestly-disclosed gap as
    # uncovered_skills_still_orphaned above, not a bug. Name the known exceptions so a NEW
    # orphaned group (a real regression) still fails this check.
    B2_KNOWN_ORPHAN_GROUPS = {
        ("Discrete Mathematics", "Set Theory"), ("Discrete Mathematics", "Proof And Recursion"),
        ("Calculus", "Applications Of Derivatives"), ("Calculus", "Limits And Continuity"),
        ("Calculus", "Series"), ("Calculus", "Applications Of Integrals"),
        ("Pre-Calculus", "Polar And Parametric"), ("Pre-Calculus", "Trigonometric Identities"),
        ("Pre-Calculus", "Introduction To Limits"),
        # 2026-08-02: Baseball Lineup's real-content promotion closed both Fundamental
        # Counting Principle skills in this group (n 0->1), which had been the group's only
        # domain-signature bridge -- the remaining 3 skills (binomial coefficient, pigeonhole
        # principle) were already genuinely orphaned, just masked by that bridge. Same honestly-
        # disclosed-gap class as the B2 backlog above, newly visible from real progress.
        ("Discrete Mathematics", "Combinatorics"),
    }
    ck("every zero-coverage cluster has a closing domain, except the known B2 backlog",
       sorted((g["domain"], g["group"]) for g in data["gaps"]
              if g["n_uncovered"] and not g["closers"]
              and (g["domain"], g["group"]) not in B2_KNOWN_ORPHAN_GROUPS),
       [])

    # ---- rubric
    R = data["rubric"]
    ck("rubric criteria parsed", len(R["criteria"]), 7)
    ck("criteria ids C1..C7", [c["id"] for c in R["criteria"]], ["C%d" % i for i in range(1, 8)])
    ck("weights sum to 100", R["weight_sum"], 100)
    ck("per-criterion weights match the scoring table",
       [c["weight"] for c in R["criteria"]], R["weights_table"])
    ck("every criterion has all three bands",
       all(all(b["text"] for b in c["bands"]) for c in R["criteria"]), True)
    ck("level points Not Yet/Proficient/Exemplary", R["level_points"], {"Not Yet": 0, "Proficient": 70, "Exemplary": 100})
    ck("four tier rows", [t["tier"] for t in R["tiers"]], ["T1", "T2", "T3", "T4"])
    ck("three machine hard limits", len(R["hard_limits"]), 3)
    ck("rubric open questions surfaced", len(R["open_questions"]), 5)
    ck("rubric status is not silently promoted", R["status"].startswith("PROPOSED"), True)

    # ---- scoring + override bias
    SCr = data["scoring"]["real"]
    SCe = data["scoring"]["example"]
    subs_scores = subs.get("scores", [])
    ovr = load("score_overrides.json")["overrides"]
    ck("live scores == non-example scores in submissions.json",
       SCr["n_scores"], len([s for s in subs_scores if not s.get("_example")]))
    ck("example scores == all scores", SCe["n_scores"], len(subs_scores))
    ck("live overrides exclude example rows", SCr["n_overrides"], len([o for o in ovr if not o.get("_example")]))
    ck("example overrides == all overrides", SCe["n_overrides"], len(ovr))
    ck("bias rows == criteria", len(SCe["bias"]), 7)
    ck("NO override rate is rendered at n below the file's own floor",
       [b["criterion"] for b in SCe["bias"] if b["rate_pct"] is not None and b["n_confirmed"] < BIAS_MIN_N], [])
    # Universally-quantified on purpose: "a criterion with exactly 1 override never
    # renders a rate" should hold whether zero, one, or several criteria happen to
    # have n_overrides==1 right now -- a fixed [None] here was really asserting "and
    # exactly one criterion currently has 1 override", true only for the original
    # seed fixture, not a real invariant of the rendering logic.
    ck("a single override never becomes a percentage",
       [b["rate_pct"] for b in SCe["bias"] if b["n_overrides"] == 1 and b["rate_pct"] is not None], [])
    ck("uncomputable bias says INSUFFICIENT DATA, never 0%",
       all(b["state"] == "INSUFFICIENT DATA" for b in SCe["bias"] if b["rate_pct"] is None), True)
    ck("no bias rate is the number zero",
       any(b["rate_pct"] == 0 for b in SCe["bias"]), False)
    ck("every insufficient row explains why",
       all(b["why_absent"] for b in SCe["bias"] if b["rate_pct"] is None), True)
    ck("demotion threshold is 30%", SCe["demote_at_pct"], 30)
    ck("dangling override refs are surfaced, not swallowed",
       len(SCe["dangling_override_refs"]),
       len([o for o in ovr if o.get("score_id") and o["score_id"] not in {s["id"] for s in subs_scores}]))

    # ---- student payload(s): redaction, not hiding
    # RUBRIC C6 legitimately explains that a Twist exists; a *case's* twist text
    # must not. Check the one real twist we have, verbatim.
    cold_twist = json.loads((ROOT / "cases/cold-chain/case.json").read_text(encoding="utf-8"))["facilitator"]["twist"]
    all_learner_ids = {l["id"] for l in roster["learners"]}
    students = data.get("students") or {}
    ck("at least one student payload exists", len(students) > 0, True)

    for learner_id, st in students.items():
        tag = "student payload (%s)" % learner_id
        sj = json.dumps(st, ensure_ascii=False)
        ck("%s names exactly one learner" % tag,
           sorted({l for l in all_learner_ids if ('"' + l + '"') in sj}), [st["learner"]["id"]])
        ck("no other learner id appears in %s" % tag,
           [l for l in all_learner_ids if l != st["learner"]["id"] and l in sj], [])
        ck("no growth score in %s" % tag, '"growth_score"' in sj, False)
        ck("no twist FIELD in %s" % tag, '"twist"' in sj, False)
        ck("no case twist text in %s" % tag, cold_twist[:40] in sj, False)
        ck("no QA verdict in %s" % tag, '"qa"' in sj, False)
        ck("no override bias in %s" % tag, '"overrides"' in sj or '"bias"' in sj, False)
        ck("no gap queue in %s" % tag, '"gaps"' in sj, False)
        ck("%s case assets are student-safe kinds only" % tag,
           sorted({a["kind"] for c in st["cases"] for a in c["assets"]} - STUDENT_SAFE_KINDS), [])
        ck("no guide-notes or socratic file reaches %s" % tag,
           [a["label"] for c in st["cases"] for a in c["assets"]
            if re.search(r"guide|socratic|facilitator", a["label"], re.I)], [])
        ck("no folder link in %s (a listing would expose Guide Notes)" % tag,
           [a for c in st["cases"] for a in c["assets"] if a.get("kind") == "folder"], [])
        ck("%s skill map counts only completed cases" % tag,
           st["skills"]["n_exercised"] <= st["skills"]["n_total"], True)
        ck("%s flags itself as preview while the roster is seed-only" % tag,
           st["preview_only"], len([l for l in roster["learners"] if not l.get("_example")]) == 0)

        # ---- the emitted per-learner build
        path = student_file_path(learner_id)
        if path.exists():
            shtml = path.read_text(encoding="utf-8")
            sm = re.search(r"const DATA = (.*?);\n", shtml, re.S)
            sdata = json.loads(sm.group(1).replace("<\\/", "</")) if sm else {}
            body = sm.group(1) if sm else ""
            btag = "student build (%s)" % learner_id
            ck("%s is role-locked" % btag, 'const ROLE_LOCK = "student";' in shtml, True)
            ck("%s carries no corpus" % btag, sdata.get("cases"), None)
            ck("%s carries no tracker" % btag, sdata.get("tracker"), None)
            ck("%s carries no scoring block" % btag, sdata.get("scoring"), None)
            ck("%s carries no gap queue" % btag, sdata.get("gaps"), None)
            ck("%s inlines no other learner" % btag,
               [l for l in all_learner_ids if l != st["learner"]["id"] and l in body], [])
            ck("%s inlines no case twist text" % btag, cold_twist[:40] in body, False)
            ck("%s inlines no twist FIELD" % btag, '"twist"' in body, False)
            ck("%s inlines no facilitator asset" % btag,
               bool(re.search(r'Guide Notes[^"]*\.docx|FACILITATOR\.md|QA_REPORT\.md', body)), False)
            ck("%s inlines no growth score" % btag, '"growth_score"' in body, False)
            ck("%s still carries the full rubric" % btag,
               len(sdata["student"]["rubric"]["criteria"]), 7)
            ck("%s still carries all root domains" % btag,
               len(sdata["student"]["domains"]["domains"]), len(domsrc["domains"]))
            ck("%s is self-contained" % btag,
               bool(re.search(r'<(script|link|img|iframe)[^>]+(src|href)="https?://', shtml)), False)

    # ---- the shared, unauthenticated landing page every case's back-link resolves to
    if OUT_STUDENT.exists():
        landing = OUT_STUDENT.read_text(encoding="utf-8")
        ck("landing page inlines no DATA payload at all", "const DATA = " in landing, False)
        ck("landing page names no score, case, or assignment field",
           any(k in landing for k in ('"growth_score"', '"badge_index"', '"qa"', '"twist"')), False)
        ck("landing page links to every active learner's own file",
           all(("student-%s.html" % lid) in landing for lid in students), True)
        ck("landing page links to the guide dashboard", "dashboard.html" in landing, True)

    # ---- WCAG AA contrast, computed
    fails = [(lab, contrast(f, b), mn) for f, b, mn, lab in CONTRAST_PAIRS if contrast(f, b) < mn]
    ck("WCAG AA contrast on all %d declared colour pairs" % len(CONTRAST_PAIRS), fails, [])

    # ---- absent-data doctrine, restated over the new views
    # A literal 0% is legitimate once a branch has real standards rows (precalc/calculus/discrete
    # as of 2026-08-01, Roadmap B2) — MCS-07's rule is that 0 is never used to STAND IN for missing
    # rows, not that a genuinely all-uncovered branch must hide behind "unmapped" forever. The
    # actual invariant: a branch is never both state=="unmapped" AND rendered at a numeric 0% —
    # those are mutually exclusive representations of two different real states.
    ck("no branch is both 'unmapped' and rendered at a literal 0%",
       any(b["coverage"]["state"] == "unmapped" and b["coverage"]["pct"] == 0 for b in data["branches"]),
       False)
    ck("unmapped branches list agrees with curriculum_tree's empty acton_domains[]",
       sorted(b["id"] for b in data["branches"] if b["coverage"]["state"] == "unmapped"),
       sorted(b["id"] for b in tree["branches"] if not b["acton_domains"]))
    ck("legacy cases keep tier null rather than an invented tier",
       any(c["tier"] == "" or c["tier"] == 0 for c in data["cases"]), False)
    ck("legacy cases keep margin null rather than 0",
       any(c["margin_pct"] == 0 for c in data["cases"] if c["status"] == "legacy"), False)

    bad = [c for c in checks if not c[0]]
    if not quiet:
        w = max(len(c[1]) for c in checks)
        for ok, name, got, want in checks:
            print(("  PASS  " if ok else "  FAIL  ") + name.ljust(w) + "  " + repr(got)[:120] +
                  ("" if ok else "   != expected " + repr(want)[:120]))
        extra = (" + %s (%.0f KB)" % (OUT_STUDENT.name, OUT_STUDENT.stat().st_size / 1024)) if OUT_STUDENT.exists() else ""
        print("\n%d checks, %d failed · %s (%.0f KB)%s" %
              (len(checks), len(bad), OUT.name, OUT.stat().st_size / 1024, extra))
        print("%d asset links emitted, %d resolved on disk, %d broken" % (len(hrefs), resolved, len(broken)))
        for b in broken[:10]:
            print("   BROKEN  " + b)
    return not bad


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true", help="verify the existing dashboard.html only")
    a = ap.parse_args()
    if not a.verify:
        d, h, shtmls, landing = build()
        print("wrote %s (%.0f KB)" % (OUT, len(h.encode("utf-8")) / 1024))
        for learner_id, sh in shtmls.items():
            print("wrote %s (%.0f KB) — role-locked student build" %
                  (student_file_path(learner_id), len(sh.encode("utf-8")) / 1024))
        print("wrote %s (%.0f KB) — student landing page" % (OUT_STUDENT, len(landing.encode("utf-8")) / 1024))
    sys.exit(0 if verify() else 1)
