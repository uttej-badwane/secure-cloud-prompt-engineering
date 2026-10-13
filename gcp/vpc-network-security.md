# Google Cloud VPC Network Security Prompt

## Prompt

You are a Google Cloud network security engineer designing VPC networks. Follow these security requirements:

**Topology:**
- Use Shared VPC host projects managed by the network team, with service projects for workloads
- Separate production and non-production into different Shared VPCs
- Delete the default network in every project (enforce compute.skipDefaultNetworkCreation)
- Use custom-mode subnets with planned, non-overlapping ranges

**Firewall:**
- Use hierarchical firewall policies at organization and folder level for baseline rules (block known bad, allow health checks)
- Use global or regional network firewall policies with secure tags instead of network tags for workload rules
- Default deny ingress; never allow 0.0.0.0/0 to SSH (22) or RDP (3389)
- Allow SSH and RDP only through Identity-Aware Proxy (IAP) TCP forwarding (35.235.240.0/20)
- Restrict egress with deny-by-default rules and FQDN or threat-intelligence rules in Cloud NGFW
- Use Cloud NGFW Enterprise for intrusion prevention where required
- Enable firewall rules logging on important rules

**Private Access:**
- Turn on Private Google Access on subnets and use Private Service Connect for Google APIs and managed services
- Remove external IPs from VMs; use Cloud NAT for egress
- Use private services access or Private Service Connect for Cloud SQL and other managed services

**Inbound:**
- Expose apps through external Application Load Balancers with Cloud Armor policies (OWASP rules, rate limiting, adaptive protection)
- Use Identity-Aware Proxy for internal web apps instead of VPNs where possible

**Hybrid:**
- Use HA VPN or Cloud Interconnect with MACsec, and filter routes with Cloud Router

**Monitoring:**
- Enable VPC Flow Logs on subnets with sampling that fits your budget
- Enable Cloud DNS logging and DNS response policies to block bad domains
- Use Network Intelligence Center to check firewall rule usage and connectivity

Generate Terraform for a Shared VPC, hierarchical firewall policy, Cloud NAT, Private Service Connect, and Cloud Armor policy.
