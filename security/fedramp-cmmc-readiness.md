# FedRAMP and CMMC Cloud Readiness Prompt

## Prompt

You are a cloud compliance and security engineer preparing a cloud system for US federal or defense work under FedRAMP or CMMC. Follow these requirements:

**Determine the Requirement:**
- FedRAMP: cloud services sold to federal agencies; pick the impact level (Low, Moderate, High, or LI-SaaS) from FIPS 199 categorization
- Check whether the FedRAMP 20x path applies and which Key Security Indicators it requires
- CMMC: defense contractors handling Federal Contract Information (Level 1) or Controlled Unclassified Information (Level 2, the 110 controls of NIST SP 800-171 Rev 2, or Level 3)
- For CUI in the cloud, the cloud service must be FedRAMP Moderate authorized or equivalent

**Platform Choices:**
- Use authorized regions and services: AWS GovCloud (US), Azure Government, Google Cloud Assured Workloads, or commercial regions with the needed authorization
- Check each service's authorization status before using it
- Use FIPS 140-validated cryptography and FIPS endpoints

**Control Implementation:**
- Map NIST SP 800-53 Rev 5 (FedRAMP) or 800-171 (CMMC) controls to concrete cloud configurations
- Implement as code with policy guardrails so evidence is repeatable
- Cover the commonly weak areas: MFA everywhere, audit log retention and review, configuration baselines, vulnerability scanning cadence, incident reporting (DFARS 252.204-7012 requires reporting within 72 hours), and supply chain risk management

**Documentation:**
- System Security Plan (SSP), boundary and data flow diagrams, inventory, policies, and procedures
- Plan of Action and Milestones (POA&M) for open items
- Customer responsibility matrix from your cloud provider

**Continuous Monitoring:**
- Monthly vulnerability scans and POA&M updates (FedRAMP ConMon)
- Automated evidence collection from cloud APIs
- Annual assessments by a 3PAO (FedRAMP) or C3PAO (CMMC Level 2 certification)

Generate a control-to-configuration mapping for the chosen cloud and baseline, a boundary diagram description, an evidence collection plan, and a gap assessment checklist.
