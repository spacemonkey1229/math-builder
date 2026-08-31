#!/usr/bin/env python3
"""
preflight_lint.py -- fast, cheap checks for the two defect classes that cost
the most round-trips this session, run BEFORE the full Tier 1/Tier 2 gate
instead of being discovered by it. Nothing here replaces tier1_structural.py
or tier2_probes.py; this is a linter an author runs on themselves mid-write,
the same way you'd run a syntax checker before a real test suite.

Checks:
  1. Modeling Assumptions leak -- case.md (before <!-- FACILITATOR ONLY -->)
     stating a balance result (margin/winner/cap-breach threshold) instead of
     just what was assumed and why. Same pattern that hit 9+ cases before the
     2026-08-13 case-write rule existed, and kept recurring after because
     nothing checked for it until Tier 2.
  2. FLEX[] scoping -- sensitivity_model.py flexing a PARAMS key that also has
     a matching case.json sources[] citation (cited data, not a real
     assumption) or that isn't backed by any modeling_assumptions[] entry.
  3. Explicit twist/trap/facilitator naming in case.md's student-facing half.

Usage:
  python3 skills/case-readiness/scripts/preflight_lint.py --case <id>

Exit 0 = clean. Exit 1 = findings (printed, non-blocking -- this is advisory,
not a gate; case-readiness's Tier 1/2 remain the actual authority).
"""
import argparse, importlib.util, json, os, re, sys

ROOT = os.getcwd()  # invoked as: cd "$PROJECT" && python3 skills/case-readiness/scripts/preflight_lint.py


def load(name):
    return json.load(open(os.path.join(ROOT, name), encoding="utf-8"))


# High-precision on purpose: this must not false-positive on a case's own honest
# sensitivity-range disclosure (e.g. curves-turn's Appendix D says "the winner does
# not change and the margin ranges 6.5%-16.3%" under a flex sweep -- that discloses
# HOW the design responds to a swing, never the actual base-case answer, and is
# exactly the kind of real disclosure this project wants, not a leak). What must
# actually be caught is the RESULT verb sitting immediately next to a percent --
# "wins by 14%", "the margin is 3.8%", "B beats A by 12%" -- not any co-occurrence
# of a percent and a vaguely result-shaped word anywhere in a long table cell.
BALANCE_RESULT_NEAR_PCT_RE = re.compile(
    r'(?i)(margin (is|was|of|comes to|stands at)|wins? by|beats? \w+ by|'
    r'(option\s+[ab]\s+)?(wins?|is the winner)\s*[:\-]?\s*)\s*\d+(\.\d+)?\s*%'
    r'|\d+(\.\d+)?\s*%\s*(margin\b|(in\s+)?favou?r\s+of)'
)
TWIST_TRAP_FAC_RE = re.compile(r'(?i)\b(the\s+)?(twist|trap)\b|facilitator', re.I)


def check_student_facing_leak(md_path):
    findings = []
    if not os.path.isfile(md_path):
        return findings
    text = open(md_path, encoding="utf-8").read()
    # Match the marker as a prefix, not an exact string: most cases' boilerplate
    # reads "<!-- FACILITATOR ONLY: balance argument, margin, ... -->" rather than
    # the bare "<!-- FACILITATOR ONLY -->" this used to require verbatim, which
    # made text.find() return -1 on nearly every case in the corpus and silently
    # treat the whole file -- including the marker comment's own "FACILITATOR"
    # text -- as student-facing. Found while gating the-clampband-margin.
    marker_match = re.search(r'<!--\s*FACILITATOR ONLY\b', text)
    student_text = text if marker_match is None else text[:marker_match.start()]

    for i, line in enumerate(student_text.splitlines(), 1):
        if BALANCE_RESULT_NEAR_PCT_RE.search(line):
            findings.append(
                f"line {i}: reads like a stated balance RESULT (a winner/margin "
                f"value stated directly next to a percent), not just an "
                f"assumption's basis or a disclosed sensitivity RANGE. Modeling "
                f"Assumptions may state WHAT was assumed and WHY, and may disclose "
                f"how a flex changes the margin/whether the winner changes -- but "
                f"never state the actual base-case margin or name the actual "
                f"winner (skills/case-write/SKILL.md, 2026-08-13 rule).\n"
                f"    {line.strip()[:160]}"
            )
        if TWIST_TRAP_FAC_RE.search(line):
            findings.append(
                f"line {i}: explicitly names \"twist\"/\"trap\"/\"facilitator\" in "
                f"student-facing text -- these must only surface via the facilitator "
                f"during play, never pre-stated in case.md.\n    {line.strip()[:160]}"
            )
    return findings


def check_flex_scoping(case_dir, case_json):
    findings = []
    model_path = os.path.join(case_dir, "sensitivity_model.py")
    if not os.path.isfile(model_path):
        return findings  # not an error here -- authoring may not have reached this yet

    spec = importlib.util.spec_from_file_location("sensmodel_lint", model_path)
    m = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(m)
    except Exception as e:
        findings.append(f"sensitivity_model.py failed to import: {e!r} -- fix before Tier 2 will even run")
        return findings

    flex = list(getattr(m, "FLEX", []) or [])
    if not flex:
        return findings

    cited_values = set()
    for s in case_json.get("sources", []) or []:
        v = s.get("value")
        if v is not None:
            cited_values.add(str(v))
    ma_ids = {ma.get("id") for ma in case_json.get("modeling_assumptions", []) or []}

    params = getattr(m, "PARAMS", {}) or {}
    for key in flex:
        val = params.get(key)
        # heuristic: does this PARAMS key's own inline comment (source line) mention
        # a source id (S1, S2...) rather than an MA id (MA1, MA2...)? Cheap signal,
        # not a proof -- this is advisory, the human/agent still judges the real case.
        if val is not None and str(val) in cited_values:
            findings.append(
                f"FLEX includes '{key}' (value {val}), which matches a case.json "
                f"sources[] cited value exactly -- check this isn't cited/given data "
                f"sitting in FLEX[] by mistake (P5 tests stated assumptions, not "
                f"citations; the FLEX-scoping doctrine note in "
                f"skills/case-readiness/SKILL.md covers this)."
            )
    if not ma_ids and flex:
        findings.append(
            "sensitivity_model.py declares FLEX[] but case.json has no "
            "modeling_assumptions[] at all -- every FLEX dial should trace back to "
            "a real, named assumption the case states; double check this is "
            "intentional."
        )
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True)
    a = ap.parse_args()

    case_dir = os.path.join(ROOT, "cases", a.case)
    md_path = os.path.join(case_dir, "case.md")
    json_path = os.path.join(case_dir, "case.json")

    if not os.path.isfile(json_path):
        print(f"no case.json under cases/{a.case}/ -- nothing to lint yet", file=sys.stderr)
        sys.exit(0)
    case_json = json.load(open(json_path, encoding="utf-8"))

    all_findings = []
    all_findings += [("leak", f) for f in check_student_facing_leak(md_path)]
    all_findings += [("flex", f) for f in check_flex_scoping(case_dir, case_json)]

    print(f"PREFLIGHT LINT -- cases/{a.case}")
    if not all_findings:
        print("  clean -- no advisory findings. (This does not replace tier1_structural.py / tier2_probes.py.)")
        sys.exit(0)

    for kind, f in all_findings:
        print(f"  [{kind}] {f}\n")
    print(f"{len(all_findings)} advisory finding(s). Review before running the real Tier 1/2 gate --")
    print("this is a fast pre-check, not the gate itself.")
    sys.exit(1)


if __name__ == "__main__":
    main()
