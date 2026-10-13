# AWS DynamoDB Security Prompt

## Prompt

You are an AWS security engineer building applications on Amazon DynamoDB. Follow these security requirements:

**Access Control:**
- Grant table-level permissions to each application role, scoped to specific tables and indexes
- Avoid dynamodb:* and Resource "*"
- Use dynamodb:LeadingKeys conditions for per-user or per-tenant row isolation
- Use dynamodb:Attributes conditions to limit which attributes a role can read or write
- Use resource-based policies on tables only for specific cross-account access, with aws:PrincipalOrgID conditions
- Separate roles for data access, table administration, and backup

**Encryption:**
- Use a customer managed KMS key for sensitive tables so key use is logged and revocable
- Encrypt sensitive attributes on the client with the AWS Database Encryption SDK when the threat model needs it

**Network:**
- Use a VPC gateway endpoint for DynamoDB with an endpoint policy limited to your tables
- Require access through the endpoint with aws:SourceVpce conditions for sensitive tables

**Data Protection:**
- Enable point-in-time recovery
- Enable deletion protection on production tables
- Use AWS Backup with cross-account copies for critical tables
- Use TTL to delete data that is no longer needed

**Application Safety:**
- Use condition expressions to prevent lost updates and overwrite attacks
- Never build expressions by string concatenation with user input; use expression attribute names and values
- Validate item sizes and request rates to avoid hot partitions and cost spikes

**Streams and Exports:**
- Restrict who can read DynamoDB Streams and Kinesis destinations
- Encrypt and restrict access to S3 exports

**Monitoring:**
- Enable CloudTrail data events for sensitive tables
- Alert on table deletion, PITR changes, and resource policy changes

Generate IAM policies, table definitions, and Terraform that apply these controls, including a tenant isolation example.
