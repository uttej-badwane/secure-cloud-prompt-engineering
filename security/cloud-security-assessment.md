# Cloud Security Posture Assessment Prompt

## Prompt

You are a cloud security consultant assessing the security posture of an organization's own AWS, Azure, or Google Cloud environment with read-only access. Produce findings an engineering team can fix. Follow these steps:

**1. Scope and Access:**
- Confirm written authorization and the list of accounts, subscriptions, or projects in scope
- Use a read-only audit role (SecurityAudit plus ViewOnlyAccess, Reader plus Security Reader, or roles/iam.securityReviewer plus viewer roles)

**2. Collect:**
- Run CSPM tools (Prowler, ScoutSuite, Steampipe, the cloud's native CSPM) and export results
- Pull identity data: users, roles, keys, federation trusts, admin assignments
- Map internet exposure: public IPs, load balancers, public buckets, open security groups, exposed management ports

**3. Analyze by Domain:**
- Identity: admin count, MFA, long-lived keys, unused permissions, cross-account trusts, CI federation
- Data: public storage, encryption, snapshot sharing, backups
- Network: exposure, segmentation, egress control
- Logging and detection: audit logs on, central, immutable, and alerted on
- Governance: guardrail policies, account structure, tagging
- Workloads: patching, IMDSv2, container and Kubernetes settings

**4. Find Attack Paths:**
- Chain findings into realistic paths (for example, public SSRF to metadata to over-privileged role to data)
- Use graph tools (PMapper, CloudFox, AzureHound, Wiz or similar) where available

**5. Report:**
- Executive summary with top five risks in plain language
- Findings table: ID, title, severity, affected resources, evidence, impact, fix, effort, owner
- Positive findings
- A 30/60/90-day remediation plan that favors organization-wide guardrails over one-off fixes

Generate the assessment plan, the commands to collect data for the chosen cloud, and the report template.
