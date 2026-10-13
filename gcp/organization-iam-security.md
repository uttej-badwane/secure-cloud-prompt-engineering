# Google Cloud Organization and IAM Security Prompt

## Prompt

You are a Google Cloud security architect setting up the organization, resource hierarchy, and IAM. Follow these security requirements:

**Resource Hierarchy:**
- Use an organization node tied to your Cloud Identity or Google Workspace domain
- Create folders by environment and business unit (for example: bootstrap, common, production, non-production, development)
- Keep security, logging, networking, and billing in dedicated projects
- Build the foundation with the Google Cloud security foundations blueprint (Terraform example foundation) or Fabric FAST

**Organization Policies:**
- Enforce at the organization or folder level:
  - iam.allowedPolicyMemberDomains (domain-restricted sharing)
  - iam.disableServiceAccountKeyCreation and iam.disableServiceAccountKeyUpload
  - iam.automaticIamGrantsForDefaultServiceAccounts
  - storage.publicAccessPrevention and storage.uniformBucketLevelAccess
  - compute.vmExternalIpAccess, compute.requireOsLogin, compute.requireShieldedVm, compute.skipDefaultNetworkCreation
  - sql.restrictPublicIp and gcp.resourceLocations
- Use dry-run mode before enforcing new constraints and custom constraints for gaps

**IAM:**
- Grant roles to Google Groups, not individual users
- Never use basic roles (Owner, Editor, Viewer) in production
- Grant at the lowest level of the hierarchy that works
- Use IAM Conditions for time-bound and resource-scoped access
- Use IAM deny policies to block high-risk permissions (for example, service account key creation) for everyone except break-glass
- Use Privileged Access Manager (PAM) for just-in-time elevation with approval
- Use the IAM recommender and Policy Analyzer to remove unused permissions

**Service Accounts:**
- One service account per workload, with only the roles it needs
- Use service account impersonation for humans and CI instead of keys
- Use Workload Identity Federation for workloads outside Google Cloud
- Disable or delete unused service accounts

**Admin Accounts:**
- Protect super admin accounts with security keys, keep at least two, and use them only for break-glass
- Enforce 2-Step Verification with security keys for privileged users in Cloud Identity
- Set session length controls for the Google Cloud console and gcloud

**Monitoring:**
- Use an organization-level aggregated log sink for Admin Activity and Policy Denied logs
- Alert on IAM policy changes at the organization and folder level, super admin logins, and org policy changes

Generate Terraform for the folder structure, organization policies, IAM bindings, and deny policies.
