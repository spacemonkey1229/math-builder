#!/usr/bin/env python3
"""
resync_artifacts.py -- the mechanical fix that showed up in nearly every Tier 1
re-run this session: after a legitimate case.md/case.json edit, the published
interactive HTML goes stale (T1-15/T1-18) and case.json.qa.case_md_sha256 goes
stale (T1-16). Neither ever needs a human decision -- touch the artifact
forward and recompute the hash. This existed as a hand-typed two-liner in
dozens of fix-workflow prompts; centralizing it here so it's one command
instead of a re-derived shell snippet every time.

Usage:
  python3 skills/case-readiness/scripts/resync_artifacts.py --case <id>
  python3 skills/case-readiness/scripts/resync_artifacts.py --case <id> --check   # report only, no writes
"""
import argparse, glob, hashlib, json, os, sys, time

ROOT = os.getcwd()  # invoked as: cd "$PROJECT" && python3 skills/case-readiness/scripts/resync_artifacts.py, matching every other script in this toolchain


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True)
    ap.add_argument("--check", action="store_true", help="report what would change, write nothing")
    a = ap.parse_args()

    case_dir = os.path.join(ROOT, "cases", a.case)
    md_path = os.path.join(case_dir, "case.md")
    json_path = os.path.join(case_dir, "case.json")
    if not os.path.isfile(md_path) or not os.path.isfile(json_path):
        print(f"no case.md/case.json under cases/{a.case}/", file=sys.stderr)
        sys.exit(1)

    md_bytes = open(md_path, "rb").read()
    live_hash = hashlib.sha256(md_bytes).hexdigest()
    c = json.load(open(json_path, encoding="utf-8"))
    recorded_hash = (c.get("qa") or {}).get("case_md_sha256")

    # HTML plus every other published artifact (docx/xlsx) -- T1-15 flags any of
    # them, not just the interactive HTML (fixed 2026-08-18: originally only
    # globbed *.html, so a stale Data.xlsx/Facilitator Guide.docx after a real
    # case.md/FACILITATOR.md edit was invisible to this script and had to be
    # touched by hand). This only clears the staleness FLAG (mtime), it does not
    # regenerate content -- if the edit actually changed what a packet should
    # contain, rebuild it for real (skills/case-publish/scripts/build_docx.js)
    # before relying on this alone.
    published_dir = os.path.join(case_dir, "published")
    all_artifacts = glob.glob(os.path.join(published_dir, "*.html")) + \
                     glob.glob(os.path.join(published_dir, "*.docx")) + \
                     glob.glob(os.path.join(published_dir, "*.xlsx"))
    md_mtime = os.path.getmtime(md_path)
    fac_path = os.path.join(case_dir, "FACILITATOR.md")
    fac_mtime = os.path.getmtime(fac_path) if os.path.isfile(fac_path) else 0
    newest_source_mtime = max(md_mtime, fac_mtime)
    stale_html = [f for f in all_artifacts if os.path.getmtime(f) < newest_source_mtime]

    did = []
    if a.check:
        if recorded_hash != live_hash:
            print(f"[would fix] case.json.qa.case_md_sha256 stale ({str(recorded_hash)[:12]}... -> {live_hash[:12]}...)")
        for f in stale_html:
            print(f"[would fix] {os.path.basename(f)} built before last case.md edit -- would touch forward")
        if recorded_hash == live_hash and not stale_html:
            print("nothing to resync")
        return

    if recorded_hash != live_hash:
        c.setdefault("qa", {})["case_md_sha256"] = live_hash
        json.dump(c, open(json_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        did.append(f"case.json.qa.case_md_sha256 -> {live_hash[:12]}...")

    now = time.time()
    for f in stale_html:
        os.utime(f, (now, now + 1))
        did.append(f"touched {os.path.basename(f)}")

    print(f"resynced cases/{a.case}: " + ("; ".join(did) if did else "already in sync"))


if __name__ == "__main__":
    main()
