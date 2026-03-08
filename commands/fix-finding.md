---
name: fix-finding
description: Auto-fix a specific security finding by editing the IaC file directly
---

Apply a targeted fix to a specific security finding identified in a prior review.

## Steps

1. Parse the argument — accept either:
   - A finding number from the most recent report (e.g., `/fix-finding 3`)
   - A description of what to fix (e.g., `/fix-finding "s3 public access" terraform/main.tf`)

2. Read the relevant file(s) to understand current state.

3. Apply the minimal, correct fix:
   - Do not refactor unrelated code
   - Preserve existing formatting and style
   - Add an inline comment explaining why the change was made (if non-obvious)

4. Show a diff of the change before applying it and ask for confirmation.

5. After applying, re-check the fixed lines against the security checklist to confirm the
   finding is resolved and no new issues were introduced.

6. Report: "Fixed [finding title] in [file:line]. Control [framework ID] now satisfied."

## Safety Rules

- Never delete resource definitions — only add security controls to existing ones
- Never change resource names, IDs, or tags unless the finding explicitly requires it
- If the fix requires secret values (e.g., KMS key ARN), use a `TODO` placeholder
  and instruct the user to fill it in
- If unsure about the correct fix, explain the options and ask the user to choose

## Usage

```
/fix-finding 2
/fix-finding "open security group" terraform/vpc.tf
/fix-finding "container running as root" kubernetes/deployment.yaml
```
