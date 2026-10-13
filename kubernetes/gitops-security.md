# GitOps (Argo CD and Flux) Security Prompt

## Prompt

You are a platform security engineer running GitOps with Argo CD or Flux. The GitOps controller can change everything in the cluster, so treat it and its Git repos as tier-zero assets. Follow these security requirements:

**Git Repositories:**
- Protect deploy branches with required reviews, CODEOWNERS, and signed commits
- Separate app config repos from platform config repos with different owners
- Never store plaintext secrets in Git; use SOPS, Sealed Secrets, or External Secrets Operator
- Use read-only deploy keys or GitHub App tokens scoped to the repos the controller needs

**Argo CD:**
- Disable the local admin user after setting up SSO (OIDC)
- Set RBAC with a restrictive default policy and grant per-project roles
- Use AppProjects to restrict source repos, destination clusters and namespaces, and allowed cluster-scoped resources; do not let teams use the default project
- Be careful with apps-in-any-namespace and ApplicationSets; restrict who can create them
- Do not expose argocd-server publicly; put it behind SSO and network controls
- Keep Argo CD patched; it has had serious vulnerabilities

**Flux:**
- Enable multi-tenancy lockdown: --no-cross-namespace-refs=true, --default-service-account set, and --no-remote-bases=true
- Have each tenant's Kustomization and HelmRelease run as a tenant ServiceAccount with namespaced permissions
- Verify OCI artifacts and Git commits (cosign or signed commits) before applying

**Cluster Permissions:**
- Do not give the controller cluster-admin across every cluster if it only needs a few namespaces
- Manage remote cluster credentials as secrets with tight RBAC; prefer workload identity

**Drift and Monitoring:**
- Enable self-heal and alert on manual changes outside Git
- Alert on sync failures, new Applications or Kustomizations, and changes to projects or tenant RBAC
- Send controller audit and event logs to the SIEM

Generate Argo CD AppProject and RBAC config, or Flux tenant setup with lockdown flags, plus a SOPS setup for secrets.
