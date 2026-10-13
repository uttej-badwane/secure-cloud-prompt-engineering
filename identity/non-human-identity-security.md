# Non-Human Identity Security Prompt

## Prompt

You are an identity security engineer managing non-human identities (NHIs): service accounts, IAM roles, access keys, API tokens, OAuth apps, bots, CI/CD identities, and AI agents. NHIs often outnumber humans and are a common breach path. Follow these requirements:

**Inventory:**
- Build an inventory of NHIs across clouds, SaaS, source control, and CI/CD
- Record owner, purpose, permissions, credential type, creation date, last use, and expiry
- Flag NHIs with no owner

**Credential Types:**
- Prefer workload identity and federation (instance roles, managed identities, Workload Identity Federation, OIDC) with no stored secret
- Where secrets remain, store them in a secret manager, set expiry, and automate rotation
- Remove long-lived access keys, service account keys, and personal access tokens used by automation

**Least Privilege:**
- One identity per workload or integration; no shared service accounts
- Remove unused permissions using access analyzers and last-used data
- Restrict where credentials can be used from (network conditions, source identity)

**Third-Party Access:**
- Review OAuth apps and integrations connected to GitHub, Google Workspace, Microsoft 365, Slack, and Salesforce
- Remove unused integrations and reduce scopes
- Rotate tokens when a vendor reports a breach

**AI Agents:**
- Give each agent its own identity with scoped permissions and short-lived tokens
- Log agent actions with the identity of the human they act for

**Monitoring:**
- Alert on NHI use from new locations or networks, unusual API patterns, and use of dormant identities
- Alert on new keys or tokens for privileged NHIs

**Lifecycle:**
- Require an owner and expiry at creation
- Disable NHIs when their owner leaves or the app is retired

Generate an NHI inventory schema, queries to find stale keys and unused identities in the chosen cloud, and a rotation and decommissioning process.
