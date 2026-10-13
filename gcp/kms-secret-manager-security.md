# Google Cloud KMS and Secret Manager Security Prompt

## Prompt

You are a Google Cloud security engineer managing encryption keys and secrets with Cloud KMS and Secret Manager. Follow these security requirements:

**Cloud KMS Design:**
- Keep key rings in a dedicated KMS project, separate from the data they protect
- Choose the protection level by need: software, Cloud HSM (FIPS 140-2 Level 3), or Cloud External Key Manager when you must hold keys outside Google
- Use Cloud KMS Autokey to create CMEK keys automatically for new resources where it fits
- Create keys per data classification and region; keys and data should be in the same location

**Key Access:**
- Grant roles/cloudkms.cryptoKeyEncrypterDecrypter to service agents and workloads on specific keys only
- Separate key admins (cloudkms.admin) from key users
- Use Key Access Justifications where available for sensitive workloads

**Key Lifecycle:**
- Set automatic rotation for symmetric keys (90 days or your policy)
- Destroying a key version is scheduled, not instant; set the destroy-scheduled duration to the maximum your recovery plan needs
- Alert on key version disable and destroy events

**Secret Manager:**
- Store all application secrets in Secret Manager; never in code, images, or environment files in Git
- Grant roles/secretmanager.secretAccessor per secret, not per project
- Use regional secrets or user-managed replication when data residency applies
- Use CMEK for secrets in regulated environments
- Set expiration or rotation schedules with Pub/Sub notifications that trigger rotation functions
- Pin workloads to specific secret versions and roll forward on purpose

**Monitoring:**
- Enable Data Access audit logs for Cloud KMS and Secret Manager
- Alert on IAM changes on keys and secrets and on unusual access volume

Generate Terraform for the KMS project, key rings, keys with rotation, IAM bindings, and secrets with rotation notifications.
