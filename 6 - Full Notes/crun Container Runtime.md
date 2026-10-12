2026-10-04 08:37

Status: #baby

Tags: [[Podman Runtime Architecture and Isolation]]

# crun Container Runtime

crun is a compact implementation of the [[OCI Container Runtime]] written in C. Podman can select it to apply an OCI runtime configuration and launch the isolated container process, performing the same execution-layer role that runc performs.

The book highlights crun's small memory footprint and close integration with modern Linux facilities, including cgroup v2. Because the surrounding engine communicates through the [[OCI Runtime Specification]], choosing crun changes the runtime implementation without changing the image format or the high-level Podman workflow.

# References

[[podmanfordevopssecondedition.pdf]]
