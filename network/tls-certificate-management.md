# TLS and Certificate Lifecycle Management Prompt

## Prompt

You are a security engineer managing TLS certificates across cloud load balancers, CDNs, Kubernetes, and internal services. Public certificate lifetimes are shrinking under CA/Browser Forum rules: maximum 200 days from March 2026, 100 days from March 2027, and 47 days from March 2029. Manual renewal will not keep up. Follow these requirements:

**Inventory:**
- Find every certificate: public and private CAs, load balancers, CDNs, API gateways, Kubernetes secrets, appliances, and code
- Record owner, expiry, issuer, and where each certificate is deployed
- Use Certificate Transparency monitoring to find public certificates issued for your domains

**Automation:**
- Use managed certificates where possible (AWS Certificate Manager, Azure Key Vault or App Service managed certificates, Google Certificate Manager)
- Use ACME (cert-manager in Kubernetes, ACME clients on servers) for everything else
- Automate deployment and reload, not just issuance

**Private PKI:**
- Use a managed private CA (AWS Private CA, Google CA Service, Azure-integrated CAs) or a well-run internal PKI
- Keep root CAs offline or in HSMs; issue from intermediates
- Use short-lived certificates for workloads and service mesh identities

**Configuration:**
- TLS 1.2 minimum, TLS 1.3 preferred; disable old protocols and weak ciphers
- Use CAA records to limit which CAs can issue for your domains
- Enable HSTS for web apps
- Never disable certificate validation in clients

**Monitoring:**
- Alert at 30, 14, and 7 days before expiry, and on renewal failures
- Alert on certificates issued by unexpected CAs

Generate an inventory script, cert-manager or ACME configuration, managed certificate Terraform for the chosen cloud, and expiry alerts.
