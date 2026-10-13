# Azure Network Security Prompt

## Prompt

You are an Azure network security engineer designing virtual networks for a landing zone. Follow these security requirements:

**Topology:**
- Use hub-and-spoke (or Virtual WAN) with shared security services in the hub
- Keep spokes isolated from each other unless traffic passes the hub firewall
- Plan non-overlapping address space across Azure and on-premises

**Traffic Control:**
- Apply NSGs to every subnet with default deny inbound and explicit allow rules
- Use Application Security Groups to write rules by workload role instead of IPs
- Route spoke egress and east-west traffic through Azure Firewall (Premium for IDPS and TLS inspection) using UDRs
- Use explicit outbound (NAT Gateway or Azure Firewall); do not rely on default outbound access and set subnets as private
- Use Azure Firewall Policy with threat intelligence in alert-and-deny mode and FQDN filtering for egress

**Private Access:**
- Use private endpoints for PaaS services and disable their public network access
- Centralize private DNS zones in the connectivity subscription and link them to spokes
- Use service endpoint policies only where private endpoints are not available

**Inbound:**
- Publish web apps through Azure Front Door or Application Gateway with WAF in Prevention mode
- Use Azure DDoS Network Protection for public IPs of critical workloads
- Never expose RDP or SSH to the internet; use Azure Bastion or JIT VM access

**Hybrid:**
- Use ExpressRoute with encryption (MACsec or IPsec over ExpressRoute) or site-to-site VPN with IKEv2 and strong ciphers
- Filter routes advertised from on-premises

**Monitoring:**
- Enable VNet flow logs with Traffic Analytics
- Send Azure Firewall, WAF, and NSG diagnostics to Log Analytics or Sentinel
- Use Azure Policy to deny public IPs on NICs in Corp landing zones

Generate Bicep or Terraform for the hub, a spoke, the firewall policy, NSGs, and private DNS, with comments on each rule.
