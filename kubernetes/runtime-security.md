# Kubernetes Runtime Security Prompt

## Prompt

You are a Kubernetes security engineer detecting and limiting attacks inside running containers. Follow these security requirements:

**Prevention at Runtime:**
- Apply seccomp RuntimeDefault to all pods and custom profiles for sensitive workloads (Security Profiles Operator can record them)
- Apply AppArmor or SELinux profiles
- Use read-only root filesystems so attackers cannot drop tools
- Use sandboxed runtimes (gVisor, Kata Containers) through RuntimeClass for untrusted or multi-tenant code
- Remove shells and package managers from production images

**Detection:**
- Deploy a runtime detection tool (Falco, Tetragon, KubeArmor, or a cloud service like GuardDuty Runtime Monitoring, Defender for Containers, GKE Container Threat Detection)
- Detect: shells in containers, unexpected process execution, writes to binaries, crypto miners, reverse shells, access to service account tokens, and calls to the metadata service
- Detect container drift: binaries that were not in the image
- Use Kubernetes audit logs to detect exec, secret reads, privileged pod creation, and RBAC changes

**Response:**
- Route alerts to the SOC with pod, node, image digest, and namespace context
- Isolate a suspicious pod with a deny-all NetworkPolicy and label, keep it for forensics, and replace it from a clean image
- Cordon the node if host compromise is possible

**Tuning:**
- Start with the vendor default rules, then tune per namespace
- Track false positives and suppressions in Git

**Coverage:**
- Run the agent on every node, including system node pools
- Monitor agent health and alert when it stops reporting

Generate Falco or Tetragon rules for the detections above, a seccomp profile example, and a RuntimeClass for gVisor.
