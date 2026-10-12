2026-10-04 08:37

Status: #baby

Tags: [[Podman Runtime Architecture and Isolation]] [[Docker Runtime and Container Lifecycle]]

# OCI Container Runtime

An OCI container runtime creates, starts, and deletes a container process from an OCI runtime bundle. It applies the requested namespaces, mounts, capabilities, cgroups, root filesystem, and process configuration, then invokes the kernel facilities that establish the isolated environment.

runc and crun are interchangeable implementations of this narrow execution layer. A higher-level [[Container Engine]] prepares images, storage, networking, and metadata before calling the runtime, while [[Conmon]] remains available to supervise the resulting workload after the short-lived runtime process exits.

Docker's stack narrows responsibility as it descends: the Engine manages the user-facing lifecycle, containerd manages image transfer and container supervision, and an OCI runtime such as runc performs the tightly scoped act of creating a containerized process from an OCI bundle. That separation allows interoperable low-level runtimes beneath higher-level tooling.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[podmanfordevopssecondedition.pdf]]
