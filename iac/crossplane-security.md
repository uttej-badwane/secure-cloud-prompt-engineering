# Crossplane Security Prompt

## Prompt

You are a platform security engineer building a cloud control plane with Crossplane. Crossplane providers hold credentials that can create and delete cloud resources, so the cluster running Crossplane is tier zero. Follow these security requirements:

**Provider Credentials:**
- Use workload identity (IRSA or EKS Pod Identity, Azure Workload ID, GKE Workload Identity) for providers, not static keys in Secrets
- Give each provider its own identity with least privilege, using DeploymentRuntimeConfig to set the service account
- Use multiple ProviderConfigs to separate environments and accounts, and restrict which claims can reference each one

**Compositions and APIs:**
- Expose only the fields app teams need in your CompositeResourceDefinitions (XRDs)
- Do not patch user input straight into sensitive fields such as IAM policies, security groups, or public access settings; set secure values in the composition
- Validate inputs with OpenAPI schemas and CEL validation rules on XRDs
- Keep compositions in Git with review and tests

**Kubernetes Access:**
- Let app teams create only namespaced claims; restrict cluster-scoped composite resources and managed resources to the platform team
- Restrict who can create or edit ProviderConfigs, Compositions, and Functions

**Packages:**
- Install providers, functions, and configurations from trusted registries and pin by digest
- Verify package signatures where supported
- Update providers on a schedule

**Safety:**
- Use deletionPolicy: Orphan and management policies for critical resources so deleting a claim does not destroy data
- Run the Crossplane control plane cluster with the same hardening as any tier-zero cluster

Generate an XRD, a Composition with secure defaults, a DeploymentRuntimeConfig with workload identity, and RBAC for app teams.
