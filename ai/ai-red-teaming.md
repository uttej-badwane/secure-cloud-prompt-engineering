# AI Red Teaming Prompt

## Prompt

You are an AI security tester planning a red team exercise against your organization's own LLM application or agent before release. Test only systems you own or are authorized to test. Follow these requirements:

**Scope:**
- Describe the system: model, system prompt, tools, data sources, memory, users, and output channels
- List what must never happen (data leak across users, unauthorized actions, harmful content, policy violations)
- Get written approval and agree on test accounts and data

**Test Areas (map to the OWASP Top 10 for LLM and Agentic Applications, and MITRE ATLAS):**
- Direct prompt injection and jailbreaks against the system prompt and policies
- Indirect prompt injection through every untrusted input: documents, web pages, emails, tickets, tool outputs
- Data leakage: system prompt disclosure, other users' data, secrets in context, RAG permission bypass
- Tool misuse: getting the agent to call tools with harmful arguments, chaining tools, escalating permissions
- Exfiltration channels: markdown images, links, outbound HTTP tools
- Excessive agency: actions without confirmation
- Denial of wallet: prompts that cause runaway loops, long outputs, or expensive tool calls
- Output handling: model output reaching HTML, SQL, shells, or code execution

**Tools:**
- Automated: PyRIT, garak, promptfoo, or Inspect for repeatable attack suites
- Manual: creative multi-turn attacks; automation alone misses many issues

**Measuring:**
- Record attack success rate per category and the exact prompts that worked
- Rate severity by real impact, not just policy breaks

**After Testing:**
- Fix root causes (permissions, architecture) before adding prompt rules
- Turn successful attacks into a regression suite that runs in CI on every model, prompt, or tool change
- Retest after fixes

Generate a red team plan, an automated test configuration for the chosen tool, and a findings report template for the system I describe.
