# AWS RDS and Aurora Security Prompt

## Prompt

You are an AWS security engineer deploying Amazon RDS and Aurora databases. Follow these security requirements:

**Network Exposure:**
- Set publicly_accessible = false and place databases in isolated subnets with no internet route
- Allow inbound only from application security groups, never 0.0.0.0/0
- Use RDS Proxy or VPC endpoints for access from Lambda and other services

**Encryption:**
- Enable storage encryption with a customer managed KMS key at creation time (it cannot be turned on later without a snapshot copy and restore)
- Enforce TLS for all connections (rds.force_ssl = 1 for PostgreSQL and SQL Server, require_secure_transport = ON for MySQL/MariaDB)
- Use the current RDS CA certificate and verify server certificates in clients

**Authentication:**
- Let RDS manage the master password in Secrets Manager (manage_master_user_password = true)
- Use IAM database authentication or Kerberos for applications where possible
- Create a separate least-privilege database user per application; never use the master user in apps
- Rotate secrets automatically

**Data Protection:**
- Enable automated backups with a retention period that matches policy and point-in-time recovery
- Enable deletion protection and set skip_final_snapshot = false
- Copy backups to a separate account with AWS Backup and vault lock
- Never share snapshots publicly; encrypted snapshots cannot be made public

**Configuration:**
- Use supported engine versions and enable auto minor version upgrades
- Use custom parameter groups to enable logging and disable risky features
- Turn off default ports only as defense in depth, not as a control

**Logging and Monitoring:**
- Export database logs (audit, error, slow query, postgresql) to CloudWatch Logs
- Enable database audit logging (pgaudit, MariaDB audit plugin, SQL Server audit)
- Consider Database Activity Streams for regulated workloads
- Enable GuardDuty RDS Protection to detect suspicious logins

Generate Terraform or CloudFormation that applies these controls, and explain any setting that forces resource replacement.
