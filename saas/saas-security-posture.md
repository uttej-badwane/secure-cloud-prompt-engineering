# SaaS Security Posture Management Prompt

## Prompt

You are a security engineer running a SaaS security program across apps like Salesforce, Snowflake, Slack, Atlassian, ServiceNow, Workday, and Zoom. Many recent breaches started in SaaS: stolen credentials on accounts without MFA (the 2024 Snowflake customer breaches) and stolen OAuth tokens from a connected third-party app (the 2025 Salesloft Drift incident). Follow these requirements:

**Inventory:**
- Discover all SaaS apps in use through SSO, expense data, OAuth grants, and browser or network telemetry
- Record owner, data handled, users, admins, and integrations for each app

**Access:**
- Put every app behind SSO and turn off local logins, except break-glass accounts with MFA
- Require MFA in the app itself where SSO can be bypassed
- Use SCIM so leavers lose access automatically
- Review admins in each app every quarter

**Integrations:**
- Inventory OAuth apps, API tokens, and service accounts connected to each SaaS app
- Reduce scopes, set token expiry, and restrict by IP where the app supports it
- Remove integrations that are unused or owned by departed staff
- Have a plan to revoke all tokens for a vendor quickly after a vendor breach

**Configuration:**
- Define a baseline per critical app (for example: Salesforce guest user access, Snowflake network policies and MFA, Slack external sharing)
- Use an SSPM tool or vendor health checks to detect drift

**Data:**
- Limit exports and public sharing; turn on vendor DLP features for sensitive data
- Know which apps hold regulated data

**Logging:**
- Collect admin and access logs from critical apps into the SIEM
- Alert on mass exports, new integrations, admin changes, and logins from unusual locations

**Vendor Risk:**
- Review security terms, SOC 2 reports, breach notification terms, and data residency for apps that hold sensitive data

Generate a SaaS inventory template, a baseline for the apps I list, and detection rules for SaaS abuse.
