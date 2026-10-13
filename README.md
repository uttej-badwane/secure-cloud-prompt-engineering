# 🔐 Secure Cloud Prompt Engineering

**130+ ready-to-use security prompts for cloud engineers, platform teams, developers, and AI builders.**

Paste a prompt into Claude, ChatGPT, Copilot, Gemini, or any AI assistant, add your requirements, and get infrastructure, code, policies, and runbooks that follow current security practice for AWS, Azure, Google Cloud, Kubernetes, CI/CD, SaaS, and AI systems.

It also ships as a **Claude Code plugin** with an IaC security review skill, slash commands, and agents.

---

## 🚀 Quick Start

### Use a prompt

1. Find the prompt for your task in the [catalog](#-prompt-catalog) below
2. Copy the text under `## Prompt`
3. Paste it into your AI assistant and add your details, for example: *"Create an S3 bucket for audit logs in account 1234 with 7-year retention"*
4. Review the output, run your scanners, and test before production

### Install the Claude Code plugin

```
/plugin install secure-cloud-prompt-engineering --marketplace uttej-badwane/secure-cloud-prompt-engineering
```

On Claude Code versions before 2.1.275, add the marketplace first:

```
/plugin marketplace add uttej-badwane/secure-cloud-prompt-engineering
/plugin install secure-cloud-prompt-engineering@uttej-badwane
```

Or install only the skill by hand:

```bash
git clone https://github.com/uttej-badwane/secure-cloud-prompt-engineering.git
cp -r secure-cloud-prompt-engineering/skills/iac-security-review ~/.claude/skills/
```

Then try:

- `"Review my Terraform files for security issues"`
- `"Audit the Kubernetes manifests against CIS benchmarks"`
- `"Scan my GitHub Actions workflows for security misconfigurations"`
- `"Run a compliance check against NIST 800-53 and PCI-DSS"`

See [`skills/iac-security-review/README.md`](skills/iac-security-review/README.md) for details.

---

## 📚 Prompt Catalog

Each folder has its own README with the full list of prompts and what each one covers.

| Folder | Prompts | What it covers |
|---|---|---|
| ☁️ [aws/](aws/) | 19 | IAM, S3, VPC, EC2, KMS, RDS, DynamoDB, ECS/ECR, Lambda, CloudFront/WAF, Cognito, Route 53, messaging, data perimeter, Control Tower, security services, CDK, CloudFormation, CLI |
| 🔷 [azure/](azure/) | 10 | Entra ID, landing zone and policy, Storage, Key Vault, networking, App Service/Functions, SQL/Cosmos DB, Defender/Sentinel, Bicep, VMs |
| 🟢 [gcp/](gcp/) | 10 | Organization and IAM, VPC, Cloud Storage, Cloud Run, Cloud SQL, BigQuery, KMS/Secret Manager, logging/SCC, VPC Service Controls, Compute Engine |
| ☸️ [kubernetes/](kubernetes/) | 13 | Pod security, managed clusters (EKS/AKS/GKE), RBAC, admission policy, network policy and mesh, Gateway API, runtime, GitOps, multi-tenancy, secrets, cluster hardening, Helm, Kustomize |
| 🐳 [docker/](docker/) | 4 | Dockerfile, Compose, host and daemon hardening, container registries |
| 🏗️ [terraform/](terraform/) | 8 | AWS, Azure, GCP, multi-cloud, state security, module and provider supply chain, HCP Terraform, OpenTofu |
| 🧱 [iac/](iac/) | 2 | Pulumi, Crossplane |
| 🔄 [cicd/](cicd/) | 8 | GitHub Actions, GitLab CI, Jenkins, Azure DevOps, CodeBuild/CodePipeline, Cloud Build, CircleCI, self-hosted runners |
| ⚙️ [ansible/](ansible/) | 4 | Playbooks, Vault, Automation Platform/AWX, CIS and STIG hardening |
| 🪪 [identity/](identity/) | 5 | Workload identity federation, workforce SSO and MFA, privileged access, non-human identities, OAuth/OIDC |
| 🌐 [network/](network/) | 6 | API security, WAF and DDoS, zero trust access, hybrid connectivity, egress control, TLS certificates |
| 📊 [monitoring/](monitoring/) | 4 | Logging, audit logging baseline, detection engineering, observability stack |
| 🛡️ [security/](security/) | 19 | Threat modeling, architecture review, IR, forensics, tabletops, supply chain, secrets, keys, data/DLP, ransomware, policy as code, assessments, pentesting, compliance, FedRAMP/CMMC, sovereignty, post-quantum crypto |
| 🤖 [ai/](ai/) | 8 | AI agents and MCP, LLM platforms, RAG, coding assistants, model supply chain, MLOps, AI red teaming, AI gateways |
| 🧩 [saas/](saas/) | 5 | GitHub organizations, Microsoft 365, Google Workspace, Okta, SaaS posture |
| 🐍 [python/](python/) | 5 | Secure coding, cloud SDKs, FastAPI/Django/Flask, packaging, clean code style |
| ✨ [code-quality/](code-quality/) | 4 | Clean code, secure code review, IaC style, testing strategy |

Plus [`docs/security-checklist.md`](docs/security-checklist.md), a pre-deployment checklist.

---

## 🧭 Start Here by Role

| You are a... | Start with |
|---|---|
| Cloud security engineer | [security-services](aws/security-services.md), [cloud-security-assessment](security/cloud-security-assessment.md), [data-perimeter](aws/data-perimeter-security.md), [detection-engineering](monitoring/detection-engineering.md) |
| Platform or DevOps engineer | [terraform-state](terraform/general/terraform-state-security.md), [managed-kubernetes](kubernetes/managed-kubernetes-security.md), [github-actions](cicd/github-actions-security.md), [workload-identity-federation](identity/workload-identity-federation.md) |
| Application developer | [python-secure-coding](python/python-secure-coding.md), [api-security](network/api-security.md), [oauth-oidc](identity/oauth-oidc-implementation.md), [secure-code-review](code-quality/secure-code-review.md) |
| AI engineer | [ai-agent-mcp](ai/ai-agent-mcp-security.md), [rag-security](ai/rag-security.md), [model-supply-chain](ai/model-supply-chain-security.md), [ai-red-teaming](ai/ai-red-teaming.md) |
| Incident responder | [cloud-incident-response](security/cloud-incident-response.md), [cloud-forensics](security/cloud-forensics.md), [incident-response-tabletop](security/incident-response-tabletop.md) |
| GRC or public sector | [compliance-frameworks](security/compliance-frameworks.md), [fedramp-cmmc-readiness](security/fedramp-cmmc-readiness.md), [data-residency](security/data-residency-sovereign-cloud.md), [ansible-cis-stig](ansible/ansible-cis-stig-hardening.md) |

---

## 🤖 Claude Code Plugin Contents

| Component | What it does |
|---|---|
| [`skills/iac-security-review`](skills/iac-security-review/) | Reviews Terraform, Kubernetes, Docker, CloudFormation, Ansible, Helm, and CI/CD files, with findings mapped to CIS, NIST 800-53, NIST 800-171, PCI DSS, SOC 2, HIPAA, GDPR, and ISO 27001 |
| [`commands/`](commands/) | `/iac-security-review`, `/compliance-check`, `/secret-scan`, `/fix-finding`, `/generate-report` |
| [`agents/`](agents/) | `security-reviewer`, `compliance-mapper`, `report-generator` |
| [`rules/`](rules/) | Security-first and IaC coding standards |
| [`hooks/`](hooks/) | Session context and a warning before destructive commands |

---

## ✅ What Makes These Prompts Different

- **Current:** reviewed against 2026 guidance (for example SHA-pinned actions after the tj-actions and trivy-action compromises, Gateway API after the ingress-nginx retirement, S3 native state locking, ISO 27001:2022 and PCI DSS v4.0.1 control IDs)
- **Specific:** names the exact settings, policies, and condition keys to use, not generic advice
- **Threat-driven:** built around how real cloud breaches happen
- **Plain language:** short, scannable, and easy to adapt

Always review AI-generated output, run your own scanners, and test before production. Prompts are guidance, not a guarantee of compliance.

---

## 🤝 Contributing

New prompts and fixes are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and start from the [prompt template](docs/prompt-template.md). Run `python3 scripts/build_index.py` after adding a prompt to update the folder index.

---

## 👥 Maintainer

- [@uttej-badwane](https://github.com/uttej-badwane)

## 📄 License

MIT. See [LICENSE](LICENSE).

**⭐ If this helps you, please star the repo and share it with your team.**
