#!/usr/bin/env node
/**
 * SessionStop hook — saves session state (open findings, notes) for the next session.
 * Reads from environment variables set by the skill during the session.
 */

const fs = require('fs');
const path = require('path');

const projectRoot = path.resolve(__dirname, '..');
const sessionFile = path.join(projectRoot, '.claude-session.json');

// Read any session data passed via env vars (set by generate_report.py or the skill)
const openFindingsRaw = process.env.IAC_OPEN_FINDINGS;
const sessionNotes = process.env.IAC_SESSION_NOTES;

const existing = (() => {
  if (fs.existsSync(sessionFile)) {
    try { return JSON.parse(fs.readFileSync(sessionFile, 'utf8')); } catch { return {}; }
  }
  return {};
})();

const session = {
  ...existing,
  lastReviewDate: new Date().toISOString().split('T')[0],
};

if (openFindingsRaw) {
  try {
    session.openFindings = JSON.parse(openFindingsRaw);
  } catch { /* ignore parse errors */ }
}

if (sessionNotes) {
  session.notes = sessionNotes;
}

fs.writeFileSync(sessionFile, JSON.stringify(session, null, 2));
console.log(`Session saved to ${sessionFile}`);
