# Secure Cloud Prompt Engineering

**IaC security reviews, automated. Powered by Claude.**

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blueviolet)](https://github.com/uttej-badwane/secure-cloud-prompt-engineering)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-blue)](CHANGELOG.md)

> Review Terraform, Kubernetes, Docker, CloudFormation, Ansible, GitHub Actions, and more —
> directly in Claude Code or automatically on every PR.

---

## Install

### Claude Code (Free)

```bash
# One-command install
./install.sh

# Or install just the skill manually
cp -r skills/iac-security-review ~/.claude/skills/
```

Or via Claude Code:
```
/plugin install uttej-badwane/secure-cloud-prompt-engineering
```

### GitHub App (Pro — $29/mo)

Automatically reviews every PR that touches IaC files. Posts findings as inline PR comments.
Optionally blocks merges on CRITICAL findings.

**[Install on GitHub Marketplace →](https://github.com/marketplace/iac-security-review)**

No code changes needed. Just install the app and add `ANTHROPIC_API_KEY` to your repo secrets.

---

## What It Does

After installing the Claude Code plugin, use natural language or slash commands:

```
/iac-security-review              # Full scan of current directory
/compliance-check pci terraform/  # PCI-DSS check on Terraform files
/secret-scan                      # Find hardcoded secrets
/fix-finding 2                    # Auto-fix finding #2 in place
/generate-report json             # Export findings as JSON
```

Or trigger by describing what you want:
- *"Review my Terraform for security issues"*
- *"Audit Kubernetes manifests against CIS benchmarks"*
- *"Check this Dockerfile for vulnerabilities"*
- *"Scan GitHub Actions workflows for supply chain risks"*

### IaC Types Supported

| Type | Files |
|---|---|
| Terraform | `*.tf`, `*.tfvars` |
| Kubernetes | `*.yaml` with `apiVersion:` |
| Docker | `Dockerfile*`, `docker-compose*.yml` |
| CloudFormation | `*.yaml` with `AWSTemplateFormatVersion` |
| Ansible | Playbooks with `hosts:` / `tasks:` |
| Helm | `Chart.yaml`, `values.yaml` |
| GitHub Actions | `.github/workflows/*.yml` |
| GitLab CI | `.gitlab-ci.yml` |
| Kustomize | `kustomization.yaml` |

### Compliance Frameworks

CIS Benchmarks · NIST 800-53 · NIST 800-171 · PCI-DSS · SOC 2 · HIPAA · GDPR · ISO 27001

---

## Pricing

| | Free | Pro | Enterprise |
|---|:---:|:---:|:---:|
| Claude Code plugin | ✅ | ✅ | ✅ |
| 5 slash commands | ✅ | ✅ | ✅ |
| CIS + NIST mapping | ✅ | ✅ | ✅ |
| All 8 frameworks | — | ✅ | ✅ |
| GitHub App (auto PR review) | — | ✅ | ✅ |
| Block merges on CRITICAL | — | ✅ | ✅ |
| JSON export / integrations | — | ✅ | ✅ |
| Self-hosted deployment | — | — | ✅ |
| Custom OPA/Rego rules | — | — | ✅ |
| SAML SSO + audit log | — | — | ✅ |
| SLA + dedicated support | — | — | ✅ |
| **Price** | **Free** | **$29/mo/org** | **Contact us** |

[Full pricing details →](PRICING.md)

---

## Repository Layout

```
skills/iac-security-review/    # Claude Code skill
  SKILL.md                     # Skill definition and workflow
  references/                  # Security checklists and compliance mappings
  scripts/generate_report.py   # Report generator (markdown/JSON)

commands/                      # Slash commands (/iac-security-review, /compliance-check, ...)
agents/                        # Specialized subagents (security-reviewer, compliance-mapper, ...)
rules/                         # Always-follow guidelines (security-first, iac-standards)
hooks/                         # Session lifecycle hooks

.github/
  workflows/pr-security-review.yml  # GitHub Action for automated PR reviews
  scripts/iac_review.py             # Claude API integration for CI/CD

terraform/{aws,azure,gcp,multi-cloud}/  # Terraform security prompts
kubernetes/                    # Kubernetes, Helm, Kustomize prompts
docker/                        # Dockerfile and Compose prompts
aws/                           # AWS service-specific prompts
cicd/                          # GitHub Actions and GitLab CI prompts
security/                      # Cross-cutting security topics
ansible/                       # Ansible playbook prompts
monitoring/                    # Logging and observability prompts
```

---

## Contributing

Contributions welcome. Please ensure new checks:
- Reference a specific CIS, NIST, or vendor security document
- Include a working remediation code snippet
- Specify the severity level (CRITICAL / HIGH / MEDIUM / LOW)

---

## Maintainer

[@uttej-badwane](https://github.com/uttej-badwane) — Senior Security Engineer, CISSP

**Enterprise inquiries:** [enterprise@securecloud.dev](mailto:enterprise@securecloud.dev)

---

## License

MIT — free for personal and commercial use. See [LICENSE](LICENSE).

---

*Comparable tools: Checkov, Snyk IaC ($20K+/yr), Wiz Code ($24K+/yr). We charge $29/month.*
