---
name: generate-report
description: Generate a structured security review report in markdown or JSON format
---

Generate a formatted security report from an existing review or by running a fresh scan.

## Steps

1. Check if a review has already been performed in this session. If yes, use those findings.
   If no prior review exists, run `/iac-security-review` first.

2. Determine output format from argument:
   - `markdown` (default) — human-readable report with tables and code blocks
   - `json` — machine-readable format for ticketing system integration

3. Run the report generator:

```bash
python3 skills/iac-security-review/scripts/generate_report.py \
  --format <format> \
  --scope <scope> \
  --output <output-file>
```

4. If the script is unavailable, generate the report directly using this structure:

```
# IaC Security Review Report
Date: [date]
Scope: [files reviewed]
Reviewer: Claude IaC Security Review Skill

## Executive Summary
[total counts by severity, overall risk rating: CRITICAL/HIGH/MEDIUM/LOW]

## Findings

### [SEVERITY] #N — [Title]
- File: [path:line]
- Description: [what's wrong]
- Risk: [impact if exploited]
- Compliance: [framework controls violated]
- Remediation: [code snippet]
- Reference: [link]

## Compliance Summary
[framework × control pass/fail matrix]

## Positive Findings
[things done well]

## Recommended Next Steps
[prioritized action items]
```

5. Save the report and tell the user the output file path.

## Usage

```
/generate-report
/generate-report markdown
/generate-report json
/generate-report json --output findings.json
```
