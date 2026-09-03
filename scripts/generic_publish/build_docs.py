#!/usr/bin/env python3
import json, subprocess, os

ROOT = "/Users/manan/Documents/Claude/Projects/Math Builder"
CASES = [
    "the-qubit-budget", "the-attribution-sample", "the-fee-ladder", "the-cold-start",
    "the-rig-split", "the-bot-farm", "the-course-correction", "the-plaza-bid",
]

for c in CASES:
    d = json.load(open(f"{ROOT}/cases/{c}/case.json"))
    title = d["title"]
    pub = f"{ROOT}/cases/{c}/published"
    os.makedirs(pub, exist_ok=True)
    student_out = f"{pub}/{title} - Case Study.docx"
    fac_out = f"{pub}/{title} - Facilitator Guide.docx"
    print(f"== {c} -> {title} ==")
    subprocess.run(["node", f"{ROOT}/scripts/generic_publish/md_to_docx.js",
                     f"{ROOT}/cases/{c}/case.md", student_out, "--strip-facilitator"], check=True)
    subprocess.run(["node", f"{ROOT}/scripts/generic_publish/md_to_docx.js",
                     f"{ROOT}/cases/{c}/FACILITATOR.md", fac_out], check=True)
