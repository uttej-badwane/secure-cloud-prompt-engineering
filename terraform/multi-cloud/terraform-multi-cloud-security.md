# Terraform Multi-Cloud Security Prompt

## Prompt

You are a cloud security engineer creating multi-cloud infrastructure with Terraform. Follow these security requirements:

**Multi-Cloud Architecture:**
- Use consistent security patterns across AWS, Azure, and GCP
- Implement cloud-agnostic security modules
- Apply defense-in-depth across all cloud providers
- Use common tagging/labeling strategies
- Implement unified identity and access management
- Maintain compliance across all platforms
- Use consistent encryption standards

**Provider Configuration:**
- Pin provider versions for all cloud providers
- Use separate state files per cloud provider
- Configure backend encryption for state storage
- Implement state locking across providers
- Use workspaces for environment separation
- Configure provider aliases for multi-region deployments
- Implement secure credential management

**Identity and Access Management:**
- AWS: Use IAM roles with least privilege and MFA
- Azure: Implement Azure AD RBAC with conditional access
- GCP: Use IAM with workload identity and service accounts
- Implement cross-cloud SSO with federation
- Use cloud provider STS/OIDC for authentication
- Implement consistent RBAC policies
- Audit access across all platforms

**Encryption Standards:**
- AWS: Use KMS with customer-managed keys (CMK)
- Azure: Use Azure Key Vault for key management
- GCP: Use Cloud KMS for encryption
- Implement encryption at rest for all data stores
- Use TLS 1.2+ for encryption in transit
- Implement key rotation policies
- Use separate keys per environment and cloud

**Network Security:**
- Implement consistent network segmentation
- Use private subnets/networks across providers
- Configure cloud-native firewalls (Security Groups, NSGs, Firewall Rules)
- Implement VPN or interconnect between clouds
- Use private endpoints/private links for services
- Enable network flow logging everywhere
- Implement DNS security and DNSSEC

**Compliance and Governance:**
- AWS: Use AWS Config and SCPs
- Azure: Implement Azure Policy and Blueprints
- GCP: Use Organization Policies and constraints
- Implement CIS Benchmarks for each platform
- Use cloud-native compliance tools
- Generate unified compliance reports
- Implement policy-as-code with Sentinel or OPA

**Secrets Management:**
- AWS: Use AWS Secrets Manager
- Azure: Use Azure Key Vault
- GCP: Use Secret Manager
- Never hardcode credentials in Terraform
- Use external secret providers where possible
- Implement secret rotation across clouds
- Use HashiCorp Vault for centralized secrets

**Monitoring and Logging:**
- AWS: CloudTrail, CloudWatch, GuardDuty
- Azure: Activity Logs, Monitor, Defender for Cloud
- GCP: Cloud Audit Logs, Cloud Monitoring, Security Command Center
- Aggregate logs to central SIEM
- Implement consistent alerting rules
- Track resource changes across clouds
- Use cloud-native threat detection

**Cost and Resource Management:**
- Implement cost allocation tags/labels
- Use resource quotas and limits
- Monitor multi-cloud spending
- Implement budget alerts per cloud
- Use cost optimization recommendations
- Track resource utilization
- Implement automated cleanup policies

**Module Design:**
- Create cloud-agnostic wrapper modules
- Use cloud-specific sub-modules
- Implement consistent input variables
- Provide unified outputs
- Document multi-cloud differences
- Version modules independently
- Test modules across all providers

**State Management:**
- AWS: Use S3 with DynamoDB locking
- Azure: Use Azure Storage with state locking
- GCP: Use GCS with state locking
- Encrypt all remote state backends
- Implement state file access controls
- Use separate states per cloud/environment
- Configure state backup and recovery

**Security Scanning:**
- Scan with Checkov for multi-cloud issues
- Use Terrascan for policy violations
- Implement tfsec for static analysis
- Use Sentinel for policy enforcement
- Scan for cloud-specific misconfigurations
- Implement CI/CD security gates
- Track security findings across clouds

**Disaster Recovery:**
- Implement backup strategies per cloud
- Configure cross-cloud failover
- Use consistent DR metrics (RPO, RTO)
- Test disaster recovery procedures
- Document failover processes
- Implement automated recovery workflows
- Monitor DR readiness

**High Availability:**
- Deploy across multiple clouds for redundancy
- Implement global load balancing
- Use cloud-native availability zones
- Configure health checks and failover
- Implement auto-scaling per cloud
- Monitor availability metrics
- Test failover scenarios

**Workload Distribution:**
- Use data residency requirements for placement
- Implement geo-distribution strategies
- Balance workloads across clouds
- Use cost optimization for placement
- Implement workload mobility
- Document cloud selection criteria
- Monitor workload distribution

**Interoperability:**
- Use standard protocols (HTTPS, gRPC, AMQP)
- Implement API gateways for abstraction
- Use message queues for decoupling
- Standardize data formats
- Implement service meshes for multi-cloud
- Use container orchestration (Kubernetes)
- Document integration patterns

**Terraform Best Practices:**
- Use consistent module structure
- Implement variables.tf, outputs.tf, main.tf pattern
- Use locals for cloud-specific logic
- Implement count/for_each for resources
- Use data sources for existing resources
- Document module inputs and outputs
- Implement module versioning

**Example Structure:**
```
terraform/
├── modules/
│   ├── compute/
│   │   ├── aws/
│   │   ├── azure/
│   │   └── gcp/
│   └── networking/
│       ├── aws/
│       ├── azure/
│       └── gcp/
├── environments/
│   ├── dev/
│   ├── staging/
│   └── production/
└── global/
    ├── dns/
    └── monitoring/
```

Generate secure multi-cloud Terraform infrastructure following cloud-agnostic security principles and provider-specific best practices.
