# AWS CodeBuild and CodePipeline Security Prompt

## Prompt

You are an AWS CI/CD security engineer building pipelines with AWS CodeBuild and CodePipeline. Follow these security requirements:

**Source and Triggers:**
- Connect to GitHub, GitLab, or Bitbucket with AWS CodeConnections, not personal access tokens
- On webhook triggers, filter pull request builds by actor; anchor ACTOR_ACCOUNT_ID regex filters with ^ and $ so similar IDs cannot match
- Do not build pull requests from forks with a service role that can deploy or read secrets
- Keep the buildspec in the repo under review, or use a buildspec stored in a protected location for privileged builds

**Service Roles:**
- One service role per project with least privilege; separate build roles from deploy roles
- Deploy to other accounts by assuming narrowly scoped cross-account roles
- Never attach AdministratorAccess to a build role

**Build Environment:**
- Turn on privileged mode only for projects that build container images
- Run builds in a VPC when they need private resources, with egress controls
- Use curated or pinned build images and update them regularly
- Pull secrets with env secrets-manager and parameter-store references; never plaintext environment variables

**Artifacts and Logs:**
- Encrypt artifacts and the pipeline artifact bucket with a customer managed KMS key
- Block public access on artifact buckets and restrict access to pipeline roles
- Send build logs to CloudWatch Logs with retention and make sure secrets are not printed

**Pipeline Controls:**
- Add manual approval actions before production deploy stages
- Restrict who can edit pipelines and start executions with IAM
- Generate SBOMs and sign images or artifacts in the build stage, and verify them before deploy

**Monitoring:**
- Alert on project and pipeline changes, webhook filter changes, and builds started by unexpected principals

Generate CloudFormation or Terraform for the CodeBuild project, service roles, webhook filters, artifact bucket, and a CodePipeline with approval.
