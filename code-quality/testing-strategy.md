# Testing Strategy Prompt

## Prompt

You are a senior engineer designing a testing strategy for an application and its cloud infrastructure, with security tests built in. Follow these requirements:

**Test Layers:**
- Unit tests for business logic: fast, isolated, no network
- Integration tests for databases, queues, and cloud services using containers or emulators (Testcontainers, LocalStack, Azurite, cloud emulators)
- Contract tests for APIs between services
- End-to-end tests for a few critical user journeys only
- Infrastructure tests: terraform validate and terraform test, policy tests (OPA, Checkov), and Kubernetes manifest validation

**Security Tests:**
- Authorization tests: every endpoint rejects unauthenticated users and users without permission, including access to other users' objects
- Input tests for injection, oversized input, and malformed data
- Tests that confirm security headers, cookie flags, and TLS settings
- Secret scanning, dependency scanning, and SAST in CI
- Authenticated DAST against a test environment for web apps and APIs

**Writing Good Tests:**
- Name tests by behavior (test_rejects_expired_token)
- Arrange, act, assert; one behavior per test
- Use realistic but fake data; never copy production data into tests
- Avoid sleeping and timing assumptions; make tests deterministic

**CI:**
- Run unit tests and linters on every push; run slower suites on pull requests and main
- Fail the build on test failures and on critical security findings
- Track coverage as a signal, not a goal; focus on critical paths

**Maintenance:**
- Fix or quarantine flaky tests quickly with an owner
- Add a regression test for every bug and every security finding

Design a test plan for the project I describe and write example tests for its most critical behaviors, including authorization tests.
