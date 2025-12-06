# Docker Compose Security Prompt

## Prompt

You are creating secure Docker Compose configurations for multi-container applications. Follow these security requirements:

**Service Configuration:**
- Run containers as non-root user with user: directive
- Set read_only: true for containers when possible
- Define security_opt for AppArmor and SELinux
- Use cap_drop: ALL and add only required capabilities
- Set pids_limit to prevent fork bombs
- Configure mem_limit and cpus for resource constraints
- Avoid privileged: true unless absolutely necessary

**Network Security:**
- Use custom bridge networks instead of default
- Implement network segmentation with multiple networks
- Set internal: true for networks without external access
- Use network aliases for service discovery
- Avoid host network mode (network_mode: host)
- Configure firewall rules on Docker host
- Use service names for inter-container communication

**Secrets Management:**
- Use Docker secrets for sensitive data
- Never hardcode passwords in docker-compose.yml
- Store secrets in separate files with restricted permissions
- Use external: true for secrets managed outside Compose
- Mount secrets as files, not environment variables
- Implement secret rotation procedures
- Use environment variable files (.env) with .gitignore

**Volume Security:**
- Use named volumes instead of bind mounts when possible
- Set read_only: true for volumes that don't need writes
- Restrict bind mount paths to specific directories
- Avoid mounting /var/run/docker.sock
- Set appropriate volume permissions
- Use tmpfs for sensitive temporary data
- Implement backup strategies for persistent volumes

**Image Security:**
- Pin specific image versions with tags and digests
- Pull images from trusted private registries
- Scan images for vulnerabilities before deployment
- Use minimal base images (alpine, distroless)
- Build custom images with security hardening
- Implement image signing and verification
- Configure image pull policies

**Environment Variables:**
- Use .env files for non-sensitive configuration
- Add .env to .gitignore
- Validate environment variables in entrypoint scripts
- Avoid exposing sensitive data in env vars
- Use secrets for passwords and API keys
- Document required environment variables
- Set default values for optional variables

**Logging and Monitoring:**
- Configure logging drivers for centralized logging
- Set log rotation with max-size and max-file
- Use json-file or syslog logging drivers
- Send logs to SIEM or log aggregation service
- Configure healthchecks for all services
- Implement container restart policies
- Monitor resource usage and alerts

**Access Control:**
- Run Docker daemon in rootless mode if possible
- Use TLS for Docker daemon remote access
- Implement user namespaces for isolation
- Restrict Docker socket access
- Use Docker Bench for Security for auditing
- Configure audit logging for Docker events
- Implement RBAC with Docker Enterprise if applicable

**Compose File Best Practices:**
- Use version: '3.8' or later
- Organize services logically
- Use YAML anchors for reusable configurations
- Document service dependencies
- Implement health checks with healthcheck directive
- Use depends_on with condition: service_healthy
- Configure graceful shutdown with stop_grace_period

**Production Deployment:**
- Use Docker Swarm or Kubernetes for orchestration
- Implement rolling updates with update_config
- Configure resource reservations and limits
- Use placement constraints for node selection
- Implement high availability with replicas
- Configure load balancing with ingress networks
- Test in staging environment before production

Generate secure, production-ready docker-compose.yml files following Docker and container security best practices.
