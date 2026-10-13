# AWS Data Perimeter Security Prompt

## Prompt

You are an AWS security engineer building a data perimeter for an AWS Organization. The goal: only trusted identities can access trusted resources from expected networks. Follow these security requirements:

**Perimeter Building Blocks:**
- Service Control Policies (SCPs) limit what your principals can do
- Resource Control Policies (RCPs) limit what anyone can do to your resources, including external principals
- VPC endpoint policies limit what can be reached through your private network paths
- Resource-based policies add per-resource rules

**Identity Perimeter (only trusted identities):**
- Use RCPs to deny access to S3, KMS, STS, SQS, and Secrets Manager unless aws:PrincipalOrgID matches your organization
- Allow AWS service principals through with aws:PrincipalIsAWSService, and protect against confused deputy with aws:SourceOrgID or aws:SourceAccount
- Use VPC endpoint policies that only allow principals from your organization

**Resource Perimeter (only trusted resources):**
- Use SCPs that deny actions unless aws:ResourceOrgID matches your organization, so stolen credentials cannot copy data to an attacker's bucket
- Add documented exceptions for AWS-owned resources and approved third-party accounts

**Network Perimeter (only expected networks):**
- Deny access to sensitive resources unless the request comes from your VPCs (aws:SourceVpc), your VPC endpoints, or your corporate IP ranges
- Use aws:ViaAWSService to allow requests that AWS services make on your behalf
- Protect role credentials from use outside your networks where practical

**Rollout:**
- Start with CloudTrail and IAM Access Analyzer to find current external access before enforcing
- Test policies in a sandbox OU, then roll out OU by OU
- Use condition keys like aws:PrincipalTag to create break-glass exceptions, and log every exception
- Keep policies in version control and deploy them through IaC with review

**Monitoring:**
- Alert on AccessDenied spikes after each rollout step
- Track RCP and SCP changes with EventBridge rules
- Review Access Analyzer external access findings regularly

Generate SCPs, RCPs, and VPC endpoint policies in JSON plus Terraform to attach them, based on the AWS data perimeter policy examples, with comments explaining every condition key.
