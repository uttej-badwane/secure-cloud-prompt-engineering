# Terraform Module and Provider Supply Chain Prompt

## Prompt

You are a security engineer managing Terraform and OpenTofu modules and providers. Modules and providers run code on the machine that runs plan, with its credentials, so treat them as dependencies with full trust. Follow these security requirements:

**Providers:**
- Pin provider versions with exact or narrow constraints
- Commit .terraform.lock.hcl and include hashes for every platform you run on (terraform providers lock -platform=...)
- Install providers only from the public registry with signature checks, or from an internal network or filesystem mirror
- Review new third-party providers before use; prefer official and partner providers

**Modules:**
- Pin registry modules to exact versions and Git modules to a commit SHA (ref=<sha>), never a branch
- Use a private module registry for internal modules with access control on publishing
- Review external modules before adopting them; look for local-exec, external data sources, and http data sources that run code or send data out during plan
- Fork critical third-party modules into your organization and update them through reviewed pull requests

**Plan Safety:**
- Treat terraform plan as code execution; never run plan with production credentials on untrusted pull requests
- Run plan for pull requests with read-only credentials and apply only from protected branches
- Restrict provisioners; prefer cloud-init, configuration management, or images instead

**Scanning:**
- Scan modules and plans with Checkov, Trivy, or KICS, and with OPA or Sentinel policies on the plan JSON
- Use Renovate or Dependabot to update pins with review

**Publishing Internal Modules:**
- Version modules with semantic versioning and release notes
- Ship secure defaults (encryption on, public access off, logging on) and make insecure options explicit
- Include tests (terraform test) and examples

Generate a versions.tf with pinned providers, module blocks pinned by version and SHA, a provider mirror configuration, and a CI job that runs plan with read-only credentials.
