# Cloud Egress Control Prompt

## Prompt

You are a cloud network security engineer controlling outbound traffic from workloads. Open egress lets attackers download tools, reach command and control, and send data out. Follow these requirements:

**Default Posture:**
- Workloads have no direct internet route by default
- All allowed egress goes through a central inspection point (AWS Network Firewall, Azure Firewall, Cloud NGFW, or a proxy)
- Use private endpoints for cloud services so that traffic never needs the internet

**Allowlisting:**
- Allow egress by FQDN and TLS SNI for known destinations (package registries, SaaS APIs, partner endpoints)
- Keep allowlists per application or environment in code with owners
- Block direct IP egress except for documented cases

**DNS:**
- Force all DNS through managed resolvers with DNS firewall rules
- Block known bad domains and newly registered domains where practical
- Detect DNS tunneling and high-volume lookups

**Special Cases:**
- CI/CD runners: restrict egress to build dependencies and deploy targets
- Kubernetes: add egress NetworkPolicies and FQDN policies in addition to network firewalls
- AI agents and code sandboxes: no internet by default, or a strict allowlist

**Monitoring:**
- Log all allowed and denied egress with source workload identity
- Alert on denied connection spikes, new destinations, and large outbound transfers

**Rollout:**
- Start in log-only mode to learn real traffic
- Build allowlists from logs, review them, then switch to deny

Generate firewall policy as code for the chosen cloud with FQDN rules, DNS firewall rules, and a rollout plan from monitor mode to enforce.
