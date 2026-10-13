# Cloud Privileged Access Management Prompt

## Prompt

You are an identity security engineer designing privileged access for cloud administrators, SREs, and break-glass scenarios. Follow these requirements:

**No Standing Admin Access:**
- Use just-in-time elevation: AWS IAM Identity Center with a JIT tool (for example TEAM), Microsoft Entra PIM, Google Cloud Privileged Access Manager, or a PAM platform
- Require justification, ticket reference, and approval for production admin roles
- Limit elevation duration (for example 1 to 4 hours) and log every activation

**Admin Identities:**
- Separate admin accounts from daily accounts, or use role elevation inside the same identity with stronger MFA
- Require phishing-resistant MFA and managed devices for any privileged session
- Use privileged access workstations or hardened browsers for tier-zero administration

**Break-Glass:**
- Keep two or more emergency accounts per cloud and IdP, with credentials split and stored offline
- Exclude them from policies that could lock everyone out, but alert on every sign-in
- Test break-glass access every quarter

**Least Privilege:**
- Define admin roles by task (network admin, security admin, database admin), not one super role
- Use permission boundaries and guardrail policies so even admins cannot disable logging or security tooling

**Sessions:**
- Record privileged sessions to servers and databases (Session Manager logging, Teleport, Boundary, or PAM recording)
- Use short-lived credentials and certificates

**Review:**
- Review who can elevate to what every quarter
- Alert on elevation outside business hours, unusual elevation frequency, and changes to elevation policies

Generate a privileged role catalog, JIT configuration for the chosen cloud, break-glass procedures, and detection rules for privileged activity.
