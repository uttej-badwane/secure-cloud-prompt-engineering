# AI Gateway and Guardrails Prompt

## Prompt

You are a platform security engineer building a central AI gateway that all internal apps use to reach LLM providers (cloud model services, Anthropic, OpenAI, open models). Follow these requirements:

**Why a Gateway:**
- One place to enforce authentication, approved models, data rules, quotas, logging, and guardrails
- Apps never hold provider API keys; the gateway does

**Access:**
- Authenticate apps with workload identity or per-app keys stored in a secret manager
- Allow each app only approved models and features (tools, file uploads, web search)
- Set per-app and per-team rate limits and budgets

**Provider Keys:**
- Store provider keys in a secret manager, rotate them, and use separate keys per environment
- Prefer cloud-native access (Bedrock, Vertex AI, Azure AI Foundry with managed identity) where possible

**Data Controls:**
- Detect and redact secrets and personal data in prompts before they leave the organization, based on data class rules
- Block regulated data from going to providers without the right agreements and regions
- Do not cache responses across users unless the cache key includes user and permission scope

**Guardrails:**
- Apply input checks (prompt injection detection, policy filters) and output checks (PII, secrets, unsafe content)
- Use provider guardrails plus your own; treat guardrails as one layer, not the only control

**Gateway Software:**
- If you run an open source gateway (for example LiteLLM, Kong AI Gateway, Envoy AI Gateway), pin versions and verify releases; AI gateway packages have been targeted in supply chain attacks
- Run it with least privilege and private networking

**Logging:**
- Log app, user, model, token counts, cost, guardrail actions, and latency
- Store prompt and response bodies only where policy allows, encrypted, with short retention

**Monitoring:**
- Alert on budget spikes, new models used, guardrail block spikes, and key use outside the gateway

Generate the gateway architecture, configuration for the chosen gateway, a data redaction policy, and dashboards for cost and guardrail events.
