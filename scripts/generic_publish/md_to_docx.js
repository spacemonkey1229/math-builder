#!/usr/bin/env node
/*
 * md_to_docx.js -- generic case.md/FACILITATOR.md -> .docx converter.
 *
 * Usage: node md_to_docx.js <input.md> <output.docx> [--strip-facilitator] [--title-suffix "..."]
 *
 * Handles the subset of markdown this project's case.md/FACILITATOR.md files
 * actually use: #/##/### headers, --- horizontal rules -> page-break-free
 * section spacers, pipe tables, **bold**, *italic*, bullet lists (- / *),
 * numbered lists (1. / 1)), blockquotes (>), and plain paragraphs. Bare
 * markdown links [text](url) become real hyperlinks.
 *
 * --strip-facilitator removes everything from the first
 * "<!-- FACILITATOR ONLY" marker onward (case-publish's hard rule: the
 * answer key must never reach the student docx).
 */
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, ExternalHyperlink, PageBreak
} = require('docx');

const args = process.argv.slice(2);
const inputPath = args[0];
const outputPath = args[1];
const stripFacilitator = args.includes('--strip-facilitator');

if (!inputPath || !outputPath) {
  console.error('usage: node md_to_docx.js <in.md> <out.docx> [--strip-facilitator]');
  process.exit(1);
}

let raw = fs.readFileSync(inputPath, 'utf8');

if (stripFacilitator) {
  const idx = raw.indexOf('<!-- FACILITATOR ONLY');
  if (idx !== -1) raw = raw.slice(0, idx);
}

// Strip HTML comments entirely (facilitator-only inline notes, etc.)
raw = raw.replace(/<!--[\s\S]*?-->/g, '');

const lines = raw.split('\n');

// ---------- inline formatting: bold/italic/links -> TextRun[] ----------
function parseInline(text) {
  const runs = [];
  // tokenize on **bold**, *italic*, [text](url)
  const re = /(\*\*(.+?)\*\*)|(\*(.+?)\*)|(\[([^\]]+)\]\(([^)]+)\))/g;
  let last = 0;
  let m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) runs.push(new TextRun(text.slice(last, m.index)));
    if (m[1]) {
      runs.push(new TextRun({ text: m[2], bold: true }));
    } else if (m[3]) {
      runs.push(new TextRun({ text: m[4], italics: true }));
    } else if (m[5]) {
      runs.push(new ExternalHyperlink({
        link: m[7],
        children: [new TextRun({ text: m[6], style: 'Hyperlink' })],
      }));
    }
    last = re.lastIndex;
  }
  if (last < text.length) runs.push(new TextRun(text.slice(last)));
  if (runs.length === 0) runs.push(new TextRun(text));
  return runs;
}

function cleanCell(text) {
  return text.replace(/\\\|/g, '|').trim();
}

function isTableSep(line) {
  return /^\s*\|?[\s:|-]+\|?\s*$/.test(line) && line.includes('-');
}

function makeTable(headerCells, rows) {
  const ncols = headerCells.length;
  const colWidth = Math.floor(9000 / ncols);
  const widths = new Array(ncols).fill(colWidth);
  const headerRow = new TableRow({
    children: headerCells.map((c, i) => new TableCell({
      width: { size: widths[i], type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: 'DDDDDD' },
      children: [new Paragraph({ children: parseInline(cleanCell(c)).map(r => { r.bold = true; return r; }) })],
    })),
  });
  const bodyRows = rows.map(r => new TableRow({
    children: r.map((c, i) => new TableCell({
      width: { size: widths[i] || colWidth, type: WidthType.DXA },
      children: [new Paragraph({ children: parseInline(cleanCell(c)) })],
    })),
  }));
  return new Table({
    width: { size: 9000, type: WidthType.DXA },
    columnWidths: widths,
    rows: [headerRow, ...bodyRows],
  });
}

const children = [];
let i = 0;
while (i < lines.length) {
  let line = lines[i];

  if (line.trim() === '') { i++; continue; }
  if (line.trim() === '---') { i++; continue; } // section rule -> just spacing

  // Title block first line "# Case Study: X"
  if (/^#\s+/.test(line)) {
    children.push(new Paragraph({ text: line.replace(/^#\s+/, ''), heading: HeadingLevel.TITLE }));
    i++; continue;
  }
  if (/^##\s+/.test(line)) {
    children.push(new Paragraph({ text: line.replace(/^##\s+/, ''), heading: HeadingLevel.HEADING_1, spacing: { before: 300, after: 150 } }));
    i++; continue;
  }
  if (/^###\s+/.test(line)) {
    children.push(new Paragraph({ text: line.replace(/^###\s+/, ''), heading: HeadingLevel.HEADING_2, spacing: { before: 250, after: 120 } }));
    i++; continue;
  }

  // Table block
  if (line.trim().startsWith('|')) {
    const headerCells = line.trim().replace(/^\||\|$/g, '').split('|').map(s => s.trim());
    if (i + 1 < lines.length && isTableSep(lines[i + 1])) {
      let j = i + 2;
      const rows = [];
      while (j < lines.length && lines[j].trim().startsWith('|')) {
        const cells = lines[j].trim().replace(/^\||\|$/g, '').split('|').map(s => s.trim());
        rows.push(cells);
        j++;
      }
      children.push(makeTable(headerCells, rows));
      children.push(new Paragraph({ text: '' }));
      i = j; continue;
    }
  }

  // Bullet list
  if (/^\s*[-*]\s+/.test(line)) {
    while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) {
      const indent = lines[i].match(/^(\s*)/)[1].length;
      const text = lines[i].replace(/^\s*[-*]\s+/, '');
      children.push(new Paragraph({
        children: parseInline(text),
        bullet: { level: indent > 0 ? 1 : 0 },
      }));
      i++;
    }
    continue;
  }

  // Numbered list ("1.)" / "1." / "a.)")
  if (/^\s*[a-zA-Z0-9]+[.)]\s*[a-zA-Z0-9]*[.)]?\s+/.test(line) && /^\s*\d+[.)]/.test(line)) {
    while (i < lines.length && /^\s*\d+[.)]/.test(lines[i])) {
      const indent = lines[i].match(/^(\s*)/)[1].length;
      const text = lines[i].replace(/^\s*/, '');
      children.push(new Paragraph({
        children: parseInline(text),
        indent: { left: indent > 0 ? 720 : 0 },
      }));
      i++;
    }
    continue;
  }
  if (/^\s{4}[a-z][.)]\s+/.test(line)) {
    const text = line.trim();
    children.push(new Paragraph({ children: parseInline(text), indent: { left: 720 } }));
    i++; continue;
  }

  // Blockquote
  if (/^>\s*/.test(line)) {
    let buf = [];
    while (i < lines.length && /^>\s*/.test(lines[i])) {
      buf.push(lines[i].replace(/^>\s*/, ''));
      i++;
    }
    children.push(new Paragraph({
      children: parseInline(buf.join(' ')),
      indent: { left: 720 },
      border: { left: { style: BorderStyle.SINGLE, size: 12, color: 'AAAAAA', space: 8 } },
    }));
    continue;
  }

  // Plain paragraph -- collect until blank/structural line
  let buf = [line];
  i++;
  while (i < lines.length && lines[i].trim() !== '' && lines[i].trim() !== '---' &&
         !/^#{1,3}\s+/.test(lines[i]) && !lines[i].trim().startsWith('|') &&
         !/^\s*[-*]\s+/.test(lines[i]) && !/^\s*\d+[.)]/.test(lines[i]) && !/^>\s*/.test(lines[i])) {
    buf.push(lines[i]);
    i++;
  }
  children.push(new Paragraph({ children: parseInline(buf.join(' ')), spacing: { after: 150 } }));
}

const doc = new Document({
  sections: [{
    properties: {
      page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 } },
    },
    children,
  }],
  styles: {
    default: {
      document: { run: { font: 'Calibri', size: 22 } },
    },
  },
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(outputPath, buf);
  console.log('wrote', outputPath, buf.length, 'bytes');
});
