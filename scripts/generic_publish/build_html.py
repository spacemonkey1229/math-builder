#!/usr/bin/env python3
"""Assemble cases/<id>/published/<Title> - Interactive.html from
templates/interactive_shell.html + case.md/case.json content + a per-case
CONFIG dict (imported from cases/<id>/html_config.py) supplying the genuinely
bespoke bits: option labels, notebook steps, check-function JS, JS PARAMS/
evaluate port, twist narrative, glossary object.
"""
import importlib.util
import json
import re
import sys

ROOT = "/Users/manan/Documents/Claude/Projects/Math Builder"
SHELL = f"{ROOT}/templates/interactive_shell.html"


def load_config(case_id):
    path = f"{ROOT}/cases/{case_id}/html_config.py"
    spec = importlib.util.spec_from_file_location("cfg", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.CONFIG


def md_inline_to_html(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    text = text.replace('\\|', '|')
    return text


def section_text(md, name):
    m = re.search(rf'(?m)^## {name}\s*\n(.*?)(?=\n---\n)', md, re.S)
    return m.group(1).strip() if m else ""


def paragraphs_html(block):
    paras = [p.strip() for p in block.split('\n\n') if p.strip()]
    out = []
    for p in paras:
        if p.startswith('*') and p.endswith('*') and not p.startswith('**'):
            out.append(f'<p><em>{md_inline_to_html(p[1:-1])}</em></p>')
        else:
            out.append(f'<p>{md_inline_to_html(p)}</p>')
    return '\n'.join(out)


def parse_appendices(md):
    parts = re.split(r'(?m)^## (Appendix [A-Z]\s*[:—-].*)$', md)
    appendices = []
    for i in range(1, len(parts), 2):
        header = parts[i].strip()
        body = re.split(r'\n---\n', parts[i + 1])[0]
        m = re.match(r'Appendix ([A-Z])\s*[:—-]\s*(.*)', header)
        letter, title = m.group(1), m.group(2).strip()
        appendices.append({"letter": letter, "title": title, "body": body})
    return appendices


def table_html(header, rows):
    th = ''.join(f'<th>{md_inline_to_html(h)}</th>' for h in header)
    trs = []
    for r in rows:
        tds = ''.join(f'<td>{md_inline_to_html(c)}</td>' for c in r)
        trs.append(f'<tr>{tds}</tr>')
    return f'<table><thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table>'


def appendix_body_html(body):
    lines = body.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('|'):
            header = [c.strip() for c in line.strip('|').split('|')]
            if i + 1 < len(lines) and re.match(r'^\s*\|?[\s:|-]+\|?\s*$', lines[i + 1]) and '-' in lines[i + 1]:
                j = i + 2
                rows = []
                while j < len(lines) and lines[j].strip().startswith('|'):
                    rows.append([c.strip() for c in lines[j].strip('|').split('|')])
                    j += 1
                out.append(table_html(header, rows))
                i = j
                continue
        if line:
            if line.startswith('*') and line.endswith('*'):
                out.append(f'<p><em>{md_inline_to_html(line[1:-1])}</em></p>')
            else:
                out.append(f'<p>{md_inline_to_html(line)}</p>')
        i += 1
    return '\n'.join(out)


def appendices_html(md, skip_letters):
    apps = parse_appendices(md)
    out = []
    for ap in apps:
        if ap["letter"] in skip_letters:
            continue
        body_html = appendix_body_html(ap["body"])
        out.append(
            f'<details><summary>Appendix {ap["letter"]} &mdash; {md_inline_to_html(ap["title"])}</summary>'
            f'<div class="inner">{body_html}</div></details>'
        )
    return '\n'.join(out)


def sources_list_html(case_json):
    lis = []
    for s in case_json.get("sources", []):
        org = s.get("org", "")
        title = s.get("title", s.get("claim", ""))
        url = s.get("url", "")
        lis.append(f'<li>[{s.get("id","")}] {org} &mdash; <a href="{url}" target="_blank" rel="noopener">{title}</a> ({s.get("accessed", s.get("as_of",""))})</li>')
    return '\n'.join(lis)


def build(case_id):
    case_dir = f"{ROOT}/cases/{case_id}"
    case_json = json.load(open(f"{case_dir}/case.json"))
    md = open(f"{case_dir}/case.md", encoding="utf-8").read()
    cfg = load_config(case_id)

    shell = open(SHELL, encoding="utf-8").read()

    overview = paragraphs_html(section_text(md, "Overview"))
    background = paragraphs_html(section_text(md, "Background"))

    apps = parse_appendices(md)
    final_letter = apps[-1]["letter"] if apps else "?"
    sources_letter = apps[-2]["letter"] if len(apps) >= 2 else "?"
    appx_html = appendices_html(md, skip_letters={sources_letter, final_letter})

    title = case_json["title"]
    band = case_json.get("band", [])
    band_str = "/".join(band) if isinstance(band, list) else str(band)

    repl = {
        "{{CASE_TITLE}}": title,
        "{{CASE_YEAR}}": "2026-27",
        "{{CASE_TIER}}": case_json.get("tier", "?").replace("T", ""),
        "{{CASE_BAND}}": band_str,
        "{{CASE_STRAND_SUMMARY}}": cfg["strand_summary"],
        "{{CASE_SPECIFIC_CSS}}": cfg.get("extra_css", ""),
        "{{CASE_SPECIFIC_ICON_SYMBOLS}}": "",
        "{{CASE_OVERVIEW_BANNER_SVG}}": cfg.get("overview_banner_svg", ""),
        "{{CASE_OVERVIEW_TEXT}}": overview,
        "{{CASE_BACKGROUND_TEXT}}": background,
        "{{CASE_PROTAGONIST}}": cfg["protagonist"],
        "{{CASE_OPTION_A_LABEL}}": cfg["option_a_label"],
        "{{CASE_OPTION_A_TEXT}}": cfg["option_a_text"],
        "{{CASE_OPTION_B_LABEL}}": cfg["option_b_label"],
        "{{CASE_OPTION_B_TEXT}}": cfg["option_b_text"],
        "{{CASE_GLOSSARY_APPENDIX_LETTER}}": f"Appendix {final_letter}",
        "{{CASE_CHALLENGE_3_DELIVERABLES_SUMMARY}}": cfg["challenge3_summary"],
        "{{CASE_APPENDICES_A_THROUGH_F}}": appx_html,
        "{{CASE_GLOSSARY_VERIFIED_DATE}}": "2026-09-01",
        "{{CASE_NOTEBOOK_STEPS}}": cfg["notebook_steps_html"],
        "{{CASE_TWIST_NARRATIVE}}": cfg["twist_narrative_html"],
        "{{CASE_TWIST_APPLY_LABEL}}": cfg["twist_apply_label"],
        "{{CASE_SOURCES_LIST}}": sources_list_html(case_json),
        "{{CASE_JS_DATA_BLOCK}}": cfg["js_data_block"],
        "{{CASE_NOTEBOOK_CHECK_FUNCTIONS}}": cfg["notebook_check_functions"],
        "{{CASE_ID}}": case_id.replace("the-", ""),
        "{{CASE_DELIVERABLES_ARRAY}}": json.dumps(cfg["deliverables"]),
        "{{CASE_GLOSSARY_OBJECT}}": cfg["glossary_js"],
        "{{CASE_HOWTO_ARRAY}}": cfg["howto_js"],
        "{{CASE_ON_TWIST_TOGGLE_FUNCTION}}": cfg["on_twist_toggle_js"],
    }

    out = shell
    for k, v in repl.items():
        out = out.replace(k, v)

    remaining = re.findall(r'\{\{[A-Z_0-9]+\}\}', out)
    if remaining:
        print("WARNING: unfilled placeholders:", set(remaining))

    out_path = f"{case_dir}/published/{title} - Interactive.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", out_path, len(out), "bytes")


if __name__ == "__main__":
    for cid in sys.argv[1:]:
        build(cid)
