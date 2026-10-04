2026-10-04 08:37

Status: #baby

Tags: [[Buildah Container Image Construction]]

# Red Hat Universal Base Image

Red Hat Universal Base Image is a family of redistributable RHEL-derived container base images. Standard, Minimal, Micro, and Init variants expose different amounts of userland and package-management capability so a builder can choose between convenience, size, and runtime requirements.

The Standard image supplies a broad environment, Minimal reduces packages and uses `microdnf`, Micro omits a package manager for a smaller attack surface, and Init includes systemd-oriented behavior for workloads that need it. A [[Multi-Stage Docker Build]] can compile in a richer variant and copy only the application into a smaller runtime variant.

# References

[[podmanfordevopssecondedition.pdf]]
