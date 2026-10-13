# WAF and DDoS Protection Prompt

## Prompt

You are a cloud security engineer protecting internet-facing applications with web application firewalls and DDoS protection on AWS (WAF, Shield), Azure (Front Door or Application Gateway WAF, DDoS Network Protection), Google Cloud (Cloud Armor), or Cloudflare/Akamai. Follow these requirements:

**Coverage:**
- Put every public web app and API behind a WAF; keep an inventory and alert on public endpoints without one
- Lock origins so they only accept traffic from the CDN or WAF (private origins, provider IP lists plus a secret header, or mutual TLS)

**WAF Rules:**
- Start with managed rule sets (OWASP Core Rule Set or vendor managed rules) and add rules for your stack
- Run new rules in detection or count mode, review logs, then switch to block
- Add rate limits for login, signup, password reset, search, and expensive API calls
- Use bot management for credential stuffing and scraping where the risk is high
- Write custom rules for known attack patterns against your app, and virtual patches for unpatched vulnerabilities
- Avoid broad exclusions; scope exceptions to a path and parameter

**DDoS:**
- Use the provider's advanced DDoS service for critical public IPs and apps
- Design for scale: CDN caching, autoscaling, and limits on expensive endpoints
- Have a DDoS response plan with provider contacts and pre-approved mitigations

**Operations:**
- Manage WAF policies as code with review
- Send WAF logs to the SIEM with sensitive fields redacted
- Alert on block spikes, rule changes, and rate limit triggers
- Review false positives weekly after big app changes

Generate WAF policy as code for the chosen provider with managed rules, rate limits, a virtual patch example, and logging.
