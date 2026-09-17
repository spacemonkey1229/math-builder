#!/usr/bin/env python3
"""
REGRESSION TEST for render_context.py.

Copies a real case into a tempdir and exercises the renderer against it, asserting each
guarantee holds. The specific case this guards against (2026-09-16): re.sub's STRING
replacement argument processes backslash escapes (\\1, \\\\, ...) and silently corrupted the
auto-linker's own embedded regex-escaping code the first time this script ran against a case
with no existing STORY_GLOSSARY -- `node --check` on the output failed with a mangled regex
literal. The fix was to use a function replacement (`lambda m: ...`) everywhere, whose return
value is never escape-processed. This test would have caught that before it shipped.

    python3 skills/case-publish/scripts/selftest_render_context.py --project "$PROJECT"

Exit 0 = all assertions hold. Exit 1 = a regression. Run after any edit to render_context.py.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
RC = os.path.join(HERE, 'render_context.py')


def sh(*args, cwd=None):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


def node_check(js_text, tmp):
    path = os.path.join(tmp, '_check.js')
    open(path, 'w', encoding='utf-8').write(js_text)
    rc, out, err = sh('node', '--check', path)
    return rc == 0, err


def extract_script(html):
    html_nc = re.sub(r'<!--.*?-->', '', html, flags=re.S)
    m = re.search(r'<script>(.*?)</script>', html_nc, re.S)
    return m.group(1) if m else ''


def setup_case(tmp, cid, real_project, html_name, glossary, domain_label=None, strip_existing=False):
    """Copy a real case's shape into tmp, optionally stripping any existing STORY_GLOSSARY
    so the fresh-scaffold path gets exercised, and set case.json.context_glossary[]."""
    cdir = os.path.join(tmp, 'cases', cid)
    os.makedirs(os.path.join(cdir, 'published'), exist_ok=True)
    src_html = os.path.join(real_project, 'cases', cid, 'published', html_name)
    html = open(src_html, encoding='utf-8').read()
    if strip_existing:
        html = re.sub(r'const STORY_GLOSSARY\s*=\s*\{.*?\n\};\n?', '', html, flags=re.S)
        html = re.sub(r'\n?function stermHTML.*?^autoLinkStoryTerms\(\[[^\]]*\]\);\n?', '\n',
                       html, flags=re.S | re.M)
        html = re.sub(r'\.sterm\{.*?\.glossary-grid\{[^}]*\}\n?', '', html, flags=re.S)
        html = re.sub(r'<div class="card" id="storyGlossaryCard">.*?</div>\n?', '', html, flags=re.S)
    dst_html = os.path.join(cdir, 'published', html_name)
    open(dst_html, 'w', encoding='utf-8').write(html)
    d = json.load(open(os.path.join(real_project, 'cases', cid, 'case.json')))
    d['context_glossary'] = glossary
    if domain_label:
        d['context_domain_label'] = domain_label
    json.dump(d, open(os.path.join(cdir, 'case.json'), 'w'), indent=2, ensure_ascii=False)
    return dst_html


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--project', required=True)
    args = ap.parse_args()
    project = args.project
    fails = []

    test_glossary = [
        {"term": "Gross Pay", "desc": "Total earnings before any taxes or deductions are taken out.",
         "link": "https://en.wikipedia.org/wiki/Gross_income"},
        {"term": "Withholding", "desc": "Money an employer holds back from a paycheck for tax authorities.",
         "link": "https://en.wikipedia.org/wiki/Tax_withholding"},
    ]

    with tempfile.TemporaryDirectory() as tmp:
        # --- Test 1: fresh scaffold onto a case with NO existing STORY_GLOSSARY must produce
        #     valid, parseable JS. This is the exact regression this file guards against.
        html_path = setup_case(tmp, 'payroll', project, 'Payroll - Interactive.html',
                                test_glossary, domain_label='Payroll', strip_existing=True)
        rc, out, err = sh('python3', RC, '--case', 'payroll', '--project', tmp)
        if rc != 0:
            fails.append(f"[fresh-scaffold] render_context.py exited {rc}: {err}")
        else:
            html = open(html_path, encoding='utf-8').read()
            ok, node_err = node_check(extract_script(html), tmp)
            if not ok:
                fails.append(f"[fresh-scaffold] generated <script> failed node --check: {node_err}")
            # The exact bug: check the auto-linker's own escaping regex survived intact.
            if r"/[.*+?^${}()|[\]\\]/g" not in html:
                fails.append("[fresh-scaffold] autoLinkStoryTerms's own esc() regex literal is "
                             "missing or corrupted -- the re.sub-backslash-escaping regression")
            if 'Gross Pay' not in html or 'storyGlossaryCard' not in html:
                fails.append("[fresh-scaffold] glossary content or card scaffold missing")

        # --- Test 2: idempotency. Running --check right after a real render must report no
        #     further change (case.json is authoritative; re-running must be a no-op).
        rc, out, err = sh('python3', RC, '--case', 'payroll', '--project', tmp, '--check')
        if rc != 0 or 'up to date' not in out:
            fails.append(f"[idempotency] --check after a fresh render reported a pending change: "
                         f"rc={rc} out={out!r}")

        # --- Test 3: editing case.json and re-rendering must reach the HTML with no hand-editing.
        d = json.load(open(os.path.join(tmp, 'cases', 'payroll', 'case.json')))
        d['context_glossary'].append({"term": "Net Pay",
                                       "desc": "Take-home pay after all deductions.",
                                       "link": "https://en.wikipedia.org/wiki/Net_income"})
        json.dump(d, open(os.path.join(tmp, 'cases', 'payroll', 'case.json'), 'w'), indent=2)
        sh('python3', RC, '--case', 'payroll', '--project', tmp)
        html = open(html_path, encoding='utf-8').read()
        if 'Net Pay' not in html:
            fails.append("[case.json-drives-html] adding a term to case.json.context_glossary[] "
                         "and re-rendering did not reach the published HTML")

        # --- Test 4: an already-marked, already-up-to-date case (upgrade path: hand-authored
        #     STORY_GLOSSARY, first run wraps it in markers) must also produce valid JS and be
        #     idempotent on a second run.
        html_path2 = setup_case(tmp, 'six-degrees-of-exposure', project,
                                 'Six Degrees Of Exposure - Interactive.html',
                                 [{"term": "Contact Tracing", "desc": "Finding who a sick person was near.",
                                   "link": "https://en.wikipedia.org/wiki/Contact_tracing"}],
                                 strip_existing=False)
        rc, out, err = sh('python3', RC, '--case', 'six-degrees-of-exposure', '--project', tmp)
        html = open(html_path2, encoding='utf-8').read()
        ok, node_err = node_check(extract_script(html), tmp)
        if not ok:
            fails.append(f"[upgrade-existing] generated <script> failed node --check: {node_err}")
        rc, out, err = sh('python3', RC, '--case', 'six-degrees-of-exposure', '--project', tmp, '--check')
        if rc != 0 or 'up to date' not in out:
            fails.append(f"[upgrade-existing] not idempotent after upgrading a hand-authored case: "
                         f"rc={rc} out={out!r}")

    if fails:
        print(f"FAIL — {len(fails)} regression(s):")
        for f in fails:
            print(" -", f)
        sys.exit(1)
    print("PASS — all render_context.py regression checks hold.")


if __name__ == '__main__':
    main()
