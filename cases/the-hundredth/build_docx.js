// Student Case Study .docx for The Hundredth, converted from case.md (so the two cannot drift).
// Strips everything from <!-- FACILITATOR ONLY ... --> onward before converting.
// Run from anywhere: node cases/the-hundredth/build_docx.js
const fs = require("fs");
const path = require("path");
const { Document, Packer, Paragraph, TextRun, AlignmentType } = require("docx");
const { mdToChildren, numbering, NAVY } = require("./docx_lib");

let md = fs.readFileSync(path.join(__dirname, "case.md"), "utf8");
md = md.split(/<!--\s*FACILITATOR ONLY[\s\S]*?-->/)[0] + (md.split(/<!--\s*FACILITATOR ONLY[\s\S]*?-->/)[1] || "");
const lines = md.split("\n");
const titleLine = lines[0].trim();
const subLine = lines[1].trim();
const body = lines.slice(2).join("\n");

const doc = new Document({
  numbering,
  styles: {
    default: { document: { run: { font: "Calibri", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 30, bold: true, color: NAVY, font: "Calibri" } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 26, bold: true, color: NAVY, font: "Calibri" } },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 80 }, children: [new TextRun({ text: titleLine, bold: true, size: 40, color: NAVY })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 }, children: [new TextRun({ text: subLine, italics: true, size: 22 })] }),
      ...mdToChildren(body, { svgPrefix: "student_diag" }),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  const out = path.join(__dirname, "published", "The Hundredth - Case Study.docx");
  fs.mkdirSync(path.dirname(out), { recursive: true });
  fs.writeFileSync(out, buf);
  console.log("wrote", out, buf.length, "bytes");
});
