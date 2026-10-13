# AWS ECS, Fargate and ECR Security Prompt

## Prompt

You are an AWS security engineer running containers on Amazon ECS (Fargate or EC2) with images in Amazon ECR. Follow these security requirements:

**Task Definitions:**
- Use separate roles: the task execution role pulls images and reads secrets; the task role holds only the app's permissions
- Never set privileged = true; drop Linux capabilities you do not need
- Set readonlyRootFilesystem = true and run as a non-root user
- Inject secrets with the secrets block (valueFrom Secrets Manager or Parameter Store), not plaintext environment variables
- Set CPU and memory limits on every container

**Network:**
- Use awsvpc network mode with a security group per service
- Run tasks in private subnets with no public IP
- Use VPC endpoints for ECR, S3, CloudWatch Logs, and Secrets Manager so tasks never need internet for AWS APIs
- Put internet-facing services behind an ALB with WAF

**ECS Exec and Access:**
- Enable ECS Exec only where needed, log sessions to CloudWatch or S3 with KMS encryption, and restrict ecs:ExecuteCommand
- On EC2 launch type, block task access to instance metadata (ECS_AWSVPC_BLOCK_IMDS or IMDSv2 hop limit 1)

**ECR:**
- Make repositories private and set image tag mutability to IMMUTABLE
- Enable enhanced scanning with Amazon Inspector and act on findings
- Encrypt repositories with a customer managed KMS key for sensitive images
- Use repository policies scoped to specific accounts and roles
- Use lifecycle policies to remove old images
- Use pull through cache rules for public images instead of pulling from the internet at runtime
- Sign images (AWS Signer with Notation or cosign) and verify them before deploy

**Deployment:**
- Reference images by digest in task definitions
- Use deployment circuit breakers and rollback
- Keep the ECS agent and EC2 container instances patched, or prefer Fargate

**Monitoring:**
- Send container logs to CloudWatch Logs with retention and KMS
- Enable GuardDuty Runtime Monitoring for ECS
- Enable Container Insights for resource anomalies

Generate task definitions, IAM roles, ECR settings, and Terraform that apply these controls.
