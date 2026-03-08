# Pricing

IaC Security Review for Claude Code is **free and open source** for individual use.
Paid tiers unlock automation and enterprise features.

---

## Free — Open Source

**$0 / forever**

The full Claude Code plugin. Install once, use everywhere.

- IaC security review skill (Terraform, Kubernetes, Docker, CloudFormation, Ansible, Helm, GitHub Actions, GitLab CI)
- 5 slash commands: `/iac-security-review`, `/compliance-check`, `/generate-report`, `/fix-finding`, `/secret-scan`
- 3 specialized agents: security-reviewer, compliance-mapper, report-generator
- Always-follow security rules (security-first, IaC standards)
- Session hooks (auto-loads context, saves findings between sessions)
- CIS Benchmarks + NIST 800-53 compliance mapping

**Install:**
```bash
# One-line install
./install.sh

# Or via Claude Code
/plugin install uttej-badwane/secure-cloud-prompt-engineering
```

---

## Pro — GitHub App

**$29 / month per organization**

Automate security reviews on every pull request. Never merge insecure IaC again.

- Everything in Free
- **GitHub App** that triggers automatically on every PR touching IaC files
- Inline PR comments with severity-ordered findings
- Block merges on CRITICAL findings (configurable per repo)
- All 8 compliance frameworks: CIS, NIST 800-53, NIST 800-171, PCI-DSS, SOC 2, HIPAA, GDPR, ISO 27001
- JSON export for Jira, Linear, and GitHub Issues integration
- Custom severity thresholds
- Review history dashboard

**Get Pro:** [github.com/marketplace/iac-security-review](https://github.com/marketplace/iac-security-review)

> If you use Claude Code today, the GitHub App uses the same security logic — just fully automated on every PR.

---

## Enterprise

**Custom pricing — annual contract**

For teams with compliance requirements, self-hosting needs, or large engineering organizations.

- Everything in Pro
- **Self-hosted deployment** (no data leaves your infrastructure)
- Custom security rules via OPA/Rego policies
- SAML SSO and full audit logging
- Private compliance framework mappings (internal standards, custom controls)
- 99.9% uptime SLA
- Dedicated Slack support channel
- Quarterly security posture review calls with the maintainer
- Volume discount for 50+ developers

**Contact:** [enterprise@securecloud.dev](mailto:enterprise@securecloud.dev)

---

## Comparison

| Feature | Free | Pro | Enterprise |
|---|:---:|:---:|:---:|
| Claude Code plugin | ✅ | ✅ | ✅ |
| Slash commands | ✅ | ✅ | ✅ |
| Specialized agents | ✅ | ✅ | ✅ |
| CIS + NIST mapping | ✅ | ✅ | ✅ |
| All 8 frameworks | — | ✅ | ✅ |
| GitHub App (auto PR review) | — | ✅ | ✅ |
| Block merges on CRITICAL | — | ✅ | ✅ |
| JSON export / integrations | — | ✅ | ✅ |
| Custom severity thresholds | — | ✅ | ✅ |
| Self-hosted deployment | — | — | ✅ |
| Custom OPA/Rego rules | — | — | ✅ |
| SAML SSO + audit log | — | — | ✅ |
| 99.9% SLA | — | — | ✅ |
| Dedicated support | — | — | ✅ |
| **Price** | **Free** | **$29/mo/org** | **Contact us** |

---

## Why Pay?

The free plugin is genuinely useful — it reviews your IaC interactively in Claude Code.
The paid tiers solve a different problem: **enforcement at scale**.

When you have 10+ engineers pushing Terraform and Kubernetes changes daily, manual reviews
get skipped. The GitHub App makes security review automatic and non-optional, without
adding friction to the developer workflow.

The **IaC security market charges $20K–$38K/year** for comparable automation (Snyk IaC,
Wiz Code, Checkov Enterprise). We charge $29/month.

---

*Questions? Open an issue or email [uttej@securecloud.dev](mailto:uttej@securecloud.dev)*
