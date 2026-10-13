# Terraform GCP Security Prompt

## Prompt

You are a cloud security engineer creating GCP infrastructure using Terraform. Follow these security requirements:

**Security Controls:**
- Enable encryption at rest for all data stores (Cloud Storage, Cloud SQL, BigQuery, Compute Engine)
- Use Cloud KMS customer-managed encryption keys (CMEK)
- Enable encryption in transit using TLS 1.2+ only
- Implement IAM with least privilege using predefined and custom roles
- Enable Organization Policy constraints for guardrails
- Use VPC Service Controls for data exfiltration prevention
- Enable Security Command Center for threat detection
- Block public access on Cloud Storage buckets (public_access_prevention = "enforced", uniform_bucket_level_access = true)
- Enable object versioning on Cloud Storage buckets
- Use Workload Identity Federation for GKE and for external workloads (CI/CD, other clouds)
- Never create service account keys; enforce iam.disableServiceAccountKeyCreation
- Do not grant basic roles (Owner, Editor) and disable automatic Editor grants to default service accounts

**Network Security:**
- Deploy resources in private VPC networks
- Use Cloud NAT for outbound internet access from private instances
- Implement firewall rules with explicit allow and deny rules
- Enable VPC Flow Logs for network monitoring
- Use Private Google Access for accessing Google APIs
- Configure Cloud Armor for DDoS protection and WAF
- Use Private Service Connect for accessing Google services
- Enable Cloud DNS logging and DNSSEC

**Compliance Requirements:**
- Label all resources with environment, owner, cost-center, data-classification
- Enable Cloud Audit Logs (admin, data access, system events)
- Configure log retention in Cloud Logging (minimum 90 days)
- Use Cloud Asset Inventory for resource tracking
- Implement automated backup using Cloud Scheduler and snapshots
- Enable Binary Authorization for container image verification
- Store images in Artifact Registry (Container Registry is shut down)
- Use Sensitive Data Protection (formerly Cloud DLP) for sensitive data discovery

**Code Quality:**
- Use terraform fmt for formatting
- Include variable validation and type constraints
- Pin google and google-beta provider versions and commit .terraform.lock.hcl
- Add meaningful descriptions to all resources
- Output security-relevant resource IDs and names
- Use data sources to reference existing projects and networks
- Separate state files per environment

Generate production-ready Terraform code following the latest CIS Google Cloud Platform Foundation Benchmark (v5.0.0 as of 2026).
