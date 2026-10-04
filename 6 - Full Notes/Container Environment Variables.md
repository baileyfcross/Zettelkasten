2026-09-27 11:23

Status: #baby

Tags: [[Containerized Microservice Architecture]] [[Podman Container Lifecycle and Storage]]

# Container Environment Variables

Container environment variables provide deploy-time configuration without rebuilding an application image. ASP.NET Core's configuration system can map them into settings such as service addresses, connection strings, or environment names when a container starts.

This separates one immutable image from the environments that run it. Secrets still require protected storage and delivery; placing them in a plain Compose file or committed configuration merely changes where they are exposed.

Podman can pass selected variables with `--env` and also propagates common proxy variables from the host. Runtime variables are therefore appropriate for behavior that differs between deployments, while files, credentials, and values needing stronger controls should use mounts or a protected secret mechanism instead.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[podmanfordevopssecondedition.pdf]]
