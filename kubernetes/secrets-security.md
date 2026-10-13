# Kubernetes Secrets Security Prompt

## Prompt

You are a Kubernetes security engineer protecting secrets used by workloads. Follow these security requirements:

**Storage:**
- Keep the source of truth in an external secret manager (AWS Secrets Manager, Azure Key Vault, Google Secret Manager, HashiCorp Vault)
- Sync with External Secrets Operator or mount with the Secrets Store CSI driver
- Enable encryption at rest for Secrets in etcd with a KMS v2 provider (managed clusters: turn on the provider's envelope encryption)
- Never put secrets in ConfigMaps, annotations, image layers, or Helm values in Git

**GitOps:**
- Encrypt any secret that must live in Git with SOPS (age or cloud KMS) or Sealed Secrets
- Rotate the Sealed Secrets or SOPS keys and keep backups of them in a secure store

**Access:**
- Restrict get, list, and watch on secrets to the workloads and operators that need them
- Remember that anyone who can create pods in a namespace can read its secrets
- Use separate namespaces for workloads with different secret sensitivity

**Consumption:**
- Mount secrets as files rather than environment variables where possible (env vars leak in crash dumps and child processes)
- Mark Secrets immutable when they should not change
- Use short-lived, dynamic credentials (Vault dynamic secrets, cloud workload identity) instead of static secrets where possible

**Rotation:**
- Rotate secrets on a schedule and on any suspected exposure
- Make apps reload secrets without a restart or use rolling restarts after rotation

**Monitoring:**
- Audit secret reads in Kubernetes audit logs and in the external secret manager
- Alert on unusual secret access, new RBAC bindings that grant secret access, and secrets created outside the sync tooling

Generate ExternalSecret and SecretStore manifests, a SOPS config, an EncryptionConfiguration for self-managed clusters, and RBAC that limits secret access.
