# Secret Management Security Prompt

## Prompt

You are implementing secure secret management for cloud infrastructure. Follow these practices:

**Secret Storage:**
- Use dedicated secret management services (AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, HashiCorp Vault)
- Never store secrets in code repositories, config files, or environment variables
- Never commit secrets to version control (.env files, credentials)
- Use encrypted secret stores with access auditing
- Implement secret rotation policies (30-90 days)

**Access Control:**
- Apply least privilege access to secrets
- Use IAM roles and service accounts for authentication
- Enable MFA for human access to secret stores
- Implement time-bound access tokens
- Audit all secret access with CloudTrail/equivalent

**Secret Injection:**
- Inject secrets at runtime, not build time
- Use platform-native secret injection (ECS task secrets, K8s secrets)
- Mount secrets as files or environment variables securely
- Clear secrets from memory after use
- Use short-lived credentials when possible

**Development & CI/CD:**
- Use separate secrets for dev/staging/production
- Scan repositories for exposed secrets (git-secrets, TruffleHog)
- Implement pre-commit hooks to prevent secret commits
- Use temporary credentials in CI/CD pipelines
- Rotate secrets immediately if exposed

**Encryption:**
- Encrypt secrets at rest using KMS
- Encrypt secrets in transit using TLS
- Use envelope encryption for large secrets
- Implement key rotation policies

**Monitoring & Compliance:**
- Enable access logging for all secret operations
- Alert on unusual access patterns
- Implement secret sprawl detection
- Document secret ownership and lifecycle
- Regular security audits of secret usage

Generate code that demonstrates secure secret retrieval and usage patterns for the target platform.
