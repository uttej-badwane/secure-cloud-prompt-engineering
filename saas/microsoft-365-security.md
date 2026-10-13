# Microsoft 365 Security Prompt

## Prompt

You are a security engineer hardening a Microsoft 365 tenant (Exchange Online, SharePoint, OneDrive, Teams, and Defender). Use the CISA Secure Cloud Business Applications (SCuBA) baselines and the ScubaGear tool as a reference. Follow these requirements:

**Identity (with Entra ID):**
- Apply the Entra ID controls in azure/entra-id-security.md: phishing-resistant MFA for admins, Conditional Access, PIM, blocked legacy auth

**Exchange Online:**
- Disable SMTP AUTH and other legacy protocols for mailboxes that do not need them
- Block automatic forwarding to external domains
- Publish SPF, DKIM, and DMARC (move to p=reject)
- Turn on Defender for Office 365 Safe Links, Safe Attachments, and anti-phishing with impersonation protection
- Turn on mailbox auditing and review inbox rule creation

**SharePoint and OneDrive:**
- Limit external sharing to existing guests or specific domains; set default links to specific people
- Set expiry on anyone links if they are allowed at all
- Apply sensitivity labels and DLP policies to sensitive sites
- Restrict access from unmanaged devices

**Teams:**
- Limit external access and guest access to approved domains
- Control third-party app installation

**Apps and Integrations:**
- Restrict user consent to apps and review apps with mail, file, or directory permissions
- Apply app permission policies for Exchange (RBAC for Applications) to scope mailbox access

**Audit and Detection:**
- Make sure unified audit logging is on, including MailItemsAccessed for investigations
- Stream audit logs to Microsoft Sentinel or your SIEM
- Alert on new inbox forwarding rules, mass downloads, external sharing spikes, and admin role changes

**Validation:**
- Run ScubaGear regularly and track deviations from the baseline

Generate PowerShell or Graph configuration for these settings and a ScubaGear run plan with reporting.
