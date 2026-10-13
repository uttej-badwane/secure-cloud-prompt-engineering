# GitHub Organization and Enterprise Security Prompt

## Prompt

You are a security engineer hardening a GitHub organization or enterprise (GitHub.com, Enterprise Managed Users, or GitHub Enterprise Server). Source control holds code, secrets, and the keys to production through CI/CD. Follow these requirements:

**Identity:**
- Use SAML SSO or Enterprise Managed Users tied to your identity provider, with SCIM provisioning
- Require 2FA, and prefer passkeys or security keys
- Review outside collaborators every quarter and remove those not needed

**Organization Settings:**
- Set base repository permission to None or Read
- Restrict who can create public repositories, change visibility, delete repos, and transfer repos
- Disable forking of private repositories unless needed
- Require approval for fine-grained personal access tokens and restrict classic PATs
- Restrict OAuth app access and prefer GitHub Apps with minimal permissions
- Use IP allow lists where your network model supports it

**Repository Protection:**
- Use rulesets on default and release branches: required reviews, CODEOWNERS review, status checks, signed commits where practical, and no force pushes
- Keep the bypass list small and audited
- Protect tags used for releases

**Security Features:**
- Turn on secret scanning with push protection, Dependabot alerts and updates, and code scanning across all repos
- Turn on private vulnerability reporting for public repos

**GitHub Actions:**
- Set default GITHUB_TOKEN permissions to read
- Allow only selected actions and require SHA pinning
- Require approval for workflows from outside contributors
- Use environments with required reviewers for deployments
- Restrict self-hosted runners to specific repos through runner groups

**Monitoring:**
- Stream the audit log to the SIEM
- Alert on visibility changes, new admins, ruleset changes, new deploy keys, PAT approvals, and secret scanning bypasses

Generate Terraform (github provider) for organization settings, rulesets, and Actions policies, plus a checklist for settings that need the UI or API.
