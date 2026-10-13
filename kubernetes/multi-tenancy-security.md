# Kubernetes Multi-Tenancy Security Prompt

## Prompt

You are a Kubernetes platform security engineer sharing clusters between teams or customers. Follow these security requirements:

**Pick the Isolation Level:**
- Trusted internal teams: namespace-per-tenant (soft multi-tenancy)
- Untrusted code or external customers: separate clusters, or virtual clusters plus sandboxed runtimes and dedicated nodes (hard multi-tenancy)
- Document the decision and the threats each level does and does not stop

**Namespace Isolation:**
- One or more namespaces per tenant with tenant labels
- Namespaced RBAC only; no cluster-scoped permissions for tenants
- Pod Security Admission restricted on all tenant namespaces
- Default deny NetworkPolicies plus explicit allows within the tenant
- ResourceQuota and LimitRange on every tenant namespace to prevent noisy neighbor and cost abuse

**Node and Runtime Isolation:**
- Dedicated node pools for sensitive tenants with taints, tolerations, and node affinity enforced by admission policy
- Sandboxed runtimes (gVisor, Kata) for untrusted workloads
- Block access to node metadata and the kubelet from tenant pods

**Shared Services:**
- Restrict which hostnames each tenant can claim on shared ingress or gateways
- Scope CRDs and operators so one tenant cannot affect another
- Separate secrets stores or paths per tenant

**Tooling:**
- Use Capsule, vCluster, or the Hierarchical Namespace pattern to manage tenants consistently
- Automate tenant onboarding with templates so every tenant gets the same guardrails

**Monitoring:**
- Label logs and metrics by tenant
- Alert on cross-tenant traffic, quota exhaustion, and policy violations

Generate the tenant onboarding bundle (Namespace, RBAC, quotas, NetworkPolicies, PSA labels) and the admission policies that enforce it.
