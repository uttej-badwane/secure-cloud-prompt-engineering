# Infrastructure Security Checklist

## Pre-Deployment Security Checklist

### Identity & Access Management
- [ ] Least privilege IAM policies applied
- [ ] No hardcoded credentials in code
- [ ] Service accounts use minimal permissions
- [ ] Phishing-resistant MFA enabled for privileged accounts
- [ ] CI/CD uses OIDC federation, not long-lived cloud keys
- [ ] Regular access reviews scheduled

### Data Protection
- [ ] Encryption at rest enabled (AES-256)
- [ ] Encryption in transit enforced (TLS 1.2+)
- [ ] KMS customer-managed keys used
- [ ] Backup and recovery tested
- [ ] Data retention policies configured

### Network Security
- [ ] No unnecessary public exposure
- [ ] Security groups follow least privilege
- [ ] Network segmentation implemented
- [ ] VPC Flow Logs enabled
- [ ] DDoS protection configured

### Logging & Monitoring
- [ ] Centralized logging enabled
- [ ] CloudTrail/audit logs active
- [ ] Security alerting configured
- [ ] Log retention meets compliance
- [ ] SIEM integration completed

### Compliance & Governance
- [ ] Resources properly tagged
- [ ] Compliance controls validated
- [ ] Security scanning integrated
- [ ] Change management documented
- [ ] Incident response plan defined

### Container & Kubernetes
- [ ] Images scanned for vulnerabilities
- [ ] Non-root containers enforced
- [ ] Resource limits defined
- [ ] NetworkPolicies implemented
- [ ] Secrets externalized
- [ ] Pod Security Admission enforces the restricted profile
- [ ] Images signed and verified at admission

### Supply Chain
- [ ] Actions, images and modules pinned to SHA or digest
- [ ] SBOM and provenance generated for build artifacts
- [ ] Terraform lock file committed; secrets kept out of state

Use this checklist before deploying infrastructure to production environments.
