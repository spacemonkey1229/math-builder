// Case-local student .docx builder for The Gijon Rule (same precedent as cases/the-cold-hit/build_docx.js,
// but the body is converted from case.md so the two cannot drift). Run from this directory:
//     python3 build_worked_example.py && node build_docx.js && node build_facilitator_docx.js
// Exports mdToChildren()/styles/numbering so build_facilitator_docx.js shares one renderer.
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType,
  ShadingType, AlignmentType, LevelFormat, ExternalHyperlink, ImageRun, BorderStyle,
  Footer, PageNumber,
} = require("docx");

const NAVY = "1a3a5c";
const GOLD = "c9a227";
const CONTENT_W = 10040;           // US Letter 12240 - 2 x 1100 margins

const numbering = {
  config: [{
    reference: "bullets",
    levels: [
      { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 540, hanging: 270 } } } },
      { level: 1, format: LevelFormat.BULLET, text: "–", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 1080, hanging: 270 } } } },
    ],
  }],
};

const styles = {
  default: { document: { run: { font: "Calibri", size: 22 } } },
  paragraphStyles: [
    { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 30, bold: true, color: NAVY, font: "Calibri" },
      paragraph: { spacing: { before: 320, after: 140 }, outlineLevel: 0, keepNext: true } },
    { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 25, bold: true, color: NAVY, font: "Calibri" },
      paragraph: { spacing: { before: 240, after: 100 }, outlineLevel: 1, keepNext: true } },
  ],
};

// ---------- inline markdown -> runs ----------
function inlineRuns(text, base = {}) {
  const runs = [];
  const re = /(\*\*[^*]+\*\*)|(\[[^\]]+\]\([^)]+\))|(`[^`]+`)|(\*[^*\s][^*]*\*)/g;
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

function plainLen(s) { return s.replace(/\*\*|\*|`|\[([^\]]+)\]\([^)]+\)/g, "$1").length; }

// ---------- tables ----------
function parseTable(lines, { grid = false } = {}) {
  const rows = lines.filter((l) => !/^\|[\s:|-]+\|$/.test(l.trim()));
  const cells = rows.map((l) => l.trim().replace(/^\||\|$/g, "").split("|").map((c) => c.trim()));
  const ncols = Math.max(...cells.map((r) => r.length));
  let widths;
  if (grid) {
    const first = 1500; const rest = Math.floor((CONTENT_W - first) / (ncols - 1));
    widths = [first, ...Array(ncols - 1).fill(rest)];
  } else {
    const weight = Array.from({ length: ncols }, (_, ci) =>
      Math.min(46, Math.max(5, ...cells.map((r) => Math.min(46, plainLen(r[ci] || "")))) ) + 3);
    const tot = weight.reduce((a, b) => a + b, 0);
    widths = weight.map((w) => Math.max(600, Math.floor((w / tot) * CONTENT_W)));
    const drift = CONTENT_W - widths.reduce((a, b) => a + b, 0);
    widths[widths.length - 1] += drift;
  }
  const border = { style: BorderStyle.SINGLE, size: 4, color: "B8C2CE" };
  const borders = { top: border, bottom: border, left: border, right: border };
  const mk = (text, ci, header, rowIdx) => new TableCell({
    width: { size: widths[ci], type: WidthType.DXA },
    borders,
    margins: { top: 50, bottom: 50, left: 90, right: 90 },
    shading: header ? { type: ShadingType.CLEAR, color: "auto", fill: NAVY }
      : (grid && ci === 0 ? { type: ShadingType.CLEAR, color: "auto", fill: "E8EEF5" } : undefined),
    children: [new Paragraph({
      alignment: grid && ci > 0 ? AlignmentType.CENTER : AlignmentType.LEFT,
      children: inlineRuns(text || "", { size: 18, color: header ? "FFFFFF" : undefined, bold: header ? true : undefined }),
    })],
  });
  const trs = cells.map((r, ri) => new TableRow({
    tableHeader: ri === 0, cantSplit: true,
    height: grid && ri > 0 ? { value: 420, rule: "atLeast" } : undefined,
    children: Array.from({ length: ncols }, (_, ci) => mk(r[ci] || "", ci, ri === 0, ri)),
  }));
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: widths, rows: trs });
}

// ---------- markdown body -> docx children ----------
const LISTRE = /^(\s*)([-*]|\d+\.\)|\d+\.|[a-z]\.\))\s+(.*)$/;
function mdToChildren(md, opts = {}) {
  const lines = md.split("\n");
  const out = [];
  let i = 0;
  const isBlock = (l) => /^\s*$/.test(l) || /^#{1,3}\s+/.test(l) || /^\|/.test(l.trim()) || /^>\s?/.test(l)
    || /^---+\s*$/.test(l.trim()) || LISTRE.test(l) || /^<(figure|svg|!--)/.test(l.trim());
  while (i < lines.length) {
    const line = lines[i];
    if (/^\s*$/.test(line)) { i++; continue; }
    if (/^<!--/.test(line.trim())) { while (i < lines.length && !/-->/.test(lines[i])) i++; i++; continue; }
    if (/^---+\s*$/.test(line.trim())) { i++; continue; }
    const hm = line.match(/^(#{1,3})\s+(.*)$/);
    if (hm) {
      out.push(new Paragraph({ heading: hm[1].length === 1 ? HeadingLevel.HEADING_1 : (hm[1].length === 2 ? HeadingLevel.HEADING_1 : HeadingLevel.HEADING_2),
        children: inlineRuns(hm[2]) }));
      i++; continue;
    }
    if (/^<svg/.test(line.trim())) {
      while (i < lines.length && !/<\/svg>/.test(lines[i])) i++;
      i++;
      const png = fs.readFileSync(path.join(__dirname, "_worked_example.png"));
      out.push(new Paragraph({ alignment: AlignmentType.CENTER, keepNext: false, spacing: { before: 120, after: 120 },
        children: [new ImageRun({ type: "png", data: png, transformation: { width: 650, height: 279 },
          altText: { title: "Worked example", description: "Worked example for a West Germany 2-0 Austria scoreline: two filled 7 by 7 grids (Algeria goals against Chile goals) marked safe, not safe or unresolved under Option A and Option B, and a Venn diagram of the safe cells with region counts 5, 29 and 0.", name: "worked-example" } })] }));
      continue;
    }
    if (/^<figure/.test(line.trim())) {
      const buf = [];
      while (i < lines.length) { buf.push(lines[i]); if (/<\/figure>/.test(lines[i])) break; i++; }
      i++;
      const html = buf.join(" ");
      const cap = (html.match(/<figcaption>(.*?)<\/figcaption>/) || [, ""])[1];
      // Photo is deliberately not embedded in the printable copy (no image file is downloaded at build time);
      // the caption and the Commons source link carry the attribution. The Interactive HTML shows the photo.
      out.push(new Paragraph({ spacing: { before: 60, after: 40 }, children: [new TextRun({ text: "Photograph (shown in the Interactive version; not reproduced in this printable copy):", italics: true, size: 20 })] }));
      out.push(new Paragraph({ spacing: { after: 140 }, children: [
        new TextRun({ text: cap.replace(/\s*\[S12\]\s*$/, "") + " [S12] ", italics: true, size: 20 }),
        new ExternalHyperlink({ link: "https://commons.wikimedia.org/wiki/File:Interior_de_El_Molin%C3%B3n.JPG", children: [new TextRun({ text: "View the photo on Wikimedia Commons", style: "Hyperlink", size: 20 })] }),
      ] }));
      continue;
    }
    if (/^\|/.test(line.trim())) {
      const t = [];
      while (i < lines.length && /^\|/.test(lines[i].trim())) { t.push(lines[i]); i++; }
      const grid = /^\|\s*Algeria \\ Chile/.test(t[0]);
      out.push(parseTable(t, { grid }));
      out.push(new Paragraph({ spacing: { after: 80 }, children: [] }));
      continue;
    }
    if (/^>\s?/.test(line)) {
      // blockquote: a bare ">" line separates quoted paragraphs
      let q = [];
      const flush = () => {
        if (!q.length) return;
        out.push(new Paragraph({ spacing: { before: 40, after: 90 }, indent: { left: 240, right: 240 },
          shading: { type: ShadingType.CLEAR, color: "auto", fill: "FBF4DC" },
          border: { left: { style: BorderStyle.SINGLE, size: 18, color: GOLD, space: 8 } },
          children: inlineRuns(q.join(" ")) }));
        q = [];
      };
      while (i < lines.length && /^>\s?/.test(lines[i])) {
        const t = lines[i].replace(/^>\s?/, "").trim();
        if (!t) flush(); else q.push(t);
        i++;
      }
      flush();
      continue;
    }
    const lm = line.match(LISTRE);
    if (lm) {
      const indent = lm[1].length;
      const body = [lm[3]]; i++;
      while (i < lines.length && !isBlock(lines[i])) { body.push(lines[i].trim()); i++; }
      const text = body.join(" ");
      if (/^[-*]$/.test(lm[2])) {
        out.push(new Paragraph({ numbering: { reference: "bullets", level: indent >= 2 ? 1 : 0 }, spacing: { after: 90 }, children: inlineRuns(text) }));
      } else {
        const ind = indent >= 2 ? 1080 : 360;
        out.push(new Paragraph({ spacing: { after: 100 }, indent: { left: ind, hanging: 360 },
          children: [new TextRun({ text: lm[2] + "\t" }), ...inlineRuns(text)],
          tabStops: [{ type: "left", position: ind }] }));
      }
      continue;
    }
    const para = [line.trim()]; i++;
    while (i < lines.length && !isBlock(lines[i])) { para.push(lines[i].trim()); i++; }
    out.push(new Paragraph({ spacing: { after: 130 }, children: inlineRuns(para.join(" ")) }));
  }
  return out;
}

function footer(label) {
  return new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
    new TextRun({ text: label + "  |  Page ", size: 16, color: "5b6472" }),
    new TextRun({ children: [PageNumber.CURRENT], size: 16, color: "5b6472", font: "Calibri" }),
  ] })] });
}

async function buildStudent() {
  let md = fs.readFileSync(path.join(__dirname, "case.md"), "utf8");
  // Only the FACILITATOR ONLY comment marker line is removed (it is a bare HTML comment mid-file; Appendix H follows it
  // and is student-facing). case.md holds no facilitator prose; that lives in FACILITATOR.md and case.json.
  md = md.replace(/<!--\s*FACILITATOR ONLY[\s\S]*?-->/g, "");
  const ls = md.split("\n");
  const title = ls[0].trim();      // "Case Study: The Gijon Rule"
  const sub = ls[1].trim();
  const body = ls.slice(2).join("\n");
  const children = [
    new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: title, bold: true, size: 44, color: NAVY })] }),
    new Paragraph({ spacing: { after: 200 }, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 6 } },
      children: [new TextRun({ text: sub, italics: true, size: 22 })] }),
    ...mdToChildren(body),
  ];
  const doc = new Document({
    numbering, styles,
    sections: [{
      properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 } } },
      footers: { default: footer("The Gijon Rule — Case Study") },
      children,
    }],
  });
  const buf = await Packer.toBuffer(doc);
  fs.mkdirSync(path.join(__dirname, "published"), { recursive: true });
  const out = path.join(__dirname, "published", "The Gijon Rule - Case Study.docx");
  fs.writeFileSync(out, buf);
  console.log("wrote", out, buf.length, "bytes");
}

module.exports = { mdToChildren, inlineRuns, parseTable, styles, numbering, footer, NAVY, GOLD, CONTENT_W };
if (require.main === module) buildStudent().catch((e) => { console.error(e); process.exit(1); });
