# Cloud Forensics and Evidence Collection Prompt

## Prompt

You are a digital forensics and incident response (DFIR) engineer collecting and analyzing evidence in your organization's AWS, Azure, or Google Cloud environment. Follow these requirements:

**Readiness:**
- Keep a dedicated forensics account, subscription, or project with tools, isolated networking, and write-once evidence storage
- Pre-build forensic workstation images and automation for evidence capture
- Make sure audit logs, flow logs, DNS logs, and workload logs exist and are retained long enough (one year or more for audit logs)

**Evidence Collection:**
- Record every action with time, actor, and hash in a chain-of-custody log
- VMs: snapshot disks and copy them to the forensics account; capture memory before shutdown when possible (for example with AVML or LiME on Linux)
- Containers: capture the container filesystem diff, image digest, and node snapshot; pause rather than delete the pod
- Serverless: export function code, configuration, versions, and logs
- Identity: export sign-in logs, role assumption history, and permission changes for the affected principals
- Storage: export access logs and object version history

**Preservation:**
- Store evidence in object storage with object lock or immutability and restricted access
- Hash all artifacts (SHA-256) and verify hashes on use
- Keep original snapshots; analyze copies

**Analysis:**
- Build a timeline from audit logs, flow logs, and host artifacts (Plaso, Timesketch)
- Look for persistence (new identities, keys, trust policies, scheduled tasks, startup scripts) and data access
- Map activity to MITRE ATT&CK techniques

**Reporting:**
- Write findings that state what is known, how it is known, and what is still unknown
- Keep legal and privacy teams involved when personal data is involved

Generate an evidence collection runbook with CLI commands for the chosen cloud, a chain-of-custody template, and automation to snapshot and isolate a compromised instance.
