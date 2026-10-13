# Workforce SSO and MFA Prompt

## Prompt

You are an identity security engineer rolling out single sign-on and strong authentication for employees and contractors across cloud consoles, SaaS, and internal apps. Follow these requirements:

**Identity Provider:**
- Use one primary identity provider (Microsoft Entra ID, Okta, Google Workspace, Ping, or similar) as the source of truth
- Provision and deprovision accounts automatically from HR with SCIM
- Remove access within hours of termination, including sessions and tokens

**Authentication:**
- Require phishing-resistant MFA (FIDO2 security keys, passkeys, platform authenticators) for admins and high-risk roles, and move all users there over time
- Disable SMS and voice where possible; block MFA fatigue with number matching
- Protect help desk flows: verify identity strongly before resetting MFA or passwords (attackers target help desks)

**SSO Coverage:**
- Connect AWS (IAM Identity Center), Azure, Google Cloud, GitHub, and SaaS apps to SSO with SAML or OIDC
- Turn off local passwords in apps once SSO works, except break-glass accounts
- Find apps outside SSO through SaaS discovery and bring them in

**Access Policies:**
- Use group-based access with least privilege and access reviews every quarter
- Require managed devices for sensitive apps
- Set session lifetimes by risk

**Protect the IdP:**
- Keep IdP admin roles small, JIT, and on phishing-resistant MFA
- Review IdP admin actions, new apps, and policy changes daily with alerts
- Stream IdP logs to the SIEM and detect session hijacking and token replay

Generate an SSO rollout plan, authentication policies for the chosen IdP, and SCIM provisioning setup for AWS IAM Identity Center and GitHub.
