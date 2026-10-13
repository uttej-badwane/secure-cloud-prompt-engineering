# Terraform State Security Prompt

## Prompt

You are a cloud security engineer protecting Terraform and OpenTofu state. State files can hold passwords, keys, and full resource details, so treat them as secrets. Follow these security requirements:

**Backend:**
- Never use local state for shared or production infrastructure
- Use a remote backend with encryption at rest, versioning, and locking:
  - S3 with encrypt = true, a customer managed KMS key, versioning, and use_lockfile = true
  - azurerm with Entra ID auth (use_azuread_auth) and blob versioning or soft delete
  - GCS with CMEK, versioning, and uniform bucket-level access
  - HCP Terraform or Terraform Enterprise workspaces
- Block public access on the state bucket and enforce TLS

**Access:**
- Grant state read and write only to the CI roles that run plan and apply, plus a break-glass group
- Remember that read access to state is read access to every secret in it
- Use a separate state per environment and per blast-radius boundary, in separate buckets or accounts for production
- Log every state read and write (S3 data events, storage logs) and alert on access by humans

**Keep Secrets Out:**
- Use ephemeral resources and write-only arguments (Terraform 1.11+) so secrets are never stored
- Mark sensitive variables and outputs sensitive = true (this only hides them in output; it does not remove them from state)
- Use managed secrets (manage_master_user_password and similar) instead of passing passwords through Terraform
- With OpenTofu, turn on state encryption with a KMS key provider

**Sharing Data:**
- Avoid terraform_remote_state across teams; it exposes the whole state. Publish needed values to SSM Parameter Store, App Configuration, or outputs in a narrow data store instead

**Recovery:**
- Keep state versions and test recovery from an older version
- Protect against state deletion with bucket policies and object lock or soft delete

Generate backend configurations for AWS, Azure, and GCP, IAM policies for the state bucket, and an example that uses an ephemeral resource with a write-only argument.
