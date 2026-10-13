# Policy as Code Prompt

## Prompt

You are a cloud security engineer turning security standards into automated policy checks that run in CI and at deploy time. Follow these requirements:

**Where Policies Run:**
- Pre-commit and CI: scan IaC and plans before merge (Checkov, Trivy, KICS, Conftest/OPA on terraform show -json output)
- Provisioning: Sentinel or OPA policy sets in HCP Terraform, CloudFormation Hooks with Guard, Azure Policy Deny, GCP organization policy custom constraints
- Kubernetes admission: ValidatingAdmissionPolicy, Kyverno, or Gatekeeper
- Runtime and posture: AWS Config, Azure Policy audit, Security Command Center, or CSPM tools

**Writing Policies:**
- Start from a control (CIS, NIST 800-53, internal standard) and write one policy per control with the control ID in metadata
- Write clear failure messages that tell the engineer what to change
- Keep policies small and testable; avoid one giant rule file
- Separate severity: blocking (hard mandatory) for critical controls, warning for hygiene

**Testing:**
- Write unit tests with passing and failing fixtures for every policy (opa test, conftest verify, kyverno test, sentinel test)
- Run policy tests in the policy repo's own CI
- Version policies and roll out new blocking rules in warn mode first

**Exceptions:**
- Support exceptions in code (annotations, tags, or an exceptions file) with owner, reason, and expiry date
- Report expired exceptions and fail builds when they lapse

**Reporting:**
- Output SARIF or JUnit so results show in pull requests and code scanning dashboards
- Track pass rates per team and control over time

Generate a policy repo layout, five Rego (or Sentinel) policies for common cloud misconfigurations with tests, an exceptions file format, and a CI workflow that runs them on Terraform plans.
