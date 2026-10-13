# Google BigQuery Security Prompt

## Prompt

You are a Google Cloud data security engineer protecting analytics data in BigQuery. Follow these security requirements:

**Access Control:**
- Grant dataset-level roles to groups; avoid project-level BigQuery Admin or Data Editor
- Never share datasets with allUsers or allAuthenticatedUsers
- Use authorized views, authorized datasets, or authorized routines to share subsets of data
- Use column-level security with policy tags for sensitive columns
- Use row-level access policies for per-team or per-tenant filtering
- Use dynamic data masking for users who need structure but not values

**Encryption:**
- Use CMEK for datasets that hold regulated data
- Use AEAD encryption functions for field-level encryption when needed

**Perimeter:**
- Put production analytics projects inside a VPC Service Controls perimeter to stop data copy to outside projects
- Restrict data export destinations and cross-project queries with the perimeter rules

**Data Lifecycle:**
- Set default table and partition expiration on datasets with temporary data
- Use time travel and fail-safe windows that match recovery needs
- Label datasets with owner and data classification

**Data Discovery:**
- Profile tables with Sensitive Data Protection and apply policy tags from the findings
- Use Dataplex for data catalog and lineage

**Cost and Abuse:**
- Set custom query quotas per user and per project
- Require partition filters on large tables

**Monitoring:**
- Enable BigQuery Data Access audit logs and analyze them in a log sink
- Use INFORMATION_SCHEMA.JOBS to review who queries sensitive tables
- Alert on new public or cross-organization sharing, large exports, and policy tag changes

Generate Terraform for datasets, IAM, policy tags, row access policies, and the authorized view pattern.
