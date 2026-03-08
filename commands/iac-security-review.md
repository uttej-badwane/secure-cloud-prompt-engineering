---
name: iac-security-review
description: Run a full IaC security review of the current directory or specified files
---

Perform a comprehensive IaC security review by following the skill at
`skills/iac-security-review/SKILL.md`.

## Steps

1. **Identify scope** — scan the current directory (or files provided as arguments) for IaC files:
   `*.tf`, `*.tfvars`, `*.yaml`, `*.yml`, `Dockerfile*`, `docker-compose*.yml`, `kustomization.yaml`

2. **Run security checks** — evaluate each file against the checklists in
   `skills/iac-security-review/references/security-checks.md`

3. **Map to compliance** — map findings to CIS + NIST 800-53 by default (or frameworks specified by the user)
   using `skills/iac-security-review/references/compliance-mapping.md`

4. **Generate report** — produce a structured report with severity-ordered findings, compliance matrix,
   positive findings, and prioritized remediation steps

5. **Offer to fix** — after presenting the report, ask if the user wants to auto-fix specific findings

## Usage

```
/iac-security-review
/iac-security-review terraform/
/iac-security-review .github/workflows/deploy.yml
```

If arguments are provided, limit the review scope to those paths.
If no arguments are provided, scan the entire current directory tree.
