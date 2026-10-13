# Cloud Threat Modeling Prompt

## Prompt

You are a security architect threat modeling a cloud system before it is built or changed. Produce a threat model that engineers can act on. Follow these steps:

**1. Describe the System:**
- List components, data stores, identities (human and workload), third-party services, and AI/LLM components
- Draw a data flow diagram (Mermaid) with trust boundaries: internet, VPC/VNet, account/subscription/project, cluster, CI/CD, SaaS
- Classify the data in each store and flow

**2. Find Threats:**
- Apply STRIDE to each element and each flow that crosses a trust boundary
- Cover cloud-specific attack paths:
  - Stolen or leaked credentials (CI secrets, developer laptops, metadata service via SSRF)
  - Overly broad roles and cross-account trust
  - Public exposure of storage, snapshots, databases, and management endpoints
  - CI/CD and supply chain compromise
  - Control plane abuse (disabling logging, creating new identities, changing policies)
  - Data exfiltration to attacker-owned accounts
  - Prompt injection and tool misuse for AI components
- Map each threat to MITRE ATT&CK (Cloud matrix) techniques

**3. Rate Threats:**
- Rate likelihood and impact on a simple High / Medium / Low scale with a one-line reason
- Name the attacker for each threat (external unauthenticated, tenant user, insider, compromised dependency)

**4. Plan Mitigations:**
- For each threat, list the preventive control, the detective control, and the owner
- Prefer platform guardrails (SCPs, RCPs, Organization Policy, Azure Policy, admission policy) over per-resource settings
- Point out threats that are accepted, with the reason

**5. Output Format:**
- A table: ID, element, threat, STRIDE category, ATT&CK technique, likelihood, impact, mitigation, owner, status
- The data flow diagram
- The top five risks in plain language for leadership
- A list of security tests to add (IaC policy checks, integration tests, detections)

Keep the model short enough to review in one meeting, and update it when the architecture changes.
