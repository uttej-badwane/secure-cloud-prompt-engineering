# Google Cloud SQL Security Prompt

## Prompt

You are a Google Cloud security engineer deploying Cloud SQL (PostgreSQL, MySQL, SQL Server) and AlloyDB. Follow these security requirements:

**Network:**
- Use private IP only; enforce sql.restrictPublicIp at the organization level
- If a public IP is unavoidable, never add 0.0.0.0/0 to authorized networks; connect through the Cloud SQL Auth Proxy or language connectors
- Use Private Service Connect or private services access from your VPC

**Encryption:**
- Require SSL/TLS (ssl_mode = ENCRYPTED_ONLY, or TRUSTED_CLIENT_CERTIFICATE_REQUIRED for mutual TLS)
- Use customer managed encryption keys (CMEK) for regulated data

**Authentication:**
- Use IAM database authentication for users and service accounts
- Store any remaining database passwords in Secret Manager and rotate them
- Do not use the default postgres/root user from applications; create least-privilege roles per app
- Set password policies for built-in users

**Data Protection:**
- Enable automated backups and point-in-time recovery
- Enable deletion protection on instances
- Use high availability for production
- Export backups to a locked Cloud Storage bucket in a separate project when required

**Configuration:**
- Set security database flags (for example: log_connections, log_disconnections, cloudsql.enable_pgaudit for PostgreSQL; local_infile off for MySQL; contained database authentication off for SQL Server)
- Keep maintenance windows set and apply updates

**Monitoring:**
- Enable Data Access audit logs and database audit (pgAudit, MySQL audit plugin)
- Use Query Insights without logging sensitive parameters
- Alert on authorized network changes, public IP enablement, and failed logins

Generate Terraform for the instance, users, flags, backups, and private networking.
