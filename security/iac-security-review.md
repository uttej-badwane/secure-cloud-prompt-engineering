# Infrastructure as Code Security Review Prompt

## Prompt

You are conducting a security review of Infrastructure as Code. Perform a comprehensive security assessment:

**Authentication & Authorization:**
- Check for overly permissive IAM/RBAC policies
- Verify least privilege principles are applied
- Identify use of wildcard permissions
- Review service account and role assignments
- Check for hardcoded credentials or API keys

**Data Protection:**
- Verify encryption at rest is enabled for all data stores
- Confirm encryption in transit (TLS 1.2+ only)
- Check for proper key management (KMS/HSM usage)
- Review data classification and handling
- Validate backup and recovery configurations

**Network Security:**
- Identify publicly exposed resources
- Review security group and firewall rules
- Check for unnecessary open ports
- Verify network segmentation and isolation
- Review VPN and private connectivity configurations

**Compliance & Governance:**
- Check for required tagging and labeling
- Verify logging and monitoring are enabled
- Review audit trail configurations
- Validate compliance with frameworks (CIS, NIST, PCI-DSS)
- Check for proper resource lifecycle management

**Vulnerability Assessment:**
- Identify outdated versions and deprecated resources
- Check for known CVEs in dependencies
- Review container image security
- Assess supply chain security risks

**Output Format:**
Provide findings categorized by severity (Critical, High, Medium, Low) with:
1. Issue description and location
2. Security impact
3. Remediation recommendation with code example

Follow OWASP IaC Security practices and provide actionable remediation guidance.
