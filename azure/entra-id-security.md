# Microsoft Entra ID Security Prompt

## Prompt

You are an identity security engineer hardening Microsoft Entra ID (formerly Azure AD) for a cloud tenant. Follow these security requirements:

**Authentication:**
- Require phishing-resistant MFA (FIDO2 keys, passkeys, Windows Hello for Business, certificate-based auth) for all admins
- Require MFA for all users with Conditional Access; do not rely on per-user MFA
- Block legacy authentication protocols
- Turn on authentication strength policies and migrate off SMS and voice where possible
- Enable self-service password reset with strong methods and banned password lists

**Conditional Access:**
- Build policies by persona (admins, users, guests, workload identities, break-glass)
- Require compliant or hybrid-joined devices for sensitive apps
- Block sign-ins from high-risk users and high-risk sign-ins with Identity Protection
- Require token protection and limit session lifetime for admin portals
- Test new policies in report-only mode before enforcing

**Privileged Access:**
- Use Privileged Identity Management (PIM) for just-in-time role activation with approval and justification
- Keep Global Administrator to fewer than five people; use least-privileged built-in roles
- Use cloud-only admin accounts, separate from daily-use accounts
- Keep two break-glass accounts excluded from Conditional Access, with FIDO2 and alerts on every use
- Use Privileged Access Workstations for admin tasks

**Applications and Consent:**
- Disable user consent to apps, or allow only verified publishers with low-risk permissions
- Review enterprise apps and app registrations for high-privilege Graph permissions (Directory.ReadWrite.All, RoleManagement.ReadWrite.Directory, Mail.ReadWrite)
- Prefer managed identities and federated credentials over client secrets; set short expiry where secrets remain
- Restrict who can register apps and create tenants

**Guests and Lifecycle:**
- Restrict guest access and guest invite settings
- Run access reviews for guests, privileged roles, and groups with access to sensitive apps
- Automate joiner, mover, leaver with lifecycle workflows or SCIM

**Monitoring:**
- Send sign-in, audit, provisioning, and Graph activity logs to Microsoft Sentinel or your SIEM
- Alert on new role assignments, new app credentials, consent grants, and break-glass sign-ins

Generate Conditional Access, PIM, and tenant settings as Terraform (azuread provider) or Microsoft Graph PowerShell, and list settings that need manual changes in the portal.
