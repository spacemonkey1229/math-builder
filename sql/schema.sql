-- Math Builder admin — Neon Postgres schema.
--
-- Mirrors the three readmodel/*.json files the admin app actually writes
-- (roster.json, submissions.json, score_overrides.json) plus demoted_criteria.json,
-- which guide_confirm.py --audit can also write. Every other readmodel/*.json file
-- (cases_index, curriculum_tree, domains, ...) is build-time content and ships as
-- static read-only files in the deployment, not as tables here.
--
-- See DECISIONS.md for why this exists and app/store_postgres.py for how these
-- rows round-trip through the same JSON document shapes app/admin_core.py already
-- operates on.
--
-- No FK constraints: matches the source JSON files, where every "FK" (learner_id,
-- case_id, assignment_id, score_id, ...) is a documented convention enforced by
-- admin_core.py's do_* functions, never by a database. This also avoids an
-- ordering hazard -- app/store_postgres.py's save() does a full DELETE+INSERT per
-- table, and do_delete_learner() saves roster.json (deletes the learner row) and
-- submissions.json (deletes their assignments/etc.) as two separate calls, so a
-- real FK from assignments.learner_id -> learners.id would reject the first save.

CREATE TABLE IF NOT EXISTS programs (
  id              text PRIMARY KEY,
  badges          int  NOT NULL,
  cases_per_badge int  NOT NULL,
  cases_required  int  NOT NULL,
  badge_names     jsonb  -- array of strings, length == badges; badge_names[i] names badge_index i. Nullable: falls back to numeric display.
);

-- CREATE TABLE IF NOT EXISTS above is a no-op against an already-existing programs
-- table, and programs is seeded once, never rewritten by the app itself (see
-- store_postgres.py) -- a plain ALTER is the only thing that reaches an
-- already-deployed database. Same pattern used below for learners.self_assessment.
ALTER TABLE programs ADD COLUMN IF NOT EXISTS badge_names jsonb;

CREATE TABLE IF NOT EXISTS learners (
  id               text PRIMARY KEY,
  display_name     text NOT NULL,
  program          text NOT NULL,  -- logical FK -> programs.id
  cohort           text,
  status           text NOT NULL CHECK (status IN ('active','paused','alumni')),
  started_on       date NOT NULL,
  badges_earned    jsonb NOT NULL DEFAULT '[]',
  drive_folder_id  text,
  drive_folder_url text,
  notes            text NOT NULL DEFAULT '',
  self_assessment  jsonb  -- {interests[], note, captured_on, captured_by, reviewed_by_guide, reviewed_on, reviewed_by}; null until a guide records one. See app/admin_core.py's do_set_self_assessment.
);

-- CREATE TABLE IF NOT EXISTS above is a no-op against an already-existing
-- learners table, so a column added after the table's first deploy (like
-- self_assessment, added 2026-08-12) needs its own idempotent statement here.
ALTER TABLE learners ADD COLUMN IF NOT EXISTS self_assessment jsonb;

-- goals: free-text captured at add-learner time (distinct from self_assessment's
-- structured interests[], which is a separate guide-mediated conversation).
-- passcode: the student's own login code for the live student portal -- see
-- app/admin_web/app.py's /student-login. Generated once at add-learner time
-- (admin_core._gen_passcode), never derived from anything guessable.
ALTER TABLE learners ADD COLUMN IF NOT EXISTS goals text NOT NULL DEFAULT '';
ALTER TABLE learners ADD COLUMN IF NOT EXISTS passcode text;

CREATE TABLE IF NOT EXISTS assignments (
  id           text PRIMARY KEY,
  learner_id   text NOT NULL,  -- logical FK -> learners.id
  case_id      text NOT NULL,
  assigned_on  date NOT NULL,
  due_on       date,
  assigned_by  text,
  badge_index  int,
  status       text NOT NULL CHECK (status IN ('assigned','submitted','reviewed','complete','withdrawn')),
  notes        text
);
CREATE INDEX IF NOT EXISTS assignments_learner_idx ON assignments(learner_id);

CREATE TABLE IF NOT EXISTS submissions (
  id              text PRIMARY KEY,
  assignment_id   text NOT NULL,  -- logical FK -> assignments.id
  learner_id      text NOT NULL,
  case_id         text NOT NULL,
  submitted_on    date NOT NULL,
  artifacts       jsonb NOT NULL,
  source          text NOT NULL,
  drive_artifacts jsonb,
  reviewed_on     date,
  reviewed_by     text,
  review_note     text,
  outcome         text CHECK (outcome IN ('accepted','revise','not-accepted'))
);
CREATE INDEX IF NOT EXISTS submissions_assignment_idx ON submissions(assignment_id);
CREATE INDEX IF NOT EXISTS submissions_learner_case_idx ON submissions(learner_id, case_id);

CREATE TABLE IF NOT EXISTS discussions (
  id           text PRIMARY KEY,
  learner_id   text NOT NULL,
  case_id      text NOT NULL,
  date         date NOT NULL,
  mode         text NOT NULL CHECK (mode IN ('live','written-500')),
  recorded_by  text,
  note         text
);
CREATE INDEX IF NOT EXISTS discussions_learner_case_idx ON discussions(learner_id, case_id);

CREATE TABLE IF NOT EXISTS ratings (
  id         text PRIMARY KEY,
  learner_id text NOT NULL,
  case_id    text NOT NULL,
  stars      int  NOT NULL CHECK (stars BETWEEN 1 AND 5),
  note       text,
  rated_on   date NOT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS ratings_learner_case_uq ON ratings(learner_id, case_id);
CREATE INDEX IF NOT EXISTS ratings_case_idx ON ratings(case_id);

CREATE TABLE IF NOT EXISTS scores (
  id             text PRIMARY KEY,
  learner_id     text NOT NULL,
  case_id        text NOT NULL,
  scored_on      date NOT NULL,
  status         text NOT NULL CHECK (status IN ('machine-first-pass','confirmed')),
  criteria       jsonb NOT NULL,
  badge_eligible boolean NOT NULL,
  growth_score   numeric NOT NULL,
  surface_first  jsonb NOT NULL DEFAULT '[]',
  confirmed_by   text,
  confirmed_on   date,
  overrides      jsonb NOT NULL DEFAULT '[]',
  report         text
);
CREATE INDEX IF NOT EXISTS scores_learner_case_idx ON scores(learner_id, case_id);

CREATE TABLE IF NOT EXISTS score_overrides (
  id                 text PRIMARY KEY,
  learner_id         text NOT NULL,
  case_id            text NOT NULL,
  score_id           text NOT NULL,
  criterion          text NOT NULL,
  machine_level      text NOT NULL,
  guide_level        text NOT NULL,
  "from"             text NOT NULL,
  "to"               text NOT NULL,
  machine_confidence text,
  reason             text NOT NULL,
  by                 text NOT NULL,
  on_date            date NOT NULL
);

-- demoted_criteria.json is a single small document (criterion -> audit stats),
-- not a collection -- one singleton row holding the whole doc as JSONB.
CREATE TABLE IF NOT EXISTS demoted_criteria_doc (
  id  int PRIMARY KEY DEFAULT 1 CHECK (id = 1),
  doc jsonb NOT NULL
);

-- Replaces student_work/<learner>/<case>/submitted/<file> on local disk. Files in
-- this project are small text docs (pitch write-ups, SCORE.md reports), so bytes
-- live directly in Postgres -- no Vercel Blob or second storage service needed.
CREATE TABLE IF NOT EXISTS submitted_files (
  path         text PRIMARY KEY,
  learner_id   text NOT NULL,
  case_id      text NOT NULL,
  content      bytea NOT NULL,
  content_type text,
  uploaded_on  timestamptz NOT NULL DEFAULT now()
);

-- A separate, deliberately simpler lane for live weekly-class sessions: one
-- shared link per case, a walk-up student types their name and submits an
-- answer, no pre-registered learner/passcode and none of the C1-C7
-- independent-study rubric in submissions/scores above -- that machinery is
-- for a self-directed multi-week research capstone, not a 45-60 min
-- facilitated case discussion with a small live group. photo_path, when set,
-- points at a row in submitted_files (case_id-scoped path under class_work/).
CREATE TABLE IF NOT EXISTS class_submissions (
  id            text PRIMARY KEY,
  case_id       text NOT NULL,
  group_label   text NOT NULL,
  student_name  text NOT NULL,
  answer_text   text,
  photo_path    text,
  submitted_on  timestamptz NOT NULL DEFAULT now(),
  reviewed_on   timestamptz,
  reviewed_by   text,
  review_note   text
);
CREATE INDEX IF NOT EXISTS class_submissions_case_idx ON class_submissions(case_id);
