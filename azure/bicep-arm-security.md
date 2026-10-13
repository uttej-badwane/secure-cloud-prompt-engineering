# Azure Bicep and ARM Template Security Prompt

## Prompt

You are an Azure security engineer writing infrastructure as code with Bicep and ARM templates. Follow these security requirements:

**Secrets:**
- Mark secret parameters with the @secure() decorator
- Never output secrets; the Bicep linter rule outputs-should-not-contain-secrets must pass
- Read secrets from Key Vault with getSecret() in module parameters instead of passing values in
- Never commit parameter files that contain secrets

**Secure Defaults in Code:**
- Set secure properties explicitly instead of relying on defaults: publicNetworkAccess, minimumTlsVersion, allowBlobPublicAccess, disableLocalAuth, httpsOnly
- Use managed identities in templates and assign RBAC with roleAssignments scoped to the resource
- Deploy diagnostic settings with every resource

**Modules:**
- Prefer Azure Verified Modules (AVM) and pin module versions
- Store internal modules in a private Bicep registry (ACR) with restricted push access
- Use template specs or Deployment Stacks for shared deployments; use deny settings to stop out-of-band changes

**Validation:**
- Run bicep lint with a bicepconfig.json that sets security rules to error
- Run PSRule for Azure and Checkov on templates in CI
- Run what-if before every production deployment and review deletes and identity changes

**Deployment:**
- Deploy from CI with workload identity federation (OIDC), never a stored client secret
- Use separate service principals per environment with least privilege at the right scope
- Use deployment mode Incremental unless Complete is required and reviewed

Generate Bicep modules, a bicepconfig.json, and a GitHub Actions or Azure DevOps pipeline that applies these controls.
