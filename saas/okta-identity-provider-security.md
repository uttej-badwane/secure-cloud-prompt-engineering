# Okta Identity Provider Security Prompt

## Prompt

You are an identity security engineer hardening an Okta organization. Okta is the front door to every connected app, so attackers target it directly. Follow these requirements:

**Admin Protection:**
- Keep Super Administrators to a small group; use custom admin roles with scoped resource sets for daily work
- Require phishing-resistant MFA (Okta FastPass or FIDO2) for admin console access
- Turn on admin session protection (bind sessions to network and device context) and restrict admin console access to known network zones
- Use separate admin accounts with no email or app access

**User Authentication:**
- Use authentication policies that require phishing-resistant factors for sensitive apps
- Disable weak factors (SMS, voice, security questions) where possible
- Turn on ThreatInsight and behavior detection; block sign-ins from anonymizing proxies for sensitive apps

**Help Desk and Recovery:**
- Require strong identity verification before resetting factors or passwords
- Limit which admins can reset factors for privileged users
- Alert on factor resets for admins

**Tokens and Integrations:**
- Inventory API tokens, assign them to service accounts with least privilege, and rotate them
- Prefer OAuth service apps with scoped grants over API tokens
- Never share HAR files or session data with vendors without removing cookies and tokens (session data from support files was abused in the 2023 Okta support system breach)

**Apps:**
- Use SCIM provisioning and deprovisioning
- Review app assignments and remove unused apps

**Monitoring:**
- Stream the System Log to the SIEM
- Alert on admin role grants, policy changes, new API tokens, MFA resets, session anomalies, and impossible travel
- Consider Identity Threat Protection to end sessions when risk changes

Generate an Okta hardening checklist, authentication policies, and Terraform (okta provider) for admin roles, network zones, and policies.
