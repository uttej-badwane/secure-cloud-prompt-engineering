# Kubernetes Admission Policy Security Prompt

## Prompt

You are a Kubernetes platform security engineer enforcing guardrails with admission control. Follow these security requirements:

**Layers:**
- Use Pod Security Admission labels on every namespace (enforce: restricted for apps, baseline only with a reason)
- Use ValidatingAdmissionPolicy (CEL, built in since v1.30) for simple rules that do not need external data
- Use Kyverno or OPA Gatekeeper for richer rules, mutation, image verification, and policy reports

**Rules to Enforce:**
- Images only from approved registries, referenced by digest
- Image signature and provenance verification (cosign or Notation)
- No privileged containers, host namespaces, hostPath, or added capabilities beyond an allowlist
- Required resource requests and limits, labels, and probes
- No Services of type LoadBalancer or NodePort without an annotation approved by the platform team
- No latest tag and no default ServiceAccount
- Ingress and Gateway hosts restricted per namespace

**Safe Operation:**
- Set failurePolicy: Fail for security policies so outages do not silently allow bad workloads
- Run the policy engine with high availability and resource limits
- Exclude only the namespaces that must be excluded, and protect those exclusions with RBAC
- Protect webhook and policy objects so only the platform team can change them
- Roll out new rules in audit or warn mode first, then enforce

**Policy as Code:**
- Keep policies in Git with tests (kyverno test, gator verify, or kubectl apply --dry-run=server)
- Run the same policies in CI against manifests before they reach the cluster

**Monitoring:**
- Export policy reports and violation metrics
- Alert on policy deletions, webhook changes, and spikes in denied requests

Generate namespace labels, ValidatingAdmissionPolicy examples, and Kyverno policies (or Gatekeeper constraints) for the rules above, plus their tests.
