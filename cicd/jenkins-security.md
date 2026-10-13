# Jenkins Security Prompt

## Prompt

You are a CI/CD security engineer hardening a Jenkins controller and its agents. Jenkins often holds deploy credentials for everything, so treat it as a tier-zero system. Follow these security requirements:

**Controller:**
- Run a current LTS release and update plugins often; Jenkins and its plugins have had critical bugs (for example CVE-2024-23897, arbitrary file read through the CLI)
- Set executors on the built-in node to 0 so builds never run on the controller
- Do not expose the controller to the internet; put it behind SSO and a VPN or identity-aware proxy
- Disable the CLI if you do not use it, and restrict the script console to a tiny admin group
- Manage configuration as code with the Configuration as Code (JCasC) plugin in Git

**Authentication and Authorization:**
- Use SSO (OIDC or SAML) with MFA; disable local accounts except break-glass
- Use Matrix or Role-based authorization; anonymous users get no access
- Limit Job/Configure, Run/Replay, and Credentials permissions to the teams that own each folder

**Pipelines:**
- Keep the Groovy sandbox on; approve scripts in In-process Script Approval only after review
- Load shared libraries as trusted only from protected repos; others run untrusted
- For pull requests from forks, only build Jenkinsfiles from users with write access (GitHub Branch Source trust settings)
- Never print secrets; use withCredentials and rely on masking only as a backup

**Credentials:**
- Scope credentials to folders, not the global store
- Prefer short-lived cloud credentials (OIDC, Vault) over stored keys
- Rotate any credential that has been in Jenkins for a long time

**Agents:**
- Use ephemeral agents (Kubernetes or cloud agents) that are destroyed after each build
- Separate agent pools by trust level; never run untrusted PR builds on agents that hold production credentials
- Connect agents over WebSocket or TLS

**Monitoring:**
- Send audit logs (Audit Trail plugin) and build logs to the SIEM
- Alert on new admins, script console use, credential changes, and plugin installs

Generate a JCasC configuration, folder-level authorization, a Kubernetes agent template, and a sample Jenkinsfile that use these controls.
