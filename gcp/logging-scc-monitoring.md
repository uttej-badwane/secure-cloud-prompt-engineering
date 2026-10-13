# Google Cloud Logging and Security Command Center Prompt

## Prompt

You are a Google Cloud security operations engineer setting up logging, posture management, and threat detection. Follow these security requirements:

**Audit Logs:**
- Admin Activity and System Event logs are always on; keep them
- Turn on Data Access audit logs (off by default for most services) for IAM, KMS, Secret Manager, Cloud Storage, BigQuery, and Cloud SQL in production
- Enable Access Transparency (and Access Approval where needed) for Google staff access visibility

**Central Log Storage:**
- Create an organization-level aggregated sink with include-children to a central logging project
- Route to log buckets with locked retention for audit evidence, and to BigQuery or your SIEM for analysis
- Use Log Analytics on log buckets for SQL queries
- Restrict access to log buckets and sinks with dedicated groups; nobody should be able to delete the sink without alerting

**Security Command Center:**
- Activate Security Command Center at organization level (Premium or Enterprise tier for threat detection and attack path simulation)
- Turn on Event Threat Detection, Container Threat Detection, VM Threat Detection, and Security Health Analytics
- Use posture management with predefined postures (for example, the secure-by-default and CIS postures)
- Export findings to Pub/Sub for ticketing and SIEM, and mute only with documented reasons

**Alerting:**
- Create log-based alerts for IAM policy changes at org and folder level, org policy changes, audit config changes, VPC firewall changes, service account key creation, and super admin logins
- Map detections to MITRE ATT&CK

**SIEM:**
- Use Google Security Operations (SecOps) or forward to your SIEM through Pub/Sub
- Keep parsers and detection rules in version control

Generate Terraform for the aggregated sink, log buckets with retention, SCC notification configs, and log-based alert policies.
