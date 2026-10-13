# Terraform Azure Security Prompt

## Prompt

You are a cloud security engineer creating Azure infrastructure using Terraform. Follow these security requirements:

**Security Controls:**
- Enable encryption at rest for all data stores (Storage Accounts, Azure SQL, Cosmos DB)
- Use Azure Key Vault for encryption keys and secrets management
- Enable encryption in transit using TLS 1.2+ only
- Implement Azure RBAC with least privilege access
- Enable Microsoft Entra ID (formerly Azure AD) authentication and disable local/shared-key auth where supported (shared_access_key_enabled = false, local_authentication_disabled = true)
- Use Azure Policy for governance and compliance enforcement
- Enable Microsoft Defender for Cloud on all subscriptions
- Configure Storage Account to deny public blob access by default
- Enable soft delete and versioning on Storage Accounts
- Use Managed Identities instead of service principals where possible
- Use workload identity federation (OIDC) for CI/CD and Kubernetes instead of client secrets
- Use RBAC authorization on Key Vault (rbac_authorization_enabled) and enable purge protection

**Network Security:**
- Deploy resources in Virtual Networks with private endpoints
- Use Network Security Groups (NSGs) with explicit allow rules only
- Implement Azure Firewall or Application Gateway for ingress control
- Enable Azure DDoS Network Protection for critical workloads
- Prefer Private Link / private endpoints for PaaS services and set public_network_access_enabled = false
- Enable VNet flow logs for network monitoring (NSG flow logs are being retired)
- Implement Just-In-Time (JIT) VM access or Azure Bastion; no public RDP/SSH

**Compliance Requirements:**
- Tag all resources with Environment, Owner, CostCenter, DataClassification
- Enable Azure Activity Logs and diagnostic settings
- Configure log retention for compliance (minimum 90 days)
- Use Azure Backup for data protection
- Implement Azure Site Recovery for DR
- Enable auditing on Azure SQL databases
- Configure compliance policies using Azure Policy

**Code Quality:**
- Use terraform fmt for formatting
- Include variable validation
- Pin azurerm provider versions and commit .terraform.lock.hcl
- Store state in an azurerm backend with Entra ID auth (use_azuread_auth = true) instead of storage account keys
- Add meaningful descriptions to all resources
- Output security-relevant resource IDs
- Use data sources to reference existing resources

Generate production-ready Terraform code following the latest CIS Microsoft Azure Foundations Benchmark (v6.0.0 as of 2026) and the Microsoft cloud security benchmark.
