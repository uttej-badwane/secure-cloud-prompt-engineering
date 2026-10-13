# AWS Route 53 and DNS Security Prompt

## Prompt

You are an AWS security engineer managing DNS with Amazon Route 53. Follow these security requirements:

**Domain and Zone Protection:**
- Enable registrar transfer lock and auto-renew on every domain
- Restrict route53:ChangeResourceRecordSets and route53domains:* to a small set of roles
- Add CAA records that list only the certificate authorities you use
- Enable DNSSEC signing for public hosted zones with a KMS key in us-east-1, and set up the DS record at the parent

**Subdomain Takeover:**
- Delete DNS records when you delete the resource they point to (S3 website buckets, CloudFront, Elastic Beanstalk, Elastic IPs, third-party SaaS)
- Prefer alias records to AWS resources so records follow the resource lifecycle
- Scan zones regularly for dangling CNAME and A records

**Private DNS:**
- Use private hosted zones for internal names and do not leak internal names in public zones
- Use Route 53 Resolver endpoints and rules for hybrid DNS, shared through AWS RAM

**DNS Firewall and Logging:**
- Enable Route 53 Resolver DNS Firewall with AWS managed domain lists (malware, botnet, aggregate threat list)
- Turn on DNS Firewall Advanced protections against DNS tunneling and domain generation algorithms where available
- Enable Resolver query logging for all VPCs to a central log account
- Enable public hosted zone query logging for important zones

**Email Security Records:**
- Publish SPF, DKIM, and DMARC (p=reject when ready) for every domain, including domains that never send mail

**Monitoring:**
- Alert on hosted zone record changes, DNSSEC status changes, and domain transfer attempts
- Use GuardDuty, which analyzes DNS logs for threats

Generate Terraform for the zones, DNSSEC, DNS Firewall, and query logging, plus a script that finds dangling records.
