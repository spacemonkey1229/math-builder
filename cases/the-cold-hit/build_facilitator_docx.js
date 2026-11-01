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
      new Paragraph({ children: [new TextRun({ text: "Facilitator Guide: The Cold Hit", bold: true, size: 40, color: NAVY })], spacing: { after: 80 } }),
      p("FACILITATOR ONLY — contains the balance argument, the margin, and the trap. Do not distribute to Heroes.", { bold: true, color: "a3312a" }),
      p("Case: The Cold Hit  ·  Tier: T3 (MS-stretch / HS-entry)  ·  Studio: Adventure  ·  Primary metric: cold-hit cases closed per detective-and-lab hour  ·  Base margin: 10.26% (fragile — see the sensitivity note before Lessons Learned)"),
      p("Standards: Independent Event, Permutation, Multistage Sampling, Convenience Sampling, Conditional Probability, Population, Sample, Random, How to determine the number of outcomes of a permutation, How to determine the number of outcomes of a combination, How to determine the probability of conditional events, How to determine the probability of a compound event, How to find the percent of a number (see case.json.standards[])."),

      // Boxed SPEC Section 6 sensitivity note, at the top per skill 1c
      new Table({
        width: { size: 9000, type: WidthType.DXA },
        columnWidths: [9000],
        rows: [new TableRow({ children: [new TableCell({
          width: { size: 9000, type: WidthType.DXA },
          shading: { type: ShadingType.CLEAR, color: "auto", fill: "FBEAEA" },
          children: [
            new Paragraph({ children: [new TextRun({ text: "SPEC Section 6 flag — read before you run this room", bold: true, color: "a3312a" })], spacing: { after: 60 } }),
            new Paragraph({ children: [new TextRun({ text: "This case touches wrongful accusation. Not a death/illness/family-hardship stake, but real enough to name at the top of the room: “the math here is really a question about what happens to someone who didn't do it.” Framed as protection (avoiding a wrongful referral), not punishment, per SPEC Section 6's protection-over-destruction guidance." })] }),
          ],
        })] })],
      }),
      p(""),

      h1("The Balance Argument (Answer Key — Facilitator Only)"),
      p("Argument for A (Refer on Match): Refer on Match wins on this year's actual numbers (10.26% margin) because the expected number of coincidental (false) referrals is still low even for partial-profile hits — fewer than one expected per year — so paying a corroboration cost on every single one of this year's 60 cases costs more total hours than absorbing the rare, expensive rework cost only when a false referral actually happens."),
      p("Argument for B (Hold for Corroboration): Hold for Corroboration wins if the caseload shifts toward more degraded, harder-to-resolve evidence — and a real, disclosed scenario (the twist) shows that threshold is not hypothetical: a grant-funded initiative that specifically clears the most degraded backlog first raises the partial-profile share from 60% to 100%, which is enough to flip the winner, because Policy A's cost scales with the (now higher) expected false-referral count while Policy B's cost per case never changes."),
      p("Margin at this year's base numbers: 10.26%, Refer on Match (A) wins.", { bold: true }),
      p("The Trap: most learners will assume that because a coincidental DNA match sounds astronomically unlikely, Policy A (refer immediately) is obviously fine and Policy B's extra step is pure overhead with no real benefit. The real trap is that this specific hit came from a partial, 8-locus profile — not a full 20-locus one — and the database searched has millions of records in it. A learner who does D1 correctly but skips D2 (the database-size correction) will badly underestimate how often a coincidental match like this one is expected to occur, and will not understand why the case is close at all."),

      h1("Facilitator Notes"),
      h2("Intro"),
      p("Heroes, Dana has one memo to write and a supervisor waiting on it. One policy is fast for everyone. The other costs everyone a little time, every time, on purpose. There's no answer I'm holding back from you — the DA's office doesn't have one either until they see Dana's numbers."),
      h2("Launch"),
      p("Show a simple diagram: a cold-case DNA sample going into a search, and coming out the other side with just a name and a number. Ask: “If all you had was that — a name and a probability — would you send someone to trial on it? What would you want to know first?” Let them argue it cold. Then: “Dana's unit reviews a hit like this roughly once a week. She has to pick ONE policy for the whole year — not case by case.” Hero name — Refer on Match, or Hold for Corroboration? Commit out loud."),
      h2("Anchor 1 — Take a stand and vote"),
      p("Refer on Match (A) or Hold for Corroboration (B). No reasoning yet. Hands up for A. Hands up for B. Write the split on the board. “Is anyone courageous enough to stand with ______?”"),
      h2("Anchor 2 — What is the problem we're solving?"),
      p("Do not let them start calculating yet. What's the actual question, in one sentence? Is it “which policy is fair to the defendant”? Is it “which policy never lets a guilty person go”? Is it “which policy closes the most cases correctly per hour of investigator time”? Those sound similar and are not the same question — only the last one is what this case's numbers actually measure. Someone will say “obviously hold for corroboration, you can never be too careful.” Push: “Careful costs hours. Every hour spent double-checking a hit that was already correct is an hour not spent on the next cold case. Is 'never be too careful' actually free?” Let the confusion grow. Say it out loud: “Huh — 'better safe than sorry' has a cost, and we haven't priced it yet.” Do not rescue them."),
      h2("Anchor 3 — What is the process?"),
      p("What's the process we'll go through to answer it? If we calculate “how unlikely is this exact match,” are we done? Is that the same question as “how likely is at least one coincidental match somewhere in a database this size”? If we end up with two rates like 0.1225 and 0.1111 cases per hour, how do we decide that's close enough to be a real discussion, versus one policy just winning? What's our tiebreaker before we see the numbers? Is our question still the right question?"),
      h2("Anchor 4 — What don't we know?"),
      p("What's missing that we'd need to answer this properly? Appendix F gives you the assumptions behind every non-probability figure — the caseload, the time costs. Do you believe them? Have them actually try a bigger and a smaller version of each and see how much the comparison moves. What are we assuming stays the same about which kinds of cold cases the unit reviews this year? (This is the case's built-in opening for the twist — don't tip it.)"),

      h1("Data Deep Dive"),
      p("Now the numbers. Work these on the board with them."),
      p("Step 1 — RMP for the 8-locus partial profile (D1). Per-locus match probability = 0.075. RMP = 0.075⁸ ≈ 1.001 × 10⁻⁹ (about 1 in 1 billion) — treating each locus as an independent event, so the probabilities multiply."),
      p("Step 2 — database match probability, both search stages (D2)."),
      table(["Stage", "Calculation", "Result"], [
        ["Stage 1 (state, 3,368,310 profiles, no hit)", "DMP = 3,368,310 × 1.001×10⁻⁹", "≈ 0.00337 (about 1 in 297)"],
        ["Stage 2 (national NDIS, 18,000,000 profiles, hit found here)", "DMP = 18,000,000 × 1.001×10⁻⁹", "≈ 0.01802 (about 1 in 55.5)"],
      ], [3800, 3400, 1800]),
      p("Push the room directly: “1 in 55 sounds a lot less impressive than 1 in a billion. Which number is actually the right one to weigh this hit against?” (Answer: the database one — the 1-in-a-billion figure answers “how unlikely is THIS exact profile,” but the hit wasn't produced by comparing one suspect to one profile; it was produced by searching 18 million.)"),
      p("Step 3 — cases closed per hour, both policies (D3)."),
      table(["Policy", "Work", "Hours"], [
        ["A — Refer on Match", "60 cases × 6 h base", "360"],
        ["A — Refer on Match", "0.649 expected false referrals × 200 h rework", "≈130"],
        ["A total", "", "≈489.75 h → rate 0.1225/h"],
        ["B — Hold for Corroboration", "60 cases × 6 h base", "360"],
        ["B — Hold for Corroboration", "60 cases × 3 h corroboration", "180"],
        ["B total", "", "540 h → rate 0.1111/h"],
      ], [3600, 4000, 1400]),
      p("Refer on Match wins by 10.26% — comfortably inside the 20% balance cap, but not by much.", { bold: true }),

      h1("Twist — drop this at ~15 minutes into the discussion"),
      p("Deliver it slowly. Let each piece land."),
      p("“New funding came through this morning.” (pause) “A state grant, specifically for clearing the oldest, most degraded cases in the backlog — the ones everyone's been putting off because the evidence is in the worst shape.” (pause) “Every single cold hit on this year's list is now a partial profile. Not 60% of them. All of them.”", { italics: true }),
      p("Facilitator only — read before you drop this, do not read aloud. frac_partial rises from 0.6 to 1.0. Expected false referrals under Policy A rise from 0.649/year to 1.081/year, raising Policy A's total hours from 489.75 to 576.24 (rate drops to 0.1041/h). Policy B's total (540 h, rate 0.1111/h) is unaffected — corroboration is applied to every case either way. The winner flips to Hold for Corroboration, by 6.71%. Confirm a room that gets there against these numbers, not just the logic.", { italics: true }),
      p("Now: “Sixty seconds. Are you changing your recommendation — or not?”"),

      h2("Immediate recommit"),
      p("Who is not changing? Why? Who is reconsidering, even if they're not flipping? What just broke in your original model? Were you wrong — or were you just missing information? (Sit on this one.) Who built their case entirely on “a coincidental match is basically impossible” without ever running D2's database-size correction?"),

      h1("Deep Conflict — Threads (20–30 min)"),
      p("Thread 1 — The prosecutor's fallacy, made concrete. RMP tells you the probability of the evidence if the person is innocent. It does not tell you the probability the person is innocent. “If someone told a jury '1 in a billion, so there's a 1-in-a-billion chance he's innocent' — what exactly did they get wrong?” Push toward: with an 18-million-profile database searched, the relevant number isn't 1-in-a-billion, it's roughly 1-in-55 for some coincidental hit to occur somewhere in that search — the search itself, not just the profile, changes what the evidence means."),
      p("Thread 2 — Fragility to a single number. Every one of the five caseload/cost figures (Appendix F) is a disclosed assumption with no real public source behind it. Flex h_corrob or h_rework by 50% in either direction, and the winner flips (see case.json's sensitivity_disclosure — do not read this section aloud, but use it to steer questions). “Which policy would you defend to a department head who asks 'what if corroboration actually only takes half the time you assumed?'”"),

      h1("Five Socratic Questions"),
      p("1. If all you had was a name and a probability, would you send someone to trial on it? What would you want to know first?"),
      p("2. “Careful costs hours” — is 'never be too careful' actually free? What's the real cost of Policy B's extra step?"),
      p("3. “1 in 55” sounds a lot less impressive than “1 in a billion.” Which number is actually the right one to weigh this hit against, and why?"),
      p("4. If someone told a jury “1 in a billion, so there's a 1-in-a-billion chance he's innocent,” what exactly did they get wrong?"),
      p("5. Refer on Match wins this year by 10.26% — but several of the underlying assumptions flip the winner or breach the 20% cap at a ±50% swing. Is a 10.26% margin built on assumptions this shaky a “real” win?"),

      h1("Sensitivity Note (boxed — read before Lessons Learned)"),
      p("Base margin (10.26%) is a direct, computable function of all five disclosed Modeling Assumptions (MA1–MA5) via sensitivity_model.py. Per case.json's sensitivity_disclosure[], frac_partial, h_corrob, and h_rework each flip the winner or breach the SPEC §2 20% cap at a ±50% flex — a real, disclosed finding about how tightly this case's margin depends on undisclosed real-world lab-operational data, not a defect introduced by an unscoped sweep. n_hits (MA1) does NOT change the winner or margin at all when flexed ±50% — it scales every term in both policies' totals proportionally, so it cancels out of the ratio; a useful contrast for showing not every assumption is equally load-bearing. h_base (MA3) narrows or widens the margin without ever flipping it, since it applies equally to both policies. The real cited figures (RMP_locus, N_state, N_national) are deliberately excluded from this flex sweep — see sensitivity_model.py's docstring."),

      h1("What a Strong Defense Sounds Like"),
      p("Not an answer key — a Hero defending either policy well will: name the actual metric (cold-hit cases closed per detective-and-lab hour, not raw match improbability) and why it's the fair comparison; show the two-stage database-size correction (D1 into D2) rather than stopping at the RMP alone — a defense that runs the full D1→D2 correction and can explain why 1-in-55 is the number that matters, not 1-in-a-billion, is doing meaningfully stronger reasoning than one that cites only the RMP and calls a coincidental match “basically impossible”; name which cost assumption their answer is most sensitive to; and address the twist directly — acknowledging the win is real but fragile — rather than picking a side and ignoring the disclosed uncertainty."),

      h1("Cohort Bands"),
      table(["Band", "What changes"], [
        ["Full (12-20)", "Socratic plan runs as written. Anchor 1 vote is a real show-of-hands split worth reading; both deep-conflict threads run."],
        ["Compressed (6-11)", "Combine Anchor 2 and Anchor 3 into one pass. Run only the sharper deep-conflict thread (the prosecutor's-fallacy framing) at 20:00-30:00. Twist still drops at 15:00. Total runtime ~30 min."],
        ["1:1 or pair (1-2)", "No vote at Anchor 1 — the learner states an initial position instead. The guide argues the other side directly rather than cold-calling. The twist still lands; 'who reverses' becomes 'would you reverse, and why'. Skip the deep-conflict threads; go straight from twist-recommit to Close."],
      ], [2600, 6400]),

      h1("45-Minute Socratic Plan"),
      table(["Time", "Move"], [
        ["0:00-3:00", "Cold-call launch. “Thirty seconds — refer now, or hold?” Two or three learners, fast. Stand/sit vote, no explanation yet."],
        ["3:00-10:00", "Position defense (pre-twist). “Convince us it's better, not just safer-sounding.” · “What's your actual cases-per-hour rate — not a guess.”"],
        ["10:00-15:00", "Pressure-test the models. “Which policy is more fragile to one wrong time estimate?” · “What single number does your policy depend on most?”"],
        ["15:00", "DROP THE TWIST. Slowly, with pauses. Finish with: “Sixty seconds. Are you changing your recommendation — or not?”"],
        ["15:00-20:00", "Immediate recommit. Who reverses? “What just broke?”"],
        ["20:00-30:00", "The two threads: the prosecutor's fallacy made concrete · fragility to a single assumption."],
        ["30:00-45:00", "Close, re-vote, reflection, lessons learned."],
      ], [1800, 7200]),

      h1("Close"),
      p("Vote again. Compare to the Anchor 1 board. Who moved? We asked ______ as our key question — was it the right one? What math was new to you here, and how did you attack it? If you got a case like this again, what would you check first?"),

      h1("Lessons Learned"),
      p("The arithmetic has a clean structure: an independent-event product tells you how unlikely one exact match is, and a database-size multiplication tells you how likely some coincidental match is across an entire search — those are very different numbers, and the gap between them (1 in a billion versus roughly 1 in 55) is the whole reason this case is close instead of obvious. Refer on Match's win (10.26%) is real on this year's numbers, and it is also fragile — three of the five underlying assumptions flip the winner or breach the SPEC balance cap at a plausible ±50% swing, and a realistic shift in caseload composition (the twist) is enough to flip it for real. That is a disclosed, not eliminated, sensitivity — case.json.sensitivity_disclosure[] carries a Category-F entry for every cost/caseload dial, because none of them can be tightened by more research; they are genuine lab-operational unknowns no public source measures."),
      p("A facilitator running this room should say plainly what the case says: Refer on Match wins on the numbers as modeled, that win is real, and it is also genuinely fragile to several disclosed assumptions and to a realistic caseload shift — both things are true at once, and naming both is stronger than picking one."),

      h1("Real-World Basis (read aloud only after the vote is closed)"),
      p("Dana Osei and her lab are fictional. The numbers problem she's facing is not — it happened, in a real courtroom, with a real conviction on the line."),
      p("In 2008, John Puckett was convicted of a 1972 California murder on a DNA “cold hit” produced by searching the state's database of 338,711 offender profiles. The prosecutor told the jury the match had a 1-in-1.1-million chance of being coincidental — the raw per-profile random match probability. What the jury was never told: once you account for the fact that the match came from searching 338,711 people rather than comparing one suspect to one profile, the odds of a coincidental match turning up somewhere in that search were closer to 1 in 3. That's the exact database-size correction this case makes you compute in D2 — it's not a classroom simplification. It's Recommendation 5.1 of the National Research Council's 1996 DNA forensic science report (the same S6 source behind this case's Appendix C formula), left out of a real trial."),
      p("Puckett's conviction was upheld on appeal. The case remains a standard reference point in the ongoing legal and statistical debate over how — and whether — cold-hit probabilities should be explained to a jury. Tell the room: “The math you just did isn't hypothetical. A jury got the 1-in-1.1-million number and not the 1-in-3 number, and it mattered.”"),
      p("Sources: Cold Case Hits Use Vastly Exaggerated DNA “Match” Statistics (Prison Legal News, https://www.prisonlegalnews.org/news/2009/jan/15/cold-case-hits-use-vastly-exaggerated-dna-match-statistics-8232upheld-by-california-supreme-court/); In DNA Numbers Game, Statistics Could Lead to False Convictions (The Crime Report, https://thecrimereport.org/2008/05/08/in-dna-numbers-game-statistics-could-lead-to-false-convictions/); Roth, “Safety in Numbers? Deciding When DNA Alone Is Enough to Convict” (2010, https://www.marcellodibello.com/mathtrial/resources/RothDNA2010.pdf).", { italics: true, size: 20 }),

      h1("Skills This Case Exercises"),
      p("Independent Event · Permutation · Multistage Sampling · Convenience Sampling · Conditional Probability · Population · Sample · Random · How to determine the number of outcomes of a permutation · How to determine the number of outcomes of a combination · How to determine the probability of conditional events · How to determine the probability of a compound event · How to find the percent of a number — name these explicitly in debrief so learners connect today's decision back to the vocabulary from Appendix H."),
    ],
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("The Cold Hit - Facilitator Guide.docx", buf);
  console.log("wrote docx", buf.length, "bytes");
});
