---
name: secret-scan
description: Scan files for hardcoded secrets, credentials, and sensitive data leaks
---

Perform a targeted scan for hardcoded secrets and credential leaks across IaC files,
config files, and CI/CD pipeline definitions.

## What to Look For

### High-Confidence Patterns (CRITICAL)
- AWS access keys (`AKIA[0-9A-Z]{16}`)
- AWS secret keys (40-char alphanumeric strings near "secret")
- Private keys (`-----BEGIN RSA PRIVATE KEY-----`, `-----BEGIN EC PRIVATE KEY-----`)
- GitHub personal access tokens (`ghp_`, `gho_`, `ghs_`, `ghu_`)
- Generic API keys in assignments (`api_key = "..."`, `token = "..."`)
- Database connection strings with embedded passwords
- Kubernetes `Secret` resources with base64 values that decode to credentials

### Medium-Confidence Patterns (HIGH)
- Passwords in `ENV`, `ARG`, or environment variable blocks
- Secrets in `.env` files committed to the repository
- Sensitive values in `terraform.tfvars` or `*.auto.tfvars`
- Credentials in CI/CD YAML (not using `${{ secrets.* }}` or `$CI_*`)
- Ansible variables containing "password", "secret", "key", "token"

### Common False Positives to Exclude
- Example/placeholder values (`"your-api-key-here"`, `"REPLACE_ME"`, `"<token>"`)
- Test fixtures clearly marked as fake
- Commented-out code

## Steps

1. Scan target files (or entire directory if no argument)
2. For each match, report:
   - File path and line number
   - The matched pattern type
   - Severity (CRITICAL/HIGH)
   - Recommended fix (use secret manager reference instead)
3. Never print the actual secret value — mask it as `[REDACTED]`
4. After reporting, offer to replace hardcoded values with the appropriate secret reference:
   - Terraform: `data.aws_secretsmanager_secret_version.*`
   - Kubernetes: `secretKeyRef` or External Secrets Operator
   - GitHub Actions: `${{ secrets.SECRET_NAME }}`
   - Ansible: `"{{ vault_variable_name }}"`

## Usage

```
/secret-scan
/secret-scan terraform/
/secret-scan .github/workflows/deploy.yml
```
