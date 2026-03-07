# IaC Security Checks Reference

Consolidated security check criteria for the IaC Security Review skill.
Drawn from the repo's existing prompt library and pre-deployment checklists.

---

## Pre-Deployment Checklist

### Identity & Access Management
- [ ] Least privilege IAM policies applied — no wildcard `*` actions or resources
- [ ] No hardcoded credentials, API keys, or secrets in code or tfvars
- [ ] Service accounts use minimal permissions
- [ ] MFA enabled for privileged accounts
- [ ] Regular access reviews scheduled

### Data Protection
- [ ] Encryption at rest enabled (AES-256) for all data stores (S3, EBS, RDS, DynamoDB)
- [ ] Encryption in transit enforced (TLS 1.2+ only)
- [ ] KMS customer-managed keys (CMK) used instead of AWS-managed keys
- [ ] Proper key management configured (KMS/HSM)
- [ ] Data classification and handling reviewed
- [ ] Backup and recovery tested
- [ ] Data retention policies configured

### Network Security
- [ ] No unnecessary public exposure — resources in private subnets where possible
- [ ] Security groups follow least privilege (no `0.0.0.0/0` on sensitive ports)
- [ ] Network segmentation and VPC isolation implemented
- [ ] VPC Flow Logs enabled
- [ ] VPN and private connectivity configurations reviewed
- [ ] DDoS protection configured

### Logging & Monitoring
- [ ] Centralized logging enabled
- [ ] CloudTrail / audit logs active in all regions
- [ ] Security alerting configured
- [ ] Log retention meets compliance requirements
- [ ] GuardDuty or equivalent threat detection enabled

### Compliance & Governance
- [ ] Resources tagged with Owner, Environment, CostCenter, Compliance
- [ ] Compliance controls validated against applicable framework
- [ ] Security scanning integrated in CI/CD pipeline
- [ ] Change management documented
- [ ] Resource lifecycle management reviewed (deletion policies, expiry)
- [ ] Incident response plan defined

### Container & Kubernetes
- [ ] Images scanned for vulnerabilities (Trivy, Grype, Snyk)
- [ ] Non-root containers enforced (`runAsNonRoot: true`)
- [ ] CPU and memory resource limits defined
- [ ] NetworkPolicies implemented
- [ ] Secrets externalized (external secrets operator, Vault)

### Secret Management
- [ ] Secrets stored in dedicated services (AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, HashiCorp Vault)
- [ ] No secrets in code repositories, config files, or environment variables
- [ ] Secret rotation policies implemented (30–90 day rotation)
- [ ] Secrets injected at runtime, not build time
- [ ] Pre-commit hooks and secret scanning enabled (git-secrets, TruffleHog)
- [ ] Access logging enabled for all secret operations

### Vulnerability Assessment
- [ ] Outdated versions and deprecated resources identified
- [ ] Known CVEs in dependencies checked
- [ ] Container image security reviewed
- [ ] Supply chain security risks assessed
- [ ] OWASP IaC Security practices followed

---

## Terraform Security Checks

### Authentication & Authorization
- No hardcoded `aws_access_key_id` / `aws_secret_access_key` in `.tf` or `.tfvars`
- IAM policies scoped to specific actions and resources (no `*`)
- Service roles use `aws_iam_role` with least-privilege inline or managed policies
- `aws_iam_policy_attachment` preferred over direct `aws_iam_user_policy`

### Storage
- `aws_s3_bucket` → `block_public_acls`, `block_public_policy`, `ignore_public_acls`, `restrict_public_buckets` all `true`
- `aws_s3_bucket_server_side_encryption_configuration` configured with CMK
- `versioning { enabled = true }` on sensitive buckets
- `lifecycle_rule` with `prevent_destroy` on stateful resources

### Compute & Networking
- Security groups restrict ingress; avoid `cidr_blocks = ["0.0.0.0/0"]` on ports 22, 3389, 5432, 3306
- RDS instances: `storage_encrypted = true`, `multi_az = true`, no public endpoint
- EC2 instances: `ebs_optimized = true`, root volume encrypted, IMDSv2 enforced (`metadata_options { http_tokens = "required" }`)
- No `default` VPC usage; custom VPC with explicit subnets
- VPN and private connectivity reviewed; AWS PrivateLink or VPC endpoints for service access

### Observability
- `aws_cloudtrail` resource present with `is_multi_region_trail = true`, `enable_log_file_validation = true`
- `aws_guardduty_detector` enabled
- `aws_config_configuration_recorder` active

### State & Backend
- Backend configured with encryption and DynamoDB state locking
- Remote state not publicly accessible

---

## Kubernetes Security Checks

### Pod Security
- `securityContext.runAsNonRoot: true`
- `securityContext.readOnlyRootFilesystem: true`
- `securityContext.allowPrivilegeEscalation: false`
- `securityContext.capabilities.drop: ["ALL"]`
- No `privileged: true` without documented justification

### Resource Management
- `resources.requests` and `resources.limits` set for CPU and memory on all containers
- Pod Disruption Budgets defined for production workloads
- Liveness and readiness probes configured

### Networking
- NetworkPolicies restrict ingress/egress to required paths only
- Services do not expose `hostPort` without justification
- `hostNetwork: false`, `hostPID: false`, `hostIPC: false`

### Images
- No `latest` tag — use specific digest pinning (`image@sha256:...`)
- Images scanned before deployment; CI/CD gate blocks critical CVEs
- Images pulled from trusted private registry, not public Docker Hub by default

### Secrets
- No `Secret` objects with base64-encoded values committed to Git
- Use external secrets operator or Vault agent injection
- ServiceAccounts scoped minimally; no `cluster-admin` ClusterRoleBinding

---

## Dockerfile Security Checks

- `USER` instruction sets a non-root user before `CMD`/`ENTRYPOINT`
- Base image pinned to a specific digest or non-`latest` tag
- Multi-stage builds used to minimize final image size and attack surface
- `.dockerignore` present and excludes `.git`, `.env`, credentials
- No `ADD` from remote URLs — use `COPY` with verified downloads
- Secrets not passed via `ARG` or `ENV` at build time
- `HEALTHCHECK` instruction present
- Unnecessary packages not installed; `--no-install-recommends` used with apt

---

## CI/CD Security Checks (GitHub Actions / GitLab CI)

- Secrets accessed via `${{ secrets.NAME }}` / GitLab CI variables, never hardcoded
- `permissions:` block scoped to minimum required (avoid `write-all`)
- OIDC used for cloud authentication — no long-lived access keys in secrets
- Action versions pinned to SHA (`uses: actions/checkout@abc123...`)
- `pull_request_target` trigger does not check out untrusted PR code
- Branch protection rules enforced; required reviewers for main/prod
- Artifacts scanned for secrets before upload
- Pipeline fails on critical/high vulnerability findings
- Separate secrets used for dev/staging/production environments
- Temporary credentials used in CI/CD pipelines (short-lived tokens)

---

## CloudFormation Security Checks

- `DeletionPolicy: Retain` on stateful resources (RDS, S3, DynamoDB)
- Security groups restrict `0.0.0.0/0` ingress
- IAM roles use managed policies; avoid broad inline policies
- `AWS::CloudTrail::Trail` resource present
- All storage resources have encryption properties configured
- Stack policies defined to protect critical resources from update/delete
- VPN and private connectivity reviewed for inter-service communication

---

## Ansible Security Checks

- Passwords and keys stored in Ansible Vault, not in plaintext in playbooks
- `become: yes` scoped to specific tasks, not entire playbooks
- `shell` and `command` modules avoid user-controlled variables without sanitization
- `no_log: true` on tasks that handle secrets or sensitive output
- Package repositories use HTTPS URLs
- `ansible-lint` integrated in CI pipeline

---

## Secret Management Checks

These checks apply cross-cutting across all IaC types.

### Secret Storage
- Use dedicated secret management services: AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, or HashiCorp Vault
- Never store secrets in code repositories, config files, or environment variables
- Never commit `.env` files or credential files to version control
- Use encrypted secret stores with access auditing enabled
- Implement secret rotation policies (30–90 days); automate rotation where possible

### Access Control
- Apply least privilege access to secrets
- Use IAM roles and service accounts for programmatic authentication — not static credentials
- Enable MFA for human access to secret stores
- Implement time-bound access tokens
- Audit all secret access with CloudTrail or equivalent

### Secret Injection
- Inject secrets at runtime, not build time
- Use platform-native secret injection: ECS task secrets, Kubernetes secret volumes, GitHub Actions secrets
- Mount secrets as files rather than environment variables where supported
- Clear secrets from memory after use
- Use short-lived credentials (OIDC, STS, Workload Identity) when possible

### Development & CI/CD
- Use separate secrets for dev/staging/production environments
- Scan repositories for exposed secrets with git-secrets, TruffleHog, GitGuardian, or detect-secrets
- Implement pre-commit hooks to prevent accidental secret commits
- Use temporary credentials in CI/CD pipelines
- Rotate secrets immediately if exposure is detected or suspected

### Encryption
- Encrypt secrets at rest using KMS
- Encrypt secrets in transit using TLS
- Use envelope encryption for large secrets
- Implement and test key rotation policies

### Monitoring & Compliance
- Enable access logging for all secret operations
- Alert on unusual access patterns (unexpected principals, off-hours access)
- Implement secret sprawl detection — inventory all secrets and their owners
- Document secret ownership and lifecycle (creation, rotation, expiry, revocation)
- Conduct regular security audits of secret usage

---

## Vulnerability Assessment & Supply Chain Checks

### Dependency Scanning
- Scan lock files and manifests for known CVEs (npm audit, pip-audit, bundler-audit)
- Use Dependabot or Renovate for automated dependency update PRs
- Use OWASP Dependency-Check or Snyk for package vulnerability detection
- Monitor new vulnerabilities with WhiteSource/Mend or Sonatype Nexus IQ
- Fail CI builds on critical/high severity dependency vulnerabilities

### Static Application Security Testing (SAST)
- SonarQube for code quality and security analysis
- Semgrep for pattern-based security scanning (custom rules for IaC patterns)
- CodeQL for semantic code analysis
- Bandit for Python, GoSec for Go, FindSecBugs for Java, ESLint security plugins for JavaScript

### Dynamic Application Security Testing (DAST)
- OWASP ZAP or Burp Suite for web application scanning
- Nuclei for vulnerability scanning with community templates
- Nikto for web server configuration scanning
- Perform authenticated DAST scans against staging environments

### Supply Chain Security
- Identify outdated versions and deprecated resources (EOL runtimes, deprecated API versions)
- Pin all third-party dependencies to specific versions or SHA digests
- Verify integrity of downloaded artifacts (checksums, signatures)
- Review base image provenance and use distroless or minimal base images
- Assess software bill of materials (SBOM) for container images

### Vulnerability Management
- Prioritize findings by severity (CVSS score) and exploitability
- Implement SLA for remediation: Critical ≤ 24h, High ≤ 7d, Medium ≤ 30d, Low ≤ 90d
- Track vulnerability trends over time
- Implement exception and risk acceptance workflows with documented approvals
- Track mean time to remediate (MTTR) as a security metric
- Verify fixes with rescanning after remediation

### Reporting & Metrics
- Generate vulnerability reports in SARIF format for GitHub Security tab integration
- Create security scorecards and executive dashboards
- Track vulnerability density metrics (findings per 1000 lines of IaC)
- Monitor scanning coverage across all repositories and environments
- Generate compliance reports for audits

### Remediation Workflow
- Automatically create tickets (Jira, ServiceNow) for security findings
- Assign ownership based on code ownership (CODEOWNERS file)
- Implement automated patching where possible (Dependabot auto-merge for low-risk updates)
- Escalate stale vulnerabilities past SLA automatically
- Document accepted risks and exceptions with expiry dates

---

## Vulnerability Scanning Tools Reference

| Category | Recommended Tools |
|---|---|
| **IaC — Terraform** | tfsec, Checkov, Terrascan, KICS |
| **IaC — Kubernetes** | kube-score, Kubesec, kube-bench, Polaris |
| **IaC — Dockerfile** | Trivy, Grype, Hadolint, Snyk, Clair |
| **IaC — CloudFormation** | cfn_nag, Checkov |
| **IaC — GitHub Actions** | actionlint, StepSecurity |
| **IaC — General** | OPA/Conftest, Semgrep, KICS |
| **Secrets** | TruffleHog, git-secrets, GitGuardian, detect-secrets |
| **Cloud Posture** | Prowler (AWS), ScoutSuite (Azure/GCP), CloudSploit, Steampipe |
| **Cloud Native** | AWS Security Hub, Azure Defender, GCP Security Command Center |
| **Dependencies** | Dependabot, OWASP Dependency-Check, Snyk, npm audit, pip-audit |
| **SAST** | SonarQube, Semgrep, CodeQL, Bandit, GoSec, FindSecBugs |
| **DAST** | OWASP ZAP, Burp Suite, Nuclei, Nikto |
| **K8s Runtime** | Falco, kube-hunter, Popeye, OPA Gatekeeper |
| **Network** | Nmap, OpenVAS, Nessus, Qualys |
| **Compliance** | Prowler, Chef InSpec, AWS Config Rules, Azure Policy, GCP Org Policy |
| **SIEM Integration** | Jira, ServiceNow, Splunk, Elastic SIEM |
