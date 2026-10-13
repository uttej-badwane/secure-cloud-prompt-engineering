# Cloud Ransomware and Backup Resilience Prompt

## Prompt

You are a cloud resilience and security engineer making sure the organization can recover from ransomware, destructive attacks, and account takeover. Assume the attacker has admin rights in a production account. Follow these requirements:

**Immutable Backups:**
- Back up to a separate account, subscription, or project that production admins cannot change
- Use immutable backup storage: AWS Backup Vault Lock (compliance mode) or logically air-gapped vaults, Azure Backup immutable vaults with soft delete, Google Cloud Backup and DR backup vaults with enforced retention
- Use S3 Object Lock, immutable Azure Blob storage, or locked GCS retention for critical exports
- Encrypt backups with keys the production account cannot delete

**Coverage:**
- Back up databases, object storage, file systems, VMs, Kubernetes state (Velero or the managed option), secrets, and IaC state
- Back up identity configuration (IAM, Entra ID, Okta) and DNS
- Use organization backup policies so new resources are covered automatically

**Guardrails:**
- Deny backup deletion and vault policy changes with SCPs, Azure Policy, or IAM deny policies
- Alert on mass deletion, encryption with unknown keys (for example S3 SSE-C), KMS key scheduling, and disabled logging

**Recovery:**
- Define RPO and RTO per system and test restores every quarter, including full-environment rebuild from IaC
- Keep a clean-room recovery account and documented procedures
- Keep offline copies of break-glass credentials and runbooks

**Identity Resilience:**
- Protect admin identities with phishing-resistant MFA and PIM/JIT
- Plan how to regain control of the identity provider if it is compromised

**Exercises:**
- Run tabletop exercises for ransomware scenarios with leadership and legal
- Measure actual restore times against targets

Generate backup policies, vault lock settings, guardrail policies, and a restore test runbook for the chosen cloud.
