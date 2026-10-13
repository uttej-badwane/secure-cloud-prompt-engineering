# Contributing

Thanks for helping make this the most useful set of cloud security prompts. This guide keeps the library consistent and accurate.

## What to Contribute

- New prompts for services, tools, or security tasks that are not covered yet
- Fixes for outdated guidance (renamed services, deprecated settings, new defaults)
- Corrections to facts, control IDs, or tool names

Check the folder README first to avoid duplicates. If a topic fits an existing prompt, improve that prompt instead of adding a new one.

## Writing a Prompt

Start from [docs/prompt-template.md](docs/prompt-template.md).

- **One topic per prompt.** A service, a tool, or a task.
- **Role first.** Open with "You are a ... engineer ..." and the goal.
- **Specific controls.** Name exact settings, policy keys, flags, and commands. Avoid "follow best practices".
- **Threat-driven.** Prefer controls that stop real attacks. Mention a real incident when it explains why a control matters.
- **Plain language.** Short bullets, simple words, no em dashes, no marketing language.
- **Current facts only.** Use current product names and settings. If something was renamed or deprecated, say so.
- **Ask for output.** End with a "Generate ..." line that says what the AI should produce (code, policies, runbooks, tables).
- **Safe scope.** Testing and offensive prompts must limit work to systems the user owns or is authorized to test.
- **Size.** Aim for 30 to 60 lines. Split prompts that grow much larger.

## File Rules

- Put the prompt in the right folder; create a new folder only for a new domain
- Name files in kebab-case ending with `-security.md` where it fits (for example `cognito-security.md`)
- Use bold section headings ending with a colon (`**Access Control:**`); the index script reads them
- Run `python3 scripts/build_index.py` to update the folder README index, and commit the result

## Pull Requests

- One topic or folder per pull request
- In the description, explain what changed, why, and how you checked the facts (link to vendor docs or changelogs)
- Keep fixes to existing prompts separate from new prompts

## Accuracy

If you are not sure a fact is current, leave it out or link the source in the pull request. Wrong security guidance is worse than missing guidance.
