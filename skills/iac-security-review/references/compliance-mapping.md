# Compliance Framework Mapping Reference

Maps common IaC security findings to applicable compliance controls.
Use this reference in Step 3 of the IaC Security Review workflow.

---

## Framework Overview

| Framework | Scope | Key Focus |
|---|---|---|
| CIS Benchmarks | Cloud, K8s, Docker | Hardening baselines |
| NIST 800-53 | Federal / general | Security controls catalog |
| NIST 800-171 | CUI handling | Protecting Controlled Unclassified Information |
| NIST CSF 2.0 | All organizations | Govern, Identify, Protect, Detect, Respond, Recover |
| PCI-DSS v4.0.1 | Payment card data | Cardholder data protection |
| SOC 2 | SaaS / service orgs | Trust Services Criteria |
| HIPAA | Healthcare | PHI protection |
| GDPR | EU data subjects | Privacy and data rights |
| ISO/IEC 27001:2022 | All organizations | ISMS management |

---

## CIS Benchmarks

Always cite the benchmark version you checked against. Section numbers move between versions.

### AWS (CIS AWS Foundations Benchmark, v7.0.0 as of 2026)
- Identity and Access Management: MFA, root account, access keys, IAM policies
- Storage: S3 public access, encryption, EBS and RDS encryption
- Logging: CloudTrail, Config, VPC flow logs, KMS rotation
- Monitoring: CloudWatch metric filters and alarms
- Networking: security groups, NACLs, default VPC, IMDSv2

### Azure (CIS Microsoft Azure Foundations Benchmark, v6.0.0 as of 2026)
- Microsoft Entra ID, Defender for Cloud, storage, networking, Key Vault, logging

### GCP (CIS Google Cloud Platform Foundation Benchmark, v5.0.0 as of 2026)
- Org policies, IAM, logging, networking, storage, Cloud KMS

### Kubernetes (CIS Kubernetes Benchmark, v2.0.1 as of 2026; use the EKS/AKS/GKE benchmarks for managed clusters)
- **4.x** Worker node security — kubelet authentication, file permissions
- **5.x** Policies — Pod Security Admission, network policies, RBAC

### Docker (CIS Docker Benchmark, latest)
- Host configuration, daemon configuration, container images, runtime security

---

## NIST 800-53 Control Mapping

| Finding Category | NIST 800-53 Controls |
|---|---|
| Hardcoded secrets / credentials | IA-5 (Authenticator Management), SC-28 (Protection at Rest) |
| Overly permissive IAM | AC-2 (Account Management), AC-6 (Least Privilege), AC-3 (Access Enforcement) |
| Missing encryption at rest | SC-28 (Protection at Rest), SC-13 (Cryptographic Protection) |
| Missing encryption in transit | SC-8 (Transmission Confidentiality), SC-23 (Session Authenticity) |
| No audit logging | AU-2 (Event Logging), AU-3 (Content of Audit Records), AU-12 (Audit Generation) |
| Public exposure / open ports | SC-7 (Boundary Protection), AC-17 (Remote Access), CM-7 (Least Functionality) |
| No MFA | IA-2 (Identification and Authentication), IA-2(1) (MFA for Privileged) |
| Missing vulnerability scanning | RA-5 (Vulnerability Monitoring and Scanning), SI-2 (Flaw Remediation) |
| No incident response | IR-4 (Incident Handling), IR-6 (Incident Reporting) |
| Missing resource tagging | CM-8 (System Component Inventory) |
| Containers running as root | CM-7 (Least Functionality), AC-6 (Least Privilege) |
| Unpinned image versions | CM-2 (Baseline Configuration), CM-3 (Configuration Change Control) |
| Missing network segmentation | SC-7 (Boundary Protection), SC-3 (Security Function Isolation) |
| No secret rotation | IA-5(1) (Password-Based Authentication), IA-5(2) (PKI-Based Authentication) |
| Supply chain risks | SR-3 (Supply Chain Controls), SR-11 (Component Authenticity), SA-8 (SA-12 was withdrawn in Rev 5) |
| Missing key management | SC-12 (Cryptographic Key Establishment and Management) |
| No data classification | RA-2 (Security Categorization), MP-3 (Media Marking) |
| No continuous monitoring | CA-7 (Continuous Monitoring), SI-4 (System Monitoring) |

---

## NIST 800-171 Control Mapping (CUI)

Applies when infrastructure handles Controlled Unclassified Information (CUI), common in federal contractor environments.

IDs below use Rev 2 numbering, which CMMC Level 2 assessments still use. Rev 3 (May 2024) renumbers controls as 03.xx.xx; map to Rev 3 when the contract requires it.

| Finding Category | NIST 800-171 Control |
|---|---|
| Missing access controls | 3.1.1 — Limit system access to authorized users |
| No MFA for privileged access | 3.5.3 — Use multifactor authentication |
| Hardcoded credentials | 3.5.10 — Store and transmit only cryptographically-protected passwords |
| Missing encryption at rest | 3.13.16 — Protect the confidentiality of CUI at rest |
| Missing encryption in transit | 3.13.8 — Implement cryptographic mechanisms to prevent unauthorized disclosure |
| No audit logging | 3.3.1 — Create and retain system audit logs |
| Missing vulnerability scanning | 3.11.2 — Scan for vulnerabilities in systems periodically |
| No incident response | 3.6.1 — Establish an operational incident-handling capability |
| No system configuration baseline | 3.4.1 — Establish and maintain baseline configurations |

---

## NIST Cybersecurity Framework (CSF) Mapping

| CSF Function | IaC Security Activities |
|---|---|
| **Govern** | Security policy, roles, risk strategy, supply chain risk management (GV.SC), policy as code ownership |
| **Identify** | Asset inventory (resource tagging), data classification, risk assessment |
| **Protect** | IAM least privilege, encryption at rest/in transit, secret management, network segmentation, secure configuration baselines |
| **Detect** | CloudTrail/audit logging, GuardDuty, vulnerability scanning, secret scanning, anomaly alerting |
| **Respond** | Incident response plan, automated remediation workflows, ticket creation for findings |
| **Recover** | Backup and recovery configurations, DeletionPolicy on stateful resources, DR testing |

---

## PCI-DSS Control Mapping

| Finding Category | PCI-DSS Requirement |
|---|---|
| Hardcoded credentials | Req 8: Identify and authenticate access to system components |
| Open network access to cardholder data | Req 1: Install and maintain network security controls |
| Missing encryption at rest | Req 3: Protect stored account data |
| Missing TLS / encryption in transit | Req 4: Protect cardholder data with strong cryptography in transit |
| No audit logging | Req 10: Log and monitor all access to system components and cardholder data |
| Outdated/unpatched systems | Req 6: Develop and maintain secure systems and software |
| Missing vulnerability scanning | Req 11: Test security of systems and networks regularly |
| Quarterly vulnerability scans not scheduled | Req 11.3.1 (internal) and 11.3.2 (external, via ASV) |
| Overly permissive access | Req 7: Restrict access to system components and cardholder data by business need to know |
| No segmentation of CDE | Req 1: Network security controls isolating CDE |
| Missing file integrity monitoring (FIM) | Req 11.5.2: Change-detection mechanism for critical files |
| No unique IDs per user | Req 8.2.1: Assign all users a unique ID before access |
| No access revocation process | Req 8.2.5 and 8.2.6: Revoke terminated users, remove inactive accounts |
| No MFA into the CDE | Req 8.4.2: MFA for all access into the CDE |
| Payment page scripts not controlled | Req 6.4.3 and 11.6.1: Script inventory and tamper detection |

---

## SOC 2 Trust Services Criteria Mapping

### Security (CC Series)
| Finding Category | SOC 2 Criteria |
|---|---|
| Missing access controls | CC6.1 — Logical and physical access controls |
| No MFA / weak auth | CC6.3 — Authentication mechanisms |
| Missing encryption | CC6.7 — Transmission and storage protection |
| No audit logging | CC7.2 — Monitoring for anomalies |
| No incident response plan | CC7.3 — Incident response |
| Missing vulnerability management | CC7.1 — Vulnerability and threat management |
| No change management | CC8.1 — Change management controls |
| No risk assessment | CC3.1 — Risk assessment process |

### Processing Integrity (PI Series)
| Finding Category | SOC 2 Criteria |
|---|---|
| No input validation or data quality checks in pipelines | PI1.2: System inputs are complete and accurate |
| Processing errors not detected or handled | PI1.3: Processing is complete, accurate and timely |

### Availability (A Series)
| Finding Category | SOC 2 Criteria |
|---|---|
| No availability measures | A1.1 — Capacity and availability planning |
| Missing backup / recovery | A1.2 — Recovery procedures |
| No DR testing | A1.3 — Recovery plan testing |

### Confidentiality (C Series)
| Finding Category | SOC 2 Criteria |
|---|---|
| No data classification | C1.1 — Identify and maintain confidential information |
| Missing confidentiality controls | C1.2 — Dispose of confidential information |

### Privacy (P Series)
| Finding Category | SOC 2 Criteria |
|---|---|
| No data retention policy | P4.3 — Retain personal information consistent with policy |
| Missing data deletion capability | P4.4 — Dispose of personal information |
| No breach notification process | P8.1 — Notify of privacy incidents |

---

## HIPAA Security Rule Mapping

| Finding Category | HIPAA Safeguard |
|---|---|
| No PHI encryption at rest | Technical — Encryption and Decryption (§164.312(a)(2)(iv)) |
| No PHI encryption in transit | Technical — Transmission Security (§164.312(e)(1)) |
| Overly permissive access to PHI systems | Technical — Access Control (§164.312(a)(1)) |
| Missing audit logs | Technical — Audit Controls (§164.312(b)) |
| No automatic session timeout | Technical — Automatic Logoff (§164.312(a)(2)(iii)) |
| Missing risk assessment | Administrative — Risk Analysis (§164.308(a)(1)) |
| No BAA with cloud provider | Administrative — Business Associate Contracts (§164.308(b)(1)) |
| Missing data backup | Administrative — Data Backup Plan (§164.308(a)(7)(ii)(A)) |
| No disaster recovery plan | Administrative — Disaster Recovery Plan (§164.308(a)(7)(ii)(B)) |
| Missing integrity controls | Technical — Integrity (§164.312(c)(1)) |

---

## GDPR Mapping

| Finding Category | GDPR Article |
|---|---|
| Missing encryption of personal data | Art. 32 — Security of processing |
| No data protection by design/default | Art. 25 — Data protection by design and by default |
| No pseudonymization of personal data | Art. 4(5) / Art. 32 — Pseudonymisation as a security measure |
| No data retention / deletion policy | Art. 5(1)(e) — Storage limitation |
| No audit trail for data access | Art. 5(2) — Accountability |
| Missing data breach detection | Art. 33 — Notification of breach to supervisory authority |
| No data portability mechanism | Art. 20 — Right to data portability |
| Missing Privacy Impact Assessment | Art. 35 — Data Protection Impact Assessment (DPIA) |
| Personal data processed beyond purpose | Art. 5(1)(b) — Purpose limitation |
| No records of processing activities | Art. 30 — Records of processing activities |
| Cross-border data transfer controls | Art. 44-49 — Transfers to third countries |

---

## ISO/IEC 27001:2022 Annex A Mapping

Uses the 2022 Annex A numbering. The 2013 numbering (A.9, A.12 and so on) is retired; 2013 certificates expired on October 31, 2025.

| Finding Category | ISO 27001:2022 Control |
|---|---|
| Hardcoded / exposed secrets | A.5.17: Authentication information; A.8.5: Secure authentication |
| Missing access controls | A.5.15: Access control; A.8.3: Information access restriction |
| Overly broad privileges | A.8.2: Privileged access rights |
| No encryption | A.8.24: Use of cryptography |
| Missing network security | A.8.20: Networks security; A.8.22: Segregation of networks |
| No logging / monitoring | A.8.15: Logging; A.8.16: Monitoring activities |
| Vulnerability management gaps | A.8.8: Management of technical vulnerabilities |
| Insecure baseline / drift | A.8.9: Configuration management |
| No change management | A.8.32: Change management |
| Missing incident response | A.5.24 to A.5.26: Incident management planning, assessment and response |
| No ISMS or risk assessment | A.5.2: Information security roles and responsibilities; Clause 6 Risk assessment |
| Missing supplier/vendor security | A.5.19 to A.5.22: Supplier relationships |
| Cloud service misconfiguration | A.5.23: Information security for use of cloud services |
| No asset inventory | A.5.9: Inventory of information and other associated assets |
| No business continuity plan | A.5.30: ICT readiness for business continuity |
| Data leakage paths | A.8.12: Data leakage prevention |
| Insecure code or IaC | A.8.25 to A.8.28: Secure development life cycle and secure coding |
| Missing security awareness | A.6.3: Information security awareness, education and training |

---

## Compliance Automation Approaches

- **Policy as Code**: OPA/Rego, HashiCorp Sentinel, Cloud Custodian
- **Compliance scanning**: Prowler (CIS/AWS), Chef InSpec profiles, AWS Config Rules, Azure Policy, GCP Organization Policy
- **CI/CD integration**: Checkov, Trivy, KICS, cfn-guard in pipeline gates; fail builds on policy violations
- **Reporting**: SARIF output to GitHub Security tab, compliance dashboards, executive scorecards
- **Ongoing monitoring**: AWS Security Hub, Microsoft Defender for Cloud, GCP Security Command Center
- **Compliance as Code**: Use IaC itself to enforce compliant configurations; document control mappings inline
- **Status tracking**: Track compliance status over time; implement remediation SLAs and workflows
- **Audit evidence**: Automate generation of audit evidence (configuration snapshots, access logs, scan reports)
