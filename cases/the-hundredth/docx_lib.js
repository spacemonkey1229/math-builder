// Shared markdown -> docx helpers for The Hundredth (case-local, same precedent as
// cases/the-odd-lot/build_docx.js). Used by build_docx.js (student) and build_facilitator_docx.js.
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");
const {
  Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, LevelFormat, ExternalHyperlink, ImageRun, BorderStyle,
} = require("docx");

const NAVY = "1a3a5c";
const CONTENT_W = 9360; // US Letter, 1" margins
const CASE_DIR = __dirname;
const BUILD_DIR = path.join(CASE_DIR, "_build");

const numbering = {
  config: [{
    reference: "bullets",
    levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 540, hanging: 270 } } } }],
  }],
};

function inlineRuns(text, base = {}) {
  const runs = [];
  const re = /(\*\*[^*]+\*\*)|(\*[^*\s][^*]*\*)|(\[[^\]]+\]\([^)]+\))|(`[^`]+`)/g;
  let last = 0, m;
  const plain = (s) => { if (s) runs.push(new TextRun({ text: s, ...base })); };
  while ((m = re.exec(text)) !== null) {
    plain(text.slice(last, m.index));
    const tok = m[0];
    if (tok.startsWith("**")) runs.push(new TextRun({ text: tok.slice(2, -2), ...base, bold: true }));
    else if (tok.startsWith("[")) {
      const mm = tok.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
      runs.push(new ExternalHyperlink({ link: mm[2], children: [new TextRun({ text: mm[1], ...base, style: "Hyperlink" })] }));
    } else if (tok.startsWith("`")) runs.push(new TextRun({ text: tok.slice(1, -1), ...base, font: "Courier New" }));
    else runs.push(new TextRun({ text: tok.slice(1, -1), ...base, italics: true }));
    last = re.lastIndex;
  }
  plain(text.slice(last));
  if (!runs.length) runs.push(new TextRun({ text: "", ...base }));
  return runs;
}

function plainLen(t) { return t.replace(/\*\*|\*|`|\[([^\]]+)\]\([^)]+\)/g, "$1").length; }

function cell(text, width, header) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    margins: { top: 50, bottom: 50, left: 90, right: 90 },
    shading: header ? { type: ShadingType.CLEAR, color: "auto", fill: NAVY } : undefined,
    children: [new Paragraph({
      children: inlineRuns(text || "", header ? { bold: true, color: "FFFFFF", size: 18 } : { size: 18 }),
    })],
  });
}

function parseTable(lines) {
  const rows = lines.filter((l) => !/^\|[\s:|-]+\|$/.test(l.trim()));
  const cells = rows.map((l) => l.trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map((c) => c.trim()));
  const n = Math.max(...cells.map((r) => r.length));
  // width weights: sqrt of the longest cell in each column, with a floor, so narrow columns stay readable
  const weights = Array.from({ length: n }, (_, c) => Math.max(9, Math.sqrt(Math.max(...cells.map((r) => plainLen(r[c] || ""))) + 4) * 3));
  const total = weights.reduce((a, b) => a + b, 0);
  const minW = Array.from({ length: n }, (_, c) => Math.max(900, Math.max(...cells.map((r) => Math.max(0, ...(r[c] || "").replace(/\*\*|\*|`|\[([^\]]+)\]\([^)]+\)/g, "$1").split(/\s+/).map((w) => w.length)))) * 105 + 220));
  let widths = weights.map((w, c) => Math.max(minW[c], Math.floor((w / total) * CONTENT_W)));
  const over = widths.reduce((a, b) => a + b, 0) - CONTENT_W;
  if (over > 0) { const big = widths.indexOf(Math.max(...widths)); widths[big] -= over; }
  const drift = CONTENT_W - widths.reduce((a, b) => a + b, 0);
  widths[widths.length - 1] += drift;
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    rows: cells.map((r, ri) => new TableRow({
      tableHeader: ri === 0,
      cantSplit: true,
      children: Array.from({ length: n }, (_, ci) => cell(r[ci] || "", widths[ci], ri === 0)),
    })),
  });
}

// ---- SVG -> PNG via soffice (no rsvg/cairosvg on this machine). Adds the frame/background the
// browser would draw from the inline style, which soffice ignores.
function svgToPng(svg, name) {
  fs.mkdirSync(BUILD_DIR, { recursive: true });
  const vb = svg.match(/viewBox="0 0 (\d+) (\d+)"/);
  const w = parseInt(vb[1], 10), h = parseInt(vb[2], 10);
  const px = 900, pxh = Math.round(px * h / w);
  let s = svg.replace(/<svg\b([^>]*)>/, (m0, attrs) => {
    attrs = attrs.replace(/\sstyle="[^"]*"/, "").replace(/\s(width|height)="[^"]*"/g, "");
    return `<svg${attrs} width="${px}" height="${pxh}"><rect x="0" y="0" width="${w}" height="${h}" fill="#fafafa" stroke="#999" stroke-width="1"/>`;
  });
  const svgPath = path.join(BUILD_DIR, name + ".svg");
  fs.writeFileSync(svgPath, s);
  const pngPath = path.join(BUILD_DIR, name + ".png");
  for (let attempt = 0; attempt < 3 && !fs.existsSync(pngPath); attempt++) {
    try { fs.rmSync(pngPath, { force: true }); execFileSync("soffice", ["--headless", "--convert-to", "png", "--outdir", BUILD_DIR, svgPath], { stdio: "pipe" }); } catch (e) { /* retry */ }
  }
  if (!fs.existsSync(pngPath)) throw new Error("soffice failed to render " + svgPath);
  return pngPath;
}

function pngSize(buf) { return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) }; }

function mdToChildren(md, opts = {}) {
  const lines = md.split("\n");
  const out = [];
  let svgCount = 0;
  let i = 0;
  const isBlockStart = (l) => /^\s*$/.test(l) || /^#{1,3}\s+/.test(l) || /^```/.test(l) || /^\|/.test(l.trim()) ||
    /^>\s?/.test(l) || /^---+\s*$/.test(l.trim()) || /^\s*([-*]|\d+[.)]|[a-z][.)])\s+/.test(l) || /^<svg/.test(l.trim()) || /^<!--/.test(l.trim());
  while (i < lines.length) {
    const line = lines[i];
    if (/^\s*$/.test(line)) { i++; continue; }
    if (/^<!--/.test(line.trim())) { while (i < lines.length && !/-->/.test(lines[i])) i++; i++; continue; }
    if (/^<svg/.test(line.trim())) {
      const buf = [];
      while (i < lines.length) { buf.push(lines[i]); if (/<\/svg>/.test(lines[i])) { i++; break; } i++; }
      const png = svgToPng(buf.join("\n"), `${opts.svgPrefix || "diag"}${svgCount++}`);
      const data = fs.readFileSync(png);
      const { width, height } = pngSize(data);
      const tw = 440, th = Math.round(tw * height / width);
      const label = (buf.join(" ").match(/aria-label="([^"]*)"/) || [, "diagram"])[1];
      out.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 80, after: 120 }, keepNext: false,
        children: [new ImageRun({ type: "png", data, transformation: { width: tw, height: th },
          altText: { title: label, description: label, name: label } })] }));
      continue;
    }
    if (/^#{1,3}\s+/.test(line)) {
      const lvl = line.startsWith("### ") ? HeadingLevel.HEADING_3 : (line.startsWith("## ") ? HeadingLevel.HEADING_1 : HeadingLevel.HEADING_2);
      out.push(new Paragraph({ heading: lvl, keepNext: true, spacing: { before: 280, after: 120 },
        children: inlineRuns(line.replace(/^#{1,3}\s+/, ""), { color: NAVY }) }));
      i++; continue;
    }
    if (/^\|/.test(line.trim())) {
      const t = [];
      while (i < lines.length && /^\|/.test(lines[i].trim())) { t.push(lines[i]); i++; }
      out.push(parseTable(t));
      out.push(new Paragraph({ spacing: { after: 100 }, children: [] }));
      continue;
    }
    if (/^>\s?/.test(line)) {
      const q = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) { q.push(lines[i].replace(/^>\s?/, "")); i++; }
      out.push(new Paragraph({ spacing: { after: 120 }, indent: { left: 360 },
        border: { left: { style: BorderStyle.SINGLE, size: 12, color: "999999", space: 8 } },
        children: inlineRuns(q.join(" "), { italics: true }) }));
      continue;
    }
    if (/^---+\s*$/.test(line.trim())) { i++; continue; }
    const bm = line.match(/^(\s*)([-*])\s+(.*)$/);
    if (bm) {
      const item = [bm[3]]; i++;
      while (i < lines.length && !isBlockStart(lines[i])) { item.push(lines[i].trim()); i++; }
      out.push(new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 70 }, children: inlineRuns(item.join(" ")) }));
      continue;
    }
    const lm = line.match(/^(\s*)(\d+[.)]|[a-z][.)]\)?)\s+(.*)$/);
    if (lm) {
      const depth = Math.min(2, Math.floor(lm[1].length / 4));
      const item = [lm[3]]; i++;
      while (i < lines.length && !isBlockStart(lines[i])) { item.push(lines[i].trim()); i++; }
      out.push(new Paragraph({ spacing: { after: 90 }, indent: { left: 360 + depth * 400, hanging: 360 },
        children: inlineRuns(`${lm[2]} ${item.join(" ")}`) }));
      continue;
    }
    const pl = [line.trim()]; i++;
    while (i < lines.length && !isBlockStart(lines[i])) { pl.push(lines[i].trim()); i++; }
    out.push(new Paragraph({ spacing: { after: 120 }, children: inlineRuns(pl.join(" ")) }));
  }
  return out;
}

function boxedNote(title, paragraphs, fill = "FBEAEA", color = "a3312a") {
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [CONTENT_W],
    rows: [new TableRow({ cantSplit: false, children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA },
      margins: { top: 100, bottom: 100, left: 160, right: 160 },
      shading: { type: ShadingType.CLEAR, color: "auto", fill },
      borders: ["top", "bottom", "left", "right"].reduce((o, k) => (o[k] = { style: BorderStyle.SINGLE, size: 10, color }, o), {}),
      children: [
        new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: title, bold: true, color, size: 22 })] }),
        ...paragraphs.map((t) => new Paragraph({ spacing: { after: 80 }, children: inlineRuns(t, { size: 20 }) })),
      ],
    })] })],
  });
}

module.exports = { inlineRuns, mdToChildren, parseTable, boxedNote, numbering, NAVY, CONTENT_W, CASE_DIR };
