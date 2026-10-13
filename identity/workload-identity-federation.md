# Workload Identity Federation Security Prompt

## Prompt

You are a cloud security engineer replacing long-lived cloud keys with OIDC workload identity federation for CI/CD systems (GitHub Actions, GitLab CI, Terraform Cloud), Kubernetes, and cross-cloud workloads. A trust policy that is too broad lets any repository or tenant on the same platform assume your role. Follow these security requirements:

**Trust Policy Rules:**
- Always check the audience (aud) claim and the subject (sub) claim
- Pin sub to an exact repository plus branch, tag, or environment (repo:org/repo:environment:prod), never repo:org/* or *
- Prefer protected environments or protected branches as the subject for deploy roles
- Use immutable IDs (repository_id, repository_owner_id, project_id) through custom sub claim templates or extra conditions, so a renamed or re-created repo cannot inherit trust
- Use StringEquals, not StringLike, unless a wildcard is truly needed and reviewed
- Never trust pull request workflows from forks for roles that can write or deploy

**AWS:**
- Create an IAM OIDC provider for the issuer and condition on token.actions.githubusercontent.com:aud and :sub (or the GitLab equivalents)
- Use separate roles for plan (read-only) and apply (write); limit max session duration
- Add a permissions boundary to CI roles that can create IAM resources

**Azure:**
- Use federated identity credentials on a user-assigned managed identity or app registration with an exact subject match
- Assign RBAC at the narrowest scope (resource group, not subscription)
- Remove client secrets and certificates once federation works

**Google Cloud:**
- Create a Workload Identity Pool and Provider with an attribute_condition that restricts repository and owner
- Grant roles/iam.workloadIdentityUser on a specific service account to a specific principal or principalSet, not the whole pool
- Enforce iam.disableServiceAccountKeyCreation in the organization

**Kubernetes:**
- Use EKS Pod Identity or IRSA, AKS Workload Identity, or GKE Workload Identity Federation instead of node-level credentials
- Bind each Kubernetes ServiceAccount to its own cloud identity

**Detection:**
- Alert on AssumeRoleWithWebIdentity (or equivalent) from unexpected subjects, repositories, or IP ranges
- Inventory every federated trust and review it quarterly
- Scan IaC for wildcard sub claims and missing aud conditions in CI

Generate Terraform for the trust configuration on the chosen cloud, plus a matching CI workflow, and explain why each condition is required.
