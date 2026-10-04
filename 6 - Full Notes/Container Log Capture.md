2026-10-04 08:37

Status: #baby

Tags: [[Podman Container Lifecycle and Storage]]

# Container Log Capture

Container log capture preserves the standard output and standard error streams of the container's main process so they can be retrieved with `podman logs`. [[Conmon]] performs this supervision for Podman and records output even after the initiating CLI command has exited.

Applications designed for containers should direct operational messages to these streams rather than depend only on files inside the ephemeral filesystem. The captured log is valuable for recent process output, but it does not replace external retention, rotation, correlation, or application-specific observability when containers are removed or distributed across hosts.

# References

[[podmanfordevopssecondedition.pdf]]
