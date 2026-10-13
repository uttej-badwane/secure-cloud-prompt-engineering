# Self-Managed Kubernetes Cluster Hardening Prompt

## Prompt

You are a Kubernetes security engineer hardening a self-managed cluster (kubeadm, RKE2, k3s, Talos, or on-premises). For EKS, AKS, and GKE use managed-kubernetes-security.md. Follow these security requirements:

**API Server:**
- Disable anonymous access, or limit it to health endpoints only
- Use --authorization-mode=Node,RBAC
- Enable admission plugins including NodeRestriction
- Configure an audit policy that logs metadata for all requests and request bodies for sensitive resources, without logging secret values
- Encrypt Secrets at rest with a KMS v2 provider
- Disable profiling and do not expose the API server to the internet; restrict with firewall rules or a VPN
- Use OIDC for user authentication; do not hand out long-lived admin client certificates

**etcd:**
- Require TLS with client certificate auth for clients and peers
- Restrict network access to API servers only
- Encrypt backups and store them off the cluster

**Kubelet:**
- Set anonymous auth to false and authorization mode to Webhook
- Disable the read-only port (readOnlyPort: 0)
- Enable certificate rotation and protectKernelDefaults
- Restrict kubelet access to the control plane network

**Nodes:**
- Use a minimal, immutable OS (Talos, Bottlerocket, Flatcar) or a CIS-hardened Linux image
- Keep the container runtime (containerd, CRI-O, runc) patched; runc escapes have happened (for example CVE-2024-21626)
- Restrict SSH to break-glass with logging

**Upgrades and Validation:**
- Stay on a supported Kubernetes minor version and patch monthly
- Run kube-bench against the CIS Kubernetes Benchmark and fix findings
- Back up and test restore of etcd and cluster PKI

Generate kubeadm or RKE2 configuration, an audit policy, an EncryptionConfiguration, and a kubelet config that apply these controls.
