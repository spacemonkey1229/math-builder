#!/usr/bin/env python3
"""Fill templates/interactive_shell.html for The Hundredth (case-local, same precedent as
cases/the-trophy-and-the-table/build_html.py). Prose/appendices are converted from case.md so the two
cannot drift; the notebook JS is a port of sensitivity_model.py. The STORY_GLOSSARY layer is then
added by skills/case-publish/scripts/render_context.py (run after this script)."""
import re, html as H, subprocess, sys

PROJECT = "/Users/manan/Documents/Claude/Projects/Math Builder"
CASE = f"{PROJECT}/cases/the-hundredth"
SHELL = f"{PROJECT}/templates/interactive_shell.html"
OUT = f"{CASE}/published/The Hundredth - Interactive.html"
md = open(f"{CASE}/case.md", encoding="utf-8").read()
md = re.sub(r'<!--\s*FACILITATOR ONLY.*?-->', '', md, flags=re.S)


def sect(title_re):
    return re.search(r'(?ms)^## ' + title_re + r'.*?\n(.*?)(?=^---\s*$|\Z)', md).group(1).strip()


def inline(t):
    t = H.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    return t


def table(lines, tid):
    cells = [[c.strip() for c in l.strip().strip('|').split('|')] for l in lines if not re.match(r'^\|[\s:|-]+\|$', l.strip())]
    h = '<table id="%s"><tr>%s</tr>\n' % (tid, ''.join('<th>%s</th>' % inline(c) for c in cells[0]))
    for r in cells[1:]:
        h += '<tr>%s</tr>\n' % ''.join('<td>%s</td>' % inline(c) for c in r)
    return '<div style="overflow-x:auto">' + h + '</table></div>'


def blocks(text, prefix):
    """Convert a markdown fragment (paragraphs, bullets, tables, blockquote, inline svg) to HTML."""
    lines = text.split('\n'); out = []; i = 0; nt = 0
    def start(l): return (not l.strip()) or l.startswith('|') or l.startswith('- ') or l.startswith('>') or l.startswith('<svg')
    while i < len(lines):
        l = lines[i]
        if not l.strip(): i += 1; continue
        if l.startswith('<svg'):
            buf = []
            while i < len(lines):
                buf.append(lines[i]); i += 1
                if '</svg>' in buf[-1]: break
            svg = '\n'.join(buf).replace('<svg ', '<svg class="diagram" ', 1)
            out.append('<figure>' + svg + '</figure>'); continue
        if l.startswith('|'):
            t = []
            while i < len(lines) and lines[i].startswith('|'): t.append(lines[i]); i += 1
            nt += 1; out.append(table(t, '%s%d' % (prefix, nt))); continue
        if l.startswith('>'):
            q = []
            while i < len(lines) and lines[i].startswith('>'): q.append(lines[i].lstrip('> ')); i += 1
            out.append('<blockquote>%s</blockquote>' % inline(' '.join(q))); continue
        if l.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                it = [lines[i][2:]]; i += 1
                while i < len(lines) and lines[i].strip() and not start(lines[i]): it.append(lines[i].strip()); i += 1
                items.append(' '.join(it))
            out.append('<ul>' + ''.join('<li>%s</li>' % inline(x) for x in items) + '</ul>'); continue
        p = [l.strip()]; i += 1
        while i < len(lines) and not start(lines[i]): p.append(lines[i].strip()); i += 1
        out.append('<p>%s</p>' % inline(' '.join(p)))
    return '\n'.join(out)


def appendix(letter):
    m = re.search(r'(?ms)^## Appendix %s — (.*?)\n(.*?)(?=^---\s*$)' % letter, md)
    return m.group(1).strip(), m.group(2).strip()


html = open(SHELL, encoding="utf-8").read()
R = {}
R["{{CASE_TITLE}}"] = "The Hundredth"
R["{{CASE_YEAR}}"] = "2026-27"
R["{{CASE_TIER}}"] = "T2"
R["{{CASE_BAND}}"] = "MS-core"
R["{{CASE_STRAND_SUMMARY}}"] = "Units &middot; Decimals &middot; Range &middot; Probability"
R["{{CASE_ID}}"] = "the-hundredth"
R["{{CASE_GLOSSARY_APPENDIX_LETTER}}"] = "Appendix H"
R["{{CASE_GLOSSARY_VERIFIED_DATE}}"] = "2026-10-04"
R["{{CASE_PROTAGONIST}}"] = "the Chief Judge"
R["{{CASE_OPTION_A_LABEL}}"] = "Pad Ranks"
R["{{CASE_OPTION_A_TEXT}}"] = "The touchpad result orders the finish, as the rule is written."
R["{{CASE_OPTION_B_LABEL}}"] = "Contact Ranks"
R["{{CASE_OPTION_B_TEXT}}"] = "First hand contact on high-speed video orders the finish."
R["{{CASE_SPECIFIC_CSS}}"] = ".num{text-align:right;font-variant-numeric:tabular-nums}\n  blockquote{margin:10px 0;padding:6px 14px;border-left:4px solid var(--line);color:#555;font-style:italic}"
R["{{CASE_SPECIFIC_ICON_SYMBOLS}}"] = ""
R["{{CASE_OVERVIEW_BANNER_SVG}}"] = ""

ov = sect('Overview').split('\n\n')
R["{{CASE_OVERVIEW_TEXT}}"] = '<p class="lede">' + inline(ov[0].replace('\n', ' ')) + '</p>\n' + blocks('\n\n'.join(ov[1:]), 'tblov')
R["{{CASE_BACKGROUND_TEXT}}"] = blocks(sect('Background'), 'tblbg')
R["{{CASE_CHALLENGE_3_DELIVERABLES_SUMMARY}}"] = (
    "Include: <strong>D1</strong> speed and distance per hundredth; <strong>D2</strong> a frame-rate band table; "
    "<strong>D3</strong> the range hiding inside &ldquo;0.01 s&rdquo;; <strong>D4</strong> a differential-lag table and your plausible range; "
    "<strong>D5</strong> a reliability comparison; <strong>D6</strong> what the model leaves out. The full wording of each is in the case document.")
R["{{CASE_DELIVERABLES_ARRAY}}"] = """[
  ["D1", "Speed and distance per hundredth"],
  ["D2", "Frame-rate band table"],
  ["D3", "The range hiding inside 0.01 s"],
  ["D4", "Differential-lag table and your plausible range"],
  ["D5", "Reliability comparison (scenario values and your own range)"],
  ["D6", "What the model leaves out"]
]"""

apx = ""
for L in "ABCDEFG":
    t, b = appendix(L)
    apx += '<details%s id="apx-%s"><summary>Appendix %s &mdash; %s</summary><div class="inner">\n%s\n</div></details>\n' % (
        ' open' if L == 'A' else '', L.lower(), L, inline(t), blocks(b, 'tbl' + L))
R["{{CASE_APPENDICES_A_THROUGH_F}}"] = apx


def step(n, title, goal, fields, fn, extra=""):
    h = '  <div class="stepbox">\n    <h4>Step %d &mdash; %s</h4>\n    <div class="goal">%s</div>\n' % (n, title, goal)
    for fid, label, ph, fbid, pre in fields:
        h += '    <div class="fieldrow"><label for="%s">%s</label><input type="number" id="%s" step="any" placeholder="%s"%s><span id="%s" class="fb"></span></div>\n' % (
            fid, label, fid, ph, (' value="%s"' % pre) if pre else '', fbid)
    return h + '    <button onclick="%s()">Check</button>\n%s  </div>\n' % (fn, extra)

nb = ""
nb += step(1, "Speed and distance per hundredth (D1)", "Using Appendix C, find the winner's average speed and how far a hand travels in one hundredth of a second at that speed.",
  [("s1v", "Average speed (m/s)", "a decimal number", "fb1a", ""), ("s1d", "Distance in 0.01 s (cm)", "a decimal number", "fb1b", "")], "checkStep1")
nb += step(2, "Frame-rate bands (D2)", "For each frame rate in Appendix D, find the time between frames (seconds) and, for the 240 and 30 frames-per-second rows, the distance a hand travels between frames (cm).",
  [("s2a", "Time between frames, 30 fps (s)", "a decimal number", "fb2a", ""), ("s2b", "Time between frames, 60 fps (s)", "a decimal number", "fb2b", ""),
   ("s2c", "Time between frames, 240 fps (s)", "a decimal number", "fb2c", ""), ("s2d", "Time between frames, 1000 fps (s)", "a decimal number", "fb2d", ""),
   ("s2e", "Hand travel per frame, 30 fps (cm)", "a decimal number", "fb2e", ""), ("s2f", "Hand travel per frame, 240 fps (cm)", "a decimal number", "fb2f", "")], "checkStep2")
nb += step(3, "The range hiding inside 0.01 s (D3)", "Using reported times of 50.58 and 50.59, find the smallest and largest true pad-time difference if the third digit is dropped, and the upper end if the time is rounded.",
  [("s3a", "Dropped digit: smallest difference (s)", "a decimal number", "fb3a", ""), ("s3b", "Dropped digit: largest difference (s)", "a decimal number", "fb3b", ""),
   ("s3c", "Rounded: upper end of the difference (s)", "a decimal number", "fb3c", "")], "checkStep3")
nb += step(4, "The differential-lag table (D4)", "Using Appendix E's sign convention and a reported pad margin of 0.01 s, find the first-contact margin c for two rows of the table, and the lag above which the pad and first contact disagree.",
  [("s4a", "c when the lag is 0.015 s", "a decimal number, negative if below zero", "fb4a", ""), ("s4b", "c when the lag is 0.005 s", "a decimal number, negative if below zero", "fb4b", ""),
   ("s4c", "Lag above which they disagree (s)", "a decimal number", "fb4c", "")], "checkStep4")
nb += step(5, "The reliability comparison (D5)", "Use Appendix E's rule with your own lag (it starts at the scenario value; change it to try your D4 range). Find each option's band and its probability of ordering a close finish correctly, then the percent difference. If the twist is applied below, the footage changes.",
  [("s5d", "Differential lag to use (s)", "a decimal number", "fb5z", "0.010"),
   ("s5a", "Option A band (s)", "a decimal number", "fb5a", ""), ("s5b", "Option B band (s)", "a decimal number", "fb5b", ""),
   ("s5c", "Probability, Option A", "a decimal (a probability)", "fb5c", ""), ("s5e", "Probability, Option B", "a decimal (a probability)", "fb5e", ""),
   ("s5f", "Percent difference (larger minus smaller, divided by smaller, times 100)", "a decimal number", "fb5f", "")], "checkStep5",
  '    <p class="side-note">These checks only confirm your arithmetic. Which ruling to choose, and what lag you believe, is still yours.</p>\n')
R["{{CASE_NOTEBOOK_STEPS}}"] = nb

R["{{CASE_TWIST_NARRATIVE}}"] = """
      <p>A technician has just walked in. The fast camera's view of the wall was blocked by spray in this lane. The only angle that clearly shows both hands at the wall is the ordinary slow-motion feed: <strong>60 frames per second</strong>. The judge's reading band J is unchanged, and nobody may read between two frames. This is a constructed what-if for discussion; it is not a record of what footage existed in 2008.</p>
"""
R["{{CASE_TWIST_APPLY_LABEL}}"] = "Apply the twist to Step 5's check (Contact Ranks uses the 60 fps feed)"

R["{{CASE_SOURCES_LIST}}"] = """
      <li>[S1] Olympedia &mdash; <a href="https://www.olympedia.org/results/261586" target="_blank" rel="noopener">Men's 100 metres Butterfly, 2008</a></li>
      <li>[S2] Wikipedia &mdash; <a href="https://en.wikipedia.org/wiki/Swimming_at_the_2008_Summer_Olympics_%E2%80%93_Men%27s_100_metre_butterfly" target="_blank" rel="noopener">Swimming at the 2008 Summer Olympics, Men's 100 metre butterfly</a></li>
      <li>[S3] ABC News &mdash; <a href="https://www.abc.net.au/news/2008-08-16/fina-throws-out-protest-against-phelps/478670" target="_blank" rel="noopener">FINA throws out protest against Phelps</a></li>
      <li>[S4] NBC News &mdash; <a href="https://www.nbcnews.com/id/wbna26232965" target="_blank" rel="noopener">Video, timing systems confirm Phelps' 7th gold</a></li>
      <li>[S5] Swimming World &mdash; <a href="https://www.swimmingworldmagazine.com/news/mark-spitz-allegedly-claims-michael-phelps-did-not-win-2008-100-fly-olympic-gold/" target="_blank" rel="noopener">Mark Spitz allegedly claims Michael Phelps did not win 2008 100 fly Olympic gold</a></li>
      <li>[S6] FINA &mdash; <a href="https://e3c1a240-348c-4e25-ba0f-d605cc91676d.usrfiles.com/ugd/e3c1a2_0b195d2a7fe747249f570c80124bbf08.pdf" target="_blank" rel="noopener">FINA Swimming Rules 2009-2013</a></li>
      <li>[S7] FINA &mdash; <a href="https://www.plavalna-zveza.si/wp-content/uploads/2021/07/FINA_SW_RULES_20150907.pdf" target="_blank" rel="noopener">Swimming Rules 2015-2017</a></li>
      <li>[S8] Derived: 100 m divided by 50.58 s</li>
"""

R["{{CASE_JS_DATA_BLOCK}}"] = """
// Ported from cases/the-hundredth/sensitivity_model.py. Raw given data and assumptions only; no verdicts.
const DISTANCE_M = 100, TIME_A = 50.58, TIME_B = 50.59, PAD_GAP = 0.01;
const PARAMS = { delta_lag: 0.010, judge_band: 0.005, fps: 240, window: 0.05, twist_fps: 60 };
const FLEX = ["delta_lag", "judge_band", "fps"];
function _p(band, window){ return Math.max(0, 1 - band/(2*window)); }
function _metrics(delta, j, fps, w){ return {A: _p(Math.abs(delta), w), B: _p(1/fps + j, w)}; }
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  return _metrics(p.delta_lag, p.judge_band, p.fps, p.window);
}
function evaluate_twist(params){
  const p = Object.assign({}, PARAMS, params||{});
  return _metrics(p.delta_lag, p.judge_band, p.twist_fps, p.window);
}
"""

R["{{CASE_NOTEBOOK_CHECK_FUNCTIONS}}"] = """
function checkStep1(){
  const v = DISTANCE_M / TIME_A;
  fb('fb1a', near(parseFloat(val('s1v')), v, 0.005));
  fb('fb1b', near(parseFloat(val('s1d')), v*PAD_GAP*100, 0.02));
}
function checkStep2(){
  const v = DISTANCE_M / TIME_A;
  fb('fb2a', near(parseFloat(val('s2a')), 1/30, 0.0002));
  fb('fb2b', near(parseFloat(val('s2b')), 1/60, 0.0002));
  fb('fb2c', near(parseFloat(val('s2c')), 1/240, 0.0002));
  fb('fb2d', near(parseFloat(val('s2d')), 1/1000, 0.0002));
  fb('fb2e', near(parseFloat(val('s2e')), v*100/30, 0.05));
  fb('fb2f', near(parseFloat(val('s2f')), v*100/240, 0.02));
}
function checkStep3(){
  // dropping the third digit: A in [50.580, 50.589], B in [50.590, 50.599]
  fb('fb3a', near(parseFloat(val('s3a')), 50.590 - 50.589, 0.0002));
  fb('fb3b', near(parseFloat(val('s3b')), 50.599 - 50.580, 0.0002));
  // rounding to the nearest hundredth: each time within +/- 0.005 s, so the gap is under 0.01 + 2*0.005
  fb('fb3c', near(parseFloat(val('s3c')), PAD_GAP + 2*0.005, 0.0002));
}
function checkStep4(){
  fb('fb4a', near(parseFloat(val('s4a')), 0.015 - PAD_GAP, 0.0003));
  fb('fb4b', near(parseFloat(val('s4b')), 0.005 - PAD_GAP, 0.0003));
  fb('fb4c', near(parseFloat(val('s4c')), PAD_GAP, 0.0003));
}
function checkStep5(){
  const d = parseFloat(val('s5d'));
  const twist = !!window.__TWIST_APPLIED__;
  const fps = twist ? PARAMS.twist_fps : PARAMS.fps;
  const m = (twist ? evaluate_twist : evaluate)({delta_lag: d});
  const bandA = Math.abs(d), bandB = 1/fps + PARAMS.judge_band;
  fb('fb5a', near(parseFloat(val('s5a')), bandA, 0.0002));
  fb('fb5b', near(parseFloat(val('s5b')), bandB, 0.0002));
  fb('fb5c', near(parseFloat(val('s5c')), m.A, 0.002));
  fb('fb5e', near(parseFloat(val('s5e')), m.B, 0.002));
  const hi = Math.max(m.A, m.B), lo = Math.min(m.A, m.B);
  fb('fb5f', near(parseFloat(val('s5f')), 100*(hi-lo)/lo, 0.25));
  document.getElementById('fb5z').className = 'fb';
}
"""
R["{{CASE_ON_TWIST_TOGGLE_FUNCTION}}"] = """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
"""

R["{{CASE_GLOSSARY_OBJECT}}"] = """{
  "Unit": {def: "A defined quantity -- a centimeter, an hour, a second -- used as a standard for measuring.",
    url: "https://www.khanacademy.org/math/cc-fifth-grade-math/imp-measurement-and-data-3"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Decimal": {def: "A number written with place value to the right of a decimal point, e.g. 0.34.",
    url: "https://www.khanacademy.org/math/arithmetic/arith-decimals"},
  "Percent": {def: "A ratio that compares a number to 100, literally per hundred.",
    url: "https://www.mathsisfun.com/percentage.html"},
  "Rounding": {def: "Replacing a number with a simpler, nearby value at a chosen place value.",
    url: "https://www.khanacademy.org/math/cc-fifth-grade-math/imp-place-value-and-decimals/imp-rounding-decimals/v/rounding-decimals"},
  "Estimating": {def: "Finding an approximate answer that is close enough to be useful, rather than an exact one.",
    url: "https://www.mathsisfun.com/numbers/estimation.html"},
  "Range": {def: "The difference between the largest and smallest values in a set; also used loosely for the span from a lowest to a highest possible value.",
    url: "https://www.mathsisfun.com/data/range.html"},
  "Probability": {def: "How likely an event is to happen, from 0 (impossible) to 1 (certain).",
    url: "https://www.mathsisfun.com/data/probability.html"},
  "Absolute Value": {def: "How far a number is from zero on the number line -- always zero or positive.",
    url: "https://www.khanacademy.org/math/algebra-home/alg-absolute-value"},
  "Variable": {def: "A letter or symbol that stands for a number you can change or do not yet know, such as the lag in this case.",
    url: "https://www.mathsisfun.com/definitions/variable.html"}
}"""
R["{{CASE_HOWTO_ARRAY}}"] = """[
  ["how to convert an amount with compound units", "Unit"],
  ["how to divide decimal numbers", "Decimal"],
  ["how to multiply decimal numbers", "Decimal"],
  ["how to subtract decimal numbers", "Decimal"],
  ["how to round a number to a specified place value", "Rounding"],
  ["how to evaluate a variable expression (Substitution Property)", "Variable"],
  ["how to evaluate an absolute value expression", "Absolute Value"],
  ["how to determine the probability of a single event", "Probability"],
  ["how to convert numbers to percents", "Percent"],
  ["how to compare two or more values", "Ratio"]
]"""

for k, v in R.items():
    if k not in html:
        raise SystemExit("MISSING PLACEHOLDER IN SHELL: " + k)
    html = html.replace(k, v)
left = [m for m in re.findall(r'\{\{[A-Z_0-9]+\}\}', html) if m != '{{PLACEHOLDER}}']
if left:
    raise SystemExit("Unfilled placeholders remain: %s" % left)
open(OUT, "w", encoding="utf-8").write(html)
print("wrote", OUT)
subprocess.check_call([sys.executable, f"{PROJECT}/skills/case-publish/scripts/render_context.py", "--case", "the-hundredth", "--project", PROJECT])
