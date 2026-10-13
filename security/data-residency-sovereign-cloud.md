# Data Residency and Sovereign Cloud Prompt

## Prompt

You are a cloud security architect designing for data residency, data sovereignty, and government cloud requirements. Follow these requirements:

**Requirements Gathering:**
- List which data must stay in which country or region, and why (law, contract, customer promise)
- Note who must not be able to access the data (foreign governments, provider staff without approval)
- Identify applicable rules (GDPR transfers, national data laws, sector rules, government classification levels)

**Location Controls:**
- Restrict allowed regions with SCPs (aws:RequestedRegion), Azure Policy allowed locations, and GCP gcp.resourceLocations
- Turn off or control cross-region features: replication, cross-region inference for AI services, global services, CDN caching of sensitive content
- Keep backups and logs in the same jurisdiction
- Check where support and telemetry data goes

**Sovereignty Controls:**
- Use customer managed or externally held keys (AWS XKS, Azure Managed HSM, Google Cloud EKM) when you must control decryption
- Use provider access controls: AWS Nitro system isolation, Microsoft Customer Lockbox, Google Access Transparency and Access Approval
- Consider sovereign or government offerings where required (AWS GovCloud or European Sovereign Cloud, Azure Government or EU Data Boundary, Google Assured Workloads or sovereign partner clouds)

**Data Transfers:**
- Document transfer mechanisms (standard contractual clauses, adequacy decisions) for any cross-border flow
- Avoid sending regulated data to third-party SaaS or AI APIs outside the allowed region

**Verification:**
- Inventory resource locations continuously and alert on resources outside allowed regions
- Audit provider access logs and key usage logs

Generate region guardrail policies for each cloud, a data residency control matrix, and a checklist for reviewing new services.
