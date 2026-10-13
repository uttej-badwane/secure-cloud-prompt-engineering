# AWS Security Services Setup Prompt

## Prompt

You are an AWS security engineer turning on and organizing AWS native security services across an AWS Organization. Follow these security requirements:

**Organization Setup:**
- Use a dedicated Security Tooling (Audit) account as the delegated administrator for each service
- Auto-enable services for all existing and new member accounts in all enabled Regions
- Deny member accounts from disabling these services with SCPs

**Threat Detection:**
- Enable Amazon GuardDuty with the protection plans you need: S3, EKS, Runtime Monitoring (EC2, ECS, EKS), Malware Protection, RDS, and Lambda
- Enable Extended Threat Detection and route findings to the incident response process
- Use suppression rules only with documented reasons

**Posture and Findings:**
- Enable AWS Security Hub for unified risk analysis, and Security Hub CSPM with the AWS Foundational Security Best Practices and CIS AWS Foundations Benchmark standards
- Aggregate findings to a home Region
- Enable AWS Config in all accounts and Regions with an organization aggregator

**Vulnerability and Data:**
- Enable Amazon Inspector for EC2, ECR, and Lambda (including code scanning)
- Enable Amazon Macie automated sensitive data discovery for S3

**Access and Investigation:**
- Enable IAM Access Analyzer for external, internal, and unused access at the organization level
- Enable Amazon Detective for investigations
- Consider Amazon Security Lake to store logs and findings in OCSF format for your SIEM

**Response:**
- Route findings through EventBridge to ticketing, chat, and SOAR
- Set severity-based SLAs and auto-remediate only low-risk, well-tested cases
- Review service coverage every quarter (new Regions, new accounts, new protection plans)

**Cost:**
- Track per-service cost and tune data sources rather than turning services off

Generate Terraform or CloudFormation StackSets to deploy this setup with delegated administration, and list the manual steps that cannot be automated.
