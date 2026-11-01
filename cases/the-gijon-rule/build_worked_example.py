#!/usr/bin/env python3
"""Case-local helper for The Gijon Rule packet builds.

case.md Appendix C carries a hand-drawn inline <svg> (the 2-0 worked example: two filled 7x7
grids and a Venn diagram). Rendered as-is it has layout defects (found in the publish pass,
2026-10-04): the one-line caption at the top is wider than the 700-unit viewBox and is clipped
on both sides; the right-hand legend lines are centred at x=515 and run underneath the Option B
grid; the "circle: safe under A" label touches the Option B grid; and the Venn diagram's
"only under B" region carries no count even though the legend says "0".

This module re-lays those text elements out WITHOUT changing any figure, cell, colour, circle or
the case.md source (case.md is hash-pinned by QA and is not edited). Output:
    _worked_example_fixed.svg   (used by build_html.py, inlined into the Interactive HTML)
    _worked_example.png         (used by build_docx.js, embedded in the student Case Study)
The PNG is rendered with soffice (headless) from a 2x scaled copy of the fixed SVG.
"""
import os
import re
import subprocess
import shutil
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def original_svg():
    md = open(os.path.join(HERE, 'case.md'), encoding='utf-8').read()
    return re.search(r'(?s)<svg.*?</svg>', md).group(0)


def fixed_svg():
    s = original_svg()
    if '<text x="350" y="14"' not in s:
        # case.md Appendix C already carries the fixed layout (synced 2026-10-04); nothing to re-lay out.
        return s

    # 1. The caption: split the one overlong line into two centred lines.
    old_caption = re.search(r'<text x="350" y="14"[^>]*>(.*?)</text>', s)
    assert old_caption, 'caption not found'
    full = old_caption.group(1)
    cut = full.index(' S = safe')
    l1, l2 = full[:cut].strip(), full[cut:].strip()
    new_caption = (
        '<text x="350" y="9" font-size="10.5" text-anchor="middle" fill="#7a4a00">%s</text>\n'
        '<text x="350" y="20" font-size="10.5" text-anchor="middle" fill="#7a4a00">%s</text>' % (l1, l2))
    s = s.replace(old_caption.group(0), new_caption, 1)

    # 2. Venn labels: move off the Option B grid.
    s = s.replace('<text x="520" y="82" font-size="10" text-anchor="middle" fill="#1a3a5c">circle: safe under A</text>',
                  '<text x="545" y="84" font-size="10" text-anchor="middle" fill="#1a3a5c">circle: safe under A</text>', 1)
    s = s.replace('<text x="640" y="98" font-size="10" text-anchor="middle" fill="#7a4a00">circle: safe under B</text>',
                  '<text x="628" y="100" font-size="10" text-anchor="middle" fill="#7a4a00">circle: safe under B</text>', 1)

    # 3. Region counts: A-only (5), overlap (29), and the missing B-only (0), one per region.
    s = s.replace('<text x="515" y="155" font-size="16" text-anchor="middle" fill="#222">5</text>',
                  '<text x="527" y="156" font-size="16" text-anchor="middle" fill="#222">5</text>', 1)
    s = s.replace('<text x="600" y="155" font-size="16" text-anchor="middle" fill="#222">29</text>',
                  '<text x="589" y="156" font-size="14" text-anchor="middle" fill="#222">29</text>\n'
                  '<text x="631" y="156" font-size="16" text-anchor="middle" fill="#222">0</text>', 1)

    # 4. Legend: left-aligned below the Venn, clear of the Option B grid (which ends at x=480).
    for old_y, txt in ((240, '5 = only under A (left part)'), (254, '29 = under both (overlap)'),
                       (268, '0 = only under B (right part)')):
        pat = r'<text x="515" y="%d" font-size="10" text-anchor="middle" fill="#222">[^<]*</text>' % old_y
        assert re.search(pat, s), 'legend line %d not found' % old_y
        s = re.sub(pat, '<text x="492" y="%d" font-size="10" text-anchor="start" fill="#222">%s</text>' % (old_y + 4, txt), s, count=1)
    return s


def main():
    svg = fixed_svg()
    out_svg = os.path.join(HERE, '_worked_example_fixed.svg')
    open(out_svg, 'w', encoding='utf-8').write(svg)
    # PNG via soffice at 2x
    tmp = tempfile.mkdtemp()
    big = svg.replace('<svg viewBox="0 0 700 300"', '<svg width="1400" height="600" viewBox="0 0 700 300"', 1)
    big = big.replace('max-width:720px;width:100%;', '')
    p = os.path.join(tmp, '_worked_example.svg')
    open(p, 'w', encoding='utf-8').write(big)
    subprocess.run(['soffice', '--headless', '--convert-to', 'png', '--outdir', tmp, p],
                   check=True, capture_output=True)
    shutil.copy(os.path.join(tmp, '_worked_example.png'), os.path.join(HERE, '_worked_example.png'))
    print('wrote', out_svg, 'and _worked_example.png')


if __name__ == '__main__':
    main()
