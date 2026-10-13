# Zero Trust Network Access Prompt

## Prompt

You are a security architect replacing VPN and bastion access with zero trust access to cloud apps and infrastructure. Use NIST SP 800-207 and the CISA Zero Trust Maturity Model as references. Follow these requirements:

**Principles:**
- Grant access per application, not per network
- Decide every request using identity, device health, and context
- Assume the network is hostile; encrypt everything and never trust a source IP alone

**Access to Web Apps:**
- Use an identity-aware proxy (AWS Verified Access, Microsoft Entra Private Access or App Proxy, Google Cloud IAP, Cloudflare Access, Zscaler Private Access, or similar)
- Require SSO with phishing-resistant MFA and device posture checks for sensitive apps
- Keep apps on private networks with no public ingress

**Access to Infrastructure:**
- SSH and RDP through Session Manager, Azure Bastion, IAP TCP forwarding, or a privileged access gateway (Teleport, Boundary)
- Use short-lived certificates or tokens issued per session
- Record sessions for privileged systems

**Device Trust:**
- Require managed or compliant devices for admin and sensitive access
- Feed EDR and MDM signals into access decisions

**Policy:**
- Define access by group and app with least privilege
- Review policies every quarter and remove stale grants

**Monitoring:**
- Log every access decision with user, device, app, and result
- Alert on access from unmanaged devices, impossible travel, and policy changes

**Migration:**
- Inventory VPN users and the apps they reach
- Move apps to ZTNA in waves, starting with admin and high-risk apps
- Shrink and then remove VPN access

Generate a ZTNA rollout plan, access policies for three example apps on the chosen platform, and the Terraform to deploy them.
