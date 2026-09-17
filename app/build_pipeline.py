#!/usr/bin/env python3
"""
build_pipeline.py — derive readmodel/pipeline_status.json, a live map of every
case (and every un-promoted concept) against the real pipeline stages.

Read-only over cases/, readmodel/cases_index.json and readmodel/standards_spine.json.
Writes only readmodel/pipeline_status.json. Never touches a frozen read-model file.

Live-runs skills/case-readiness/scripts/tier1_structural.py for every case that has
a case.json, rather than trusting case.json.qa (which this run found is not even a
consistent shape across the two real cases today — cold-chain uses
{state, note, case_md_sha256}, tide-window uses case-write's template
{verdict, run_on, blockers_open, case_md_sha256}). A live run sidesteps that
inconsistency and matches this project's own stated bias for verifying over trusting
a recorded field (see DOCTRINE_LEDGER's repeated "no ✅ without a QA report" rule,
applied here to a status board instead of a case).

Stages (the pipeline as it actually exists today, not aspirational):
  concepting  -> a concept sheet entry with no cases/<id>/ directory yet, OR a
                 legacy case whose dilemma isn't binary (SPEC §1.4) -- it needs
                 the same kind of decision a concept needs before drafting means
                 anything: which two options, exactly.
  drafting    -> case.json.status == "draft" (case-write output), OR a legacy
                 case with real usable narrative content that hasn't been
                 converted into case.md/case.json format yet. Same next real
                 step either way: get it to a case-research-ready draft.
  research    -> case.json.status == "researched"      (case-research output)
  readiness   -> case.json.status == "qa", OR any case with a case.json that has
                 been through case-write+case-research and is now gated by
                 case-readiness (this is where a live Tier 1 run's blocker/gap
                 counts actually matter)
  promotion   -> case.json.status == "published" (case-publish output;
                 promoted into cases_index.json/standards_spine.json)
  verified    -> a filed, filled cases/<id>/runs/RUN_*.md exists (Tier 3, MCS-29)

ONE board, not two. Earlier same-day version of this script kept the 55 legacy
corpus cases in a separate scorecard, off the stage board entirely -- user
explicitly said "I really don't want two pipelines." Fixed: every legacy case
now gets a real stage placement (via readmodel/legacy_readiness.json's
structural/facilitation signal, same triage logic as the "near ready / needs
redesign" categories worked out interactively), tagged origin:"legacy" so a
card still shows where it came from. Only genuine file-level problems (an
unreadable case doc, a missing core section) are held out as explicit,
minimized exceptions -- 2 of 55 today, not a parallel universe.

Usage:
  python3 app/build_pipeline.py
  python3 app/build_pipeline.py --verify   # check without rewriting
"""
import argparse, glob, json, os, re, subprocess, sys, datetime, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(name):
    return json.load(open(os.path.join(ROOT, "readmodel", name), encoding="utf-8"))


CONCEPT_HDR = re.compile(
    r"^### (C\d+) — (.+?)\s+·\s+score\s+([\d.]+)\s+·\s+tier\s+(\S+)", re.M
)


def parse_concept_sheets():
    concepts = []
    for path in sorted(glob.glob(os.path.join(ROOT, "cases", "_concepts", "*.md"))):
        fname = os.path.basename(path)
        text = open(path, encoding="utf-8").read()
        for m in CONCEPT_HDR.finditer(text):
            cid, title, score, tier = m.groups()
            concepts.append({
                "concept_id": cid,
                "title": title.strip(),
                "score": float(score),
                "tier": tier,
                "sheet": fname,
            })
    return concepts


TIER1_VERDICT_RE = re.compile(r"VERDICT:\s*(\S+)\s*\((\d+) blockers?, (\d+) gaps?\)")
TIER1_CHECKS_RE = re.compile(r"checks run:\s*(\d+)\s*PASS\s*(\d+)\s*·\s*GAP\s*(\d+)\s*·\s*FAIL\s*(\d+)")


def run_tier1(case_id):
    script = os.path.join(ROOT, "skills", "case-readiness", "scripts", "tier1_structural.py")
    try:
        p = subprocess.run(
            [sys.executable, script, "--case", case_id],
            cwd=ROOT, capture_output=True, text=True, timeout=60,
        )
    except Exception as e:
        return {"ran": False, "error": str(e)}
    out = p.stdout + p.stderr
    vm = TIER1_VERDICT_RE.search(out)
    cm = TIER1_CHECKS_RE.search(out)
    if not vm:
        return {"ran": False, "error": "no VERDICT line in output", "raw_tail": out[-400:]}
    return {
        "ran": True,
        "verdict": vm.group(1),
        "blockers": int(vm.group(2)),
        "gaps": int(vm.group(3)),
        "checks_run": int(cm.group(1)) if cm else None,
        "checks_pass": int(cm.group(2)) if cm else None,
    }


def published_date(case_id):
    """case-publish stamps published/MANIFEST.json.built_on every time it rebuilds
    the packet -- the real, already-tracked publication/last-build date. Read it
    instead of guessing from git history, which would only tell us when the file
    last changed, not when it was actually (re)published."""
    manifest_path = os.path.join(ROOT, "cases", case_id, "published", "MANIFEST.json")
    if not os.path.exists(manifest_path):
        return None
    try:
        return json.load(open(manifest_path, encoding="utf-8")).get("built_on")
    except Exception:
        return None


def has_run_report(case_id):
    runs_dir = os.path.join(ROOT, "cases", case_id, "runs")
    if not os.path.isdir(runs_dir):
        return False
    for fn in os.listdir(runs_dir):
        if fn.startswith("RUN_") and fn.endswith(".md"):
            text = open(os.path.join(runs_dir, fn), encoding="utf-8").read()
            # a blank template has an empty Section 8 attribution table; a real
            # filed report has at least one completed row. Cheap proxy: a filled
            # Guide/Date field in Section 1's table.
            if re.search(r"\|\s*Guide\s*\|\s*\S", text) and not re.search(r"\|\s*Guide\s*\|\s*\|", text):
                return True
    return False


def stage_for_case(cid, cj, tier1, run_report_filed):
    status = cj.get("status")
    if status == "published" and run_report_filed:
        return "verified"
    if status == "published":
        return "promotion"
    if status == "qa":
        return "readiness"
    if status == "researched":
        # once a case.json exists and case-research has run, the NEXT real gate
        # is case-readiness -- researched cases sit in "readiness" the moment
        # they're gate-checked, but stay labeled "research" until a human/QA
        # pass actually starts working the gate. We use status literally here
        # rather than guess intent.
        return "research"
    if status == "draft":
        return "drafting"
    return "readiness" if tier1.get("ran") else "drafting"


def next_action_for(stage, cj, tier1, run_report_filed):
    if stage == "concepting":
        return "Approve this concept, then run case-write."
    if stage == "drafting":
        return "Run case-research to fill open {{NEEDS_SOURCE}} placeholders."
    if stage == "research":
        return "Run case-readiness (Tier 1) — structural gate."
    if stage == "readiness":
        if not tier1.get("ran"):
            return "Tier 1 could not be run live — check the case manually."
        if tier1["blockers"] > 0:
            return f"Resolve {tier1['blockers']} Tier 1 blocker(s), then re-run case-readiness."
        qa_state = (cj.get("qa") or {}).get("state")
        if qa_state == "TIER2_PASS":
            return "Tier 1 + Tier 2 both clean (qa.state: TIER2_PASS) — ready for case-publish."
        return "Tier 1 clean — build a sensitivity_model.py, then run Tier 2 probes."
    if stage == "promotion":
        if tier1.get("ran") and tier1.get("blockers", 0) > 0:
            return f"Resolve {tier1['blockers']} Tier 1 blocker(s) (re-run flagged them post-publish), then re-run case-readiness."
        return "Run a Tier 3 human dry-run and file a RUN_REPORT to reach VERIFIED."
    if stage == "verified":
        return "None — this case has cleared every gate this pipeline has."
    return "—"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true")
    a = ap.parse_args()

    concepts_all = parse_concept_sheets()
    ci = load("cases_index.json")

    # which concept titles already have a real case dir (graduated out of concepting)
    case_dirs = sorted(
        d for d in os.listdir(os.path.join(ROOT, "cases"))
        if d != "_concepts" and os.path.isfile(os.path.join(ROOT, "cases", d, "case.json"))
    )
    # legacy_readiness.json's titles come from folder names, filesystem-safe
    # (e.g. "A Coach_s Dilemma"); a converted case.json carries the real
    # apostrophe. Same normalization build_legacy_readiness.py/build_dashboard.py
    # already use for exactly this reason -- without it, a genuinely-converted
    # case never matches its legacy row and shows twice (once real, once stale
    # "not yet converted").
    def norm_apos(s):
        return (s or "").replace("_s", "'s")

    # A folder-derived legacy title is filesystem-safe ASCII; the converted case.json
    # can carry real accents ("Caribbean Internet Café" vs "Caribbean Internet Cafe").
    # Found 2026-08-22: this silently duplicated an already-published, TIER2_PASS case
    # onto the board as "legacy-untouched, drafting stage, MODERATE WORK" because the
    # exact-match/norm_apos check below never saw the accent as the same title. Strip
    # diacritics on both sides so a genuinely-converted case doesn't linger stale.
    def strip_accents(s):
        return "".join(ch for ch in unicodedata.normalize("NFKD", s or "") if not unicodedata.combining(ch))

    # Same class of bug as the accent case above, different cause: the legacy
    # folder title ("Stock Market", source/Y3/Additional/Stock Market/) and the
    # case doc's own title ("Investment Portfolio", used both by case-write's
    # cases/investment-portfolio/case.json and by the pre-existing
    # standards_spine.json tagging) are genuinely different strings for the same
    # case. Mirrors the TITLE_ALIASES fix in build_legacy_readiness.py.
    LEGACY_TITLE_ALIASES = {
        "Stock Market": "Investment Portfolio",
        "Movie Producer": "Movie Executive",
        "College Football Playoff Committee": "Playoff Committee",
        "Medical Statician": "Medical Statistician",
        "AirBnb": "AirBnb Or Landlord",
    }

    written_titles = set()
    cases_out = []
    for cid in case_dirs:
        cj = json.load(open(os.path.join(ROOT, "cases", cid, "case.json"), encoding="utf-8"))
        written_titles.add(cj.get("title"))
        tier1 = run_tier1(cid)
        rr = has_run_report(cid)
        stage = stage_for_case(cid, cj, tier1, rr)
        cases_out.append({
            "id": cid,
            "title": cj.get("title"),
            "tier": cj.get("tier"),
            "band": cj.get("band"),
            "status": cj.get("status"),
            "stage": stage,
            "tier1": tier1,
            "run_report_filed": rr,
            "concept_sheet": cj.get("concept_sheet"),
            "new_coverage_count": len(cj.get("new_coverage") or []),
            "next_action": next_action_for(stage, cj, tier1, rr),
            "published_date": published_date(cid) if stage in ("promotion", "verified") else None,
        })

    # a concept sheet's title and the finished case.json's title sometimes drift
    # cosmetically -- a dropped leading "The " ("The Roofline Call" vs "Roofline
    # Call") or a capitalization difference ("Reroute or Wait" vs "Reroute Or
    # Wait"). Normalize both sides (strip a leading article, casefold) so a
    # genuinely-written case doesn't linger on the concepting board under a
    # near-miss spelling of its own title.
    def norm_title(s):
        s = (s or "").strip()
        if s.lower().startswith("the "):
            s = s[4:]
        return s.casefold()

    # Same class of drift as LEGACY_TITLE_ALIASES above, but between a concept
    # sheet's working title and the finished case.json's title, where the
    # words themselves (not just a leading article or accent) changed during
    # authoring. Found 2026-09-01: C9 "Redrawing the Lines" was written and
    # published as cases/redrawing-lines/ with title "Redrawing Lines" (an
    # internal "the" dropped, not a leading one norm_title already strips) --
    # this left a real, already-published case showing as an unwritten
    # concept on the board.
    CONCEPT_TITLE_ALIASES = {
        "redrawing the lines": "redrawing lines",
    }
    written_titles_norm = {norm_title(t) for t in written_titles}
    concepts_out = [c for c in concepts_all
                    if CONCEPT_TITLE_ALIASES.get(norm_title(c["title"]), norm_title(c["title"]))
                    not in written_titles_norm]
    concepts_out.sort(key=lambda c: -c["score"])

    pipeline_published_ids = {c["id"] for c in cases_out}
    # cases_index entries with status "published"/"qa" that don't have their own
    # cases/<id>/case.json (shouldn't normally happen, but surfaced rather than
    # silently dropped if it does)
    index_only = [c for c in ci.get("cases", [])
                  if c.get("status") not in ("legacy",) and c.get("id") not in pipeline_published_ids]

    # ---- fold the 55 legacy cases into the SAME board, one pipeline -----
    lr_path = os.path.join(ROOT, "readmodel", "legacy_readiness.json")
    legacy_exceptions = []
    legacy_source_total = 0
    legacy_converted_titles = []
    if os.path.exists(lr_path):
        lr = json.load(open(lr_path, encoding="utf-8"))
        legacy_source_total = len(lr["cases"])
        for row in lr["cases"]:
            row_title = row["title"].strip()
            row_title_aliased = LEGACY_TITLE_ALIASES.get(row_title, row_title)
            if (row_title in written_titles or norm_apos(row_title) in written_titles
                    or strip_accents(row_title) in {strip_accents(t) for t in written_titles}
                    or row_title_aliased in written_titles):
                # already converted -- a real cases/<id>/case.json exists and is
                # already in cases_out above with its own live stage/tier1. Do not
                # also list the pre-conversion legacy row, or the case appears
                # twice on the board (once real, once stale "not yet converted").
                legacy_converted_titles.append(row["title"])
                continue
            if "case_doc_error" in row:
                legacy_exceptions.append({"title": row["title"], "path": row["path"],
                                           "reason": "case doc unreadable: " + row["case_doc_error"]})
                continue
            s = row.get("structure", {})
            f = row.get("facilitation", {})
            base_ok = s.get("has_overview") and s.get("has_background") and \
                s.get("has_dilemma_heading") and s.get("has_challenges_heading")
            if not base_ok:
                legacy_exceptions.append({"title": row["title"], "path": row["path"],
                                           "reason": "missing a core SPEC §1 section (Overview/Background/Dilemma/Challenges)"})
                continue
            binary_ok = s.get("has_binary_options") and not s.get(
                "has_third_option (should be 0 -- SPEC requires strictly binary)", s.get("has_third_option"))
            guide_ok = row.get("has_guide") and f.get("has_lessons_learned")
            tagged = row.get("standards_tagged")
            if not binary_ok:
                stage, effort = "concepting", "NEEDS A REAL DESIGN DECISION"
                next_act = ("Not strictly binary (SPEC §1.4) — lock the dilemma down to exactly two "
                            "named options before drafting means anything. Same kind of decision a "
                            "brand-new concept needs.")
            elif guide_ok and tagged:
                stage, effort = "drafting", "NEAR READY"
                next_act = ("Structurally sound + Guide Notes with Lessons Learned + already standards-tagged. "
                             "Convert to case.md/case.json, update Challenge boilerplate to the current locked "
                             "text, build the mandatory final standards appendix, reformat Guide Notes to the "
                             "11-anchor ladder. Interactive HTML/glossary/sensitivity model still needed for "
                             "Tier 1 — a real, separate lift even with the A7 shell.")
            elif guide_ok or tagged:
                stage, effort = "drafting", "MODERATE WORK"
                next_act = ("Structurally sound but missing " +
                             ("standards tagging" if guide_ok else "a Guide Notes with Lessons Learned") +
                             " — close that gap, then treat the same as a near-ready case.")
            else:
                stage, effort = "drafting", "MORE WORK"
                next_act = "Structurally sound but no usable Guide Notes and not standards-tagged — both needed before this is really a drafting-stage case."
            cid = "legacy-" + re.sub(r"[^a-z0-9]+", "-", row["title"].lower()).strip("-")
            cases_out.append({
                "id": cid, "title": row["title"], "tier": None, "band": None,
                "status": "legacy-untouched", "stage": stage, "origin": "legacy",
                "effort_tier": effort,
                "tier1": {"ran": False},
                "run_report_filed": False, "concept_sheet": None, "new_coverage_count": None,
                "next_action": next_act,
                "legacy_signal": {"has_guide": row.get("has_guide"), "has_socratic_plan": row.get("has_socratic_plan"),
                                   "standards_tagged": tagged, "mentions_twist": f.get("mentions_twist"),
                                   "has_third_option": s.get("has_third_option")},
            })

    stage_order = ["concepting", "drafting", "research", "readiness", "promotion", "verified"]
    counts = {s: 0 for s in stage_order}
    for c in cases_out:
        counts[c["stage"]] += 1
    counts["concepting"] += len(concepts_out)

    out = {
        "_schema": {
            "_comment": "DERIVED — regenerate with app/build_pipeline.py. Never hand-edit. "
                        "Tier 1 status per case is LIVE (re-run at generation time), not read "
                        "from case.json.qa, because that field is not even a consistent shape "
                        "across the two real cases yet (cold-chain vs. tide-window) — see "
                        "DOCTRINE_LEDGER 2026-08-01.",
            "stage_order": stage_order,
            "stage_definitions": {
                "concepting": "A concept sheet entry (case-brainstorm output) with no cases/<id>/ directory yet, OR a legacy case whose dilemma isn't strictly binary (SPEC §1.4) and needs that design decision made first.",
                "drafting": "case.json.status == 'draft' (case-write output), OR a legacy case with real usable narrative content not yet converted into case.md/case.json format. See legacy_signal{}/effort_tier for how much work that conversion actually needs — 'NEAR READY' still means real per-case authoring (boilerplate, deliverables, facilitator reformatting, interactive HTML/glossary), not a few clicks.",
                "research": "case.json.status == 'researched' — case-research has filled placeholders with cited data or stated Modeling Assumptions.",
                "readiness": "case.json.status == 'qa' — case-readiness's Tier 1/2/3 gate is the active blocker. tier1{} below is a live re-run, not a cached field.",
                "promotion": "case.json.status == 'published' — case-publish has built the packet and promoted the case into cases_index.json/standards_spine.json. published_date is read from published/MANIFEST.json.built_on (the last case-publish rebuild), so a freshness check can be run against it.",
                "verified": "A filed, filled cases/<id>/runs/RUN_*.md exists (Tier 3, MCS-29) — the only state that may carry a checkmark in DOCTRINE_LEDGER.",
            },
        },
        "_generated_at": None,
        "stage_counts": counts,
        "concepts": concepts_out,
        "cases": cases_out,
        "index_only_cases": index_only,
        "legacy_total": legacy_source_total,
        "legacy_exceptions": legacy_exceptions,
        "legacy_converted_titles": legacy_converted_titles,
    }

    outpath = os.path.join(ROOT, "readmodel", "pipeline_status.json")
    if a.verify:
        if not os.path.exists(outpath):
            print("MISSING readmodel/pipeline_status.json — run without --verify first")
            sys.exit(1)
        existing = json.load(open(outpath, encoding="utf-8"))
        existing_cmp = dict(existing); existing_cmp.pop("_generated_at", None)
        new_cmp = dict(out); new_cmp.pop("_generated_at", None)
        if existing_cmp != new_cmp:
            print("STALE — readmodel/pipeline_status.json does not match a fresh derivation")
            sys.exit(1)
        print("pipeline_status.json is current")
        print(json.dumps(counts, indent=1))
        return

    out["_generated_at"] = datetime.date.today().isoformat()
    json.dump(out, open(outpath, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"wrote {outpath}")
    print(json.dumps(counts, indent=1))
    for c in cases_out:
        t1 = c["tier1"]
        t1s = (f"{t1['verdict']} ({t1['blockers']}b/{t1['gaps']}g)" if t1.get("ran")
               else ("legacy, not yet converted (" + c.get("effort_tier", "?") + ")" if c.get("origin") == "legacy"
                     else "tier1 did not run"))
        print(f"  {c['id']:28s} stage={c['stage']:10s} {t1s}")
    print(f"  concepts (not yet written): {len(concepts_out)}")
    print(f"  legacy total: {legacy_source_total} -- {len(legacy_converted_titles)} converted to a real case, "
          f"{len(legacy_exceptions)} exception(s), rest folded into the board above")


if __name__ == "__main__":
    main()
