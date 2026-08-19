#!/usr/bin/env node
// Generic case.md -> student .docx and FACILITATOR.md -> facilitator .docx converter.
// Reusable across every case in the pipeline. Reads markdown, does a reasonably faithful
// (not pixel-perfect) render: headings, paragraphs with **bold**/*italic*/[link](url), and
// pipe tables. Strips everything from <!-- FACILITATOR ONLY --> onward for the student docx.
//
// Usage: node build_docx.js <case-id> [--project <path>]
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, ExternalHyperlink, PageBreak,
} = require('docx');

const args = process.argv.slice(2);
const caseId = args[0];
if (!caseId) { console.error('usage: build_docx.js <case-id>'); process.exit(1); }
const projIdx = args.indexOf('--project');
const PROJECT = projIdx >= 0 ? args[projIdx + 1] : process.cwd();
const cdir = path.join(PROJECT, 'cases', caseId);

const US_LETTER = { size: { width: 12240, height: 15840 } };

// ---------- inline markdown -> TextRun[] ----------
function inlineRuns(text) {
  const runs = [];
  // tokenize on **bold**, *italic*, [text](url), `code`
  const re = /(\*\*[^*]+\*\*)|(\*[^*]+\*)|(\[[^\]]+\]\([^)]+\))|(`[^`]+`)/g;
  let last = 0, m;
  const pushPlain = (s) => { if (s) runs.push(new TextRun(s)); };
  while ((m = re.exec(text)) !== null) {
    pushPlain(text.slice(last, m.index));
    const tok = m[0];
    if (tok.startsWith('**')) runs.push(new TextRun({ text: tok.slice(2, -2), bold: true }));
    else if (tok.startsWith('[')) {
      const mm = tok.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
      runs.push(new ExternalHyperlink({
        link: mm[2],
        children: [new TextRun({ text: mm[1], style: 'Hyperlink' })],
      }));
    } else if (tok.startsWith('`')) runs.push(new TextRun({ text: tok.slice(1, -1), font: 'Courier New' }));
    else runs.push(new TextRun({ text: tok.slice(1, -1), italics: true }));
    last = re.lastIndex;
  }
  pushPlain(text.slice(last));
  if (runs.length === 0) runs.push(new TextRun(''));
  return runs;
}

function cell(text, opts = {}) {
  return new TableCell({
    width: { size: opts.width || 2000, type: WidthType.DXA },
    shading: opts.header ? { type: ShadingType.CLEAR, fill: 'DDDDDD' } : undefined,
    children: [new Paragraph({ children: inlineRuns(text || ''), }, )],
  });
}

function parseTable(lines) {
  // lines: array of "| a | b |" strings, first = header, second = separator
  const rows = lines.filter((l) => !/^\|[\s:|-]+\|$/.test(l.trim()));
  const cells = rows.map((l) => l.trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map((c) => c.trim()));
  const ncols = Math.max(...cells.map((r) => r.length));
  const colWidth = Math.floor(9000 / ncols);
  const trs = cells.map((r, ri) => new TableRow({
    children: Array.from({ length: ncols }, (_, ci) => cell(r[ci] || '', { header: ri === 0, width: colWidth })),
  }));
  return new Table({
    width: { size: 9000, type: WidthType.DXA },
    columnWidths: Array.from({ length: ncols }, () => colWidth),
    rows: trs,
  });
}

function mdToParagraphs(md, { stripFacilitator = true } = {}) {
  if (stripFacilitator) {
    // The marker may be a bare `<!-- FACILITATOR ONLY -->` or an annotated
    // one-line comment like `<!-- FACILITATOR ONLY: ... -->` (the form used
    // by nearly every case.md in this corpus) -- match either, and strip
    // everything from the marker onward, INCLUDING the comment line itself,
    // which must never survive as literal visible text in the student docx.
    // (Found 2026-08-18 while publishing airplane-manufacturer: the old
    // exact-match regex left the whole comment, unrendered, as a plain
    // paragraph at the end of every case study docx built from this script.)
    md = md.split(/<!--\s*FACILITATOR ONLY[\s\S]*?-->/)[0];
  }
  const lines = md.split('\n');
  const out = [];
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (/^\s*$/.test(line)) { i++; continue; }
    if (/^#{1,2}\s+/.test(line)) {
      const level = line.startsWith('## ') ? HeadingLevel.HEADING_2 : HeadingLevel.HEADING_1;
      out.push(new Paragraph({ heading: level, children: inlineRuns(line.replace(/^#{1,2}\s+/, '')), spacing: { before: 240, after: 120 } }));
      i++; continue;
    }
    if (/^```/.test(line)) {
      i++; const codeLines = [];
      while (i < lines.length && !/^```/.test(lines[i])) { codeLines.push(lines[i]); i++; }
      i++; // skip closing ```
      out.push(new Paragraph({ children: [new TextRun({ text: codeLines.join('\n'), font: 'Courier New' })], shading: { type: ShadingType.CLEAR, fill: 'F0F0F0' } }));
      continue;
    }
    if (/^\|/.test(line.trim())) {
      const tlines = [];
      while (i < lines.length && /^\|/.test(lines[i].trim())) { tlines.push(lines[i]); i++; }
      out.push(parseTable(tlines));
      out.push(new Paragraph({ text: '' }));
      continue;
    }
    if (/^>\s?/.test(line)) {
      const quoteLines = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) { quoteLines.push(lines[i].replace(/^>\s?/, '')); i++; }
      out.push(new Paragraph({ children: inlineRuns(quoteLines.join(' ')), indent: { left: 480 }, italics: true }));
      continue;
    }
    if (/^---+\s*$/.test(line.trim())) { i++; continue; }
    // list item (bullet or numbered, incl. sub-lettered a.) b.))
    const bulletM = line.match(/^(\s*)([-*]|\d+[.)]|[a-z][.)])\s+(.*)$/);
    if (bulletM) {
      const indentLevel = Math.min(2, Math.floor(bulletM[1].length / 4));
      const itemLines = [bulletM[3]];
      i++;
      while (
        i < lines.length &&
        !/^\s*$/.test(lines[i]) &&
        !/^#{1,2}\s+/.test(lines[i]) &&
        !/^```/.test(lines[i]) &&
        !/^\|/.test(lines[i].trim()) &&
        !/^>\s?/.test(lines[i]) &&
        !/^---+\s*$/.test(lines[i].trim()) &&
        !/^(\s*)([-*]|\d+[.)]|[a-z][.)])\s+(.*)$/.test(lines[i])
      ) {
        itemLines.push(lines[i]);
        i++;
      }
      out.push(new Paragraph({ children: inlineRuns(`${bulletM[2]} ${itemLines.join(' ')}`), indent: { left: 360 + indentLevel * 360 } }));
      continue;
    }
    // Plain text: a hard-wrapped source paragraph is a run of consecutive plain lines
    // with no blank line between them. Join them with a space before parsing inline
    // markdown, otherwise **bold**/[links]() that wrap across a source line break render
    // as literal asterisks/brackets and every wrapped line becomes its own paragraph.
    {
      const paraLines = [line];
      i++;
      while (
        i < lines.length &&
        !/^\s*$/.test(lines[i]) &&
        !/^#{1,2}\s+/.test(lines[i]) &&
        !/^```/.test(lines[i]) &&
        !/^\|/.test(lines[i].trim()) &&
        !/^>\s?/.test(lines[i]) &&
        !/^---+\s*$/.test(lines[i].trim()) &&
        !/^(\s*)([-*]|\d+[.)]|[a-z][.)])\s+(.*)$/.test(lines[i])
      ) {
        paraLines.push(lines[i]);
        i++;
      }
      out.push(new Paragraph({ children: inlineRuns(paraLines.join(' ')) }));
    }
  }
  return out;
}

function buildStudentDoc(caseMd, title) {
  const lines = caseMd.split('\n');
  const titleLine = (lines[0] || `Case Study: ${title}`).replace(/^#{1,2}\s+/, '');
  const subLine = lines[1] || '';
  const body = lines.slice(2).join('\n');
  const header = [
    new Paragraph({ children: [new TextRun({ text: titleLine, bold: true, size: 32 })], alignment: AlignmentType.CENTER, spacing: { after: 80 } }),
    new Paragraph({ children: [new TextRun({ text: subLine, italics: true, size: 22 })], alignment: AlignmentType.CENTER, spacing: { after: 240 } }),
  ];
  return new Document({
    sections: [{ properties: { page: US_LETTER }, children: [...header, ...mdToParagraphs(body, { stripFacilitator: true })] }],
  });
}

function buildFacilitatorDoc(facMd, title) {
  const header = [
    new Paragraph({ children: [new TextRun({ text: `Facilitator Guide: ${title}`, bold: true, size: 32 })], alignment: AlignmentType.CENTER, spacing: { after: 40 } }),
    new Paragraph({ children: [new TextRun({ text: 'FACILITATOR-ONLY -- contains the balance, the twist, and the trap. Do not share with Heroes before the discussion.', bold: true, color: 'CC0000' })], alignment: AlignmentType.CENTER, spacing: { after: 240 } }),
  ];
  return new Document({
    sections: [{ properties: { page: US_LETTER }, children: [...header, ...mdToParagraphs(facMd, { stripFacilitator: false })] }],
  });
}

async function main() {
  const caseMd = fs.readFileSync(path.join(cdir, 'case.md'), 'utf8');
  const facMd = fs.readFileSync(path.join(cdir, 'FACILITATOR.md'), 'utf8');
  const caseJson = JSON.parse(fs.readFileSync(path.join(cdir, 'case.json'), 'utf8'));
  const title = caseJson.title;

  const outDir = path.join(cdir, 'published');
  fs.mkdirSync(outDir, { recursive: true });

  const studentDoc = buildStudentDoc(caseMd, title);
  const facDoc = buildFacilitatorDoc(facMd, title);

  const studentPath = path.join(outDir, `${title} - Case Study.docx`);
  const facPath = path.join(outDir, `${title} - Facilitator Guide.docx`);

  fs.writeFileSync(studentPath, await Packer.toBuffer(studentDoc));
  fs.writeFileSync(facPath, await Packer.toBuffer(facDoc));

  console.log('wrote', studentPath);
  console.log('wrote', facPath);
}

main().catch((e) => { console.error(e); process.exit(1); });
