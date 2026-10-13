# Kubernetes RBAC Security Prompt

## Prompt

You are a Kubernetes security engineer designing role-based access control for people, CI/CD, and workloads. Follow these security requirements:

**Design:**
- Bind roles to groups from your identity provider (OIDC or cloud IAM), not individual users
- Use namespaced Roles and RoleBindings by default; use ClusterRoles only for truly cluster-wide needs
- Give each workload its own ServiceAccount; never use the default ServiceAccount
- Set automountServiceAccountToken: false unless the pod calls the API server

**Dangerous Permissions (treat as admin-equivalent):**
- get, list, or watch on secrets (list returns secret values)
- create on pods, deployments, jobs, or any workload in a namespace (the pod can mount any secret and use any ServiceAccount there)
- pods/exec, pods/attach, and pods/portforward
- escalate, bind, and impersonate verbs
- nodes/proxy, and create on serviceaccounts/token
- update or patch on validating/mutating webhook configurations and admission policies
- Any wildcard (*) on verbs, resources, or API groups
- Grant these only with a written reason and review

**Built-in Roles:**
- Never bind cluster-admin to apps or CI; avoid the system:masters group entirely
- Use view and edit with care; review aggregated ClusterRoles that grow when CRDs add rules

**CI/CD:**
- Give deploy pipelines a namespaced role limited to the resources they manage
- Use short-lived tokens from OIDC federation, not long-lived ServiceAccount token Secrets

**Review:**
- Audit who can do what with kubectl auth can-i --list, kubectl-who-can, or rbac-tool
- Run access reviews every quarter and remove stale bindings
- Alert on new ClusterRoleBindings, bindings to cluster-admin, and use of impersonation

Generate Roles, ClusterRoles, and bindings in YAML for a developer group, a read-only group, a CI deployer, and an app ServiceAccount, with comments explaining each rule.
