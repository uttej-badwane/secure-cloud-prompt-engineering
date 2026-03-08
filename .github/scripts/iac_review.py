#!/usr/bin/env python3
"""
IaC Security Review — GitHub Actions script
Calls Claude to review changed IaC files in a PR and outputs a formatted report.

Environment variables:
  ANTHROPIC_API_KEY     Required. Your Anthropic API key.
  CHANGED_FILES         Space-separated list of changed IaC files to review.
  COMPLIANCE_FRAMEWORKS Comma-separated list of frameworks (default: cis,nist).
  BLOCK_ON_CRITICAL     Set to 'true' to fail the job on CRITICAL findings.
  GITHUB_OUTPUT         Set by GitHub Actions runner for output variables.
"""

import os
import sys
import json
import pathlib

try:
    import anthropic
except ImportError:
    print("Error: 'anthropic' package not installed. Run: pip install anthropic", file=sys.stderr)
    sys.exit(1)

SEVERITY_EMOJI = {
    "CRITICAL": "🔴",
    "HIGH": "🟠",
    "MEDIUM": "🟡",
    "LOW": "🔵",
    "INFO": "ℹ️",
}

FRAMEWORK_LABELS = {
    "cis": "CIS Benchmarks",
    "nist": "NIST 800-53",
    "nist-171": "NIST 800-171",
    "pci": "PCI-DSS",
    "soc2": "SOC 2",
    "hipaa": "HIPAA",
    "gdpr": "GDPR",
    "iso27001": "ISO 27001",
}


def read_files(file_list: list[str]) -> dict[str, str]:
    """Read file contents, skipping files that are too large or unreadable."""
    contents = {}
    for path in file_list:
        p = pathlib.Path(path)
        if not p.exists():
            continue
        if p.stat().st_size > 100_000:  # skip files > 100KB
            contents[path] = f"[Skipped — file too large ({p.stat().st_size} bytes)]"
            continue
        try:
            contents[path] = p.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            contents[path] = f"[Could not read: {e}]"
    return contents


def build_prompt(file_contents: dict[str, str], frameworks: list[str]) -> str:
    framework_str = ", ".join(FRAMEWORK_LABELS.get(f, f.upper()) for f in frameworks)

    files_block = ""
    for path, content in file_contents.items():
        files_block += f"\n### File: `{path}`\n```\n{content}\n```\n"

    return f"""You are an expert IaC security reviewer. Review the following Infrastructure as Code
files that were changed in a pull request. Identify security misconfigurations, compliance gaps,
and hardening opportunities.

## Compliance Frameworks
Map all findings to: {framework_str}

## Files to Review
{files_block}

## Output Format

Respond with a JSON object following this exact schema:
{{
  "summary": {{
    "critical": <int>,
    "high": <int>,
    "medium": <int>,
    "low": <int>,
    "info": <int>,
    "overall_risk": "<CRITICAL|HIGH|MEDIUM|LOW|PASS>"
  }},
  "findings": [
    {{
      "severity": "<CRITICAL|HIGH|MEDIUM|LOW|INFO>",
      "title": "<short title>",
      "file": "<path>",
      "line": <int or null>,
      "description": "<what is wrong>",
      "risk": "<what an attacker could do>",
      "compliance": {{
        "cis": "<section or null>",
        "nist": "<control IDs or null>",
        "pci_dss": "<requirement or null>",
        "hipaa": "<safeguard or null>",
        "soc2": "<criteria or null>"
      }},
      "remediation": "<working code snippet or config change>",
      "reference": "<URL or null>"
    }}
  ],
  "positive_findings": ["<string>"],
  "next_steps": ["<string>"]
}}

Rules:
- Only report genuine security findings — do not pad with low-value observations
- Provide working remediation code for every finding
- Cite exact file paths and line numbers where possible
- Acknowledge positive security controls in positive_findings
- Order findings by severity (CRITICAL first)
"""


def format_markdown_report(data: dict, frameworks: list[str], changed_files: list[str]) -> str:
    s = data.get("summary", {})
    findings = data.get("findings", [])
    positives = data.get("positive_findings", [])
    next_steps = data.get("next_steps", [])
    overall = s.get("overall_risk", "UNKNOWN")

    risk_emoji = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🔵", "PASS": "✅"}.get(overall, "⚪")

    lines = [
        "## IaC Security Review",
        "",
        f"**Risk Rating:** {risk_emoji} {overall}  ",
        f"**Files reviewed:** {len(changed_files)}  ",
        f"**Frameworks:** {', '.join(FRAMEWORK_LABELS.get(f, f.upper()) for f in frameworks)}",
        "",
        "| 🔴 Critical | 🟠 High | 🟡 Medium | 🔵 Low | ℹ️ Info |",
        "|---|---|---|---|---|",
        f"| {s.get('critical', 0)} | {s.get('high', 0)} | {s.get('medium', 0)} | {s.get('low', 0)} | {s.get('info', 0)} |",
        "",
    ]

    if findings:
        lines.append("---")
        lines.append("")
        lines.append("## Findings")
        lines.append("")
        for i, f in enumerate(findings, 1):
            sev = f.get("severity", "INFO")
            emoji = SEVERITY_EMOJI.get(sev, "⚪")
            file_ref = f.get("file", "")
            line_ref = f.get("line")
            loc = f"`{file_ref}:{line_ref}`" if line_ref else f"`{file_ref}`"

            lines.append(f"### {emoji} {sev} #{i} — {f.get('title', 'Untitled')}")
            lines.append("")
            lines.append(f"- **Location:** {loc}")
            lines.append(f"- **Issue:** {f.get('description', '')}")
            lines.append(f"- **Risk:** {f.get('risk', '')}")

            compliance = f.get("compliance", {})
            mapped = [f"{k.upper()}: {v}" for k, v in compliance.items() if v]
            if mapped:
                lines.append(f"- **Compliance:** {' | '.join(mapped)}")

            remediation = f.get("remediation", "")
            if remediation:
                lines.append("")
                lines.append("<details><summary>Remediation</summary>")
                lines.append("")
                lines.append("```")
                lines.append(remediation)
                lines.append("```")
                lines.append("")
                lines.append("</details>")

            ref = f.get("reference")
            if ref:
                lines.append(f"- **Reference:** [{ref}]({ref})")

            lines.append("")

    if positives:
        lines.append("---")
        lines.append("")
        lines.append("## Positive Findings")
        lines.append("")
        for p in positives:
            lines.append(f"- ✅ {p}")
        lines.append("")

    if next_steps:
        lines.append("---")
        lines.append("")
        lines.append("## Recommended Next Steps")
        lines.append("")
        for i, step in enumerate(next_steps, 1):
            lines.append(f"{i}. {step}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        "*Powered by [IaC Security Review for Claude Code](https://github.com/uttej-badwane/secure-cloud-prompt-engineering) "
        "— [Get Pro](https://github.com/marketplace/iac-security-review)*"
    )

    return "\n".join(lines)


def write_output(key: str, value: str) -> None:
    """Write a key=value pair to $GITHUB_OUTPUT (multiline-safe)."""
    github_output = os.environ.get("GITHUB_OUTPUT")
    if not github_output:
        print(f"OUTPUT {key}={value[:200]}...")
        return
    with open(github_output, "a") as f:
        delimiter = "EOF_REPORT"
        f.write(f"{key}<<{delimiter}\n{value}\n{delimiter}\n")


def main() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY is not set.", file=sys.stderr)
        sys.exit(1)

    changed_files_str = os.environ.get("CHANGED_FILES", "").strip()
    if not changed_files_str:
        print("No IaC files to review.")
        return

    changed_files = [f for f in changed_files_str.split() if f]
    frameworks_str = os.environ.get("COMPLIANCE_FRAMEWORKS", "cis,nist")
    frameworks = [f.strip().lower() for f in frameworks_str.split(",") if f.strip()]

    print(f"Reviewing {len(changed_files)} IaC file(s) against {frameworks}...")

    file_contents = read_files(changed_files)
    if not file_contents:
        print("No readable IaC files found.")
        return

    client = anthropic.Anthropic(api_key=api_key)
    prompt = build_prompt(file_contents, frameworks)

    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )
    except anthropic.APIError as e:
        print(f"Claude API error: {e}", file=sys.stderr)
        sys.exit(1)

    response_text = message.content[0].text.strip()

    # Parse JSON from response (Claude may wrap it in a code block)
    if "```json" in response_text:
        response_text = response_text.split("```json")[1].split("```")[0].strip()
    elif "```" in response_text:
        response_text = response_text.split("```")[1].split("```")[0].strip()

    try:
        review_data = json.loads(response_text)
    except json.JSONDecodeError as e:
        print(f"Failed to parse Claude response as JSON: {e}", file=sys.stderr)
        print(f"Response: {response_text[:500]}", file=sys.stderr)
        sys.exit(1)

    report = format_markdown_report(review_data, frameworks, changed_files)
    critical_count = review_data.get("summary", {}).get("critical", 0)

    write_output("report", report)
    write_output("critical_count", str(critical_count))

    print(f"Review complete. Critical: {critical_count}, Overall risk: {review_data.get('summary', {}).get('overall_risk', 'UNKNOWN')}")


if __name__ == "__main__":
    main()
