#!/usr/bin/env node
// the-search-box facilitator docx: same generic renderer as build_docx.js, but
// wraps the "Sensitivity note" section (SPEC §6 human-reviewed flag) in a
// visually boxed/shaded block at the top, per case-publish SKILL.md 1c.
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, AlignmentType, ExternalHyperlink,
} = require('docx');

const PROJECT = '/Users/manan/Documents/Claude/Projects/Math Builder';
const CID = 'the-search-box';
const cdir = path.join(PROJECT, 'cases', CID);
const US_LETTER = { size: { width: 12240, height: 15840 } };

// ---- reuse the generic renderer logic (copied, not re-implemented, from
// skills/case-publish/scripts/build_docx.js so behavior matches exactly) ----
function inlineRuns(text) {
  const runs = [];
  const re = /(\*\*[^*]+\*\*)|(\*[^*]+\*)|(\[[^\]]+\]\([^)]+\))|(`[^`]+`)/g;
  let last = 0, m;
  const pushPlain = (s) => { if (s) runs.push(new TextRun(s)); };
  while ((m = re.exec(text)) !== null) {
    pushPlain(text.slice(last, m.index));
    const tok = m[0];
    if (tok.startsWith('**')) runs.push(new TextRun({ text: tok.slice(2, -2), bold: true }));
    else if (tok.startsWith('[')) {
      const mm = tok.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
      runs.push(new ExternalHyperlink({ link: mm[2], children: [new TextRun({ text: mm[1], style: 'Hyperlink' })] }));
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
    children: [new Paragraph({ children: inlineRuns(text || '') })],
  });
}

function parseTable(lines) {
  const rows = lines.filter((l) => !/^\|[\s:|-]+\|$/.test(l.trim()));
  const cells = rows.map((l) => l.trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map((c) => c.trim()));
  const ncols = Math.max(...cells.map((r) => r.length));
  const colWidth = Math.floor(9000 / ncols);
  const trs = cells.map((r, ri) => new TableRow({
    children: Array.from({ length: ncols }, (_, ci) => cell(r[ci] || '', { header: ri === 0, width: colWidth })),
  }));
  return new Table({ width: { size: 9000, type: WidthType.DXA }, columnWidths: Array.from({ length: ncols }, () => colWidth), rows: trs });
}

// mdToParagraphs: identical control flow to the generic script, but every
// paragraph/table/heading it emits can optionally be shaded (boxed = true),
// used only for the sensitivity-note slice below.
function mdToParagraphs(md, { boxed = false } = {}) {
  const shading = boxed ? { type: ShadingType.CLEAR, fill: 'FFF4CC' } : undefined;
  const lines = md.split('\n');
  const out = [];
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (/^\s*$/.test(line)) { i++; continue; }
    if (/^#{1,3}\s+/.test(line)) {
      const level = line.startsWith('### ') ? HeadingLevel.HEADING_3 : (line.startsWith('## ') ? HeadingLevel.HEADING_2 : HeadingLevel.HEADING_1);
      out.push(new Paragraph({ heading: level, children: inlineRuns(line.replace(/^#{1,3}\s+/, '')), spacing: { before: 240, after: 120 }, shading }));
      i++; continue;
    }
    if (/^\|/.test(line.trim())) {
      const tlines = [];
      while (i < lines.length && /^\|/.test(lines[i].trim())) { tlines.push(lines[i]); i++; }
      out.push(parseTable(tlines));
      out.push(new Paragraph({ text: '', shading }));
      continue;
    }
    if (/^>\s?/.test(line)) {
      const quoteLines = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) { quoteLines.push(lines[i].replace(/^>\s?/, '')); i++; }
      out.push(new Paragraph({ children: inlineRuns(quoteLines.join(' ')), indent: { left: 480 }, italics: true, shading }));
      continue;
    }
    if (/^---+\s*$/.test(line.trim())) { i++; continue; }
    const bulletM = line.match(/^(\s*)([-*]|\d+[.)]|[a-z][.)])\s+(.*)$/);
    if (bulletM) {
      const indentLevel = Math.min(2, Math.floor(bulletM[1].length / 4));
      const itemLines = [bulletM[3]];
      i++;
      while (i < lines.length && !/^\s*$/.test(lines[i]) && !/^#{1,3}\s+/.test(lines[i]) && !/^\|/.test(lines[i].trim()) && !/^>\s?/.test(lines[i]) && !/^---+\s*$/.test(lines[i].trim()) && !/^(\s*)([-*]|\d+[.)]|[a-z][.)])\s+(.*)$/.test(lines[i])) {
        itemLines.push(lines[i]); i++;
      }
      out.push(new Paragraph({ children: inlineRuns(`${bulletM[2]} ${itemLines.join(' ')}`), indent: { left: 360 + indentLevel * 360 }, shading }));
      continue;
    }
    {
      const paraLines = [line];
      i++;
      while (i < lines.length && !/^\s*$/.test(lines[i]) && !/^#{1,3}\s+/.test(lines[i]) && !/^\|/.test(lines[i].trim()) && !/^>\s?/.test(lines[i]) && !/^---+\s*$/.test(lines[i].trim()) && !/^(\s*)([-*]|\d+[.)]|[a-z][.)])\s+(.*)$/.test(lines[i])) {
        paraLines.push(lines[i]); i++;
      }
      out.push(new Paragraph({ children: inlineRuns(paraLines.join(' ')), shading }));
    }
  }
  return out;
}

async function main() {
  const facMd = fs.readFileSync(path.join(cdir, 'FACILITATOR.md'), 'utf8');
  const caseJson = JSON.parse(fs.readFileSync(path.join(cdir, 'case.json'), 'utf8'));
  const title = caseJson.title;

  // Split out the "## Sensitivity note ..." section (SPEC §6 flag) so it can be
  // rendered boxed, at the very top, ahead of the rest of the guide.
  const lines = facMd.split('\n');
  const senStart = lines.findIndex((l) => /^##\s+Sensitivity note/.test(l));
  const nextHeading = lines.findIndex((l, idx) => idx > senStart && /^##\s+/.test(l));
  const before = lines.slice(0, senStart).join('\n');       // title/status block
  const senSection = lines.slice(senStart, nextHeading).join('\n');
  const rest = lines.slice(nextHeading).join('\n');

  const header = [
    new Paragraph({ children: [new TextRun({ text: `Facilitator Guide: ${title}`, bold: true, size: 32 })], alignment: AlignmentType.CENTER, spacing: { after: 40 } }),
    new Paragraph({ children: [new TextRun({ text: 'FACILITATOR-ONLY -- contains the balance, the twist, and the trap. Do not share with Heroes before the discussion.', bold: true, color: 'CC0000' })], alignment: AlignmentType.CENTER, spacing: { after: 240 } }),
  ];

  const body = [
    ...header,
    ...mdToParagraphs(before, { boxed: false }),
    ...mdToParagraphs(senSection, { boxed: true }),
    new Paragraph({ text: '', spacing: { after: 120 } }),
    ...mdToParagraphs(rest, { boxed: false }),
  ];

  const doc = new Document({ sections: [{ properties: { page: US_LETTER }, children: body }] });
  const outPath = path.join(cdir, 'published', `${title} - Facilitator Guide.docx`);
  fs.writeFileSync(outPath, await Packer.toBuffer(doc));
  console.log('wrote', outPath);
}

main().catch((e) => { console.error(e); process.exit(1); });
