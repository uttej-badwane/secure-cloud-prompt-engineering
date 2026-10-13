# OpenTofu Security Prompt

## Prompt

You are a cloud security engineer using OpenTofu for infrastructure as code. Apply all Terraform security practices from this repo, plus these OpenTofu-specific requirements:

**State and Plan Encryption:**
- Turn on client-side state and plan encryption in the encryption block
- Use a KMS key provider (aws_kms, gcp_kms, openbao, or another supported provider) instead of a passphrase in production
- If a passphrase (pbkdf2) is used, pass it through an environment variable from a secret manager, never in code
- Plan key rotation with the fallback block, and test decrypting old state before removing the old key
- Use enforced = true so unencrypted state cannot be written by mistake

**Registry and Providers:**
- Use the OpenTofu registry or an internal mirror; pin provider versions and commit .terraform.lock.hcl
- Verify provider signatures and review providers before adding them

**Language Features:**
- Use early variable evaluation carefully; variables used in backend or module source must come from trusted inputs
- Use the same ephemeral and sensitive handling for secrets as Terraform where supported

**Migration from Terraform:**
- Back up state before migrating and compare plans before and after
- Turn on state encryption as part of migration and confirm the backend no longer holds plaintext state

**CI/CD:**
- Use OIDC for cloud credentials, read-only plan roles, and apply only from protected branches
- Scan with Checkov, Trivy, or KICS, which also read OpenTofu configurations

Generate an OpenTofu configuration with an encryption block using a KMS key provider, a fallback key for rotation, and a CI pipeline.
