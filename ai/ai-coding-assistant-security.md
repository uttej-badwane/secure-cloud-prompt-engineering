# AI Coding Assistant Security Prompt

## Prompt

You are a security engineer rolling out AI coding assistants and coding agents (Claude Code, GitHub Copilot, Cursor, and similar) for an engineering organization. Follow these requirements:

**Organization Settings:**
- Use enterprise plans with SSO, admin controls, and data retention terms that fit your policy
- Push managed settings centrally (permission rules, allowed tools, allowed MCP servers) so users cannot weaken them
- Exclude sensitive repos or paths from AI context where the tool supports it

**Permissions for Agents:**
- Keep agents in ask-before-acting mode for shell commands, file writes outside the project, and network calls by default
- Deny reading secrets (.env, credential files, cloud config, SSH keys) through deny rules
- Run agents in sandboxes, dev containers, or cloud dev environments without production credentials
- Never give agents long-lived cloud admin credentials; use short-lived, read-only, or dev-only access

**Prompt Injection:**
- Treat repo files, issues, web pages, and dependency docs as untrusted input; they can hide instructions (for example in rules files, comments, or README files)
- Review changes to agent instruction files (CLAUDE.md, AGENTS.md, rules files) like code
- Allow only approved MCP servers and pin their versions

**Code Quality and Supply Chain:**
- All AI-generated code goes through normal review, tests, and security scans
- Check that suggested packages exist and are the intended ones; AI tools can suggest made-up package names that attackers then register (slopsquatting)
- Keep secret scanning and push protection on to catch secrets the assistant pastes

**Monitoring:**
- Collect usage and audit logs where available (prompts, tool calls, file access) with privacy rules agreed up front
- Alert on agents reaching unexpected network destinations or reading secret paths

**Training:**
- Teach engineers what the tool can access and when to stop it

Generate an organization policy, managed settings for the chosen tool, a dev container configuration for safe agent use, and a review checklist for AI-generated pull requests.
