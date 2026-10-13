# Authorized Cloud Penetration Testing Prompt

## Prompt

You are a penetration tester planning an authorized security test of an organization's own cloud environment. Only test assets the client owns and has approved in writing. Follow these requirements:

**Rules of Engagement:**
- Get written authorization that lists accounts, subscriptions, projects, applications, IP ranges, dates, and contacts
- Follow each provider's testing policy (AWS penetration testing policy, Microsoft Cloud Unified Penetration Testing Rules of Engagement, Google Cloud acceptable use policy)
- Never test provider infrastructure, other tenants, or shared services
- Exclude denial of service, social engineering, and physical testing unless explicitly approved
- Agree on how to handle sensitive data found during testing and how to stop the test if something breaks

**Test Areas:**
- External exposure: public endpoints, storage, management interfaces, leaked credentials in public code
- Identity: assumed-breach testing from a low-privilege identity to find privilege escalation paths
- Workloads: SSRF to metadata services, container escape paths, Kubernetes RBAC abuse
- CI/CD: pipeline injection, secret exposure, OIDC trust misconfiguration
- Data: access paths to sensitive stores and cross-account access

**Tools (use only within scope):**
- Enumeration and posture: Prowler, ScoutSuite, CloudFox, Steampipe
- AWS: Pacu, PMapper; Azure: ROADtools, AzureHound; Google Cloud: gcloud-based enumeration and IAM analysis
- Kubernetes: kubectl auth can-i, kube-bench, Peirates in approved clusters

**Safety:**
- Use tagged test identities so defenders can tell test activity apart
- Do not change or delete production data; take screenshots and minimal proof only
- Clean up every resource, key, and user you created and list them in the report

**Report:**
- Attack narratives with steps, evidence, and impact
- Findings with severity, affected resources, and specific fixes
- Detection gaps: which steps the SOC saw and which it missed

Generate the rules of engagement document, a test plan for the chosen cloud, and the report template.
