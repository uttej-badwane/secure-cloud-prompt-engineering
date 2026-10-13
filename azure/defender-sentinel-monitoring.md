# Azure Defender for Cloud and Sentinel Monitoring Prompt

## Prompt

You are an Azure security operations engineer setting up posture management, threat detection, and SIEM with Microsoft Defender for Cloud and Microsoft Sentinel. Follow these security requirements:

**Defender for Cloud:**
- Enable foundational CSPM everywhere and Defender CSPM for attack path analysis on production
- Enable workload plans that match your resources: Servers, Storage, SQL, Containers, Key Vault, App Service, Resource Manager, APIs, AI services
- Assign the Microsoft cloud security benchmark and any regulatory standards you need
- Connect AWS and GCP accounts if you run multi-cloud
- Route recommendations to owners with governance rules and due dates

**Log Collection:**
- Use a central Log Analytics workspace (or a few, by data residency) in the management subscription
- Send Activity Logs from every subscription with diagnostic settings enforced by Azure Policy
- Collect Entra ID sign-in, audit, and Graph activity logs
- Collect Defender XDR, Azure Firewall, WAF, Key Vault, and Storage logs
- Use data collection rules to filter noisy logs before ingestion

**Microsoft Sentinel:**
- Enable Sentinel on the central workspace and install content hub solutions for your sources
- Turn on analytics rules for identity attacks, privilege escalation, mass downloads, and policy changes
- Map rules to MITRE ATT&CK and tune false positives
- Use automation rules and playbooks (Logic Apps) for enrichment and containment, with human approval for destructive actions
- Manage analytics rules as code (Sentinel repositories) with review

**Access and Retention:**
- Use resource-context or table-level RBAC so teams see only their data
- Set retention per table and archive tier for long-term compliance
- Lock the workspace and diagnostic settings against deletion

**Health:**
- Monitor data connector health and alert when a source stops sending
- Review coverage against MITRE ATT&CK every quarter

Generate Bicep or Terraform for Defender plans, diagnostic policy assignments, the Sentinel workspace, and three example analytics rules in KQL.
