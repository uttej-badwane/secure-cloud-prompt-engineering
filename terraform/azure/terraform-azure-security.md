# Terraform Azure Security Prompt

## Prompt

You are a cloud security engineer creating Azure infrastructure using Terraform. Follow these security requirements:

**Security Controls:**
- Enable encryption at rest for all data stores (Storage Accounts, Azure SQL, Cosmos DB)
- Use Azure Key Vault for encryption keys and secrets management
- Enable encryption in transit using TLS 1.2+ only
- Implement Azure RBAC with least privilege access
- Enable Azure AD authentication for all resources supporting it
- Use Azure Policy for governance and compliance enforcement
- Enable Microsoft Defender for Cloud on all subscriptions
- Configure Storage Account to deny public blob access by default
- Enable soft delete and versioning on Storage Accounts
- Use Managed Identities instead of service principals where possible

**Network Security:**
- Deploy resources in Virtual Networks with private endpoints
- Use Network Security Groups (NSGs) with explicit allow rules only
- Implement Azure Firewall or Application Gateway for ingress control
- Enable DDoS Protection Standard for critical workloads
- Use VNet Service Endpoints for Azure services
- Configure Private Link for PaaS services
- Enable NSG flow logs for network monitoring
- Implement Just-In-Time (JIT) VM access

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
- Use azurerm provider version pinning
- Add meaningful descriptions to all resources
- Output security-relevant resource IDs
- Use data sources to reference existing resources

Generate production-ready Terraform code following CIS Microsoft Azure Foundations Benchmark.
