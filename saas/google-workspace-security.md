# Google Workspace Security Prompt

## Prompt

You are a security engineer hardening a Google Workspace tenant. Use the CISA SCuBA baselines for Google Workspace and the ScubaGoggles tool as a reference. Follow these requirements:

**Admin Accounts:**
- Keep super admins to a small break-glass set and use delegated admin roles for daily work
- Enforce security keys for all admins and enroll them in the Advanced Protection Program
- Do not use super admin accounts for email or daily browsing

**Authentication:**
- Enforce 2-Step Verification for all users, with security keys or passkeys for high-risk groups
- Turn on login challenges and suspicious login alerts
- Use context-aware access for sensitive apps (device and location conditions)

**Third-Party Apps:**
- Restrict OAuth app access in API controls; allow only reviewed apps and block high-risk scopes (Gmail, Drive full access) for unreviewed apps
- Review connected apps every quarter

**Gmail:**
- Publish SPF, DKIM, and DMARC; turn on enhanced pre-delivery scanning and attachment protections
- Block automatic forwarding to external addresses or require admin approval
- Disable less secure apps and POP/IMAP where not needed

**Drive:**
- Limit external sharing to allowlisted domains; warn on sharing outside
- Turn off "anyone with the link" for sensitive organizational units
- Use DLP rules and labels for sensitive data

**Devices:**
- Require endpoint management for access to company data on mobile and desktop

**Logging and Detection:**
- Export audit and activity logs to BigQuery or your SIEM
- Use the alert center and rules for suspicious logins, OAuth grants, external sharing spikes, and admin changes

**Validation:**
- Run ScubaGoggles regularly and track gaps

Generate the settings checklist by admin console area, OAuth app policy, and log export setup.
