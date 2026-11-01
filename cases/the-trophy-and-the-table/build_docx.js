// Student Case Study .docx for "The Trophy and the Table", built directly from case.md.
// Strips everything from the <!-- FACILITATOR ONLY marker onward and all HTML comments.
// Inline SVGs are rendered to PNG by render_svgs.py (build_assets/) and embedded as images.
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType,
  ShadingType, AlignmentType, LevelFormat, ExternalHyperlink, ImageRun, BorderStyle,
} = require("../../node_modules/docx");

const HERE = __dirname;
const NAVY = "1a3a5c";
const CONTENT_W = 10080; // US Letter, 1080 margins
let raw = fs.readFileSync(path.join(HERE, "case.md"), "utf8");
const cut = raw.indexOf("<!-- FACILITATOR ONLY");
if (cut !== -1) raw = raw.slice(0, cut) + raw.slice(raw.indexOf("-->", cut) + 3); // drop the marker comment only; nothing student-facing follows it except Appendix H
raw = raw.replace(/<!--[\s\S]*?-->/g, "");

// pull SVG blocks out and replace with tokens
const svgNames = ["scoring_rule", "persistence_scatter", "residual_example"];
const svgAlts = [];
let svgIdx = 0;
raw = raw.replace(/<svg[\s\S]*?<\/svg>/g, (m) => {
  const alt = (m.match(/aria-label="([^"]*)"/) || [, ""])[1];
  svgAlts.push(alt);
  return `@@IMG${svgIdx++}@@`;
});
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
    kids.push(new Paragraph({ children: [new TextRun({ text: t, bold: true, size: 40, color: NAVY })], spacing: { after: 80 } }));
    i++;
    if (lines[i] && lines[i].trim()) { kids.push(new Paragraph({ children: [new TextRun({ text: lines[i].trim(), italics: true, size: 20 })], spacing: { after: 160 } })); i++; }
    continue;
  }
  const img = t.match(/^@@IMG(\d)@@$/);
  if (img) {
    const k = +img[1];
    const buf = fs.readFileSync(path.join(HERE, "build_assets", svgNames[k] + ".png"));
    const wpx = 470, ratio = [200 / 380, 250 / 380, 210 / 360][k];
    kids.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 80, after: 60 }, keepNext: k === 1,
      children: [new ImageRun({ type: "png", data: buf, transformation: { width: wpx, height: Math.round(wpx * ratio) },
        altText: { title: svgNames[k], description: svgAlts[k], name: svgNames[k] } })] }));
    if (k === 1) kids.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 160 },
      children: [new TextRun({ text: "153 club-pairs, 2015/16 to 2024/25. Red line = the fitted slope. Derived by the case author.", italics: true, size: 18 })] }));
    i++; continue;
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
      kids.push(new Paragraph({ children: inline(lines[i].replace(/^\s*-\s+/, "")), numbering: { reference: "bullets", level: 0 }, spacing: { after: 70 } }));
      i++;
    }
    continue;
  }
  if (/^\s{2,}[a-z]\.\)/.test(line)) { kids.push(new Paragraph({ children: inline(t), indent: { left: 540 }, spacing: { after: 80 } })); i++; continue; }
  // paragraph: gather consecutive plain lines
  const buf = [t]; i++;
  while (i < lines.length && lines[i].trim() !== "" && lines[i].trim() !== "---" && !/^##\s/.test(lines[i]) &&
         !lines[i].trim().startsWith("|") && !/^\s*-\s+/.test(lines[i]) && !/^\s{2,}[a-z]\.\)/.test(lines[i]) && !/^@@IMG/.test(lines[i].trim())) { buf.push(lines[i].trim()); i++; }
  kids.push(new Paragraph({ children: inline(buf.join(" ")), spacing: { after: 130 } }));
}

const doc = new Document({
  creator: "Math Builder", title: "Case Study: The Trophy and the Table",
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
  const out = path.join(HERE, "published", "The Trophy and the Table - Case Study.docx");
  fs.writeFileSync(out, buf); console.log("wrote", out, buf.length);
});
