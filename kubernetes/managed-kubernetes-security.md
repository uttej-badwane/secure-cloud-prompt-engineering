# Managed Kubernetes (EKS, AKS, GKE) Security Prompt

## Prompt

You are a cloud security engineer building managed Kubernetes clusters on Amazon EKS, Azure AKS, or Google GKE. Workload-level hardening lives in k8s-security.md; this prompt covers the cloud layer. Follow these security requirements:

**Control Plane Access:**
- Use a private API endpoint, or restrict the public endpoint to known CIDRs
- Use cloud IAM for cluster authentication and keep cluster-admin grants to a small break-glass group
- EKS: use access entries and access policies instead of the aws-auth ConfigMap
- AKS: enable Entra ID integration with Azure RBAC and disable local accounts
- GKE: use Google Groups for RBAC and avoid legacy basic auth and client certificates

**Workload Identity:**
- EKS: use EKS Pod Identity or IRSA
- AKS: use Microsoft Entra Workload ID (pod-managed identity is deprecated)
- GKE: use Workload Identity Federation for GKE
- Block pod access to the node metadata service (IMDSv2 hop limit 1 on EKS, GKE metadata server, AKS network policy)
- Never put cloud keys in Kubernetes Secrets

**Nodes:**
- Use hardened, minimal node images (Bottlerocket, Azure Linux, Container-Optimized OS)
- Enable automatic node upgrades or managed node groups and stay on a supported Kubernetes version
- Use shielded or secure boot nodes where offered
- Keep nodes in private subnets with no public IPs
- Consider EKS Auto Mode, GKE Autopilot, or AKS Automatic to reduce node management

**Secrets and Encryption:**
- Encrypt Kubernetes Secrets with a customer-managed KMS key (EKS envelope encryption, AKS KMS etcd encryption, GKE application-layer secrets encryption)
- Use the Secrets Store CSI driver or External Secrets Operator with the cloud secret manager

**Network:**
- Enable a network policy engine (Cilium, Calico, or the provider option) and default-deny policies
- Use internal load balancers for internal services
- Restrict egress from the cluster through NAT or a firewall with logging

**Logging and Threat Detection:**
- Enable control plane audit logs (EKS control plane logging, AKS diagnostic settings, GKE Cloud Audit Logs)
- Enable runtime threat detection (GuardDuty EKS Protection and Runtime Monitoring, Defender for Containers, GKE Security Posture / Container Threat Detection)
- Alert on new cluster-admin bindings, exec into pods, and privileged pod creation

**Supply Chain:**
- Pull images only from your private registry (ECR, ACR, Artifact Registry)
- Enforce signature verification with Binary Authorization, Ratify, or Kyverno/Sigstore policy

**Benchmarks:**
- Follow the CIS Amazon EKS, CIS Azure AKS, or CIS Google GKE Benchmark for the managed layer

Generate Terraform for the chosen provider that applies these controls, and list the settings that cannot be changed after cluster creation.
