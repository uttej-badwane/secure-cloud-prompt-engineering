# Cloud Audit Logging Baseline Prompt

## Prompt

You are a cloud security engineer defining the minimum logging baseline across AWS, Azure, and Google Cloud so incidents can be detected and investigated. Follow these requirements:

**AWS:**
- Organization CloudTrail trail for all Regions with log file validation, KMS encryption, and delivery to a locked bucket in the log archive account
- CloudTrail data events for sensitive S3 buckets, Lambda, and DynamoDB tables
- VPC Flow Logs, Route 53 Resolver query logs, ELB, CloudFront, and WAF logs
- AWS Config in all accounts and Regions
- EKS control plane audit logs

**Azure:**
- Activity Logs from every subscription, Entra ID sign-in, audit, and Graph activity logs
- Resource diagnostic logs for Key Vault, Storage, SQL, Firewall, WAF, and AKS (kube-audit)
- VNet flow logs
- Microsoft Defender XDR and Defender for Cloud alerts

**Google Cloud:**
- Organization-level aggregated sink including Admin Activity, Data Access (for sensitive services), System Event, and Policy Denied logs
- VPC Flow Logs, Cloud DNS logs, firewall rules logs, and load balancer logs
- GKE audit logs and Security Command Center findings

**Cross-Cutting:**
- Identity provider logs (Okta, Entra ID, Google Workspace)
- Source control and CI/CD audit logs (GitHub, GitLab, Azure DevOps)
- SaaS admin audit logs

**Protection:**
- Store logs in a separate account, subscription, or project that workload admins cannot change
- Use immutability and retention locks; keep audit logs at least one year (longer where regulated)
- Alert when any log source stops sending or logging settings change

**Format and Cost:**
- Normalize to a common schema (OCSF or your SIEM's schema) for correlation
- Use tiered storage: hot for recent searchable data, cheap archive for long retention

Generate Terraform for the logging baseline on the chosen cloud, a log source inventory table, and alerts for log tampering.
