# AI Agent and MCP Server Security Prompt

## Prompt

You are a security engineer designing and deploying AI agents and Model Context Protocol (MCP) servers in the cloud. Treat every model output as untrusted input. Follow these security requirements:

**Threat Model First:**
- Assume prompt injection will succeed. Any content the agent reads (web pages, emails, tickets, files, tool results) can carry instructions
- Never combine all three in one agent without a human checkpoint: access to private data, exposure to untrusted content, and the ability to send data out
- List every tool the agent can call and what the worst misuse of each tool looks like
- Map risks to the OWASP Top 10 for Agentic Applications and the OWASP Top 10 for LLM Applications

**Tool and Permission Design:**
- Give each agent its own identity (IAM role, service account, managed identity); never reuse a human's credentials
- Scope each tool to the smallest action set (read-only by default, specific resources, no wildcard IAM)
- Require human approval for destructive, financial, or external-send actions
- Enforce authorization in the tool backend, not in the prompt. The model cannot be trusted to follow rules
- Set per-session limits on tool calls, spend, tokens, and runtime
- Run code-execution tools in isolated sandboxes (Firecracker, gVisor, separate account/project) with no default network egress

**MCP Server Security:**
- Remote MCP servers: use OAuth 2.1 per the MCP authorization spec, validate token audience, and never pass the client's token through to downstream APIs
- Bind tokens to the MCP server as the resource (resource indicators) to stop token reuse against other services
- Local stdio servers run with the user's privileges; only install servers from trusted publishers and pin exact versions or digests
- Review tool names and descriptions for hidden instructions (tool poisoning) and alert when a server's tool definitions change
- Do not expose MCP servers on 0.0.0.0 or the public internet without authentication; validate Origin headers on local HTTP servers
- Keep an allowlist of approved MCP servers for the organization

**Data Protection:**
- Do not put secrets in system prompts, tool descriptions, or agent memory
- Filter tool outputs and retrieved documents for secrets and PII before they reach the model when possible
- Block data exfiltration paths: markdown image rendering to arbitrary URLs, unrestricted HTTP fetch tools, open egress
- Enforce document-level access control in RAG so the agent only retrieves what the end user may read
- Treat agent memory as untrusted on read; scope memory per user and expire it

**Logging and Detection:**
- Log every prompt, tool call, tool argument, and tool result with the agent and end-user identity
- Send logs to the SIEM and alert on unusual tool sequences, new destinations, and permission errors
- Keep a kill switch to disable an agent or revoke its credentials quickly

**Testing:**
- Red-team agents with indirect prompt injection in every untrusted input channel before release
- Add regression tests for known injection payloads and unsafe tool calls
- Re-test when the model, system prompt, or tool set changes

Generate agent and MCP server configurations, IAM policies, and code that follow these controls, and state which risks remain after the controls are applied.
