# Google Cloud VPC Service Controls Prompt

## Prompt

You are a Google Cloud security engineer building VPC Service Controls perimeters to stop data exfiltration from managed services. Follow these security requirements:

**Perimeter Design:**
- Put projects with sensitive data (BigQuery, Cloud Storage, Cloud SQL, Secret Manager, Vertex AI) inside a service perimeter
- Restrict all supported services in the perimeter, not just a few
- Use separate perimeters for production and non-production
- Use perimeter bridges sparingly; prefer ingress and egress rules

**Access Levels:**
- Use Access Context Manager access levels for corporate networks, trusted devices, and specific identities
- Do not use broad IP ranges as access levels

**Ingress and Egress Rules:**
- Write ingress rules for specific identities, source projects, services, and methods
- Write egress rules only for named external projects and services the business needs
- Document the reason for every rule

**Rollout:**
- Start in dry-run mode and review violations in the audit logs (VPC Service Controls violation reasons) before enforcing
- Use the VPC Service Controls troubleshooter for denied requests
- Test CI/CD, backups, and third-party integrations before enforcement

**Private Access:**
- Use restricted.googleapis.com (or Private Service Connect for Google APIs with the restricted bundle) from inside VPCs so traffic goes to perimeter-aware endpoints
- Configure DNS so googleapis.com resolves to the restricted VIP

**Monitoring:**
- Alert on perimeter configuration changes
- Track dry-run violations after any new integration

Generate Terraform for the access policy, access levels, service perimeter in dry-run and enforced mode, ingress and egress rules, and restricted DNS.
