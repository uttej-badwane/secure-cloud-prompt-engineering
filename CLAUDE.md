# CLAUDE.md — Secure Cloud Prompt Engineering

This file is read automatically by Claude Code. It defines how to work with this project.

## Project Purpose

This repository is a **security-focused prompt and skill library** for AI-assisted Infrastructure as Code (IaC) development. It provides:

- A Claude Code skill (`skills/iac-security-review/`) for automated IaC security reviews
- 33+ markdown prompt files covering Terraform, Kubernetes, Docker, AWS, CI/CD, and more
- Compliance mappings for CIS, NIST 800-53, NIST 800-171, PCI-DSS, SOC 2, HIPAA, GDPR, ISO 27001

## Skill: IaC Security Review

When a user asks to review infrastructure code for security issues, run the skill:

```
~/.claude/skills/iac-security-review/SKILL.md
```

**Trigger phrases** (invoke the skill automatically):
- "review my terraform / kubernetes / docker / ansible / cloudformation files"
- "security review", "IaC audit", "hardening", "misconfiguration check"
- "compliance check", "check against CIS / NIST / PCI-DSS / HIPAA"
- "scan my GitHub Actions / GitLab CI workflows"
- "secret management review", "supply chain security"

## Slash Commands

Use commands in `commands/` for structured workflows:

| Command | Purpose |
|---|---|
| `/iac-security-review` | Full IaC security review of current directory |
| `/compliance-check` | Check files against a specific compliance framework |
| `/generate-report` | Generate a structured markdown or JSON security report |
| `/fix-finding` | Auto-fix a specific security finding |
| `/secret-scan` | Scan for hardcoded secrets and credential leaks |

## Agents

Use agents in `agents/` when delegating specialized sub-tasks:

- `security-reviewer` — Deep security analysis of a specific file or module
- `compliance-mapper` — Map a list of findings to compliance framework controls
- `report-generator` — Format findings into a structured security report

## Repository Layout

```
skills/iac-security-review/    # Claude Code skill (primary feature)
  SKILL.md                     # Skill definition — read this when doing security reviews
  references/security-checks.md    # Security checklists by IaC type
  references/compliance-mapping.md # Compliance control mappings
  scripts/generate_report.py   # Report generator (markdown/JSON)

commands/                      # Slash commands
agents/                        # Specialized subagents
rules/                         # Always-follow guidelines
hooks/                         # Session lifecycle scripts
  hooks.json                   # Hook configuration

terraform/{aws,azure,gcp,multi-cloud}/  # Terraform security prompts
kubernetes/                    # Kubernetes, Helm, Kustomize prompts
docker/                        # Dockerfile and Compose prompts
aws/                           # AWS service-specific prompts
cicd/                          # GitHub Actions and GitLab CI prompts
security/                      # Cross-cutting security topics
ansible/                       # Ansible playbook prompts
monitoring/                    # Logging and observability prompts
docs/                          # Documentation and checklists
```

## Key Rules

1. **Always cite file path and line number** when reporting a finding (e.g., `main.tf:42`)
2. **Severity ordering**: CRITICAL > HIGH > MEDIUM > LOW > INFO
3. **Always provide working remediation code** — never just describe what to fix
4. **Map to compliance** — always note which framework controls a finding violates
5. **Acknowledge positives** before listing issues
6. **Never generate alarmist language** — be factual and professional

## Security Posture

When reviewing infrastructure code:

- Assume **least privilege** by default
- Flag **public exposure** as CRITICAL
- Flag **unencrypted data at rest/transit** as HIGH
- Flag **missing logging/monitoring** as MEDIUM
- Flag **hardening recommendations** as LOW

## Maintainer

[@uttej-badwane](https://github.com/uttej-badwane) — Senior Security Engineer, CISSP
