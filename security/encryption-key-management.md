# Cloud Encryption and Key Management Strategy Prompt

## Prompt

You are a security architect defining an encryption and key management strategy across AWS, Azure, and Google Cloud. Follow these requirements:

**Classify First:**
- Map data classes (public, internal, confidential, regulated) to required controls
- Decide per class: provider-managed keys, customer managed keys (CMK/CMEK), HSM-backed keys, or external key management (AWS XKS, Azure Managed HSM, Google Cloud EKM)
- Use external or HSM keys only where a regulation or contract needs them; they add outage risk

**Key Hierarchy:**
- Use envelope encryption: data keys protected by key encryption keys in the cloud KMS
- Separate keys by environment, data class, and tenant where isolation matters
- Keep key management in a dedicated account, subscription, or project

**Access and Separation of Duties:**
- Key admins cannot use keys; key users cannot change key policies
- Bind key use to specific services and workloads (kms:ViaService, Azure RBAC on key scope, per-key IAM in Cloud KMS)
- Protect key deletion with waiting periods, guardrail policies, and alerts

**Rotation and Lifecycle:**
- Turn on automatic rotation for symmetric keys
- Plan rotation for asymmetric and imported keys, including re-encryption where needed
- Document crypto-shredding: how deleting a key renders data unreadable, and test it

**In Transit:**
- TLS 1.2 minimum, TLS 1.3 preferred, with modern cipher suites
- Mutual TLS or workload identity for service-to-service traffic
- Track certificates and automate renewal

**Cryptographic Agility:**
- Keep an inventory of algorithms, key sizes, and libraries in use
- Use FIPS 140-validated modules where required (FedRAMP, CMMC, government)
- Plan for post-quantum migration (see post-quantum-cryptography-readiness.md)

**Monitoring:**
- Log all key operations and alert on policy changes, disable or delete events, and unusual decrypt volume

Generate a key management standard document, a per-cloud mapping table of services and settings, and Terraform examples for each cloud.
