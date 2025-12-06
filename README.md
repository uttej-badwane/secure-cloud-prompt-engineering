# 🔐 Secure Cloud Prompt Engineering

A collection of security-focused prompts for AI-assisted Infrastructure as Code (IaC) development.

---

## 🎯 Purpose

Prompt templates to guide AI tools in generating secure cloud infrastructure code following security best practices.

Covers Terraform, Kubernetes, Docker, and cloud-native services with a focus on security controls and compliance.

---

## 📁 Repository Structure

```
📦 secure-cloud-prompt-engineering
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
