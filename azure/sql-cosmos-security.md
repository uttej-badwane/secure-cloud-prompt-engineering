# Azure SQL and Cosmos DB Security Prompt

## Prompt

You are an Azure security engineer deploying Azure SQL Database, SQL Managed Instance, PostgreSQL/MySQL Flexible Server, and Cosmos DB. Follow these security requirements:

**Authentication:**
- Azure SQL: enable Microsoft Entra-only authentication and connect apps with managed identities
- PostgreSQL/MySQL Flexible Server: use Entra authentication and disable password auth where possible
- Cosmos DB: set disableLocalAuth = true and use Entra RBAC data-plane roles; set disableKeyBasedMetadataWriteAccess = true
- Grant database roles per application with least privilege

**Network:**
- Set publicNetworkAccess = Disabled and use private endpoints
- Never add the 0.0.0.0 "Allow Azure services" rule for sensitive databases
- Require TLS 1.2 minimum on all servers

**Encryption:**
- Use Transparent Data Encryption with customer managed keys in Key Vault for regulated data
- Use Always Encrypted for highly sensitive columns
- Use customer managed keys for Cosmos DB where required

**Data Protection:**
- Configure backup retention and long-term retention to match policy
- Use geo-redundant backup or replicas for disaster recovery
- Enable Cosmos DB continuous backup
- Apply resource locks to production servers

**Auditing and Threat Detection:**
- Enable auditing to a Log Analytics workspace or immutable storage
- Enable Microsoft Defender for SQL and Defender for Azure Cosmos DB
- Run vulnerability assessment and fix findings
- Use Microsoft Purview or SQL data discovery to classify sensitive data

**Application Safety:**
- Use parameterized queries only
- Use row-level security and dynamic data masking where they fit the threat model

Generate Bicep or Terraform for the database, private endpoint, Entra admin, auditing, and Defender settings.
