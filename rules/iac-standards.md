# IaC Coding Standards

These rules apply when writing or modifying Infrastructure as Code in this repository.

## Terraform

### Required on Every Resource

```hcl
# Tags — required for all taggable resources
tags = {
  Environment = var.environment   # dev | staging | prod
  Owner       = var.owner         # team or individual
  Project     = var.project_name
  ManagedBy   = "terraform"
}

# Lifecycle — protect stateful resources in production
lifecycle {
  prevent_destroy = true          # for databases, S3 buckets, KMS keys
}
```

### Variables Must Have Types and Descriptions

```hcl
variable "environment" {
  type        = string
  description = "Deployment environment (dev, staging, prod)"
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}
```

### Backend Must Be Remote with Encryption and Locking

```hcl
terraform {
  backend "s3" {
    bucket         = "company-tf-state"
    key            = "project/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}
```

### Outputs Must Not Expose Secrets

```hcl
output "db_password" {
  value     = aws_db_instance.main.password
  sensitive = true   # required for any secret output
}
```

## Kubernetes

### Every Deployment Must Have a securityContext

```yaml
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000
  containers:
    - name: app
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
```

### Resource Limits Are Required

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
  limits:
    cpu: "500m"
    memory: "512Mi"
```

### Image Tags Must Be Pinned to a Digest

```yaml
image: nginx@sha256:abc123...  # not nginx:latest or nginx:1.25
```

## Docker

### Use Non-Root User

```dockerfile
RUN addgroup --system app && adduser --system --ingroup app app
USER app
```

### Pin Base Image Digest

```dockerfile
FROM node:20-alpine@sha256:abc123...
```

### Use .dockerignore

Always include a `.dockerignore` that excludes:
```
.git
.env
*.tfvars
*_rsa
*_ed25519
node_modules
```

## CI/CD (GitHub Actions)

### Pin Action Versions to SHA

```yaml
- uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  # v4.2.2
```

### Use Least-Privilege Permissions

```yaml
permissions:
  contents: read      # only what the job needs
  id-token: write     # for OIDC only
```

### Never Use Long-Lived Credentials

Use OIDC for cloud authentication:
```yaml
- uses: aws-actions/configure-aws-credentials@...
  with:
    role-to-assume: arn:aws:iam::123456789012:role/github-actions-role
    aws-region: us-east-1
```

## General

- **No inline secrets** — use AWS Secrets Manager, HashiCorp Vault, or GitHub Secrets
- **No default VPCs** — always create explicit VPCs with documented CIDR ranges
- **No `latest` tags** — pin all image, action, and module versions
- **No `*` in IAM** — scope all policies to specific actions and resources
