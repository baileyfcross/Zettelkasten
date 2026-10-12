2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Virtualization and Containers]]

# HostProcess Container

A HostProcess container is a privileged Windows container that runs with direct access to the host namespace rather than ordinary application-container isolation. It is designed for cluster-management and node-level workloads that must interact with host networking, storage, services, or devices while still being packaged and deployed as a container image.

Because the process can affect the node, HostProcess is not a stronger sandbox for untrusted code. Its image and orchestrator permissions should be treated like administrative software installed on every eligible host. Narrow scheduling, controlled service accounts, signed and scanned images, and auditable deployment are essential. The model is valuable when operational agents need container lifecycle and distribution but cannot perform their function from inside a normal isolated container.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
