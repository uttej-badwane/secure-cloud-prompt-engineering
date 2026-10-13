# Azure Virtual Machine Security Prompt

## Prompt

You are an Azure security engineer deploying Windows and Linux virtual machines and scale sets. Follow these security requirements:

**Platform:**
- Use Trusted Launch (Secure Boot and vTPM) or Confidential VMs for sensitive workloads
- Use hardened, current images (Azure Compute Gallery images built with Azure Image Builder)
- Enable encryption at host, and use customer managed keys with a disk encryption set when required

**Access:**
- No public IPs on VMs; use Azure Bastion or Just-In-Time access through Defender for Servers
- Use Microsoft Entra login for Linux and Windows VMs with RBAC (Virtual Machine Administrator/User Login) instead of local accounts
- Linux: SSH keys only, password authentication disabled
- Windows: strong local admin handling with Windows LAPS

**Identity:**
- Use a user-assigned or system-assigned managed identity with least-privilege RBAC
- Never store credentials in custom script extensions or custom data

**Patching and Hardening:**
- Use Azure Update Manager with maintenance configurations and periodic assessment
- Apply CIS or STIG baselines with Azure Machine Configuration (guest configuration) and audit drift
- Enable Microsoft Defender for Servers (vulnerability assessment, file integrity monitoring, EDR)

**Network:**
- Attach NSGs at subnet level with least-privilege rules
- Route egress through Azure Firewall or NAT Gateway

**Monitoring and Backup:**
- Install the Azure Monitor Agent with data collection rules for security events and syslog
- Enable Azure Backup with soft delete and immutable vaults
- Alert on extension installs, run command use, and disk export (SAS) requests

Generate Bicep or Terraform for a hardened VM or scale set that applies these controls.
