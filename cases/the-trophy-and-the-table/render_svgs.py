#!/usr/bin/env python3
"""Rasterise the three inline SVGs in case.md to PNG (headless Chrome) for the docx builder."""
import re, subprocess, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
md = open(f"{HERE}/case.md", encoding="utf-8").read()
svgs = re.findall(r'(?s)<svg.*?</svg>', md)
names = ["scoring_rule", "persistence_scatter", "residual_example"]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for name, svg in zip(names, svgs):
    vb = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg)
    w, h = int(vb.group(1)), int(vb.group(2))
    src = svg
    if name == 'persistence_scatter':  # caption overflows the viewBox in case.md; the docx carries it as a real caption paragraph
        src = re.sub(r'<text x="200" y="244".*?</text>', '', src)
    s = re.sub(r'style="[^"]*"', 'style="background:#fafafa;font-family:Arial,sans-serif"', src, count=1)
    if name == 'residual_example':  # label text overflows the viewBox in case.md; widen canvas so it is not clipped
        s = s.replace('viewBox="0 0 320 210"', 'viewBox="0 0 360 210"'); w = 360
    s = s.replace('<svg ', f'<svg width="{w*3}" height="{h*3}" ', 1)
    page = f'<html><body style="margin:0;background:#fff">{s}</body></html>'
    hp = f"{HERE}/build_assets/{name}.html"
    open(hp, "w").write(page)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", f"--window-size={w*3},{h*3}",
                    "--hide-scrollbars", f"--screenshot={HERE}/build_assets/{name}.png",
                    f"file://{hp}"], check=True, capture_output=True)
    os.remove(hp)
    print(name, w, h)
