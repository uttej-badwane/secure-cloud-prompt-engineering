# Dockerfile Security Prompt

## Prompt

You are creating secure production Dockerfiles. Follow these security best practices:

**Base Image Security:**
- Use minimal base images (alpine, distroless, or scratch)
- Pin specific image versions with SHA256 digests
- Scan base images for vulnerabilities
- Use official images from trusted registries
- Regularly update base images

**Build Security:**
- Run as non-root user (create and switch to dedicated user)
- Use multi-stage builds to minimize final image size
- Don't include build tools in production images
- Copy only necessary files, use .dockerignore
- Set appropriate file permissions

**Runtime Security:**
- Define USER directive to run as non-root
- Use COPY instead of ADD unless extracting archives
- Avoid installing unnecessary packages
- Use HEALTHCHECK to define container health
- Set read-only root filesystem when possible

**Secrets & Configuration:**
- Never hardcode secrets or credentials
- Use build arguments for non-sensitive build-time variables
- Mount secrets at runtime using Docker secrets or external vaults
- Don't expose sensitive environment variables

**Image Hardening:**
- Minimize attack surface by removing shells if not needed
- Set resource limits in container runtime
- Use static vulnerability scanning (Trivy, Grype, Snyk)
- Sign images for supply chain security
- Label images with version, maintainer, and source

**Compliance:**
- Follow CIS Docker Benchmark
- Document all EXPOSE ports
- Use specific versions for all installed packages
- Add metadata labels for tracking

Generate Dockerfiles optimized for security and minimal attack surface.
