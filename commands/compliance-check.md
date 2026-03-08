---
name: compliance-check
description: Check IaC files against a specific compliance framework
---

Run a targeted compliance check against a specified framework.

## Supported Frameworks

| Argument | Framework |
|---|---|
| `cis` | CIS Benchmarks (AWS, Azure, GCP, Kubernetes, Docker) |
| `nist` | NIST 800-53 (Federal security controls) |
| `nist-171` | NIST 800-171 (Controlled Unclassified Information) |
| `pci` | PCI-DSS (Payment card data) |
| `soc2` | SOC 2 (Service organization controls) |
| `hipaa` | HIPAA (Healthcare data protection) |
| `gdpr` | GDPR (EU data privacy) |
| `iso27001` | ISO 27001 (Information security management) |

## Steps

1. Parse the framework argument (e.g., `/compliance-check pci terraform/`)
2. Load the compliance control mappings from `skills/iac-security-review/references/compliance-mapping.md`
3. Scan the target files against controls relevant to that framework
4. Report each finding with:
   - The specific control ID violated (e.g., `PCI-DSS 3.4`, `NIST AC-3`)
   - File path and line number
   - What the control requires
   - Current state vs. required state
   - Remediation code snippet
5. Produce a pass/fail compliance summary table

## Usage

```
/compliance-check cis
/compliance-check pci terraform/aws/
/compliance-check hipaa kubernetes/
/compliance-check nist .github/workflows/
```

If no framework is provided, default to `cis` + `nist`.
If no path is provided, scan the entire current directory.
