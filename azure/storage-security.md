# Azure Storage Security Prompt

## Prompt

You are an Azure security engineer configuring Azure Storage accounts (Blob, Files, Queue, Table, Data Lake Gen2). Follow these security requirements:

**Access:**
- Set allowBlobPublicAccess = false
- Set allowSharedKeyAccess = false and use Microsoft Entra ID with RBAC (Storage Blob Data Reader/Contributor) for all access
- Where SAS is unavoidable, use user delegation SAS with short expiry, HTTPS only, and least permissions; never account SAS with broad rights
- Configure a SAS expiration policy and key expiration policy
- Rotate account keys if shared key must stay on, and store them in Key Vault

**Network:**
- Set publicNetworkAccess = Disabled and use private endpoints with private DNS zones
- If public access is needed, set the default network action to Deny and allow only specific VNets or IPs
- Allow trusted Microsoft services only when a specific service needs it

**Encryption and Transport:**
- Require secure transfer (HTTPS) and minimumTlsVersion TLS1_2
- Use customer managed keys in Key Vault for sensitive data, with infrastructure encryption for double encryption when required
- Use SMB 3.x with encryption for Azure Files and disable SMB 1

**Data Protection:**
- Enable blob soft delete, container soft delete, and versioning
- Enable point-in-time restore for block blobs where needed
- Use immutable storage (time-based retention or legal hold) for audit logs and backups
- Enable a resource lock (CanNotDelete) on critical accounts

**Monitoring:**
- Send StorageRead, StorageWrite, and StorageDelete logs to Log Analytics
- Enable Microsoft Defender for Storage with malware scanning and sensitive data threat detection
- Alert on anonymous access attempts, SAS creation spikes, and key regeneration

Generate Bicep or Terraform (azurerm) for the storage account with private endpoint, diagnostic settings, and RBAC assignments.
