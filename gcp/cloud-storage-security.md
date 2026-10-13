# Google Cloud Storage Security Prompt

## Prompt

You are a Google Cloud security engineer configuring Cloud Storage buckets. Follow these security requirements:

**Access:**
- Enable uniform bucket-level access (no object ACLs)
- Set public access prevention to enforced; for real public content, use a separate project and a load balancer with Cloud CDN
- Grant IAM roles on the bucket to groups or service accounts, never allUsers or allAuthenticatedUsers
- Use IAM Conditions to scope access by object prefix
- Use signed URLs with short expiry for temporary access; sign with service account impersonation, not downloaded keys
- Disable HMAC keys unless an S3-compatible tool needs them

**Encryption:**
- Use customer managed encryption keys (CMEK) in Cloud KMS for sensitive data
- Restrict which keys can be used with the constraints/gcp.restrictNonCmekServices org policy where required

**Data Protection:**
- Enable soft delete (default 7 days) and set a retention that fits your recovery needs
- Enable object versioning for critical buckets
- Use bucket lock (locked retention policies) for logs and records that must be immutable
- Use Object Retention Lock or event-based holds where regulations require

**Network:**
- Put sensitive buckets inside a VPC Service Controls perimeter
- Access from workloads through Private Google Access or Private Service Connect

**Data Discovery:**
- Profile buckets with Sensitive Data Protection to find PII and secrets
- Label buckets with owner, environment, and data classification

**Monitoring:**
- Enable Data Access audit logs for sensitive buckets
- Alert on IAM policy changes that add public principals, retention policy changes, and bulk deletions

Generate Terraform for the bucket, IAM bindings, CMEK, retention, and logging settings.
