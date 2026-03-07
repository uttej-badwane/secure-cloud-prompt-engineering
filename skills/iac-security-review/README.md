# IaC Security Review — Claude Code Skill

A Claude Code skill that performs comprehensive security reviews of Infrastructure as Code,
mapping findings to CIS, NIST 800-53, NIST 800-171, PCI-DSS, SOC 2, HIPAA, GDPR, and ISO 27001.

## Installation

```bash
cp -r skills/iac-security-review ~/.claude/skills/
```

Claude Code will automatically detect and load the skill on next launch.

## Activation

The skill activates automatically when your request involves IaC security. Trigger phrases include:

- "Review my Terraform for security issues"
- "Audit this Kubernetes manifest against CIS benchmarks"
- "Check this Dockerfile for vulnerabilities"
- "Scan my GitHub Actions workflow for security problems"
- "Perform a compliance check against NIST 800-53"
- "Security review", "IaC audit", "hardening", "misconfiguration"

## IaC Types Covered

| File Type | Examples |
|-----------|---------|
| Terraform | `*.tf`, `*.tfvars` |
| Kubernetes | YAML with `apiVersion:` |
| Docker | `Dockerfile*`, `docker-compose*.yml` |
| CloudFormation | YAML with `AWSTemplateFormatVersion:` |
| Ansible | Playbooks with `hosts:` or `tasks:` |
| Helm | `Chart.yaml`, `values.yaml` |
| CI/CD | `.github/workflows/*.yml`, `.gitlab-ci.yml` |
| Kustomize | `kustomization.yaml` |

## What Gets Checked

- **Authentication & Authorization** — IAM least privilege, no wildcards, service account scoping
- **Encryption** — at rest and in transit, KMS/CMK usage, key rotation
- **Network Security** — public exposure, security groups, VPN/PrivateLink
- **Secret Management** — dedicated vaults, rotation, runtime injection, no build-time secrets
- **Supply Chain** — pinned versions, SBOM, dependency scanning, artifact integrity
- **Compliance** — mapped to 8 frameworks per finding

## Report Format

The skill generates a structured report with:

- Executive summary (finding counts by severity)
- Per-finding: file path, description, risk, compliance controls, remediation with code snippet
- Compliance summary matrix
- Positive findings (what's done well)
- Prioritized next steps

To generate a report file directly:

```bash
python3 scripts/generate_report.py --format markdown --scope "terraform/" --output report.md
python3 scripts/generate_report.py --format json --scope "." --output report.json
```

## Reference Files

| File | Purpose |
|------|---------|
| `references/security-checks.md` | Full checklists by IaC type + vulnerability management |
| `references/compliance-mapping.md` | Finding → control mapping for 8 frameworks |
| `scripts/generate_report.py` | Report template generator (markdown + JSON) |

## Credits

Built by Uttej Badwane ([@uttej-badwane](https://github.com/uttej-badwane)) — Senior Security Engineer, CISSP.
Based on the [secure-cloud-prompt-engineering](https://github.com/uttej-badwane/secure-cloud-prompt-engineering) project.
