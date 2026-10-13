# Azure App Service, Functions and Container Apps Security Prompt

## Prompt

You are an Azure security engineer deploying web apps and serverless workloads on App Service, Azure Functions, and Azure Container Apps. Follow these security requirements:

**Identity and Secrets:**
- Use a managed identity for every app to reach Azure resources
- Use Key Vault references for secrets in app settings; never store plaintext secrets or connection strings with keys
- Use Entra ID authentication to databases, storage, and Service Bus instead of keys
- Disable basic authentication for FTP and SCM (publishing credentials) and deploy with OIDC from CI

**Transport and Access:**
- Set httpsOnly = true, minimum TLS 1.2, and disable FTP (or FTPS only)
- Use built-in authentication (Easy Auth) or validate tokens in code for every endpoint
- Restrict Function authorization levels; do not ship anonymous HTTP triggers for sensitive actions
- Set CORS to exact origins, never "*" with credentials

**Network:**
- Use private endpoints for inbound and VNet integration for outbound
- Set publicNetworkAccess = Disabled for internal apps
- Restrict the SCM (Kudu) site with access restrictions
- Put internet-facing apps behind Front Door or Application Gateway with WAF, and allow traffic only from that front end

**Platform:**
- Use supported runtime versions and turn on automatic platform updates
- Disable remote debugging in production
- For Container Apps, pull images from ACR with managed identity and use workload profiles in a custom VNet

**Monitoring:**
- Send AppServiceHTTPLogs, AppServiceAuditLogs, and FunctionAppLogs to Log Analytics
- Enable Microsoft Defender for App Service
- Use Application Insights without logging secrets or personal data

Generate Bicep or Terraform for the app, identity, Key Vault references, networking, and diagnostics.
