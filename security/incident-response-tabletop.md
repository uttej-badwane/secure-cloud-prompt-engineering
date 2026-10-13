# Cloud Incident Response Tabletop Exercise Prompt

## Prompt

You are an incident response lead designing a tabletop exercise for a cloud security incident. The goal is to test people, decisions, and runbooks, not tools. Follow these requirements:

**Planning:**
- Pick one scenario that matches real risk for the organization, for example:
  - Leaked CI/CD credentials used to create admin roles
  - Ransomware in a cloud account with backup deletion attempts
  - Compromised identity provider admin account
  - Malicious package in a production dependency
  - Prompt injection causing an AI agent to leak customer data
  - Public storage bucket with regulated data found by a researcher
- Set objectives (for example: decide containment within 30 minutes, test legal notification steps)
- Invite engineering, security, legal, communications, leadership, and key vendors as needed

**Scenario Design:**
- Write 4 to 6 injects that unfold over time, each with new facts and pressure
- Include at least one conflicting signal and one decision with business trade-offs (for example, shutting down a revenue system)
- Base injects on real log examples and tools the team uses

**Running the Exercise:**
- Assign a facilitator and a note taker
- Ask who decides, what they do, what they need, and how long it takes
- Track gaps in runbooks, access, logs, and contacts

**Notifications:**
- Walk through regulatory and contractual timelines (for example GDPR 72 hours, SEC 4 business days after materiality, HIPAA, state breach laws, CIRCIA for critical infrastructure)

**After Action:**
- Write an after-action report with what worked, gaps, owners, and due dates
- Update runbooks and schedule the next exercise

Generate a full tabletop package for the chosen scenario: objectives, participant list, injects with timing, facilitator questions, and an after-action report template.
