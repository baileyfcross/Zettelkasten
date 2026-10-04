2026-10-04 08:37

Status: #baby

Tags: [[Podman Runtime Architecture and Isolation]]

# OCI Container Runtime

An OCI container runtime creates, starts, and deletes a container process from an OCI runtime bundle. It applies the requested namespaces, mounts, capabilities, cgroups, root filesystem, and process configuration, then invokes the kernel facilities that establish the isolated environment.

runc and crun are interchangeable implementations of this narrow execution layer. A higher-level [[Container Engine]] prepares images, storage, networking, and metadata before calling the runtime, while [[Conmon]] remains available to supervise the resulting workload after the short-lived runtime process exits.

# References

[[podmanfordevopssecondedition.pdf]]
