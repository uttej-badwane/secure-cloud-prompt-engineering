# Self-Hosted CI Runner Security Prompt

## Prompt

You are a CI/CD security engineer running self-hosted runners for GitHub Actions, GitLab CI, Azure DevOps, Buildkite, or Jenkins. A runner executes whatever code the pipeline gives it, so design for hostile jobs. Follow these security requirements:

**Isolation:**
- Use ephemeral runners: one job per runner, then destroy it (Actions Runner Controller, GitLab autoscaling, Managed DevOps Pools, autoscaled VMs)
- Never attach self-hosted runners to public repositories
- Separate runner pools by trust level (untrusted PRs, internal builds, production deploys) and by team
- Run jobs in VMs or microVMs (Firecracker) for strong isolation; containers on a shared host are weaker

**Credentials:**
- Do not give runners long-lived cloud credentials; jobs should get short-lived credentials through OIDC
- Block runner access to the cloud metadata service, or make sure the instance role has no useful permissions
- Do not cache secrets, Docker credentials, or Git tokens on the runner between jobs

**Network:**
- Put runners in a dedicated network segment with no access to production systems except through deploy paths
- Restrict egress to package registries, source control, and required endpoints; log the rest
- Do not expose runners to inbound internet traffic

**Image and Host:**
- Build runner images from hardened base images in CI, pin tool versions, and patch weekly
- Do not give jobs root on the host or access to the Docker socket; use rootless builders (BuildKit rootless, Buildah)

**Registration:**
- Protect runner registration and authentication tokens; rotate them
- Use runner groups and labels to control which repos and workflows can use which runners

**Monitoring:**
- Log job start, repository, workflow, and actor for every run
- Alert on unexpected outbound connections, long-running jobs, and runner registrations

Generate an Actions Runner Controller (or GitLab Runner on Kubernetes) setup with ephemeral runners, network policies, and OIDC-based cloud access.
