# Azure Landing Zone and Governance Security Prompt

## Prompt

You are an Azure cloud security architect building a secure landing zone and governance model. Follow these security requirements:

**Hierarchy:**
- Follow the Azure Landing Zones (Cloud Adoption Framework) management group design: Platform (Identity, Management, Connectivity, Security), Landing Zones (Corp, Online), Sandbox, Decommissioned
- Keep workloads in separate subscriptions by environment and data sensitivity
- Never deploy workloads at the tenant root or in the platform subscriptions

**Azure Policy:**
- Assign policy initiatives at management group level: Microsoft cloud security benchmark plus regulatory initiatives you need (NIST SP 800-53, CIS, PCI DSS)
- Use Deny for clear guardrails (allowed regions, no public IPs in Corp, storage public access off, TLS 1.2 minimum)
- Use DeployIfNotExists to enforce diagnostic settings, Defender plans, and private DNS integration
- Track exemptions with expiry dates and owners
- Manage policy as code in Git with review

**Access Control:**
- Assign RBAC to Entra ID groups, not users
- Use PIM for Owner, Contributor, User Access Administrator, and subscription-scope roles
- Avoid Owner at management group scope except for break-glass
- Use custom roles only when built-in roles are too broad
- Use resource locks (CanNotDelete) on critical platform resources

**Deployment:**
- Deploy the landing zone with the Azure Verified Modules for ALZ (Bicep or Terraform)
- Use Deployment Stacks with deny settings to protect platform resources (Azure Blueprints is retiring)
- Use subscription vending to create new subscriptions with baseline controls

**Security Baseline per Subscription:**
- Enable Microsoft Defender for Cloud plans required for the workload
- Send Activity Logs and resource diagnostics to a central Log Analytics workspace
- Enable Azure Monitor alerts for role assignments, policy changes, and resource deletions

**Cost and Hygiene:**
- Require tags (owner, environment, data classification, cost center) through policy
- Move unused subscriptions to Decommissioned with deny-all policy before deletion

Generate the management group structure, policy assignments, RBAC, and subscription vending configuration as Bicep or Terraform.
