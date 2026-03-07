# 🔐 Secure Cloud Prompt Engineering

A collection of security-focused prompts for AI-assisted Infrastructure as Code (IaC) development.

> **Now available as a Claude Code skill!** Install in one command and get automated IaC security reviews directly in your editor. See [Quick Start](#-claude-code-skill--quick-start) below.

---

## 🎯 Purpose

Prompt templates to guide AI tools in generating secure cloud infrastructure code following security best practices.

Covers Terraform, Kubernetes, Docker, and cloud-native services with a focus on security controls and compliance.

---

## 🚀 Claude Code Skill — Quick Start

**Now available as a Claude Code skill!** Install the IaC Security Review skill and get automated security reviews of your infrastructure code.

### Install

```bash
# Clone the repo and copy the skill to your Claude Code skills directory
git clone https://github.com/uttej-badwane/secure-cloud-prompt-engineering.git
cp -r secure-cloud-prompt-engineering/skills/iac-security-review ~/.claude/skills/
```

### Use

Open Claude Code in any project with IaC files and try:

- `"Review my Terraform files for security issues"`
- `"Audit the Kubernetes manifests against CIS benchmarks"`
- `"Check this Dockerfile for vulnerabilities"`
- `"Scan my GitHub Actions workflows for security misconfigurations"`
- `"Run a compliance check against NIST 800-53 and PCI-DSS"`

The skill covers Terraform, Kubernetes, Docker, CloudFormation, Ansible, Helm, GitHub Actions, and GitLab CI — with findings mapped to CIS, NIST 800-53, NIST 800-171, PCI-DSS, SOC 2, HIPAA, GDPR, and ISO 27001.

For full details see [`skills/iac-security-review/README.md`](skills/iac-security-review/README.md).

---

## 📁 Repository Structure

```
📦 secure-cloud-prompt-engineering
│
├── 🤖 skills/
│   └── iac-security-review/   → Claude Code skill (automated IaC security review)
│       ├── SKILL.md           → Skill definition and workflow
│       ├── README.md          → Installation and usage guide
│       ├── references/        → Security checklists and compliance mappings
│       └── scripts/           → Report generator (markdown + JSON)
│
├── 🏗️  terraform/
│   ├── aws/           → AWS Terraform security prompts
│   ├── azure/         → Azure Terraform security prompts
│   ├── gcp/           → GCP Terraform security prompts
│   └── multi-cloud/   → Multi-cloud Terraform patterns
│
├── ☸️  kubernetes/
│   ├── k8s-security.md       → Kubernetes security best practices
│   ├── helm-security.md      → Helm chart security
│   └── kustomize-security.md → Kustomize configuration security
│
├── 🐳 docker/
│   ├── dockerfile-security.md      → Dockerfile security hardening
│   └── docker-compose-security.md  → Docker Compose security
│
├── ☁️  aws/
│   ├── aws-cli-security.md         → AWS CLI secure usage
│   ├── cloudformation-security.md  → CloudFormation templates
│   └── cdk-security.md             → AWS CDK security patterns
│
├── ⚙️  ansible/
│   ├── ansible-security.md       → Ansible playbook security
│   └── ansible-vault-security.md → Ansible Vault secrets management
│
├── 🔄 cicd/
│   ├── github-actions-security.md → GitHub Actions workflows
│   └── gitlab-ci-security.md      → GitLab CI/CD pipelines
│
├── 📊 monitoring/
│   └── logging-security.md → Logging and monitoring security
│
├── 🛡️  security/
│   ├── iac-security-review.md    → IaC security review checklist
│   ├── secret-management.md      → Secrets management strategies
│   ├── compliance-frameworks.md  → CIS, NIST, PCI-DSS, SOC2, HIPAA, GDPR
│   └── vulnerability-scanning.md → Vulnerability scanning tools and practices
│
└── 📚 docs/
    └── security-checklist.md → Security best practices checklist
```

---

## 🚀 Usage

1. Select the prompt file for your technology stack
2. Copy the prompt content
3. Provide it to your AI assistant with your specific requirements
4. Review and validate the generated code

**Note:** Always scan and audit AI-generated code before production deployment.

---

## ✨ Features

- **Security-first approach** - Emphasizes least privilege, defense-in-depth, and security controls
- **Multi-cloud support** - AWS, Azure, and GCP
- **Compliance frameworks** - CIS benchmarks, NIST, PCI-DSS
- **Production patterns** - Enterprise security configurations

---

## 🤝 Contributing

Contributions are welcome. Please ensure prompts are:
- Concise and well-documented
- Security-focused with clear threat models
- Under 40 lines
- Tested with popular AI assistants

---

## 👥 Maintainers

- [@uttej-badwane](https://github.com/uttej-badwane) - Repository Owner & Primary Maintainer

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

**⭐ If you find this repository helpful, please consider giving it a star!**

*Made with ❤️ for the Security & DevOps Community*
