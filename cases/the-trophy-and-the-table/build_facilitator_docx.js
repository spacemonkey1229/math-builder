// Facilitator Guide .docx for "The Trophy and the Table", built from FACILITATOR.md (+ publish-time run-of-show additions).
// FACILITATOR ONLY: never ship alongside student files.
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType,
  ShadingType, AlignmentType, LevelFormat, ExternalHyperlink, ImageRun, BorderStyle,
} = require("../../node_modules/docx");

const HERE = __dirname;
const NAVY = "1a3a5c";
const CONTENT_W = 10080; // US Letter, 1080 margins
let raw = fs.readFileSync(path.join(HERE, "FACILITATOR.md"), "utf8");
raw = raw.replace(/<!--[\s\S]*?-->/g, "");
const svgNames = [], svgAlts = [];
const lines = raw.split("\n");

function inline(text, base = {}) {
  const runs = [];
  const re = /(\*\*(.+?)\*\*)|(\*([^*\s][^*]*?)\*)|(\[([^\]]+)\]\(([^)]+)\))/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) runs.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    if (m[1]) runs.push(new TextRun({ text: m[2], ...base, bold: true }));
    else if (m[3]) runs.push(new TextRun({ text: m[4], ...base, italics: true }));
    else runs.push(new ExternalHyperlink({ link: m[7], children: [new TextRun({ text: m[6], ...base, style: "Hyperlink" })] }));
    last = re.lastIndex;
  }
  if (last < text.length) runs.push(new TextRun({ text: text.slice(last), ...base }));
  if (!runs.length) runs.push(new TextRun({ text, ...base }));
  return runs;
}
const plain = (t) => t.replace(/\*\*(.+?)\*\*/g, "$1").replace(/\*(.+?)\*/g, "$1").replace(/\[([^\]]+)\]\(([^)]+)\)/g, "$1");

function tableFrom(header, rows) {
  const n = header.length;
  const small = n >= 5;
  const sz = small ? 17 : 20;
  // width weights from content length (bounded), then scaled to CONTENT_W
  const w = header.map((h, i) => {
    const lens = [plain(h).length, ...rows.map((r) => plain(r[i] || "").length)];
    const avg = lens.reduce((a, b) => a + b, 0) / lens.length;
    return Math.min(Math.max(avg, 4), 60);
  });
  const sum = w.reduce((a, b) => a + b, 0);
  const lw = header.map((h, i) => Math.max(...[h, ...rows.map((r) => r[i] || "")].map((c) => Math.max(0, ...plain(c).split(/\s+/).map((x) => x.length)))));
  const minw = lw.map((n, ci) => Math.max(header[ci] === "#" ? 820 : 520, Math.ceil(n * (small ? 105 : 112)) + 170));
  let cw = w.map((x) => Math.floor((x / sum) * CONTENT_W));
  cw = cw.map((x, i) => Math.max(x, minw[i]));
  const tot = cw.reduce((a, b) => a + b, 0);
  cw = cw.map((x) => Math.floor((x / tot) * CONTENT_W));
  cw[cw.length - 1] += CONTENT_W - cw.reduce((a, b) => a + b, 0);
  const keep = rows.length <= 12;
  const mk = (txt, i, hdr, last) => new TableCell({
    width: { size: cw[i], type: WidthType.DXA },
    shading: hdr ? { type: ShadingType.CLEAR, color: "auto", fill: NAVY } : undefined,
    margins: { top: 40, bottom: 40, left: 70, right: 70 },
    children: [new Paragraph({ keepNext: keep && !last, children: inline(txt, { size: sz, ...(hdr ? { bold: true, color: "FFFFFF" } : {}) }) })],
  });
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: cw,
    rows: [
      new TableRow({ tableHeader: true, cantSplit: true, children: header.map((h, i) => mk(h, i, true)) }),
      ...rows.map((r, ri) => new TableRow({ cantSplit: true, children: header.map((_, i) => mk(r[i] || "", i, false, ri === rows.length - 1)) })),
    ],
  });
}

const kids = [];
let i = 0;
const splitRow = (l) => l.trim().replace(/^\||\|$/g, "").split("|").map((s) => s.trim());
let firstLine = true;
while (i < lines.length) {
  const line = lines[i];
  const t = line.trim();
  if (t === "" || t === "---") { i++; continue; }
  if (firstLine) {
    firstLine = false;
    kids.push(new Paragraph({ children: [new TextRun({ text: "Facilitator Guide: The Trophy and the Table", bold: true, size: 40, color: NAVY })], spacing: { after: 80 } }));
    kids.push(new Paragraph({ children: [new TextRun({ text: "FACILITATOR ONLY \u2014 contains the balance argument, the margin, the trap and the twist numbers. Do not distribute to Heroes.", bold: true, color: "a3312a" })], spacing: { after: 120 } }));
    i++;
    while (lines[i] && lines[i].trim()) { kids.push(new Paragraph({ children: inline(lines[i].trim(), { size: 20 }), spacing: { after: 100 } })); i++; }
    // boxed teacher-facing note, pulled from the guide's own "Teacher note" section
    const m = raw.match(/## Teacher note[^\n]*\n([\s\S]*?)\n---/);
    const paras = m[1].trim().split(/\n\s*\n/).map((x) => x.replace(/\n/g, " ").trim());
    kids.push(new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
      rows: [new TableRow({ cantSplit: true, children: [new TableCell({ width: { size: CONTENT_W, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, color: "auto", fill: "FBEAEA" },
        borders: ["top", "bottom", "left", "right"].reduce((o, k) => (o[k] = { style: BorderStyle.SINGLE, size: 12, color: "a3312a" }, o), {}),
        margins: { top: 100, bottom: 100, left: 160, right: 160 },
        children: [new Paragraph({ children: [new TextRun({ text: "Teacher note (required) \u2014 read before the room fills", bold: true, color: "a3312a", size: 24 })], spacing: { after: 80 } }),
          ...paras.map((x) => new Paragraph({ children: inline(x), spacing: { after: 80 } }))] })] })] }));
    kids.push(new Paragraph({ text: "", spacing: { after: 80 } }));
    // skip the original Teacher note section in the flow
    while (i < lines.length && !/^## Intro/.test(lines[i])) i++;
    continue;
  }
  const img = null;
  if (img) {
    const k = +img[1];
    const buf = fs.readFileSync(path.join(HERE, "build_assets", svgNames[k] + ".png"));
    const wpx = 470, ratio = [200 / 380, 250 / 380, 210 / 320][k];
    kids.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 80, after: 60 }, keepNext: k === 1,
      children: [new ImageRun({ type: "png", data: buf, transformation: { width: wpx, height: Math.round(wpx * ratio) },
        altText: { title: svgNames[k], description: svgAlts[k], name: svgNames[k] } })] }));
    if (k === 1) kids.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 160 },
      children: [new TextRun({ text: "153 club-pairs, 2015/16 to 2024/25. Red line = the fitted slope. Derived by the case author.", italics: true, size: 18 })] }));
    i++; continue;
  }
  if (/^###\s+/.test(t)) { kids.push(new Paragraph({ text: t.replace(/^###\s+/, ""), heading: HeadingLevel.HEADING_2, keepNext: true, spacing: { before: 220, after: 100 } })); i++; continue; }
  if (/^>\s?/.test(t)) {
    const b = [];
    while (i < lines.length && /^>\s?/.test(lines[i].trim())) { b.push(lines[i].trim().replace(/^>\s?/, "")); i++; }
    kids.push(new Paragraph({ children: inline(b.join(" ").trim()), indent: { left: 540 }, spacing: { after: 130 },
      border: { left: { style: BorderStyle.SINGLE, size: 12, color: "AAAAAA", space: 8 } } }));
    continue;
  }
  if (/^\d+\.\s+/.test(t)) {
    while (i < lines.length && /^\d+\.\s+/.test(lines[i].trim())) { kids.push(new Paragraph({ children: inline(lines[i].trim()), indent: { left: 540, hanging: 360 }, spacing: { after: 80 } })); i++; }
    continue;
  }
  if (/^##\s+/.test(t)) { kids.push(new Paragraph({ text: t.replace(/^##\s+/, ""), heading: HeadingLevel.HEADING_1, keepNext: true, spacing: { before: 320, after: 140 } })); i++; continue; }
  if (t.startsWith("|") && lines[i + 1] && /^\s*\|?[\s:|-]+\|?\s*$/.test(lines[i + 1]) && lines[i + 1].includes("-")) {
    const header = splitRow(t); let j = i + 2; const rows = [];
    while (j < lines.length && lines[j].trim().startsWith("|")) { rows.push(splitRow(lines[j])); j++; }
    kids.push(tableFrom(header, rows)); kids.push(new Paragraph({ text: "", spacing: { after: 80 } }));
    i = j; continue;
  }
  if (/^\s*-\s+/.test(line)) {
    while (i < lines.length && /^\s*-\s+/.test(lines[i])) {
      let txt = lines[i].replace(/^\s*-\s+/, ""); i++;
      while (i < lines.length && /^\s{2,}\S/.test(lines[i]) && !/^\s*-\s+/.test(lines[i])) { txt += " " + lines[i].trim(); i++; }
      kids.push(new Paragraph({ children: inline(txt), numbering: { reference: "bullets", level: 0 }, spacing: { after: 70 } }));
    }
    continue;
  }
  if (/^\s{2,}[a-z]\.\)/.test(line)) { kids.push(new Paragraph({ children: inline(t), indent: { left: 540 }, spacing: { after: 80 } })); i++; continue; }
  // paragraph: gather consecutive plain lines
  const buf = [t]; i++;
  while (i < lines.length && lines[i].trim() !== "" && lines[i].trim() !== "---" && !/^##\s/.test(lines[i]) &&
         !lines[i].trim().startsWith("|") && !/^\s*-\s+/.test(lines[i]) && !/^\s{2,}[a-z]\.\)/.test(lines[i]) && !/^>/.test(lines[i].trim()) && !/^\d+\.\s/.test(lines[i].trim()) && !/^###?\s/.test(lines[i])) { buf.push(lines[i].trim()); i++; }
  kids.push(new Paragraph({ children: inline(buf.join(" ")), spacing: { after: 130 } }));
}


// ---- publish-time run-of-show addition (not an answer key) ----
kids.push(new Paragraph({ text: "What a strong defense sounds like", heading: HeadingLevel.HEADING_1, keepNext: true, spacing: { before: 320, after: 140 } }));
kids.push(new Paragraph({ children: inline("The case has no single right answer: at the 2-point test point Keep the Winner leads narrowly, and the lead is fragile. Listen for reasoning quality, not for a side. A strong defense (a) separates detecting a shortfall from attributing it to anyone; (b) works both options from the model's predicted points, not from the 38 points actually earned; (c) states the break-even reset cost as the quantity the decision turns on, and says whether a reset cost below it is believable and why; (d) names which assumption it leans on that nobody can check (the reset cost, the 0.11 slope) and what changes if it moves; (e) reacts to the twist by saying what moved (the slope assumption) and what did not (nothing says a new manager repairs a real problem); and (f) talks about a model and a club's points, never about what a real person deserved. Accept any defended reset-cost range."), spacing: { after: 130 } }));
kids.push(new Paragraph({ children: inline("**Skills to name in the debrief:** scatter plot, correlation, line of best fit, linear equation, slope, mean, outlier, variability, sample size, random, evaluating a variable expression, percent of a number and solving a one-step equation (full list under Standards Touched On above)."), spacing: { after: 130 } }));

const doc = new Document({
  creator: "Math Builder", title: "Facilitator Guide: The Trophy and the Table",
  numbering: { config: [{ reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }] },
  styles: {
    default: { document: { run: { font: "Calibri", size: 22 } } },
    paragraphStyles: [{ id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 28, bold: true, color: NAVY, font: "Calibri" } }],
  },
  sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 } } }, children: kids }],
});
Packer.toBuffer(doc).then((buf) => {
  const out = path.join(HERE, "published", "The Trophy and the Table - Facilitator Guide.docx");
  fs.writeFileSync(out, buf); console.log("wrote", out, buf.length);
});
