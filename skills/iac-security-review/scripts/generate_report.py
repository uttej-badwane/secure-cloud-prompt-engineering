#!/usr/bin/env python3
"""IaC Security Review Report Generator

Generates structured security review report templates for Infrastructure as Code.
Called by Claude as part of the iac-security-review skill workflow (Step 4).

Usage:
    python3 generate_report.py --format markdown --scope "terraform/" --output /tmp/report.md
    python3 generate_report.py --format json --scope "." --output /tmp/report.json
    python3 generate_report.py --format markdown --scope "test"   # stdout
"""

import argparse
import json
import sys
from datetime import date

MARKDOWN_TEMPLATE = """\
# IaC Security Review Report

**Date:** {date}
**Scope:** {scope}
**Reviewer:** Claude IaC Security Review Skill
**Author:** Uttej Badwane (github.com/uttej-badwane)

---

## Executive Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| HIGH     | 0 |
| MEDIUM   | 0 |
| LOW      | 0 |
| INFO     | 0 |

**Overall Risk Rating:** <!-- CRITICAL / HIGH / MEDIUM / LOW / INFORMATIONAL -->

---

## Findings

<!-- One section per finding, ordered by severity -->

### [SEVERITY] Finding #1: [Title]

- **File:** [path:line]
- **Description:** [what is wrong]
- **Risk:** [impact if exploited]
- **Compliance:** [framework controls violated]
- **Remediation:** [specific fix with code example]
- **Reference:** [link to CIS/NIST/vendor doc]

---

## Compliance Summary Table

| Framework    | Status          | Notes |
|--------------|-----------------|-------|
| CIS          | Not assessed    |       |
| NIST 800-53  | Not assessed    |       |
| NIST 800-171 | Not assessed    |       |
| PCI-DSS      | Not assessed    |       |
| SOC 2        | Not assessed    |       |
| HIPAA        | Not assessed    |       |
| GDPR         | Not assessed    |       |
| ISO 27001    | Not assessed    |       |

---

## Positive Findings

<!-- Acknowledge good practices found during the review -->

---

## Recommended Next Steps

<!-- Prioritized action items -->

1. (CRITICAL/HIGH) ...
2. (MEDIUM) ...
3. (LOW) ...
"""

JSON_SCHEMA = {
    "report": {
        "date": None,
        "scope": None,
        "reviewer": "Claude IaC Security Review Skill",
        "author": "Uttej Badwane (github.com/uttej-badwane)",
    },
    "summary": {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
        "info": 0,
        "overall_risk": "UNKNOWN",
    },
    "findings": [
        # {
        #   "severity": "HIGH",
        #   "id": 1,
        #   "title": "...",
        #   "file": "path:line",
        #   "description": "...",
        #   "risk": "...",
        #   "compliance": ["NIST AC-6", "CIS 1.x"],
        #   "remediation": "...",
        #   "reference": "https://..."
        # }
    ],
    "compliance": {
        "CIS": "not_assessed",
        "NIST 800-53": "not_assessed",
        "NIST 800-171": "not_assessed",
        "PCI-DSS": "not_assessed",
        "SOC 2": "not_assessed",
        "HIPAA": "not_assessed",
        "GDPR": "not_assessed",
        "ISO 27001": "not_assessed",
    },
    "positive_findings": [],
    "next_steps": [],
}


def generate_markdown(scope: str) -> str:
    return MARKDOWN_TEMPLATE.format(date=date.today().isoformat(), scope=scope)


def generate_json(scope: str) -> str:
    report = {
        **JSON_SCHEMA,
        "report": {
            **JSON_SCHEMA["report"],
            "date": date.today().isoformat(),
            "scope": scope,
        },
    }
    return json.dumps(report, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate an IaC Security Review report template.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Output format (default: markdown)",
    )
    parser.add_argument(
        "--scope",
        default=".",
        help="Files or directory being reviewed (default: current directory)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output file path. Omit to print to stdout.",
    )
    args = parser.parse_args()

    content = generate_json(args.scope) if args.format == "json" else generate_markdown(args.scope)

    if args.output:
        with open(args.output, "w") as fh:
            fh.write(content)
        print(f"Report written to {args.output}", file=sys.stderr)
    else:
        print(content)


if __name__ == "__main__":
    main()
