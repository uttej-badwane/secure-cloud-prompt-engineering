# Security-First Rules

These rules apply to all interactions in this repository. Follow them without exception.

## 1. Never Generate Insecure IaC by Default

When writing or suggesting infrastructure code, always apply these defaults:

- **Encryption**: Enable encryption at rest and in transit unless the user explicitly says otherwise
- **Access**: Default to least privilege; never use `*` for IAM actions or resources without explanation
- **Network**: Default to private (no public IPs, no 0.0.0.0/0 ingress) unless the use case requires it
- **Secrets**: Never hardcode secrets, passwords, or tokens in any file — always reference a secret manager

## 2. Always Cite Sources for Security Claims

When you state that something is a security risk, cite the specific standard:
- CIS Benchmark section (e.g., "CIS AWS 2.1.2")
- NIST control (e.g., "NIST 800-53 AC-3")
- OWASP IaC recommendation
- Vendor security best practice document

## 3. Severity Must Be Accurate

Use these severity levels consistently and conservatively:

| Severity | Criteria |
|---|---|
| CRITICAL | Direct exploitation path, no auth required, or secrets exposed |
| HIGH | Significant risk with clear attack scenario requiring 1-2 steps |
| MEDIUM | Best practice violation that increases attack surface |
| LOW | Defense-in-depth improvement with minimal direct risk |
| INFO | Observation; no security impact |

Do not inflate severity to appear thorough. Accurate severity helps engineers prioritize correctly.

## 4. Always Provide Working Remediation

- Every finding must include a working code snippet showing the fix
- Code must be syntactically correct for the IaC type
- If the fix requires a variable or resource defined elsewhere, show the reference pattern and note the dependency
- Do not say "add encryption" — show exactly which Terraform resource block, attribute, and value to add

## 5. Never Break Working Infrastructure

When fixing findings:
- Make the minimal change needed to resolve the specific issue
- Do not refactor, rename, or reorganize surrounding code
- Do not remove resource configurations unless they are genuinely unused
- If the fix is destructive (e.g., recreates a resource), warn the user explicitly

## 6. Respect Scope

- Only review files the user explicitly provides or that are in the current directory
- If a finding is in a referenced module or dependency (not in the reviewed scope), note it as "out of scope — verify separately"
- Do not make assumptions about files you haven't read

## 7. Positive Findings Are Required

Every security review must include a **Positive Findings** section. Engineers deserve
to know what they did right, not just what to fix. This builds trust and encourages
security-first habits.

## 8. No Alarmist Language

Write factually. Avoid:
- "This is extremely dangerous"
- "This will definitely be exploited"
- "This is a disaster waiting to happen"

Instead:
- "An unauthenticated attacker with network access could..."
- "This configuration allows any principal in the account to..."
- "Without encryption, data is stored in plaintext on disk"
