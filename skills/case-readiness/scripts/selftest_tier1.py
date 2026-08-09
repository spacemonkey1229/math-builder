#!/usr/bin/env python3
"""
REGRESSION TEST for tier1_structural.py.

Copies a real case into a tempdir, mutates it, and asserts Tier 1 catches (or,
for a false-positive test, does NOT catch) each. Each mutation reproduces a
real defect that either the legacy case-qa script or an earlier version of
this script let through — the point of the test is that these specifically
cannot regress.

    python3 skills/case-readiness/scripts/selftest_tier1.py --project "$PROJECT"

Exit 0 = all assertions hold.  Exit 1 = a fix has regressed.
Run this after any edit to tier1_structural.py.  A gate with no test is a gate
you trust for no reason.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
T1 = os.path.join(HERE, 'tier1_structural.py')

# Each mutation targets one or more files in a case's directory. `setup(paths)`
# receives {'md': <case.md text>, 'json': <case.json dict>, 'html': <first
# published/*.html text, or None>} and returns the same shape with whichever
# entries it changed (omit or return unchanged for anything it doesn't touch).
MUTATIONS = [
    # (name, case, setup(paths) -> paths, expect_match: bool, regex the report MUST/MUST-NOT contain, why)
    ("numeral-form drift hides a rewritten Challenge", 'cold-chain',
     lambda p: {**p, 'md': p['md'].replace(
         '2.) Post 250 or more "excellent" words pitching a firm stance',
         '**2.** Post 200 or more "excellent" words pitching a soft stance')},
     True,
     [r'T1-04.*Challenge 2 is NOT verbatim', r'T1-05.*numeral form'],
     "legacy regex required `N.)`, so `**2.**` matched nothing and the whole diff "
     "examined zero sections (Cold Chain QA_REPORT B3)"),

    ("separator-run vocabulary label is off-spine", 'cold-chain',
     lambda p: {**p, 'md': p['md'].replace(
         'Volume · Surface Area · Prism ·', 'Volume · Surface Area · Prisms ·')},
     True,
     [r"T1-07.*NOT verbatim spine labels.*Prisms"],
     "legacy check read only '- ' bullets, so the 14 middot-separated Vocabulary "
     "labels were never checked against the spine at all"),

    ("unreferenced appendix whose title says 'how to'", 'cold-chain',
     lambda p: {**p, 'md': p['md'] + "\n---\n\n## Appendix H: How To Read The Circuit Table\n\n"
                     "A short explainer that nothing references.\n"},
     True,
     [r"T1-06.*Appendix H.*ORPHAN"],
     "legacy check did `if 'how to' in title: continue`, exempting ANY appendix "
     "whose title mentions 'how to' from the orphan graph"),

    ("legacy case claims verbatim real data with no sources[] backing it", 'cardiology',
     lambda p: {**p, 'json': {**p['json'], 'sources': []}},
     True,
     [r"T1-08.*verbatim.*publicly verifiable.*sources\[\]"],
     "T1-08 only ever checked that explicit [S1]-style citation markers resolve to a "
     "sources[] row — a case with zero markers and an empty sources[] trivially passed even "
     "while its own legacy_conversion_note claimed the data was 'verbatim' from a real, named "
     "source (this exact gap is how Cardiology's fabricated clinical-trial table reached "
     "TIER1_PASS, 2026-08-04)"),

    ("small round margin_pct false-positives against CSS/prose (must NOT block)", 'cardiology',
     lambda p: {**p,
                'json': {**p['json'], 'balance': {**p['json']['balance'], 'margin_pct': 5.0}},
                'html': (p['html'] or '').replace(
                    '<style>', '<style>.selftest-mutation{margin:5px} /* Year 5 check */', 1)},
     False,
     [r"T1-18.*MCS-37.*leaks the answer"],
     "the T1-18 leak-check's bare-digit regex used to fire on ANY standalone '5' in the whole "
     "published HTML, including CSS pixel values, SVG path coordinates, and ordinary phrases "
     "like '5-year'/'Year 5' — none of which are the balance_test verdict being leaked "
     "(2026-08-04)"),

    ("a genuine literal margin leak in prose (must still block)", 'cardiology',
     lambda p: {**p,
                'json': {**p['json'], 'balance': {**p['json']['balance'], 'margin_pct': 5.0}},
                'html': (p['html'] or '').replace(
                    '<section id="dilemma">',
                    '<section id="dilemma"><p>Selftest leak: the real margin is 5.0% higher.</p>',
                    1)},
     True,
     [r"T1-18.*MCS-37.*leaks the answer"],
     "narrowing the leak-check to avoid the CSS/prose false-positive above must not also blind "
     "it to an actual literal answer printed in the page"),
]


def build(project, case):
    tmp = tempfile.mkdtemp(prefix='t1-selftest-')
    for d in ('cases', 'readmodel', 'doctrine'):
        shutil.copytree(os.path.join(project, d), os.path.join(tmp, d))
    case_dir = os.path.join(tmp, 'cases', case)
    mdp = os.path.join(case_dir, 'case.md')
    jsonp = os.path.join(case_dir, 'case.json')
    pub = os.path.join(case_dir, 'published')
    htmlp = None
    if os.path.isdir(pub):
        htmls = [f for f in os.listdir(pub) if f.lower().endswith('.html')]
        if htmls:
            htmlp = os.path.join(pub, htmls[0])
    return tmp, {'md': mdp, 'json': jsonp, 'html': htmlp}


def load_paths(paths):
    with open(paths['md'], encoding='utf-8') as fh:
        md = fh.read()
    with open(paths['json'], encoding='utf-8') as fh:
        j = json.load(fh)
    html = None
    if paths['html']:
        with open(paths['html'], encoding='utf-8') as fh:
            html = fh.read()
    return {'md': md, 'json': j, 'html': html}


def save_paths(paths, data):
    with open(paths['md'], 'w', encoding='utf-8') as fh:
        fh.write(data['md'])
    with open(paths['json'], 'w', encoding='utf-8') as fh:
        json.dump(data['json'], fh, indent=2)
    if paths['html'] and data['html'] is not None:
        with open(paths['html'], 'w', encoding='utf-8') as fh:
            fh.write(data['html'])
        # bump mtime past case.md's so T1-15/T1-18 staleness checks don't fire
        # spuriously and mask the thing this mutation is actually testing
        now = os.path.getmtime(paths['md']) + 5
        os.utime(paths['html'], (now, now))


def run_gate(tmp, case):
    p = subprocess.run([sys.executable, T1, '--case', case, '--project', tmp],
                       capture_output=True, text=True)
    return p.stdout + p.stderr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--project', default=os.getcwd())
    ap.add_argument('--case', default='cold-chain')
    a = ap.parse_args()

    fails = []
    print(f"selftest_tier1 — fixture {a.case}\n")

    # 0. baseline must PARSE and produce a report at all
    tmp, paths = build(a.project, a.case)
    base = run_gate(tmp, a.case)
    if 'VERDICT:' not in base:
        fails.append("baseline run produced no verdict — the gate is broken, not the fixes")
        print("  baseline            FAIL (no verdict)")
    else:
        nchecks = re.search(r'checks run:\s*(\d+)', base)
        print(f"  baseline            ok ({nchecks.group(1) if nchecks else '?'} checks ran)")
    shutil.rmtree(tmp)

    for name, case, setup, expect_match, needles, why in MUTATIONS:
        tmp, paths = build(a.project, case)
        original = load_paths(paths)
        mutated = setup(original)
        assert mutated != original, f"mutation {name!r} did not change the fixture"
        save_paths(paths, mutated)
        rep = run_gate(tmp, case)
        found = [n for n in needles if re.search(n, rep, re.S)]
        ok = (len(found) == len(needles)) if expect_match else (len(found) == 0)
        if not ok:
            verb = "did NOT report" if expect_match else "WRONGLY reported"
            detail = [n for n in needles if n not in found] if expect_match else found
            fails.append(f"{name}: gate {verb} {detail}")
            print(f"  FAIL  {name}\n        gate {verb} {detail}\n        (defect: {why})")
        else:
            print(f"  pass  {name}")
        shutil.rmtree(tmp)

    print()
    if fails:
        print(f"SELFTEST FAILED — {len(fails)} regression(s)")
        for f in fails:
            print("  *", f)
        sys.exit(1)
    print(f"SELFTEST PASSED — {len(MUTATIONS)} defect fixes hold")
    sys.exit(0)


if __name__ == '__main__':
    main()
