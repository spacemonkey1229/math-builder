const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType,
} = require("docx");

const NAVY = "1a3a5c";

function h1(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_1, spacing: { before: 300, after: 150 } }); }
function h2(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 100 } }); }
function p(text, opts = {}) { return new Paragraph({ children: [new TextRun({ text, ...opts })], spacing: { after: 120 } }); }
function cell(text, opts = {}) {
  return new TableCell({
    width: { size: opts.width || 2000, type: WidthType.DXA },
    shading: opts.header ? { type: ShadingType.CLEAR, color: "auto", fill: NAVY } : undefined,
    children: [new Paragraph({ children: [new TextRun({ text: String(text), bold: !!opts.header, color: opts.header ? "FFFFFF" : undefined, size: 20 })] })],
  });
}
function table(headers, rows, widths) {
  const w = widths || headers.map(() => Math.floor(9000 / headers.length));
  return new Table({
    width: { size: 9000, type: WidthType.DXA },
    columnWidths: w,
    rows: [
      new TableRow({ children: headers.map((h, i) => cell(h, { header: true, width: w[i] })) }),
      ...rows.map(r => new TableRow({ children: r.map((c, i) => cell(c, { width: w[i] })) })),
    ],
  });
}

const doc = new Document({
  styles: { default: { document: { run: { font: "Calibri", size: 22 } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 } } },
    children: [
      new Paragraph({ children: [new TextRun({ text: "Facilitator Guide: The Manifest Split", bold: true, size: 40, color: NAVY })], spacing: { after: 80 } }),
      p("FACILITATOR ONLY — contains the balance argument, the margin, and the trap. Do not distribute to Heroes.", { bold: true, color: "a3312a" }),
      p("Case: The Manifest Split  ·  Tier: T2 (MS-core)  ·  Studio: Adventure  ·  Primary metric: containers cleared per inspector-hour  ·  Base margin: 11.26% (fragile — see the sensitivity note before Lessons Learned)"),
      p("Standards: Set, Subset, Union, Intersection, Empty Set, Venn Diagram, How to find the union and intersection of two sets, How to represent a set relationship using a Venn diagram (see case.json.standards[])."),

      h1("The Balance Argument (Answer Key — Facilitator Only)"),
      p("Argument for A (The Combined Lane): The Combined Lane wins if the intersection of hazmat-and-reefer containers is large enough that The Split Lanes’ re-handling cost outweighs its per-check speed advantage — and the twist shows that threshold is not hypothetical: a modest reclassification of 30 containers pushes the intersection from 25 to 55, past the crossover point (x = 40 at baseline H+R), and The Combined Lane’s simplicity (no re-handling, ever) wins outright."),
      p("Argument for B (The Split Lanes): The Split Lanes wins on tonight’s actual numbers (11.26% margin) because its specialist crews are faster at every single check, and tonight’s intersection (25 containers, out of 195 total flagged) is not yet large enough for the re-handling cost to erase that per-check speed advantage."),
      p("Margin at tonight’s base numbers: 11.26%, The Split Lanes (B) wins.", { bold: true }),
      p("The Trap: most learners will assume that because only a small slice of tonight’s flagged containers are dual-flagged (25 out of 195 — about 13%), the re-handling cost in The Split Lanes must be a minor detail that can’t possibly outweigh two specialist crews working faster on every single check. The real trap is that the intersection is exactly where the two plans’ fates are decided — a 13% slice earns its overlap being counted twice in Split Lanes’ cost column (once per lane, plus the re-handle), and that’s enough to erase most of the specialist speed advantage on tonight’s numbers. A learner who dismisses the intersection as “too small to matter” without actually running D2’s arithmetic will misjudge which lane is really ahead — and it’s much closer than the “specialists are always faster” instinct suggests."),

      h1("Facilitator Notes"),
      h2("Intro"),
      p("Heroes, Marcus has one lane decision and four hours before cutoff. One option is simple and never needs to move a container twice. The other is faster per check but sometimes has to move a container across the yard mid-inspection. There’s no lane the facilitator should pick either — the terminal manager doesn’t either until she sees the numbers."),
      h2("Launch"),
      p("Show a photo or diagram of a container yard with two inspection lanes side by side. Ask: “If you ran this yard tonight, would you rather have one lane that does everything, or two lanes that each do one thing really well?” Let them argue it cold, no numbers yet. Then: “Marcus has to commit to one lane setup before the shift locks in. Same containers, same cutoff, completely different bet on how the work gets split.” Ask each Hero: which lane do you run? Commit out loud."),
      h2("Anchor 1 — Take a stand and vote"),
      p("The Combined Lane or The Split Lanes. No reasoning yet. Hands up for A (Combined). Hands up for B (Split). Write the split on the board. “Is anyone courageous enough to stand with ______?”"),
      h2("Anchor 2 — What is the problem we’re solving?"),
      p("Do not let them start calculating yet. What’s the actual question, in one sentence? Is it “which lane checks containers fastest per container”? Is it “which lane never has to move a container twice”? Is it “which lane clears the whole flagged pool with the fewest total inspector-hours”? Those sound similar and are not the same question — only the last one is what Marcus’s shift actually gets measured on. Someone will say “obviously split them, specialists are always faster.” Push: “Faster at what, exactly? Faster per check, or faster to clear the whole pool tonight?” This is where the trap above lives — let the confusion grow, do not rescue them."),
      h2("Anchor 3 — What is the process?"),
      p("What’s the process we’ll go through to answer it? If we just add up how many hazmat checks and how many reefer checks happen, are we done? Is that the same as counting how many distinct containers get cleared tonight? If we end up with two rates like 7.18 and 7.99, how do we decide that’s close enough to be a real discussion, versus one lane just winning? What’s our tiebreaker before we see the numbers?"),
      h2("Anchor 4 — What don’t we know?"),
      p("What’s missing that we’d need to answer this properly? Appendix D gives the assumptions behind every timing figure — none of the five per-container check times are pulled from a real published number for this exact kind of terminal check. Have them try a faster and a slower version of each time and see how much the comparison moves. What are we assuming stays the same about tonight’s flagged pool between now and when the crew actually finishes? (This is the case’s built-in opening for the twist — don’t tip it.)"),
      h2("Data Deep Dive"),
      p("Step 1 — find the intersection (D1). H = 90, R = 130, H ∪ R = 195. By inclusion-exclusion: |H ∩ R| = |H| + |R| − |H ∪ R| = 90 + 130 − 195 = 25. H-only = 65, R-only = 105, both = 25."),
      p("Step 2 — total inspector-minutes per configuration (D2). The Combined Lane: 90 hazmat checks × 8 min = 720; 130 reefer checks × 7 min = 910; total 1,630 min = 27.17 inspector-hours. The Split Lanes: 90 hazmat checks × 6 min = 540; 130 reefer checks × 5 min = 650; 25 re-handles × 11 min = 275; total 1,465 min = 24.42 inspector-hours."),
      p("Step 3 — containers cleared per inspector-hour (D3). Both configurations clear the same 195 distinct containers (the union — do not let anyone add 90 + 130 = 220 here; that double-counts the 25 in both sets). The Combined Lane: 195 ÷ 27.17 = 7.18/inspector-hour. The Split Lanes: 195 ÷ 24.42 = 7.99/inspector-hour. The Split Lanes wins by 11.26% — comfortably inside the 20% balance cap."),
      p("Push the room directly: “Only 25 of 195 containers are dual-flagged. Why does that 13% slice decide the whole comparison?” Answer, if nobody gets there: those 25 containers are the only place the two configurations’ cost structures actually differ in kind — Combined Lane pays a small per-container speed tax on all 195 containers, Split Lanes pays a chunky one-time re-handle tax on just the 25. Whichever tax adds up to more, wins."),

      h1("Twist — drop this at approximately 15:00"),
      p("Deliver it slowly. Let each piece land. “It’s 11:15pm. Compliance calls.” (pause) “New bulletin, effective tonight: refrigerated shipments of lithium-ion cells now require hazmat placarding too — not just a reefer flag.” (pause) “Your crew re-checks the reefer set. Thirty of those containers are lithium-ion cell shipments. They’re hazmat-flagged now.”"),
      p("Facilitator only — read before you drop this, do not read aloud: Those 30 containers were already inside R (reefer-flagged); they now also join H. Because they were already counted in the union, the union stays at 195 — but H rises from 90 to 120, and by inclusion-exclusion the intersection jumps from 25 to 55. Re-run Step 2 and Step 3: Combined Lane total becomes 8(120)+7(130) = 1,870 min = 31.17 hours, rate 195/31.17 = 6.26. Split Lanes total becomes 6(120)+5(130)+11(55) = 1,975 min = 32.92 hours, rate 195/32.92 = 5.92. The Combined Lane now wins, by 5.61% — the winner flips. This is a real, computable flip driven entirely by the intersection growing past its crossover point (x = 40, for tonight’s H+R), not a vaguely-worded “things changed” twist.", { italics: true }),
      p("Then: “Sixty seconds. Are you changing your lane assignment — or not?”"),

      h2("Immediate recommit"),
      p("Who is not changing? Why? Who is reconsidering, even if they’re not flipping? What just broke in your original model? Were you wrong — or were you just missing information? (Sit on this one.) Who built their case entirely on “specialists are always faster” without ever checking how the intersection was sized?"),

      h1("Deep Conflict — Threads (20–30 min)"),
      p("Thread 1 — Specialization vs. the hidden double cost. The Split Lanes’ crews are faster at every individual check, and still lose once the intersection is large enough. “If specialists are faster at everything, why does the combined lane ever win?” Push toward: the intersection is checked and moved under Split Lanes, but only checked once under Combined — specialization only pays off on the containers that never cross between lanes."),
      p("Thread 2 — Fragility to a single number. Every one of the five per-container timing figures (Appendix D) is a disclosed assumption with no real public source behind it. Flex any single one by 50% in either direction, and the winner either flips or the margin blows past the 20% balance cap (see the sensitivity note below — do not read it aloud, use it to steer questions). “Which lane would you commit to if you had to defend it to a terminal manager who might ask ‘what if the reefer check actually takes six minutes, not five?’”"),

      h1("Five Socratic Questions"),
      p("1. Only 25 of 195 containers are dual-flagged (about 13%) — why does that small slice decide the whole comparison instead of being a minor detail?"),
      p("2. If we end up with two rates like 7.18 and 7.99, how close is “close” before you’d call this a real toss-up rather than one lane clearly winning?"),
      p("3. None of the five per-container check times (Appendix D) come from a published source for this exact terminal check — which single one, if it moved by a few minutes, would worry you the most, and why?"),
      p("4. If the intersection had been the empty set instead of 25, would the two configurations’ rates differ at all? Use what a no-overlap Venn diagram actually shows about each container’s inspection path."),
      p("5. The Split Lanes wins tonight by 11.26% — but every one of the five timing assumptions flips the winner or breaches the 20% cap at a ±50% swing. Is an 11.26% margin built on assumptions this shaky a “real” win?"),

      h1("Sensitivity Note (boxed — read before Lessons Learned)"),
      p("Base margin (11.26%) is a direct, computable function of all five timing assumptions (MA2–MA6) via sensitivity_model.py. Every one of the five timing assumptions flips the winner or breaches the SPEC §2 20% cap at a ±50% flex: t_hazmat_combined (+50% → 35.84%, B wins wider; −50% → flips to A at 15.35%); t_reefer_combined (+50% → 42.32%; −50% → flips to A and breaches the cap at 24.68% — the single most load-bearing assumption); t_hazmat_split (+50% → flips to A at 6.44%; −50% → breaches the cap at 36.40%); t_reefer_split (+50% → flips to A at 9.82%; −50% → breaches the cap at 42.98%); t_rehandle (−50% → breaches the cap at 22.79% without flipping; +50% → narrows the margin sharply to 1.72% without flipping — this is the assumption the twist deliberately does NOT flex directly; the twist instead changes the intersection size, a structurally different and more decisive lever). H, R, and the union are deliberately excluded from this flex sweep — see sensitivity_model.py’s docstring. No SPEC §6 subject-matter sensitivity applies; this is an operations/compliance decision with no death, illness, or family-hardship stakes."),

      h1("What a Strong Defense Sounds Like"),
      p("Not an answer key — a Hero defending either lane well will: name the actual metric (containers cleared per inspector-hour, not raw check speed) and why it’s the fair comparison; show the inclusion-exclusion arithmetic for the intersection rather than eyeballing it off the diagram; name which timing assumption their answer is most sensitive to; address the twist directly — acknowledging the win is real but fragile — rather than picking a side and ignoring the disclosed uncertainty."),

      h1("Cohort Bands"),
      table(["Band", "What changes"], [
        ["Full (12-20)", "Socratic plan runs as written. Anchor 1 vote is a real show-of-hands split worth reading; both deep-conflict threads run."],
        ["Compressed (6-11)", "Combine Anchor 2 and Anchor 3 into one pass. Run only the sharper deep-conflict thread (fragility to a single assumption) at 20:00-30:00. Twist still drops at 15:00. Total runtime ~30 min."],
        ["1:1 or pair (1-2)", "No vote at Anchor 1 — the learner states an initial position instead. The guide argues the other side directly rather than cold-calling. The twist still lands; ‘who reverses’ becomes ‘would you reverse, and why’. Skip the deep-conflict threads; go straight from twist-recommit to Close."],
      ], [2600, 6400]),

      h1("45-Minute Socratic Plan"),
      table(["Time", "Move"], [
        ["0:00-3:00", "Cold-call launch. “Thirty seconds — Combined or Split?” Two or three learners, fast. Stand/sit vote, no explanation yet."],
        ["3:00-10:00", "Position defense (pre-twist). “Convince us it’s better, not just louder.” · “How many containers does your lane clear per inspector-hour — the actual rate, not a guess.”"],
        ["10:00-15:00", "Pressure-test the models. “Which lane is more fragile to one wrong timing assumption?” · “What single number does your lane depend on most?”"],
        ["15:00", "DROP THE TWIST. Slowly, with pauses. Finish with: “Sixty seconds. Are you changing your lane — or not?”"],
        ["15:00-20:00", "Immediate recommit. Who reverses? “What just broke?”"],
        ["20:00-30:00", "The two threads: specialization vs. the hidden double cost · fragility to a single assumption."],
        ["30:00-45:00", "Close, re-vote, reflection, lessons learned."],
      ], [1800, 7200]),

      h1("Close"),
      p("Vote again. Compare to the Anchor 1 board. Who moved? We asked ______ as our key question — was it the right one? What math was new to you here, and how did you attack it? If you got a case like this again, what would you check first?"),

      h1("Lessons Learned"),
      p("The arithmetic has a clean structure: a union tells you how many distinct things you actually have, and an intersection tells you exactly where two competing plans’ cost structures genuinely differ. The Split Lanes’ win (11.26%) is real on tonight’s numbers, and it is also fragile — every one of the five timing assumptions behind it flips the winner or breaches the SPEC balance cap at a plausible ±50% swing, and a small, realistic reclassification (30 containers, out of 195) is enough to flip it for real. That is a disclosed, not eliminated, sensitivity."),
      p("A facilitator running this room should say plainly what the case says: The Split Lanes wins on the numbers as modeled, that win is real, and it is also genuinely fragile to several disclosed assumptions and to a realistic reclassification — both things are true at once, and naming both is stronger than picking one."),

      h1("Skills This Case Exercises"),
      p("Set · Subset · Union · Intersection · Empty Set · Venn Diagram · How to find the union and intersection of two sets · How to represent a set relationship using a Venn diagram — name these explicitly in debrief so learners connect tonight’s decision back to the vocabulary from Appendix F."),
    ],
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("The Manifest Split - Facilitator Guide.docx", buf);
  console.log("wrote docx", buf.length, "bytes");
});
