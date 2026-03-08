#!/usr/bin/env node
/**
 * SessionStart hook — prints context to orient Claude at the start of each session.
 * Outputs a summary of the project and any prior session notes.
 */

const fs = require('fs');
const path = require('path');

const projectRoot = path.resolve(__dirname, '..');
const sessionFile = path.join(projectRoot, '.claude-session.json');

function loadSession() {
  if (fs.existsSync(sessionFile)) {
    try {
      return JSON.parse(fs.readFileSync(sessionFile, 'utf8'));
    } catch {
      return null;
    }
  }
  return null;
}

const session = loadSession();

console.log('=== Secure Cloud Prompt Engineering ===');
console.log('Security-focused IaC prompt library + Claude Code skill.');
console.log('');
console.log('Key paths:');
console.log('  skills/iac-security-review/SKILL.md  — IaC security review skill');
console.log('  commands/                             — slash commands');
console.log('  agents/                               — specialized subagents');
console.log('  rules/                                — always-follow guidelines');
console.log('');

if (session) {
  console.log('=== Prior Session Notes ===');
  if (session.lastReviewDate) {
    console.log(`Last review: ${session.lastReviewDate}`);
  }
  if (session.openFindings && session.openFindings.length > 0) {
    console.log(`Open findings from last session (${session.openFindings.length}):`);
    session.openFindings.slice(0, 5).forEach((f, i) => {
      console.log(`  ${i + 1}. [${f.severity}] ${f.title} — ${f.file}`);
    });
    if (session.openFindings.length > 5) {
      console.log(`  ... and ${session.openFindings.length - 5} more`);
    }
  }
  if (session.notes) {
    console.log(`Notes: ${session.notes}`);
  }
  console.log('');
}

console.log('Type /iac-security-review to start a security review.');
