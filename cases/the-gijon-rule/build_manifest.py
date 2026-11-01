#!/usr/bin/env python3
"""Write published/MANIFEST.json for The Gijon Rule (SKILL 1e). Run last, after the docx/xlsx/html builds."""
import hashlib, json, os, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
pub = os.path.join(HERE, "published")
c = json.load(open(os.path.join(HERE, "case.json"), encoding="utf-8"))
h = hashlib.sha256(open(os.path.join(HERE, "case.md"), "rb").read()).hexdigest()
assert h == c["qa"]["case_md_sha256"], "case.md hash is stale vs qa"
files = [("The Gijon Rule - Case Study.docx", "student"), ("The Gijon Rule - Data.xlsx", "student"),
         ("The Gijon Rule - Facilitator Guide.docx", "facilitator"), ("The Gijon Rule - Interactive.html", "student")]
m = {
    "case_id": "the-gijon-rule",
    "built_on": datetime.date.today().isoformat(),
    "case_md_sha256": h,
    "qa_report": "cases/the-gijon-rule/QA_REPORT.md",
    "qa_verdict": "PASS",
    "waived_gaps": [],
    "publish_notes": [
        "Appendix C's worked-example SVG is re-laid-out at build time (caption split into two lines, legend moved clear of the Option B grid, 'only under B' count 0 added to the Venn diagram); no figure, cell or colour changed and case.md is untouched. The docx embeds it as a PNG rendered from the fixed SVG; the HTML inlines the fixed SVG.",
        "The Appendix B photograph is shown in the Interactive HTML (served via the Commons file-path URL on the cited commons.wikimedia.org domain) and is NOT embedded in the printable Case Study docx (no image file was downloaded at build time); the docx carries the caption and a link to the Commons file page.",
        "The Data workbook holds raw cited data and blank work areas only; no standings, points, goal differences, counts, percents or rankings are stored.",
    ],
    "files": [{"name": n, "bytes": os.path.getsize(os.path.join(pub, n)), "audience": a} for n, a in files],
    "drive": {"pushed": False, "folder_id": None, "urls": []},
}
json.dump(m, open(os.path.join(pub, "MANIFEST.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(json.dumps(m["files"], indent=1))
